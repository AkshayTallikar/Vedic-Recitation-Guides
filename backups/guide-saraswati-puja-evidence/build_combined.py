#!/usr/bin/env python3
"""Build one source-aware guide, cut padded clips, and record reproducible checks."""
import argparse
import concurrent.futures
import hashlib
import json
from pathlib import Path
import subprocess
from align_line_cues import align

WORK = Path(__file__).resolve().parent
SOURCES = {
    'avahana': {'url':'https://www.youtube.com/watch?v=Cno0ngZM6KU','role':'Avahana and Preparation'},
    'puja': {'url':'https://www.youtube.com/watch?v=hC8efJAiY2c','role':'Saraswati Puja'},
    'visarjana': {'url':'https://www.youtube.com/watch?v=cw2W5gl6Low','role':'Visarjana and Vijayadashami'},
}

def clock(seconds):
    return f'{int(seconds)//60:02}:{int(seconds)%60:02}'

def probe(file):
    return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(file)]))

def portable_paths(value):
    if isinstance(value,dict):return {k:portable_paths(v) for k,v in value.items()}
    if isinstance(value,list):return [portable_paths(v) for v in value]
    if isinstance(value,str):
        if value.startswith(str(WORK)+'/'):return 'backups/guide-saraswati-puja-evidence/'+value[len(str(WORK))+1:]
        if value.startswith('/tmp/vedic-saraswati-guide/'):return value[len('/tmp/vedic-saraswati-guide/'):]
    return value

def cut_audio(item):
    section,site=item
    source=WORK/section['sourceId']/'source/original.mp3'
    path=site/section['audioFile']
    subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss',str(section['audioStartSeconds']),'-i',str(source),'-t',str(round(section['audioEndSeconds']-section['audioStartSeconds'],3)),'-vn','-c:a','libmp3lame','-b:a','64k','-ac','1',str(path)],check=True)
    measured=probe(path)
    expected=section['audioEndSeconds']-section['audioStartSeconds']
    if abs(measured-expected)>0.09: raise RuntimeError(f'Audio duration mismatch {section["id"]}: {measured} vs {expected}')
    return {'id':section['id'],'file':section['audioFile'],'sourceId':section['sourceId'],'sourceStart':section['audioStartSeconds'],'sourceEnd':section['audioEndSeconds'],'expectedDuration':round(expected,3),'measuredDuration':round(measured,3),'encodingToleranceSeconds':0.09,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--site',type=Path,required=True);args=parser.parse_args()
    site=args.site.resolve();(site/'audio17').mkdir(exist_ok=True,parents=True)
    sections=[];sources=[];segments=[];line_checks=[]
    for name,info in SOURCES.items():
        raw=json.loads((WORK/name/'reconciled/sections.json').read_text())
        if isinstance(raw,dict):raw=raw['sections']
        duration=probe(WORK/name/'source/original.mp3')
        events=json.loads((WORK/name/'captions/native-word-events.json').read_text())['events']
        events=[dict(e,text=e['raw_word'],source={'cueIndex':e['raw_cue_ref']['cue_index']}) for e in events]
        original=''.join(s['originalScript'] for s in raw)
        complete=(WORK/name/'reconciled/complete-source.txt').read_text()
        if complete!=original: raise RuntimeError(f'{name} complete source differs from sections')
        sources.append({'id':name,'url':info['url'],'role':info['role'],'durationSeconds':duration,'originalScript':complete,'mediaSha256':hashlib.sha256((WORK/name/'source/original.mp3').read_bytes()).hexdigest()})
        for section in raw:
            s=json.loads(json.dumps(section));s['originalId']=s.get('id');s['id']=f'{len(sections)+1:02}'
            s['originalSlug']=s['slug'];s['slug']=name+'-'+s['slug']
            s['endSeconds']=min(s['endSeconds'],duration)
            for block in s['structuredBlocks']:
                block['endSeconds']=min(block['endSeconds'],duration)
                for line in block.get('gloss',{}).get('lines',[]):
                    if line and 'endSeconds' in line:line['endSeconds']=min(line['endSeconds'],duration)
            s['sourceId']=name;s['sourceVideo']=info['url'];s['source']=info['url']
            s['group']=info['role'];s['start']=clock(s['startSeconds']);s['end']=clock(s['endSeconds'])
            s['audioStartSeconds']=round(max(0,s['startSeconds']-0.25),3)
            s['audioEndSeconds']=min(duration,round(s['endSeconds']+0.25,3))
            s['audioFile']=f'audio17/{s["id"]}-{s["slug"]}.mp3'
            s['audio']=True
            merged=[]
            for block in s['structuredBlocks']:
                block['sourceSegmentIds']=[block.get('segmentId') or block.get('id') or f'{name}-{s["originalId"]}-{len(merged)+1:03}']
                if merged and block['kind']=='mantra' and merged[-1]['kind']=='mantra':
                    previous=merged[-1]
                    previous['sourceOriginal']+=block['sourceOriginal']
                    previous['sourceRoman']=previous.get('sourceRoman',previous['text'])+block.get('sourceRoman',block['text'])
                    previous['text']=previous['text'].rstrip()+'\n\n'+block['text'].lstrip()
                    previous['gloss']['lines']+= [None]+block['gloss']['lines']
                    previous['endSeconds']=block['endSeconds']
                    previous['notes']=' '.join(str(x) for x in [previous.get('notes',''),block.get('notes','')] if x)
                    previous['sourceSegmentIds']+=block['sourceSegmentIds']
                else:merged.append(block)
            s['structuredBlocks']=merged
            for block in merged:
                if block['kind']=='mantra':
                    line_checks += [dict(x,sectionId=s['id'],sourceId=name) for x in align(block,events,duration)]
            s['mantra']='\n\n'.join(b['text'] for b in s['structuredBlocks'] if b['kind']=='mantra')
            if ''.join(b['sourceOriginal'] for b in s['structuredBlocks'])!=s['originalScript']:raise RuntimeError(f'Lossless block mismatch {s["id"]}')
            for bi,b in enumerate(s['structuredBlocks']):
                segment={'id':f'{name}-{s["id"]}-{bi+1:03}','sourceId':name,'start':b.get('startSeconds',s['startSeconds']),'end':b.get('endSeconds',s['endSeconds']),'sourceOriginal':b['sourceOriginal'],'sectionId':s['id'],'blockIndex':bi,'sourceSegmentIds':b['sourceSegmentIds']}
                b['integrationSegmentId']=segment['id']
                if segments and segments[-1]['sourceId']==name and segment['start']<segments[-1]['end']:
                    prior=segments[-1]
                    overlap=[e for e in events if e['start']<=segment['start']+0.02 and e['end']>=prior['end']-0.02]
                    if not overlap:raise RuntimeError(f'Unexplained block overlap {segment["id"]}')
                    shared={'cueIndices':list(dict.fromkeys(e['source']['cueIndex'] for e in overlap)),'start':min(e['start'] for e in overlap),'end':max(e['end'] for e in overlap)}
                    segment['sharedCaptionCue']=shared;prior['sharedCaptionCue']=shared
                segments.append(segment)
            sections.append(s)
    aliases={(seg['sourceId'],alias):seg['id'] for seg in segments for alias in seg['sourceSegmentIds']}
    for s in sections:
        for key in ['guidanceReferences','enrichmentEvidence']:
            for entries in s.get(key,{}).values():
                for ref in entries:
                    if (ref.get('sourceId'),ref.get('segmentId')) in aliases:
                        ref['integrationSegmentId']=aliases[(ref['sourceId'],ref['segmentId'])]
    sections=portable_paths(sections)
    guide={'key':'saraswati-puja','title':'Saraswati Puja','tabLabel':'Complete (51 min)','audioDir':'audio17','renderStructured':True,'hideLosslessReferences':True,'source':SOURCES['puja']['url'],'sourceCredit':'CHARANAM PAVITHRAM (Kongu Dwaitha), three original teaching videos','subtitle':'Avahana, puja, visarjana and Vijayadashami observance with Roman Sanskrit, English meanings and ritual actions','notice':'Each phase keeps its own recording timeline. Recorded dates and timing advice are 2025 examples. Reading notes identify unclear words; Passage buttons replay a shared phrase when individual line timing cannot be resolved.','sources':sources,'sections':sections}
    # The source ledger belongs in the evidence file, not in duplicate page data.
    guide['sources']=[{k:v for k,v in src.items() if k!='originalScript'} for src in sources]
    (site/'data17.js').write_text('// One combined Saraswati guide; raw witnesses are preserved in backups/guide-saraswati-puja-evidence.\n(window.GUIDES = window.GUIDES || []).push('+json.dumps(guide,ensure_ascii=False,indent=2)+');\n')
    evidence={'sources':sources,'segments':segments}
    (WORK/'guide-evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
    (WORK/'line-cue-checks.json').write_text(json.dumps(line_checks,ensure_ascii=False,indent=2)+'\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        checks=list(pool.map(cut_audio,[(s,site) for s in sections]))
    retained={s['audioFile'].split('/')[-1] for s in sections}
    for clip in (site/'audio17').glob('*.mp3'):
        if clip.name not in retained:clip.unlink()
    (WORK/'audio-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
    print(json.dumps({'sections':len(sections),'sources':len(sources),'clips':len(checks),'sourceCharacters':sum(len(src['originalScript']) for src in sources),'site':str(site)}))

if __name__=='__main__':main()
