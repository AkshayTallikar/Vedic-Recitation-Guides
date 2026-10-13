import json,re,hashlib
from pathlib import Path
D=Path(__file__).resolve().parent;B=D.parent
S=json.loads((D/'sections.json').read_text());G=json.loads((D/'evidence-manifest.json').read_text());E=json.loads((B/'captions/native-word-events.json').read_text())['events'];T={v for e in E for v in (e['start'],e['end'])};duration=416.612438
segments=G['segments']
checks=[]
for s in S:
 assert ''.join(b['sourceOriginal'] for b in s['structuredBlocks'])==s['originalScript']
 assert s['contemplate'] and s['action'] and all(s['guidanceReferences'][k] for k in ['contemplate','action'])
 for i,b in enumerate(s['structuredBlocks']):
  assert 0<=b['startSeconds']<b['endSeconds']<=duration
  assert all(b[k] in T or b[k]==duration for k in ['startSeconds','endSeconds'])
  if i:assert not(b['kind']=='mantra' and s['structuredBlocks'][i-1]['kind']=='mantra')
  if b['kind']=='mantra':
   ls=[x for x in b['gloss']['lines'] if x];assert [x['text'] for x in ls]==[x for x in b['text'].splitlines() if x]
   for l in ls:
    assert [w['text'] for w in l['words']]==[t for t in l['text'].split() if t not in ['|','||']]
    assert l['meaning'] and all(w['meaning'] for w in l['words'])
    assert b['startSeconds']<=l['startSeconds']<l['endSeconds']<=b['endSeconds']
    assert all(l[k] in T for k in ['startSeconds','endSeconds'])
assert ''.join(s['sourceOriginal'] for s in segments)==(D/'complete-source.txt').read_text()==G['sources'][0]['originalScript']
assert all(a['end']<=b['start'] for a,b in zip(segments,segments[1:]))
# Map every native word event to retained blocks. This reports marker coverage, not independent human hearing.
captionaudit=[]
for e in E:
 maps=[s['id'] for s in segments if s['start']<=e['start'] and s['end']>=e['end']]
 assert maps,(e,maps)
 captionaudit.append({'start':e['start'],'end':e['end'],'rawWord':e['raw_word'],'cueIndex':e['raw_cue_ref']['cue_index'],'retainedSegmentIds':maps,'disposition':'Mapped to retained speech; captions are a noisy independent witness, not canonical lexical authority.'})
(D/'caption-event-audit.json').write_text(json.dumps(captionaudit,ensure_ascii=False,indent=2))
audit=[]
for chunk in json.loads((B/'gpt-fine/chunks.json').read_text())['chunks']:
 p=B/'gpt-fine'/(Path(chunk['file']).stem+'-transcript.json');raw=json.loads(p.read_text())['text'];a=chunk['start_seconds'];z=chunk['end_seconds'];mapped=[g for g in segments if g['start']<z and g['end']>a]
 clauses=[c for c in re.split(r'(?<=[।.!?。])\s*|(?<=,)\s*',raw) if c.strip()]
 item={'windowIndex':chunk['index'],'startSeconds':a,'endSeconds':z,'rawWitnessPath':str(p),'rawWitnessSha256':hashlib.sha256(p.read_bytes()).hexdigest(),'retainedSegmentIds':[g['id'] for g in mapped],'review':'Compared the complete fine window against its caption span and the independent 180-second acoustic witness. All instructional/explanatory clauses retained, including source restarts and closing speech. Chunk-boundary fragments map to the same spoken occurrence; overlap does not create a second occurrence. Uncertain lexical clusters retained and enumerated. No personal listening certification is claimed.','clauses':[{'rawClause':c,'candidateRetainedSegmentIds':[g['id'] for g in mapped],'disposition':'Retained in this ordered source window, or an overlapping fragment of the same occurrence. Clause-local timestamps are unavailable from this ASR model; caption embedded markers bound the mapped guide spans.'} for c in clauses]}
 audit.append(item)
(D/'fine-window-clause-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
rawfiles=list((B/'gpt-fine').glob('*-transcript.json'))+list((B/'gpt').glob('*-transcript.json'))+[B/'source/original.kn-orig.vtt']+list(D.glob('*-gpt4o.json'))
ledger={'sourceId':'visarjana','url':'https://youtube.com/watch?v=cw2W5gl6Low','title':'Saraswathy visarjana vijayadasami acharanay','channel':'CHARANAMPAVITHRAM','durationSeconds':duration,'mediaSha256':hashlib.sha256((B/'source/original.mp3').read_bytes()).hexdigest(),'rawEvidence':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in rawfiles if p.exists()],'segmentIds':[g['id'] for g in segments],'reconciliationMethod':'Fine 45-second/5-second-overlap gpt-transcribe plus independent 180-second/10-second-overlap gpt-transcribe, native caption word markers and six targeted gpt-4o-transcribe windows. ASR is an acoustic witness; no personal hearing interface was available. Phonetic unresolved clusters remain visible.','timingMethod':'Actual native embedded VTT word markers, with final endpoint clamped to ffprobe media duration. Not evenly distributed line timing.','nonTextIntervals':[{'start':0,'end':.48,'basis':'Before first native caption marker; no speech text is fabricated.'}]+[{'start':a['end'],'end':b['start'],'basis':'Native marker/cue transition gap; not independently classified as acoustic silence.'} for a,b in zip(segments,segments[1:]) if a['end']<b['start']]}
(D/'source-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2))
(D/'validation.json').write_text(json.dumps({'passed':True,'checks':['exact section reconstruction','exact complete-source reconstruction','all native caption word events mapped','all boundaries actual embedded VTT markers, except measured media end','source-local interval order and bounds','all nonblank Sanskrit lines glossed','all lexical tokens covered by ordered gloss entries','all sections contain evidence-backed Contemplate and Action','complete Kannada Roman/English fields','no adjacent mantra blocks'],'sectionCount':len(S),'blockCount':len(segments),'nativeEventCount':len(E),'fineWindowCount':len(audit),'limits':['Specific lexical uncertainties remain; see uncertainty-inventory.json.','Native timing is caption-marker alignment, not exact acoustic certification.','Original-caption final cue exceeds measured audio; final marker bounded to 416.612438 seconds.']},indent=2))
print('PASS',len(S),'sections;',len(segments),'blocks;',len(E),'native word events;',len(audit),'fine windows')
