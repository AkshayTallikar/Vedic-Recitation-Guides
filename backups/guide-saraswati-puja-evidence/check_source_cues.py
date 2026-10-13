"""Check integrated native cue provenance and independent source coverage."""
import json
import re
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parent
SITE=Path('/tmp/vedic-saraswati-guide/site')
data=(SITE/'data17.js').read_text()
guide=json.loads(data[data.index('.push(')+6:data.rindex(');')])
report={'sources':[],'sectionCount':len(guide['sections']),'manualListeningAvailable':False,
        'synchronizationBasis':'Two overlapping gpt-transcribe passes, targeted acoustic checks, native VTT markers and measured source/clip durations; no human listening claim.'}
for source in guide['sources']:
    name=source['id'];duration=source['durationSeconds']
    events=json.loads((ROOT/name/'captions/native-word-events.json').read_text())['events']
    sections=[s for s in guide['sections'] if s['sourceId']==name]
    blocks=[b for s in sections for b in s['structuredBlocks']]
    boundaries=[0,duration]+[min(duration,e[t]) for e in events for t in ['start','end']]
    missing=[];nonlexical=[]
    for e in events:
        if e['start']>=duration:continue
        if re.fullmatch(r'\[.*?\]',e['raw_word'].strip()):
            nonlexical.append(dict(e,status='Nonlexical caption marker retained in this ledger; not fabricated spoken text or independent acoustic classification.'))
            continue
        if not any(b['startSeconds']<min(duration,e['end']) and b['endSeconds']>e['start'] for b in blocks):missing.append(e)
    if missing:raise ValueError(f'{name}: {len(missing)} native speech events not covered')
    gaps=[];prior=0
    for b in blocks:
        a,z=b['startSeconds'],b['endSeconds']
        if a>prior:gaps.append({'start':prior,'end':a,'status':'No native lexical caption event here; unclassified transition, not certified silence.'})
        prior=max(prior,z)
        assert 0<=a<z<=duration,(name,a,z)
        for t in [a,z]:
            assert min(abs(t-x) for x in boundaries)<0.021,(name,'block boundary not native',t)
        for line in b.get('gloss',{}).get('lines',[]):
            if not line:continue
            la,lz=line['startSeconds'],line['endSeconds']
            assert a<=la<lz<=z,(name,'line outside block',line['text'],la,lz,a,z)
            for t in [la,lz]:
                assert min(abs(t-x) for x in boundaries)<0.021,(name,'line boundary not native',line['text'],t)
    if prior<duration:gaps.append({'start':prior,'end':duration,'status':'No native lexical caption event here; recording tail, not certified silence.'})
    for s in sections:
        measured=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(SITE/s['audioFile'])]))
        assert abs(measured-(s['audioEndSeconds']-s['audioStartSeconds']))<=0.09
        assert s['sourceVideo']==source['url']
    report['sources'].append({'sourceId':name,'durationSeconds':duration,'sections':len(sections),'blocks':len(blocks),
        'nativeWordEvents':len(events),'unmappedEvents':0,'unclassifiedCaptionTransitionIntervals':gaps,
        'nonlexicalCaptionEvents':nonlexical,
        'exactCharacterReconstruction':''.join(b['sourceOriginal'] for b in blocks)==(ROOT/name/'reconciled/complete-source.txt').read_text()})
assert all(x['exactCharacterReconstruction'] for x in report['sources'])
(ROOT/'source-cue-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='sources'}))
print(json.dumps([{k:v for k,v in x.items() if k!='unclassifiedCaptionTransitionIntervals'} for x in report['sources']]))
