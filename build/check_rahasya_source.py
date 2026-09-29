#!/usr/bin/env python3
"""Structural audit for the matched 2010 Pooja Rahasya transcription."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
source = json.loads((ROOT / "source/pooja-rahasya-2010.json").read_text(encoding="utf-8"))
entries = json.loads((ROOT / "source/pooja-rahasya-map.json").read_text(encoding="utf-8"))["entries"]
passages = source["passages"]
by_id = {p["id"]: p for p in passages}
problems: list[str] = []

if len(by_id) != len(passages):
    problems.append("Duplicate passage IDs")
if set(entries) != {f"{n:02d}" for n in range(1, 48)}:
    problems.append("Guide map does not cover exactly steps 01–47")
for passage in passages:
    if not passage.get("text", "").strip() and not passage.get("pageImageNotes"):
        problems.append(f"{passage['id']}: empty passage")
    if not source["source"]["pdfPages"]["start"] <= int(passage["pdfPage"]) <= source["source"]["pdfPages"]["end"]:
        problems.append(f"{passage['id']}: outside Rahasya PDF pages")
    if not passage.get("printedPage"):
        problems.append(f"{passage['id']}: printed page number missing")
    if "transcriptionStatus" not in passage:
        problems.append(f"{passage['id']}: no verification status")
for step, entry in entries.items():
    refs = entry.get("passageIds", [])
    if entry.get("matchStatus") == "no_direct_match" and refs:
        problems.append(f"{step}: no-direct entry has source links")
    if entry.get("matchStatus") != "no_direct_match" and not refs:
        problems.append(f"{step}: matched entry has no source links")
    for pid in refs:
        if pid not in by_id:
            problems.append(f"{step}: missing source passage {pid}")
        elif step not in by_id[pid].get("guideIds", []):
            problems.append(f"{step}: reverse link missing from {pid}")
for passage in passages:
    for step in passage.get("guideIds", []):
        if step not in entries or passage["id"] not in entries[step].get("passageIds", []):
            problems.append(f"{passage['id']}: stale reverse link to {step}")

if problems:
    raise SystemExit("\n".join(problems))
print(f"47 steps checked; {len(passages)} source passages; {len({p['pdfPage'] for p in passages})} PDF spreads")
