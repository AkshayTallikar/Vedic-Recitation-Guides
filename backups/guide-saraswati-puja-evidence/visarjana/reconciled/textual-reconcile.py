import json,hashlib
from pathlib import Path
D=Path(__file__).resolve().parent
S=json.loads((D/'sections.json').read_text());oldsource=(D/'complete-source.txt').read_text()
refs=[]
for name in ['data4.js','data10.js']:
 p=Path('/tmp/vedic-saraswati-guide/site')/name
 refs.append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'role':'Independent existing local guide textual candidate; not this recording’s acoustic or timing authority.'})
b=S[2]['structuredBlocks'][1];oldtext=b['text'];rawroman=b['sourceRoman'];l=b['gloss']['lines'][0]
l['text']='abhramaṃ bhaṅgarahitam ajaḍaṃ vimalaṃ sadā |'
l['meaning']='[Textually reconciled reading:] Ever free from error, free from impairment, not inert, and pure [qualifying Anandatirtha in the next line].'
l['words']=[{'text':'abhramaṃ','meaning':'free from error or delusion (a- + bhrama); accusative singular qualifying Anandatirtha'},{'text':'bhaṅgarahitam','meaning':'free from break, destruction or impairment (bhaṅga + rahita); accusative singular qualifying Anandatirtha'},{'text':'ajaḍaṃ','meaning':'not inert or dull; conscious and discerning'},{'text':'vimalaṃ','meaning':'pure, stainless'},{'text':'sadā','meaning':'always; qualifies the enduring freedom from these defects'}]
b['text']='\n'.join(x['text'] if x else '' for x in b['gloss']['lines']);b['sourceRoman']=rawroman
note='The displayed opening is textually reconciled as abhramaṃ bhaṅgarahitam: local UTM-book data4.js, page 33, and independent guide data10.js both supply this reading. Fine acoustic GPT has abrahmaṃ baṅgaragitaṃ, coarse GPT abrahmaṃ baṅgāragitaṃ, targeted GPT-4o abramam-baṅkāritam. These phonetic shapes and the shared ajaḍaṃ vimalaṃ sadā/ānandatīrtha continuation support the candidate. This is an explicitly marked textual correction, not exact acoustic certainty; sourceOriginal and raw sourceRoman remain unchanged.'
b['notes']=[note]
b['readingReconciliation']={'status':'textually-reconciled-audio-compatible','previousDisplay':oldtext,'retainedSourceRoman':rawroman,'displayReading':b['text'],'timingBasis':'Native embedded VTT markers unchanged','references':refs,'acousticWitnesses':[{'path':str(D.parent/'gpt-fine/original-part-004-transcript.json'),'reading':'ಅಬ್ರಹ್ಮಂ ಬಂಗರಗಿತಂ, ಅಜಡಂ ವಿಮಲಂ ಸದಾ ಆನಂದತೀರ್ಥಮದುಲಂ'},{'path':str(D.parent/'gpt/original-part-001-transcript.json'),'reading':'ಅಬ್ರಹ್ಮಂ ಬಂಗಾರಗಿತಂ, ಅಜಡಂ ವಿಮಲಂ ಸದಾ ಆನಂದತೀರ್ಥಮುದಲಂ'},{'path':str(D/'madhva-gpt4o.json'),'reading':'ಅಬ್ರಮಮ್ಬಂಕಾರಿತಂ ಗಚತಂ ವಿಮಲಂ ಸದ ಆನಂದ ತೀರ್ಥಮುದುಲಂ'}]}
S[2]['verifyNotes']=[n for n in S[2]['verifyNotes'] if 'Opening abrahmaṃ' not in n]+[note]
# Supplementary textual candidates improve interpretation while retaining uncertain audible clusters in display.
candidates=[
 ('V04',1,'A dictionary quotation of Nirnayasindhu supplies śamīyuktaṃ jagannāthaṃ bhaktānāmabhayaṅkaram / arcayitvā śamīvṛkṣamarcayecca tataḥ punaḥ. This explains the prayer’s object: Jagannatha associated with shami, granting devotees fearlessness, followed by tree worship. The recording’s arcayāmi tvāṃ and damaged ending differ; the candidate is not substituted.'),
 ('V06',0,'Digitized Prativarshikapujakathasangraha, Shami worship passage, supplies duḥkhapraṇaśinīṃ dhanyāṃ prapadyēhaṃ śamīṃ śubhām; another tradition reads duḥsvapnanāśinīm. This supports a prayer to the auspicious shami as remover of suffering, approached for refuge. The recording’s duḥkhāpnu sanīṃ cluster does not securely distinguish these variants, so it remains retained.'),
 ('V07',0,'Digitized Prativarshikapujakathasangraha supplies dhāriṇyārjunabāṇānāṃ rāmasya priyavādinī / kariṣyamāṇayātrāyāṃ … nirvighnakartrī tvaṃ. These candidates explain shami as bearer of Arjuna’s arrows, dear-speaking to Rama, and remover of journey obstacles. The recording has an initial dharaṇi restart and noisy prajñavādini/kartritvaṃ; original wording remains rather than silently inserting the standard verse.')]
webrefs=[{'url':'https://www.transliteral.org/pages/z130122224142/view','title':'Prativarshikapujakathasangraha, Navaratrotthapanavidhi, Shami-vriksha-pujanavidhi','role':'Digitized ritual text candidate; publisher page supplies no edition/primary-source references, so it is not represented as an official authenticated edition.','support':'Shami suffering-removal and journey-prayer candidates; differing transmitted variants remain visible.'},{'url':'https://kosha.app/word/sa/%E0%A4%A8%E0%A4%B5%E0%A4%B0%E0%A4%BE%E0%A4%A4%E0%A5%8D%E0%A4%B0','title':'Kosha Shabdakalpadruma Navaratra entry, quoting Nirnayasindhu','role':'Secondary dictionary quotation of a primary ritual text, not official authenticated primary edition.','support':'Jagannatha/shami worship candidate; source-specific audible wording retained.'}]
for sid,i,n in candidates:
 s=next(s for s in S if s['id']==sid);q=s['structuredBlocks'][i];q['notes'].append(n);s['verifyNotes'].append(n);q['textualCandidates']=webrefs
# Specific gloss interpretations of intact components in damaged clusters.
q=S[5]['structuredBlocks'][0]['gloss']['lines'][1]
q['meaning']='[Acoustically damaged:] I approach the auspicious shami, described as pacifying suffering or bad dreams and as blessed. The exact first compound and verb remain uncertain; textual variants are listed in the note.'
q['words'][2]['meaning']='audible dhānyaṃ; contextual textual candidate dhanyāṃ means blessed or fortunate, feminine accusative qualifying shami; exact vowel/consonant reading remains uncertain'
q['words'][3]['meaning']='audible prāptayēhaṃ; textually compatible candidate prapadyēham means “I approach/take refuge” (prapadyē + aham), but the verb is not acoustically secure'
q=S[6]['structuredBlocks'][0]['gloss']['lines'][0]
q['words'][1]['meaning']='audible dhāriṇyārjuna; textual candidate dhāriṇī + arjuna means “bearer of Arjuna’s [arrows]”; the compound division remains uncertain'
q['words'][4]['meaning']='audible prajñavādini; textual candidate priyavādini means “one speaking pleasantly/dearly [to Rama]”; intended epithet not acoustically secure'
q=S[6]['structuredBlocks'][0]['gloss']['lines'][2]
q['words'][1]['meaning']='audible nirvighnakartṛtvaṃ; textual candidate nirvighnakartrī tvaṃ means “you who make [the journey] free from obstacles”; segmentation/ending remains uncertain'
(D/'sections.json').write_text(json.dumps(S,ensure_ascii=False,indent=2))
assert ''.join(s['originalScript'] for s in S)==oldsource
(D/'complete-roman.txt').write_text(''.join(b['sourceRoman'] for s in S for b in s['structuredBlocks']))
(D/'uncertainty-inventory.json').write_text(json.dumps([{'segmentId':b['segmentId'],'startSeconds':b['startSeconds'],'endSeconds':b['endSeconds'],'notes':b['notes']} for s in S for b in s['structuredBlocks'] if b.get('notes')],ensure_ascii=False,indent=2))
(D/'textual-reconciliation-provenance.json').write_text(json.dumps({'madhvaOpening':b if False else S[2]['structuredBlocks'][1]['readingReconciliation'],'shamiCandidates':webrefs,'charity':'No reliable official primary textual witness was identified in the scoped search. Damaged quotation remains unchanged.','scope':'Display/gloss interpretation improved with explicit candidate provenance; originalScript/sourceOriginal/raw sourceRoman and source-local timing retained byte-for-byte.'},ensure_ascii=False,indent=2))
print('Textual reconciliation applied; complete-source unchanged.')
