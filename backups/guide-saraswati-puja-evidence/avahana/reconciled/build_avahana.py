from pathlib import Path
import re,json,html,hashlib,shutil
ROOT=Path(__file__).resolve().parent;BASE=ROOT.parent;URL='https://www.youtube.com/watch?v=Cno0ngZM6KU';DURATION=1035.633208
vowels=dict(zip('ಅಆಇಈಉಊಋೠಎಏಐಒಓಔ',['a','ā','i','ī','u','ū','ṛ','ṝ','e','ē','ai','o','ō','au']))
signs=dict(zip('ಾ಼ಿೀುೂೃೄೆೇೈೊೋೌ',['ā','','i','ī','u','ū','ṛ','ṝ','e','ē','ai','o','ō','au']))
cons=dict(zip('ಕಖಗಘಙಚಛಜಝಞಟಠಡಢಣತಥದಧನಪಫಬಭಮಯರಲವಶಷಸಹಳ',['k','kh','g','gh','ṅ','c','ch','j','jh','ñ','ṭ','ṭh','ḍ','ḍh','ṇ','t','th','d','dh','n','p','ph','b','bh','m','y','r','l','v','ś','ṣ','s','h','ḷ']))
other={'ಂ':'ṁ','ಃ':'ḥ','್':'','ಽ':"'",'೦':'0','೧':'1','೨':'2','೩':'3','೪':'4','೫':'5','೬':'6','೭':'7','೮':'8','೯':'9'}
def roman(text):
 out='';i=0
 while i<len(text):
  c=text[i]
  if c in cons:
   out+=cons[c]
   if i+1<len(text) and text[i+1] in signs:out+=signs[text[i+1]];i+=1
   elif i+1<len(text) and text[i+1]=='್':i+=1
   else:out+='a'
  else:out+=vowels.get(c,signs.get(c,other.get(c,c)))
  i+=1
 return out

def write(name,obj):(ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def secs(t):h,m,s=t.split(':');return round(int(h)*3600+int(m)*60+float(s),3)
def clean(t):return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>','',t))).strip()
raw=(BASE/'source/original.kn-orig.vtt').read_text();shutil.copy2(BASE/'source/original.kn-orig.vtt',ROOT/'original.kn-orig.vtt')
cuepat=re.compile(r'(\d\d:\d\d:\d\d\.\d+) --> (\d\d:\d\d:\d\d\.\d+)[^\n]*\n(.*?)(?=\n\n|\Z)',re.S)
rawcues=[];tokens=[];seen=set()
for i,m in enumerate(cuepat.finditer(raw)):
 a,z=secs(m[1]),secs(m[2]);body=m[3];rawcues.append({'id':f'avahana-cue-{i:04d}','startSeconds':a,'endSeconds':z,'rawBody':body,'text':clean(body)})
 lines=[x.strip() for x in body.splitlines() if x.strip()]
 if z-a<.05:continue
 marked=[x for x in lines if re.search(r'<\d\d:\d\d:',x)]
 fresh=marked[-1] if marked else (lines[-1] if lines else '')
 chunks=re.split(r'<(\d\d:\d\d:\d\d\.\d+)>',fresh)
 spans=[];time=a
 for j in range(0,len(chunks),2):
  text=clean(chunks[j])
  end=secs(chunks[j+1]) if j+1<len(chunks) else z
  if text:spans.append((time,end,text))
  if j+1<len(chunks):time=end
 for ta,tz,text in spans:
  key=(ta,text)
  if key in seen:continue
  seen.add(key);tokens.append({'id':f'avahana-word-{len(tokens):04d}','sourceId':'avahana','startSeconds':ta,'endSeconds':tz,'sourceOriginal':text+' ','sourceRoman':roman(text)+' ','cueId':f'avahana-cue-{i:04d}','timingBasis':'native VTT inline word marker; first word uses the fresh caption line cue onset','rawCaptionText':text})
write('raw-caption-cues.json',rawcues);write('native-word-markers.json',tokens)
(ROOT/'caption-readable.txt').write_text('\n'.join(f"{r['startSeconds']:08.3f} {r['sourceOriginal']}" for r in tokens),encoding='utf-8')
# Per-minute view helps inspect all speech without loading rolling duplicates.
for minute in range(18):
 selected=[t for t in tokens if minute*60<=t['startSeconds']<(minute+1)*60]
 if selected:print(str(minute)+': '+' '.join(x['sourceOriginal'].strip() for x in selected))
# Speech roles use native word markers at actual language transitions.
ACTION={
1.839:('Welcome','To the dear viewers of the Charanam Pavithram YouTube channel, greetings.'),
6.72:('Saraswati worship','Worship of Saraswati. In the worship of Saraswati, it has been said:'),
19.68:('The four nakshatra days','Thus it has been stated. On Mula nakshatra day, invoke Saraswati and perform the installation. On the following Purvashadha nakshatra day, perform the worship. On Uttarashadha nakshatra day, give bali, the offering. Perform the conclusion on Shravana, on the Shravana Vijayadashami day. This is the Navaratri sequence. The coming Mula nakshatra means Monday, the 29th, for the installation and worship of Saraswati. [These are the recording’s 29 September 2025 examples, not dates prescribed for the present year.]'),
65.12:('Books and shrine preparation','In the morning, finish all your daily obligatory practices and complete the worship of the deity. On a plank or in a pavilion, prepare the setting [the native-caption wording about rangoli/red earth is unclear]. Arrange and decorate the books—the scriptural books that you have—on that plank. Decorate with the stated cloth, flowers and adornment [the exact cloth-name phrase requires an acoustic witness]. A Saraswati image or a Saraswati picture is suitable. Place a picture of Vedavyasa in front and perform the worship. Place it in front and perform the worship. For the worship, prepare turmeric, kumkuma, gandha and mantrakshata.'),
120.0:('Offerings and vessels','Then, for the offering, betel leaves and areca nut, fruit, the stated cloth adornment, incense sticks, camphor, coconut, the arati plate, panchapatra and uddharani. Two panchapatras: one for the deity and one for you. Put water in them; have the bowl and flowers and all these articles ready and sit for the worship. The first day, under Mula nakshatra, is invocation only. Sit facing north, north-facing; otherwise sit facing east and perform achamana.'),
183.76:('Pranayama instruction','Pranayama: hold the nose.'),
208.159:('Preparing for sankalpa','Put a little mantrakshata in the left hand, place the right hand over the left hand and rest them on the right thigh.'),
275.759:('Beginning the invocations','Saying this, pour out the water and release it. After releasing it, have the lamp lighted [caption word needs acoustic review]. Take mantrakshata in the hand. Take mantrakshata in the hand and meditate. First invoke Kapila and Dattatreya. Kapila, Dattatreya.'),
346.479:('Hayagriva instruction','Second, meditate on Hayagriva. Hold mantrakshata in the hand.'),
381.6:('Rama instruction','Meditate on Rama. Take mantrakshata in the hand.'),
400.639:('Rama offering cue','Mantrakshata [a short spoken cue between the salutation and invocation].'),
403.84:('Krishna instruction','Again take mantrakshata.'),
421.199:('Parashurama instruction','Again take mantrakshata [native captions read hattu, “ten”; this phrase requires comparison with the acoustic witness].'),
441.199:('Narasimha instruction','Again take mantrakshata.'),
468.56:('Vyasa instruction','Next, Vyasa meditation. Mantrakshata.'),
498.479:('Narayana instruction','Again, mantrakshata.'),
541.68:('Lakshmi instruction','Shri meditation: meditate on Lakshmi. Mantrakshata.'),
562.399:('Bhu instruction','Again, mantrakshata.'),
584.48:('Durga instruction','Again, mantrakshata.'),
604.56:('Mukhyaprana instruction','Again take mantrakshata.'),
630.48:('Saraswati instruction','Again take mantrakshata and meditate on Saraswati. Saraswati meditation.'),
720.0:('Books invocation instruction','Take mantrakshata.'),
759.04:('Offering flowers','Saying this, place the mantrakshata and offer pushpanjali, the handful of flowers.'),
766.399:('Associated invocations instruction','Again take mantrakshata.'),
839.76:('Installation instruction','Saying this, place the flowers in it. Keep mantrakshata in the hand.'),
895.04:('Prayer instruction','Saying this, place the mantrakshata and again take flowers and mantrakshata.'),
940.399:('Touching the books','Saying this, place flowers and mantrakshata. Touch the books and say:'),
945.199:('Eight repetitions and flower worship','Say this eight times. After saying it, perform archana with flowers.'),
962.48:('Hymns and offerings','Saying this, place the flowers and mantrakshata. If you know any suktas, you may recite them. If you do not know suktas, recite a stotra of the deity and offer pushpanjali. Offer betel leaves, areca nut and coconut as naivedya [the short connective around “coconut” is unclear]. Having offered naivedya, perform mangalarati and finish. Perform mangalarati in the hand [the wording needs an acoustic check]. After doing that, hold mantrakshata in the right hand and pour two uddharanis of water into it.'),
1017.279:('Releasing the dedication','Saying this, release it into the bowl.'),
1020.8:('Evening worship and next lesson','Thus: in the evening perform panchopachara worship, with turmeric and kumkuma. Likewise offer betel leaves, areca nut and fruit as naivedya in the evening. Next, let us watch the Saraswati worship video. Thank you.')}
ACTION[62.32]=ACTION.pop(65.12);ACTION[123.92]=ACTION.pop(120.0);ACTION[720.88]=ACTION.pop(720.0)
MANTRA_STARTS=[.56,10.559,159.84,186.319,214.959,308.56,351.039,385.12,401.68,405.44,422.72,443.759,473.84,500.24,545.2,563.6,585.839,607.2,640.24,720.0,722.0,763.92,767.68,847.36,898.88,943.519,949.6,1005.12,1019.519]
starts=sorted([(x,'mantra') for x in MANTRA_STARTS]+[(x,'action') for x in ACTION])
roles=[]
for i,(a,kind) in enumerate(starts):
 z=starts[i+1][0] if i+1<len(starts) else DURATION
 selected=[t for t in tokens if a<=t['startSeconds']<z]
 if not selected:continue
 title,english=ACTION.get(a,('Recorded recitation',''))
 roles.append({'id':f'avahana-block-{i:03d}','kind':kind,'startSeconds':selected[0]['startSeconds'],'endSeconds':min(selected[-1]['endSeconds'],DURATION),'sourceOriginal':''.join(t['sourceOriginal'] for t in selected),'sourceRoman':''.join(t['sourceRoman'] for t in selected),'nativeMarkerIds':[t['id'] for t in selected],'title':title,'english':english,'status':'caption-derived linguistic-role draft; acoustic reconciliation pending'})
write('draft-roles.json',roles)
print('Speech roles drafted: '+str(len(roles))+' blocks, '+str(len(tokens))+' native marker spans.')
SECTION_PLAN=[
(.56,'Welcome and the four nakshatra days'),(62.32,'Preparing the books and deity pictures'),(123.92,'Offerings vessels and seating'),(159.84,'Achamana'),(183.76,'Pranayama'),(208.159,'Sankalpa'),(275.759,'Kapila and Dattatreya'),(346.479,'Hayagriva'),(381.6,'Rama'),(403.84,'Krishna'),(421.199,'Parashurama'),(441.199,'Lakshmi Narasimha'),(468.56,'Vedavyasa'),(498.479,'Narayana'),(541.68,'Lakshmi'),(562.399,'Bhu'),(584.48,'Durga'),(604.56,'Mukhyaprana'),(630.48,'Saraswati and the attendant deities'),(720.0,'Invocation in the scriptural books'),(763.92,'Associated forms sages and teachers'),(839.76,'Establishing the presence'),(895.04,'Prayer for continued presence'),(940.399,'Touching the books and the eight syllable mantra'),(949.6,'Invocation positions and grace'),(962.48,'Hymns offerings and arati'),(1005.12,'Dedication'),(1020.8,'Evening worship and the next lesson')]
write('section-plan.json',[{'id':f'A{i+1:02d}','title':title,'startSeconds':start,'endSeconds':SECTION_PLAN[i+1][0] if i+1<len(SECTION_PLAN) else DURATION,'blockIds':[b['id'] for b in roles if start<=b['startSeconds']<(SECTION_PLAN[i+1][0] if i+1<len(SECTION_PLAN) else DURATION)]} for i,(start,title) in enumerate(SECTION_PLAN)])
# Final acoustic reconciliation: two complete overlapping passes plus independent
# gpt-4o witnesses at the four hardest passages. Raw evidence is never overwritten.
from recitation_edits import DATA
fine_manifest=BASE/'gpt-fine/chunks.json';coarse_manifest=BASE/'gpt/chunks.json'
if not fine_manifest.exists() or not coarse_manifest.exists():raise SystemExit('Acoustic witnesses pending; role draft only.')
fine=json.loads(fine_manifest.read_text())['chunks'];coarse=json.loads(coarse_manifest.read_text())['chunks']
for folder,chunks in [('gpt-fine',fine),('gpt',coarse)]:
 for c in chunks:
  if not (BASE/folder/(Path(c['file']).stem+'-transcript.json')).exists():raise SystemExit('Incomplete acoustic pass: '+folder+'/'+c['file'])
NOTES={
308.56:'The Kapila-Dattatreya verse contains audible restarts around the knowledge/fearlessness and Aja-assembly phrases. Both model passes and an independent targeted model are noisy there; the displayed phonetic joins remain provisional. No omitted continuation is supplied from a text.',
351.039:'The inserted pratihati fragment and the conch/rosary/understanding compound are phonetically variable across acoustic witnesses. The recitation ends after the Brahma/Isha phrase; the unspoken continuation in Tantrasara is not added.',
385.12:'The sun/moon joining phrase sounds ravīndum iti across witnesses. Its exact sandhi and the final great-praise phrase remain provisional.',
405.44:'The gem-comparison opening sounds harirmaṇi across witnesses; the reference text has darinmaṇi. The acoustic reading is retained rather than silently replacing it.',
443.759:'The Narasimha prayer is present in both acoustic passes but its initial words lack separate usable native markers. That line replays the explicitly shared encompassing passage. The recited forms and dhyana compounds have noisy sandhi in the witnesses.',
500.24:'The discus/conch phrase is repeatedly restarted, and the faultless-power phrase repeats. The eight-forms fragment is retained where heard, without adding its reference-text continuation.',
545.2:'The second meditation line is recovered by both acoustic passes despite omission/garbling in the captions. Its passage cue is shared where no separate reliable native lexical match survives.',
563.6:'The Bhu meditation is omitted from the coarse pass but retained by the fine pass and native captions. The blue-flower/betel and boon compound remains a provisional acoustic joining.',
585.839:'The conch/discus/trident compound and middle meditation line are noisy. The repeated discus-lotus wording is retained; exact inflections remain provisional.',
607.2:'The boon/fearlessness hand expression differs across the acoustic passes. The main Prana forms and the repeated invocation remain separately retained.',
640.24:'The meditation begins with a restart and repeats the perception and Self-knowledge phrases. Gauri’s one/two/four/eight/nine-footed sequence is recovered through the acoustic witnesses; some joining syllables remain provisional. The independent targeted model is also noisy, so no canonical pronunciation verification is claimed.',
722.0:'The book-letter/luminous-line/Prana-Shri expression and the all-knowledge/excellence compound are disputed across both passes and the independent targeted model. Mahidasa and the favorable-presence verb are provisional lexical readings. The form and deity lists are fully retained.',
767.68:'The Jaganti, Svayampriti and Gugu/Kuhu-like deity names, and Jayatirtha’s contracted name, remain acoustic-name variants. The Janaki/Satya/Rukmini list restarts and is retained twice.',
847.36:'The establishment passage is noisy in native captions, both full passes and the independent targeted model. The vihā/gṛhā opening, praise-by-speech joining, house/livestock expression and sovereignty-related forms are preserved as specific phonetic readings. Meanings of those clauses are tentative contextual readings, not a supplied canonical edition.',
898.88:'The offerings/arghya phrase is restarted and some endings vary. The image-to-book location correction is retained. Exact introductory gosvāmin wording remains provisional.',
949.6:'The native caption has three distinct presence-related expressions; the coarse pass omits one and the fine pass varies their order. All captioned occurrence slots are retained; the precise middle forms require further lexical review.',
1005.12:'The Mula-nakshatra inflection and the joining between Saraswati, Bharati, Mukhyaprana and Lakshmi-Vedavyasa are provisional acoustic forms. This is the recording’s dedication, not a newly composed formula.'}
# Complete Kannada instructions refined from the two acoustic passes.
ACTION[62.32]=(ACTION[62.32][0],ACTION[62.32][1].replace('[the native-caption wording about rangoli/red earth is unclear]','with rangoli and red earth [rangoḷe/kemmaṇṇu, recovered by both acoustic passes]').replace('[the exact cloth-name phrase requires an acoustic witness]','[gajavastrādi, the recorded cloth-adornment name retained]'))
ACTION[275.759]=(ACTION[275.759][0],ACTION[275.759][1].replace('[caption word needs acoustic review]','[mūḍisittu, the lamp-lighting expression varies slightly in the witnesses]'))
ACTION[421.199]=(ACTION[421.199][0],'Again take mantrakshata. [Both acoustic passes read mattu, “again”; native captions read hattu.]')
ACTION[962.48]=(ACTION[962.48][0],ACTION[962.48][1].replace('[the wording needs an acoustic check]','[the two acoustic passes retain this instruction’s wording; it is not expanded into an unrecorded motion]'))
# Apply only lexical Kannada corrections with paired acoustic support.
kncorrections={'ತೊಂಗಲ':'ರಂಗೋಲೆ','ಕೂದುಕಡ್ಡಿ':'ಊದುಕಡ್ಡಿ','ಹತ್ತು':'ಮತ್ತು','ಮಂತ್ರಾಸ್ತೆಯನ್ನ':'ಮಂತ್ರಾಕ್ಷತೆಯನ್ನ','ಮಂತ್ರಸ್ತೆಯನ್ನ':'ಮಂತ್ರಾಕ್ಷತೆಯನ್ನ','ಮಂತ್ರಸ್ಥೆಯನ್ನ':'ಮಂತ್ರಾಕ್ಷತೆಯನ್ನ','ಮಂತ್ರಾಸ್ತೆಯನ್ನು':'ಮಂತ್ರಾಕ್ಷತೆಯನ್ನು'}
NOTES[214.959]='The recorded ādya probably represents adya, today/now; its vowel remains uncertain. The bhautāvatāre dating-formula cluster is not securely parsed: bauddhāvatāre is a candidate, not a verified replacement or a confident material-incarnation claim. Recorded2025 dating/locality wording is preserved.'
NOTES[500.24]+=' Primary Tantrasara1.20 reads niḥśeṣaśaktimān, possessing complete/all powers. Native markers at527.360 and531.760 and fine window14/coarse window4 instead recognize nirdoṣa/niddhoṣa, faultless. The apparent spoken variant and both repetitions are retained; the primary-text difference is explicit rather than silently corrected.'
NOTES[722.0]+=' The prāṇaśrī cluster does not securely establish two deity names Prana and Shri; that proposed division remains unconfirmed.'
sections=[];segments=[];corrections=[]
for idx,(sa,title) in enumerate(SECTION_PLAN):
 sz=SECTION_PLAN[idx+1][0] if idx+1<len(SECTION_PLAN) else DURATION
 blocks=[];sectionid=f'A{idx+1:02d}'
 for role in [b for b in roles if sa<=b['startSeconds']<sz]:
  start=role['startSeconds'];end=role['endSeconds'];caption=role['sourceOriginal'];bid=f'{sectionid}-block-{len(blocks)+1:02d}'
  evfiles=[f'{folder}/{Path(c["file"]).stem}-transcript.json' for folder,chunks in [('gpt-fine',fine),('gpt',coarse)] for c in chunks if c['start_seconds']<end and c['end_seconds']>start]
  evidence={'sourceId':'avahana','startSeconds':start,'endSeconds':end,'segmentId':bid,'basis':'Native VTT inline marker boundaries; Kannada/Sanskrit wording compared against both overlapping acoustic passes.','files':evfiles,'nativeMarkerIds':role['nativeMarkerIds']}
  common={'kind':role['kind'],'startSeconds':start,'endSeconds':end,'sourceId':'avahana','evidenceReferences':[evidence],'captionOriginal':caption,'timingEvidence':{'basis':'native VTT inline markers','nativeMarkerIds':role['nativeMarkerIds']},'timingStatus':'native-word-marker-boundaries','role':'explanation' if role['kind']=='action' else 'recitation'}
  if role['kind']=='action':
   english=ACTION[start][1]
   source=caption
   for old,new in kncorrections.items():
    if old in source:
     # hattu is corrected only in this short repeated-akshata instruction.
     if old=='ಹತ್ತು' and start!=421.199:continue
     source=source.replace(old,new)
   common.update({'sourceOriginal':source,'sourceRoman':roman(source),'english':english})
   if '[' in english:common['notes']='Specific reading note: '+english[english.find('[')+1:english.find(']')]
  else:
   rows=DATA[start];gloss=[];texts=[]
   for j,(a,text,meaning,lex) in enumerate(rows):
    d=dict(pair.strip().split(':',1) for pair in lex.split(';') if pair.strip());words=[]
    for w in text.split():
     if w not in d:raise RuntimeError(f'Missing specific word gloss: {bid} {w}')
     words.append({'text':w,'meaning':d[w]})
    nexta=rows[j+1][0] if j+1<len(rows) else end
    valid=a in {r['startSeconds'] for r in tokens} and nexta>a
    # Ambiguous recovered lines share their recorded passage; they never get
    # an evenly divided or fabricated duration.
    shared=not valid or (start==443.759 and j==2) or (start in [545.2,563.6,585.839,607.2] and j==1) or start==847.36
    if shared:a,z=start,end
    else:z=min(nexta,end)
    line={'text':text,'meaning':meaning,'words':words,'startSeconds':a,'endSeconds':z,'sourceId':'avahana','timingStatus':'shared-native-passage' if shared else 'native-marker-line-window','timingEvidence':{'basis':'Explicit enclosing native passage where recovered syllables lack independent markers' if shared else 'Native inline marker at matched clause onset, next native clause onset as endpoint','segmentId':bid,'nativeMarkerIds':[r['id'] for r in tokens if a<=r['startSeconds']<z]},'translationEvidence':'Editorial lexical interpretation of acoustic reading; matched Tantrasara passages used only to interpret words, never to append recitation.'}
    if shared:line.update({'sharedPassageCue':True,'sharedCueGroup':bid,'notes':f'Shared recorded passage {a:.3f}–{z:.3f}s; an individual-line acoustic onset is not established.'})
    gloss.append(line);texts.append(text)
   source='\n'.join(texts)+'\n'
   common.update({'sourceOriginal':source,'sourceRoman':source,'text':'\n'.join(texts),'gloss':{'lines':gloss}})
   if start in NOTES:common['notes']=NOTES[start]
  if common['sourceOriginal']!=caption:corrections.append({'segmentId':bid,'captionOriginal':caption,'reconciledReading':common['sourceOriginal'],'reason':'Acoustic-backed recitation edition with restarts and omissions preserved, or paired-witness Kannada lexical correction; raw caption separately retained.','files':evfiles})
  common['id']=bid;blocks.append(common);segments.append({'id':bid,'sourceId':'avahana','start':start,'end':end,'startSeconds':start,'endSeconds':end,'sourceOriginal':common['sourceOriginal'],'sourceRoman':common['sourceRoman'],'sectionId':sectionid,'blockIndex':len(blocks)-1,'captionOriginal':caption,'nativeMarkerIds':role['nativeMarkerIds'],'files':evfiles})
 original=''.join(b['sourceOriginal'] for b in blocks);refs=[{'sourceId':'avahana','startSeconds':b['startSeconds'],'endSeconds':b['endSeconds'],'segmentId':b['id'],'basis':'Guidance derived from this recorded explanation or deity meditation; no unspoken ritual motions added.'} for b in blocks]
 c='Attend to '+title.lower()+' as explained or recited in this recording.'
 a='Follow the recorded instructions in this step and recite the retained invocation where shown.' if any(b['kind']=='action' for b in blocks) else 'Recite the shown passage, including recorded repetitions and restarts.'
 if idx in [0,5]:c+=' The calendar and locality expressions belong to the September2025 recording example.'
 sections.append({'id':sectionid,'slug':re.sub('[^a-z0-9]+','-',title.lower()).strip('-'),'title':title,'group':'Saraswati Avahana','sourceId':'avahana','source':URL,'type':'mantra' if any(b['kind']=='mantra' for b in blocks) else 'context','startSeconds':blocks[0]['startSeconds'],'endSeconds':blocks[-1]['endSeconds'],'originalScript':original,'sourceOriginal':original,'sourceRoman':''.join(b['sourceRoman'] for b in blocks),'structuredBlocks':blocks,'contemplate':c,'action':a,'evidenceReferences':{'contemplate':refs,'action':refs},'guidanceReferences':{'contemplate':refs,'action':refs},'enrichmentEvidence':{'contemplate':refs,'action':refs},'verify':any(b.get('notes') for b in blocks),'verifyNotes':[b['notes'] for b in blocks if b.get('notes')]})
full=''.join(s['originalScript'] for s in sections)
(ROOT/'complete-source.txt').write_text(full,encoding='utf-8');(ROOT/'complete-roman.txt').write_text(''.join(s['sourceRoman'] for s in sections),encoding='utf-8')
write('sections.json',sections);write('correction-log.json',corrections)
ledger={'sources':[{'id':'avahana','url':URL,'title':'Saraswati Avahanam 29-9-2025','durationSeconds':DURATION,'originalScript':full,'originalScriptBasis':'Reconciled spoken edition: full Kannada teaching and Roman Sanskrit acoustic reading. Native captions and all acoustic outputs preserved separately.','rawCaptionSHA256':hashlib.sha256((ROOT/'original.kn-orig.vtt').read_bytes()).hexdigest()}],'segments':segments}
write('source-ledger.json',ledger);write('evidence-manifest.json',ledger)
# Every fine-window output is traceable to source clauses, even where Sanskrit
# lexical reading remains specifically disputed. Mapping is not a blanket proof
# of acoustic accuracy or a claim that the transcription model cannot omit words.
audit=[]
for c in fine:
 f=BASE/'gpt-fine'/(Path(c['file']).stem+'-transcript.json');text=json.loads(f.read_text())['text'];mapped=[b for b in segments if b['start']<c['end_seconds'] and b['end']>c['start_seconds']]
 audit.append({'chunkIndex':c['index'],'startSeconds':c['start_seconds'],'endSeconds':c['end_seconds'],'file':str(f.relative_to(BASE)),'rawGPTText':text,'segmentIds':[b['id'] for b in mapped],'nativeMarkerIds':[t['id'] for t in tokens if c['start_seconds']<=t['startSeconds']<c['end_seconds']],'reviewStatus':'Full window compared to chronological native caption clauses and recitation role edition; variants retained in block notes.'})
write('clause-audit.json',audit)
write('uncertainty-inventory.json',[{'sectionId':s['id'],'notes':s['verifyNotes']} for s in sections if s['verifyNotes']])
checks={'sourceReconstruction':''.join(b['sourceOriginal'] for s in sections for b in s['structuredBlocks'])==full,'sectionReconstruction':all(''.join(b['sourceOriginal'] for b in s['structuredBlocks'])==s['originalScript'] for s in sections),'allFineWindowsMapped':len(audit)==len(fine) and all(a['segmentIds'] for a in audit),'allNativeMarkersRetained':len({x for seg in segments for x in seg['nativeMarkerIds']})==len(tokens),'allBounds':all(0<=b['start']<b['end']<=DURATION for b in segments),'allLexicalGlosses':all([w['text'] for w in line['words']]==line['text'].split() for s in sections for b in s['structuredBlocks'] if b['kind']=='mantra' for line in b['gloss']['lines'] if line)}
if not all(checks.values()):raise RuntimeError(json.dumps(checks))
write('evidence-report.json',{'status':'Complete chronological draft reconciled against both acoustic passes; specifically uncertain Sanskrit variants are visible, shared cue ranges explicitly labelled; no human-listening claim.','sections':len(sections),'blocks':len(segments),'nativeMarkerSpans':len(tokens),'fineWindows':len(fine),'coarseWindows':len(coarse),'independentTargetedClips':4,'checks':checks})
print(json.dumps(checks,indent=2))
GUIDANCE=[
('Remember the recorded order: invocation under Mula, worship under Purvashadha, bali under Uttarashadha and conclusion under Shravana.','Listen to the greeting and four-day sequence; treat the Monday29September date as the recorded2025 example.'),
('The scriptural books are prepared as the place of Saraswati and Vedavyasa worship.','Complete daily observances and deity worship, prepare the plank or pavilion with rangoli/red earth, decorate the books and place Saraswati and Vedavyasa pictures as described.'),
('The first Mula-day phase is invocation; north- or east-facing seating is specified.','Prepare all the named offerings, two water vessels, bowl and flowers; sit facing north or east and begin achamana.'),
('Attend to the retained names of Vishnu in the recorded achamana sequence.','Perform achamana with the recorded names and formulas.'),
('Attend to the invocation of the realms and Savitr’s illumination of understanding.','Hold the nose for pranayama as directed, and recite the displayed application and Gayatri passage.'),
('Understand the declared intention: Vedavyasa’s pleasure and Saraswati-form invocation in the books, within the recorded indwelling hierarchy.','Place mantrakshata in the left hand, cover it with the right and rest on the right thigh; recite the recorded sankalpa, keeping its2025 calendar/locality example distinct from your own details.'),
('Contemplate Kapila and Dattatreya, sun-like and awakening the divine assembly, as described in the retained meditation.','Release the sankalpa water, ready the lamp, take mantrakshata and meditate on and invoke Kapila and Dattatreya in the book.'),
('Contemplate the horse-faced Hayagriva, moon-white, illuminating within and without, and issuing knowledge.','Take mantrakshata, recite the retained Hayagriva meditation and invoke Hayagriva.'),
('Contemplate Rama, dark-hued, bearing the arrow and revealing his nature to Hanuman and the others.','Take mantrakshata, meditate on Rama, and follow the short akshata cue before invoking Rama.'),
('Contemplate Krishna, the essence of beauty, bearing discus and conch with boon and fearlessness, accompanied by Bhaishmi and Satya.','Again take mantrakshata and recite the Krishna meditation and salutation.'),
('Contemplate the ember-colored Parashurama bearing axe and bow, praised by the gods.','Again take mantrakshata and recite the Parashurama meditation and Bhargava salutation.'),
('Contemplate Lakshmi Narasimha with sun-like radiance, discus and conch, and the fierce yet auspicious nature named in the prayer.','Again take mantrakshata and recite the retained meditation, prayer and invocation, using the shared passage replay where marked.'),
('Contemplate emerald-like Vedavyasa, filling the cosmic sphere with knowledge and granting understanding.','Take mantrakshata and recite the Vyasa meditation, seed salutation and Gayatri.'),
('Contemplate Narayana amidst his forms and attendant deities, embraced by Lakshmi and Dhara, possessing enduring faultless power.','Again take mantrakshata and retain the recorded restarts and repeated meditation phrases before invoking Narayana.'),
('Contemplate Mahalakshmi in yellow silk, lotus-eyed, holding lotuses and showing boon and fearlessness.','Take mantrakshata and recite the retained Shri meditation and salutation.'),
('Contemplate Bhu with the yellow-silk, dark-radiant form and stated offerings and gestures.','Again take mantrakshata and retain the repeated Bhu salutation in the meditation.'),
('Contemplate Durga in red silk with three lotus-like eyes and the stated weapons and gestures.','Again take mantrakshata and recite the Durga meditation with its recorded restart.'),
('Contemplate Mukhyaprana at Acyuta’s feet, engaged in praise, with exalted power of action.','Again take mantrakshata; meditate on and invoke Mukhyaprana, preserving the second invocation.'),
('Contemplate Saraswati as Self-knowledge, radiantly seated, holding the teaching gesture and book; attend to the following Bharati, Shesha, Shiva, Gauri and Vinayaka invocations.','Take mantrakshata and recite all the retained meditation and attendant-deity invocations, including repetitions.'),
('Attend to the recorded presence of the named divine forms within the scriptural book’s written lines.','Take mantrakshata, recite the full book-invocation formula, and offer mantrakshata and pushpanjali as directed.'),
('Attend to Rama/Lakshmi’s named forms, the sages, sūkta deities and the commentary teachers invoked in the book’s presence.','Again take mantrakshata and recite the complete associated list, including its restarted names, before offering flowers.'),
('Attend to the establishment passage’s theme of support and presence; its specifically disputed phonetic clauses remain visible.','Place the flowers and hold mantrakshata, recite the retained establishment passage using the shared replay range, then place the akshata.'),
('Pray that Janardana accept the worship, protect the devotee and remain graciously present in the book until worship ends.','Take flowers and mantrakshata, recite the continued-presence prayer and retain the image-to-book spoken correction.'),
('Attend to Narayana’s presence while touching the books.','Place flowers and mantrakshata, touch the books, say Om Namo Narayanaya Om eight times as instructed and worship with flowers.'),
('Pray for invocation, establishment, favorable presence and grace, preserving the three pleas prasida.','Recite every retained presence-related formula and all three repetitions of prasida.'),
('Understand the teacher’s alternative: known suktas may be recited; otherwise a deity stotra is given as the option.','Offer flowers and akshata, recite known suktas or a deity stotra, offer pushpanjali and naivedya, perform the recorded arati and hold akshata in the right hand with two spoonfuls of water.'),
('Offer this Mula-day Saraswati invocation worship for the pleasure of Lakshmi-Vedavyasa through the recorded indwelling hierarchy.','Recite the dedication, release the water into the bowl and say Shrikrishnarpanam astu.'),
('Attend to the separate evening services and the transition to the next Saraswati worship lesson.','In the evening perform the stated panchopachara worship with turmeric/kumkuma and offer betel, areca and fruit; then continue to the worship lesson.')]
for s,(c,a) in zip(sections,GUIDANCE):s['contemplate']=c;s['action']=a
write('sections.json',sections)
(ROOT/'complete-english-teaching.txt').write_text('\n\n'.join(s['id']+' '+s['title']+'\n'+'\n'.join(b['english'] if b['kind']=='action' else '\n'.join(line['meaning'] for line in b['gloss']['lines'] if line) for b in s['structuredBlocks']) for s in sections)+'\n',encoding='utf-8')
# Enrich corrected establishment reading with primary textual provenance while
# preserving the original caption and every unedited acoustic witness.
PRIMARY=[{'reference':'Aitareya Brahmana3.24','url':'https://vishvasa.github.io/vedAH_Rk/shAkalam/aitareya-brAhmaNam/sarva-prastutiH/3/12_khaNDaH_1-13/24/','passage':'gṛhā vai pratiṣṭhā sūktam; tatpratiṣṭhitatamayā vācā śaṁstavyam; cattle and houses foundation clauses'}, {'reference':'Aitareya Brahmana1.30','url':'https://vishvasa.github.io/vedAH_Rk/shAkalam/aitareya-brAhmaNam/sarva-prastutiH/1/5_khaNDaH_1-4/30/','passage':'uttamā pratiṣṭhā; divine sovereignty, Śrī, lordship, Bradhna abode, Prajapati dwelling, independent rule and etam evaitābhiḥ'}]
for s in sections:
 for b in s['structuredBlocks']:
  if b['kind']=='mantra' and b['startSeconds']==847.36:
   b['notes']='Noisy automatic readings have been corrected by comparing the retained acoustic clauses with Aitareya Brahmana3.24 and1.30. Kṣatra means sovereignty, not a canopy. Recorded repetitions and the final return to the foundation phrase remain. The final return’s exact gṛhāṇām inflection and api fragment are provisional. No surrounding canonical continuation has been added.'
   b['textualReferences']=PRIMARY
   for line in b['gloss']['lines']:line['textualReferences']=PRIMARY;line['translationEvidence']='Primary Aitareya textual reading compared with native captions and both acoustic passes; independent gpt4o targeted witness retained, without pretending exact pronunciation is established.'
 s['verifyNotes']=[b['notes'] for b in s['structuredBlocks'] if b.get('notes')]
write('sections.json',sections);write('uncertainty-inventory.json',[{'sectionId':s['id'],'notes':s['verifyNotes']} for s in sections if s['verifyNotes']]);write('textual-reading-provenance.json',PRIMARY)
(ROOT/'complete-english-teaching.txt').write_text('\n\n'.join(s['id']+' '+s['title']+'\n'+'\n'.join(b['english'] if b['kind']=='action' else '\n'.join(line['meaning'] for line in b['gloss']['lines'] if line) for b in s['structuredBlocks']) for s in sections)+'\n',encoding='utf-8')

# Record the substance divergence rather than changing a clear native word to a
# different ritual material on the strength of one acoustic recognition.
for s in sections:
 if s['id']=='A02':
  s['structuredBlocks'][0]['notes']='At116.079s the native word is ariśina (turmeric); fine window3 instead recognizes aṣṭagandha, and the coarse pass has a noisy aṣṭanā join. Turmeric is retained from the explicit native marker; the divergent acoustic recognition is preserved in the clause audit.'
 s['verifyNotes']=[b['notes'] for b in s['structuredBlocks'] if b.get('notes')]
write('sections.json',sections)
write('uncertainty-inventory.json',[{'sectionId':s['id'],'notes':s['verifyNotes']} for s in sections if s['verifyNotes']])
# Clause-level audit preserves every fine-response character, maps lexical clauses
# to retained occurrences, and makes witness disagreements explicit.
import difflib
DV={
1:'Native verse spelling is repaired with fine/coarse agreement; calendar clauses retained.',
2:'Rangoli/red-earth wording is recovered by both acoustic passes; all preparation clauses retained.',
3:'Repeated picture-placement instruction is retained twice. Fine aṣṭagandha versus native ariśina and coarse aṣṭanā remains explicitly disputed, with turmeric retained from the native marker.',
4:'Incense word ūdukaḍḍi is acoustically recovered from native kūdukaḍḍi. All vessel/count/seating clauses retained.',
5:'The fine pass has acyuta in an earlier name slot where native and coarse have Vishnu; Vishnu retained. Fast name list and pranayama formulas represented; uncertain name endings visible.',
6:'Sankalpa locality and era forms preserved from the acoustic witnesses rather than replaced with a modern-location formula.',
7:'Native/paired acoustic date and purpose clauses retained; pouring/releasing water belongs to the following Kannada block rather than Sanskrit recitation.',
8:'Full lamp/akshata instructions retained; damaged Kapila verse discussed in specific notes, not filled with its unspoken textual continuation.',
9:'Kapila knowledge/fearlessness and Aja-assembly restarts retained. Dattatreya seed formula recovered acoustically. Hayagriva inserted pratihati fragment retained.',
10:'Hayagriva terminates after vidyā/aśeṣata/Brahma-Isha expression; no extra reference-text lines added. Rama akshata cue and invocation retain their interruption.',
11:'Krishna and Parashurama forms retained; native hattu instruction corrected to acoustic mattu. Name/sandhi alternatives recorded in block notes.',
12:'Narasimha prayer recovered acoustically despite native dropped opening; shares a native passage cue. No pronunciation certainty claimed.',
13:'Vyasa meditation and Gayatri clauses retained; Narayana restarts beginning at discus/conch preserved.',
14:'Lakshmi middle meditation line recovered acoustically where native captions omit or garble it; Narayana repeated faultless-power phrase retained.',
15:'Bhu meditation recovered from fine+native despite whole omission in coarse. Repeated Bhu salutation and Durga restarted discus-lotus expression retained.',
16:'Mukhyaprana invocation occurs twice and both retained; hand-gesture joining varies and is noted.',
17:'Saraswati opening/perception/Self-knowledge restarts retained. Gauri footed-form sequence recovered acoustically; Sanskrit joining readings remain specifically provisional.',
18:'Bharati and Shesha repetitions retained at their native occurrence slots. Extra Bharati meditation-only echo in fine/coarse remains a witness repetition variant; no separate native onset proves a third occurrence.',
19:'Book invocation deity-name list retained in full; book-line/Prana-Shri and excellence phrase variants remain explicitly noted.',
20:'Janaki/Satya/Rukmini list repeated; both occurrences retained, not overlap-deduplicated across actual different native times.',
21:'Complete sage/deity/commentary-teacher list retained. Gugu/Kuhu-like name and contracted Jayatirtha remain noted variants.',
22:'Establishment wording corrected through primary Aitareya3.24 text matched to native/acoustic syllables; original VTT and targeted response untouched.',
23:'Divine-sovereignty clause corrected through primary Aitareya1.30, not canopy semantics. Ityadi and returned foundation phrase retained. Prayer’s arghya expression restarts retained.',
24:'Image-to-book location correction retained; eightfold instruction translates actual speech without inserting eight unrecorded mantra occurrences. Middle presence-form variants documented.',
25:'Every sukta-or-stotra option, repeated naivedya instruction, arati instruction and two-spoonful water clause retained.',
26:'Dedication, release, ShriKrishna offering, evening panchopachara and next-video thanks retained. Turmeric/ashtanga acoustic joining is not expanded into an unrecorded rite.'}
# Devanagari-to-Roman comparison is used only to find evidence correspondences;
# source editions and raw responses remain distinct.
dvcons=dict(zip('कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह',['k','kh','g','gh','ṅ','c','ch','j','jh','ñ','ṭ','ṭh','ḍ','ḍh','ṇ','t','th','d','dh','n','p','ph','b','bh','m','y','r','l','v','ś','ṣ','s','h']))
dvsign=dict(zip('ािीुूृॄेैोौ',['ā','i','ī','u','ū','ṛ','ṝ','e','ai','o','au']));dvvol=dict(zip('अआइईउऊऋॠएऐओऔ',['a','ā','i','ī','u','ū','ṛ','ṝ','e','ai','o','au']))
def roman_compare(text):
 text=roman(text);out='';i=0
 while i<len(text):
  c=text[i]
  if c in dvcons:
   out+=dvcons[c]
   if i+1<len(text) and text[i+1] in dvsign:out+=dvsign[text[i+1]];i+=1
   elif i+1<len(text) and text[i+1]=='्':i+=1
   else:out+='a'
  else:out+=dvvol.get(c,dvsign.get(c,{'ं':'ṁ','ः':'ḥ','ऽ':"'"}.get(c,c)))
  i+=1
 return re.sub('[^a-z ]','',__import__('unicodedata').normalize('NFKD',out.lower()).encode('ascii','ignore').decode())
clause_audit=[];prior_occurrences={}
for window in audit:
 rawtext=window['rawGPTText'];clauses=re.findall(r'[^.।?!]*[.।?!]+\s*|[^.।?!]+$',rawtext)
 assert ''.join(clauses)==rawtext
 entries=[]
 for ci,clause in enumerate(clauses):
  eligible=[b for s in sections for b in s['structuredBlocks'] if b['id'] in window['segmentIds']]
  normalized=roman_compare(clause)
  ranked=sorted([(difflib.SequenceMatcher(None,normalized,roman_compare(b['sourceRoman'])).ratio(),b) for b in eligible],key=lambda x:x[0],reverse=True)
  # Short clause token containment is stronger than comparing its length to a
  # long uninterrupted recitation run.
  if ranked:
   score,best=ranked[0];chosen=[best['id']]
   for score2,b in ranked[1:]:
    if score2>=.20 and score2>=score*.75:chosen.append(b['id'])
  else:score=0;chosen=[]
  duplicates=[]
  for bid in chosen:
   for widx,oldtext in prior_occurrences.get(bid,[]):
    if abs(widx-window['chunkIndex'])==1 and difflib.SequenceMatcher(None,normalized,oldtext).ratio()>.70:duplicates.append({'priorWindow':widx,'sameRetainedOccurrenceSegmentId':bid,'basis':'same native occurrence ID in overlapping acoustic windows; actual later repeated occurrence retains a different native marker span'})
   prior_occurrences.setdefault(bid,[]).append((window['chunkIndex'],normalized))
  entries.append({'clauseId':f"avahana-fine-{window['chunkIndex']:02d}-clause-{ci+1:02d}",'rawOriginal':clause,'retainedSegmentIds':chosen,'nativeWindowSegmentIds':window['segmentIds'],'mappingBasis':'source-local overlap plus normalized lexical comparison; manual window-specific disposition below','lexicalSimilarity':round(score,3),'disposition':DV[window['chunkIndex']],'overlapOccurrenceMapping':duplicates,'specificReadingNotes':[b.get('notes') for b in eligible if b['id'] in chosen and b.get('notes')],'confidence':'lexical-correspondence' if score>=.25 else 'shared-window correspondence; lexical reading specifically disputed'})
 clause_audit.append({**window,'clauses':entries,'exactRawClauseReconstruction':''.join(e['rawOriginal'] for e in entries)==rawtext})
write('clause-audit.json',clause_audit)
write('caption-clause-audit.json',[{'cueId':c['id'],'rawText':c['text'],'retainedMarkerIds':[t['id'] for t in tokens if t['cueId']==c['id']],'disposition':'fresh native word markers retained with exact time/text; previous display context retained in rawBody only' if any(t['cueId']==c['id'] for t in tokens) else 'rolling-caption redisplay/context cue, exact rawBody preserved; no new spoken occurrence asserted'} for c in rawcues])
for s in sections:
 for b in s['structuredBlocks']:
  if b['kind']=='mantra' and b['startSeconds']==640.24:
   for line in b['gloss']['lines']:
    if line['text']=='bhāratīṁ dhyāyāmi' or (line['text']=='bhāratyai namaḥ bhāratīṁ dhyāyāmi' and line['startSeconds']==640.24):
     line.update({'startSeconds':684.079,'endSeconds':686.88,'sharedPassageCue':True,'sharedCueGroup':'avahana-bharati-echo-684','timingStatus':'shared-native-passage','notes':'Shared684.079–686.880s native range: both acoustic passes retain an additional meditation-only echo, without an independent native word-marker onset.'})
   b['notes']+=' Both acoustic passes retain an additional Bharati meditation-only echo; it is preserved with the shared684.079–686.880s range rather than silently removed.'
 s['verifyNotes']=[b['notes'] for b in s['structuredBlocks'] if b.get('notes')]
for window in clause_audit:
 if window['chunkIndex']==18:
  for entry in window['clauses']:entry['disposition']='Bharati and Shesha repetitions are retained; the additional meditation-only Bharati echo supported by fine window18 and coarse window5 shares native684.079–686.880s because no independent onset exists.'
write('sections.json',sections);write('clause-audit.json',clause_audit);write('uncertainty-inventory.json',[{'sectionId':s['id'],'notes':s['verifyNotes']} for s in sections if s['verifyNotes']])
(ROOT/'complete-english-teaching.txt').write_text('\n\n'.join(s['id']+' '+s['title']+'\n'+'\n'.join(b['english'] if b['kind']=='action' else '\n'.join(line['meaning'] for line in b['gloss']['lines'] if line) for b in s['structuredBlocks']) for s in sections)+'\n',encoding='utf-8')

# Semantic peer-review refinements affect interpretation only, not the retained
# source spellings or acoustic occurrence count.
write('semantic-review-fixes.json',[
 {'sectionId':'A09','change':'smaratorugīrbhiḥ qualifies the Hanuman-led recipients remembering with mighty praises; not a new imperative','basis':'Tantrasara4.36 grammar and read-only semantic peer review'},
 {'sectionId':'A06','change':'ādya retained but probable adya today/now and vowel uncertainty explicit; bhautāvatāre no material-incarnation assertion','basis':'Recorded fine/coarse phonetic form retained; contextual grammatical candidate distinguished from proof'},
 {'sectionId':'A14','change':'nirdoṣa reading and repetitions retained; niḥśeṣa complete/all-powers primary-text candidate explicitly contrasted','basis':'native527.360/531.760; fine14; coarse4; Tantrasara1.20'},
 {'sectionId':'A20','change':'prāṇaśrī is an uncertain cluster; two-deity split unconfirmed','basis':'Disagreement in fine19/coarse5/targeted book-invocation4o; no secure independent lexical identification'}])
