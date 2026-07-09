#!/usr/bin/env python3
"""Verify rendered audio against the manifest.

Checks every renderable shloka for a wav, and every wav for validity
(readable header, non-empty, expected 24 kHz mono, sane duration).
Run after dropping new wavs into audio/ — it tells you coverage + any bad files.

Also flags STALE audio: a wav whose source markdown was edited (e.g. a typo
fix) after the wav was rendered, meaning the audio no longer matches the
text on the page. Caught by comparing file mtimes.

Usage:
  python3 verify_audio.py          # report only
  python3 verify_audio.py --tidy   # also move wavs for excluded (tts_skip) shlokas to audio/_excluded/,
                                    # and stale wavs (text edited since render) to audio/_stale/
"""
import os, re, sys, json, wave, glob, shutil, contextlib

ROOT = os.path.dirname(os.path.abspath(__file__))
AUDIO = os.path.join(ROOT, 'audio')
EXPECT_RATE = 24000          # vagdhenu output sample rate
MIN_SEC, MAX_SEC = 0.4, 180  # sane duration bounds

def probe(path):
    """Return (ok, info-or-error)."""
    try:
        with contextlib.closing(wave.open(path, 'rb')) as w:
            ch, rate, n = w.getnchannels(), w.getframerate(), w.getnframes()
        if n == 0:
            return False, 'EMPTY (0 frames)'
        dur = n / float(rate) if rate else 0
        warn = []
        if rate != EXPECT_RATE: warn.append(f'rate={rate}≠{EXPECT_RATE}')
        if ch != 1:             warn.append(f'channels={ch}≠1')
        if dur < MIN_SEC:       warn.append(f'short={dur:.2f}s')
        if dur > MAX_SEC:       warn.append(f'long={dur:.1f}s')
        return True, (f'{dur:5.1f}s {rate}Hz {ch}ch' + ('  ⚠ '+', '.join(warn) if warn else ''))
    except wave.Error as e:
        return False, f'CORRUPT ({e})'
    except Exception as e:
        return False, f'ERROR ({e})'

STALE_SLACK_SEC = 5  # tolerate small clock skew between writing md and unzipping audio

def excluded_ids():
    """ids of shlokas marked tts_skip in the source markdown."""
    ids = set()
    for f in glob.glob(os.path.join(ROOT, 'shlokas', '*.md')):
        txt = open(f, encoding='utf-8').read()
        head = txt[3:txt.index('\n---', 3)]
        if re.search(r'^tts_skip:\s*true', head, re.M | re.I):
            m = re.search(r'^id:\s*(\d+)', head, re.M)
            if m: ids.add(int(m.group(1)))
    return ids

def md_mtimes():
    """id -> mtime of its source markdown file."""
    out = {}
    for f in glob.glob(os.path.join(ROOT, 'shlokas', '*.md')):
        b = os.path.basename(f)
        try: out[int(b[:3])] = os.path.getmtime(f)
        except ValueError: pass
    return out

def main():
    tidy = '--tidy' in sys.argv
    manifest = json.load(open(os.path.join(ROOT, 'audio_manifest.json'), encoding='utf-8'))
    want = {e['id']: e['slug'] for e in manifest}          # renderable shlokas

    mtimes = md_mtimes()

    if tidy:
        excl = excluded_ids()
        os.makedirs(os.path.join(AUDIO, '_excluded'), exist_ok=True)
        os.makedirs(os.path.join(AUDIO, '_stale'), exist_ok=True)
        moved, staled = [], []
        for p in glob.glob(os.path.join(AUDIO, '*.wav')):
            b = os.path.basename(p)
            try: rid = int(b[:3])
            except ValueError: continue
            if rid in excl:
                shutil.move(p, os.path.join(AUDIO, '_excluded', b)); moved.append(b)
            elif rid in mtimes and mtimes[rid] > os.path.getmtime(p) + STALE_SLACK_SEC:
                shutil.move(p, os.path.join(AUDIO, '_stale', b)); staled.append(b)
        print(f'--tidy: moved {len(moved)} excluded wav(s) to audio/_excluded/' + (': '+', '.join(moved) if moved else ''))
        print(f'--tidy: moved {len(staled)} stale wav(s) (text edited since render) to audio/_stale/' + (': '+', '.join(staled) if staled else ''))

    wavs = {}
    for p in glob.glob(os.path.join(AUDIO, '*.wav')):
        b = os.path.basename(p)
        try: wavs[int(b[:3])] = p
        except ValueError: pass

    missing, present, bad, warned, stale = [], [], [], [], []
    for rid in sorted(want):
        if rid not in wavs:
            missing.append(rid); continue
        ok, info = probe(wavs[rid])
        if not ok: bad.append((rid, info))
        else:
            present.append(rid)
            if '⚠' in info: warned.append((rid, info))
            if rid in mtimes and mtimes[rid] > os.path.getmtime(wavs[rid]) + STALE_SLACK_SEC:
                stale.append((rid, mtimes[rid] - os.path.getmtime(wavs[rid])))

    extra = sorted(i for i in wavs if i not in want)       # wavs not in manifest (e.g., excluded)

    print(f'Renderable shlokas in manifest : {len(want)}')
    print(f'  ✅ valid wav present          : {len(present)}')
    print(f'  ❌ missing (need render)       : {len(missing)}')
    print(f'  ⚠  present but flagged         : {len(warned)}')
    print(f'  💥 corrupt/empty              : {len(bad)}')
    print(f'  🕐 STALE (text edited since)  : {len(stale)}' + ('  ← run --tidy to relocate' if stale and not tidy else ''))
    print(f'  ℹ  wavs outside manifest      : {len(extra)} {extra if extra else ""}')
    if missing:
        print('\nMISSING ids (to render):')
        print(' ', ', '.join(f'{i:03d}' for i in missing))
    if warned:
        print('\nFLAGGED (present, but check):')
        for i, info in warned: print(f'  {i:03d} {want[i]}: {info}')
    if bad:
        print('\nCORRUPT/EMPTY (re-render these):')
        for i, info in bad: print(f'  {i:03d} {want[i]}: {info}')
    if stale:
        print('\nSTALE — source text was edited after this audio was rendered (re-render these):')
        for i, delta in stale: print(f'  {i:03d} {want[i]}: text is {delta/3600:.1f}h newer than audio')
    if not missing and not bad and not stale:
        print('\n🎉 Every renderable shloka has a valid, up-to-date wav.')

if __name__ == '__main__':
    main()
