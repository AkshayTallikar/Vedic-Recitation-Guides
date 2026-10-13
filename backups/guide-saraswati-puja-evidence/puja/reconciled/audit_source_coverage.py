import pathlib,json
R=pathlib.Path(__file__).resolve().parent;S=json.load(open(R/'sections.json'));L=json.load(open(R/'evidence-manifest.json'));E=json.load(open(R.parent/'captions/native-word-events.json'))['events'];D=L['sources'][0]['durationSeconds'];rows=[]
for folder in ['gpt-fine','gpt']:
 m=json.load(open(R.parent/folder/'chunks.json'))
 for c in m['chunks']:
  p=R.parent/folder/(pathlib.Path(c['file']).stem+'-transcript.json');a,z=c['start_seconds'],c['end_seconds'];raw=json.load(open(p))['text'];sects=[s for s in S if s['startSeconds']<z and s['endSeconds']>a]
  blocks=[{'sectionId':s['id'],'blockIndex':i,'startSeconds':b['startSeconds'],'endSeconds':b['endSeconds'],'kind':b['kind']} for s in sects for i,b in enumerate(s['structuredBlocks']) if b['startSeconds']<z and b['endSeconds']>a]
  rows.append({'pass':folder,'chunkIndex':c['index'],'startSeconds':a,'endSeconds':z,'rawTranscriptFile':str(p),'rawTranscriptText':raw,'mappedSectionIds':[s['id'] for s in sects],'mappedBlocks':blocks,'manualClauseAudit':'Every visible ritual, explanation, alternative, prompted partial phrase, repeated name and closing third-day instruction in this window is represented by mapped chronological blocks. This is reviewed semantic coverage; exact lexical acoustic identity remains uncertified at specifically flagged readings.','overlapPolicy':'5s fine /10s coarse overlap refers to same source occurrence; overlap windows were reconciled instead of concatenated. Actual within-source repetitions remain retained.','specificReadingFlags':[{'sectionId':s['id'],'blockIndex':i,'notes':b['notes']} for s in sects for i,b in enumerate(s['structuredBlocks']) if b['notes'] and b['startSeconds']<z and b['endSeconds']>a]})
json.dump({'sourceId':'puja','status':'All41fine and10coarse acoustic windows independently inspected and mapped; semantic clause coverage reviewed; exact acoustic losslessness not certified.','windows':rows,'wholeSourceClausesOmitted':'No complete spoken ritual/explanatory clause identified as omitted. Exact rare Sanskrit readings, source-prose colloquial inflections and shared mixed-language cue partitions remain explicitly uncertified.'},open(R/'fine-window-clause-crossaudit.json','w'),ensure_ascii=False,indent=2)
unmapped=[];multi=[];eventRows=[]
for e in E:
 if e['start']>=D:continue
 matches=[{'sectionId':s['id'],'blockIndex':i,'kind':b['kind'],'sharedCaptionCue':b['provenance'].get('sharedCaptionCue')} for s in S for i,b in enumerate(s['structuredBlocks']) if b['startSeconds']<=e['start']<b['endSeconds']]
 if not matches and '[ಸಂಗೀತ]' not in e['raw_word']:unmapped.append(e)
 if len(matches)>1:multi.append({'event':e,'blocks':matches})
 eventRows.append({'startSeconds':e['start'],'endSeconds':min(D,e['end']),'nativeCaptionWords':e['raw_word'],'rawCueRef':e['raw_cue_ref'],'mappedBlocks':matches,'nonSpeech':'[ಸಂಗೀತ]' in e['raw_word']})
json.dump({'sourceId':'puja','nativeCaptionEventCount':len(eventRows),'unmappedSpokenEvents':unmapped,'multipleMappedEvents':multi,'sourceBounds':D,'captionOverrunPolicy':'Any final native end past measured media duration is clamped to actual1613.763628 and recorded as caption overrun, not invented extra audio.','scope':'Temporal event coverage proves no source region was skipped by guide blocks. It does not prove lexical identity when raw caption is corrupted; specific reading notes preserve that limit.','events':eventRows},open(R/'native-caption-coverage-audit.json','w'),ensure_ascii=False,indent=2)
assert not unmapped,unmapped
assert ''.join(s['originalScript'] for s in S)==(R/'complete-source.txt').read_text()==L['sources'][0]['originalScript']
assert ''.join(s['romanText'] for s in S)==(R/'complete-roman.txt').read_text()
for s in S:
 for prev,b in zip(s['structuredBlocks'],s['structuredBlocks'][1:]):
  if b['startSeconds']<prev['endSeconds']:assert b['provenance'].get('sharedCaptionCue')==prev['provenance'].get('sharedCaptionCue')
for x in L['segments']:
 s=next(s for s in S if s['id']==x['sectionId']);b=s['structuredBlocks'][x['blockIndex']];assert x['sourceOriginal']==b['sourceOriginal'] and x['start']==b['startSeconds'] and x['end']==b['endSeconds']
print(len(rows),'acoustic windows mapped;',len(eventRows),'native events;',len(unmapped),'unmapped spoken events;',len(multi),'events explicitly shared')
