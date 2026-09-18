#!/usr/bin/env python3
"""Render synthetic practice audio with the official Vāgdhenu production renderer.

Run in the notebook's isolated TTS environment. Text is read from reviewed
data15.js, never replaced by ASR. Outputs are drafts pending pronunciation QA.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import urllib.request

from indic_transliteration import sanscript
import numpy as np
import soundfile as sf


def source_guide(source):
    if source.startswith('https://'):
        with urllib.request.urlopen(source) as response:
            raw = response.read().decode('utf-8')
    else:
        raw = Path(source).read_text(encoding='utf-8')
    return json.loads(raw.split('.push(', 1)[1].rsplit(');', 1)[0])


def prepare(section):
    roman = section['originalScript']
    normalized = roman.replace('...', ',').replace(':', ',')
    # A practice recording reads both printed weekday alternatives separately.
    # It is not a date-specific sankalpa; choose the actual weekday when worshipping.
    normalized = normalized.replace('budha/bṛhaspati-vāsare', 'budha-vāsare, bṛhaspati-vāsare')
    normalized = normalized.replace('-', '')
    normalized = re.sub(r'\|\|\s*\d+\s*\|\|', '||', normalized)
    lines = [line.strip() for line in normalized.splitlines() if line.strip()]
    units = []
    verse = []
    def add(meter, texts):
        padas = []
        for text in texts:
            text = re.sub(r'[|\d]+', '', text).strip()
            if text:
                padas.append(sanscript.transliterate(text, sanscript.IAST, sanscript.DEVANAGARI))
        if padas:
            if units and units[-1]['meter'] == meter:
                units[-1]['padas'].extend(padas)
            else:
                units.append({'meter': meter, 'padas': padas})
    if section['id'] == '02':
        # Keep long prose below the model's chunk-duration limit.
        fragments = re.split(r'[,|]', ' '.join(lines))
        for text in fragments:
            words = text.split()
            while words:
                add('gadya', [' '.join(words[:10])])
                words = words[10:]
    else:
        for line in lines:
            if line.startswith(('oṃ ', 'jyeṣṭhādevyai ', 'jyeṣṭhālakṣmyai ')) or section['id'] in ('04', '05', '21', '22', '23') or 'samarpayāmi' in line or len(line.split()) < 4:
                if verse:
                    add('anuṣṭubh', verse)
                    verse = []
                add('gadya', [line])
            elif (section['id'] == '32' and line.startswith('anena ')) or (section['id'] == '06' and line.startswith(('saśrīkaṃ ', 'āgacchāgaccha '))):
                if verse:
                    add('anuṣṭubh', verse)
                    verse = []
                add('gadya', [line])
            else:
                verse.append(line)
                if '||' in line:
                    add('anuṣṭubh', verse)
                    verse = []
        if verse:
            add('gadya' if section['id'] == '06' else 'anuṣṭubh', verse)
    return {'id': section['id'], 'title': section['title'], 'originalScript': roman,
            'textSha256': hashlib.sha256(roman.encode()).hexdigest(), 'units': units}


def render(args):
    guide = source_guide(args.source)
    records = [prepare(s) for s in guide['sections'] if s['originalScript']]
    assert len(records) == 30
    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    units_dir = output / 'units'
    units_dir.mkdir(exist_ok=True)
    previous_path = output / 'manifest.json'
    if previous_path.exists():
        previous = {r['id']: r for r in json.loads(previous_path.read_text(encoding='utf-8'))}
        for record in records:
            assert previous[record['id']]['textSha256'] == record['textSha256'], 'Source text changed; use a fresh output directory.'
    for record in records:
        combined = output / f"jyeshtha-{record['id']}.wav"
        if combined.exists():
            info = sf.info(combined)
            assert info.samplerate == 24000 and info.channels == 1
            record['duration'] = info.duration
    previous_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
    repo = Path(args.repo).resolve()
    env = dict(os.environ, MPLBACKEND='Agg', PYTHONPATH=str(repo / 'BigVGAN') + os.pathsep + os.environ.get('PYTHONPATH', ''))
    selected = [r for r in records if not args.only or r['id'] in args.only.split(',')]
    failed = []
    for record in selected:
        waves = []
        for index, unit in enumerate(record['units'], 1):
            stem = f"jyeshtha-{record['id']}-{index:02d}"
            target = units_dir / (stem + '.wav')
            text = units_dir / (stem + '.json')
            text.write_text(json.dumps(unit['padas'], ensure_ascii=False), encoding='utf-8')
            if not target.exists():
                print(f"RENDER {stem}: {unit['meter']}", flush=True)
                cmd = [sys.executable, 'src/render_production.py', '--padas', str(text),
                       '--meter', unit['meter'], '--voice', str(repo / 'models/voice_steer_ema_2026-06-17.pt'),
                       '--voc', str(repo / 'models/voc_bigvgan_EMA_2026-06-11.pth'),
                       '--bank', str(repo / 'src/reference_bank/bank.json'), '--out', str(target)]
                with (units_dir / (stem + '.log')).open('w', encoding='utf-8') as log:
                    result = subprocess.run(cmd, cwd=repo, env=env, stdout=log, stderr=subprocess.STDOUT)
                if result.returncode or not target.exists():
                    print('FAILED', stem, (units_dir / (stem + '.log')).read_text()[-3000:], flush=True)
                    failed.append(stem)
                    break
            wave, rate = sf.read(target, dtype='float32')
            assert rate == 24000 and wave.ndim == 1 and len(wave) > rate * 0.3
            assert np.isfinite(wave).all() and np.sqrt(np.mean(wave ** 2)) > 0.002
            waves.extend([wave, np.zeros(int(rate * 0.65), dtype=np.float32)])
        else:
            combined = np.concatenate(waves[:-1])
            target = output / f"jyeshtha-{record['id']}.wav"
            sf.write(target, combined, 24000)
            record['duration'] = len(combined) / 24000
            (output / 'manifest.json').write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
            print(f"CARD COMPLETE {record['id']}: {record['duration']:.2f}s", flush=True)
    (output / 'manifest.json').write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
    if failed:
        raise RuntimeError('Failed units: ' + ', '.join(failed))
    print('BATCH COMPLETE', len(selected), 'cards', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--source', default='https://raw.githubusercontent.com/AkshayTallikar/Vedic-Recitation-Guides/main/site/data15.js')
    parser.add_argument('--only', help='Comma-separated card IDs, e.g. 07')
    render(parser.parse_args())
