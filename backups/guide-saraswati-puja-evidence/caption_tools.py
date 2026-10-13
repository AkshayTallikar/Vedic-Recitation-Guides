#!/usr/bin/env python3
"""Build loss-aware inspection aids from Saraswati Puja native YouTube VTTs."""

from __future__ import annotations

import html
import json
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SECTIONS = ("avahana", "puja", "visarjana")
TIMING = re.compile(r"^(\S+)\s+-->\s+(\S+)")
INLINE = re.compile(r"<(?P<time>\d{2}:\d{2}:\d{2}\.\d{3})>")
TAGS = re.compile(r"</?[^>]+>")
MUSIC = re.compile(r"ಸಂಗೀತ|\[music\]|\bmusic\b", re.IGNORECASE)


def seconds(value: str) -> float:
    h, m, s = value.replace(",", ".").split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def stamp(value: float) -> str:
    ms_total = round(value * 1000)
    h, rem = divmod(ms_total, 3_600_000)
    m, rem = divmod(rem, 60_000)
    s, ms = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(TAGS.sub("", value))).strip()


def parse_vtt(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    cues = []
    i = 0
    while i < len(lines):
        match = TIMING.match(lines[i].strip())
        if not match:
            i += 1
            continue
        start, end = map(seconds, match.groups())
        i += 1
        body = []
        while i < len(lines) and not TIMING.match(lines[i].strip()):
            if lines[i].strip() and lines[i].strip() != "WEBVTT":
                body.append(lines[i])
            i += 1
        fresh = next((line.strip() for line in reversed(body) if line.strip()), "")
        cues.append({"cue_index": len(cues) + 1, "start": start, "end": end,
                     "raw_lines": body, "fresh_line": fresh, "text": clean(fresh)})
    return cues


def cue_timeline(cues: list[dict]) -> tuple[list[dict], int]:
    """Use each cue's final fresh line; collapse exact timestamp duplicates only."""
    result = []
    seen = set()
    collapsed = 0
    for cue in cues:
        key = (cue["start"], cue["end"], cue["fresh_line"])
        if key in seen:
            collapsed += 1
            continue
        seen.add(key)
        result.append({"cue_index": cue["cue_index"], "start": cue["start"],
                       "end": cue["end"], "start_time": stamp(cue["start"]),
                       "end_time": stamp(cue["end"]), "text": cue["text"],
                       "short_redisplay_candidate": cue["end"] - cue["start"] <= 0.03})
    return result, collapsed


def chunks_for_cue(cue: dict) -> list[dict]:
    """Extract timing-marker phrases from the fresh line; never split phrases."""
    line = cue["fresh_line"]
    matches = list(INLINE.finditer(line))
    chunks = []
    if not matches:
        text = clean(line)
        if text:
            chunks.append({"start": cue["start"], "text": text})
    else:
        prefix = clean(line[:matches[0].start()])
        if prefix:
            chunks.append({"start": cue["start"], "text": prefix})
        for n, match in enumerate(matches):
            next_start = matches[n + 1].start() if n + 1 < len(matches) else len(line)
            text = clean(line[match.end():next_start])
            if text:
                chunks.append({"start": seconds(match.group("time")), "text": text})
    events = []
    for n, chunk in enumerate(chunks):
        raw_start = chunk["start"]
        raw_end = chunks[n + 1]["start"] if n + 1 < len(chunks) else cue["end"]
        start = max(cue["start"], min(raw_start, cue["end"]))
        end = max(start, min(raw_end, cue["end"]))
        if end > start:
            events.append({"start": start, "end": end, "raw_word": chunk["text"]})
    return events


def audio_duration(source: Path) -> tuple[float | None, str | None]:
    probe = shutil.which("ffprobe") or ("/opt/homebrew/bin/ffprobe" if Path("/opt/homebrew/bin/ffprobe").exists() else None)
    if not probe:
        return None, None
    for name in ("original.mp3", "original.webm"):
        media = source / name
        if not media.exists():
            continue
        proc = subprocess.run([probe, "-v", "error", "-show_entries", "format=duration",
                               "-of", "default=noprint_wrappers=1:nokey=1", str(media)],
                              capture_output=True, text=True, check=False)
        try:
            return float(proc.stdout.strip()), name
        except ValueError:
            continue
    return None, None


def make_events(cues: list[dict], duration: float) -> tuple[list[dict], int, int]:
    events = []
    short_count = 0
    collapsed = 0
    seen = set()
    for cue in cues:
        if cue["end"] - cue["start"] <= 0.03:
            short_count += 1
            continue
        for piece in chunks_for_cue(cue):
            raw_start, raw_end = piece["start"], piece["end"]
            start = max(0.0, min(raw_start, duration))
            end = max(start, min(raw_end, duration))
            if end <= start:
                continue
            # Collapse only exact timestamp/text duplicates; repeated speech at
            # any different timestamp remains a separate event.
            key = (start, end, piece["raw_word"])
            if key in seen:
                collapsed += 1
                continue
            seen.add(key)
            event = {"start": round(start, 3), "end": round(end, 3),
                     "start_time": stamp(start), "end_time": stamp(end),
                     "raw_cue_ref": {"source_file": "original.kn-orig.vtt",
                                      "cue_index": cue["cue_index"],
                                      "start_time": stamp(cue["start"]),
                                      "end_time": stamp(cue["end"])},
                     "raw_word": piece["raw_word"]}
            if raw_start > duration or raw_end > duration:
                event["note"] = "Event exceeded source duration; bounds clamped."
            events.append(event)
    return events, short_count, collapsed


def analyze_gaps(timeline: list[dict], duration: float, threshold: float = 5.0) -> list[dict]:
    covered = [c for c in timeline if c["text"] and not c["short_redisplay_candidate"]]
    gaps = []
    for left, right in zip(covered, covered[1:]):
        delta = right["start"] - left["end"]
        if delta > threshold:
            gaps.append({"start": left["end"], "end": right["start"],
                         "start_time": stamp(left["end"]), "end_time": stamp(right["start"]),
                         "gap_seconds": round(delta, 3), "type": "suspected_caption_gap",
                         "context_before": left["text"], "context_after": right["text"]})
    if covered and duration - covered[-1]["end"] > threshold:
        gaps.append({"start": covered[-1]["end"], "end": duration,
                     "start_time": stamp(covered[-1]["end"]), "end_time": stamp(duration),
                     "gap_seconds": round(duration - covered[-1]["end"], 3),
                     "type": "suspected_caption_gap_at_end", "context_before": covered[-1]["text"]})
    return gaps


def main() -> None:
    for section in SECTIONS:
        source = ROOT / section / "source"
        output = ROOT / section / "captions"
        output.mkdir(parents=True, exist_ok=True)
        vtt = source / "original.kn-orig.vtt"
        metadata = json.loads((source / "youtube-metadata.json").read_text(encoding="utf-8"))
        provisional_duration = float(metadata["duration"])
        probed_duration, media_name = audio_duration(source)
        duration = probed_duration if probed_duration is not None else provisional_duration
        duration_basis = f"ffprobe:{media_name}" if media_name else "youtube-metadata (provisional; audio not downloaded)"
        cues = parse_vtt(vtt)
        timeline, cue_collapsed = cue_timeline(cues)
        events, short_count, event_collapsed = make_events(cues, duration)

        (output / "native-cues.json").write_text(json.dumps([
            {"cue_index": c["cue_index"], "start": c["start"], "end": c["end"],
             "start_time": stamp(c["start"]), "end_time": stamp(c["end"]),
             "raw_lines": c["raw_lines"], "fresh_line": c["fresh_line"], "text": c["text"]}
            for c in cues], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (output / "inspection-timeline.json").write_text(json.dumps(timeline, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (output / "inspection-timeline.txt").write_text("\n".join(
            f"[{c['start_time']}–{c['end_time']}]" + (" [short redisplay candidate]" if c["short_redisplay_candidate"] else "") + f" {c['text']}"
            for c in timeline) + "\n", encoding="utf-8")

        overruns = []
        for cue in cues:
            if cue["end"] > duration:
                overruns.append({"cue_index": cue["cue_index"], "start_time": stamp(cue["start"]),
                                 "end_time": stamp(cue["end"]), "overrun_seconds": round(cue["end"] - duration, 3),
                                 "text": cue["text"]})
        music = [{"cue_index": c["cue_index"], "start_time": stamp(c["start"]),
                  "end_time": stamp(c["end"]), "text": c["text"],
                  "short_redisplay_candidate": c["end"] - c["start"] <= 0.03}
                 for c in cues if MUSIC.search(c["text"])]
        gaps = analyze_gaps(timeline, duration)
        event_overruns = sum("note" in e for e in events)
        events_payload = {"source_file": vtt.name, "source_duration_seconds": duration,
                          "duration_basis": duration_basis,
                          "timing_method": "Embedded VTT markers; phrase chunks between markers share one interval.",
                          "cue_selection": "Final nonempty line per cue; events from cues longer than 0.03s.",
                          "event_count": len(events), "skipped_short_cue_count": short_count,
                          "collapsed_exact_event_duplicates": event_collapsed, "events": events}
        (output / "native-word-events.json").write_text(json.dumps(events_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        report = {"section": section, "source_file": vtt.name, "cue_count": len(cues),
                  "inspection_timeline_count": len(timeline), "collapsed_exact_timestamp_cues": cue_collapsed,
                  "source_duration_seconds": duration, "duration_basis": duration_basis,
                  "metadata_duration_seconds": provisional_duration,
                  "first_cue": stamp(cues[0]["start"]) if cues else None,
                  "last_cue_end": stamp(cues[-1]["end"]) if cues else None,
                  "caption_end_overruns": overruns, "caption_end_overrun_count": len(overruns),
                  "native_event_count": len(events), "skipped_short_cue_count": short_count,
                  "native_event_end_overrun_count": event_overruns,
                  "music_cues": music, "suspected_caption_gaps_over_5s": gaps,
                  "note": "Timeline is an inspection aid; raw VTT and full raw cue lines are preserved. Gap/music flags require listening review and are not language or ritual judgments."}
        (output / "coverage-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{section}: {len(cues)} raw cues, {len(timeline)} inspection cues, {len(events)} native events; "
              f"duration {duration:.3f}s ({duration_basis}); overrun cues {len(overruns)}, music {len(music)}, suspected gaps {len(gaps)}")


if __name__ == "__main__":
    main()
