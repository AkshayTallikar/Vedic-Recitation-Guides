// Pañcasūkta — the five complete recitation texts used in Mādhva pūjā.
// Puruṣa, Ambhṛṇī, Baḷitthā, and Manyu: Ṛgveda Saṃhitā.
// Śrī Sūkta: the standard fifteen-ṛk Ṛgveda Khila recension.
// Manyu audio: Challakere Brothers, complete Ṛgveda 10.83–10.84 recitation.

(function () {
  function losslessSection(section) {
    section.originalScript = section.mantra;
    section.structuredBlocks = [{
      kind: "mantra",
      sourceOriginal: section.mantra,
      text: section.mantra
    }];
    return section;
  }

  var purusha =
    "sahasraśīrṣā puruṣaḥ sahasrākṣaḥ sahasrapāt |\n" +
    "sa bhūmiṃ viśvato vṛtvā'tyatiṣṭhad daśāṅgulam || 1 ||\n\n" +
    "puruṣa evedaṃ sarvaṃ yad bhūtaṃ yac ca bhavyam |\n" +
    "utāmṛtatvasyeśāno yad annenātirohati || 2 ||\n\n" +
    "etāvān asya mahimā'to jyāyāṃś ca pūruṣaḥ |\n" +
    "pādo'sya viśvā bhūtāni tripādasyāmṛtaṃ divi || 3 ||\n\n" +
    "tripād ūrdhva udait puruṣaḥ pādo'syehābhavat punaḥ |\n" +
    "tato viṣvaṅ vyakrāmat sāśanānaśane abhi || 4 ||\n\n" +
    "tasmād virāḻ ajāyata virājo adhi pūruṣaḥ |\n" +
    "sa jāto atyaricyata paścād bhūmim atho puraḥ || 5 ||\n\n" +
    "yat puruṣeṇa haviṣā devā yajñam atanvata |\n" +
    "vasanto asyāsīd ājyaṃ grīṣma idhmaḥ śarad dhaviḥ || 6 ||\n\n" +
    "taṃ yajñaṃ barhiṣi praukṣan puruṣaṃ jātam agrataḥ |\n" +
    "tena devā ayajanta sādhyā ṛṣayaś ca ye || 7 ||\n\n" +
    "tasmād yajñāt sarvahutaḥ sambhṛtaṃ pṛṣadājyam |\n" +
    "paśūn tāṃś cakre vāyavyān āraṇyān grāmyāś ca ye || 8 ||\n\n" +
    "tasmād yajñāt sarvahuta ṛcaḥ sāmāni jajñire |\n" +
    "chandāṃsi jajñire tasmād yajus tasmād ajāyata || 9 ||\n\n" +
    "tasmād aśvā ajāyanta ye ke cobhayādataḥ |\n" +
    "gāvo ha jajñire tasmāt tasmāj jātā ajāvayaḥ || 10 ||\n\n" +
    "yat puruṣaṃ vyadadhuḥ katidhā vyakalpayan |\n" +
    "mukhaṃ kim asya kau bāhū kā ūrū pādā ucyete || 11 ||\n\n" +
    "brāhmaṇo'sya mukham āsīd bāhū rājanyaḥ kṛtaḥ |\n" +
    "ūrū tad asya yad vaiśyaḥ padbhyāṃ śūdro ajāyata || 12 ||\n\n" +
    "candramā manaso jātaś cakṣoḥ sūryo ajāyata |\n" +
    "mukhād indraś cāgniś ca prāṇād vāyur ajāyata || 13 ||\n\n" +
    "nābhyā āsīd antarikṣaṃ śīrṣṇo dyauḥ samavartata |\n" +
    "padbhyāṃ bhūmir diśaḥ śrotrāt tathā lokān akalpayan || 14 ||\n\n" +
    "saptāsyāsan paridhayas triḥ sapta samidhaḥ kṛtāḥ |\n" +
    "devā yad yajñaṃ tanvānā abadhnan puruṣaṃ paśum || 15 ||\n\n" +
    "yajñena yajñam ayajanta devās tāni dharmāṇi prathamāny āsan |\n" +
    "te ha nākaṃ mahimānaḥ sacanta yatra pūrve sādhyāḥ santi devāḥ || 16 ||";

  var sri =
    "oṃ hiraṇyavarṇāṃ hariṇīṃ suvarṇa-rajata-srajām |\n" +
    "candrāṃ hiraṇmayīṃ lakṣmīṃ jātavedo ma āvaha || 1 ||\n\n" +
    "tāṃ ma āvaha jātavedo lakṣmīm anapagāminīm |\n" +
    "yasyāṃ hiraṇyaṃ vindeyaṃ gām aśvaṃ puruṣān aham || 2 ||\n\n" +
    "aśvapūrvāṃ rathamadhyāṃ hastināda-pramodinīm |\n" +
    "śriyaṃ devīm upahvaye śrīr mā devī juṣatām || 3 ||\n\n" +
    "kāṃ so'smitāṃ hiraṇyaprākārām ārdrāṃ jvalantīṃ tṛptāṃ tarpayantīm |\n" +
    "padme sthitāṃ padmavarṇāṃ tām ihopahvaye śriyam || 4 ||\n\n" +
    "candrāṃ prabhāsāṃ yaśasā jvalantīṃ śriyaṃ loke devajuṣṭām udārām |\n" +
    "tāṃ padminīm īṃ śaraṇam ahaṃ prapadye 'lakṣmīr me naśyatāṃ tvāṃ vṛṇe || 5 ||\n\n" +
    "ādityavarṇe tapaso'dhijāto vanaspatis tava vṛkṣo'tha bilvaḥ |\n" +
    "tasya phalāni tapasā nudantu māyāntarāyāś ca bāhyā alakṣmīḥ || 6 ||\n\n" +
    "upaitu māṃ devasakhaḥ kīrtiś ca maṇinā saha |\n" +
    "prādurbhūto'smi rāṣṭre'smin kīrtim ṛddhiṃ dadātu me || 7 ||\n\n" +
    "kṣutpipāsāmalāṃ jyeṣṭhām alakṣmīṃ nāśayāmy aham |\n" +
    "abhūtim asamṛddhiṃ ca sarvāṃ nirṇuda me gṛhāt || 8 ||\n\n" +
    "gandhadvārāṃ durādharṣāṃ nityapuṣṭāṃ karīṣiṇīm |\n" +
    "īśvarīṃ sarvabhūtānāṃ tām ihopahvaye śriyam || 9 ||\n\n" +
    "manasaḥ kāmam ākūtiṃ vācaḥ satyam aśīmahi |\n" +
    "paśūnāṃ rūpam annasya mayi śrīḥ śrayatāṃ yaśaḥ || 10 ||\n\n" +
    "kardamena prajā bhūtā mayi sambhava kardama |\n" +
    "śriyaṃ vāsaya me kule mātaraṃ padmamālinīm || 11 ||\n\n" +
    "āpaḥ sṛjantu snigdhāni ciklīta vasa me gṛhe |\n" +
    "ni ca devīṃ mātaraṃ śriyaṃ vāsaya me kule || 12 ||\n\n" +
    "ārdrāṃ puṣkariṇīṃ puṣṭiṃ piṅgalāṃ padmamālinīm |\n" +
    "candrāṃ hiraṇmayīṃ lakṣmīṃ jātavedo ma āvaha || 13 ||\n\n" +
    "ārdrāṃ yaḥ kariṇīṃ yaṣṭiṃ piṅgalāṃ padmamālinīm |\n" +
    "sūryāṃ hiraṇmayīṃ lakṣmīṃ jātavedo ma āvaha || 14 ||\n\n" +
    "tāṃ ma āvaha jātavedo lakṣmīm anapagāminīm |\n" +
    "yasyāṃ hiraṇyaṃ prabhūtaṃ gāvo dāsyo'śvān vindeyaṃ puruṣān aham || 15 ||";

  var ambhrini =
    "ahaṃ rudrebhir vasubhiś carāmy aham ādityair uta viśvadevaiḥ |\n" +
    "ahaṃ mitrāvaruṇobhā bibharmy aham indrāgnī aham aśvinobhā || 1 ||\n\n" +
    "ahaṃ somam āhanasaṃ bibharmy ahaṃ tvaṣṭāram uta pūṣaṇaṃ bhagam |\n" +
    "ahaṃ dadhāmi draviṇaṃ haviṣmate suprāvye yajamānāya sunvate || 2 ||\n\n" +
    "ahaṃ rāṣṭrī saṃgamanī vasūnāṃ cikituṣī prathamā yajñiyānām |\n" +
    "tāṃ mā devā vyadadhuḥ purutrā bhūristhātrāṃ bhūry āveśayantīm || 3 ||\n\n" +
    "mayā so annam atti yo vipaśyati yaḥ prāṇiti ya īṃ śṛṇoty uktam |\n" +
    "amantavo māṃ ta upa kṣiyanti śrudhi śruta śraddhivaṃ te vadāmi || 4 ||\n\n" +
    "aham eva svayam idaṃ vadāmi juṣṭaṃ devebhir uta mānuṣebhiḥ |\n" +
    "yaṃ kāmaye taṃ tam ugraṃ kṛṇomi taṃ brahmāṇaṃ tam ṛṣiṃ taṃ sumedhām || 5 ||\n\n" +
    "ahaṃ rudrāya dhanur ā tanomi brahmadviṣe śarave hantavā u |\n" +
    "ahaṃ janāya samadaṃ kṛṇomy ahaṃ dyāvāpṛthivī ā viveśa || 6 ||\n\n" +
    "ahaṃ suve pitaram asya mūrdhan mama yonir apsv antaḥ samudre |\n" +
    "tato vi tiṣṭhe bhuvanānu viśvotāmūṃ dyāṃ varṣmaṇopa spṛśāmi || 7 ||\n\n" +
    "aham eva vāta iva pra vāmy ārabhamāṇā bhuvanāni viśvā |\n" +
    "paro divā para enā pṛthivyaitāvatī mahinā saṃ babhūva || 8 ||";

  var balittha =
    "baḻitthā tad vapuṣe dhāyi darśataṃ devasya bhargaḥ sahaso yato jani |\n" +
    "yad īm upa hvarate sādhate matir ṛtasya dhenā anayanta sasrutaḥ || 1 ||\n\n" +
    "pṛkṣo vapuḥ pitumān nitya ā śaye dvitīyam ā saptaśivāsu mātṛṣu |\n" +
    "tṛtīyam asya vṛṣabhasya dohase daśapramatiṃ janayanta yoṣaṇaḥ || 2 ||\n\n" +
    "nir yad īṃ budhnān mahiṣasya varpasa īśānāsaḥ śavasā kranta sūrayaḥ |\n" +
    "yad īm anu pradivo madhva ādhave guhā santaṃ mātariśvā mathāyati || 3 ||\n\n" +
    "pra yat pituḥ paramān nīyate pary ā pṛkṣudho vīrudho daṃsu rohati |\n" +
    "ubhā yad asya januṣaṃ yad invata ādid yaviṣṭho abhavad ghṛṇā śuciḥ || 4 ||\n\n" +
    "ādin mātṝr āviśad yāsv ā śucir ahiṃsyamāna urviyā vi vāvṛdhe |\n" +
    "anu yat pūrvā aruhat sanājuvo ni navyasīṣv avarāsu dhāvate || 5 ||\n\n" +
    "ādid dhotāraṃ vṛṇate diviṣṭiṣu bhagam iva papṛcānāsa ṛñjate |\n" +
    "devān yat kratvā majmanā puruṣṭuto martaṃ śaṃsaṃ viśvadhā veti dhāyase || 6 ||\n\n" +
    "vi yad asthād yajato vātacodito hvāro na vakvā jaraṇā anākṛtaḥ |\n" +
    "tasya patman dakṣuṣaḥ kṛṣṇajaṃhasaḥ śucijanmano raja ā vyadhvanaḥ || 7 ||\n\n" +
    "ratho na yātaḥ śikvabhiḥ kṛto dyām aṅgebhir aruṣebhir īyate |\n" +
    "ādasya te kṛṣṇāso dakṣi sūrayaḥ śūrasyeva tveṣathād īṣate vayaḥ || 8 ||\n\n" +
    "tvayā hy agne varuṇo dhṛtavrato mitraḥ śāśadre aryamā sudānavaḥ |\n" +
    "yat sīm anu kratunā viśvathā vibhur arān na nemiḥ paribhūr ajāyathāḥ || 9 ||\n\n" +
    "tvam agne śaśamānāya sunvate ratnaṃ yaviṣṭha devatātim invasi |\n" +
    "taṃ tvā nu navyaṃ sahaso yuvan vayaṃ bhagaṃ na kāre mahiratna dhīmahi || 10 ||\n\n" +
    "asme rayiṃ na svarthaṃ damūnasaṃ bhagaṃ dakṣaṃ na papṛcāsi dharṇasim |\n" +
    "raśmīṃr iva yo yamati janmanī ubhe devānāṃ śaṃsam ṛta ā ca sukratuḥ || 11 ||\n\n" +
    "uta naḥ sudyotmā jīrāśvo hotā mandraḥ śṛṇavac candrarathaḥ |\n" +
    "sa no neṣan neṣatamair amūro 'gnir vāmaṃ suvitaṃ vasyo accha || 12 ||\n\n" +
    "astāvy agniḥ śimīvadbhir arkaiḥ sāmrājyāya prataraṃ dadhānaḥ |\n" +
    "amī ca ye maghavāno vayaṃ ca mihaṃ na sūro ati niṣṭatanyuḥ || 13 ||";

  var manyuVerses = [
    {
      ref: "Ṛgveda 10.83.1", start: "0:17.55", end: "0:35.85",
      audioFile: "audio12/05-manyu-10-83-verse-1.mp3",
      text: "yas te manyo'vidhad vajra sāyaka saha ojaḥ puṣyati viśvam ānuṣak |\nsāhyāma dāsam āryaṃ tvayā yujā sahaskṛtena sahasā sahasvatā || 10.83.1 ||"
    },
    {
      ref: "Ṛgveda 10.83.2", start: "0:35.85", end: "0:56.85",
      audioFile: "audio12/06-manyu-10-83-verse-2.mp3",
      text: "manyur indro manyur evāsa devo manyur hotā varuṇo jātavedāḥ |\nmanyuṃ viśa īḻate mānuṣīr yāḥ pāhi no manyo tapasā sajoṣāḥ || 10.83.2 ||"
    },
    {
      ref: "Ṛgveda 10.83.3", start: "0:56.85", end: "1:14.65",
      audioFile: "audio12/07-manyu-10-83-verse-3.mp3",
      text: "abhīhi manyo tavasas tavīyān tapasā yujā vi jahi śatrūn |\namitrahā vṛtrahā dasyuhā ca viśvā vasūny ā bharā tvaṃ naḥ || 10.83.3 ||"
    },
    {
      ref: "Ṛgveda 10.83.4", start: "1:14.65", end: "1:34.75",
      audioFile: "audio12/08-manyu-10-83-verse-4.mp3",
      text: "tvaṃ hi manyo abhibhūtyojāḥ svayambhūr bhāmo abhimātiṣāhaḥ |\nviśvacarṣaṇiḥ sahuriḥ sahāvān asmāsv ojaḥ pṛtanāsu dhehi || 10.83.4 ||"
    },
    {
      ref: "Ṛgveda 10.83.5", start: "1:34.75", end: "1:55.10",
      audioFile: "audio12/09-manyu-10-83-verse-5.mp3",
      text: "abhāgaḥ sann apa pareto asmi tava kratvā taviṣasya pracetaḥ |\ntaṃ tvā manyo akratur jihīḻāhaṃ svā tanūr baladeyāya mehi || 10.83.5 ||"
    },
    {
      ref: "Ṛgveda 10.83.6", start: "1:55.10", end: "2:16.10",
      audioFile: "audio12/10-manyu-10-83-verse-6.mp3",
      text: "ayaṃ te asmy upa mehy arvāṅ pratīcīnaḥ sahure viśvadhāyaḥ |\nmanyo vajrinn abhi mām ā vavṛtsva hanāva dasyūṃr uta bodhy āpeḥ || 10.83.6 ||"
    },
    {
      ref: "Ṛgveda 10.83.7", start: "2:16.10", end: "2:34.10",
      audioFile: "audio12/11-manyu-10-83-verse-7.mp3",
      text: "abhi prehi dakṣiṇato bhavā me'dhā vṛtrāṇi jaṅghanāva bhūri |\njuhomi te dharuṇaṃ madhvo agram ubhā upāṃśu prathamā pibāva || 10.83.7 ||"
    },
    {
      ref: "Ṛgveda 10.84.1", start: "2:34.10", end: "2:55.40",
      audioFile: "audio12/12-manyu-10-84-verse-1.mp3",
      text: "tvayā manyo saratham ārujanto harṣamāṇāso dhṛṣitā marutvaḥ |\ntigmeṣava āyudhā saṃśiśānā abhi pra yantu naro agnirūpāḥ || 10.84.1 ||"
    },
    {
      ref: "Ṛgveda 10.84.2", start: "2:55.40", end: "3:14.90",
      audioFile: "audio12/13-manyu-10-84-verse-2.mp3",
      text: "agnir iva manyo tviṣitaḥ sahasva senānīr naḥ sahure hūta edhi |\nhatvāya śatrūn vi bhajasva veda ojo mimāno vi mṛdho nudasva || 10.84.2 ||"
    },
    {
      ref: "Ṛgveda 10.84.3", start: "3:14.90", end: "3:34.00",
      audioFile: "audio12/14-manyu-10-84-verse-3.mp3",
      text: "sahasva manyo abhimātim asme rujan mṛṇan pramṛṇan prehi śatrūn |\nugraṃ te pājo nanv ā rurudhre vaśī vaśaṃ nayasa ekaja tvam || 10.84.3 ||"
    },
    {
      ref: "Ṛgveda 10.84.4", start: "3:34.00", end: "3:53.20",
      audioFile: "audio12/15-manyu-10-84-verse-4.mp3",
      text: "eko bahūnām asi manyav īḻito viśaṃ viśaṃ yudhaye saṃ śiśādhi |\nakṛttaruk tvayā yujā vayaṃ dyumantaṃ ghoṣaṃ vijayāya kṛṇmahe || 10.84.4 ||"
    },
    {
      ref: "Ṛgveda 10.84.5", start: "3:53.20", end: "4:13.75",
      audioFile: "audio12/16-manyu-10-84-verse-5.mp3",
      text: "vijeṣakṛd indra ivānavabravo'smākaṃ manyo adhipā bhaveha |\npriyaṃ te nāma sahure gṛṇīmasi vidmā tam utsaṃ yata ābabhūtha || 10.84.5 ||"
    },
    {
      ref: "Ṛgveda 10.84.6", start: "4:13.75", end: "4:33.30",
      audioFile: "audio12/17-manyu-10-84-verse-6.mp3",
      text: "ābhūtyā sahajā vajra sāyaka saho bibharṣy abhibhūta uttaram |\nkratvā no manyo saha medyedhi mahādhanasya puruhūta saṃsṛji || 10.84.6 ||"
    },
    {
      ref: "Ṛgveda 10.84.7", start: "4:33.30", end: "4:53.90",
      audioFile: "audio12/18-manyu-10-84-verse-7.mp3",
      text: "saṃsṛṣṭaṃ dhanam ubhayaṃ samākṛtam asmabhyaṃ dattāṃ varuṇaś ca manyuḥ |\nbhiyaṃ dadhānā hṛdayeṣu śatravaḥ parājitāso apa ni layantām || 10.84.7 ||"
    }
  ];

  var sections = [
    losslessSection({
      id: "01", slug: "purusha-sukta", group: "1 · Puruṣa Sūkta",
      title: "Complete Puruṣa Sūkta · 16 ṛks", sanskrit: "पुरुष सूक्तम् · Ṛgveda 10.90",
      mantra: purusha,
      meaning: "The complete sixteen-ṛk Ṛgvedic hymn to the Cosmic Person, used for the principal abhiṣeka in Deva Pūjā."
    }),
    losslessSection({
      id: "02", slug: "sri-sukta", group: "2 · Śrī Sūkta",
      title: "Complete Śrī Sūkta · 15 ṛks", sanskrit: "श्री सूक्तम् · Ṛgveda Khila",
      mantra: sri,
      meaning: "The complete core fifteen-ṛk Śrī Sūkta recension used to invoke and worship Śrī Mahālakṣmī."
    }),
    losslessSection({
      id: "03", slug: "ambhrini-sukta", group: "3 · Ambhṛṇī Sūkta",
      title: "Complete Ambhṛṇī / Devī Sūkta · 8 ṛks", sanskrit: "अम्भृणी / देवी सूक्तम् · Ṛgveda 10.125",
      mantra: ambhrini,
      meaning: "The complete hymn in which Vāk Ambhṛṇī proclaims the Goddess's all-pervading sovereignty."
    }),
    losslessSection({
      id: "04", slug: "balittha-sukta", group: "4 · Baḷitthā Sūkta",
      title: "Complete Baḷitthā Sūkta · 13 ṛks", sanskrit: "बळित्था सूक्तम् · Ṛgveda 1.141",
      mantra: balittha,
      meaning: "The complete hymn to Agni, traditionally recited for the abhiṣeka of Mukhyaprāṇa in Mādhva Deva Pūjā."
    })
  ];

  manyuVerses.forEach(function (verse, index) {
    var hymnVerse = index < 7 ? index + 1 : index - 6;
    sections.push(losslessSection({
      id: String(index + 5).padStart(2, "0"),
      slug: index < 7 ? "manyu-10-83-verse-" + hymnVerse : "manyu-10-84-verse-" + hymnVerse,
      group: index < 7 ? "5 · Manyu Sūkta · Ṛgveda 10.83" : "5 · Manyu Sūkta · Ṛgveda 10.84",
      title: "Manyu Sūkta · " + verse.ref,
      sanskrit: verse.ref,
      start: verse.start,
      end: verse.end,
      audio: true,
      audioFile: verse.audioFile,
      mantra: verse.text
    }));
  });

  (window.GUIDES = window.GUIDES || []).push({
    key: "panchasukta",
    tabLabel: "Pañcasūkta",
    title: "Pañcasūkta",
    subtitle: "Puruṣa · Śrī · Ambhṛṇī · Baḷitthā · complete Manyu Sūkta verse practice",
    source: "https://www.youtube.com/watch?v=CIHdtjXrnP8",
    sourceLabel: "Manyu audio",
    sourceCredit: "Texts: Ṛgveda Saṃhitā and the fifteen-ṛk Śrī Sūkta · Manyu recitation: Śrī M. S. Venugopal and Śrī M. S. Sreenivasan, Challakere Brothers Official",
    noAudio: true,
    audioDir: "audio12",
    hideNotice: true,
    mantraLabel: "IAST",
    structuredMantraLabel: "IAST",
    hideLosslessReferences: true,
    practiceMode: "repeat3",
    practiceLabel: "↻ 3× Practice",
    searchPlaceholder: "Search the five sūktas or a Manyu verse…",
    sections: sections
  });
})();
