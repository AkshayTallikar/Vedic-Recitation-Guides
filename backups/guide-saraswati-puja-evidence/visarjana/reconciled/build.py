import json,re,hashlib
from pathlib import Path
D=Path(__file__).resolve().parent; BASE=D.parent
E=json.loads((BASE/'captions/native-word-events.json').read_text())['events']
# Kannada transliteration is mechanical and reversible; Sanskrit display is editorially reconciled below.
cons=dict(zip('ಕಖಗಘಙಚಛಜಝಞಟಠಡಢಣತಥದಧನಪಫಬಭಮಯರಲವಶಷಸಹಳಱ','k kh g gh ṅ c ch j jh ñ ṭ ṭh ḍ ḍh ṇ t th d dh n p ph b bh m y r l v ś ṣ s h ḷ ṟ'.split()))
vowels=dict(zip('ಅಆಇಈಉಊಋೠಎಏಐಒಓಔ','a ā i ī u ū ṛ ṝ e ē ai o ō au'.split()))
marks=dict(zip('ಾಿೀುೂೃೄೆೇೈೊೋೌ','ā i ī u ū ṛ ṝ e ē ai o ō au'.split()))
def roman(s):
 out='';i=0
 while i<len(s):
  c=s[i]
  if c in cons:
   out+=cons[c]
   if i+1<len(s) and s[i+1] in marks:out+=marks[s[i+1]];i+=1
   elif i+1<len(s) and s[i+1]=='್':i+=1
   else:out+='a'
  elif c in vowels:out+=vowels[c]
  elif c=='ಂ':out+='ṃ'
  elif c=='ಃ':out+='ḥ'
  else:out+=c
  i+=1
 return out
sections=[];segments=[];uncertainties=[]
def sec(slug,title,contemplate,action):
 s={'id':f'V{len(sections)+1:02}','slug':slug,'title':title,'type':'instruction','sourceId':'visarjana','structuredBlocks':[],'contemplate':contemplate,'action':action,'verify':False,'verifyNotes':[]};sections.append(s);return s

def block(s,kind,start,end,orig,display,lines=None,notes=None):
 i=len(s['structuredBlocks']);sid=f"visarjana-{s['id']}-{i+1:02}"
 b={'kind':kind,'sourceOriginal':orig+' ','sourceRoman':roman(orig)+' ','startSeconds':start,'endSeconds':end,'segmentId':sid}
 if kind=='action':b['english']=display
 else:
  b['text']=display;b['sourceRoman']=display
  gloss=[]
  for text,meaning,words,a,z in lines:
   if text is None:gloss.append(None);continue
   toks=[t for t in text.split() if t not in ['|','||']]; meanings=words.split('~');assert len(toks)==len(meanings),(text,toks,meanings)
   gloss.append({'text':text,'meaning':meaning,'words':[{'text':t,'meaning':m} for t,m in zip(toks,meanings)],'startSeconds':a,'endSeconds':z,'translationAttribution':'Editorial Sanskrit analysis of acoustic and caption witnesses; uncertain readings identified in notes.'})
  b['gloss']={'lines':gloss}
 if notes:b['notes']=notes;s['verify']=True;s['verifyNotes']+=notes;uncertainties.append({'segmentId':sid,'startSeconds':start,'endSeconds':end,'notes':notes})
 s['structuredBlocks'].append(b)
 seg={'id':sid,'sourceId':'visarjana','start':start,'end':end,'sourceOriginal':b['sourceOriginal'],'sectionId':s['id'],'blockIndex':i,'language':'Sanskrit' if kind=='mantra' else 'Kannada','captionCueIndices':sorted(set(e['raw_cue_ref']['cue_index'] for e in E if e['start']<end and e['end']>start))}
 segments.append(seg)
 return b

def A(s,a,z,o,t,notes=None):return block(s,'action',a,z,o,t,notes=notes)
def M(s,a,z,o,ls,notes=None):return block(s,'mantra',a,z,o,'\n'.join(x[0] if x[0] else '' for x in ls),ls,notes)

s=sec('vijayadashami-morning','Vijayadashami morning and renewed worship','The speaker places Saraswati dismissal after the ordinary morning observances.','Complete the stated daily observances, then renew Saraswati worship and offer naivedya as described.')
A(s,.48,42.079,'ನಮಸ್ಕಾರ, ಚರಣಂ ಪವಿತ್ರಂ ಯೂಟ್ಯೂಬ್ ಚಾನೆಲ್ನ ಪ್ರಿಯ ವೀಕ್ಷಕರಿಗೆ ನಮಸ್ಕಾರ. ದಶಮಿ ಅಂದರೆ ವಿಜಯದಶಮಿ ದಿನ, ನಾಲ್ಕನೇ ದಿನ ಗುರುವಾರ. ಬೆಳಿಗ್ಗೆ ನಿಮ್ಮ ನಿತ್ಯಕರ್ಮಾನುಷ್ಠಾನಗಳು ಅಂದರೆ ಸ್ನಾನ, ಗೋಪೀಚಂದನ ಧಾರಣೆ, ಸಂಧ್ಯಾವಂದನೆ, ದೇವರ ಪೂಜೆಯನ್ನು ಪೂರ್ಣ ಮುಗಿಸಿ, ನೀವೇನು ಆವಾಹನ ಮಾಡಿಟ್ಟಿದ್ದೀರಿ ಸರಸ್ವತಿ ದೇವಿ, ಅದಕ್ಕೆ ಪುನಃ ಪೂಜೆಯನ್ನು ಮಾಡಿರಿ. ಅಕ್ಷತ ಸಮರ್ಪಣ, ಹೂವಿನಿಂದ ಅರಿಶಿಣ, ಕುಂಕುಮ, ಗಂಧ ಎಲ್ಲವನ್ನೂ ಪೂಜೆಯನ್ನು ಮಾಡಿ, ಒಂದು ನೈವೇದ್ಯ, ಹಣ್ಣು ಕಾಯಿ ನೈವೇದ್ಯವನ್ನು ಮಾಡಿ.','Greetings. Greetings to the dear viewers of the Charanam Pavithram YouTube channel. Dashami means Vijayadashami day: the fourth day, Thursday. In the morning, finish all your daily religious observances—bathing, applying gopichandana, sandhyavandana and worship of God. Then worship again the Saraswati Devi whom you have invoked. Offer akshata and worship with flowers, turmeric, kumkuma and sandal paste; perform the worship with all of these. Make a naivedya offering, an offering of fruit and coconut.', ['“The fourth day, Thursday” is the 2025 recording’s calendar context, not a current-date instruction. “Fruit and coconut” interprets the spoken haṇṇu-kāyi; exact offering quantities are not supplied.'])

s=sec('saraswati-dismissal','Saraswati dismissal prayers','The dismissal asks Saraswati to accept the worship, grant the desired blessings and return again.','Hold flowers and mantra akshata as instructed; after the dismissal verse, place the mantra akshata on the book-Saraswati.')
A(s,42.079,44.0,'ಹೂ ಮಂತ್ರಾಕ್ಷತೆ ಕೈಯಲ್ಲಿ ಹಿಡ್ಕೊಂಡು,','Holding flowers and mantra akshata in your hand,')
M(s,44.0,61.76,'ಉತ್ತಿಷ್ಠ ದೇವಿ ಕಲ್ಯಾಣಿ, ಗೃಹೀತ್ವ ಪೂಜನಂ ಮಮ, ಸ್ವಸ್ಥಾನಂ ಗಚ್ಛ ಶುಭಗೆ, ಕಾಮಾನ್ ದೇಹಿ ಸರಸ್ವತಿ. ಯಾಂತು ದೇವಗಣಾಃ ಸರ್ವೇ, ಪೂಜಾಮಾದಾಯ ಮತ್ಕೃತಾಂ, ಇಷ್ಟಕಾಮ್ಯಾಂಶ್ಚ ದದ್ಯಾತಂ, ಪುನಃ ಆಗಮನಾಯ ಚ.',[
('uttiṣṭha dēvi kalyāṇi gṛhītva pūjanaṃ mama |','Arise, auspicious Goddess, having accepted my worship.','arise~O Goddess~O auspicious one~having accepted; the audible gṛhītva is retained rather than silently expanded~worship~my',44.0,49.35),
('svasthānaṃ gaccha subhagē kāmān dēhi sarasvati ||','Go to your own abode, fortunate one; grant the desired blessings, Saraswati.','your own place or abode~go~O fortunate, gracious one~desired things or wishes~give~O Saraswati',49.36,53.75),
(None,'','',0,0),
('yāntu dēvagaṇāḥ sarvē pūjāmādāya matkṛtām |','May all the divine hosts depart, having accepted the worship performed by me.','may they go~hosts of deities~all~having accepted the worship (pūjām + ādāya)~performed by me (mat + kṛtām)',53.76,58.069),
('iṣṭakāmyāṃśca dadyātaṃ punaḥ āgamanāya ca ||','[Uncertain inflection:] May the desired wishes be granted, and [may this be] for coming again.','desired wishes, with ca “and”; the ending is uncertain in the witnesses~may [you] give; the audible ending is uncertain~again~for coming or returning~and',58.079,61.76)
],['The fine acoustic witness gives gṛhītva and iṣṭakāmyāṃśca dadyātaṃ. The last inflections are uncertain; they have not been silently regularized to a memorized verse.'])
A(s,61.76,68.0,'ಅಂತ ಪುಸ್ತಕ ಸರಸ್ವತಿಯ ಮೇಲೆ ಮಂತ್ರಾಕ್ಷತೆಯನ್ನ ಹಾಕಿರಿ. ಆವಾಗ,','Having said this, place the mantra akshata on the book-Saraswati. Then,', ['The transition after hākiri is noisy; the witnesses give “āvāga”/a similarly sounding continuation. The placement instruction is clear.'])
M(s,68.0,73.92,'ಅಕ್ಷರಾಭಿಮಾನಿ ದೇವತಾ ಶಕಿತ ಸರಸ್ವತ್ಯಂತರ್ಗತ ವೇದವ್ಯಾಸಂ ಗತಾಸ್ಥಾನಂ ಪ್ರತಿಷ್ಠಾಪಯಾಮಿ.',[
('akṣarābhimāni dēvatā śakita sarasvatyantargata vēdavyāsaṃ gatāsthānaṃ pratiṣṭhāpayāmi.','I establish Vedavyasa, present within Saraswati, [with the deities presiding over letters; connecting word and place phrase unresolved].','presiding over letters or syllables~deity/deities~audible śakita; a word linking the presiding deities is intended, but its exact form and meaning are unresolved~present within Saraswati; the compound is uncertain~Vedavyasa, object of the establishment~audible gatāsthānaṃ, containing sthāna “place”; exact prefix and relation are unresolved~I establish',68.0,73.92)
],['The captions give dēvatāśagita and vēdavyāsaṃsthānaṃ; fine GPT gives dēvatā śakita and gatāsthānaṃ. The audible śakita and gatāsthānaṃ are retained; antargata is supported by the coarse witness. No remembered establishment formula has been substituted.'])
A(s,73.92,80.88,'ಅಂತ ಅದಕ್ಕೆ ಪೂಜೆಯನ್ನು ಮಾಡಿ ಮುಗಿಸಿರಿ. ಮುಗಿಸಿಟ್ಟು,','Say this, worship it and finish. Having finished,')

s=sec('madhva-jayanti','Madhva Jayanti observance','Vijayadashami is described as the appearance day of Sri Madhvacharya, the foundational teacher of the Madhva tradition.','Honor and remember Sri Madhvacharya; recite the works or prayers the speaker names, according to the recorded instruction.')
A(s,80.88,128.8,'ಈ ದಿನ ವಿಶೇಷವಾಗಿ ಶ್ರೀಮದಾನಂದತೀರ್ಥ ಭಗವತ್ಪಾದಾಚಾರ್ಯರು, ಲೋಕಗುರುಗಳು, ನಮ್ಮನ್ನೆಲ್ಲ ಉದ್ಧಾರಣ ಮಾಡಲಿಕ್ಕಾಗಿ ಅವತಾರ ಮಾಡಿದಂಥ ದಿನ ಈ ವಿಜಯದಶಮಿ. ಶ್ರೀಮದಾಚಾರ್ಯರನ್ನ ನಾವು ವಿಶೇಷವಾಗಿ ಅವರನ್ನ ಕೊಂಡಾಡಬೇಕಾದ ದಿನ. ನಮ್ಮ ಮಧ್ವ ಸಂಪ್ರದಾಯವನ್ನ, ಮಧ್ವ ಸಂಪ್ರದಾಯದ ಆದಿಗುರುಗಳಾದ ಶ್ರೀಮದಾಚಾರ್ಯರ ಜಯಂತಿ, ಮಧ್ವ ಜಯಂತಿ. ಮತ್ತು ಆದಷ್ಟು ಅವರು ಮಾಡಿರುವ ದ್ವಾದಶ ಸ್ತೋತ್ರ, ನರಸಿಂಹನಖಸ್ತುತಿ, ಶ್ರೀಮದಾಚಾರ್ಯರ ಸುಮಧ್ವವಿಜಯ ಇತ್ಯಾದಿಗಳನ್ನ ಪಾರಾಯಣ. ಇಲ್ಲದಿದ್ದರೆ,','This day, Vijayadashami, is particularly the day on which Srimad Anandatirtha Bhagavatpadacharya, the teacher of the world, appeared to uplift us all. It is a day on which we should especially praise Srimadacharya. Our Madhva tradition—this is the birth celebration of Srimadacharya, the original teacher of the Madhva tradition, Madhva Jayanti. As much as possible, recite the Dvadasha Stotra he composed, Narasimha Nakha Stuti, Sumadhvavijaya concerning Srimadacharya, and the like. If that is not possible,', ['The work-title Narasimha Nakha Stuti is split/noisy in both caption and fine acoustic witnesses. “Sumadhvavijaya” is a contextual title reading of the acoustic sumadvavijaya. The speaker’s incomplete “our Madhva tradition” phrase is retained.'])
M(s,128.8,135.19,'ಅಬ್ರಹ್ಮಂ ಬಂಗರಗಿತಂ ಅಜಡಂ ವಿಮಲಂ ಸದಾ ಆನಂದತೀರ್ಥಮತುಲಂ ಭಜೇ ತಾಪತ್ರಯಾಪಹಂ.',[
('abrahmaṃ baṅgaragitaṃ ajaḍaṃ vimalaṃ sadā |','[Opening uncertain:] … [audible damaged word], not inert, pure, always.','opening sound abrahmaṃ; its intended lexical form and sense remain uncertain~audible baṅgaragitaṃ; baṅga/bhaṅga may involve break or impairment, but the full lexical form and meaning are unresolved~not inert or dull~pure or stainless~always',128.8,131.52),
('ānandatīrthamatulaṃ bhajē tāpatrayāpaham ||','I honor the incomparable Anandatirtha, remover of the threefold suffering.','the incomparable Anandatirtha (ānandatīrtham + atulam)~I worship or honor~remover of the threefold suffering',131.52,135.19)
],['Opening abrahmaṃ and baṅgaragitaṃ remain uncertain; fine GPT gives abrahmaṃ baṅgaragitaṃ. No remembered opening has been substituted.'])
A(s,135.2,137.28,'ಅಂತ ಇದನ್ನ ವಾರ ಹೇಳಬೇಕು.','Say this [the repetition-count word is unclear in this witness].', ['The captions and fine witness give vāra, with no secure preceding count. A repetition count must not be invented.'])
M(s,137.28,145.92,'ನ ಮಾಧವ ಸಮೋ ದೇವೋ ನ ಚ ಮಧ್ವಃ ಸಮೋ ಗುರುಃ ನ ತದ್ವಾಕ್ಯ ಸಮಂ ಶಾಸ್ತ್ರಂ ನ ಚ ತಜ್ಞ ಸಮಃ ಪುಮಾನ್.',[
('na mādhava samō dēvō na ca madhvaḥ samō guruḥ |','No deity is equal to Madhava, and no teacher is equal to Madhva.','no or not~Madhava, Vishnu; the ending is not secure~equal~deity~not~and~Madhva~equal~teacher',137.28,140.64),
('na tadvākya samaṃ śāstraṃ na ca tajña samaḥ pumān ||','No scripture is equal to his words, and no person is equal to one who knows them [compound endings uncertain].','not~his words; witness gives tatvākya~equal~scripture~not~and~one who knows that; the precise sandhi is uncertain~equal~person',140.64,145.92)
],['The fine witness and captions disagree on tadvākya/tatvākya and tajña/tadgya. The displayed forms are provisional lexical readings, not acoustic certification.'])
A(s,145.92,151.84,'ಶ್ರೀಮದಾಚಾರ್ಯರನ್ನ ಸ್ಮರಣೆಯನ್ನ ಮಾಡಬೇಕು. ಮುಗಿಸಿ ಸಂಜೆ,','Remember Srimadacharya. Having finished, in the evening,')

s=sec('shami-worship-opening','Evening worship at the shami tree','The speaker directs everyone to honor the shami tree in the evening and invokes Jagannatha.','Go to the shami tree, called vanni in the explanation; worship and offer flowers and mantra akshata.')
A(s,151.84,162.64,'ಶಮಿ ಅಂದರೆ ವನ್ನಿ ಮರ ಅಂತ ಹೇಳ್ತಾರೆ, ಶಮಿ ವೃಕ್ಷ. ಅದರ ಭಾಗಕ್ಕೆ ಹೋಗಿ ಅಲ್ಲಿ ಅರ್ಚನೆಯನ್ನು, ಅದಕ್ಕೆ ಹೂವು ಮಂತ್ರಾಕ್ಷತೆಯನ್ನ ಸಮರ್ಪಣ ಮಾಡಬೇಕು.','Shami is what they call the vanni tree, the shami tree. Go to its vicinity and worship there; offer flowers and mantra akshata to it.')
M(s,162.64,175.99,'ಶಮಿ ಯುಕ್ತಂ ಜಗನ್ನಾಥಂ ಭಕ್ತಾನಾಮಭಯಂಕರಂ ಅರ್ಚಯಾಮಿ ತ್ವಾಂ ಸಬೀಷ್ಟ ವೃಕ್ಷಮರ್ಚಗೇಷ್ಟದಃ ಪುನಃ.',[
('śami yuktaṃ jagannāthaṃ bhaktānāmabhayaṅkaram |','[Wording uncertain:] Jagannatha associated with shami, who gives fearlessness to devotees.','shami tree; case/compound connection is uncertain~associated with or joined~Jagannatha, Lord of the world~giver of fearlessness to devotees (bhaktānām + abhayaṅkaram)',162.64,168.15),
('arcayāmi tvāṃ sabīṣṭa vṛkṣamarcagēṣṭadaḥ punaḥ ||','I worship you … [the remainder concerning the tree and granting wishes is acoustically unresolved].','I worship~you~audible sabīṣṭa, possibly related to desired things; intended form uncertain~audible cluster containing vṛkṣam “tree” and iṣṭada “giver of desires”; exact words and syntax unresolved~again',168.16,175.99)
],['The second half is damaged across captions and fine GPT; the source-shaped phonetic cluster is retained. It is unsuitable for confident recitation until independently verified.'])
A(s,176.0,180.72,'ಎಲ್ಲರೂ ಕೂಡ ಶಮಿ ಪಕ್ಕ, ಶಮಿಗೆ ಹೋಗಿ ಪೂಜೆಯನ್ನು ಮಾಡಬೇಕು.','Everyone should go near the shami—to the shami—and worship.', ['The speaker restarts the “near/to the shami” phrase; both phrases are retained.'])

s=sec('shami-sankalpa','Shami worship intention','The stated intention places the worship under Sri Vishnu’s prompting and for his pleasure.','Say the recorded intention and worship the shami tree as the speaker instructs.')
M(s,180.72,188.879,'ಭಾರತೀರಮಣ ಮುಖ್ಯಪ್ರಾಣಾಂತರ್ಗತ ಶ್ರೀವಿಷ್ಣು ಪ್ರೇರಣಯಾ ಶ್ರೀವಿಷ್ಣು ಪ್ರೀತ್ಯರ್ಥಂ ಶಮೀಪೂಜಾಂ ಕರಿಷ್ಯೇ.',[
('bhāratīramaṇa mukhyaprāṇāntargata śrīviṣṇu prēraṇayā śrīviṣṇu prītyarthaṃ śamīpūjāṃ kariṣyē.','By the prompting of Sri Vishnu present within Mukhyaprana, consort of Bharati, and for Sri Vishnu’s pleasure, I will perform shami worship.','consort of Bharati, an epithet of Mukhyaprana~present within Mukhyaprana~Sri Vishnu~by the prompting~Sri Vishnu~for the pleasure~shami worship~I shall perform',180.72,188.879)
])
A(s,188.879,191.84,'ಅಂತ ಶಮಿ ವೃಕ್ಷಕ್ಕೆ ಪೂಜೆಯನ್ನು ಮಾಡಬೇಕು.','Say this and worship the shami tree.')

s=sec('shami-prayer','Prayer to shami and worship','The prayer connects shami with the pacification of misfortune and wrongdoing; some words remain unresolved.','Offer the stated prayer, then worship with turmeric and kumkuma as instructed; verify the uncertain recitation words.')
M(s,191.84,206.239,'ಅಮಂಗಲಾನಾಂ ಶಮನೀಂ ಶಮನೀಂ ದುಷ್ಟಕೃತಸ್ಯ ಚ ದುಃಖಾಪ್ನು ಸನೀಂ ಧಾನ್ಯಂ ಪ್ರಾಪ್ತಯೇಹಂ ಶಮೀಂ ಶುಭಾಂ.',[
('amaṅgalānāṃ śamanīṃ śamanīṃ duṣṭakṛtasya ca |','The one who pacifies inauspicious things, who pacifies wrongdoing also.','of inauspicious things or misfortunes~pacifying one~pacifying one, repeated in the spoken prayer~of wrongdoing or evil action~and',191.84,199.27),
('duḥkhāpnu sanīṃ dhānyaṃ prāptayēhaṃ śamīṃ śubhām ||','[Damaged phrase:] … sorrow … grain/prosperity … I approach the auspicious shami [exact syntax unresolved].','audible duḥkhāpnu, apparently involving duḥkha “suffering”; ending unresolved~audible sanīṃ, perhaps the end of a pacification word; lexical form unresolved~audible dhānyaṃ “grain”; dhanyām “blessed” is also possible~audible prāptayēhaṃ, apparently approach/attainment with aham “I”; exact division unresolved~shami, feminine object~auspicious, feminine object',199.28,206.239)
],['The second line is unresolved in both caption and acoustic witnesses. All audible clusters are retained with specific lexical uncertainty; no standard shami verse is supplied from memory.'])
A(s,206.239,208.56,'ಹೀಗೆ ಪ್ರಾರ್ಥನೆಯನ್ನು ಮಾಡಬೇಕು.','Offer the prayer in this way.')
M(s,208.56,212.48,'ಇತಿ ಶಮಿ ಧ್ಯಾನಾಭಿಃ ಸಂಪೂಜ್ಯ.',[
('iti śami dhyānābhiḥ sampūjya.','[Quoted procedural phrase, wording uncertain:] Thus, having fully worshipped shami with meditations.','thus~shami; inflection uncertain~with meditations; ending uncertain~having thoroughly worshipped',208.56,212.48)
],['The speaker’s quoted procedural Sanskrit is retained separately; captions read dhyānabihi and fine GPT dhyānābhiḥ.'])
A(s,212.48,217.44,'ಅರಿಶಿಣ ಕುಂಕುಮದಿಂದ ಪೂಜೆಯನ್ನು ಮಾಡಿರಿ. ಮಾಡಿಟ್ಟು,','Worship with turmeric and kumkuma. Having done so,', ['The caption merges sampūjya with the following turmeric word; the actual embedded marker at 212.48 is used for the language split.'])

s=sec('shami-journey-prayer','Prayer for the journey of life','The speaker explains the journey prayer as asking for favorable circumstances throughout household life.','Offer the prayer, ask that the journey of life be favorable, and give tambula and dakshina as stated.')
M(s,217.44,243.36,'ಧರಣಿ ಧಾರಿಣ್ಯಾರ್ಜುನ ಬಾಣಾನಾಂ ರಾಮಸ್ಯ ಪ್ರಜ್ಞವಾದಿನಿ ಕರಿಷ್ಯಾಮಾಣಾಂ ಯಾತ್ರಾಯಾಂ ಯಥಾಕಾಲಂ ಸುಖಂ ಮಯಾ ತತ್ರ ನಿರ್ವಿಘ್ನಕರ್ತೃತ್ವಂ ಭವ ಶ್ರೀರಾಮಪೂಜಿತೇ.',[
('dharaṇi dhāriṇyārjuna bāṇānāṃ rāmasya prajñavādini |','[Opening damaged:] … bearing Arjuna’s arrows … of Rama … [the addressed epithet is uncertain].','audible dharaṇi, earth/bearer; intended form unresolved~audible dhāriṇyārjuna, containing dhāriṇī “bearer” and Arjuna; exact division uncertain~of arrows~of Rama~audible prajñavādini, perhaps an epithet involving speech; intended form unresolved',217.44,229.03),
('kariṣyāmāṇāṃ yātrāyāṃ yathākālaṃ sukhaṃ mayā |','[Inflections uncertain:] In the journey to be undertaken by me, at the proper time, [may there be] well-being.','to be undertaken; audible feminine ending retained~in the journey~at the appropriate time~happiness, comfort or well-being; the caption has śukam~by me',229.04,236.799),
('tatra nirvighnakartṛtvaṃ bhava śrīrāmapūjitē ||','There, be the one who makes it free from obstacles, O one worshipped by Sri Rama [form uncertain].','there~making [the journey] free from obstacles; the audible compound ending is uncertain~be~O one worshipped by Sri Rama',236.799,243.36)
],['The opening dharaṇi dhāriṇyārjuna and prajñavādini is acoustically unresolved, not silently replaced with a familiar shami prayer. Other uncertain endings are visible in the gloss.'])
A(s,243.36,262.639,'ಅಂತ ಪ್ರಾರ್ಥನೆಯನ್ನು ಮಾಡಬೇಕು. ನಮ್ಮ ಈ ಏನು ಸಂಸಾರಾಂಬೋ ಈ ಯಾತ್ರೆ ಇದೆ, ಇದರಲ್ಲಿ ಎಲ್ಲವೂ ಕೂಡ ನನಗೆ ಅನುಕೂಲವಾಗಲಿ ಅಂತ ಪ್ರಾರ್ಥನೆಯನ್ನು ಮಾಡಿ ತಾಂಬೂಲ ದಕ್ಷಿಣೆಗಳನ್ನ ಕೊಡಬೇಕು ಅಂತ. ಮತ್ತೆ,','Offer this prayer. In this—what shall I say—this journey which is household life, pray, “May everything be favorable to me in it.” Having prayed, give tambula and dakshina. And then,', ['The spoken self-repair “ēnu saṃsārāṃbō” is retained; the explanation clearly compares household life to the journey.'])

s=sec('honor-teachers','Honor teachers and receive blessings','Vijayadashami is described as a special occasion for honoring the teachers who show the way.','Bow to your teachers and acharyas, give the stated gifts and dakshina, and receive their blessings.')
A(s,262.639,284.08,'ವಿಜಯದಶಮಿ ದಿನ ಇನ್ನೊಂದು ವಿಶೇಷ ಯಾವುದು ಅಂದರೆ ಗುರುಗಳನ್ನ, ನಮ್ಮ ಆಚಾರ್ಯರುಗಳನ್ನ, ನಮಗೆ ಯಾರು ಗುರುವಾಗಿದ್ದು ದಾರಿ ತೋರಿಸ್ತಾ ಇದ್ದಾರೆ ಅವರನ್ನ ನಮಸ್ಕಾರ ಮಾಡೋದು, ಅವರಿಗೆ ದಾನ ದಕ್ಷಿಣೆಗಳನ್ನ ಕೊಟ್ಟು ಅವರಿಂದ ಆಶೀರ್ವಾದ ಪಡೆಯೋದು ತುಂಬಾ ವಿಶೇಷ. ವಿಜಯದಶಮಿಯ ದಿನ,','Another special feature of Vijayadashami day is to bow to our teachers, our acharyas, those who serve as our teachers and show us the way. Giving them gifts and dakshina and receiving their blessings is especially significant. On Vijayadashami day,')
M(s,284.08,301.28,'ವಿಜಯೋ ನಾಮ ಕಾಲೋಯಂ ಸರ್ವಕಾರ್ಯಾರ್ಥ ಸಿದ್ಧಿತಃ ದಾನ ಕೋಟಿ ಗುಣಂ ಪುಣ್ಯಂ ತದೈವ ದಶಮೀ ದಿನೇ ವಿಜಯದಶಮೀ ಪ್ರೋಕ್ತಾ ಶಾಪಪುಣ್ಯಾ ಜಗತಾ ನಣಂ ದ್ರವ್ಯೈಃ ಸುಗಂಧಿಭಿಃ ತೈಸ್ತೈಸದಾ ಮನ್ಮೂರ್ತಿಂ ಬ್ರಾಹ್ಮಣಾನಪಿ.',[
('vijayō nāma kālōyaṃ sarvakāryārtha siddhitaḥ |','This time is called Vijaya, [associated with] the accomplishment of every undertaking; the closing form is uncertain.','Vijaya, victory~by name or called~this time (kālaḥ + ayam)~purpose of every undertaking~audible siddhitaḥ, related to accomplishment; inflection unresolved',284.08,288.469),
('dāna kōṭi guṇaṃ puṇyaṃ tadaiva daśamī dinē |','Giving [brings] merit multiplied a crore-fold on that very Dashami day [word connection uncertain].','giving or gift~a crore, ten million~fold or multiplied~merit~on that very occasion~Dashami, the tenth lunar day~on the day',288.479,291.6),
('vijayadaśamī prōktā śāpapuṇyā jagatā naṇaṃ |','Vijayadashami is declared … [the description of merit and the final words are unresolved].','Vijayadashami~declared or said~audible śāpapuṇyā, containing puṇya “merit”; intended compound unresolved~audible jagatā, apparently connected with the world; inflection unresolved~audible naṇaṃ; intended noun or phrase unresolved',291.6,295.51),
('dravyaiḥ sugandhibhiḥ taistaisadā manmūrtiṃ brāhmaṇānapi ||','With fragrant materials … my form … and Brahmins also [the connecting phrase is unresolved].','with materials or valuable things~with fragrant [things]~audible taistaisadā; tais tais “those various” and sadā “always” are possible, but the division is uncertain~my form; audible manmūrtiṃ retained~Brahmins also (brāhmaṇān + api)',295.52,301.28)
],['The quoted verses are not a clean text witness. śāpapuṇyā jagatā naṇaṃ and taistaisadā manmūrtiṃ remain specifically uncertain. The following Kannada supplies the speaker’s explanation without repairing the Sanskrit from memory.'])

s=sec('charity-explanation','Gifts, dakshina and the cited text','The speaker attributes the observance to Smriti Muktavali and stresses remembering teachers and receiving their blessings.','Offer the materials, fragrant things, clothing and dakshina mentioned, honoring acharyas and Brahmins; receive the teachers’ blessings.')
A(s,301.28,309.84,'ಅಂತ ಈ ಒಂದು ಆಶ್ವೀಜ ಮಾಸದ ಈ ವಿಜಯದಶಮಿಯ ದಿನ ನೀವೇನು ದಾನ ಕೊಡುತ್ತೀರಿ,','Thus, on this Vijayadashami day in the month of Ashvija, whatever gift you give,')
M(s,309.84,311.28,'ದಾನ ಕೋಟಿ ಗುಣಂ ಪುಣ್ಯಂ.',[
('dāna kōṭi guṇaṃ puṇyaṃ.','Giving [brings] merit multiplied a crore-fold [quoted again within the explanation].','giving or gift~a crore, ten million~fold or multiplied~merit',309.84,311.28)
])
A(s,311.28,354.4,'ಕೋಟಿ ಗುಣಗಳನ್ನ ಈ ದಿನದಲ್ಲಿ ಮಾಡುವ ದಾನ ವಿಶೇಷವಾಗಿ ಕೊಡುತ್ತೆ ಅಂತ. ದ್ರವ್ಯಗಳು, ಸುಗಂಧ ದ್ರವ್ಯಗಳು, ವಸ್ತ್ರಗಳು, ಅದರಿಂದ ಆಚಾರ್ಯರನ್ನ ಬ್ರಾಹ್ಮಣರನ್ನ ಸಂತೋಷಪಡಿಸಬೇಕು. ಅವರು ದಕ್ಷಿಣೆಯಿಂದ ಅವರನ್ನ ಸಂತೋಷಪಡಿಸಬೇಕು ಅಂತ ಸ್ಮೃತಿ ಮುಕ್ತಾವಳಿ ಎನ್ನುವ ಒಂದು ಗ್ರಂಥದಲ್ಲಿ ಹೇಳಿದ್ದಾರೆ. ಮುಖ್ಯವಾಗಿ ಗುರುಗಳನ್ನ, ಗುರುಗಳನ್ನ ಸ್ಮರಣೆ ಮಾಡಿ, ಗುರುಗಳಲ್ಲಿ ಅವರಿಗೆ ದಕ್ಷಿಣೆಗಳನ್ನ ಕೊಟ್ಟು, ಗುರುಗಳಿಗೆ ಸಮರ್ಪಣೆ ಮಾಡಿ ಅವರಿಂದ ಆಶೀರ್ವಾದಗಳನ್ನ ಪಡೆಯಬೇಕು ಅಂತ. ವಿಜಯದಶಮಿಯ ಆಚರಣೆ ಇಷ್ಟೇ. ಸೋ,','Giving on this day especially yields merit a crore times over. Materials, fragrant materials and clothing—with these, please the acharyas and Brahmins. Please them with dakshina. This is stated in a text called Smriti Muktavali. Above all, remember your teachers—your teachers—give them dakshina, offer it to the teachers and receive their blessings. This is the observance of Vijayadashami. So,')

s=sec('children-resume-learning','Children resume reading after dismissal','The closing household instruction connects Saraswati dismissal with children’s learning and flourishing understanding.','After Saraswati dismissal on Vijayadashami, ask the children to read one or two letters; hear the speaker’s wishes for their learning.')
A(s,354.4,372.08,'ವಿಜಯದಶಮಿ ದಿನ ಸರಸ್ವತಿಯನ್ನ ವಿಸರ್ಜನೆ ಮಾಡಿ, ಒಂದು ಎರಡು ಅಕ್ಷರಗಳನ್ನ ಮಕ್ಕಳನ್ನ ಓದು ಅಂತ ಹೇಳಿರಿ. ಮಕ್ಕಳಿಗೆಲ್ಲ ವಿಶೇಷವಾಗಿ ವಿದ್ಯಾಭ್ಯಾಸಗಳು, ಮೇಧಾವಿಲಾಸಗಳು ಎಲ್ಲವೂ ಕೂಡ ಬರಲಿ ಅಂತ.','On Vijayadashami day, dismiss Saraswati and ask the children to read one or two letters. May all the children especially gain learning and the flourishing of intelligence.')
M(s,372.08,373.52,'ವಿಜಯೋ ನಾಮ ಕಾಲೋಯಂ.',[
('vijayō nāma kālōyaṃ.','This time is called Vijaya [recalled as the speaker resumes his blessing].','Vijaya, victory~by name or called~this time (kālaḥ + ayam)',372.08,373.52)
],['The captions compress the quoted recall into vijayaganāma kālō; fine GPT gives vijayanāma kālōyaṃ. This short recall is preserved, not expanded into the earlier verse.'])

s=sec('closing-blessings','Concluding blessings and thanks','The speaker prays to Hari, Vayu and the gurus for knowledge, devotion, detachment, health, prosperity and household welfare.','Hear the concluding wishes and Sri Krishna dedication; the source prescribes no additional physical action here.')
A(s,373.52,411.12,'ಎಲ್ಲ ಕಾರ್ಯಗಳು ಸಿದ್ಧಿಯಾಗಲಿ. ಒಳ್ಳೆ ಮೇಧಾವಿಲಾಸ, ವಿದ್ಯಾವಿಲಾಸಗಳು ನಿಮಗೆಲ್ಲರಿಗೂ ಕೂಡ, ಜ್ಞಾನ ಭಕ್ತಿ ವೈರಾಗ್ಯ ಬರಲಿ, ಆಯುರಾರೋಗ್ಯ ಐಶ್ವರ್ಯ ಇರಲಿ, ಅನಂತ ಕಲ್ಯಾಣಗಳು ಮನೆಯಲ್ಲಿ ತುಂಬಿ ಬರಲಿ ಅಂತ ಹರಿವಾಯು ಗುರುಗಳನ್ನ ನಾನು ಪ್ರಾರ್ಥನೆಯನ್ನು ಮಾಡಿ ನಿಮಗೆಲ್ಲರಿಗೂ ಈ ದಸ ದಸರಾ ವಿಜಯದಶಮಿಯ ಶುಭಾಶಯಗಳನ್ನ ನಿಮಗೆಲ್ಲರಿಗೂ ಕೂಡ ತಿಳಿಸುತ್ತೇವೆ. ಎಲ್ಲರಿಗೂ ಹ್ಯಾಪಿ ವಿಜಯದಶಮಿ. ಎಲ್ಲ ಕಾರ್ಯಗಳು ವಿಜಯವಾಗಲಿ ಅಂತ ನಿಮ್ಮೆಲ್ಲರಿಗೂ ಆಶೀರ್ವಾದಗಳನ್ನ ಹರಿವಾಯು ಗುರುಗಳಿಂದ ಮಾಡಿಸ್ತಾ ಇದ್ದೇವೆ.','May all undertakings succeed. May fine intelligence and learning flourish for all of you; may knowledge, devotion and detachment come to you. May you have longevity, health and prosperity, and may countless auspicious blessings fill your homes. With these wishes, I pray to Hari, Vayu and the gurus and convey to all of you these Das—Dasara Vijayadashami greetings. Happy Vijayadashami to everyone. We are seeking blessings for all of you from Hari, Vayu and the gurus, that all your undertakings may be victorious.')
M(s,411.12,412.16,'ಶ್ರೀಕೃಷ್ಣಾರ್ಪಣ.',[
('śrīkṛṣṇārpaṇa.','An offering to Sri Krishna [the audible short dedication is retained].','dedication or offering to Sri Krishna (śrīkṛṣṇa + arpaṇa)',411.12,412.16)
])
A(s,412.16,416.612438,'ಎಲ್ಲರಿಗೂ ಎಲ್ಲಾ ಒಳ್ಳೆದುಗಳು ಆಗಲಿ. ಧನ್ಯವಾದ.','May every good thing come to everyone. Thank you.')

for s in sections:
 s['startSeconds']=s['structuredBlocks'][0]['startSeconds'];s['endSeconds']=s['structuredBlocks'][-1]['endSeconds'];s['originalScript']=''.join(b['sourceOriginal'] for b in s['structuredBlocks'])
 s['guidanceReferences']={k:[{'sourceId':'visarjana','segmentId':b['segmentId'],'startSeconds':b['startSeconds'],'endSeconds':b['endSeconds'],'basis':'Supplementary editorial guidance drawn from the retained spoken '+('instruction/explanation' if b['kind']=='action' else 'prayer')+'.'} for b in s['structuredBlocks']] for k in ['contemplate','action']}
 s['type']='mixed' if any(b['kind']=='mantra' for b in s['structuredBlocks']) else 'instruction'
# Source timings come only from embedded VTT markers; the final cue exceeds actual media length and is bounded by measured duration.
source=''.join(s['originalScript'] for s in sections)
(D/'sections.json').write_text(json.dumps(sections,ensure_ascii=False,indent=2))
(D/'complete-source.txt').write_text(source)
(D/'complete-roman.txt').write_text(''.join(b['sourceRoman'] for s in sections for b in s['structuredBlocks']))
(D/'uncertainty-inventory.json').write_text(json.dumps(uncertainties,ensure_ascii=False,indent=2))
(D/'evidence-manifest.json').write_text(json.dumps({'sources':[{'id':'visarjana','url':'https://youtube.com/watch?v=cw2W5gl6Low','durationSeconds':416.612438,'originalScript':source}],'segments':segments},ensure_ascii=False,indent=2))
(D/'aligned-segments.json').write_text(json.dumps(segments,ensure_ascii=False,indent=2))
print(len(sections),'sections',len(segments),'blocks',len(source),'source characters')
