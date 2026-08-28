// Pañcasūkta — complete verse-by-verse recitation practice for Mādhva pūjā.
(function () {
  function losslessSection(section) {
    section.originalScript = section.mantra;
    section.structuredBlocks = [{ kind: "mantra", sourceOriginal: section.mantra, text: section.mantra + "\n\n" }];
    return section;
  }

  function pad(value) { return String(value).padStart(2, "0"); }
  function clock(seconds) {
    var minutes = Math.floor(seconds / 60);
    return minutes + ":" + (seconds - minutes * 60).toFixed(2).padStart(5, "0");
  }

  var sources = {
    purusha: "https://www.youtube.com/watch?v=kyYfT94hNU4",
    sri: "https://www.youtube.com/watch?v=_yQs6-v0584",
    ambhrini: "https://www.youtube.com/watch?v=Jyw3--vT0lY",
    balittha: "https://www.youtube.com/watch?v=K4Q5Brf1PM4",
    manyu: "https://www.youtube.com/watch?v=CIHdtjXrnP8"
  };

  var purusha = `sahasraśīrṣā puruṣaḥ sahasrākṣaḥ sahasrapāt |
sa bhūmiṃ viśvato vṛtvā'tyatiṣṭhad daśāṅgulam || 1 ||

puruṣa evedaṃ sarvaṃ yad bhūtaṃ yac ca bhavyam |
utāmṛtatvasyeśāno yad annenātirohati || 2 ||

etāvān asya mahimā'to jyāyāṃś ca pūruṣaḥ |
pādo'sya viśvā bhūtāni tripādasyāmṛtaṃ divi || 3 ||

tripād ūrdhva udait puruṣaḥ pādo'syehābhavat punaḥ |
tato viṣvaṅ vyakrāmat sāśanānaśane abhi || 4 ||

tasmād virāḻ ajāyata virājo adhi pūruṣaḥ |
sa jāto atyaricyata paścād bhūmim atho puraḥ || 5 ||

yat puruṣeṇa haviṣā devā yajñam atanvata |
vasanto asyāsīd ājyaṃ grīṣma idhmaḥ śarad dhaviḥ || 6 ||

taṃ yajñaṃ barhiṣi praukṣan puruṣaṃ jātam agrataḥ |
tena devā ayajanta sādhyā ṛṣayaś ca ye || 7 ||

tasmād yajñāt sarvahutaḥ sambhṛtaṃ pṛṣadājyam |
paśūn tāṃś cakre vāyavyān āraṇyān grāmyāś ca ye || 8 ||

tasmād yajñāt sarvahuta ṛcaḥ sāmāni jajñire |
chandāṃsi jajñire tasmād yajus tasmād ajāyata || 9 ||

tasmād aśvā ajāyanta ye ke cobhayādataḥ |
gāvo ha jajñire tasmāt tasmāj jātā ajāvayaḥ || 10 ||

yat puruṣaṃ vyadadhuḥ katidhā vyakalpayan |
mukhaṃ kim asya kau bāhū kā ūrū pādā ucyete || 11 ||

brāhmaṇo'sya mukham āsīd bāhū rājanyaḥ kṛtaḥ |
ūrū tad asya yad vaiśyaḥ padbhyāṃ śūdro ajāyata || 12 ||

candramā manaso jātaś cakṣoḥ sūryo ajāyata |
mukhād indraś cāgniś ca prāṇād vāyur ajāyata || 13 ||

nābhyā āsīd antarikṣaṃ śīrṣṇo dyauḥ samavartata |
padbhyāṃ bhūmir diśaḥ śrotrāt tathā lokān akalpayan || 14 ||

saptāsyāsan paridhayas triḥ sapta samidhaḥ kṛtāḥ |
devā yad yajñaṃ tanvānā abadhnan puruṣaṃ paśum || 15 ||

yajñena yajñam ayajanta devās tāni dharmāṇi prathamāny āsan |
te ha nākaṃ mahimānaḥ sacanta yatra pūrve sādhyāḥ santi devāḥ || 16 ||`.split("\n\n");

  var sriCore = `oṃ hiraṇyavarṇāṃ hariṇīṃ suvarṇa-rajata-srajām |
candrāṃ hiraṇmayīṃ lakṣmīṃ jātavedo ma āvaha || 1 ||

tāṃ ma āvaha jātavedo lakṣmīm anapagāminīm |
yasyāṃ hiraṇyaṃ vindeyaṃ gām aśvaṃ puruṣān aham || 2 ||

aśvapūrvāṃ rathamadhyāṃ hastināda-prabodhinīm |
śriyaṃ devīm upahvaye śrīr mā devī juṣatām || 3 ||

kāṃ so'smitāṃ hiraṇyaprākārām ārdrāṃ jvalantīṃ tṛptāṃ tarpayantīm |
padme sthitāṃ padmavarṇāṃ tām ihopahvaye śriyam || 4 ||

candrāṃ prabhāsāṃ yaśasā jvalantīṃ śriyaṃ loke devajuṣṭām udārām |
tāṃ padminīm īṃ śaraṇam ahaṃ prapadye 'lakṣmīr me naśyatāṃ tvāṃ vṛṇe || 5 ||

ādityavarṇe tapaso'dhijāto vanaspatis tava vṛkṣo'tha bilvaḥ |
tasya phalāni tapasā nudantu māyāntarāyāś ca bāhyā alakṣmīḥ || 6 ||

upaitu māṃ devasakhaḥ kīrtiś ca maṇinā saha |
prādurbhūto'smi rāṣṭre'smin kīrtim ṛddhiṃ dadātu me || 7 ||

kṣutpipāsāmalāṃ jyeṣṭhām alakṣmīṃ nāśayāmy aham |
abhūtim asamṛddhiṃ ca sarvāṃ nirṇuda me gṛhāt || 8 ||

gandhadvārāṃ durādharṣāṃ nityapuṣṭāṃ karīṣiṇīm |
īśvarīṃ sarvabhūtānāṃ tām ihopahvaye śriyam || 9 ||

manasaḥ kāmam ākūtiṃ vācaḥ satyam aśīmahi |
paśūnāṃ rūpam annasya mayi śrīḥ śrayatāṃ yaśaḥ || 10 ||

kardamena prajā bhūtā mayi sambhava kardama |
śriyaṃ vāsaya me kule mātaraṃ padmamālinīm || 11 ||

āpaḥ sṛjantu snigdhāni ciklīta vasa me gṛhe |
ni ca devīṃ mātaraṃ śriyaṃ vāsaya me kule || 12 ||

ārdrāṃ puṣkariṇīṃ puṣṭiṃ piṅgalāṃ padmamālinīm |
candrāṃ hiraṇmayīṃ lakṣmīṃ jātavedo ma āvaha || 13 ||

ārdrāṃ yaḥ kariṇīṃ yaṣṭiṃ suvarṇāṃ hemamālinīm |
sūryāṃ hiraṇmayīṃ lakṣmīṃ jātavedo ma āvaha || 14 ||

tāṃ ma āvaha jātavedo lakṣmīm anapagāminīm |
yasyāṃ hiraṇyaṃ prabhūtaṃ gāvo dāsyo'śvān vindeyaṃ puruṣān aham || 15 ||`.split("\n\n");

  var sriPhalasruti = `yaḥ śuciḥ prayato bhūtvā juhuyād ājyam anvaham |
śriyaḥ pañcadaśarcaṃ ca śrīkāmaḥ satataṃ japet || 1 ||

padmānane padma ūrū padmākṣi padmasambhave |
tan me bhajasi padmākṣi yena saukhyaṃ labhāmy aham || 2 ||

aśvadāyī godāyī dhanadāyī mahādhane |
dhanaṃ me juṣatāṃ devi sarvakāmārthasiddhaye || 3 ||

putrapautra dhanaṃ dhānyaṃ hastyaśvādi gave ratham |
prajānāṃ bhavasi mātā āyuṣmantaṃ karotu mām || 4 ||

dhanam agnir dhanaṃ vāyur dhanaṃ sūryo dhanaṃ vasuḥ |
dhanam indro bṛhaspatir varuṇaṃ dhanam aśnute || 5 ||

vainateya somaṃ piba somaṃ pibatu vṛtrahā |
somaṃ dhanasya somino mahyaṃ dadātu sominaḥ || 6 ||

na krodho na ca mātsaryaṃ na lobho nāśubhā matiḥ |
bhavanti kṛtapuṇyānāṃ bhaktānāṃ śrīsūktaṃ japet sadā || 7 ||

candrābhāṃ lakṣmīm īśānāṃ sūryābhāṃ śrīmaheśvarīm |
candrasūryāgnivarṇābhāṃ mahālakṣmīm upāsmahe || 8 ||

varṣantu te vibhāvari divo abhrasya vidyutaḥ |
rohantu sarvabījāny ava brahmadviṣo jahi || 9 ||

padmapriye padmini padmahaste padmālaye padmadalāyatākṣi |
viśvapriye viṣṇumano'nukūle tvatpādapadmaṃ mayi sannidhatsva || 10 ||

yā sā padmāsanasthā vipulakaṭitaṭī padmapatrāyatākṣī |
gambhīrāvartanābhiḥ stanabhara-namitā śubhravastottarīyā |
lakṣmīr divyair gajendrair maṇigaṇakhacitaiḥ snāpitā hemakumbhaiḥ |
nityaṃ sā padmahastā mama vasatu gṛhe sarvamāṅgalyayuktā || 11 ||

siddhalakṣmīr mokṣalakṣmīr jayalakṣmīḥ sarasvatī |
śrīlakṣmīr varalakṣmīś ca prasannā mama sarvadā || 12 ||

varāṅkuśau pāśam abhītimudrāṃ karair vahantīṃ kamalāsanasthām |
bālārkakoṭipratibhāṃ trinetrāṃ bhaje'ham ādyāṃ jagadīśvarīṃ tām || 13 ||

sarvamaṅgalamāṅgalye śive sarvārthasādhike |
śaraṇye tryambake devi nārāyaṇi namo'stu te || 14 ||

śrīr varcasvam āyuṣyam ārogyam āvidhāc chobhamānaṃ mahīyate |
dhānyaṃ dhanaṃ paśuṃ bahuputralābhaṃ śatasaṃvatsaraṃ dīrgham āyuḥ || 15 ||

mahālakṣmyai ca vidmahe viṣṇupatnyai ca dhīmahi |
tan no lakṣmīḥ pracodayāt || 16 ||`.split("\n\n");

  var ambhrini = `ahaṃ rudrebhir vasubhiś carāmy aham ādityair uta viśvadevaiḥ |
ahaṃ mitrāvaruṇobhā bibharmy aham indrāgnī aham aśvinobhā || 1 ||

ahaṃ somam āhanasaṃ bibharmy ahaṃ tvaṣṭāram uta pūṣaṇaṃ bhagam |
ahaṃ dadhāmi draviṇaṃ haviṣmate suprāvye yajamānāya sunvate || 2 ||

ahaṃ rāṣṭrī saṃgamanī vasūnāṃ cikituṣī prathamā yajñiyānām |
tāṃ mā devā vyadadhuḥ purutrā bhūristhātrāṃ bhūry āveśayantīm || 3 ||

mayā so annam atti yo vipaśyati yaḥ prāṇiti ya īṃ śṛṇoty uktam |
amantavo māṃ ta upa kṣiyanti śrudhi śruta śraddhivaṃ te vadāmi || 4 ||

aham eva svayam idaṃ vadāmi juṣṭaṃ devebhir uta mānuṣebhiḥ |
yaṃ kāmaye taṃ tam ugraṃ kṛṇomi taṃ brahmāṇaṃ tam ṛṣiṃ taṃ sumedhām || 5 ||

ahaṃ rudrāya dhanur ā tanomi brahmadviṣe śarave hantavā u |
ahaṃ janāya samadaṃ kṛṇomy ahaṃ dyāvāpṛthivī ā viveśa || 6 ||

ahaṃ suve pitaram asya mūrdhan mama yonir apsv antaḥ samudre |
tato vi tiṣṭhe bhuvanānu viśvotāmūṃ dyāṃ varṣmaṇopa spṛśāmi || 7 ||

aham eva vāta iva pra vāmy ārabhamāṇā bhuvanāni viśvā |
paro divā para enā pṛthivyaitāvatī mahinā saṃ babhūva || 8 ||`.split("\n\n");

  // Mādhva Baḷitthā Sūkta is Ṛgveda 1.141.1–5.
  var balittha = `baḷitthā tad vapuṣe dhāyi darśataṃ devasya bhargaḥ sahaso yato jani |
yad īm upa hvarate sādhate matir ṛtasya dhenā anayanta sasrutaḥ || 1 ||

pṛkṣo vapuḥ pitumān nitya ā śaye dvitīyam ā saptaśivāsu mātṛṣu |
tṛtīyam asya vṛṣabhasya dohase daśapramatiṃ janayanta yoṣaṇaḥ || 2 ||

nir yad īṃ budhnān mahiṣasya varpasa īśānāsaḥ śavasā kranta sūrayaḥ |
yad īm anu pradivo madhva ādhave guhā santaṃ mātariśvā mathāyati || 3 ||

pra yat pituḥ paramān nīyate pary ā pṛkṣudho vīrudho daṃsu rohati |
ubhā yad asya januṣaṃ yad invata ādid yaviṣṭho abhavad ghṛṇā śuciḥ || 4 ||

ādin mātṝr āviśad yāsv ā śucir ahiṃsyamāna urviyā vi vāvṛdhe |
anu yat pūrvā aruhat sanājuvo ni navyasīṣv avarāsu dhāvate || 5 ||`.split("\n\n");

  var manyu = [
    ["Ṛgveda 10.83.1",17.55,35.85,"05-manyu-10-83-verse-1.mp3",`yas te manyo'vidhad vajra sāyaka saha ojaḥ puṣyati viśvam ānuṣak |
sāhyāma dāsam āryaṃ tvayā yujā sahaskṛtena sahasā sahasvatā || 10.83.1 ||`],
    ["Ṛgveda 10.83.2",35.85,56.85,"06-manyu-10-83-verse-2.mp3",`manyur indro manyur evāsa devo manyur hotā varuṇo jātavedāḥ |
manyuṃ viśa īḻate mānuṣīr yāḥ pāhi no manyo tapasā sajoṣāḥ || 10.83.2 ||`],
    ["Ṛgveda 10.83.3",56.85,74.65,"07-manyu-10-83-verse-3.mp3",`abhīhi manyo tavasas tavīyān tapasā yujā vi jahi śatrūn |
amitrahā vṛtrahā dasyuhā ca viśvā vasūny ā bharā tvaṃ naḥ || 10.83.3 ||`],
    ["Ṛgveda 10.83.4",74.65,94.75,"08-manyu-10-83-verse-4.mp3",`tvaṃ hi manyo abhibhūtyojāḥ svayambhūr bhāmo abhimātiṣāhaḥ |
viśvacarṣaṇiḥ sahuriḥ sahāvān asmāsv ojaḥ pṛtanāsu dhehi || 10.83.4 ||`],
    ["Ṛgveda 10.83.5",94.75,115.10,"09-manyu-10-83-verse-5.mp3",`abhāgaḥ sann apa pareto asmi tava kratvā taviṣasya pracetaḥ |
taṃ tvā manyo akratur jihīḻāhaṃ svā tanūr baladeyāya mehi || 10.83.5 ||`],
    ["Ṛgveda 10.83.6",115.10,136.10,"10-manyu-10-83-verse-6.mp3",`ayaṃ te asmy upa mehy arvāṅ pratīcīnaḥ sahure viśvadhāyaḥ |
manyo vajrinn abhi mām ā vavṛtsva hanāva dasyūṃr uta bodhy āpeḥ || 10.83.6 ||`],
    ["Ṛgveda 10.83.7",136.10,154.10,"11-manyu-10-83-verse-7.mp3",`abhi prehi dakṣiṇato bhavā me'dhā vṛtrāṇi jaṅghanāva bhūri |
juhomi te dharuṇaṃ madhvo agram ubhā upāṃśu prathamā pibāva || 10.83.7 ||`],
    ["Ṛgveda 10.84.1",154.10,175.40,"12-manyu-10-84-verse-1.mp3",`tvayā manyo saratham ārujanto harṣamāṇāso dhṛṣitā marutvaḥ |
tigmeṣava āyudhā saṃśiśānā abhi pra yantu naro agnirūpāḥ || 10.84.1 ||`],
    ["Ṛgveda 10.84.2",175.40,194.90,"13-manyu-10-84-verse-2.mp3",`agnir iva manyo tviṣitaḥ sahasva senānīr naḥ sahure hūta edhi |
hatvāya śatrūn vi bhajasva veda ojo mimāno vi mṛdho nudasva || 10.84.2 ||`],
    ["Ṛgveda 10.84.3",194.90,214.00,"14-manyu-10-84-verse-3.mp3",`sahasva manyo abhimātim asme rujan mṛṇan pramṛṇan prehi śatrūn |
ugraṃ te pājo nanv ā rurudhre vaśī vaśaṃ nayasa ekaja tvam || 10.84.3 ||`],
    ["Ṛgveda 10.84.4",214.00,233.20,"15-manyu-10-84-verse-4.mp3",`eko bahūnām asi manyav īḻito viśaṃ viśaṃ yudhaye saṃ śiśādhi |
akṛttaruk tvayā yujā vayaṃ dyumantaṃ ghoṣaṃ vijayāya kṛṇmahe || 10.84.4 ||`],
    ["Ṛgveda 10.84.5",233.20,253.75,"16-manyu-10-84-verse-5.mp3",`vijeṣakṛd indra ivānavabravo'smākaṃ manyo adhipā bhaveha |
priyaṃ te nāma sahure gṛṇīmasi vidmā tam utsaṃ yata ābabhūtha || 10.84.5 ||`],
    ["Ṛgveda 10.84.6",253.75,273.30,"17-manyu-10-84-verse-6.mp3",`ābhūtyā sahajā vajra sāyaka saho bibharṣy abhibhūta uttaram |
kratvā no manyo saha medyedhi mahādhanasya puruhūta saṃsṛji || 10.84.6 ||`],
    ["Ṛgveda 10.84.7",273.30,293.90,"18-manyu-10-84-verse-7.mp3",`saṃsṛṣṭaṃ dhanam ubhayaṃ samākṛtam asmabhyaṃ dattāṃ varuṇaś ca manyuḥ |
bhiyaṃ dadhānā hṛdayeṣu śatravaḥ parājitāso apa ni layantām || 10.84.7 ||`]
  ];

  var sections = [];
  var nextId = 1;
  function addSet(verses, times, options) {
    verses.forEach(function (text, index) {
      var verse = index + 1;
      sections.push(losslessSection({
        id: pad(nextId++), slug: options.slug + "-verse-" + pad(verse), group: options.group,
        title: options.title + " · verse " + verse, sanskrit: options.reference + "." + verse,
        start: clock(times[index]), end: clock(times[index + 1]), audio: true,
        audioFile: "audio12/" + options.audioPrefix + "-" + pad(verse) + ".mp3",
        sourceVideo: options.source, mantra: text
      }));
    });
  }

  addSet(purusha, [27.11,49.16,71.05,94.27,115.13,135.45,155.58,174.94,198.52,219.85,242.17,261.17,282.38,301.73,324.18,343.62,370.25],
    { slug:"purusha", group:"1 · Puruṣa Sūkta · Ṛgveda 10.90", title:"Puruṣa Sūkta", reference:"Ṛgveda 10.90", audioPrefix:"purusha", source:sources.purusha });
  addSet(sriCore, [13.63,33.90,53.85,74.29,99.04,122.75,146.13,166.58,186.05,205.10,223.35,240.37,257.09,275.19,294.84,317.09],
    { slug:"sri-core", group:"2 · Śrī Sūkta · 15 core ṛks", title:"Śrī Sūkta", reference:"Śrī Sūkta", audioPrefix:"sri-core", source:sources.sri });
  addSet(sriPhalasruti, [317.09,339.62,356.98,374.51,393.09,418.81,436.45,457.04,477.16,493.91,514.21,553.57,570.05,590.47,607.23,630.94,647.75],
    { slug:"sri-phalasruti", group:"2 · Śrī Sūkta · Phalaśruti and closing verses", title:"Śrī Sūkta Phalaśruti", reference:"Phalaśruti", audioPrefix:"sri-phalasruti", source:sources.sri });
  addSet(ambhrini, [25.68,52.16,82.34,112.81,137.69,162.01,186.09,211.12,234.18],
    { slug:"ambhrini", group:"3 · Ambhṛṇī / Devī Sūkta · Ṛgveda 10.125", title:"Ambhṛṇī Sūkta", reference:"Ṛgveda 10.125", audioPrefix:"ambhrini", source:sources.ambhrini });
  addSet(balittha, [25.31,50.53,75.30,103.57,128.15,153.41],
    { slug:"balittha", group:"4 · Baḷitthā Sūkta · Ṛgveda 1.141.1–5", title:"Baḷitthā Sūkta", reference:"Ṛgveda 1.141", audioPrefix:"balittha", source:sources.balittha });

  manyu.forEach(function (verse, index) {
    sections.push(losslessSection({
      id: pad(nextId++), slug: "manyu-" + verse[0].replace("Ṛgveda ", "").replaceAll(".", "-").toLowerCase(),
      group: index < 7 ? "5 · Manyu Sūkta · Ṛgveda 10.83" : "5 · Manyu Sūkta · Ṛgveda 10.84",
      title: "Manyu Sūkta · " + verse[0], sanskrit: verse[0], start: clock(verse[1]), end: clock(verse[2]),
      audio: true, audioFile: "audio12/" + verse[3], sourceVideo: sources.manyu, mantra: verse[4]
    }));
  });

  (window.GUIDES = window.GUIDES || []).push({
    key: "panchasukta", tabLabel: "Pañcasūkta", title: "Pañcasūkta",
    subtitle: "Five complete sūktas · 74 individually replayable verse cards",
    source: sources.purusha, sourceLabel: "Puruṣa Sūkta audio",
    sourceCredit: "Puruṣa, Śrī, Ambhṛṇī, and Baḷitthā recitation: Mukund Sidhanti and Madhwesh Joshi · Manyu recitation: Śrī M. S. Venugopal and Śrī M. S. Sreenivasan, Challakere Brothers Official",
    noAudio: true, audioDir: "audio12", hideNotice: true, mantraLabel: "IAST",
    structuredMantraLabel: "IAST", hideLosslessReferences: true,
    practiceMode: "repeat3", practiceLabel: "↻ 3× Practice",
    sourceUnitLabel: "verse", sourceUnitPlural: "verses",
    searchPlaceholder: "Search the five sūktas or any verse…",
    searchAriaLabel: "Search verses", sections: sections
  });
})();
