import json
from pathlib import Path
D=Path(__file__).resolve().parent
A=json.loads((D/'fine-window-clause-audit.json').read_text())
def ids(*xs):return ['visarjana-'+x for x in xs]
M={
1:[ids('V01-01')]*14+[ids('V02-01'),ids('V02-02')],
2:[ids('V01-01'),ids('V02-01')]+[ids('V02-02')]*7+[ids('V02-02','V02-03'),ids('V02-03')]+[ids('V02-04')]*3+[ids('V02-05'),ids('V02-05','V03-01'),[],[]],
3:[ids('V03-01')]*8+[[],[]],
4:[ids('V03-01','V03-02'),ids('V03-02'),ids('V03-02'),ids('V03-03')]+[ids('V03-04')]*3+[ids('V03-05'),ids('V03-05','V04-01')]+[ids('V04-01')]*4+[ids('V04-02')],
5:[ids('V04-01')]*2+[ids('V04-02')]*2+[ids('V04-03')]*2+[ids('V05-01','V05-02')]+[ids('V06-01')]*3+[[],[]],
6:[ids('V06-01'),ids('V06-02'),ids('V06-03','V06-04'),ids('V06-04'),ids('V07-01','V07-02')],
7:[ids('V07-01','V07-02'),ids('V07-02')]+[ids('V08-01')]*4+[ids('V08-01','V08-02'),[],[]],
8:[ids('V08-01')]*2+[ids('V08-02')]*4+[ids('V09-01')]*2+[ids('V09-02')]+[ids('V09-03')]*6+[[],[]],
9:[ids('V09-03')]*9+[ids('V09-03','V10-01'),ids('V10-01'),ids('V10-01'),[],[]],
10:[ids('V10-01')]*2+[ids('V10-01','V10-02','V11-01')]+[ids('V11-01')]*10,
11:[ids('V11-01')]*3+[ids('V11-02'),ids('V11-03'),ids('V11-03')]
}
notes={
1:'Greeting, dated Thursday/fourth-day context, all morning duties, renewed worship, all offerings and hand-held flowers/mantra-akshata retained. Final two-word prayer fragment joins the next overlapping witness at the same occurrence.',
2:'Dismissal prayer and book-akshata placement retained. Closing wishes/inflections and establishment middle words remain uncertain in three acoustic witnesses. Source-shaped śakita/gatāsthānam retained. The end-window Acharya introduction continues into window 3.',
3:'Complete Anandatirtha appearance-day explanation retained, including repeated “Madhva tradition”, Madhva Jayanti, named works and unfinished work-title continuation. It has not been reduced to a ritual instruction.',
4:'Both Madhva prayers retained; damaged opening abrahmam/baṅgaragitam and unclear repetition-count word vāra remain flagged. Sumadhvavijaya title restored by coarse/caption comparison; exact uncertain compound endings flagged. Evening transition, tree-name explanation and offerings retained.',
5:'All shami worship speech and self-restart near/to the tree retained. First prayer ending damaged in all acoustic witnesses; the whole phonetic cluster retained. Vishnu sankalpa and repeated pacification word śamanīm retained. End fragment continues into window 6.',
6:'Devanagari partial overlap maps to the same pacification-prayer occurrence. iti…sampūjya is a separately retained quoted Sanskrit instruction. Material wording is disputed: coarse aṣṭāṅga namaskāra, fine aṣṭāṅga-kumkuma, caption turmeric/kumkuma; provisional turmeric/kumkuma displayed with visible note and no invented gesture. Journey prayer preserved as actually witnessed with damaged opening and endings.',
7:'Journey ending is overlap, not an extra repeat. Complete household-life explanation, tambula/dakshina, teacher/acharya homage, gifts and blessing instructions retained. The Vijayadashami quotation begins and continues in window 8.',
8:'Complete charity quotation retained with damaged śāpapuṇyā/jagatā naṇaṃ and taistaisadā/manmūrtiṃ explicitly unresolved. All following Kannada explanation retained, including repeated dāna kōṭi guṇam puṇyam as a Sanskrit recall. Fragrant materials/clothing are not omitted.',
9:'The same overlapped gift list is retained once by timing. Complete gift/dakshina explanation, Smriti Muktavali attribution, repeated “gurus, gurus”, teacher offering/blessings, “so”, Saraswati dismissal and children reading one/two letters retained. Final children clause continues into window 10.',
10:'Children’s learning/intelligence wish completes window 9. Source “ī” before the short Vijaya quotation retained. Complete learning, knowledge/devotion/detachment, longevity/health/prosperity, household auspiciousness, Hari-Vayu-guru prayer, festival greetings and victory wishes retained. Caption-supported “das—Dasara” self-repair retained despite ASR smoothing.',
11:'Greeting overlap maps to the same occurrence; blessings from Hari/Vayu/gurus, short Sri Krishna dedication, all final good wishes and thanks retained through measured media end.'
}
for a in A:
 n=a['windowIndex'];assert len(a['clauses'])==len(M[n]),n;a['review']=notes[n]
 for c,m in zip(a['clauses'],M[n]):
  c.pop('candidateRetainedSegmentIds',None);c['retainedSegmentIds']=m
  c['disposition']='Retained in the identified ordered block(s); window-boundary overlap maps to the same occurrence. ASR clause-local timestamps are unavailable, and block timing uses native embedded VTT markers.' if m else 'Raw ASR punctuation-only ellipsis artifact; preserved in raw witness. No spoken lexical item is assigned to these punctuation characters.'
(D/'fine-window-clause-audit.json').write_text(json.dumps(A,ensure_ascii=False,indent=2))
print('Mapped',sum(len(a['clauses']) for a in A),'raw fine-window clauses explicitly.')
