import pathlib,json,re,unicodedata,difflib
R=pathlib.Path(__file__).resolve().parent
prior=R.parents[2]/'navaratri-nanda-deepa/vidhi/reconciled/build_sections.py'
scope={'__file__':str(prior)};exec(prior.read_text().split("s=sec('opening-invocation')")[0],scope)
roman_kn=scope['roman_kn'];WORDS=scope['WORDS'].copy();NAMES=scope['NAMES'];DURATION=1613.763628
EVENTS=json.load(open(R.parent/'captions/native-word-events.json'))['events'];EVENTS=[e for e in EVENTS if e['start']<DURATION]
for e in EVENTS:e['end']=min(e['end'],DURATION)
S=[];UNKNOWN=[]
def vocab(text):
 for row in text.splitlines():
  if '=' in row:
   k,v=row.split('=',1);WORDS[k.strip()]=v.strip()
def at(word,near):
 candidates=[e for e in EVENTS if e['raw_word'].startswith(word) and abs(e['start']-near)<15]
 if not candidates:raise ValueError(('No native anchor',word,near))
 return min(candidates,key=lambda e:abs(e['start']-near))['start']
def sec(slug,title,group):
 s={'id':f'P{len(S)+1:02}','slug':slug,'title':title,'group':group,'sourceId':'puja','type':'mixed','structuredBlocks':[],'verify':True,'verifyNotes':'Text reconciled using native captions and acoustic model witnesses; no direct human listening claimed. Exact uncertain readings listed in block notes. Historical dates belong to the2025 recording.'};S.append(s);return s
def gloss(text,meanings):
 lines=[];i=0
 for row in text.splitlines():
  if not row.strip():lines.append(None);continue
  if i>=len(meanings):raise ValueError(('Meanings missing',row))
  words=[]
  for token in row.split():
   key=token.strip('.,;:।॥[]');meaning=WORDS.get(key)
   if meaning is None:UNKNOWN.append(key);meaning='READING_REVIEW:'+key
   words.append({'text':token,'meaning':meaning})
  lines.append({'text':row,'meaning':meanings[i],'words':words});i+=1
 assert i==len(meanings),(text,meanings)
 return {'lines':lines,'attribution':'Editorial Sanskrit line translation and lexical analysis; not spoken English'}
def M(s,word,near,text,meaning,note=''):
 means=meaning if isinstance(meaning,list) else [meaning]
 s['structuredBlocks'].append({'kind':'mantra','startSeconds':at(word,near),'text':text+'\n\n','sourceOriginal':text+'\n','sourceRoman':text+'\n','gloss':gloss(text,means),'notes':note,'timingStatus':'Start at actual native VTT word marker matched to the stated phrase; interval ends at the next spoken block marker. No artificial subdivisions.'})
def A(s,word,near,original,english,note=''):
 s['structuredBlocks'].append({'kind':'action','startSeconds':at(word,near),'sourceOriginal':original+'\n','sourceRoman':roman_kn(original)+'\n','english':english,'notes':note,'timingStatus':'Start at actual native VTT word marker matched to Kannada phrase; interval ends at the next spoken block marker.'})
def G(s,c,a):s['contemplate']=c;s['action']=a
vocab('''jambūdvīpe=in Jambūdvīpa
vaiśvavasunāma=named Viśvāvasu
saṁvatsara=the year
śarat=autumn
ṛtau=in the season
aṣṭamyāṁ=on the eighth lunar day
bhaumavāsara=Tuesday
pūrvāṣāḍhānakṣatra=the Pūrvāṣāḍhā lunar mansion
sarasvatyantargata=indwelling in Sarasvatī
śrīvedavyāsa=Śrī Vedavyāsa
mama=my; for me
sarvaśāstrārtha=the meaning of all scriptures
vijñānādi=knowledge and the other attainments
sarvābhīṣṭa=all desired aims
siddhi=accomplishment
dvāra=through; by means of
sarasvatīātmaka=having Sarasvatī as his form
pūjāṁ=worship
navarātriutsavāṅga=as part of the Navarātri festival
aṣṭamīdivase=on the day of Aṣṭamī
kapilāya=to Kapila
kapilam=Kapila as object of invocation
dattātreyāya=to Dattātreya
dattātreyam=Dattātreya as object of invocation
hayagrīvāya=to Hayagrīva
hayagrīvam=Hayagrīva as object of invocation
rāmāya=to Rāma
rāmam=Rāma as object of invocation
kṛṣṇāya=to Kṛṣṇa
kṛṣṇam=Kṛṣṇa as object of invocation
paraśurāmāya=to Paraśurāma
paraśurāmam=Paraśurāma as object of invocation
vedavyāsam=Vedavyāsa as object of invocation
nārāyaṇam=Nārāyaṇa as object of invocation
śriyai=to Śrī, Lakṣmī
mahālakṣmīm=Mahālakṣmī
bhūdevīm=Bhūdevī, the Earth goddess
prāṇam=Prāṇa, the life deity
sarasvatīm=Sarasvatī
bhāratīm=Bhāratī
śeṣam=Śeṣa
pārvatīm=Pārvatī
vināyakam=Vināyaka, Gaṇeśa
sakalaṛṣigaṇaṁ=all the groups of seers
siddhapuruṣaṁ=the perfected beings
munigaṇaṁ=the groups of sages
abhraṁ=cloudless; pure
bhaṅgarahitaṁ=free from division; reading uncertain
ajam=unborn
vimalaṁ=spotless
sadā=always
ānandatīrthaṁ=Ānandatīrtha
gurum=the guru
vicitram=wondrous
gambhīraiḥ=profound
vākyaiḥ=with statements
mānair=with authorities or proofs
akhaṇḍitaiḥ=unbroken; incontrovertible
gurubhāvaṁ=the greatness or status of the guru
vyañjayantī=manifesting
pāti=protects
śrījayatīrthavāk=the speech of Śrī Jayatīrtha
jayatīrtha=Jayatīrtha
atyakalpitakalpaṁ=exceedingly abundant wish-granting tree; reading uncertain
pratyarthigajakesari=lion to the elephant-like opponents
vyāsatīrtha=Vyāsatīrtha
gurur=guru
bhūyāt=may be
vyāsarāja=Vyāsarāja
praṇamatkāmadhenum=wish-fulfilling cow for those who bow
bhajatāṁ=for the worshippers
suratarūpam=like the heavenly wish-granting tree
śrībhāvabodhakṛtpādaṁ=the revered author of the Bhāvabodha; Raghūttama Tīrtha
cintāmaṇim=the wish-granting jewel
upāsmahe=we worship
raghūttamatīrtha=Raghūttama Tīrtha
durvādidvāntaravaye=to the sun dispelling the darkness of errant disputants
vaiṣṇavendīvarendave=to the moon that nourishes the lotus of Vaiṣṇavas
śrīrāghavendragurave=to the revered guru Rāghavendra
namo’stu=may there be salutation
atyantadayālave=to the exceedingly compassionate one
śrīrāghavendra=Śrī Rāghavendra
ānandatīrthādi=Ānandatīrtha and the other gurus
samasta=all
gurumaṇḍala=the assembly of gurus
devatān=the divine beings
atrāgatya=having come here
jagadvandye=O revered by the world
sarvalokaikapūjite=O uniquely worshipped by all worlds
mayā=by me
kṛtām=performed
imāṁ=this
pūjāṁ=worship
gṛhāṇa=accept
tvam=you
sarasvati=O Sarasvatī
praṇavāsanārūḍhāṁ=seated upon the seat of Praṇava, Oṁ
tadarthatattvena=through the truth of its meaning
niścitām=firmly established
aṅkuśaṁ=an elephant goad
akṣasūtraṁ=a rosary
pāśapustakadhāriṇīṁ=bearing a noose and book
keyūrair=with armlets
mekhalādyair=with a girdle and other ornaments
dyotayantīṁ=illuminating
jagattrayaṁ=the three worlds
saptabrahmaraṇīṁ=the lady of the seven sacred utterances; technical epithet, reading uncertain
dhyāyet=one should meditate upon
dhyānagamyāṁ=attainable through meditation
samāhitaḥ=with a concentrated mind
bhāratīṁ=Bhāratī
sarvavedyāṁ=knowable through all scriptures; reading uncertain
bharturaṅkasthitāṁ=seated on her husband’s lap
satīṁ=the faithful goddess
dhyāyantīṁ=meditating upon
satataṁ=continually
viṣṇuṁ=Viṣṇu
dhyāyet=one should meditate upon
sarvārthadāṁ=giver of all aims or blessings
sahasraśīrṣā=thousand-headed
puruṣaḥ=the cosmic Person
sahasrākṣaḥ=thousand-eyed
sahasrapāt=thousand-footed
sa=he
bhūmiṁ=the Earth
viśvato=on every side
vṛtvā=having encompassed
atyatiṣṭhat=extended beyond
daśāṅgulaṁ=by ten finger-breadths
sarasvatyantaryāmi=the inner ruler of Sarasvatī
anekaratnasaṁyuktaṁ=adorned with many jewels
suvarṇena=with gold
virājitam=shining
muktāmaṇyaṅkitaṁ=studded with pearls and gems
cāru=beautiful
āsanaṁ=a seat
te=to you; your
dadāmyaham=I give
puruṣa=the cosmic Person; word joined in recitation
evedaṁ=alone is this
sarvaṁ=everything
yadbhūtaṁ=what has been
yacca=and what
bhavyaṁ=is yet to be
utāmṛtatvasyeśāno=and the lord of immortality
yadannenātirohati=who grows beyond through food; joined recitation
gandhapuṣpākṣatayuktaṁ=accompanied by fragrance, flowers and akṣata
gandhatoyena=with fragrant water
saṁyutam=combined
śuddhasphaṭikatulyāṅgi=O goddess whose body resembles pure crystal
pādyaṁ=water for washing the feet
etāvānasya=so great is his
mahimā=greatness
ato=greater than this
jyāyāṁśca=and still greater
pādo’sya=one quarter of him
viśvā=all
bhūtāni=beings
tripādasyāmṛtaṁ=his three quarters are immortal
divi=in heaven
bhaktābhīṣṭaprade=O giver of devotees’ desired blessings
devi=O goddess
devadevādivandite=O revered by the gods and their lords
ādhārādijagaddhātri=O sustainer of the world and its foundations
dadāmyarghyaṁ=I give honorary welcoming water
tripādūrdhva=three quarters above
udait=rose
puruṣaḥ=the cosmic Person
pādo’syehābhavatpunaḥ=one quarter of him became this world again
tato=from that
viṣvaṅ=everywhere
vyakrāmat=spread out
sāśanānaśane=among those who eat and those who do not
abhi=toward; throughout
pūrṇacandrasamānāsye=O goddess whose face resembles the full Moon
koṭisūryasamaprabhe=O goddess with the radiance of ten million suns
bhaktyā=with devotion
samarpitaṁ=offered
tubhyaṁ=to you
ācamanīyakam=water for sipping
tasmād=from him; from that
virāḍ=Virāj, the manifested cosmic form
ajāyata=was born
virājo=from Virāj
adhi=from; above
sajāto=he, once born
atyaricyata=extended beyond
paścād=behind
bhūmim=the Earth
atho=and then
puraḥ=in front
kamalabhavanajāye=O consort of the lotus-born Brahmā
koṭisūryaprakāśe=O radiant as ten million suns
śivadaśucivilāse=O pure radiance that grants auspiciousness
komale=O tender one
hārayukte=O adorned with necklaces
dadhimadhughṛtayuktaṁ=containing curd, honey and ghee
svarṇapātrasthitaṁ=placed in a golden vessel
suśri=O beautiful one; exact recited form uncertain
madhuparkaṁ=the curd-honey-ghee offering
vedavedye=O known through the Vedas
dadhi=curd
kṣīra=milk
ghṛtaṁ=ghee
śarkarā= sugar
madhusaṁyutaṁ=mixed with honey
pañcāmṛtasnānaṁ=bathing with the five nectars
śrīguru=the revered guru
sureśvari=O queen of the gods
suvarṇakalaśānītaṁ=brought in a golden pot
nānāgandhasuvāsitam=perfumed with various fragrances
gandhodakaṁ=fragrant water
nirmitaṁ=prepared
yatpuruṣeṇa=when, with the cosmic Person
haviṣā=as the oblation
devā=the gods
yajñam=the sacrifice
atanvata=performed
vasanto=the spring season
asyāsīdājyaṁ=was its ghee
grīṣma=summer
idhmaḥ=the fuel
śaraddhaviḥ=autumn was the oblation
śuddhodaka=with pure water
snānaṁ=bath
śuklavastradvayaṁ=two white garments
amalāni=spotless; exact form uncertain
kuṭilālake=O goddess with curling locks
vāṇi=O Vāṇī, goddess of speech
brahmāṇi=O consort of Brahmā
pratigṛhyatām=may it be accepted
taṁ=that
yajñaṁ=sacrifice
barhiṣi=on the sacred grass
praukṣan=they sprinkled
puruṣaṁ=the cosmic Person
jātam=born
agrataḥ=at the beginning
tena=with him
devā=the gods
ayajanta=performed sacrifice
sādhyā=the Sādhya deities
ṛṣayaśca=and the seers
vastrayugmaṁ=the pair of garments
saptabrahmaraṇe=O lady of the seven sacred utterances; epithet uncertain
saptaśāstrakṛtālaye=O abode/author of seven scriptures; reading uncertain
kaṇṭhasūtraṁ=the neck thread or necklace
gṛhāṇa=accept
śeṣaśakrādipūjite=O worshipped by Śeṣa, Śakra and other deities
mukuṭahāraiḥ=with crowns and necklaces
nūpurair=with anklets
aṅgadādyaiḥ=with armlets and other ornaments
vividhamanisaṁyuktair=adorned with various jewels
mekhalāmuktahāraiḥ=with girdles and pearl necklaces
kamalavanavilāse=O sporting in the lotus grove
kāmade=O giver of desired blessings
gṛhāṇa=accept
prakaṭitakaruṇārte=O manifestly compassionate one; exact compound uncertain
bhūriśobhūṣaṇāni=many shining ornaments; exact spoken compound uncertain
tasmādyajñātsarvahutaḥ=from that sacrifice in which all was offered
sambhṛtaṁ=collected
pṛṣadājyaṁ=curd mixed with ghee
paśūn=animals
tāṁś=certain ones
cakre=created
vāyavyān=of the air
āraṇyān=of the forest
grāmyāśca=and of the village
yē=which
ābharaṇāni=ornaments
candanāgarukastūrī=sandal, agaru and musk
karpūrādyaiḥ=with camphor and the other fragrances
gandhaṁ=fragrant paste
vidhipatni=O consort of Brahmā
ṛcaḥ=the Ṛg verses
sāmāni=the Sāman chants
jajñire=were born
chandāṁsi=the meters
yajus=the Yajur formulas
tasmādajāyata=were born from that
akṣatān=unbroken consecrated grains
dhavalān=white
divyān=divine
śālitaṇḍulamiśritān=of or mixed with rice grains
gṛhāṇa=accept
varade=O giver of blessings
śubhākṣatān=auspicious akṣata
haridrā=turmeric
kuṅkumaṁ=kumkum
gandhacūrṇādikānapi=fragrant powders and other such offerings
dāsyāmi=I shall give
parayā=with supreme
bhaktyā=devotion
aśvā=horses
ajāyanta=were born
ye=which
ke=any
cobhaya=and both
dataḥ=having teeth
gāvo=cows
ha=indeed
tasmājjātā=born from him
ajā=goats
avayaḥ=sheep
nandhyāvartādipuṣpaiśca=with nandhyāvarta and other flowers
kalhāraiḥ=with water lilies
mallikādibhiḥ=with jasmine and other flowers
karavīraiḥ=with oleanders
jāti=the jāti jasmine
kusumaiḥ=with flowers
mandāraiśca=and with mandāra flowers
manoramaiḥ=pleasing
nīlotpalaiśca=and with blue lotuses
kamalaiḥ=with lotuses
tatkālatarusambhavaiḥ=growing on trees of the season
supuṣpaiśca=and with beautiful flowers
bhaktavatsale=O affectionate toward devotees
nānāvidha=various kinds
puṣpāṇi=flowers
''')
vocab((R/'additional-vocabulary.txt').read_text())

s=sec('prepare','Prepare for Saraswati worship','Preparation')
A(s,'ಸರಸ್ವತಿಯ',1.68,'ಸರಸ್ವತಿಯ ಆವಾಹನ ಪೂಜೆಯನ್ನು ಮೂಲ ನಕ್ಷತ್ರದ ದಿನ ಮಾಡಿದ್ದೇವೆ. ಇವತ್ತು ಸರಸ್ವತಿಯ ಪೂಜೆ. ಬೆಳಿಗ್ಗೆ ನಿಮ್ಮ ಅನುಷ್ಠಾನಗಳೆಲ್ಲ ಮುಗಿಸಿ, ದೇವರ ಪೂಜೆಯನ್ನು ಪೂರ್ಣವಾಗಿ ಮುಗಿಸಿ, ಪೂರ್ವಾಭಿಮುಖ ಅಂದರೆ ಈಸ್ಟ್ ಫೇಸಿಂಗ್ ಅಥವಾ ಉತ್ತರಾಭಿಮುಖ ನಾರ್ತ್ ಫೇಸಿಂಗ್ ಆಗಿ ಕೂತು ಮತ್ತೆ ಆಚಮನ ಮಾಡಿರಿ. ಪೂಜೆಗೆ ಬೇಕಾಗಿರುವ ವಸ್ತುಗಳು ನಿನ್ನೆ ಹೇಳಿದಂತೆ ಅರಿಶಿನ ಕುಂಕುಮ, ಗಂಧ, ಮಂತ್ರಾಕ್ಷತೆ, ಗಜವಸ್ತ್ರ, ವೀಳ್ಯದೆಲೆ ಅಡಿಕೆ, ಹಣ್ಣು ತೆಂಗಿನಕಾಯಿ, ಹೂವುಗಳು, ಊದು ಕಡ್ಡಿ ಕರ್ಪೂರ, ಆರತಿ ತಟ್ಟೆ, ವಸ್ತ್ರ ಇತ್ಯಾದಿಗಳು ಇದನ್ನೆಲ್ಲ ತೆಗೆದಿಟ್ಟುಕೊಳ್ಳಿ. ಹಾಲು ಮೊಸರು ಜೇನು, ಹಾಲು [ವ್ರತ ಎಂಬ ಶಬ್ದ — ಅಸ್ಪಷ್ಟ], ಮೊಸರು ಜೇನು ತುಪ್ಪ ಮಧುಪರ್ಕಕ್ಕೆ, ಮೊಸರು ಜೇನು ತುಪ್ಪ ಸಕ್ಕರೆ ಪಂಚಾಮೃತ. ಇದನ್ನು ತೆಗೆದಿಟ್ಟುಕೊಂಡು ಎಲ್ಲವನ್ನೂ ಸಿದ್ಧಪಡಿಸಿಟ್ಟುಕೊಂಡು ದೀಪವನ್ನೆಲ್ಲ ಹಚ್ಚಿ. ಇವತ್ತು ಮಕ್ಕಳ ಸ್ಕೂಲ್ ಪುಸ್ತಕಗಳಿರುತ್ತವೆ, ಅವನ್ನೂ ಸಹಿತ ಇಟ್ಟು ಪೂಜೆಯನ್ನು ಮಾಡಬೇಕು.','We performed Saraswati invocation and worship on the day of Mula nakshatra. Today is Saraswati worship. In the morning, finish all your regular observances and complete your deity worship. Sit facing east—east facing—or north—north facing—and perform ācamana again. As explained yesterday, set out the things needed for worship: turmeric and kumkum, sandal paste, mantra-akṣata, gajavastra cloth, betel leaves and areca nut, fruit and coconut, flowers, incense sticks and camphor, an ārati plate, cloth and the other items. Milk, curd and honey; milk [the following word is unclear]; curd, honey and ghee for madhuparka; curd, honey, ghee and sugar for pañcāmṛta. Set these out, have everything ready and light the lamps. Today you should also place the children’s schoolbooks there and worship them along with the other books.','Ingredient lists repeated/partially restarted as spoken. Exact word after second milk mention uncertain across GPT/captions; no fifth ingredient silently added to the spoken four-item pañcāmṛta list. Historical earlier Mula day belongs to recording.')
G(s,'Attend to the stated continuity between earlier invocation and today’s worship.','Finish your regular morning observances, face east or north, set out the listed materials, light the lamps and include the children’s schoolbooks.')
s=sec('acamana','Acamana','Preparation')
A(s,'ಆಚಮನ',75.52,'ಆಚಮನ.','Ācamana.')
short='govinda viṣṇu madhusūdana trivikrama vāmana\nśrīdhara hṛṣīkeśa padmanābha dāmodara saṅkarṣaṇa\nvāsudeva pradyumna aniruddha puruṣottama adhokṣaja\nnārasimha acyuta janārdana upendra haraye namaḥ śrīkṛṣṇāya namaḥ'
M(s,'ಕೇಶವಾಗ',77.52,'keśavāya svāhā\nnārāyaṇāya svāhā\nmādhavāya svāhā\n'+short,['An offering to Keśava.','An offering to Nārāyaṇa.','An offering to Mādhava.','Govinda, Viṣṇu, Madhusūdana, Trivikrama and Vāmana.','Śrīdhara, Hṛṣīkeśa, Padmanābha, Dāmodara and Saṅkarṣaṇa.','Vāsudeva, Pradyumna, Aniruddha, Puruṣottama and Adhokṣaja.','Nārasiṁha, Acyuta, Janārdana and Upendra; salutation to Hari and Śrī Kṛṣṇa.'],'Short names after first three retained as heard; not expanded into unspoken full datives.')
G(s,'Attend to the divine names in the ācamana.','Perform the recorded ācamana sequence.')
s=sec('pranayama','Pranayama','Preparation')
A(s,'ಪ್ರಾಣಾಯಾಮ',103.119,'ಪ್ರಾಣಾಯಾಮ. ಮೂಗನ್ನು ಹಿಡುಕೊಳ್ಳೋದು.','Prāṇāyāma. Hold the nose.')
M(s,'ಪ್ರಣಶ',105,'praṇavasya parabrahma ṛṣiḥ paramātmā devatā\ndevī gāyatrī chandaḥ prāṇāyāme viniyogaḥ\noṁ bhūḥ oṁ bhuvaḥ oṁ svaḥ oṁ mahaḥ oṁ janaḥ oṁ tapaḥ oṁ satyaṁ\ntatsaviturvareṇyaṁ bhargo devasya dhīmahi dhiyo yo naḥ pracodayāt\noṁ āpo jyotīraso amṛtaṁ brahma bhūrbhuvassuvarom',['For Praṇava, the Supreme Brahman is the seer and the Supreme Self is the deity.','The meter is Devī Gāyatrī; its application is in prāṇāyāma.','Oṁ: earth, the intermediate world, heaven, the great world, the world of beings, austerity and truth.','We meditate on the excellent purifying radiance of the divine Savitṛ; may he inspire our intellects.','Oṁ: waters, light, essence, immortality and Brahman; earth, intermediate world, heaven and Oṁ.'])
G(s,'Meditate on the divine radiance that inspires understanding.','Hold the nose and follow the recorded prāṇāyāma recitation.')
s=sec('sankalpa','Sankalpa','Intention')
A(s,'ಎಡಗೈಯಲ್ಲಿ',128,'ಎಡಗೈಯಲ್ಲಿ ಸ್ವಲ್ಪ ಮಂತ್ರಾಕ್ಷತೆಯನ್ನು ಹಾಕಿ, ಎಡಗೈ ಮೇಲೆ ಬಲಗೈಯನ್ನು ಮುಚ್ಚಿಟ್ಟುಕೊಂಡು ಬಲದ ತೊಡೆಯಲ್ಲಿ ಇಟ್ಟುಕೊಂಡು ಸಂಕಲ್ಪವನ್ನು ಮಾಡಿಕೊಳ್ಳಿ.','Put a little mantra-akṣata in the left hand. Cover the left hand with the right hand, rest them on the right thigh and make the saṅkalpa.')
M(s,'ಶುಭ',136,'śubhe śobhane muhūrte ādya brahmaṇaḥ dvitīya parārdhe\nśrīśvetavarāhakalpe vaivasvatamanvantare kaliyuge prathamapāde\njambūdvīpe bharatavarṣe bharatakhaṇḍe daṇḍakāraṇye godāvaryāḥ dakṣiṇapārśve\nśālivāhanaśake bauddhāvatāre rāmakṣetre asmin vartamāne prabhavādi ṣaṣṭi saṁvatsarāṇāṁ madhye\nśubha vaiśvavasunāma saṁvatsare dakṣiṇāyane śaradṛtau āśvījamāse śuklapakṣe aṣṭamyāṁ\nvāsaraḥ vāsarastu bhaumavāsara yuktāyāṁ pūrvāṣāḍhānakṣatra yuktāyāṁ\nśubhanakṣatra śubhayoga śubhakaraṇa evaṁguṇa sakalaviśeṣaṇa viśiṣṭāyāṁ śubhatithau\nbhāratīramaṇa mukhyaprāṇāntargata śrī sarasvatyantargata śrīvedavyāsa preraṇayā śrīvedavyāsa prītyarthaṁ mama',['At this auspicious, splendid moment, in the second half of Brahmā’s lifetime,','In the Śvetavarāha kalpa, Vaivasvata manvantara, Kali age, first quarter,','In Jambūdvīpa, Bharatavarṣa, Bharatakhaṇḍa, Daṇḍakāraṇya, on the southern side of the Godāvarī,','In the Śālivāhana era, Buddha incarnation period, Rāmakṣetra, in the present sixty-year cycle beginning with Prabhava,','In the auspicious year named Viśvāvasu, southern course of the Sun, autumn, Āśvīja month, bright fortnight, Aṣṭamī,','The weekday—the weekday being Tuesday—joined with the Pūrvāṣāḍhā lunar mansion,','On the auspicious lunar day qualified by the auspicious star, yoga, karaṇa and all these attributes,','By the prompting of Śrī Vedavyāsa indwelling in Sarasvatī and in Mukhyaprāṇa, the consort of Bhāratī, for the pleasure of Śrī Vedavyāsa, for me—'],'Year Viśvāvasu recovered directly by independent targeted149–165 acoustic transcription, resolving the fine ASR/caption corruption. Recorded place/date must not become current date instructions.')
A(s,'ಅಂತ',189,'ಅಂತ ಹೇಳಿಕೊಳ್ಳಿರಿ.','Say it in this way.')
M(s,'ಮಮ',191.04,'mama sarvaśāstrārtha vijñānādi sarvābhīṣṭa siddhi dvāra\nsarasvatyantargata bhāratīramaṇa mukhyaprāṇāntargata śrīvedavyāsa preraṇayā vedavyāsa prītyarthaṁ\nsarasvatīātmaka śrīvedavyāsa pūjāṁ navarātriutsavāṅga aṣṭamīdivase sarasvatī pūjāṁ',['For my attainment of knowledge of all scriptural meanings and all other desired aims,','By the prompting of Śrī Vedavyāsa indwelling in Sarasvatī and in Mukhyaprāṇa, Bhāratī’s consort, for the pleasure of Vedavyāsa,','I intend Sarasvatī worship on Aṣṭamī as part of the Navarātri festival: worship of Śrī Vedavyāsa having Sarasvatī as his form.'],'The Sanskrit object is interrupted by the water instruction before final kariṣye, preserved below.')
A(s,'ಮಂತ್ರಾಸ್ತ',218,'ಮಂತ್ರಾಕ್ಷತೆ ನೀರು ಹಾಕಿ ಪೇಲಾಲಿ ಬಿಡಿರಿ.','Add water to the mantra-akṣata and release it into the bowl.')
M(s,'ಕರಿಶೆ',221.68,'kariṣye','I shall perform it.')
G(s,'Attend to the intention for understanding scripture and attaining the stated aims through Sarasvatī worship.','Hold mantra-akṣata as instructed, recite the recorded intention and release water when directed; review historical date and place examples.')
s=sec('deity-invocation','Invoke the deities in the book mandala','Invocation')
A(s,'ಮಂತ್ರಾಸ್ತೆ',224.319,'ಮಂತ್ರಾಕ್ಷತೆಯನ್ನು ತೊಕೊಂಡು ನಿನ್ನೆ ಪೂಜೆ ಮಾಡಿರುವ ಪುಸ್ತಕ ಮಂಡಲಕ್ಕೆ ಮತ್ತೆ ಪೂಜೆಯನ್ನು ಮಾಡಿರಿ.','Take mantra-akṣata and worship again the book mandala that was worshipped yesterday.')
M(s,'ಕಪಿಲಾಯ',229.519,'kapilāya namaḥ kapilam āvāhayāmi\ndattātreyāya namaḥ dattātreyam āvāhayāmi\nhayagrīvāya namaḥ hayagrīvam āvāhayāmi\noṁ rāmāya namaḥ rāmam āvāhayāmi\noṁ kṛṣṇāya namaḥ kṛṣṇam āvāhayāmi\noṁ paraśurāmāya namaḥ paraśurāmam āvāhayāmi\nvedavyāsāya namaḥ vedavyāsam āvāhayāmi\nnārāyaṇāya namaḥ nārāyaṇam āvāhayāmi\nśriyai mahālakṣmīm āvāhayāmi bhūdevīm āvāhayāmi durgāṁ āvāhayāmi\nmukhya prāṇam āvāhayāmi sarasvatīm āvāhayāmi bhāratīm āvāhayāmi',['Salutation to Kapila; I invoke Kapila.','Salutation to Dattātreya; I invoke Dattātreya.','Salutation to Hayagrīva; I invoke Hayagrīva.','Oṁ, salutation to Rāma; I invoke Rāma.','Oṁ, salutation to Kṛṣṇa; I invoke Kṛṣṇa.','Oṁ, salutation to Paraśurāma; I invoke Paraśurāma.','Salutation to Vedavyāsa; I invoke Vedavyāsa.','Salutation to Nārāyaṇa; I invoke Nārāyaṇa.','To Śrī: I invoke Mahālakṣmī, Bhūdevī and Durgā.','I invoke Prāṇa, Sarasvatī and Bhāratī.'],'mukhya recovered from independent coarse acoustic witness; fine bhoktya/caption corruption retained in provenance, not discarded.')
A(s,'ಮಂತ್ರಸ್ತೆ',268,'ಮಂತ್ರಾಕ್ಷತೆಯನ್ನು ಹಾಕ್ತಾ ಬನ್ನಿರಿ.','Keep offering mantra-akṣata as you go.')
M(s,'ಭಾರತಿಮ',269.919,'bhāratīm āvāhayāmi śeṣam āvāhayāmi\nrudram āvāhayāmi pārvatīm āvāhayāmi vināyakam āvāhayāmi\nsakalaṛṣigaṇaṁ siddhapuruṣaṁ munigaṇaṁ āvāhayāmi',['I invoke Bhāratī and Śeṣa.','I invoke Rudra, Pārvatī and Vināyaka.','I invoke all the groups of seers, perfected beings and sages.'],'Bhāratī invocation repeated across real Kannada interruption; preserve both occurrences. Collective singular/plural endings differ in acoustic ASR.')
G(s,'Attend to the complete assembly of deities and sages named for the book mandala.','Offer mantra-akṣata with each recorded invocation, including repeated Bhāratī invocation after the instruction.')
s=sec('guru-invocation','Invoke the gurus','Invocation')
A(s,'ಅಂತರಾಸ್ತ',283.759,'ಮಂತ್ರಾಕ್ಷತೆಯನ್ನು ತೊಕೊಂಡು, ನಮ್ಮ ಆಚಾರ್ಯರುಗಳು.','Take mantra-akṣata. Our teachers:')
M(s,'ಅಬ್ರಹ್ಮ',286.479,'abhramaṁ bhaṅgarahitaṁ ajaḍaṁ vimalaṁ sadā\nānandatīrtham atulaṁ bhaje tāpatrayāpahaṁ\nānandatīrtha gurum āvāhayāmi\ncitraiḥ padaiśca gambhīraiḥ vākyaiḥ mānair akhaṇḍitaiḥ\ngurubhāvaṁ vyañjayantī bhāti śrījayatīrthavāk\njayatīrtha gurum āvāhayāmi\narthikalpitakalpo’yaṁ pratyarthigajakesarī\nvyāsatīrtha gurur bhūyāt asmad iṣṭārthasiddhaye\nvyāsarāja gurum āvāhayāmi\npraṇamatkāmadhenum ca bhajatsuratarūpamam\nśrībhāvabodhakṛtpādaṁ cintāmaṇim upāsmahe\nraghūttamatīrtha gurum āvāhayāmi\ndurvādidvāntaravaye vaiṣṇavendīvarendave\nśrīrāghavendragurave namo’stu atyantadayālave\nśrīrāghavendra gurum āvāhayāmi\nānandatīrthādi samasta gurumaṇḍala devatān āvāhayāmi sthāpayāmi pūjayāmi namaḥ',['I worship the ever spotless one, free from error and division, and free from inertness—','The incomparable Ānandatīrtha, who removes the threefold suffering.','I invoke guru Ānandatīrtha.','With varied words, profound statements and incontrovertible authorities,','The speech of Śrī Jayatīrtha shines, revealing the intent of his guru’s teaching.','I invoke guru Jayatīrtha.','A wish-granting tree for petitioners and a lion to elephant-like opponents—','May guru Vyāsatīrtha grant the accomplishment of our desired aims.','I invoke guru Vyāsarāja.','The wish-fulfilling cow for those who bow and heavenly tree for worshippers—','We worship the revered author of Bhāvabodha as a wish-granting jewel.','I invoke guru Raghūttama Tīrtha.','To the sun dispelling the darkness of errant disputants and the moon nourishing the lotus of Vaiṣṇavas—','Salutation to revered guru Rāghavendra, the exceedingly compassionate one.','I invoke guru Śrī Rāghavendra.','I invoke and establish all the divine gurus beginning with Ānandatīrtha; I worship them; salutation.'],'Raw first-line acoustic ASR ಅಬ್ರಹ್ಮಂ ಬಂಗರಗಿತಂ ಅಜನಂ ವಿಮಲಂ ಶತ retained in guru-open-transcript.json; abhramaṁ (free of error) and ajaḍaṁ (not inert) are corrected display readings supported by primary-book parallel and this recording’s phonetics, still review flagged. Guru verses carry corrupted exact words in both witnesses: first abhramaṁ/ajaḍaṁ/bhaṅgarahitaṁ, Jayatīrtha citraiḥ padaiśca/bhāti corrected from fine phonetics and official Sri Vyasaraja Matha charamaśloka text; Raghūttama ca and bhajatsuratarūpamam recovered against phonetic witnesses and primary Sanskrit-book parallel. Vyāsatīrtha arthikalpitakalpo’yaṁ replaces acoustic attikalpitakalpo’yaṁ with visible review note. These are explicit corrections, not a claim of direct human listening. Do not claim verified standard restoration.')
G(s,'Remember the named gurus and their recorded qualities.','Offer mantra-akṣata with the guru invocations and establishment formula; review the specifically uncertain verse readings.')
s=sec('saraswati-invocation','Invoke Saraswati','Invocation')
A(s,'ಈಗ',340.72,'ಈಗ ಮತ್ತೆ ಹೂ ಮಂತ್ರಾಕ್ಷತೆ ತೊಗೊಳ್ಳಿರಿ.','Now take flowers and mantra-akṣata again.')
M(s,'ಅತ್ರಾಗತ್ಯ',342,'atrāgatya jagadvandye sarvalokaikapūjite\nmayā kṛtām imāṁ pūjāṁ gṛhāṇa tvam sarasvati\nsarasvatīm āvāhayāmi',['Having come here, O revered by the world, worshipped by all worlds,','Accept this worship performed by me, O Sarasvatī.','I invoke Sarasvatī.'])
G(s,'Attend to welcoming Sarasvatī to receive the worship.','Take flowers and mantra-akṣata and recite the invocation.')
s=sec('meditation','Meditation and Vedavyasa invocation','Invocation')
A(s,'ಮತ್ತು',357.28,'ಮತ್ತೆ ಹೂ ಮಂತ್ರಾಕ್ಷತೆ ತೊಗೊಳ್ಳಿರಿ.','Take flowers and mantra-akṣata again.')
M(s,'ಪ್ರಣವಾಸನ',359,'praṇavāsanaṁ\npraṇavāsanārūḍhāṁ tadarthatattvena niścitām\naṅkuśaṁ ca akṣasūtraṁ ca pāśapustakadhāriṇīṁ\nkeyūrair mekhalādyair dyotayantīṁ jagattrayaṁ\nsaptabrahmaraṇīṁ dhyāyet dhyānagamyāṁ samāhitaḥ\nbhāratīṁ sarvavedāḍhyāṁ bharturaṅkasthitāṁ satīṁ\ndhyāyantīṁ satataṁ viṣṇuṁ dhyāyet sarvārthasiddhaye\nsahasraśīrṣā puruṣaḥ sahasrākṣaḥ sahasrapāt\nsa bhūmiṁ viśvato vṛtvā atyatiṣṭhat daśāṅgulaṁ\nsarasvatyantargata vedavyāsam āvāhayāmi',['The seat of Praṇava—','Seated upon Praṇava, established in the truth of its meaning,','Bearing a goad, rosary, noose and book,','With armlets, girdle and other ornaments, illuminating the three worlds,','One should meditate with concentration upon the lady of the seven sacred utterances, attainable through meditation.','One should meditate upon Bhāratī, rich in all Vedic knowledge, faithfully seated upon her husband’s lap,','Continually meditating on Viṣṇu, for the accomplishment of all aims.','The cosmic Person is thousand-headed, thousand-eyed and thousand-footed.','Having encompassed the Earth on every side, he extends ten finger-breadths beyond it.','I invoke Vedavyāsa indwelling in Sarasvatī.'],'Opening praṇavāsana fragment retained before full phrase. Exact saptabrahmaraṇīṁ and sarvavedāḍhyāṁ readings require review; saptabrahmaraṇīṁ is a specific uncertain epithet, not a generic placeholder.')
G(s,'Meditate upon the recorded goddess forms and Vedavyāsa indwelling in Sarasvatī.','Offer the flowers and mantra-akṣata with the complete meditation and invocation.')
s=sec('asana','Offer a seat','Offerings')
A(s,'ಮಂತ್ರಸ್ತ',403.12,'ಮಂತ್ರಾಕ್ಷತೆ ತೊಗೊಳ್ಳಿರಿ.','Take mantra-akṣata.')
M(s,'ಅನೇಕರತ್ನ',405,'anekaratnasaṁyuktaṁ suvarṇena virājitam\nmuktāmaṇyaṅkitaṁ cāru āsanaṁ te dadāmyaham\npuruṣa evedaṁ sarvaṁ yadbhūtaṁ yacca bhavyaṁ\nutāmṛtatvasyeśāno yadannenātirohati\nāsanaṁ samarpayāmi',['I give you a seat adorned with many jewels and shining with gold,','Beautiful and studded with pearls and gems.','The cosmic Person alone is all this: what has been and what is yet to be.','He is also the lord of immortality, who grows beyond through food.','I offer a seat.'])
A(s,'ಅಂತ',424,'ಅಂತ ಮಂತ್ರಾಕ್ಷತೆ ಹಾಕಿರಿ.','Say this and offer mantra-akṣata.')
G(s,'Attend to offering the beautiful seat and the cosmic Person named in the Vedic verse.','Take mantra-akṣata and offer the seat with the recorded verses.')
s=sec('padya','Offer water for the feet','Offerings')
A(s,'ಉದ್ರಣೆಯಿಂದ',426.88,'ಉದ್ದರಣಿಯಿಂದ ನೀವು ಆಚಮನ ಮಾಡಿದ್ದಲ್ಲ, ಬೇರೆ ಒಂದು ನೀರು, ಉದ್ದರಣಿಯಿಂದ ನೀರು ತೊಗೊಳ್ಳಿರಿ.','Use different water from the water with which you performed ācamana; take water with the spoon.','The spoken correction/restart about different water is retained; do not use this as an added separate rule beyond the recorded distinction.')
M(s,'ಗಂಧ',431,'gandhapuṣpākṣatayuktaṁ gandhatoyena saṁyutam\nśuddhasphaṭikatulyāṅgi pādyaṁ te pratigṛhyatām\netāvānasya mahimā ato jyāyāṁśca puruṣaḥ\npādo’sya viśvā bhūtāni tripādasyāmṛtaṁ divi',['Accompanied by sandal fragrance, flowers and akṣata, and combined with fragrant water,','Accept this water for your feet, O goddess whose body resembles pure crystal.','Such is his greatness, yet the cosmic Person is greater still.','All beings are one quarter of him; his three quarters are immortal in heaven.'])
A(s,'ಮೂರು',452,'ಮೂರು ಸಲ ಪೇಲಾಲಿ ನೀರು ಬಿಡಿರಿ.','Release water into the bowl three times.')
M(s,'ಪಾದ್ಯಂ',454.08,'pādyaṁ pādyaṁ pādyaṁ samarpayāmi','Water for the feet—water for the feet—water for the feet: I offer it.','Three actual prompted repetitions corroborated by fine and coarse acoustic witnesses.')
G(s,'Attend to the welcoming water for the goddess’s feet.','Take the specified water and release it three times with the repeated pādya formula.')
s=sec('arghya','Offer welcoming water','Offerings')
A(s,'ಮತ್ತು',456.6,'ಮತ್ತೆ ಉದ್ದರಣಿಯಿಂದ ನೀರು ತೊಗೊಳ್ಳಿರಿ.','Take water with the spoon again.')
M(s,'ಭಕ್ತಭಿಷ್ಠ',459,'bhaktābhīṣṭaprade devi devadevādivandite\nādhārādijagaddhātri dadāmyarghyaṁ gṛhāṇa te\ntripādūrdhva udait puruṣaḥ pādo’syehābhavatpunaḥ\ntato viṣvaṅ vyakrāmat sāśanānaśane abhi',['O goddess granting devotees’ desired blessings, revered by gods and their lords,','Sustainer of the world and its foundations, I give this welcoming water; accept it.','Three quarters of the cosmic Person rose above; one quarter became this world again.','From there he spread everywhere, throughout what eats and what does not.'],'Exact dadāmyarghyaṁ/gṛhāṇa te and viṣvaṅ syllables vary among ASR; full provisional reading flagged.')
A(s,'ಮೂರು',478,'ಮೂರು ಸಲ ಪೇಲಾಲಿ ನೀರು ಬಿಡಿರಿ.','Release water into the bowl three times.')
M(s,'ಅರ್ಮ್ಯಂ',481,'arghyaṁ arghyaṁ arghyaṁ samarpayāmi','Welcoming water—welcoming water—welcoming water: I offer it.','Three repetitions corroborated by fine/coarse GPT despite caption compressing one.')
G(s,'Attend to the goddess as giver of blessings and sustainer of the world.','Take water and make the three welcoming-water offerings.')
s=sec('acamaniya','Offer water for sipping','Offerings')
A(s,'ಮತ್ತು',483,'ಮತ್ತೆ ಉದ್ದರಣಿಯಿಂದ ನೀರು ತೊಕೊಳ್ಳಬಹುದು.','Take water with the spoon again.')
M(s,'ಪೂರ್ಣಚಂದ್ರ',485.44,'pūrṇacandrasamānāsye koṭisūryasamaprabhe\nbhaktyā samarpitaṁ tubhyaṁ gṛhāṇa ācamanīyakam\ntasmād virāḍ ajāyata virājo adhi puruṣaḥ\nsajāto atyaricyata paścād bhūmim atho puraḥ',['O goddess whose face resembles the full Moon and whose radiance is like ten million suns,','Accept this sipping water offered to you with devotion.','From him Virāj was born, and from Virāj the cosmic Person.','Once born, he extended beyond the Earth, behind and in front.'])
A(s,'ಮೂರು',504,'ಮೂರು ಸಲ ಪೇಲಾಲಿ ನೀರು ಬಿಡಿರಿ.','Release water into the bowl three times.')
M(s,'ಆಚಮನಿಯಂ',507,'ācamanīyaṁ samarpayāmi','I offer water for sipping.')
G(s,'Attend to the devotional offering of sipping water.','Take water and release it into the bowl three times as instructed.')
s=sec('madhuparka','Offer madhuparka','Offerings')
A(s,'ಮಂತ್ರಾಸ್ತೆ',510.16,'ಮಂತ್ರಾಕ್ಷತೆಯನ್ನು ಕೈಯಲ್ಲಿ ತೊಕೊಳ್ಳಬಹುದು. ಇಲ್ಲದಿದ್ದರೆ ಮೊಸರು ಜೇನು ತುಪ್ಪ ಇದು ಮೂರನ್ನೂ ಸೇರಿಸಿ ಇಟ್ಟಿದ್ದೀರಲ್ಲ, ಅದನ್ನು ಉದ್ದರಣಿಯಿಂದ ತೊಗೊಳ್ಳಿರಿ. ಇಲ್ಲದವರು ಮಂತ್ರಾಕ್ಷತೆಯನ್ನು ತೊಗೊಳ್ಳಿರಿ.','You may take mantra-akṣata in your hand. Alternatively, take with the spoon the curd, honey and ghee—the three ingredients—you have mixed and set out. Those who do not have it should take mantra-akṣata.','The speaker presents actual mixture or mantra-akṣata alternative; retain all wording, not only substitution summary.')
M(s,'ಕಮಲ',521.12,'kamalabhavanajāye koṭisūryaprakāśe\nśivadaśucivilāse komale hārayukte\ndadhimadhughṛtayuktaṁ svarṇapātrasthitaṁ yaḥ\nsuśri madhuparko’yaṁ gṛhyatāṁ vedavedye\nmadhuparkaṁ samarpayāmi',['O consort of the lotus-born Brahmā, radiant as ten million suns,','Pure radiance granting auspiciousness, tender and adorned with necklaces,','This madhuparka of curd, honey and ghee, placed in a golden vessel,','May it be accepted, O beautiful goddess known through the Vedas.','I offer madhuparka.'],'Final two lines heavily corrupted in all ASR; suśri/madhuparko’yaṁ/gṛhyatāṁ is provisional intelligible reading. Specific technical uncertainty retained.')
A(s,'ಅಂತ',538,'ಅಂತ ಪೇಲಾಲಿ ಮಧುಪರ್ಕ ಇದ್ದರೆ ಮಧುಪರ್ಕ ಹಾಕಿರಿ. ಇಲ್ಲದಿದ್ದರೆ ಮಂತ್ರಾಕ್ಷತೆ ಹಾಕಿರಿ.','Say this and place the madhuparka in the bowl if you have it. Otherwise, offer mantra-akṣata.')
M(s,'ಮಧುವರ್ಗಕ್ಷ',544,'madhuparkārthe akṣatān samarpayāmi','I offer akṣata in place of madhuparka.')
G(s,'Attend to the goddess invoked in the madhuparka verse.','Offer the curd, honey and ghee mixture; use mantra-akṣata as the recorded alternative if it is unavailable.')
s=sec('pancamrita','Offer pancamrita bathing','Bathing')
A(s,'ಮೊಸರು',547.44,'ಮೊಸರು ಜೇನು ತುಪ್ಪ ಸಕ್ಕರೆ ಇದು ನಾಲ್ಕು ಮಿಕ್ಸ್ ಮಾಡಿದ್ದು ಪಂಚಾಮೃತ. ಇದ್ದರೆ ಅದನ್ನು ಉಪಯೋಗಿಸಿರಿ. ಇಲ್ಲದಿದ್ದರೆ ಮಂತ್ರಾಕ್ಷತೆಯನ್ನು ಹಾಕಿರಿ.','Curd, honey, ghee and sugar: these four mixed together are the pañcāmṛta described here. Use it if you have it. Otherwise, offer mantra-akṣata.','Spoken four-item list retained; Sanskrit verse also names milk. Do not silently insert milk into the Kannada instruction.')
M(s,'ದಕ್ಷೀರ',556,'dadhi kṣīra ghṛtaṁ śarkarā madhusaṁyutaṁ\npañcāmṛtasnānam idaṁ śrī kuruṣva sureśvari\npañcāmṛtasnānaṁ samarpayāmi',['Curd, milk and ghee, mixed with sugar and honey,','Please perform this bathing with the five nectars, O queen of the gods.','I offer bathing with pañcāmṛta.'],'kuruṣva sureśvari phrase differs sharply across ASR, retained as provisional reading.')
G(s,'Attend to the bathing offering and the recorded substitution.','Use the prepared pañcāmṛta if available, otherwise offer mantra-akṣata as instructed.')
s=sec('water-bathing','Offer water bathing','Bathing')
A(s,'ಉದ್ದರಣೆಯಿಂದ',564.72,'ಉದ್ದರಣಿಯಿಂದ ನೀರನ್ನು ತೊಕೊಂಡು ಎಡದ ಕೈಯಲ್ಲಿ ಇಟ್ಟುಕೊಳ್ಳಿರಿ. ಬಲದ ಕೈಯಿಂದ ಒಂದು ಹೂವನ್ನು ತೊಕೊಂಡು ಈ ಉದ್ದರಣಿಯಲ್ಲಿರುವ ನೀರನ್ನು ಮುಟ್ಟಿ ಪ್ರೋಕ್ಷಣ ಮಾಡಿರಿ, ಪುಸ್ತಕ ಮಂಡಲಕ್ಕೆ ಸರಸ್ವತಿಗೆ.','Take water with the spoon and hold it in your left hand. Take a flower with the right hand, touch it to the water in the spoon and sprinkle water on the book mandala, on Sarasvatī.')
M(s,'ಸುವರ್ಣಕಲಸ',576.24,'suvarṇakalaśānītaṁ nānāgandhasuvāsitam\ngandhodaka snānam idaṁ śrī kuruṣva sureśvari\nyatpuruṣeṇa haviṣā devā yajñam atanvata\nvasanto asyāsīdājyaṁ grīṣma idhmaḥ śaraddhaviḥ',['Brought in a golden pot and scented with various fragrances,','Please perform this bathing with fragrant water, O queen of the gods.','When the gods performed the sacrifice with the cosmic Person as the oblation,','Spring was its ghee, summer its fuel and autumn its offering.'])
A(s,'ಪ್ರೋಕ್ಷಣ',594,'ಪ್ರೋಕ್ಷಣ ಮಾಡಿರಿ.','Sprinkle the water.')
M(s,'ಶುದ್ದೋದಕ',597,'śuddhodaka snānaṁ samarpayāmi','I offer bathing with pure water.')
A(s,'ಮತ್ತು',598,'ಮತ್ತೆ ಉದ್ದರಣಿಯನ್ನು ಬಲದ ಕೈಗೆ ಮಾರಿಸಿಕೊಂಡು ಅದರಲ್ಲಿ ಮಿಕ್ಕಿರುವ ನೀರನ್ನು ಪೇಲಾಲಿ ಬಿಡಿರಿ.','Transfer the spoon to your right hand and release the remaining water in it into the bowl.')
M(s,'ಸ್ನಾನನಂತರ',603,'snānānantara ācamanīyaṁ samarpayāmi','I offer water for sipping after the bath.')
G(s,'Attend to bathing the invoked deity in the book mandala.','Hold the spoon in the left hand, use a flower to sprinkle the water, then change hands and release the remaining water as instructed.')
s=sec('clothes','Offer garments','Offerings')
A(s,'ಗಜವಸ್ತ್ರ',608,'ಗಜವಸ್ತ್ರವನ್ನು ಕೈಯಲ್ಲಿ ತೊಗೊಳ್ಳಿರಿ.','Take the gajavastra cloth in your hand.')
M(s,'ಶುಕ್ಲ',610,'śuklavastradvayaṁ','A pair of white garments—','Partial opening phrase before the preparation instruction; not silently discarded.')
A(s,'ಇಲ್ಲದಿದ್ರೆ',613,'ಇಲ್ಲದಿದ್ದರೆ ಮಾಡಿ ಇಟ್ಟು ಇಲ್ಲಿಂದ ವಿಡಿಯೋವನ್ನು ಕಂಟಿನ್ಯೂ ಮಾಡಿರಿ. ಮಾಡಿ ಇಟ್ಟಿದ್ದರೆ ತೊಕೊಂಡು ಸಮರ್ಪಣೆ ಮಾಡೋದು.','If it is not ready, prepare it and then continue the video from here. If you have prepared it, take it and make the offering.')
M(s,'ಶುಕ್ಲವಸ್ತ್ರ',619,'śuklavastradvayaṁ devi amalaṁ kuṭilālake\nbhaktyā samarpitaṁ vāṇi brahmāṇi pratigṛhyatām\ntaṁ yajñaṁ barhiṣi praukṣan puruṣaṁ jātam agrataḥ\ntena devā ayajanta sādhyā ṛṣayaśca ye\nvastrayugmaṁ samarpayāmi',['O goddess with curling locks, accept this spotless pair of white garments,','Offered with devotion, O Vāṇī, consort of Brahmā.','They sprinkled that sacrifice upon the sacred grass: the cosmic Person born in the beginning.','With him the gods performed sacrifice, together with the Sādhyas and the seers.','I offer a pair of garments.'],'amalaṁ/visuallycaptionvimalam endings uncertain; Vedic recitation restored only where phonetic witnesses permit; exact sandhi remains review flagged.')
G(s,'Attend to the devotional offering of the white garment pair.','Take the cloth; prepare it first if needed and resume the video, then offer it with the recorded verses.')
s=sec('neck-thread','Offer the neck thread','Offerings')
A(s,'ನಂತರಸ್ತ',640.959,'ಮಂತ್ರಾಕ್ಷತೆ ತೊಗೊಳ್ಳಿರಿ.','Take mantra-akṣata.')
M(s,'ಸಪ್ತ',644.24,'saptabrahmaraṇe devi saptaśāstrakṛtālaye\nkaṇṭhasūtraṁ gṛhāṇa tvam śeṣaśakrādipūjite\nkaṇṭhasūtraṁ samarpayāmi',['O goddess, lady of the seven sacred utterances and abode of seven scriptures,','Accept the neck thread, O worshipped by Śeṣa, Śakra and the other deities.','I offer the neck thread.'],'Exact saptabrahmaraṇe/saptaśāstrakṛtālaye epithets uncertain across all witnesses; meanings identify provisional interpretation explicitly.')
G(s,'Attend to the goddess’s recorded epithets and the neck-thread offering.','Take mantra-akṣata and make the neck-thread offering.')
s=sec('ornaments','Offer ornaments','Offerings')
A(s,'ಹತ್ತು',656.88,'ಮತ್ತೆ ಮಂತ್ರಾಕ್ಷತೆ ತೊಗೊಳ್ಳಿರಿ.','Take mantra-akṣata again.')
M(s,'ಮುಕುಟ',659,'kaṭaka mukuṭahāraiḥ nūpurair aṅgadādyaiḥ\nvividhamanisaṁyuktair mekhalāmuktahāraiḥ\nkamalavanavilāse kāmade tvam gṛhāṇa\nprakaṭitakaruṇārte bhūriśobhūṣaṇāni\ntasmādyajñātsarvahutaḥ sambhṛtaṁ pṛṣadājyaṁ\npaśūn tāṁś cakre vāyavyān āraṇyān grāmyāśca yē\nābharaṇāni samarpayāmi',['With bracelets, crowns, necklaces, anklets, armlets and other ornaments,','Set with various gems, with girdles and pearl necklaces,','Accept these, O giver of blessings who sports in the lotus grove,','O manifestly compassionate one, these many shining ornaments.','From that all-offering sacrifice, curd mixed with ghee was gathered.','It created animals of the air, forest and village.','I offer ornaments.'],'Opening kaṭaka recovered from640finewindow thoughcaptiondrops it; later prakaṭita/karuṇā/bhūriśobhūṣaṇāni compound is provisional phonetic reading, not certified lexical resolution.')
G(s,'Attend to the rich ornament offering named in the verse.','Take mantra-akṣata and offer the ornaments with the recorded formulas.')
s=sec('sandal','Offer sandal paste','Offerings')
A(s,'ಈಗ',692.959,'ಈಗ ಹೂವಿನಿಂದ ಗಂಧವನ್ನು ಮುಟ್ಟಿಕೊಳ್ಳಿ, ಗಂಧವನ್ನು ಮುಟ್ಟಿಕೊಂಡು.','Now touch the sandal paste with a flower—touch the sandal paste.','Spoken repetition/restart retained.')
M(s,'ಚಂದನ',697.76,'candanāgarukastūrī karpūrādyaiḥ saṁyutam\ngandhaṁ gṛhāṇa varade vidhipatni namo’stute\ntasmādyajñātsarvahutaḥ ṛcaḥ sāmāni jajñire\nchandāṁsi jajñire tasmād yajus tasmādajāyata\ngandhān samarpayāmi',['Sandal, agaru and musk, combined with camphor and other fragrances:','Accept this fragrant paste, O giver of blessings, consort of Brahmā; salutation to you.','From that all-offering sacrifice the Ṛg verses and Sāman chants were born.','From it the meters were born, and from it the Yajur formulas arose.','I offer fragrant sandal paste.'],'chandāṁsi clause retained from nativecaption711.5–718 despite fine/coarse ASR omission; not dropped merely because model omits it.')
A(s,'ಅಂತ',722,'ಅಂತ ಗಂಧವನ್ನು ಸಮರ್ಪಣೆ ಮಾಡಿರಿ. ಗಂಧದಿಂದ ಬೊಟ್ಟು ಇಡಬಹುದು.','Say this and offer the sandal paste. You may make a sandal-paste mark.')
G(s,'Attend to the fragrant paste offering and the Vedic forms named in the recitation.','Touch sandal paste with a flower, offer it and make a sandal mark as instructed.')
s=sec('aksata','Offer aksata','Offerings')
A(s,'ನಂತರ',727.279,'ಮಂತ್ರಾಕ್ಷತೆ ತೊಗೊಳ್ಳಿರಿ.','Take mantra-akṣata.')
M(s,'ಅಕ್ಷತಾನ್',729,'akṣatān dhavalān divyān śālitaṇḍulamiśritān\ngṛhāṇa varade devi brahmapatni śubhākṣatān\nakṣatān samarpayāmi',['Accept these white, divine akṣata of rice grains,','O giver of blessings, goddess and consort of Brahmā: these auspicious akṣata.','I offer akṣata.'])
A(s,'ಮಂತ್ರ',741,'ಅಂತ ಮಂತ್ರಾಕ್ಷತೆ ಹಾಕಿರಿ.','Say this and offer mantra-akṣata.')
G(s,'Attend to the offering of the auspicious white grains.','Take and offer mantra-akṣata with the verse.')
s=sec('turmeric-kumkum','Offer turmeric and kumkum','Offerings')
A(s,'ಅರ್ಶ',742,'ಅರಿಶಿನ ಕುಂಕುಮ. ಕುಂಕುಮ ಗಂಧ ಇಟ್ಟು ಕುಂಕುಮ ಹಚ್ಚಬಹುದು. ಅರಿಶಿನ ಕುಂಕುಮವನ್ನು ಪೂಜೆ ಮಾಡಿರಿ.','Turmeric and kumkum. Having applied sandal paste, you may apply kumkum. Worship with turmeric and kumkum.','The short spoken phrase around kumkum/sandal is grammatically fragmentary; full objects and instruction retained.')
M(s,'ಹರಿದ್ರ',748,'haridrā kuṅkumaṁ devi gandhacūrṇādikānapi\ndāsyāmi parayā bhaktyā brahmāṇi pratigṛhyatām\ntasmād aśvā ajāyanta ye ke cobhaya dataḥ\ngāvo ha jajñire tasmād tasmājjātā ajā avayaḥ\nharidrā cūrṇa kuṅkumān samarpayāmi',['O goddess, I shall offer turmeric, kumkum and fragrant powders and other such offerings,','With supreme devotion; accept them, O consort of Brahmā.','From him horses were born, and all animals with teeth in both jaws.','From him cows were born, and from him goats and sheep.','I offer turmeric powder and kumkum.'])
G(s,'Attend to the offering of turmeric, kumkum and fragrant powders.','Apply kumkum after sandal if desired and make the recorded turmeric and kumkum offering.')
s=sec('flowers','Offer flowers','Offerings')
A(s,'ಸ್ವಲ್ಪ',775,'ಸ್ವಲ್ಪ ಕೈಯಲ್ಲಿ ಹೂವನ್ನು ಹಿಡುಕೊಳ್ಳಿ.','Hold some flowers in your hand.')
M(s,'ನಂದ್ಯ',778,'nandhyāvartādipuṣpaiśca kalhāraiḥ mallikādibhiḥ\nkaravīraiḥ jāti kusumaiḥ mandāraiśca manoramaiḥ\nnīlotpalaiśca kamalaiḥ tatkālatarusambhavaiḥ\npūjayāmi supuṣpaiśca varade bhaktavatsale\nnānāvidha puṣpāṇi samarpayāmi',['With nandhyāvarta and other flowers, water lilies, jasmine and others,','With oleander, jāti jasmine and pleasing mandāra flowers,','With blue lotuses, lotuses and flowers growing on the season’s trees,','I worship with beautiful flowers, O giver of blessings, affectionate to devotees.','I offer various kinds of flowers.'])
G(s,'Attend to the flower offering addressed to the giver of blessings.','Hold flowers and offer them with the recorded verse.')
s=sec('anga-puja','Worship the parts of the goddess','Flower worship')
A(s,'ಹೀಗೆ',801.519,'ಹೀಗೆ ಒಂದೊಂದು ಹೂವಾಗಿ ಅಂಗ ಪೂಜೆ ಅರ್ಚನೆ ಮಾಡ್ತಾ ಬನ್ನಿರಿ.','In this way, keep performing the worship of the body parts, offering one flower at a time.')
anga=[('brahmāṇyai','pādau','Brahmā’s consort','feet'),('jagaddhātryai','gulphau','sustainer of the world','ankles'),('jagadvatsalāyai','jaṅghe','she who loves the world','shins'),('jagatpūjyāyai','jānunī','she who is worshipped by the world','knees'),('cāruvilāsinyai','ūrū','she of graceful play','thighs'),('nārāyaṇapriyāyai','kaṭiṁ','she who is dear to Nārāyaṇa','waist'),('janmahīnāyai','jaghanaṁ','the birthless one','hips'),('gambhīranābhaye','nābhiṁ','she of the deep navel','navel'),('garuḍaśeṣarudramātre','udaraṁ','mother of Garuḍa, Śeṣa and Rudra','abdomen'),('lokamātre','stanau','mother of the world','breasts'),('viśālavakṣase','vakṣasthalaṁ','she of the broad chest','chest'),('gānavicakṣaṇāyai','kaṇṭhaṁ','she who is skilled in music','throat'),('skandādidevapūjyāyai','skandhau','she who is worshipped by Skanda and other gods','shoulders'),('caturbhujāyai','bāhūn','the four-armed goddess','arms'),('pustakadhāriṇyai','hanuṁ','the bearer of the book','jaw'),('śrotriyabāndhavāyai','śrotre','friend of Vedic scholars','ears'),('sarvavedoddhāriṇyai','vaktraṁ','she who upholds all the Vedas','face'),('bimbasamānauṣṭhyai','oṣṭhau','she whose lips resemble the bimba fruit','lips'),('sunāsāyai','nāsikāṁ','she with a beautiful nose','nose'),('kamalacakṣuṣe','netre','the lotus-eyed goddess','eyes'),('tilakadhāriṇyai','phālaṁ','the wearer of the forehead mark','forehead'),('anekacandrakāntaye','keśān','she of many moonlike rays; reading uncertain','hair'),('sarvābhīṣṭadātre','śiraḥ','the giver of all desired blessings','head'),('sarasvatyai','sarvāṅgaṁ','Sarasvatī','whole form')]
for deity,part,meaning,partmeaning in anga:WORDS[deity]='to '+meaning;WORDS[part]=partmeaning
M(s,'ಬ್ರಹ್ಮಾಣ್ಯೇ',806,'\n'.join(d+' namaḥ '+p+' pūjayāmi' for d,p,_,_ in anga),['Salutation to '+d+'. I worship her '+p+'.' for _,_,d,p in anga],'cāruvilāsinyai/nārāyaṇapriyāyai, śrotriyabāndhavāyai and anekacandrakāntaye are specifically uncertain epithets across acoustic ASR; retain provisional reading notes. Do not substitute different standard anga list.')
G(s,'Attend to each named quality and body-part offering in the recorded sequence.','Offer one flower at a time while reciting the complete body-part worship.')
s=sec('names-incarnations','Worship with divine names and incarnations','Flower worship')
A(s,'ಈಗ',881.68,'ಈಗ ಕೇಶವಾದಿ ನಾಮದಿಂದ ಅರ್ಚನೆ.','Now worship with the names beginning with Keśava.')
ordered=[k for k,v in NAMES[:18]]+['nārasimhāya','acyutāya','janārdanāya','upendrāya','haraye','śrīkṛṣṇāya']
inc=[('matsyāya','Matsya'),('kūrmāya','Kūrma'),('varāhāya','Varāha'),('nārasimhāya','Nārasiṁha'),('vāmanāya','Vāmana'),('bhārgavāya','Bhārgava'),('rāmāya','Rāma'),('kṛṣṇāya','Kṛṣṇa'),('bauddhāya','Buddha'),('kalkine','Kalki')]
for k,v in inc:WORDS[k]='to '+v
M(s,'ಕೇಶವಾಯ',883,'\n'.join(k+' namaḥ' for k in ordered+ [k for k,v in inc])+'\nmatsyādi anantāvatāra rūpātmaka śrī vedavyāsāya namaḥ',['Salutation to '+dict(NAMES).get(k,k)+'.' for k in ordered]+['Salutation to '+v+'.' for k,v in inc]+['Salutation to Śrī Vedavyāsa, whose nature comprises the countless incarnations beginning with Matsya.'])
G(s,'Attend to the divine names and incarnations beginning with Matsya.','Continue flower worship with every recorded name and incarnation.')
s=sec('deity-guru-archana','Worship the deities, seers and gurus','Flower worship')
named=['kapilāya','kapilāya','dattātreyāya','hayagrīvāya','rāmāya','kṛṣṇāya','paraśurāmāya','nārasimhāya','vedavyāsāya','śrīnārāyaṇāya','mahālakṣmyai','bhūdevyai','durgāyai','hanumate','bhāratyai','sarasvatyai','brahmaṇe','śeṣāya','rudrāya','pārvatyai','vināyakāya','ṛṣibhyo','ṛṣibhyo','ṛṣibhyo','praṇavāya','kāśyapāya']
more=['kāśyapādi ṛṣigaṇebhyo','sūktābhimāni devatābhyo','sakala ṭippaṇī bhāṣyakāra devatābhyo']
gurus=['ānandatīrtha','jayatīrtha','śrīpādarāja','vyāsarāja','vādirāja','vijayendratīrtha','raghūttamatīrtha','rāghavendratīrtha','purandaradāsa','kanakadāsa','vijayadāsa','gopāladāsa','jagannāthadāsa']
lines=[k+' namaḥ' for k in named]+[k+' namaḥ' for k in more]+[k+' gurubhyo namaḥ' for k in gurus]+['sakala śāstrābhimāni akṣarābhimāni devatābhyo namaḥ','sarasvatyai namaḥ vedavyāsāya namaḥ','nānāvidha parimala patra puṣpārcanaṁ samarpayāmi']
M(s,'ಕಪಿಲಾಯ',935.279,'\n'.join(lines),['Salutation '+WORDS.get(k,'to '+k)+'.' for k in named]+['Salutation to the groups of seers beginning with Kāśyapa.','Salutation to the deities presiding over the sūktas.','Salutation to all the divinities of the annotations and commentaries.']+['Salutation to guru '+k+'.' for k in gurus]+['Salutation to all the deities presiding over scriptures and letters.','Salutation to Sarasvatī and Vedavyāsa.','I offer worship with various fragrant leaves and flowers.'],'Kapila utterance repeated twice; ṛṣibhyo repeated three times, corroborated by fine/coarse/captions. Vijaye ndra/Jagannātha Tīrtha disputed guru name: captions favor Vijayendra, fine/coarse different; exact name visibly flagged. Sūktābhimāni/śuktābhimāni technical reading uncertain.')
G(s,'Attend to the complete assembly of deities, seers, commentators and gurus honored by name.','Continue the recorded flower worship without dropping the repeated Kapila and seer salutations.')
s=sec('incense','Offer incense','Concluding offerings')
A(s,'ಈಗ',1032,'ಈಗ ಊದು ಕಡ್ಡಿ ಅಥವಾ ದಶಾಂಗವನ್ನು ಮುಡಿಸಿಕೊಳ್ಳಿರಿ. ಗಂಟೆ ಬಾರಿಸ್ತಾ ಧೂಪ ತೋರಿಸಿರಿ.','Now light an incense stick or daśāṅga incense. Ring the bell while offering the incense.')
M(s,'ಓಂ',1044.88,'oṁ\ndaśāṅgaṁ guggulopetaṁ sugandhaṁ ca manoharam\ndhūpaṁ gṛhāṇa kalyāṇi bhaktiṁ tvayi acalāṁ kuru\nyatpuruṣaṁ vyadadhuḥ katidhā vyakalpayan\nmukhaṁ kimasya kau bāhū kāvūrū pādā ucyete\ndhūpamāghrāpayāmi',['Oṁ.','Incense of ten ingredients, containing guggulu, fragrant and pleasing,','Accept this incense, O auspicious one; make devotion to you unwavering.','When they divided the cosmic Person, into how many parts did they arrange him?','What is called his mouth, what are his arms, what are his thighs and feet?','I offer incense to be inhaled.'],'guggulopetaṁ and final ucyete are intelligible provisional readings of corrupted phonetic outputs; not claimed direct-human-verified.')
A(s,'ಧೂಪವನ್ನ',1067.44,'ಧೂಪವನ್ನು ತೋರಿಸಿ ಊದು ಕಡ್ಡಿ ಸ್ಟ್ಯಾಂಡಲ್ಲಿ ಊದು ಕಡ್ಡಿಯನ್ನು ಇಟ್ಟು, ಇಟ್ಟು.','Offer the incense and put the incense stick in its stand—put it there.','Actual repeated ಇಟ್ಟು retained.')
G(s,'Attend to the recorded request for unwavering devotion.','Light incense, ring the bell while offering it, and put the stick in its stand afterward.')
s=sec('lamp-offering','Offer the lamp','Concluding offerings')
A(s,'ಹೀಗೆ',1073.36,'ಹೀಗೆ ಮೂರು ಬತ್ತಿಗಳು ತುಪ್ಪದಲ್ಲಿ ನೆನೆಸಿ ಮೂರು ಬತ್ತಿಗಳನ್ನು ಮಾಡಿ ಅದು ಹಲಿಗಾರತಿಯಲ್ಲಿ ಇಡಿರಿ, ಇಟ್ಟು.','In this way, prepare three wicks soaked in ghee and place the three wicks in the hālagārati plate—place them there.')
M(s,'ಕರತವ',1081,'ghṛtāktavartitrayaiḥ dīpitaṁ dīpam ambike\ngṛhāṇa acintyarūpe tvam kamalāsanavallabhe\nbrāhmaṇo’sya mukhamāsīd bāhū rājanyaḥ kṛtaḥ\nūrū tadasya yadvaiśyaḥ\nūrū tadasya yadvaiśyaḥ padbhyāṁ śūdro ajāyata\ndīpaṁ darśayāmi',['O Ambikā, this lamp lit with three ghee-soaked wicks,','Accept it, O goddess of inconceivable form, beloved of the lotus-seated Brahmā.','The Brahmin was his mouth; his arms were made the royal class.','His thighs were the Vaiśya—','His thighs were the Vaiśya; from his feet the Śūdra was born.','I show the lamp.'],'Lamp-opening ghṛtāktavartitrayaiḥ is provisional reconstruction of garbled shared ASR; retains recorded three-wick meaning. Vaiśya clause repeated twice in independent fine acoustic window; native captions may compact it.')
A(s,'ಹಗಂತ',1108.32,'ಹಾಗೆ ಅಂತ ದೀಪವನ್ನು ತೋರಿಸಿ ಆ ಮೂರು ಬತ್ತಿಗಳನ್ನು ಪೇಲಾಲಿ ಹಾಕಿಕೊಳ್ಳಿರಿ.','Say this, show the lamp and then place those three wicks into the bowl.')
G(s,'Attend to the lamp offered with the three ghee-soaked wicks.','Place three soaked wicks in the plate, offer the lamp and put the wicks in the bowl afterward.')
s=sec('food-preparation','Prepare the food offering','Naivedya')
A(s,'ಹಾಕಬಿಟ್ಟು',1113,'ಹಾಕಿಬಿಟ್ಟು ವೀಳ್ಯದೆಲೆ ಅಡಿಕೆ ತೆಂಗಿನಕಾಯಿ ಅದನ್ನೆಲ್ಲ ನೈವೇದ್ಯಕ್ಕೆ ತೆಗೆದಿಟ್ಟುಕೊಂಡು, ಬೇರೆ ಏನಾದರೂ ನೈವೇದ್ಯ ಇದ್ದರೆ ಅದನ್ನು ನೈವೇದ್ಯ ಮಾಡೋದು. ನೀರು ತೊಕೊಂಡು ನೈವೇದ್ಯ ಪದಾರ್ಥಗಳಿಗೆ ಪ್ರೋಕ್ಷಣ ಮಾಡಿರಿ.','After placing them there, take the betel leaves, areca nut and coconut set out for the food offering. If you have any other food offering, offer that too. Take water and sprinkle it over the food items.')
M(s,'ಭುರ್ಭುವ',1124,'bhūrbhuvassuvaḥ','Earth, the intermediate world and heaven.')
A(s,'ಪರಿಶೇಷಣ',1125.52,'ಪರಿಶೇಷಣ ಮಾಡಿರಿ.','Perform the surrounding water sprinkling.')
M(s,'ಸತ್ಯಂ',1126,'satyaṁ tvartena pariṣiñcāmi','I sprinkle truth with the cosmic order.')
A(s,'ಒಂದು',1128,'ಒಂದು ಉದ್ದರಣಿ ನೀರನ್ನು ಪೇಲಾಲಿ ಬಿಡಿರಿ.','Release one spoonful of water into the bowl.')
M(s,'ಅಮೃತೋಪಸ್ತರಣ',1131.52,'amṛtopastaraṇamasi svāhā','You are the foundation of nectar; svāhā.')
A(s,'ಆರು',1133.919,'ಆರು ಸಲ ನೀರು ಬಿಡಿರಿ.','Release water six times.')
M(s,'ಪ್ರಾಣಸ್ವಾಹ',1135,'prāṇāya svāhā apānāya svāhā vyānāya svāhā\nudānāya svāhā samānāya svāhā brahmaṇe svāhā',['An offering to Prāṇa, Apāna and Vyāna.','An offering to Udāna, Samāna and Brahman.'])
G(s,'Attend to presenting the food and the offerings to the vital breaths.','Prepare the listed food items, sprinkle the water and make the six vital-breath offerings.')
s=sec('food-verses','Offer the principal food','Naivedya')
A(s,'ಕೈಯಲ್ಲಿ',1143.84,'ಕೈಯಲ್ಲಿ ಹೂವನ್ನು ತೊಗೊಳ್ಳಿರಿ.','Take a flower in your hand.')
M(s,'ಕದಲಿ',1146,'kadalī panasa āmrāṇāṁ supakvāni phalāni ca\ndadhi kṣīra ghṛtādīni kandamūlaphalāni ca\npañcakhādyaṁ ca susvādu śītalodakam eva ca\nbhakṣyabhojyasamāyuktaṁ naivedyaṁ pratigṛhyatām\napūpān vividhān svādūn khādyān vai ghṛtapācitān\nṣaḍvidha annāni sūpaṁ ca pāyasaṁ śarkarāyutam\ncandramā manaso jātaḥ cakṣoḥ sūryo ajāyata\nmukhādindraścāgniśca prāṇādvāyurajāyata\napūpādika annādi mahānaivedyaṁ nivedayāmi',['Ripe banana, jackfruit, mango and other fruits,','Curd, milk, ghee and other offerings, tubers, roots and fruits,','Tasty pañcakhādya and cool water too,','Along with foods to be eaten and savored: accept the food offering.','Various tasty cakes and other prepared foods,','Six kinds of rice or food preparations, soup and sweetened pāyasa.','The Moon was born from his mind; from his eye the Sun was born.','From his mouth Indra and Agni, and from his vital breath Vāyu were born.','I present the principal food offering, including cakes, rice and other foods.'],'Food-list first compound āmrāṇāṁ and cooked-food lines severely corrupt; vai ghṛtapācitān is a provisional intelligible reading of acoustic vaikṛtabhāṣitān and is visibly flagged across fine/coarse/targeted witnesses; ṣaḍvidha annāni retained from three independent acoustic witnesses, despite caption compacting the phrase. Other cooked-food compounds remain unresolved. Current food-list reading/meaning is explicitly provisional and must be reviewed against source, not certified exact restoration.')
A(s,'ಅಂತ',1187,'ಅಂತ ಹೂ ಮಂತ್ರಾಕ್ಷತೆಯನ್ನು ಹಾಕಿರಿ.','Say this and offer the flower and mantra-akṣata.')
G(s,'Attend to the full food offering and the Vedic account of the cosmic Person.','Hold a flower and offer the prepared foods with the recitation; review the specifically uncertain food-list wording.')
s=sec('food-completion','Conclude the food offering','Naivedya')
A(s,'ಹಾಕಬಿಟ್ಟು',1189,'ಹಾಕಿಬಿಟ್ಟು ಒಂದು ಉದ್ದರಣಿ ನೀರನ್ನು.','After offering it, take one spoonful of water.')
M(s,'ಮಧ್ಯೆ',1193,'madhye amṛtapānīyaṁ samarpayāmi','I offer nectar-like drinking water during the meal.')
A(s,'ಐದು',1196.4,'ಐದು ಸಲ ನೀರು ಬಿಡಿರಿ.','Release water five times.')
M(s,'ಅಮೃತದಾನಂ',1198,'amṛtāpidhānamasi svāhā\nhastaprakṣālanaṁ samarpayāmi mukhaprakṣālanaṁ samarpayāmi\npādaprakṣālanaṁ samarpayāmi ācamanīyaṁ samarpayāmi',['You are the covering of nectar; svāhā.','I offer water for washing the hands and face or mouth.','I offer water for washing the feet and water for sipping.'])
G(s,'Attend to completing the food offering and its washings.','Offer the drinking water and the five concluding water offerings.')
s=sec('fruit-offering','Offer fruit and coconut','Concluding offerings')
A(s,'ಈಗ',1207.44,'ಈಗ ಹಣ್ಣು ಕಾಯಿಯನ್ನು ನೈವೇದ್ಯ ಮಾಡಿರಿ.','Now offer the fruit and coconut as naivedya.')
M(s,'ಬೀಜಪೂರ',1209.679,'bījapūra āmra panasa kharjūrī kadalīphalaṁ\nnārikelaphalaṁ divyaṁ gṛhāṇa abhīṣṭadāyini\nnānāvidha phalāni mahānaivedyaṁ nivedayāmi',['Citron, mango, jackfruit, dates and banana fruit,','And divine coconut fruit: accept these, O giver of desired blessings.','I present the various fruits as the principal food offering.'],'Fruit-list words āmra/panasa recovered from fine/coarse acoustic witnesses but captions compact them; kharjūrī form uncertain.')
G(s,'Attend to the fruits offered to the giver of blessings.','Offer the prepared fruit and coconut with the recorded formula.')
s=sec('tambula','Offer betel','Concluding offerings')
A(s,'ಮೇಲೆ',1220.559,'ವೀಳ್ಯದೆಲೆ ಅಡಿಕೆ ಮೇಲೆ ಒಂದು ಜೊಟ್ಟು ನೀರು ಪ್ರೋಕ್ಷಣ ಮಾಡಿರಿ.','Sprinkle a little water on the betel leaf and areca nut.')
M(s,'ತಾಂಬೂಲಂಚ',1222.24,'tāmbūlaṁ ca sakarpūraṁ pūganāgadalairyutam\ngṛhāṇa devadeveśi tatsvarūpe namo’stute\npūgīphala tāmbūlaṁ samarpayāmi',['Accept betel with camphor, accompanied by areca nut and betel leaves,','O queen of the gods; salutation to you in that form.','I offer areca nut and betel.'],'Exact pūganāgadalairyutam and tatsvarūpe phrase remain uncertain across all ASR; retained provisional words flagged.')
G(s,'Attend to the betel, areca and camphor offering.','Sprinkle water on the betel and areca and make the offering.')
s=sec('dakshina','Offer daksina','Concluding offerings')
A(s,'ಒಂದು',1236.24,'ಒಂದು ದಕ್ಷಿಣೆಯನ್ನು ಇಡಿರಿ.','Place an offering of dakṣiṇā.')
M(s,'ಶುವರ್ಣಂ',1238,'suvarṇaṁ sarvadhātūnāṁ śreṣṭhaṁ devi ca tatsadā\nbhaktyā dadāmi varade\nbhaktyā dadāmi varade svarṇavṛṣṭiṁ ca dehi me\nsuvarṇapuṣpa dakṣiṇāṁ samarpayāmi',['Gold is the best of all metals, O goddess, at all times.','With devotion I give it, O giver of blessings—','With devotion I give it, O giver of blessings; grant me a shower of gold.','I offer the golden flower and dakṣiṇā.'],'bhaktyā dadāmi varade is actually repeated, corroborated by fine/coarse/captions; retained both. sarvadhātūnāṁ compound corrupted in ASR but intelligible contextual reading.')
G(s,'Attend to the devotion accompanying the dakṣiṇā offering.','Place dakṣiṇā and recite the full offering, including the repeated line.')
s=sec('mangalarati','Offer mangalarati','Completion')
A(s,'ಮಂಗಳಾರತಿಗೆ',1251,'ಮಂಗಳಾರತಿಗೆ ಬತ್ತಿ ಅಥವಾ ಕರ್ಪೂರವನ್ನು ಏರಿಸಿಕೊಂಡು, ಮಂಗಳಾರತಿಯನ್ನು ಗಂಟೆ ಬಾರಿಸುತ್ತಾ ತೋರಿಸಿರಿ.','Light a wick or camphor for maṅgalārati and offer the maṅgalārati while ringing the bell.')
M(s,'ನೀರಾಜನಂ',1257.36,'nīrājanaṁ gṛhāṇa tvam jagadānandadāyini\njagattimiramārtāṇḍamaṇḍale te namo namaḥ\nnābhyāsīdantarikṣaṁ śīrṣṇo dyauḥ samavartata\npadbhyāṁ bhūmirdiśaḥ śrotrāt tathā lokān akalpayan\nmaṅgala nīrājanaṁ samarpayāmi',['Accept the waving of lights, O giver of joy to the world.','O solar orb dispelling the world’s darkness, repeated salutation to you.','From his navel came the intermediate world; from his head heaven arose.','From his feet came the Earth and from his ears the directions; thus they arranged the worlds.','I offer the auspicious waving of lights.'])
A(s,'ಅಂತ',1279,'ಅಂತ ಮಂಗಳಾರತಿಯನ್ನು ತೋರಿಸಿ ಹೂವನ್ನು ಸುತ್ತಿ ಹಾಕಿಟ್ಟು, ನೀವು ಮಂಗಳಾರತಿಯನ್ನು ತೊಕೊಂಡು ಮನೆಯಲ್ಲಿ ಇರುವವರಿಗೆಲ್ಲ ಮಂಗಳಾರತಿಯನ್ನು ಕೊಡಿರಿ. ಕೊಟ್ಟಿಟ್ಟು ಮಂಗಳಾರತಿ ತಟ್ಟೆಯನ್ನು ಕೆಳಗೆ ಇಟ್ಟು.','Say this, offer maṅgalārati, circle the flower around it and offer the flower. Receive the maṅgalārati yourself and give it to everyone in the house. After giving it, put the maṅgalārati plate down.')
G(s,'Attend to the goddess addressed as giver of joy and dispeller of darkness.','Light the wick or camphor, ring the bell during ārati, offer the circled flower, share ārati with the household and set the plate down.')
s=sec('puspanjali','Offer puspanjali','Completion')
A(s,'ಹೂವು',1290,'ಹೂವು ಮಂತ್ರಾಕ್ಷತೆಯನ್ನು ಎಲ್ಲರೂ ಕೈಯಲ್ಲಿ ತೊಕೊಳ್ಳಬಹುದು.','Everyone may take flowers and mantra-akṣata in their hands.')
M(s,'ಶಾರದೇ',1293.84,'śārade sarvalokamātastvam āśritābhīṣṭadāyini\npuṣpāñjaliṁ gṛhāṇemāṁ mayā bhaktyā samarpitām',['O Śāradā, you are the mother of all worlds and giver of desired blessings to those who seek refuge.','Accept this handful of flowers offered by me with devotion.'])
A(s,'ಹಗಂತ',1304.72,'ಹಾಗೆ ಅಂತ ಹೂ ಮಂತ್ರಾಕ್ಷತೆಯನ್ನು ಹಾಕಿರಿ.','Say this and offer the flowers and mantra-akṣata.')
G(s,'Attend to Śāradā as mother of all worlds and refuge of devotees.','Take flowers and mantra-akṣata and offer the puṣpāñjali.')
s=sec('pradaksina','Circumambulate and prostrate','Completion')
A(s,'ಹಾಕಬಿಟ್ಟು',1307,'ಹಾಕಿಬಿಟ್ಟು ಮತ್ತೆ ಹೂ ಮಂತ್ರಾಕ್ಷತೆಯನ್ನು ಕೈಯಲ್ಲಿ ತೊಕೊಂಡು ಪ್ರದಕ್ಷಿಣೆ ಮಾಡಿರಿ.','After offering them, take flowers and mantra-akṣata in the hand again and circumambulate.')
M(s,'ಯಾನಿಕಾನಿಚ',1312,'yāni kāni ca pāpāni janmāntarakṛtāni ca\ntāni tāni vinaśyanti pradakṣiṇa pade pade\nsaptāsyāsan paridhayaḥ triḥsapta samidhaḥ kṛtāḥ\ndevā yadyajñaṁ tanvānā abadhnan puruṣaṁ paśum\npāhi pāhi jagadvandye namaste bhaktavatsale\nnamastubhyaṁ namastubhyaṁ namastubhyaṁ namo namaḥ\nyajñena yajñam ayajanta devāḥ tāni dharmāṇi prathamānyāsan\nte ha nākaṁ mahimānaḥ sacante yatra pūrve sādhyāḥ santi devāḥ',['Whatever wrongdoing was committed in other births,','All of it is destroyed with each step of circumambulation.','Seven were its enclosing sticks, and three times seven fuel sticks were made.','The gods, performing the sacrifice, bound the cosmic Person as the sacrificial offering.','Protect, protect me, O revered by the world; salutation to you, affectionate to devotees.','Salutation to you, salutation to you, salutation to you; repeated salutation.','With sacrifice the gods worshipped the sacrifice; these were the first ordinances.','Those powers reached the heavenly realm where the ancient Sādhyas and gods dwell.'])
A(s,'ಎಂದ',1351,'ಎಂದು ಪ್ರದಕ್ಷಿಣೆ ಮಾಡಿ ನಮಸ್ಕಾರವನ್ನು ಮಾಡಿರಿ.','Say this, circumambulate and prostrate.')
G(s,'Attend to the prayer for protection and the full Vedic recitation accompanying circumambulation.','Circumambulate with flowers and mantra-akṣata and prostrate as instructed.')
s=sec('family-prayers','Pray together with the household','Prayers')
A(s,'ಮಾಡುಟು',1355,'ಮಾಡಿಟ್ಟು ಎಲ್ಲರೂ ಮನೆಯಲ್ಲಿ ಇರುವ ಮಕ್ಕಳು ಎಲ್ಲರೂ ಸೇರಿ ಪ್ರಾರ್ಥನೆಯನ್ನು ಮಾಡೋದು. ಹೂ ಮಂತ್ರಾಕ್ಷತೆ ತೊಕೊಂಡು ಹೇಳಿರಿ.','After doing that, everyone in the house, including all the children, should gather and pray. Take flowers and mantra-akṣata and say:')
M(s,'ಪಾಷಾಂಕುಷ',1362,'pāśāṅkuśa\npāśāṅkuśadharā vāṇī vīṇāpustakadhāriṇī\nmama vaktre vaset nityaṁ dugdhakundendunirmalā\nyathā na devi bhagavān brahmā lokapitāmahaḥ\ntvāṁ parityajya santiṣṭhet tathā bhava varapradā\nvedāḥ śāstrāṇi sarvāṇi nṛtya gītādikaṁ ca yat\nna vihīnaṁ tvayā mātaḥ tathā me santu siddhayaḥ\nlakṣmīr medhā dharā puṣṭiḥ dhṛtiḥ tuṣṭiḥ prabhā matiḥ\netābhiḥ pāhi tanubhiḥ aṣṭābhirmāṁ sarasvati\nsarasvati namastubhyaṁ varade kāmarūpiṇi\nvidyārambhaṁ kariṣyāmi siddhirbhavatu me sadā',['Noose and goad—','Vāṇī bearing the noose and goad, the vīṇā and book,','May she always dwell in my mouth, pure as milk, jasmine and the Moon.','Just as the blessed Brahmā, grandfather of the world, O goddess,','Does not remain apart from you, so be with me, O giver of blessings.','The Vedas, all scriptures, dance, song and whatever other arts there are,','None is complete without you, O mother; in that way may I attain accomplishment.','Prosperity, wisdom, sustaining power, nourishment, firmness, contentment, radiance and understanding,','Protect me with these eight forms, O Sarasvatī.','Sarasvatī, salutation to you, giver of blessings who can take any desired form.','I am beginning learning; may accomplishment always be mine.'],'Initial pāśāṅkuśa prompt repeated before full line, retained both. yathā na/brahmā lokapitāmahaḥ, tvayā/tathā and etābhiḥ pāhi tanubhiḥ lexical links uncertain in phonetic ASR; meaning is provisional specific Sanskrit interpretation. dhṛtiḥ preserved as actually heard rather than substituting another standard list.')
M(s,'ದೋರ್ಬಿರ್ಯುಕ್ತ',1427.12,'dorbhiryuktā caturbhiḥ sphaṭikamaṇimayīm akṣamālāṁ dadhānā\nhastenaikena padmaṁ sitamapi śukaṁ pustakaṁ cāpareṇa\nbhāsā kundenduśaṅkhasphaṭikamaṇinibhā bhāsamānā samānā\nsā me vāgdevateyaṁ nivasatu vadane sarvadā suprasannā\nprārthanāṁ samarpayāmi',['Four-armed, holding a rosary made of crystal gems,','With one hand a white lotus, and with the others a parrot and book,','Shining with a radiance like jasmine, the Moon, conch and crystal,','May this goddess of speech always dwell, serene and gracious, in my mouth.','I offer the prayer.'],'sit amapi śukaṁ (parrot) versus śuklaṁ (white) remains an exact lexical uncertainty in the second line; current literal reading not presented as definitive iconography. Third-line samānā and compound pronunciation uncertain; preserved rather than replaced from an alternate verse.')
A(s,'ಅಂತ',1456,'ಅಂತ ಹೂ ಮಂತ್ರಾಕ್ಷತೆಯನ್ನು ಹಾಕಿಬಿಡಿರಿ.','Say this and offer the flowers and mantra-akṣata.')
G(s,'Attend to the household prayer for learning, understanding and the goddess’s presence in speech.','Gather with the household and children, hold flowers and mantra-akṣata, recite the full prayers and offer them afterward.')
s=sec('dedication','Conclude and dedicate the worship','Completion')
A(s,'ಮಂತ್ರಸ್ತೆ',1460.08,'ಮಂತ್ರಾಕ್ಷತೆಯನ್ನು ಬಲದ ಕೈಯಲ್ಲಿ ಹಾಕಿಕೊಂಡು ಮೂರು ಉದ್ದರಣಿ ನೀರನ್ನು ಬಲದ ಕೈಯಲ್ಲಿ ಹಾಕಿ.','Put mantra-akṣata in your right hand and pour three spoonfuls of water into the right hand.')
M(s,'ಹಾಕಿಸ್ಮತ್ನ',1464.799,'yasya smṛtyā ca nāmoktyā tapaḥ pūjākriyādiṣu\nnyūnaṁ sampūrṇatāṁ yāti sadyo vande tamacyutam\nmantrahīnaṁ kriyāhīnaṁ bhaktihīnaṁ ramāpate\nyatpūjanaṁ mayā deva paripūrṇaṁ tadastu te\nanena navarātryāṁ śarad navarātri mahotsave ācarita sarasvatī pūjanena\nsarasvatyantargata bhagavān bhāratīramaṇa mukhyaprāṇāntargata śrī vyāsa paraśurāma prīyatāṁ',['By remembrance and utterance of whose name, in austerity, worship and other acts,','Whatever is deficient immediately becomes complete: I bow to that Acyuta.','O Lord of Ramā, this worship is deficient in mantra, action and devotion.','Whatever worship I have performed, O Lord, may it be complete for you.','By this Sarasvatī worship performed during the autumn Navarātri festival,','May the blessed Vyāsa and Paraśurāma indwelling in Sarasvatī and in Mukhyaprāṇa, the consort of Bhāratī, be pleased.'],'First completion verse is phonetic reconstruction supported by fine/coarse/targeted acoustic words; exact yasya/sadyo sentence remains review flagged. Recorded repetition navarātryāṁ/śarad navarātri retained; final Vyāsa–Paraśurāma form not replaced with generic deity.')
A(s,'ಅಂತ',1489,'ಅಂತ ನೀರು ಹಾಕಿ ಬಿಟ್ಟುಬಿಡಿರಿ.','Say this, add water and release it.')
M(s,'ಶ್ರೀಕೃಷ್ಣರ್ಪಣ',1491.039,'śrīkṛṣṇārpaṇamastu','May this be an offering to Śrī Kṛṣṇa.')
G(s,'Attend to the prayer that deficiencies be made complete and the dedication of the worship.','Place mantra-akṣata and three spoonfuls of water in the right hand, recite the completion and dedication, then release the water.')
s=sec('third-day-bali','Third-day worship and bali','Following observance')
A(s,'ಮೂರನೇ',1495.679,'ಮೂರನೇ ದಿನ ಬಲಿದಾನ ಅಂತ ಹೇಳಿದ್ದಾರೆ. ಬಲಿದಾನ ಅಂದರೆ ಏನು ಮಾಡಬೇಕು? ಬೆಳಿಗ್ಗೆ ಮೂರನೇ ದಿನ ಅಂದರೆ ಬುಧವಾರ ಬೆಳಿಗ್ಗೆ ಪುನರ್ಪೂಜೆಯನ್ನು ಪಂಚೋಪಚಾರ ಪೂಜೆ ಮಾಡಿ ನೈವೇದ್ಯಗಳನ್ನು ಮಾಡಿರಿ. ಸಂಜೆ ಮನೆಯಲ್ಲಿ ಇರುವ ನಮ್ಮ ಆಯುಧಗಳು, ಮನೆಯಲ್ಲಿ ಉಪಯೋಗಿಸುವ ಗಾಡಿ, ಅಡುಗೆ ಮಾಡುವ ಪಾತ್ರೆಗಳು ಸ್ಟವ್ ಇದಕ್ಕೆಲ್ಲ ಒರೆಸಿ ಗಂಧಾಕ್ಷತೆ ಬೊಟ್ಟುಗಳನ್ನಿಟ್ಟು, ಅವಲಕ್ಕಿ ಕಡಲೆ ಸಕ್ಕರೆ ಬಾಳೆಹಣ್ಣು ಅದನ್ನೆಲ್ಲ ಒಂದು ಎಲೆಯಲ್ಲಿ ಹಾಕಿ ಆ ಸರಸ್ವತಿ ದೇವಿಯ ಮುಂದೆ ಇಟ್ಟು ನೈವೇದ್ಯವನ್ನು ಮಾಡಿ. ಅದೇನೆಲ್ಲ ಇಟ್ಟಿದ್ದಿರಿ ಪಂಚಖಾದ್ಯ ಅಂತ ಹೇಳ್ತಾರೆ.','It is said that the third day is for bali. What should one do for bali? On the morning of the third day—that is, Wednesday—perform the renewed worship with the five offerings and make the food offerings. In the evening, wipe clean the implements in the house, the vehicle you use at home, cooking vessels and the stove. Apply sandal paste and akṣata marks to all of them. Put flattened rice, gram, sugar and banana on a leaf, place these in front of Sarasvatī and offer them as naivedya. What you have prepared there is called pañcakhādya.','Wednesday is the historical third-day example from2025 recording, not a current-week instruction. ಕಡಲೆ/ಕಳ್ಳೆ is retained generically as gram; exact variety not invented.')
G(s,'Attend to the stated third-day worship and honoring of household implements.','On the recorded third-day pattern, renew the worship in the morning; clean and mark the household implements in the evening and make the described offering.')
s=sec('pancakhadya-recipe','Prepare pancakhadya','Following observance')
A(s,'ಪಂಚಕಾದ್ಯ',1537.52,'ಪಂಚಖಾದ್ಯ ಅಂದರೆ ಕಡಲೆ, ಕಡಲೆಬೇಳೆಯನ್ನು ಹುರಿಕೊಳ್ಳಿ. ಚನ್ನಾ ಅಂದರೆ ಕಡಲೆಬೇಳೆ. ಕಡಲೆಬೇಳೆಯನ್ನು ಹುರಿಕೊಳ್ಳೋದು, ಅದನ್ನು ಪುಡಿ ಮಾಡಿಕೊಳ್ಳೋದು, ಅದರಲ್ಲಿ ತೆಂಗಿನಕಾಯಿಯನ್ನು ತುರಿದು ಹಾಕೋದು, ಸಕ್ಕರೆ ಸೇರಿಸೋದು, ಏಲಕ್ಕಿ ಮತ್ತು ಈ ಕರಿ ಎಳ್ಳು ಇದೆ ನೋಡಿರಿ, ಕರಿ ಎಳ್ಳನ್ನು ಹುರಿದು ಅದರಲ್ಲಿ ಹಾಕಿ ಸ್ವಲ್ಪ ತುಪ್ಪವನ್ನು ಹಾಕಿ ಮಿಶ್ರ ಮಿಶ್ರ ಮಾಡಿರಿ. ಇದು ಪಂಚಖಾದ್ಯ ಅಂತ ಇದಕ್ಕೆ ಹೆಸರು. ಇದನ್ನು ನೈವೇದ್ಯ ಮಾಡಬೇಕು.','Pañcakhādya means gram—roast the Bengal gram dal. “Channa” means Bengal gram dal. Roast the dal, powder it, add grated coconut, add sugar and cardamom. And you see this black sesame: roast the black sesame and add it, add a little ghee and mix—mix it together. This is called pañcakhādya. Offer it as naivedya.','Restarts/repetition around gram and mix retained; recipe is the speaker’s description, not an independently standardized replacement.')
G(s,'Attend to the recorded preparation of the food offered to Sarasvatī.','Roast and powder the gram dal; combine grated coconut, sugar, cardamom, roasted black sesame and a little ghee, then offer the mixture.')
s=sec('bali-arati','Complete bali and household arati','Following observance')
A(s,'ಅವಿಲಿಕ್ಕಿ',1561.52,'ಅವಲಕ್ಕಿ ಸಕ್ಕರೆ ಕಡಲೆಗಳು ಇದನ್ನೆಲ್ಲ ಎಲೆಯಲ್ಲಿ ಹಾಕಿ, ವೀಳ್ಯದೆಲೆ ಅಡಿಕೆ ಬಾಳೆಹಣ್ಣು ಎಲ್ಲ ಇಟ್ಟು, ಅದನ್ನು ನೈವೇದ್ಯ ಮಾಡೋದೇ ಬಲಿದಾನ, ಬೇರೆ ಏನಿಲ್ಲ. ಮಾಡಿ ಮಂಗಳಾರತಿಯನ್ನೆಲ್ಲ ಮಾಡಿ, ಮನೆಯಲ್ಲಿ ಇರುವ ಎಲ್ಲ ಆಯುಧಗಳು ಗಾಡಿ ಬಂಡಿ ಎಲ್ಲಕ್ಕೂ ಕೂಡ ಮಂಗಳಾರತಿಯನ್ನು ಮಾಡಿರಿ. ಮಂಗಳಾರತಿಯನ್ನು ಮಾಡಿ ಮುಗಿಸಿ. ಇದು ಸಂಜೆ. ಇದುವೇ ಬಲಿದಾನ. ಬಲಿದಾನ ಮಾಡಿ ಮಂಗಳಾರತಿ ಮಾಡಿದಿರಿ ಅಂದರೆ ಇದು ಬಲಿದಾನವರೆಗೂ. ಸರಸ್ವತಿ ಬಲಿದಾನ, ಮೂರನೇ ದಿನ ಮಾಡಬೇಕಾದ ಕರ್ತವ್ಯಗಳನ್ನು ಕೂಡ ಇದರಲ್ಲಿ ಕೊಟ್ಟಿದ್ದೇವೆ.','Put flattened rice, sugar and gram on a leaf, along with betel leaves, areca nut and bananas. Offering these as naivedya is bali; there is nothing else to it. Perform it and do the maṅgalārati. Also offer maṅgalārati to all the household implements and to the vehicles and carts. Finish the maṅgalārati. This is in the evening. This itself is bali. Having performed bali and maṅgalārati, the observance has been explained through the bali. We have included Sarasvatī bali and the duties to be done on the third day in this video too.','The repeated bali explanation and fragment “through the bali” retained rather than compacted into a single instruction.')
G(s,'Attend to the speaker’s explanation of bali as this food offering and ārati.','Offer the listed foods and share ārati with all household implements and vehicles in the evening.')
s=sec('closing','Next observance and closing thanks','Closing')
A(s,'ನೆಕ್ಸ್ಟ್',1602.64,'ನೆಕ್ಸ್ಟ್ ವಿಜಯದಶಮಿಯ ಆಚರಣೆ ಏನು ಮಾಡಬೇಕು, ಅವತ್ತು ಸರಸ್ವತಿಯ ವಿಸರ್ಜನೆ ಏನು ಅಂಬುದನ್ನು ಮುಂದೆ ಬರುವ ವಿಡಿಯೋದಲ್ಲಿ ಕೊಡುತ್ತೇವೆ. ಧನ್ಯವಾದ.','Next, we will explain in the upcoming video what to do for Vijayadaśamī and what Sarasvatī dismissal means on that day. Thank you.')
G(s,'Attend to the announced continuation on Vijayadaśamī and Sarasvatī dismissal.','Listen to the closing announcement; no additional ritual action is given here.')
# Resolve every block end from the next explicitly word-matched native start.
flat=[(s,b) for s in S for b in s['structuredBlocks']]
for n,(s,b) in enumerate(flat):
 b['endSeconds']=flat[n+1][1]['startSeconds'] if n+1<len(flat) else DURATION
 assert b['startSeconds']<b['endSeconds'],(s['slug'],b['startSeconds'],b['endSeconds'])
 b['provenance']={'sourceId':'puja','nativeCaptionSpan':{'startSeconds':b['startSeconds'],'endSeconds':b['endSeconds'],'events':[e for e in EVENTS if b['startSeconds']<=e['start']<b['endSeconds']]},'rawAcousticWitnessDirs':['../gpt-fine/','../gpt/'],'sourceScriptPolicy':'Retained reconciled Sanskrit in Roman IAST; original Kannada speech with Roman counterpart and full English translation; immutable raw ASR/caption scripts retained separately.'}
# Two genuine ambiguous word-marker events contain both languages; document sharing, never guess fractional partitions.
orn=next(s for s in S if s['slug']=='ornaments');a,m=orn['structuredBlocks'][:2]
a['endSeconds']=659.75;m['startSeconds']=657.839
share={'startSeconds':657.839,'endSeconds':659.75,'rawWord':'ತಗೊಳರಿಕ','reason':'Native ASR combines the take-mantra-akṣata instruction with the acoustic kaṭaka opening, recovered from fine640s witness; no separate Kaṭaka timestamp exists.'}
for b in [a,m]:b['provenance']['sharedCaptionCue']=share;b['notes']+=' Take-akṣata instruction and kaṭaka opening share native event657.839–659.75; exact intra-event partition unresolved.'
ded=next(s for s in S if s['slug']=='dedication');a,m=ded['structuredBlocks'][:2];a['endSeconds']=1470.789
share={'startSeconds':1464.799,'endSeconds':1470.789,'rawWord':'ಹಾಕಿಸ್ಮತ್ನಪೂಜಕ್ರಿಯ','reason':'Native ASR combines Kannada ಹಾಕಿ with first completion verse; both retained in acoustic witnesses, no separate intra-event boundaries.'}
for b in [a,m]:b['provenance']['sharedCaptionCue']=share;b['notes']+=' Last water instruction and first completion verse share native event1464.799–1470.789; exact intra-event partition unresolved.'
ded['structuredBlocks'][-1]['endSeconds']=1493.19
# Every line initially uses honest passage playback. Root may refine shared cues against the actual native words.
for s in S:
 s['startSeconds']=s['structuredBlocks'][0]['startSeconds'];s['endSeconds']=max(b['endSeconds'] for b in s['structuredBlocks'])
 s['guidanceReferences']={key:[{'sourceId':'puja','segmentId':s['id'],'startSeconds':s['startSeconds'],'endSeconds':s['endSeconds'],'basis':'Recorded recitation or instruction; contemplate/action are supplementary editorial guidance, not replacement transcript.'}] for key in ['contemplate','action']}
 for b in s['structuredBlocks']:
  b['provenance']['nativeCaptionSpan']={'startSeconds':b['startSeconds'],'endSeconds':b['endSeconds'],'events':[e for e in EVENTS if b['startSeconds']<=e['start']<b['endSeconds']]}
  if b['kind']=='mantra':
   nonblank=[l for l in b['gloss']['lines'] if l]
   for l in nonblank:
    l['startSeconds']=b['startSeconds'];l['endSeconds']=b['endSeconds'];l['sharedPassageCue']=len(nonblank)>1 or 'sharedCaptionCue' in b['provenance'];l['timingStatus']='Shared complete recitation passage; independent line timing not resolved.' if l['sharedPassageCue'] else 'Single spoken phrase bounded by directly matched native VTT events.';l['timingEvidence']={'sourceId':'puja','nativeStartSeconds':b['startSeconds'],'nativeEndSeconds':b['endSeconds'],'basis':'Actual VTT phrase markers and acoustic transcript witnesses; no human listening claim','sharedCaptionCue':b['provenance'].get('sharedCaptionCue')}
   b['gloss']['evidence']=[{'sourceId':'puja','startSeconds':b['startSeconds'],'endSeconds':b['endSeconds'],'attribution':'Editorial Sanskrit interpretation; specific uncertain lexical readings identified in notes.'}]
 # Combine adjacent uninterrupted recitation runs, preserving all source characters and all repeated utterances.
 out=[]
 for b in s['structuredBlocks']:
  if out and out[-1]['kind']=='mantra' and b['kind']=='mantra':
   p=out[-1];p['sourceOriginal']+=b['sourceOriginal'];p['sourceRoman']+=b['sourceRoman'];p['text']+=b['text'];p['endSeconds']=b['endSeconds'];p['gloss']['lines']+=[None]+b['gloss']['lines'];p['gloss']['evidence']+=b['gloss']['evidence'];p['notes']=' '.join(x for x in [p['notes'],b['notes']] if x);p['provenance']['continuationSpans']=p['provenance'].get('continuationSpans',[])+[b['provenance']]
  else:out.append(b)
 s['structuredBlocks']=out;s['originalScript']=''.join(b['sourceOriginal'] for b in out);s['romanText']=''.join(b['sourceRoman'] for b in out);s['verifyNotes']+=' '+' '.join(b['notes'] for b in out if b['notes']);s['verifyNotes']=s['verifyNotes'].replace('the2025','the 2025');s['timingStatus']='Section and block boundaries matched to actual native VTT word markers, with two explicitly documented shared mixed-language events; individual broad-line cues marked sharedPassageCue.'
 (R/(s['slug']+'.txt')).write_text(s['originalScript'])
assert not UNKNOWN,sorted(set(UNKNOWN))
markers={t for e in EVENTS for t in [e['start'],e['end']]}|{DURATION}
for s in S:
 assert s['originalScript']==''.join(b['sourceOriginal'] for b in s['structuredBlocks'])
 for b in s['structuredBlocks']:
  assert b['startSeconds'] in markers and b['endSeconds'] in markers,(s['slug'],b['startSeconds'],b['endSeconds'])
  assert s['startSeconds']<=b['startSeconds']<b['endSeconds']<=s['endSeconds']
  if b['kind']=='mantra':
   assert [l for l in b['text'].splitlines() if l.strip()]==[l['text'] for l in b['gloss']['lines'] if l]
   for l in b['gloss']['lines']:
    if l:assert l['text'].split()==[w['text'] for w in l['words']]
json.dump(S,open(R/'sections.json','w'),ensure_ascii=False,indent=2)
(R/'complete-source.txt').write_text(''.join(s['originalScript'] for s in S));(R/'complete-roman.txt').write_text(''.join(s['romanText'] for s in S))
L={'sources':[{'id':'puja','url':'https://youtube.com/watch?v=hC8efJAiY2c','role':'complete recorded Saraswati puja and third-day bali instructions','durationSeconds':DURATION,'originalScript':''.join(s['originalScript'] for s in S),'originalMedia':'../source/original.mp3','captions':'../source/original.kn-orig.vtt','rawFineWitnesses':'../gpt-fine/','rawCoarseWitnesses':'../gpt/','sourceScriptPolicy':flat[0][1]['provenance']['sourceScriptPolicy']}],'segments':[]}
for s in S:
 for i,b in enumerate(s['structuredBlocks']):
  entry={'id':s['id']+f'-block-{i:03}','sourceId':'puja','start':b['startSeconds'],'end':b['endSeconds'],'sourceOriginal':b['sourceOriginal'],'sectionId':s['id'],'blockIndex':i,'timingStatus':b['timingStatus'],'provenance':b['provenance']}
  if 'sharedCaptionCue' in b['provenance']:entry['sharedCaptionCue']=b['provenance']['sharedCaptionCue']
  L['segments'].append(entry)
json.dump(L,open(R/'evidence-manifest.json','w'),ensure_ascii=False,indent=2)
coverage={'status':'Full chronological candidate; exact acoustic losslessness not certified; specifically uncertain readings visibly flagged','sourceId':'puja','durationSeconds':DURATION,'sectionCount':len(S),'blockCount':sum(len(s['structuredBlocks']) for s in S),'mantraLineCount':sum(sum(l is not None for l in b.get('gloss',{}).get('lines',[])) for s in S for b in s['structuredBlocks']),'sourceReconstructionPassed':True,'romanReconstructionPassed':True,'glossLineAndTokenCoveragePassed':True,'nativeMarkerBoundsPassed':True,'directHumanListening':False,'sourceCompletenessCertification':False,'witnesses':{'fine45sChunks':41,'coarse180sChunks':10,'targetedShortChecks':7,'nativeVttEvents':len(EVENTS)},'uncertainBlocks':[{'sectionId':s['id'],'slug':s['slug'],'blockIndex':i,'startSeconds':b['startSeconds'],'endSeconds':b['endSeconds'],'notes':b['notes']} for s in S for i,b in enumerate(s['structuredBlocks']) if b['notes']],'nonSpeechIntervals':[{'startSeconds':0,'endSeconds':1.68,'kind':'No captioned speech in opening lead-in; coarse/fine model starts with first introduction; no fabricated words.'},{'startSeconds':1493.19,'endSeconds':1495.679,'kind':'Native caption music event1493.2–1495.669 plus adjacent10ms gaps; no spoken text.'}],'captionEndSeconds':1615.159,'captionOverrunSeconds':1615.159-DURATION,'datePolicy':'Historical Viśvāvasu/Aṣṭamī/Tuesday and Wednesday third-day examples from2025 retained as historical speech, not current auspicious-time guidance.','actualRepetitionsPreserved':['ingredient-list restarts','mama before and after Kannada instruction','Bhāratī invocation before and after offering instruction','praṇavāsana partial opening','pādya three times','arghya three times','śuklavastradvaya partial opening','Kapila twice','ṛṣibhyo three times','Vaiśya clause twice','bhaktyā dadāmi varade twice','pāśāṅkuśa prompted partial opening twice','panchakhadya gram and mix restarts/repetitions'],'sourceLanguagePolicy':'Sanskrit is displayed in Roman IAST. Original-script Kannada explanation, Roman Kannada and complete English translation are separate retained fields; Sanskrit meanings/glosses never replace recitation.'}
json.dump(coverage,open(R/'coverage-report.json','w'),ensure_ascii=False,indent=2)
print(json.dumps({k:coverage[k] for k in ['sectionCount','blockCount','mantraLineCount']},ensure_ascii=False))
