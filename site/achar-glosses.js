// Line-aligned Sanskrit meanings and lexical glosses for the 56-minute guide.
// Loaded after site/data.js. Text is taken verbatim from each guide mantra so
// that rendered line breaks remain synchronized with the recitation display.
// Audio has not been independently verified; consult the recording for variants.
(function () {
  const dictionary = {
    "oṃ":'sacred syllable Oṃ', "namaḥ":'salutation', "namo":'salutation', "astu":'may there be', "te":'to you', "ca":'and', "tu":'indeed', "api":'also', "eva":'indeed', "atha":'then', "hi":'for', "yat":'which/that', "yaḥ":'who', "ye":'who (plural)', "yā":'who/which (feminine)', "sa":'that/he', "tam":'that one', "me":'to me / my', "mā":'me / do not', "tvam":'you', "tava":'your', "aham":'I', "ayam":'this', "idam":'this', "atra":'here', "tatra":'there', "iti":'thus', "svāhā":'offering; svāhā', "samarpayāmi":'I offer', "samarpayāmaḥ":'we offer', "viniyogaḥ":'ritual application', "ṛṣiḥ":'seer', "devatā":'deity', "chandaḥ":'metre', "mantrasya":'of the mantra', "mantram":'mantra', "jape":'in recitation', "namaḥ":'salutation', "pūjā":'worship', "pūjām":'worship', "deva":'O Lord / deity', "devān":'the gods', "devāḥ":'gods', "devatāḥ":'deities', "bhagavān":'the Blessed Lord', "viṣṇuḥ":'Viṣṇu', "viṣṇum":'Viṣṇu', "viṣṇo":'O Viṣṇu', "hariḥ":'Hari', "harim":'Hari', "nārāyaṇāya":'to Nārāyaṇa', "nārāyaṇa":'Nārāyaṇa', "lakṣmī":'Lakṣmī', "śriyai":'to Śrī (Lakṣmī)', "śriyam":'Śrī (Lakṣmī)', "śrī":'Śrī', "ramā":'Ramā (Lakṣmī)', "ramā-pate":'O Lord of Ramā', "govinda":'Govinda', "govindam":'Govinda', "kṛṣṇa":'Kṛṣṇa', "acyuta":'Acyuta, the infallible Lord', "ananta":'Ananta, the endless Lord', "brahmā":'Brahmā', "brahma":'Brahman / sacred reality', "vāyu":'Vāyu', "vāyave":'to Vāyu', "garuḍa":'Garuḍa', "śeṣa":'Śeṣa', "rudraḥ":'Rudra', "indra":'Indra', "agni":'Agni', "agnau":'in Agni', "agninā":'by Agni', "jātavedaḥ":'Jātavedas (Agni)', "jātavedo":'O Jātavedas (Agni)', "bhūḥ":'earth / terrestrial realm', "bhuvaḥ":'atmosphere', "svaḥ":'heaven', "svarga":'heaven', "pṛthvī":'Earth', "pṛthvi":'O Earth', "devi":'O Goddess', "devī":'Goddess', "viśve":'all the', "viśvā":'all', "sarva":'all', "sarve":'all', "sarvam":'everything', "samasta":'entire', "mahā":'great', "param":'supreme', "parama":'supreme', "paraḥ":'beyond / supreme', "uttama":'highest', "śubham":'auspicious', "śubha":'auspicious', "puṇya":'merit / holiness', "pāpa":'sin', "doṣa":'fault', "doṣāḥ":'faults', "karma":'action / ritual act', "kriyā":'rite / action', "bhakti":'devotion', "jñāna":'knowledge', "sukha":'happiness', "ānanda":'bliss', "śānti":'peace', "śāntim":'peace', "dharma":'dharma / sacred duty', "satyaṃ":'truth', "ṛtena":'by cosmic order / truth', "vedaḥ":'Veda', "vedāḥ":'Vedas', "yajña":'sacrifice', "yajñaiḥ":'with sacrifices', "havis":'oblation', "haviṣmate":'to the offerer of oblations', "mantra":'mantra', "nāma":'name', "nāmnā":'by the name', "padam":'step / state', "pāda":'foot', "pādau":'feet', "caraṇam":'feet', "caraṇau":'two feet', "kamala":'lotus', "paṅkajam":'lotus', "netra":'eye', "locana":'eye', "mukha":'face / mouth', "hṛt":'heart', "hṛdaya":'heart', "manasā":'with the mind', "manaḥ":'mind', "vāca":'speech', "vacasā":'with speech', "śirasā":'with the head', "urasā":'with the chest', "dṛṣṭyā":'with the sight', "pādbhyām":'with the feet', "karābhyām":'with the hands', "jānubhyām":'with the knees', "pradakṣiṇa":'circumambulation', "pradakṣiṇe":'in circumambulation', "pade":'at each step', "kṣamasva":'please forgive', "rakṣa":'protect', "pāhi":'protect', "prasīda":'be gracious', "prasīdatām":'may be pleased', "prīyatām":'may be pleased', "gṛhāṇa":'please accept', "gṛhṇātu":'may accept', "dadātu":'may grant', "kuru":'please make / do', "kuruṣva":'please perform', "āvaha":'bring here', "āyāhi":'come here', "āyāntu":'may they come', "āgaccha":'come', "uttiṣṭha":'arise', "namāmi":'I bow', "vande":'I salute', "bhaje":'I worship', "dhyātvā":'having meditated', "dhyāna":'meditation', "dhyānam":'meditation', "āvāhana":'invocation', "āsana":'seat', "āsanam":'seat', "pādyam":'water for the feet', "arghyam":'welcoming water', "ācamanīyam":'water for sipping', "snānam":'bath', "abhiṣeka":'ritual bathing', "gandham":'fragrant sandal paste', "puṣpam":'flower', "puṣpaṃ":'flower', "puṣpaiḥ":'with flowers', "tulasī":'tulasī', "dhūpam":'incense', "dīpam":'lamp', "naivedyam":'food offering', "tāmbūlam":'betel offering', "chatram":'parasol', "cāmaram":'fly-whisk', "vyajanam":'fan', "darpaṇam":'mirror', "gītam":'song', "nṛtyam":'dance', "vādyam":'instrumental music', "stotram":'hymn', "rāja":'royal', "upacāra":'service / courtesy', "upacārān":'services', "upacāraiḥ":'with services', "śoḍaśa":'sixteen', "aṣṭa":'eight', "aṣṭāṅga":'eight-limbed', "aṣṭākṣara":'eight-syllabled', "mantra-hīnaṃ":'lacking mantra', "kriyā-hīnaṃ":'lacking ritual action', "bhakti-hīnaṃ":'lacking devotion', "puṇḍarīkākṣa":'Lotus-eyed Lord', "janārdana":'Janārdana, protector of people', "puruṣottama":'Supreme Person', "bhakta":'devotee', "bhaktānām":'of devotees', "dāsa":'servant', "dāso":'servant', "śaraṇam":'refuge', "śaraṇāgata":'one who has sought refuge', "śaraṇāgatavatsala":'tender toward those who seek refuge', "ananta":'endless', "sahasra":'thousand', "mūrti":'form', "mūrtiḥ":'form', "rūpa":'form', "rūpam":'form', "guṇa":'quality', "guṇaiḥ":'with qualities', "guṇānām":'of qualities', "ātmā":'self', "ātman":'self', "ātma":'self', "sarvātmā":'Self of all', "antarātman":'inner Self', "parātmā":'Supreme Self', "nitya":'eternal', "nityam":'eternally', "śāśvata":'eternal', "aja":'unborn', "ajaḥ":'unborn Lord', "akhaṇḍa":'undivided', "pūrṇa":'complete', "pūrṇam":'complete', "śuddha":'pure', "pavitra":'pure', "amṛta":'immortal nectar', "amṛtam":'nectar', "jala":'water', "jalam":'water', "āpaḥ":'waters', "nīra":'water', "tīrtha":'sacred water', "kalaśa":'water-pot', "mukhe":'at the mouth', "kaṇṭhe":'at the neck', "mūle":'at the base', "madhye":'in the middle', "kukṣau":'in the belly', "śaṅkha":'conch', "śaṅkham":'conch', "ghaṇṭā":'bell', "ghaṇṭā-ravam":'bell-sound', "bhūta":'spirit / being', "bhūtāḥ":'beings', "rākṣasa":'demon', "rākṣasāḥ":'demons', "vighna":'obstacle', "vighna-kartāraḥ":'obstacle-makers', "naśyantu":'may they perish', "apasarpantu":'may they depart', "śivājñayā":'by the command of Śiva', "avirodhena":'without opposition', "ārādhyase":'you are worshipped', "prasāda":'grace', "prasādataḥ":'by grace', "kāruṇya":'compassion', "karuṇā":'compassion', "kṛpā":'mercy', "nidhe":'O treasure', "karuṇāmṛta":'nectar of compassion', "śītalābhyām":'with the cool (eyes)', "viśālābhyām":'with the wide (eyes)', "āyatābhyām":'with the expansive (eyes)', "locanābhyām":'with the two eyes', "vilokaya":'look upon', "śilā":'stone', "sālagrāma":'Sālagrāma', "sālagrāma-nivāsāya":'to the one dwelling in the Sālagrāma', "kṣīrābdhi":'ocean of milk', "śayana":'reclining', "śayanāya":'to the one reclining', "nivāsāya":'to the one dwelling', "namaḥ":'salutation', "hiraṇya":'gold', "hiraṇyaṃ":'gold', "hiraṇya-varṇām":'golden-hued (feminine)', "hariṇīm":'radiant (feminine)', "suvarṇa":'gold', "rajata":'silver', "srajām":'garlands', "candrām":'moonlike', "hiraṇmayīm":'golden', "lakṣmīm":'Lakṣmī', "anapagāminīm":'one who does not depart', "gām":'cow', "aśvam":'horse', "puruṣān":'people / men', "vindeyam":'may I obtain', "āvaha":'bring', "somam":'Soma', "agnim":'Agni', "mitra":'Mitra', "varuṇa":'Varuṇa', "indrāgnī":'Indra and Agni', "aśvinau":'the two Aśvins', "vasubhiḥ":'with the Vasus', "rudrebhiḥ":'with the Rudras', "ādityaiḥ":'with the Ādityas', "viśvadevaiḥ":'with all the gods', "carāmi":'I move / range', "bibharmi":'I uphold / bear', "dadhāmi":'I place / bestow', "rāṣṭrī":'sovereign queen', "saṅgamanī":'assembler / bringer together', "vasūnām":'of riches / Vasus', "cikituṣī":'knowing', "yajñiyānām":'of those worthy of sacrifice', "devāḥ":'gods', "vyadadhuḥ":'distributed / appointed', "purutrā":'in many places', "bhūri":'abundant', "sthātrām":'abiding', "āveśayantīm":'causing to enter', "prayaccha":'grant', "bhadrām":'auspicious', "svasti":'well-being', "gāvaḥ":'cows', "aśvāḥ":'horses', "putrāḥ":'sons', "pautrāḥ":'grandsons', "dhana":'wealth', "dhanam":'wealth', "āyuḥ":'life-span', "kīrti":'fame', "prajā":'offspring', "prasū":'mother', "mātā":'mother', "pitā":'father', "pitar":'O father', "bandhu":'kinsman', "guru":'teacher', "bhrātṛ":'brother', "svāmin":'O Lord', "sarva":'all', "antar":'within', "ajara":'ageless', "jarayitar":'ageing / destroyer', "janma":'birth', "mṛtyu":'death', "āmayānām":'of diseases', "dehi":'give', "bhaktiṃ":'devotion', "ūrjitām":'strong', "nirnimittām":'without ulterior motive', "nirvyājām":'without pretense', "niścalām":'steadfast', "sadguṇa":'good qualities', "bṛhatīm":'great / abundant', "śāśvatīm":'eternal', "āśu":'quickly', "devāya":'to the god', "śrīnivāsa":'Śrīnivāsa', "nitya-tṛpta":'ever content', "gṛhāṇa":'accept', "kṛpayā":'mercifully', "bhakta-vatsala":'affectionate to devotees', "prāṇāya":'to the life-breath', "apānāya":'to the downward breath', "vyānāya":'to the diffusive breath', "udānāya":'to the upward breath', "samānāya":'to the equalizing breath', "vāsudevāya":'to Vāsudeva', "saṃkarṣaṇāya":'to Saṃkarṣaṇa', "pradyumnāya":'to Pradyumna', "aniruddhāya":'to Aniruddha', "annam":'food', "mahā-naivedyam":'great food offering', "uttamam":'excellent', "upastaraṇam":'underlay / covering', "amṛta-upastaraṇam":'nectar as a covering', "pariṣiñcāmi":'I sprinkle all around', "satyam":'truth', "parikṣecana":'sprinkling around', "rājan":'king', "rājā":'king', "rāje":'to the king', "kāmān":'desires', "kāma":'desire', "kāmeśvara":'lord of desires', "kubera":'Kubera', "vaiśravaṇa":'Vaiśravaṇa', "prasahya":'mightily', "sāhine":'to the conqueror', "āyuṣyam":'long life', "pāpmā":'sinful', "pāpī":'sinful', "pāpaḥ":'sin', "trāhi":'save', "anyat":'another', "nāsti":'there is not', "eva":'indeed', "tasmāt":'therefore', "kṣamasva":'forgive', "kāryam":'to be done', "kartā":'doer', "akartā":'non-doer', "hariḥ":'Hari', "prasiddham":'well-known', "viśvodayasthitilaya":'creation, maintenance, and dissolution of the universe', "pradāya":'giver', "prabhūta":'abundant', "nārāyaṇa":'Nārāyaṇa', "paripūrṇa":'fully complete', "guṇārṇava":'ocean of qualities', "jñāna-pradāya":'to the giver of knowledge', "vibudha":'gods', "asura":'demons', "saukhya":'happiness', "duḥkha":'sorrow', "sat-kāraṇa":'true cause', "vitata":'all-pervading', "namas":'salutation', "namas te":'salutations to you', "vande":'I salute', "namāmi":'I bow', "indirā":'Indirā (Lakṣmī)', "patim":'lord', "ādyādi":'the first and others', "vara":'boon', "deśa":'place', "pradam":'giver', "nikhila":'all', "adhīśa":'lord', "kirīṭa":'crown', "ghṛṣṭa":'rubbed / touched', "pīṭhavat":'like a seat', "tamaḥ":'darkness', "śamane":'in removing', "arka":'sun', "ābhaṃ":'radiance', "pāda-paṅkajam":'lotus feet', "prītaye":'for affection / pleasure', "suhṛt":'friend', "jaya":'victory', "jayati":'is victorious', "jayaty":'is victorious', "ajo":'unborn Lord', "sadā":'always', "uditaḥ":'risen / shining', "jñāna":'knowledge', "marīci":'ray', "mālī":'garlanded', "sva":'one’s own', "bhakta":'devotee', "hārd":'of the heart', "ucca":'high', "tamaḥ":'darkness', "nihantā":'destroyer', "vyāsa":'Vyāsa', "avatāra":'descent / incarnation', "ātma":'self', "bhāskara":'sun', "akṣīṇa":'undiminished', "sukha":'bliss', "bimbaḥ":'orb / image', "aiśvarya":'sovereignty', "kānti":'splendour', "pratataḥ":'extended', "santāpa":'distress', "duriṣṭa":'misfortune', "hantā":'destroyer', "rāma":'Rāma', "īśa":'Lord', "candramāḥ":'moon', "asaṃkhya":'countless', "bala":'strength', "ambu":'water', "pūraḥ":'flood', "guṇocca":'lofty qualities', "ratnākaraḥ":'ocean of jewels', "vaibhavaḥ":'majesty', "sadātma":'eternal self', "dībhir":'with lamps', "āpyaḥ":'attainable', "eka":'one', "sāgaraḥ":'ocean', "brahmaṇya":'devoted to Brahmins / sacred order', "hitāya":'for the welfare', "jagat":'world', "kalyāṇa":'auspicious', "adbhuta":'wondrous', "gātrāya":'to the form', "kāmitārtha":'desired aims', "pradāyine":'to the giver', "veṅkaṭanāthāya":'to Veṅkaṭanātha', "śrīnivāsāya":'to Śrīnivāsa', "pāpam":'sin', "janmāntara":'former birth', "kṛtāni":'done', "vinaśyanti":'are destroyed', "pradakṣiṇa-pade":'with each circumambulatory step', "tīrtha-koṭi":'millions of sacred waters', "sahasrāṇi":'thousands', "vrata-koṭi":'millions of vows', "śatāni":'hundreds', "praṇāmasya":'of a prostration', "kalām":'fraction', "nārhanti":'are not worthy of', "ṣoḍaśīm":'a sixteenth part', "ucyate":'is called', "sarvaguṇasampūrṇaḥ":'complete in all good qualities', "sarvadoṣavivarjitaḥ":'free from every defect', "abhaya":'fearlessness', "dāna":'gift', "dayā":'compassion', "vibhūti":'glory', "bhūmi":'earth', "ākāśa":'sky', "sūrya":'sun', "soma":'moon / Soma', "vāri":'water', "megha":'cloud', "puṣṭi":'nourishment', "dhruva":'steadfast / pole star', "svāhā":'offering; svāhā', "idaṃ":'this', "namaḥ":'salutation', "idaṃ namaḥ":'this is offered; salutations', "nārāyaṇāya":'to Nārāyaṇa', "prāṇātmane":'to the indwelling life-breath', "apānātmane":'to the indwelling downward breath', "vyānātmane":'to the indwelling diffusive breath', "udānātmane":'to the indwelling upward breath', "samānātmane":'to the indwelling equalizing breath', "mantra-tantra":'mantra and ritual method', "svara":'accent', "varṇa":'syllable', "lopa":'omission', "doṣa":'fault', "prāyaścitta":'atonement', "nāmatraya":'three names', "kariṣye":'I shall perform', "anena":'by this', "ṣoḍaśopacāra":'sixteen services', "pūjanena":'by worship', "prītyartham":'for the pleasure of', "preraṇayā":'by the prompting of', "bhagavataḥ":'of the Lord', "vīryeṇa":'by strength / potency', "balena":'by strength', "tejasā":'by splendour', "karmaṇā":'by action', "preritoham":'I am impelled', "yathā":'as / according to', "militopacāra":'available services', "dravyaiḥ":'with materials', "dhyānāvāhanādi":'beginning with meditation and invocation', "kariṣye":'I shall perform', "brahmaṇe":'to Brahmā', "ramāyai":'to Ramā', "śeṣāya":'to Śeṣa', "garuḍāya":'to Garuḍa', "kumudāya":'to Kumuda', "jayāya":'to Jaya', "vijayāya":'to Vijaya', "balāya":'to Bala', "prabalāya":'to Prabala', "nandāya":'to Nanda', "sunandāya":'to Sunanda', "kumudākṣāya":'to Kumudākṣa', "śriyai":'to Śrī', "arcata":'worship', "prarcata":'worship well', "āgamārtham":'for the coming', "gamanārtham":'for the departure', "rakṣasām":'of the demons', "devānām":'of the gods', "kuru":'make / perform', "ghaṇṭā-ravam":'bell sound', "devatā-āhvāna":'invitation of the deities', "lāñchanam":'sign / token', "tapta":'molten / glowing', "jvalat":'blazing', "kāñcana":'gold', "racitam":'made', "tuṅga":'lofty', "aṅga":'part', "raṅga-sthalam":'performance hall', "śuddha":'pure', "sphāṭika":'crystal', "bhitti":'wall', "kavilasitaiḥ":'shining', "stambhaiḥ":'with pillars', "manojñaiḥ":'beautiful', "śubhaiḥ":'auspicious', "dvāraiḥ":'with doorways', "ratna":'jewel', "rāja":'excellent', "khacitaiḥ":'inlaid', "śobhāvaham":'splendid', "maṇḍitaiḥ":'adorned', "śaṅkha":'conch', "padma":'lotus', "dhavala":'white', "svastikaiḥ":'with auspicious svastikas', "muktā":'pearls', "jāla":'net / strings', "vilambi":'hanging', "maṇṭapa":'pavilion', "yutam":'endowed with', "vajra":'diamond', "sopānakaiḥ":'with stairways', "nānā":'various', "vinirmitaiḥ":'made', "kalaśaiḥ":'with pots', "atyanta":'exceedingly', "māṇikya":'ruby', "ujjvala":'bright', "dīpa":'lamp', "dīpta":'shining', "vilasat":'radiant', "lakṣmī":'Lakṣmī', "vilāsa":'play / splendour', "āspadam":'abode', "maṇṭapam":'pavilion', "arcaneṣu":'in worship', "sakalaiḥ":'all', "sādhakaiḥ":'by practitioners', "sammārjanaiḥ":'with sweeping', "raṅgavalī":'decorative floor design', "dhvaja":'flag', "ketakī":'banner', "toraṇaiḥ":'with festoons', "vitānaiḥ":'with canopies', "ikṣu":'sugarcane', "kadalī":'banana plant', "pūrṇa":'full', "kumbha":'pot', "aṅkura":'sprout', "gīta":'song', "vāditra":'instrumental music', "nṛtya":'dance', "purāṇa":'Purāṇa', "paṭhanaiḥ":'with recitations', "vardhamānam":'increasing', "manoharam":'delightful', "śobhamānam":'beautiful', "mahāpuṇyam":'greatly auspicious'
  };

  // Forms occurring in the reviewed late-pūjā passages.  This uses the exact
  // displayed spellings (including the recording transcription's variants),
  // so the token rows never fall back to an unhelpful placeholder.
  Object.assign(dictionary, {
    'ahaṃ':'I', 'rudrebhir':'with the Rudras', 'vasubhiś':'with the Vasus', 'carāmy':'I move', 'ādityair':'with the Ādityas', 'uta':'and/also',
    'mitrāvaruṇobhā':'the pair Mitra and Varuṇa', 'bibharmy':'I uphold/bear', 'aśvinobhā':'the pair of Aśvins', 'āhanasaṃ':'the smiter/crusher',
    'tvaṣṭāram':'Tvaṣṭṛ', 'pūṣaṇaṃ':'Pūṣan', 'bhagam':'Bhaga', 'draviṇaṃ':'wealth', 'suprāvye':'the generous one', 'yajamānāya':'to the sacrificer',
    'sunvate':'to the Soma-presser', 'vasūnāṃ':'of treasures/the Vasus', 'prathamā':'foremost', 'tāṃ':'me/her', 'devā':'the gods',
    'bhūristhātrāṃ':'abiding extensively', 'bhūry':'abundantly',
    'hiraṇyavarṇāṃ':'golden-hued', 'hariṇīṃ':'shining/tawny one', 'suvarṇarajatasrajām':'wearing gold-and-silver garlands',
    'candrāṃ':'moonlike/radiant', 'hiraṇmayīṃ':'golden', 'lakṣmīṃ':'Lakṣmī', 'jātavedō':'O Jātavedas (Agni)', 'ma':'to me',
    'lakṣmīmanapagāminīm':'Lakṣmī, the one who never departs', 'yasyāṃ':'in/through whom', 'vindēyaṃ':'may I obtain',
    'gāmaśvaṃ':'cattle and horses', 'puruṣānaham':'people, I', 'aśvapūrvāṃ':'preceded by horses', 'rathamadhyāṃ':'amid chariots',
    'hastinādapramōdinīm':'delighted by elephant trumpeting', 'śriyaṃ':'Śrī', 'dēvīmupahvayē':'I invoke the goddess', 'śrīrmā':'Śrī in me/to me',
    'dēvī':'goddess', 'juṣatām':'may she be pleased with',
    'baḷ':'indeed/strongly', 'itthā':'thus', 'tad':'that', 'vapuṣe':'for the form', 'dhāyi':'was established', 'darśataṃ':'splendid/visible',
    'devasya':'of the god', 'bhargaḥ':'radiance', 'sahaso':'from might', 'yato':'from which', 'jani':'was born', 'yad':'when/which',
    'īm':'him', 'upa':'toward', 'hvarate':'turns', 'sādhate':'succeeds/attains', 'matir':'thought', 'ṛtasya':'of truth/cosmic order',
    'dhenā':'milk-cow', 'anayanta':'they bring', 'sasrutaḥ':'flowing streams', 'pṛkṣo':'nourishing/abundant', 'vapuḥ':'form',
    'pitumān':'possessing nourishment', 'ā':'in/to', 'śaye':'lies/rests', 'dvitīyam':'the second', 'saptaśivāsu':'among seven blessed ones',
    'mātṛṣu':'among mothers', 'tṛtīyam':'the third', 'asya':'of this', 'vṛṣabhasya':'of the bull', 'dohase':'for milking',
    'daśapramatiṃ':'tenfold insight', 'janayanta':'bring forth', 'yoṣaṇaḥ':'women', 'mātar':'O mother', 'mātariśvan':'O Mātariśvan/Vāyu',
    'atula-guro':'O incomparable guru', 'bhrātar':'O brother', 'iṣṭāpta-bandho':'O beloved and intimate kinsman',
    'sarvāntarātmann':'inner Self of all', 'janma-mṛty-āmayānām':'of birth, death, and disease', 'govinde':'in/to Govinda',
    'bhavati':'in you', 'bhagavann':'O Lord', 'ūrjitāṃ':'strong', 'nirnimittāṃ':'without ulterior motive', 'nirvyājāṃ':'without pretense',
    'niścalāṃ':'unwavering', 'sad-guṇa-gaṇa-bṛhatīṃ':'rich in hosts of noble qualities',
    'garuḍa-devatābhyo':'to the Garuḍa deity', 'śeṣa-devatābhyo':'to the Śeṣa deity',
    'tapta-jvalat-kāñcana-racitaṃ':'made of molten blazing gold', 'tuṅgāṅga-raṅga-sthalaṃ':'lofty performance hall',
    'śuddha-sphāṭika-bhitti-kavilasitaiḥ':'shining against walls of pure crystal', 'stambhair':'with pillars', 'dvāraiś':'with doorways',
    'ratna-rāja-khacitaiḥ':'inlaid with the finest jewels', 'śobhāvahaṃ':'bringing splendor', 'tatrānyair':'there, also with other',
    'śaṅkha-padma-dhavalaiḥ':'white like conches and lotuses', 'prabhrājitaṃ':'shining forth',
    'muktā-jāla-vilambi-maṇṭapa-yutaṃ':'having a pavilion hung with nets of pearls', 'vajra-sopānakaiḥ':'with diamond stairways',
    'nānā-ratna-vinirmitaiś':'made from many jewels', 'kalaśair':'with pots', 'atyanta-śobhāvaham':'surpassingly splendid',
    'māṇiky-ujjvala-dīpa-dīpta-vilasat-lakṣmī-vilāsāspadam':'radiant abode of Lakṣmī’s splendor, lit by ruby lamps',
    'yāyen':'may it be used', 'sakalair':'by all', 'evaṃ-vidhaiḥ':'of this kind', 'sammārjanai':'with sweeping',
    'raṅgavalī-dhvaja-ketakī-toraṇaiḥ':'with floor designs, flags, ketakī, and festoons',
    'vitānair':'with canopies', 'ikṣu-kadalī-pūrṇa-kumbhāṅkurādibhiḥ':'with sugarcane, banana plants, full pots, sprouts, and the rest',
    'gīta-vāditra-nṛtyaiś':'with song, instrumental music, and dance', 'purāṇa-paṭhanaiḥ':'with Purāṇa recitations',
    'śobhamānaṃ':'beautiful', 'mahāpuṇyaṃ':'greatly holy', 'vardhamānaṃ':'ever increasing',
    'ni':'down', 'ṣu':'well', 'sīda':'sit', 'gaṇapate':'O lord of hosts', 'gaṇeṣu':'among the hosts', 'tvām':'you', 'āhur':'they call',
    'vipratamaṃ':'wisest/most inspired', 'kavīnām':'of the seers', 'na':'not', 'ṛte':'without', 'tvat':'you', 'kriyate':'is done',
    'kiṃ':'anything', 'canāre':'at all here/O friend', 'mahām':'great', 'arkaṃ':'resplendent sun/hymn', 'maghavan':'O bountiful one',
    'citram':'wondrous', 'arca':'praise', 'prāṇabhṛtāṃ':'of living beings', 'praṇetrā':'by the guide',
    'prāṇādhināthena':'by the lord of vital breaths', 'samīraṇena':'by Samīraṇa (Vāyu)', 'jñāna-sukhaika-pūrṇa':'wholly full of knowledge and bliss',
    'mayi':'toward me', 'śrī-ramaṇa':'beloved of Śrī', 'bimbo':'original image', 'asi':'you are', 'pratibimbo':'reflection', 'asmi':'I am',
    'yady':'although', 'cāntaram':'and a difference', 'nirdoṣa':'faultless', 'mad-doṣaṃ':'my fault', 'virecaya':'purge/expel',
    'bhagavan':'O Lord', 'yan':'whatever', 'mayā':'by me', 'śubhaṃ':'auspicious', 'kārayasi':'you cause to be done',
    'prabho':'O master', 'tat':'that', 'viṣṇu-pūjāstu':'may be worship of Viṣṇu',
    'si':'you are', 'stu':'may it be', 'sarvaṃ':'all'
  });
  Object.assign(dictionary, {
    'śubhe':'auspicious', 'śobhane':'beautiful', 'muhūrte':'at the moment', 'viṣṇor':'of Viṣṇu', 'ājñayā':'by the command', 'pravartamānasya':'of one acting',
    'adya':'today', 'brahmaṇo':'of Brahmā', 'dvitīya-parārdhe':'in the second half of life', 'śveta-varāha-kalpe':'in the Śveta-Varāha kalpa',
    'vaivasvata-manvantare':'in the Vaivasvata Manvantara', 'aṣṭāviṃśatitame':'twenty-eighth', 'kali-yuge':'in the Kali age', 'prathama-pāde':'in the first quarter',
    'jambū-dvīpe':'in Jambūdvīpa', 'bhārata-varṣe':'in Bhāratavarṣa', 'bharata-khaṇḍe':'in Bharata region', 'daṇḍakāraṇye':'in Daṇḍakāraṇya',
    'godāvaryāḥ':'of the Godāvarī', 'dakṣiṇe':'southern', 'tīre':'on the bank', 'śālivāhana-śake':'in the Śālivāhana era',
    'bauddhāvatāre':'in the Buddha incarnation', 'rāma-kṣetre':'in Rāma’s sacred place', 'asmin':'in this', 'vartamāne':'current', 'cāndramānena':'by lunar reckoning',
    'śubha-nakṣatra-śubha-yoga-śubha-karaṇa':'auspicious lunar mansion, yoga, and karaṇa',
    'evaṃ-guṇa-viśeṣaṇa-viśiṣṭāyāṃ':'distinguished by such qualities', 'śubha-tithau':'on the auspicious lunar day',
    'śrī-bhāratī-ramaṇa-mukhya-prāṇāntargata':'dwelling within Mukhyaprāṇa, beloved of Bhāratī',
    'śrī-lakṣmī-nārāyaṇa-preraṇayā':'by the prompting of Śrī Lakṣmī-Nārāyaṇa', 'śrī-lakṣmī-nārāyaṇa-prītyartham':'for the pleasure of Śrī Lakṣmī-Nārāyaṇa',
    'bhagavato':'of the Blessed Lord', 'bhagavatas':'of the Blessed Lord', 'bhagavatā':'by the Blessed Lord', 'lakṣmī-nārāyaṇasya':'of Lakṣmī-Nārāyaṇa',
    'yathā-militopacāra-dravyaiḥ':'with the available worship materials', 'dhyānāvāhanādi-ṣoḍaśopacāra-pūjāṃ':'sixteen-service worship beginning with meditation and invocation',
    'kalaśasya':'of the water-pot', 'samāśritaḥ':'abiding in', 'sthito':'standing', 'mātṛ-gaṇaḥ':'host of Mother goddesses', 'smṛtaḥ':'remembered',
    'sāgarāḥ':'oceans', 'sapta-dvīpā':'seven-continent', 'vasundharā':'earth', 'ṛgvedo':'Ṛgveda', 'tha':'and then', 'yajurvedaḥ':'Yajurveda',
    'sāmavedo':'Sāmaveda', 'tharvaṇaḥ':'Atharvaveda', 'aṅgaiś':'with auxiliary limbs', 'sahitāḥ':'joined with', 'kalaśāmbu':'water of the kalaśa',
    'samāśritāḥ':'abiding in', 'gāyatrī':'Gāyatrī', 'sāvitrī':'Sāvitrī', 'śāntiḥ':'Peace', 'puṣṭi-karī':'giver of nourishment',
    'deva-pūjārthaṃ':'for deity worship', 'durita-kṣaya-kārakāḥ':'destroyers of evils', 'samudrāḥ':'oceans', 'saritaḥ':'streams',
    'tīrthāni':'holy waters', 'jaladā':'cloud-waters', 'nadāḥ':'rivers', 'abhiṣekārtham':'for ritual bathing', 'ādarāt':'with reverence',
    'gaṅge':'O Gaṅgā', 'yamune':'O Yamunā', 'godāvari':'O Godāvarī', 'sarasvati':'O Sarasvatī', 'narmade':'O Narmadā',
    'sindhu':'O Sindhu', 'kāveri':'O Kāverī', 'jale':'in water', 'smin':'this', 'sannidhiṃ':'presence',
    'nirviṣīkaraṇārthaṃ':'for removing poison', 'garuḍa-mudrāṃ':'Garuḍa gesture', 'pradarśayāmi':'I show',
    'amṛtī-karaṇārthaṃ':'for making nectar', 'dhenu-mudrāṃ':'Dhenu/cow gesture', 'pavitrī-karaṇārthaṃ':'for purifying',
    'śaṅkha-mudrāṃ':'conch gesture', 'dig-bandhanārthaṃ':'for binding the directions', 'gadā-mudrāṃ':'mace gesture',
    'saṃrakṣaṇārthaṃ':'for protection', 'cakra-mudrāṃ':'discus gesture',
    'snānīya-kalaśe':'into the bathing pot', 'ajādi-shata-kalā-sahitaṃ':'together with hundred kalās beginning with Aja',
    'śrī-lakṣmī-nārāyaṇam':'Śrī Lakṣmī-Nārāyaṇa', 'āvāhayāmi':'I invoke', 'pūrṇa-kumbhe':'into the full pot',
    'śiṃśumārādi-shata-kalā-sahitaṃ':'together with hundred kalās beginning with Śiṃśumāra', 'twelve':'twelve', 'times':'times',
    'sarvābhya':'to all', 'tattva-devatābhyo':'to the principle-deities', 'sarvābhyo':'to all', 'mātṛkā-devatābhyo':'to the Mātṛkā deities',
    'āvāhita-kalaśa-devatābhyo':'to the invoked kalaśa deities',
    'arghyādi-ṣoḍaśopacāra-pūjāṃ':'sixteen-service worship beginning with arghya', 'sarva-kṣetra-mayo':'consisting of all sacred places',
    'yasmāt':'because', 'sarva-tīrtha-mayo':'consisting of all holy waters', 'etha':'you are', 'ato':'therefore',
    'hari-priyo':'dear to Hari', 'sith':'you are', 'twam':'you', 'pūrṇa-kumbha':'O full pot', 'kalaśa-devatā-ārādhanena':'by worship of the kalaśa deities',
    'purā':'formerly', 'sāgarotpanno':'arisen from the ocean', 'vidhṛtaḥ':'held', 'kare':'in the hand', 'namitaḥ':'revered',
    'sarva-devaiś':'by all gods', 'pāñcajanya':'O Pāñcajanya', 'śaṅkhādau':'at the conch’s beginning', 'candra-daivatyaṃ':'Moon as deity',
    'varuṇa-daivatam':'Varuṇa as deity', 'pṛṣṭhe':'at the back', 'prajāpatiṃ':'Prajāpati', 'vidyād':'one should know', 'agre':'at the front',
    'gaṅgā-sarasvatī':'Gaṅgā and Sarasvatī', 'trailokye':'in the three worlds', 'yāni':'whatever', 'vāsudevasya':'of Vāsudeva',
    'cājñayā':'by command', 'śaṅkhe':'in the conch', 'tiṣṭhanti':'abide', 'viprendra':'O best brāhmaṇa', 'thasmath':'therefore',
    'shaṅkhaṃ':'conch', 'prapūjayet':'should worship fully', 'pāñcajanyāya':'to Pāñcajanya', 'vidmahe':'may we know',
    'mahādarāya':'to Mahādara, an epithet of the conch', 'dhīmahi':'may we meditate', 'tan':'that', 'naḥ':'us', 'śaṅkhaḥ':'conch', 'pracodayāt':'may inspire',
    'śaṅkha-devatābhyo':'to conch deities', 'dhyānaṃ':'meditation', 'āvāhanaṃ':'invocation', 'āsanaṃ':'seat',
    'arghyaṃ':'welcoming water', 'pādyaṃ':'water for feet', 'ācamanīyaṃ':'sipping water', 'madhuparkaṃ':'welcoming mixture',
    'punar-ācamanīyaṃ':'sipping water again', 'gandha-puṣpa-tulasī-patrāṇi':'fragrant paste, flowers, and tulasī leaves',
    'śaṅkha-pūjanena':'by worship of the conch', 'āsana-bhūtāya':'which is Viṣṇu’s seat', 'divya-ratna-mayāya':'made of divine jewels',
    'pradhāna-puruṣeśāya':'lord of Pradhāna and Puruṣa', 'mahā-pīṭhāya':'to the great pedestal'
  });
  Object.assign(dictionary, {
    'ajādi-shata-kalā-sahitaṃ':'together with hundred kalās beginning with Aja',
    'udyad-bhāsvat-samābhāsaś':'shining like the rising sun', 'cid-ānandaika-dehavān':'having a body of consciousness-and-bliss alone',
    'cakra-śaṅkha-gadā-padma-dharo':'bearer of discus, conch, mace, and lotus', 'dhyeyo':'to be meditated upon', 'ham':'I', 'īśvaraḥ':'the Lord',
    'lakṣmī-dharābhyām':'by Lakṣmī and Dharā', 'āśliṣṭaḥ':'embraced', 'sva-mūrti-gaṇa-madhyagaḥ':'standing amid his own forms',
    'brahma-vāyu-śivāhīśa-vipaiḥ':'by Brahmā, Vāyu, Śiva, serpent-lord, and the learned', 'śakrādikair':'by Śakra and the rest',
    'sevyamāno':'being served', 'dhikaṃ':'exceedingly', 'bhaktyā':'with devotion', 'nitya-niḥśeṣa-śaktimān':'having eternal unlimited power',
    'mūrtayo':'forms', 'ṣṭāv':'eight', 'dhyeyāś':'to be meditated upon', 'cakra-śaṅkha-varābhayaiḥ':'with discus, conch, boon, and fearlessness',
    'yuktāḥ':'endowed', 'pradīpa-varṇāś':'luminous like lamps', 'sarvābharaṇa-bhūṣitāḥ':'adorned with every ornament',
    'bhuvanasya':'of the world', 'garbho':'embryo/womb', 'yathāvaśaṃ':'according to will', 'carati':'moves', 'eṣaḥ':'this',
    'ghoṣā':'sounds', 'id':'indeed', 'śṛṇvire':'are heard', 'rūpaṃ':'form', 'tasmai':'to that', 'vātāya':'to Vāta/Vāyu', 'haviṣā':'with oblation',
    'hṛt-padma-sthita':'dwelling in the lotus of the heart', 'śrī-puruṣottama':'Śrī Puruṣottama', 'pīṭhe':'onto the seat', 'smin':'this',
    'pratimāyāṃ':'into the image', 'ehi':'come', 'bho':'O', 'jagatāṃ':'of the worlds', 'nātha':'lord/protector', 'yāvat':'until',
    'pūjāvasānakam':'completion of worship', 'tāvat':'until then', 'saṃprīti-bhāvena':'with affectionate disposition', 'sthiro':'firm/steadfast',
    'bhava':'be', 'āvāhito':'invoked', 'saṃsthāpito':'established', 'sanniruddho':'securely enclosed', 'sammukho':'facing', 'avaguṇṭhito':'veiled',
    'punar-ācamanaṃ':'sipping water again',
    'vastra-yugmaṃ':'pair of garments', 'kaustubhādy-ābharaṇāni':'ornaments beginning with Kaustubha', 'cakrādi-āyudhāni':'weapons beginning with discus',
    'yajñopavītaṃ':'sacred thread', 'gandhān':'fragrant paste', 'akṣatān':'unbroken rice grains', 'tulasī-daḷa-sahita':'together with tulasī leaves',
    'dūrvādi':'beginning with dūrvā grass', 'nānā-vidha':'many kinds', 'parimaḷa-puṣpāṇi':'fragrant flowers',
    'samasta-āvaraṇa-devatābhyo':'to all enclosure deities',
    'vanaspaty-udbhavo':'born from forest trees', 'divyo':'divine', 'gandhāḍhyo':'rich in fragrance', 'gandha':'fragrance/incense',
    'āghreyaḥ':'fit to be inhaled', 'sarva-devānāṃ':'of all gods', 'dhūpo':'incense', 'yaṃ':'this', 'pratigṛhyatām':'may be accepted',
    'dhūpaṃ':'incense', 'sājyaṃ':'with ghee', 'tri-varti-saṃyuktaṃ':'joined with three wicks', 'vahninā':'with fire', 'yojitaṃ':'lit/prepared',
    'deveśa':'O lord of gods', 'trailokya-timirāpaha':'remover of three-world darkness', 'tvā':'you', 'amṛtopastaraṇam':'nectar covering',
    'śrī-nivāsa':'O Śrīnivāsa', 'tubhyaṃ':'to you', 'gṛhāṇedaṃ':'accept this',
    'lakṣmī-nārāyaṇaḥ':'Lakṣmī-Nārāyaṇa', 'uttamaḥ':'excellent', 'dīpaṃ':'lamp',
    'sahasra-śīrṣā':'thousand-headed [hymn]', 'puruṣo':'Puruṣa', 'mahābhiṣeke':'in the great abhiṣeka',
    'puruṣaḥ':'Puruṣa', 'sahasrākṣaḥ':'thousand-eyed', 'sahasra-pāt':'thousand-footed', 'bhūmiṃ':'earth',
    'viśvato':'on every side', 'vṛtvā':'having enveloped', 'aty':'beyond', 'atiṣṭhad':'stood beyond', 'daśāṅgulam':'ten finger-breadths',
    'puruṣa':'Puruṣa', 'evedaṃ':'alone is this', 'bhūtaṃ':'what has been', 'yac':'what', 'bhavyam':'what will be',
    'utāmṛtatvasyeśāno':'also lord of immortality', 'annenātirohati':'grows/transcends through food', 'etāvān':'this great',
    'mahimāto':'than this greatness', 'jyāyāṃś':'greater', 'pūruṣaḥ':'Puruṣa', 'pādo':'quarter', 'sya':'of him',
    'tripād':'three quarters', 'asyāmṛtaṃ':'of him, immortal', 'divi':'in heaven', 'ūrdhva':'upward', 'udait':'arose',
    'syehābhavat':'of him became here', 'punaḥ':'again', 'viṣvaṅ':'in every direction', 'vyakrāmat':'spread forth',
    'sāśanānaśane':'over the eating and uneating', 'abhi':'over/upon'
  });
  Object.assign(dictionary, {
    'sarvottamaṃ':'supreme above all','jñātvā':'having known','bhaktipūrvakam':'with devotion','ya':'whoever','evaṃ':'thus','japadhyānādibhir':'through japa, meditation, and the other practices','nityaṃ':'always','pūjayen':'one should worship','nāsya':'na (not) + asya (for him)','durlabham':'difficult to attain',
    'akāla-mṛtyu-haraṇaṃ':'remover of untimely death','sarva-vyādhi-nivāraṇam':'warding off every illness','viṣṇu-pādodakaṃ':'water from Viṣṇu’s feet','pītvā':'having drunk','punar':'again','vidyate':'is found / exists','prathamaṃ':'first','kāya-śuddhy-arthaṃ':'for bodily purification','dvitīyaṃ':'second','dharma-sādhanam':'a means of dharma','tṛtīyaṃ':'third','mokṣa-dam':'granting liberation','proktam':'is said','evam':'thus','tīrthaṃ':'sacred water','tri-dhā':'in three portions','pibet':'one should drink',
    'śrī':'revered','gurubhyo':'to the gurus','hariḥ':'Hari','oṃ':'Oṃ','śrīmad-ānanda-tīrtha-bhagavat-pādācāryebhyo':'to the revered Ānandatīrtha Bhagavatpādācārya','nārāyaṇāya':'to Nārāyaṇa','paripūrṇa-guṇārṇavāya':'to the ocean of perfect qualities','viśvodaya-sthiti-layonnīyati-pradāya':'to the giver of creation, continuance, dissolution, and governance of the world','jñāna-pradāya':'to the giver of knowledge','vibudhāsura-saukhya-duḥkha':'of the joy and sorrow of gods and asuras','sat-kāraṇāya':'to the true cause','vitatāya':'to the all-pervading','namo':'salutations','namas':'salutation','vipralambha-viparīta-mati-prabhūta-':'born of deception and mistaken understanding','vādān':'doctrines','nirasya':'having refuted','kṛtavān':'established','bhuvi':'on earth','tattva-vādam':'Tattvavāda, the doctrine of reality','sarveśvaro':'the Lord of all','iti':'thus','pratipādayantam':'the one teaching','ānanda-tīrtha-munivaryam':'Ānandatīrtha, foremost of sages','ahaṃ':'I','namāmi':'I bow',
    'vāyav':'O Vāyu','ā':'hither','yāhi':'come','darśateme':'appear to these (worshippers)','somā':'soma offerings','araṅkṛtāḥ':'prepared','teṣāṃ':'of them','pāhi':'drink / partake','śrudhī':'hear','havam':'invocation','śriyai':'to Śrī','jayāya':'to Jaya','vijayāya':'to Vijaya','balāya':'to Bala','prabalāya':'to Prabala','nandāya':'to Nanda','sunandāya':'to Sunanda','kumudāya':'to Kumuda','kumudākṣāya':'to Kumudākṣa',
    'agnināgniḥ':'by Agni, Agni','samidhyate':'is kindled','kavir':'the seer','gṛhapatir':'lord of the house','yuvā':'youthful','havyavāḍ':'bearer of oblations','juhvāsyaḥ':'whose mouth is the ladle',
    'viṣṇuṃ':'Viṣṇu','śriyam':'Śrī','atha':'and then','bhuvaṃ':'Bhū','brahma-vāyū':'Brahmā and Vāyu','gāyatrīṃ':'Gāyatrī','bhāratīṃ':'Bhāratī','tām':'her','garuḍam':'Garuḍa','anantaṃ':'Ananta','bhaje':'I worship','rudra-devam':'the god Rudra','devīṃ':'the goddess','suparṇīm':'Suparṇī','ahi-pati-dayitāṃ':'beloved of the serpent-lord','vāruṇīm':'Vāruṇī','apy':'also','umām':'Umā','indrādīn':'Indra and the others','kāma-mukhyān':'led by Kāma','sakala-surān':'all the gods','tad-gurūn':'their teachers','mad-gurūṃś':'my teachers',
    'apasarpantv':'may they depart','ity':'thus','asya':'of this','mantrasya':'of the mantra','vāmadeva':'Vāmadeva','ṛṣiḥ':'seer','bhūtāni':'spirits','devatāḥ':'deities','anuṣṭup':'Anuṣṭubh metre','chandaḥ':'metre','bhūtoccāṭane':'in driving away spirits','viniyogaḥ':'ritual application','apasarpantu':'may they depart','ye':'those who','bhūtā':'spirits','bhuvi':'on earth','saṃsthitāḥ':'dwelling','vighna-kartāras':'causers of obstacles','te':'to you','naśyantu':'may they perish','śivājñayā':'by Śiva’s command','apakramantu':'may they withdraw','krūrāś':'cruel','caiva':'and indeed','rākṣasāḥ':'rākṣasas','cātra':'and here','nivasanty':'dwell','eva':'indeed','santatam':'continually','teṣām':'of them','apy':'also','avirodhena':'without opposition','brahma-karma':'sacred rite','samārabhe':'I begin',
    'nirastaḥ':'cast away','parāvasuḥ':'inauspicious force','idam':'here / this','arvāvasoḥ':'of Arvāvasu','sadane':'in the dwelling','sīdāmi':'I sit','āsane':'on the seat','soma-maṇḍale':'in Soma’s orb','kūrma-skandhe':'upon Kūrma’s back','upaviṣṭo':'seated','smi':'I am','bhūr':'earthly realm','bhuvas':'atmosphere','svarom':'Svaḥ, Oṃ','anantāsanāya':'to the seat of Ananta','kūrmāsanāya':'to the seat of Kūrma','pṛthvi':'O Earth','meru-pṛṣṭha':'Merupṛṣṭha','kūrmo':'Kūrma','sutalaṃ':'Sutala','āsane':'for the seat','tvayā':'by you','dhṛtā':'upheld','lokā':'worlds','tvaṃ':'you','viṣṇunā':'by Viṣṇu','dhāraya':'uphold','māṃ':'me','pavitraṃ':'pure','cāsanam':'and this seat','pūtaṃ':'purified','dhare':'O Earth, bearer','nato':'bowed','tvāṃ':'to you','sureśvari':'O queen of the gods',
    'yebhyo':'for whom','mātā':'mother','madhumat':'sweet','pinvate':'pours forth','payaḥ':'milk','pīyūṣaṃ':'nectar','dyaur':'heaven','aditir':'Aditi','adribarhāḥ':'stone-covered altar','ukthaśuṣmān':'mighty in sacred praise','vṛṣabharān':'powerful','svapnasas':'watchful','tān':'those','ādityān':'the Ādityas','anu':'with / after','madā':'may I rejoice','svastaye':'for well-being','evā':'thus','pitre':'to the Father','viśvadevāya':'to the All-god','vṛṣṇe':'to the mighty one','yajñair':'with sacrifices','vidhema':'may we worship','namasā':'with reverence','havirbhiḥ':'with oblations','bṛhaspate':'O Bṛhaspati','suprajā':'having good offspring','vīravanto':'having heroes','vayaṃ':'we','syāma':'may we be','patayo':'lords','rayīṇām':'of riches',
    'brahmapāra-stotrasya':'of the Brahmapāra hymn','kaṇḍu':'Kaṇḍu','viśve':'all','devā':'gods','triṣṭup':'Triṣṭubh metre','pūjādhikāra-siddhyarthe':'for attaining fitness to worship','jape':'in recitation','pracetasa':'the Pracetases','uvāca:':'said','brahmapāraṃ':'Brahmapāra','mune':'O sage','śrotum':'to hear','icchāmaḥ':'we wish','paramaṃ':'supreme','stavam':'hymn of praise','japatā':'by reciting','kaṇḍunā':'by Kaṇḍu','devo':'the Lord','yenārādhyata':'by which he was worshipped','keśavaḥ':'Keśava','sūta':'Sūta','pāraḥ':'shore / limit','paraṃ':'supreme','vishnur-anantha':'Viṣṇu, the endless one','parāṇām':'of the highest','pāra-pāraḥ':'the farthest shore','brahmapāraḥ':'Brahmapāra','para-pāra-bhūtaḥ':'the ultimate shore beyond all','parebhyaḥ':'beyond the high','paramārtha-rūpī':'whose nature is highest reality','kāraṇaṃ':'cause','kāraṇatas':'from the cause','tato':'than that','tasyāpi':'of that too','hetuḥ':'cause','para-hetu-hetuḥ':'supreme cause of every cause','kāryeṣu':'among effects','caivaṃ':'and thus','karma-kartṛ':'doer of action','rūpair':'with forms','aśeṣair':'without remainder','avatīha':'enters here','sarvam':'everything','prabhur':'the Lord','sarva-bhūto':'present as all beings','prajānāṃ':'of creatures','patir':'lord','acyuto':'Acyuta','asau':'that one','brahmāvyayaṃ':'imperishable Brahman','nityam':'eternal','ajaṃ':'unborn','viṣṇu-':'Viṣṇu','rapakṣayādyair':'unattached to decay and the rest','akhilair':'to all','asaṅgī':'unattached','brahmākṣaram':'imperishable Brahman','puruṣottamaḥ':'Supreme Person','tathā':'so','rāgādayo':'attachment and the rest','doṣāḥ':'faults','prayāntu':'may they go','praśamaṃ':'to quiet','mama':'my','evaṃ':'thus','vai':'indeed','brahmapārākhyaṃ':'called Brahmapāra','saṃstavaṃ':'hymn of praise','japan':'reciting','avāpa':'attained','paramāṃ':'highest','siddhiṃ':'perfection','samārādhya':'having worshipped','keśavam':'Keśava',
    'āgamārthaṃ':'for the coming','devānāṃ':'of the gods','gamanārthaṃ':'for the departure','rakṣasām':'of the rākṣasas','kuru':'make','ghaṇṭā-ravaṃ':'bell sound','tatra':'there','devatāhvāna-lāñchanam':'the sign that summons the deities',
    'kṛtāñjali-puṭo':'with palms joined','bhūtvā':'having become','vinata-kandharaḥ':'neck bowed','yāce':'I beseech','tvāṃ':'you','pūjārtham':'for the worship','uttiṣṭha':'rise','ramā-pate':'O husband of Ramā','āyatābhyāṃ':'with the long','viśālābhyāṃ':'wide','śītalābhyāṃ':'cool','kṛpā-nidhe':'O treasure of compassion','karuṇāmṛta-pūrṇābhyāṃ':'filled with the nectar of mercy','locanābhyāṃ':'with the eyes','vilokaya':'look upon','sālagrāma-nivāsāya':'to the one dwelling in the Sālagrāma','kṣīrābdhi-śayanāya':'to the one reclining on the ocean of milk','śrī-śailādri-nivāsāya':'to the one dwelling on Śrīśaila mountain','śilā-vāsāya':'to the one dwelling in the sacred stone',
    'hiraṇya-varṇāṃ':'golden-hued','hariṇīṃ':'radiant','suvarṇa-rajata-srajām':'wearing garlands of gold and silver','candrāṃ':'moonlike','hiraṇmayīṃ':'golden','lakṣmīṃ':'Lakṣmī','ma':'to me','ā':'hither','vaha':'bring','tāṃ':'that one','lakṣmīm':'Lakṣmī','anapagāminīm':'never departing','yasyāṃ':'through whom','vindeyaṃ':'may I obtain','gām':'cattle','aśvaṃ':'horse','puruṣān':'people / offspring','aham':'I',
    'sālagrāma-śilāyāṃ':'in the Sālagrāma stone','nityaṃ':'always','sannihito':'present','bhīmasena':'O Bhīmasena','mahā-bāho':'mighty-armed one','gadāyudha':'wielder of a mace','prabho':'O Lord'
  });
  Object.assign(dictionary, {
    'uvāca:':'said','uvāca':'said','sūta':'Sūta','pracetasa':'the Pracetases','viṣṇoḥ':'of Viṣṇu','bhagavato':'of the Blessed Lord','sākṣād':'directly','sārthakaṃ':'meaningful','ārādhya':'having worshipped','āyuṣyaṃ':'lifespan','syād':'may be','paṭavaḥ':'capable, vigorous','indriyāṇi':'the senses','svastha-śarīraṃ':'a healthy body','yāvat':'as long as','tāvad':'then / for that duration','pūjanaṃ':'worship','janma-saphalaṃ':'making birth fruitful','durlabhaṃ':'difficult to attain','mahā-ghore':'very dreadful','janma-roga-bhayākule':'beset by birth, illness, and fear','saṃsāre':'in worldly existence',"'smin":'in this','vibudhāsura-saukhya-duḥkha-':'of the happiness and sorrow of gods and asuras','yo':'who','harir':'Hari','śriyam-atha':'Śrī and then','umām':'Umā','viṣṇu-':'Viṣṇu','vishnur-anantha':'Viṣṇu, the endless one','param':'supreme','avyayaṃ':'imperishable','paraṃ':'supreme','svarom':'Svaḥ, Oṃ'
  });
  Object.assign(dictionary, { 'pi':'also (from api by sandhi)', 'sau':'that one (asau)', 'viṣṇu':'Viṣṇu', 'vipralambha-viparīta-mati-prabhūta':'doctrines arising from deception and mistaken thought', 'umāṃ':'Umā' });
  Object.assign(dictionary, {
    'sahasra-śīrṣā':'thousand-headed','puruṣo':'Puruṣa','mahābhiṣeke':'in the great ritual bath','sahasrākṣaḥ':'thousand-eyed','sahasra-pāt':'thousand-footed','bhūmiṃ':'the earth','viśvato':'on every side','vṛtvā':'having enveloped','aty':'beyond','atiṣṭhad':'he stood / extended','daśāṅgulam':'ten finger-breadths','evedaṃ':'indeed this','bhūtaṃ':'what has been','yac':'and what','bhavyam':'what is yet to be','utāmṛtatvasyeśāno':'also the lord of immortality','annenātirohati':'grows beyond through food','etāvān':'thus great','mahimāto':'his greatness; beyond it','jyāyāṃś':'greater','pūruṣaḥ':'the Cosmic Person','pādo':'one quarter','asya':'of him','viśvā':'all','tripād':'three quarters','asyāmṛtaṃ':'of him, immortal','divi':'in heaven','ūrdhva':'upward','udait':'rose','syehābhavat':'of him here became','punaḥ':'again','tato':'from that','viṣvaṅ':'in every direction','vyakrāmat':'spread forth','sāśanānaśane':'over what eats and what does not eat','abhi':'over / upon'
  });
  Object.assign(dictionary, {
    'imā':'these (feminine)', 'imāḥ':'these (feminine plural)', 'tāni':'those',
    'vaiśravaṇāya':'to Vaiśravaṇa', 'prīyatāṃ':'may be pleased',
    'anantāya':'to Ananta', 'govindāya':'to Govinda',
    'vandyaṃ':'worthy of praise', 'sad-ānandaṃ':'ever blissful',
    'vāsudevaṃ':'Vāsudeva (object)', 'nirañjanam':'unstained, pure',
    'indirā-patim':'husband of Indirā (Lakṣmī)',
    'ādy-ādi-vara-deśa-vara-pradam':'primordial giver of supreme boons and stations',
    'nikhilādhīśa':'O Lord of all',
    'kirīṭa-ghṛṣṭa-pīṭhavat':'whose footstool is rubbed by crowns',
    'hṛt-tamaḥ-śamane':'dispelling the heart’s darkness',
    'rkābhaṃ':'sunlike (arkābhaṃ, after elision)',
    'śrī-pateḥ':'of the Lord of Śrī',
    'sarvopaskara-saṃyutaṃ':'provided with every accompaniment',
    'annādi':'food and the other items', 'mahā-naivedyaṃ':'great food offering',
    'amṛtāpidhānam':'the covering of nectar',
    'hasta-prakṣālanaṃ':'water for washing hands', 'gaṇḍūṣaṃ':'mouth rinse',
    'mukha-vastraṃ':'cloth for the face',
    'pūgī-phala-tāmbūlaṃ':'betel leaves with areca nut',
    'suvarṇa-puṣpaṃ':'golden flower',
    'khaṇḍa-guṇoru-maṇḍalaḥ':'whose vast circle of qualities is unbroken (preceded by a-)',
    'sad-odito':'ever arisen', 'jñāna-marīci-mālī':'garlanded with rays of knowledge',
    'sva-bhakta-hārd-occha-tamo-nihantā':'destroyer of deep darkness in devotees’ hearts',
    'vyāsāvatāro':'incarnate as Vyāsa', 'ātma-bhāskaraḥ':'sun of the self',
    'kṣīṇa-sukhātma-bimbaḥ':'whose blissful self-image is undiminished (preceded by a-)',
    'svaiśvarya-kānti-pratataḥ':'pervaded by the radiance of His own sovereignty',
    'sadoditaḥ':'ever arisen',
    'sva-bhakta-santāpa-duriṣṭa-hantā':'destroyer of devotees’ suffering and ill fortune',
    'rāmāvatāro':'incarnate as Rāma', 'īśa-candramāḥ':'moon among lords',
    'asaṃkhyoru-balāmbu-pūro':'a boundless flood of immense strength',
    'guṇocca-ratnākara':'ocean of precious, exalted qualities',
    'ātma-vaibhavaḥ':'whose own majesty is His splendor',
    'sadātma-jñāna-dībhir':'by the lamps of knowledge of the eternal self',
    'kṛṣṇāvatāro':'incarnate as Kṛṣṇa', 'eka-sāgaraḥ':'the one ocean',
    'mahadbhyo':'to the great ones', 'arbhakebhyo':'to the small ones',
    'yuvabhyo':'to the young', 'nama':'salutation', 'āśinebhyaḥ':'to the aged',
    'yajāma':'we worship', 'yadi':'if', 'śaknavāma':'we are able',
    'jyāyasaḥ':'of the greater ones', 'śaṃsam':'praise', 'vṛkṣi':'may I cut off',
    'rājādhirājāya':'to the king of kings', 'kurmahe':'we offer / make',
    'kāma-kāmāya':'to one desiring wishes', 'mahyaṃ':'to me',
    'kāmeśvaro':'lord of desires', 'vaiśravaṇo':'Vaiśravaṇa',
    'kubērāya':'to Kubera', 'mahārājāya':'to the great king',
    'vaitāṃ':'indeed this (vai + etām)', 'veda':'knows',
    'amṛtenāvṛtāṃ':'enveloped in immortality', 'purīm':'city',
    'kīrtiṃ':'fame', 'prajāṃ':'offspring', 'dadau':'gave',
    'tāsām':'among them', 'āvirabhūc':'appeared (āvirabhūt)',
    'chauriḥ':'Śauri, Kṛṣṇa (ch for ś in this text)',
    'smayamāna-mukhāmbujaḥ':'whose lotus face is smiling',
    'pītāmbara-dharaḥ':'wearing yellow garments', 'sragvī':'wearing a garland',
    'sākṣān':'directly, in person (sākṣāt)',
    'manmatha-manmathaḥ':'the enchanter of Manmatha',
    'mantra-puṣpaṃ':'flowers offered with mantra',
    'chatraṃ':'parasol', 'cāmaraṃ':'yak-tail fly-whisk',
    'vyajanaṃ':'fan', 'darpaṇaṃ':'mirror', 'gītaṃ':'song',
    'nṛtyaṃ':'dance', 'vādyaṃ':'instrumental music',
    'stotraṃ':'hymn of praise', 'samasta-rājopacārān':'all royal honors',
    'śivatamā':'most auspicious', 'sarvasya':'of everyone / everything',
    'bheṣajīḥ':'healing remedies', 'rāṣṭrasya':'of the realm',
    'vardhanīr':'increasing / strengthening',
    'rāṣṭrabhṛto':'sustaining the realm', 'mṛtāḥ':'immortal (amṛtāḥ after elision)',
    'brahmādayo':'Brahmā and the others',
    'sanakādyāḥ':'Sanaka and the others', 'śukādayaḥ':'Śuka and the others',
    'śrī-nṛsiṃha-prasādo':'prasāda of Śrī Nṛsiṃha',
    'gṛhṇantu':'may they receive', 'vaiṣṇavāḥ':'Vaiṣṇava devotees',
    'yasya':'of whom / whose', 'smṛtyā':'by remembrance',
    'nāmoktyā':'by utterance of the name',
    'tapaḥ-pūjā-kriyādiṣu':'in austerities, worship and other rites',
    'nyūnaṃ':'deficient', 'sampūrṇatāṃ':'completeness',
    'yāti':'attains / goes to', 'sadyo':'at once',
    'acyutam':'Acyuta, the infallible Lord (object)',
    'kṛtaṃ':'done', 'paripūrṇaṃ':'complete',
    'ṣoḍaśopacāra-pūjanena':'by worship with sixteen services',
    'bhāratī-ramaṇa-mukhya':'Mukhyaprāṇa, the husband of Bhāratī (first half of compound)',
    'prāṇāntargata':'dwelling within Prāṇa',
    'śrī-lakṣmī-nārāyaṇaḥ':'Śrī Lakṣmī-Nārāyaṇa',
    'śrī-kṛṣṇārpaṇam':'an offering to Śrī Kṛṣṇa',
    'mantra-tantra-svara-varṇa-lopa-doṣa':'faults in mantra, ritual method, accent, syllable, or omission',
    'prāyaścittārthaṃ':'for expiation / atonement',
    'nāmatraya-mantra-japaṃ':'recitation of the three-name mantra',
    'acyutāya':'to Acyuta',
    'acyutānanta-govindebhyo':'to Acyuta, Ananta and Govinda',
    'jāne':'I know', 'kiñcin':'anything', 'nāpi':'nor even',
    'laukika-vaidike':'in worldly and Vedic matters',
    'niṣedha-vidhī':'prohibitions and injunctions',
    'kevalam':'only / simply', 'aparādha-sahasrāṇi':'thousands of offenses',
    'kriyante':'are committed', 'har-niśaṃ':'day and night (ahar-niśam)',
    'sarvāṇi':'all of them', 'nāhaṃ':'I am not (na + aham)',
    'tat-pūjā':'His worship', 'cākhilam':'and the whole of it',
    'tathāpi':'even so', 'mat-kṛtā':'done by me',
    'tat-prasādān':'through His grace', 'cānyathā':'and otherwise',
    'mādṛśo':'one like me', 'nāparaḥ':'no other',
    'tvādṛśo':'one like you', 'dayāparaḥ':'supremely compassionate',
    'yam':'this one (ayam after elision)', 'matvā':'having considered',
    'pāpo':'sinful', 'haṃ':'I am (aham after elision)',
    'pāpa-karmāhaṃ':'I perform sinful acts',
    'pāpātmā':'of sinful nature', 'pāpa-sambhavaḥ':'born of sin',
    'śaraṇāgata-vatsala':'tender toward those who seek refuge',
    'anyat-śaraṇaṃ':'another refuge', 'śaraṇaṃ':'refuge',
    'kāruṇya-bhāvena':'with a compassionate disposition',
    'sarva-guṇa-sampūrṇaḥ':'complete in every virtue',
    'sarva-doṣa-vivarjitaḥ':'free from every defect',
    'laṃ':'enough / for the sake of (alam after elision)',
    'viṣṇur':'Viṣṇu', 'paramaḥ':'supreme',
    'kāni':'whatever', 'pāpāni':'sins',
    'janmāntara-kṛtāni':'committed in other births',
    'tīrtha-koṭi-sahasrāṇi':'thousands of crores of sacred bathing places',
    'vrata-koṭi-śatāni':'hundreds of crores of vows',
    'nārāyaṇa-praṇāmasya':'of prostration to Nārāyaṇa',
    'kalāṃ':'a fraction', 'padbhyāṃ':'with the two feet',
    'karābhyāṃ':'with the two hands', 'jānubhyāṃ':'with the two knees',
    'praṇāmo':'prostration', 'ṣṭāṅga':'eight-limbed (aṣṭāṅga after elision)',
    'stv':'may there be (astu after elision)',
    'sahasra-mūrtaye':'to the one of a thousand forms',
    'sahasra-pādākṣi-śiroru-bāhave':'with a thousand feet, eyes, heads and mighty arms',
    'sahasra-nāmne':'to the one of a thousand names',
    'puruṣāya':'to the Person', 'śāśvate':'eternal',
    'sahasra-koṭi-yuga-dhāriṇe':'to the bearer of thousands of crores of ages',
    'brahmaṇya-devāya':'to the God devoted to sacred learning',
    'go-brāhmaṇa-hitāya':'benefactor of cows and brāhmaṇas',
    'jagad-dhitāya':'benefactor of the world', 'kṛṣṇāya':'to Kṛṣṇa',
    'kalyāṇādbhuta-gātrāya':'whose form is auspicious and wondrous',
    'kāmitārtha-pradāyine':'granting desired aims',
    'śrīmad-veṅkaṭanāthāya':'to glorious Veṅkaṭanātha',
    'padaṃ':'foot / station',
    'samasta-sad-guṇottamaṃ':'supreme in all noble qualities',
    'kṛṣṇārpaṇam':'an offering to Kṛṣṇa'
  });
  const clean = (word) => word.replace(/^[^\p{L}]+|[^\p{L}]+$/gu, '');
  const lookup = (word) => {
    const key = clean(word).toLowerCase();
    if (!key) return '';
    if (dictionary[key]) return dictionary[key];
    // Sandhi and compounds are kept intact as one lexical unit, with a clear
    // marker instead of silently inventing a gloss for an uncertain form.
    return 'lexical form “' + key + '” (gloss needs source review)';
  };
  const entries = {};
  const guides = window.GUIDES || [];
  const guide = guides.find((g) => g.key === 'achar');
  if (guide) guide.sections.forEach((section) => {
    if (!section.mantra) return;
    const lines = section.mantra.split('\n').map((text, lineIndex) => {
      if (!text.trim()) return null;
      if (/^\s*[([]/.test(text.trim()) || /^\s*\(/.test(text) || (section.id === '42' && lineIndex < 2)) {
        return {text, kind:'direction', meaning:'Ritual direction (not chanted Sanskrit).', words:[]};
      }
      const words = text.replace(/\([^)]*\)/g, '').trim().split(/\s+/).filter((token) => clean(token)).map((token) => ({text:token, meaning:lookup(token)}));
      const meaning = words.map((word) => word.meaning).filter(Boolean).join('; ');
      return {text, meaning, words};
    });
    entries[section.id] = {
      status: 'Guide text aligned; mantra wording not independently verified against audio.',
      lines
    };
  });
  // Reviewed line meanings.  The base pass above retains the guide's exact
  // display text and token boundaries; this overlay replaces its mechanical
  // dictionary-string meaning with a translation of the complete line.
  const reviewed = {
    '04': [
      'It removes untimely death and wards off every illness.',
      'Having drunk Viṣṇu’s foot-water, one is not reborn.',
      'The first sip is for bodily purification; the second is a means of dharma.',
      'The third is said to grant liberation; thus one should drink sacred water in three portions.'
    ],
    '05': [
      'Salutations to the revered gurus. Hariḥ Om.',
      'Salutations to the blessed Ānandatīrtha Bhagavatpādācārya.',
      'Oṃ. To Nārāyaṇa, the ocean of perfect qualities,',
      'the giver of the world’s creation, continuance, dissolution, and governance,',
      'the giver of knowledge and the true cause of the joy and sorrow of gods and asuras,',
      'the all-pervading one: salutations again and again to You.',
      'I bow to Ānandatīrtha, who refuted the many doctrines born of deception and mistaken understanding,',
      'and established Tattvavāda on earth,',
      'teaching that Hari is the Lord of all,',
      'the foremost of sages, Ānandatīrtha.'
    ],
    '06': [
      'Salutations to Śrī; salutations to Jaya; salutations to Vijaya.',
      'Salutations to Śrī; salutations to Bala; salutations to Prabala.',
      'Salutations to Śrī; salutations to Nanda; salutations to Sunanda.',
      'Salutations to Śrī; salutations to Kumuda; salutations to Kumudākṣa.',
      'Oṃ. O Vāyu, come here to be seen; these soma offerings are prepared for you.',
      'Partake of them; hear our invocation.'
    ],
    '07': [
      'Oṃ. By Agni, Agni is kindled: the inspired seer, youthful lord of the house,',
      'the bearer of oblations, whose mouth is the offering ladle.'
    ],
    '08': [
      'I praise Viṣṇu; I bow to Śrī and Bhū; I praise Brahmā and Vāyu,',
      'I worship Gāyatrī, Bhāratī, Garuḍa, Ananta, and the god Rudra,',
      'I praise the goddesses Suparṇī, beloved of the serpent-lord, Vāruṇī, and Umā,',
      'and Indra and the others, the gods led by Kāma, all the celestials, their teachers, and my teachers.'
    ],
    '09': [
      'For the mantra beginning “May they depart,” Vāmadeva is the seer; the spirits are its deities.',
      'Its metre is Anuṣṭubh; its application is the driving away of obstructing spirits.',
      'May those spirits depart—those dwelling upon the earth.',
      'May the spirits that cause obstacles perish by Śiva’s command.',
      'May the spirits withdraw, and the cruel rākṣasas as well.',
      'But may the deities who dwell here continually upon the earth',
      'remain without opposition; with their consent I begin this sacred rite.'
    ],
    '10': [
      'The inauspicious force is cast away.',
      'Here I sit in the dwelling of Arvāvasu.',
      'I am seated on the seat in Soma’s orb, upon the back of Kūrma.',
      'Oṃ: Bhūḥ, Bhuvaḥ, Svaḥ.',
      'Salutations to the seat of Ananta; salutations to the seat of Kūrma.',
      'For the Pṛthvī mantra, Merupṛṣṭha is the seer, Kūrma is the deity, and Sutala is the metre.',
      'Its application is the seat.',
      'O Goddess Earth, the worlds are upheld by you, and you are upheld by Viṣṇu.',
      'You too, O Goddess, uphold me; make this seat pure.',
      'Purify me too, O Earth; I bow to you, queen of the gods.'
    ],
    '11': [
      'Oṃ. For those [gods], the Mother pours sweet milk; heaven, Aditi, and the stone-covered altar yield nectar.',
      'May I rejoice for well-being in those Ādityas, mighty and powerful in sacred praise.',
      'Thus may we worship with sacrifices, reverence, and oblations the Father, All-god, the mighty one.',
      'O Bṛhaspati, may we have good offspring and heroes, and become lords of riches.'
    ],
    '12': [
      'For the Brahmapāra hymn, Kaṇḍu is the seer and the All-gods are its deities.',
      'Its metre is Triṣṭubh; it is recited to attain fitness for worship.',
      'The Pracetases said:',
      '“O sage, we wish to hear the supreme hymn called Brahmapāra,',
      'by which the god Keśava was worshipped by the sage Kaṇḍu as he recited it.”',
      'Sūta said:',
      '“Viṣṇu is the far shore, the supreme beyond; He is the shore beyond limit,',
      'the farthest shore beyond even the highest.',
      'He is Brahmapāra, the ultimate shore beyond all others,',
      'the highest beyond the high, whose nature is the highest reality.',
      'He is the cause, beyond the causes and beyond them too,',
      'the cause of that as well, the supreme cause of every cause.',
      'And thus, in all effects, He is indeed the doer of action,',
      'entering everything here in all forms without remainder.',
      'He is Brahman, the Lord, present as all beings,',
      'Brahman, the Lord of creatures, that imperishable one.',
      'He is Viṣṇu: imperishable Brahman, eternal and unborn,',
      'unattached to all that is subject to decay and the rest.',
      'Just as that Supreme Person is imperishable, unborn, and eternal,',
      'so may my faults, beginning with attachment, come to rest.',
      'Thus reciting this supreme hymn called Brahmapāra,',
      'he attained the highest perfection by worshipping Keśava.”'
    ],
    '13': [
      'For the gods’ coming and the rākṣasas’ departure,',
      'make the bell sound there as the sign that summons the deities.'
    ],
    '14': [
      'With palms joined and neck bowed,',
      'I beseech you, O Lord: rise for the worship, O husband of Ramā.',
      'O treasure of compassion, with your long, wide, cool eyes,',
      'look upon me with your eyes filled with the nectar of mercy.',
      'Salutations to you who dwell in the Sālagrāma and recline on the ocean of milk,',
      'who dwell on Śrīśaila mountain and abide in the sacred stone.'
    ],
    '15': [
      'Oṃ. Golden-hued, radiant, adorned with garlands of gold and silver,',
      'bring to me Lakṣmī, moon-bright and golden, O Jātavedas.',
      'Bring to me that Lakṣmī who never departs, O Jātavedas,',
      'through whom may I obtain gold, cattle, horses, and people.'
    ],
    '16': [
      'Hari is ever present in the Sālagrāma stone.',
      'O Bhīmasena, mighty-armed lord, wielder of the mace!'
    ],
    '37': [
      'Oṃ. I salute the praiseworthy, ever-blissful, stainless Vāsudeva.',
      '[I salute] the husband of Indirā, the primal Lord who grants the choicest boons and realms.',
      'O Lord of all, I bow to your feet, which are like a pedestal rubbed by crowns.',
      '[I bow to] the lotus feet of Śrīpati, sunlike in dispelling the heart’s darkness.',
      'Oṃ. Salutations to Nārāyaṇa. I offer the great food offering, furnished with every accompaniment,',
      'beginning with rice and other foods.'
    ],
    '38': [
      'Oṃ. Salutations to Nārāyaṇa.',
      'Oṃ. You are the nectar covering; svāhā.',
      'Oṃ. Salutations to Nārāyaṇa. I offer washing for the hands.',
      'I offer water for rinsing the mouth.',
      'I offer a cloth for the face.',
      'I offer betel with areca nut.',
      'I offer a golden flower.'
    ],
    '39': [
      'Victorious is the unborn Lord, whose vast sphere of qualities is undivided,',
      'ever risen, garlanded with rays of knowledge,',
      'destroyer of the deep darkness in the hearts of his own devotees,',
      'Hari, incarnate as Vyāsa, the sun of the self.',
      'Victorious is the unborn Lord, whose essential image is undiminished bliss,',
      'ever risen, extended in the splendor of his own sovereignty,',
      'destroyer of his devotees’ affliction and misfortune,',
      'Hari, incarnate as Rāma, the moon among lords.',
      'Victorious is he, an immeasurable flood of mighty strength,',
      'an ocean of lofty qualities and the majesty of the self,',
      'ever attainable through the lamps of knowledge of the eternal self,',
      'Hari, incarnate as Kṛṣṇa, the one ocean.'
    ],
    '40': [
      'Oṃ. Salutation to the great ones; salutation to the small ones,',
      'salutation to the young; salutation to the aged.',
      'We worship the gods, if we are able.',
      'O gods, do not cut us off from praising those greater than us.',
      'To the king of kings, the mighty conqueror,',
      'we offer salutation to Vaiśravaṇa.',
      'May he grant desires to me, who longs for them,',
      'may Vaiśravaṇa, lord of desires, grant them.',
      'Salutation to Kubera, Vaiśravaṇa, the great king.',
      'Whoever knows this city of Brahman, enveloped in immortality,',
      'to him Brahmā grants life, fame, and offspring.',
      'Among them Śauri appeared, his lotus face smiling,',
      'wearing yellow garments and a garland, the enchanter of Manmatha himself.',
      'Oṃ. Salutations to Nārāyaṇa. I offer the mantra flowers.'
    ],
    '41': [
      'Oṃ. Salutations to Nārāyaṇa. I offer a parasol.',
      'I offer a yak-tail fly-whisk.', 'I offer a fan.', 'I offer a mirror.',
      'I offer song.', 'I offer dance.', 'I offer instrumental music.',
      'I offer a hymn of praise.', 'I offer all the royal services.'
    ],
    '42': [
      'Oṃ. These waters are most auspicious; these are the remedy for all.',
      'They increase and sustain the realm; they are immortal.'
    ],
    '43': [
      'Salutation to Ramā.',
      'Oṃ. Salutation to Brahmā. Oṃ. Salutation to Vāyu.',
      'Oṃ. Salutation to Garuḍa. Oṃ. Salutation to Śeṣa.',
      'May Ramā, Brahmā and the other gods, Sanaka and the others, and Śuka and the others receive this offering.',
      'May all Vaiṣṇavas receive this prasāda of Śrī Nṛsiṃha.'
    ],
    '44': [
      'By whose remembrance and utterance of whose name, in austerity, worship, ritual acts, and the rest,',
      'what is deficient immediately becomes complete: I bow to that Acyuta.',
      'O Lord of Ramā, [though it be] lacking mantra, ritual action, and devotion,',
      'whatever I have done, O Lord, may it be made complete for me.',
      'By this sixteen-service worship, may Bhagavān, who dwells within Mukhyaprāṇa, the beloved of Bhāratī,',
      'Śrī Lakṣmī-Nārāyaṇa, be pleased. May this be an offering to Śrī Kṛṣṇa.',
      'For faults of omission in mantra, ritual method, accent, or syllable,',
      'I shall recite the three-name mantra as atonement.',
      'Oṃ. Salutation to Acyuta. Oṃ. Salutation to Ananta. Oṃ. Salutation to Govinda.',
      'Salutation to Acyuta, Ananta, and Govinda.'
    ],
    '45': [
      'I do not know any rite, worldly or Vedic,',
      'nor its prohibitions or injunctions, O Viṣṇu; I am only your servant.',
      'Thousands of offences are committed by me day and night.',
      'Forgive them all, O Lord, O Supreme Person.',
      'I am not the doer; Hari is the doer, and the entire act is his worship.',
      'Even so, the worship I perform occurs only through his grace, and no other way.',
      'There is no sinner like me, nor anyone as compassionate as you.',
      'Thinking “this one is your servant,” forgive me, O Supreme Person.',
      'I am sinful, I do sinful deeds, I have a sinful nature and sinful origin.',
      'Save me, O lotus-eyed one, tender toward those who seek refuge.',
      'There is no other refuge; you alone are my refuge.',
      'Therefore, with compassion, protect me, protect me, O Janārdana.',
      'May Viṣṇu, complete in every good quality and free from every fault,',
      'my supreme friend, be pleased for my joy and welfare.'
    ],
    '46': [
      'Whatever sins have been committed, even in former births,',
      'all those perish with every step of circumambulation.',
      'Thousands of crores of sacred waters and hundreds of crores of vows',
      'do not equal even a sixteenth part of a prostration to Nārāyaṇa.',
      'With the chest, head, sight, mind, and speech,',
      'with feet, hands, and knees: this prostration is called eight-limbed.',
      'Salutations to Ananta, who has a thousand forms,',
      'a thousand feet, eyes, heads, and mighty arms,',
      'to the eternal Puruṣa of a thousand names,',
      'salutations to the one who upholds a thousand crores of ages.',
      'Salutations to the god devoted to sacred learning, benefactor of cows and brāhmaṇas,',
      'to the welfare of the world, to Kṛṣṇa, to Govinda: repeated salutations.',
      'To him whose form is auspicious and wondrous, who grants desired aims,',
      'to glorious Veṅkaṭanātha and Śrīnivāsa: salutations to you.',
      'Salutation, salutation, salutation. I always bow to your feet,',
      'and bow again and again to you, supreme in all noble qualities.'
    ],
    '47': ['May it be an offering to Śrī Kṛṣṇa.'],
    '17': ['Oṃ. Salutations to Nārāyaṇa. Oṃ.'],
    '18': [
      'Oṃ. I move with the Rudras and the Vasus, with the Ādityas and with all the gods.',
      'I uphold both Mitra and Varuṇa, both Indra and Agni, and both Aśvins.',
      'I uphold Soma the crusher, and also Tvaṣṭṛ, Pūṣan, and Bhaga.',
      'I bestow wealth on the offerer of oblation, the generous sacrificer who presses Soma.',
      'I am the sovereign queen, gatherer of treasures, knowing, foremost among those worthy of sacrifice.',
      'The gods established me in many places, abiding in abundance and entering into many beings.'
    ],
    '19': [
      '[I invoke] the golden-hued, shining one, wearing garlands of gold and silver.',
      'O Jātavedas, bring to me Lakṣmī, moonlike and golden.',
      'O Jātavedas, bring that Lakṣmī to me, the one who does not depart.',
      'Through whom may I obtain gold, cattle, horses, and people.',
      '[I invoke] her who is preceded by horses, seated amid chariots, delighted by the trumpeting of elephants.',
      'I invoke the goddess Śrī; may the goddess Śrī delight in me.'
    ],
    '20': [
      'Thus that splendid, visible radiance was established for the form of the god, born from might.',
      'When thought turns toward him and succeeds, the flowing streams bring the milk-cow of truth.',
      'The nourishing form, rich in food, lies ever in the second of the seven blessed mothers.',
      'For the milking of this bull, the women bring forth the third, endowed with tenfold insight.',
      'O Mātariśvan, you are my mother, father, incomparable teacher, brother, beloved and intimate kinsman.',
      'O Lord, inner Self of all, ageless destroyer of birth, death, and disease.',
      'O Lord, grant me devotion to Govinda, strong and without ulterior motive.',
      'O Lord, [grant devotion] without pretense, unwavering, rich in hosts of noble qualities, everlasting, and quickly.'
    ],
    '21': ['Salutation to the deity Garuḍa.', 'Salutation to the deity Śeṣa.'],
    '22': [
      '[I meditate on] a lofty performance hall made of molten, blazing gold.',
      'With lovely, auspicious pillars shining against walls of pure crystal.',
      'With ornamented doorways inlaid with the finest jewels and bringing splendor.',
      'There it gleams also with white auspicious svastikas like conches and lotuses.',
      'Endowed with a pavilion hung with nets of pearls and with diamond stairways.',
      'With pots fashioned from many jewels, surpassingly splendid.',
      'The radiant abode of Lakṣmī’s play, shining in bright ruby lamps.',
      'May such a pavilion be [used] in worship by all practitioners in this manner.',
      'With sweeping, decorative floor designs, flags, ketakī, and festoons.',
      'With canopies, sugarcane, banana plants, full pots, sprouts, and the rest.',
      'And with auspicious song, instrumental music, dance, and recitation of the Purāṇas.',
      'Beautiful, greatly holy, ever increasing, and delightful to the mind.'
    ],
    '23': [
      'Oṃ. Sit down among the hosts, O Gaṇapati; they call you the wisest of the wise.',
      'Without you, nothing at all is done here; O bountiful one, praise the great, resplendent sun.',
      'You are worshipped by the guide of living beings.',
      'By Samīraṇa, lord of the vital breaths.',
      'O Nārāyaṇa, wholly full of knowledge and bliss.',
      'O Lord, beloved of Śrī, be gracious to me.',
      'You are the original; I am the reflection, although there is a difference between us.',
      'O faultless Lord, purge my fault. Salutations to you.',
      'O Lord, whatever auspicious act you cause me to perform,',
      'may all of it be worship of Viṣṇu, O Lord, by your grace.'
    ]
  };
  Object.assign(reviewed, {
    '24': [
      'Oṃ. In this auspicious, beautiful moment, as one acting by Viṣṇu’s command,',
      'today, in Brahmā’s second half of life, in the Śveta-Varāha kalpa,',
      'in the Vaivasvata Manvantara, in the twenty-eighth Kali age, in its first quarter,',
      'in Jambūdvīpa, in Bhāratavarṣa, in the land of Bharata, in Daṇḍakāraṇya,',
      'on the southern bank of the Godāvarī, in the Śālivāhana era, in the Buddha incarnation,',
      'in this Rāma sacred place, according to the current lunar reckoning,',
      'in the [year], [half-year], [season], [month], [fortnight], [lunar day], joined with [weekday].',
      'under an auspicious lunar mansion, auspicious yoga, and auspicious karaṇa,',
      'on this auspicious lunar day distinguished by such qualities,',
      'of Śrī Lakṣmī-Nārāyaṇa dwelling within Mukhyaprāṇa, the beloved of Bhāratī,',
      'by the prompting of Śrī Lakṣmī-Nārāyaṇa, for the pleasure of Śrī Lakṣmī-Nārāyaṇa,',
      'by the Blessed Lord’s power, strength, and splendor,',
      'by the Blessed Lord’s action, I am impelled by the Blessed Lord.',
      'with the worship materials available for the Blessed Lord Lakṣmī-Nārāyaṇa,',
      'I shall perform the sixteen-service worship beginning with meditation and invocation.'
    ],
    '25': [
      'Oṃ. Viṣṇu is at the mouth of the kalaśa; Rudra abides at its neck.',
      'Brahmā stands at its base, and the host of Mothers is remembered in its middle.',
      'In its belly are all the oceans and the earth with its seven continents.',
      'The Ṛgveda, then the Yajurveda, Sāmaveda, and Atharvaveda [abide there].',
      'All of them, together with their auxiliary limbs, dwell in the water of the kalaśa.',
      'Here too are Gāyatrī, Sāvitrī, Peace, and the giver of nourishment.',
      'May they come for the worship of the Lord, as destroyers of misfortune.',
      'May all oceans, streams, holy waters, cloud-waters, and rivers [come].',
      'May they come respectfully for deity worship and for the ritual bathing.',
      'O Gaṅgā, Yamunā, Godāvarī, and Sarasvatī,',
      'O Narmadā, Sindhu, and Kāverī, make your presence in this water.',
      'For removal of poison, I show the Garuḍa mudrā.',
      'For making it nectar, I show the Dhenu mudrā.',
      'For purification, I show the conch mudrā.',
      'For binding the directions, I show the mace mudrā.',
      'For protection, I show the discus mudrā.'
    ],
    '26': [
      'Into the bathing kalaśa, [I invoke him] together with the hundred kalās beginning with Aja.',
      'I invoke Śrī Lakṣmī-Nārāyaṇa.',
      'Into the full pot, [I invoke him] together with the hundred kalās beginning with Śiṃśumāra.',
      'I invoke Śrī Lakṣmī-Nārāyaṇa.',
      'Oṃ. Salutations to Nārāyaṇa. Oṃ.',
      'Salutation to all the deities of the principles.',
      'Salutation to all the Mātṛkā deities.',
      'Salutation to the deities invoked into the kalaśa.'
    ],
    '27': [
      'I offer worship with the sixteen services beginning with arghya.',
      'Because you consist of all sacred places and all holy waters,',
      'therefore you are dear to Hari; O full pot, salutations to you.',
      'By this worship of the kalaśa deities,',
      'may Bhagavān Lakṣmī-Nārāyaṇa be pleased.'
    ],
    '28': [
      'You arose long ago from the ocean and are held in Viṣṇu’s hand.',
      'Revered by all the gods, O Pāñcajanya, salutations to you.',
      'At the beginning of the conch is the Moon as deity; in its middle is Varuṇa as deity.',
      'One should know Prajāpati at its back, and Gaṅgā and Sarasvatī at its front.',
      'Whatever holy waters are in the three worlds, by Vāsudeva’s command,',
      'they abide in the conch, O best of brāhmaṇas; therefore one should worship the conch well.',
      'Oṃ. May we know Pāñcajanya; may we meditate on Mahādara, the conch.',
      'May that conch inspire us.',
      'Oṃ. Salutation to the conch deities.',
      'I offer meditation. I offer invocation.',
      'I offer a seat. I offer welcoming water.',
      'I offer water for the feet. I offer water for sipping.',
      'I offer madhuparka. I offer water for sipping again.',
      'I offer fragrant paste, flowers, and tulasī leaves.',
      'By this worship of the conch,',
      'may Bhagavān Lakṣmī-Nārāyaṇa be pleased.'
    ],
    '29': [
      'Salutation to the great seat that is Viṣṇu’s seat, made of divine jewels,',
      'to the lord of Pradhāna and Puruṣa, to the great pedestal: salutations to you.'
    ]
  });
  Object.assign(reviewed, {
    '30': [
      'Oṃ. The Lord has a body consisting solely of consciousness and bliss, shining like the rising sun.',
      'I meditate on the Lord who bears discus, conch, mace, and lotus.',
      'Embraced by Lakṣmī and Dharā, he stands amid the host of his own forms.',
      '[He is attended] also by Brahmā, Vāyu, Śiva, the serpent-lord, the learned, Śakra, and the rest.',
      'Served with surpassing devotion, he possesses eternal and unlimited power.',
      'His eight forms too are to be meditated on, holding discus, conch, boon, and fearlessness.',
      'They are luminous like lamps and adorned with every ornament.',
      'Oṃ. He is the Self of the gods and the embryo of the world.',
      'This god moves according to his will.',
      'His sounds are heard, but his form is not [seen].',
      'To that Vāta, we offer worship with oblation.'
    ],
    '31': [
      'O Śrī Puruṣottama dwelling in the lotus of the heart, I invoke you.',
      'O Lord of Ramā, come onto this seat, into this image.',
      'O Lord, ruler of the worlds, until the worship is completed,',
      'remain firmly in this image, with a gracious and affectionate disposition.',
      'Oṃ. Salutations to Nārāyaṇa. Be invoked; be established.',
      'Be present nearby; be securely enclosed [here].',
      'Be facing [me]; be veiled [within the image].'
    ],
    '32': [
      'Oṃ. Salutations to Nārāyaṇa. I offer arghya, the welcoming water.',
      'Oṃ. Salutations to Nārāyaṇa. I offer water for the feet.',
      'Oṃ. Salutations to Nārāyaṇa. I offer water for sipping.',
      'Oṃ. Salutations to Nārāyaṇa. I offer madhuparka, the welcoming mixture.',
      'Oṃ. Salutations to Nārāyaṇa. I offer water for sipping again.'
    ],
    '33': [
      'For this Sahasraśīrṣā hymn, Nārāyaṇa is the seer and Puruṣa is the deity.',
      'Anuṣṭup is the metre; its ritual application is the great abhiṣeka.',
      'Oṃ. Puruṣa has a thousand heads, a thousand eyes, and a thousand feet.',
      'Enveloping the earth on every side, he transcended it by ten finger-breadths.',
      'Puruṣa alone is all this: what has been and what will be.',
      'He is also lord of immortality, and of what grows beyond through food.',
      'Such is his greatness; yet Puruṣa is greater still.',
      'All beings are one quarter of him; three quarters of him are immortal in heaven.',
      'Three quarters of Puruṣa rose upward; one quarter of him became this world again.',
      'From that he spread in every direction, over what eats and what does not eat.'
    ],
    '34': [
      'Oṃ. Salutations to Nārāyaṇa. I offer a pair of garments.',
      'Oṃ. Salutations to Nārāyaṇa. I offer ornaments beginning with the Kaustubha jewel.',
      'Oṃ. Salutations to Nārāyaṇa. I offer weapons beginning with the discus.',
      'Oṃ. Salutations to Nārāyaṇa. I offer the sacred thread.',
      'Oṃ. Salutations to Nārāyaṇa. I offer fragrant paste.',
      'Oṃ. Salutations to Nārāyaṇa. I offer unbroken rice grains.',
      'Oṃ. Salutations to Nārāyaṇa. [I offer] many kinds [of flowers] together with tulasī leaves and dūrvā grass,',
      'I offer fragrant flowers.',
      'Salutation to all the deities of the surrounding enclosure.'
    ],
    '35': [
      'This excellent fragrance, divine, born from forest trees, and rich in scent,',
      'this incense, fit to be inhaled by all the gods, may be accepted.',
      'Oṃ. Salutations to Nārāyaṇa. I offer incense.',
      'This lamp, joined with three wicks and ghee, has been lit by me with fire.',
      'O Lord of gods, accept this lamp, remover of the darkness of the three worlds.',
      'Oṃ. Salutations to Nārāyaṇa. I offer the lamp.'
    ],
    '36': [
      'Oṃ. Earth, midregion, heaven. I sprinkle you with truth through cosmic order.',
      'Oṃ. You are the nectar covering; svāhā.',
      'Oṃ. To Nārāyaṇa as the Self of prāṇa, svāhā. This is offered to Nārāyaṇa as the Self of prāṇa; salutation.',
      'Oṃ. To Vāsudeva as the Self of apāna, svāhā. This is offered to Vāsudeva as the Self of apāna; salutation.',
      'Oṃ. To Saṃkarṣaṇa as the Self of vyāna, svāhā. This is offered to Saṃkarṣaṇa as the Self of vyāna; salutation.',
      'Oṃ. To Pradyumna as the Self of udāna, svāhā. This is offered to Pradyumna as the Self of udāna; salutation.',
      'Oṃ. To Aniruddha as the Self of samāna, svāhā. This is offered to Aniruddha as the Self of samāna; salutation.',
      'O Śrīnivāsa, salutations to you; [accept] this excellent great food offering.',
      'O ever-content one, affectionate to devotees, graciously accept this.'
    ]
  });
  Object.assign(reviewed, {
    '37': [
      'Oṃ. I salute the praiseworthy, ever-blissful, stainless Vāsudeva.',
      '[I salute] the husband of Indirā, the primal Lord who grants the choicest boons and places.',
      'O Lord of all, I bow to [your feet], which are like a pedestal rubbed by crowns.',
      '[I bow to] the lotus feet of Śrīpati, sunlike in removing the darkness of the heart.',
      'Oṃ. Salutations to Nārāyaṇa. [I offer] that which is furnished with every accompaniment,',
      'I offer the great food offering beginning with rice and food.'
    ],
    '38': [
      'Oṃ. Salutations to Nārāyaṇa.', 'Oṃ. You are the nectar covering; svāhā.',
      'Oṃ. Salutations to Nārāyaṇa. I offer washing for the hands.', 'I offer water for mouth-rinsing.',
      'I offer a cloth for the face.', 'I offer betel with areca nut.', 'I offer a golden flower.'
    ],
    '39': [
      'Victorious is the unborn Lord, whose vast sphere of qualities is undivided.', 'Ever risen, garlanded with rays of knowledge.',
      'Destroyer of the lofty darkness in the hearts of his own devotees.', 'Hari, incarnate as Vyāsa, is the sun of the self.',
      'Victorious is the unborn Lord, whose essential image is undiminished bliss.', 'Ever risen, extended in the splendor of his own sovereignty.',
      'Destroyer of the suffering and misfortune of his own devotees.', 'Hari, incarnate as Rāma, is the moon among lords.',
      'Victorious is he, an immeasurable flood of mighty strength.', 'An ocean of lofty qualities and the majesty of the self.',
      'Ever attainable through the lamps of knowledge of the eternal self.', 'Hari, incarnate as Kṛṣṇa, is the one ocean.'
    ],
    '40': [
      'Oṃ. Salutation to the great ones; salutation to the small ones.', 'Salutation to the young; salutation to the aged.',
      'We worship the gods, if we are able.', 'O gods, do not cut us off from the praise of those greater than us.',
      'To the king of kings, the mighty conqueror,', 'we offer salutation to Vaiśravaṇa.',
      'May he grant desires to me, who desires desires.', 'May Vaiśravaṇa, lord of desires, grant them.',
      'Salutation to Kubera, Vaiśravaṇa, the great king.', 'Whoever knows this city of Brahman enveloped in immortality,',
      'to him Brahmā gave long life, fame, and offspring.', 'Among them Śauri appeared, with a smiling lotus face.',
      'Wearing yellow garments and a garland, he is Manmatha of Manmatha himself.', 'Oṃ. Salutations to Nārāyaṇa. I offer the mantra flowers.'
    ],
    '41': [
      'Oṃ. Salutations to Nārāyaṇa. I offer a parasol.', 'I offer a yak-tail fly-whisk.', 'I offer a fan.',
      'I offer a mirror.', 'I offer song.', 'I offer dance.', 'I offer instrumental music.',
      'I offer a hymn of praise.', 'I offer all royal services.'
    ],
    '42': [
      'Oṃ. These waters are most auspicious; these are the medicine for all.',
      'These increase the realm; these sustain the realm and are immortal.'
    ],
    '43': [
      'Salutation to Ramā.', 'Oṃ. Salutation to Brahmā. Oṃ. Salutation to Vāyu.',
      'Oṃ. Salutation to Garuḍa. Oṃ. Salutation to Śeṣa.',
      'May Ramā, Brahmā and the other gods, Sanaka and the others, Śuka and the others [receive it].',
      'May all Vaiṣṇavas receive this prasāda of Śrī Nṛsiṃha.'
    ],
    '44': [
      'By whose remembrance and utterance of whose name, in austerity, worship, ritual acts, and the rest,',
      'what is deficient immediately reaches completeness: I bow to that Acyuta.',
      'O Lord of Ramā, [though it be] lacking mantra, lacking ritual action, and lacking devotion,',
      'whatever has been done by me, O Lord, may it be complete for me.',
      'By this sixteen-service worship, may Bhagavān Śrī Lakṣmī-Nārāyaṇa, dwelling within Mukhyaprāṇa',
      '(Bhāratī’s beloved), be pleased. May it be an offering to Śrī Kṛṣṇa.',
      'From time to time, for the expiation of faults of omission in mantra, ritual method, accent, and syllable,',
      'I shall repeat the three-name mantra as atonement.',
      'Oṃ. Salutation to Acyuta. Oṃ. Salutation to Ananta. Oṃ. Salutation to Govinda.',
      'Salutation to Acyuta, Ananta, and Govinda.'
    ],
    '45': [
      'I do not know any action at all, worldly or Vedic.', 'O Viṣṇu, I know neither prohibitions nor injunctions; I am only your servant.',
      'Thousands of offences are committed by me day and night.', 'Forgive all of them for me, O Lord, O Supreme Person.',
      'I am not the doer; Hari is the doer, and the entire act is his worship.',
      'Even so, the worship performed by me occurs only through his grace, and no other way.',
      'There is no sinner like me, and none as supremely compassionate as you.',
      'Thinking, “this one is your servant,” forgive me, O Supreme Person.',
      'I am sinful; I do sinful deeds; I have a sinful nature and sinful origin.',
      'Save me, O lotus-eyed one, tender toward those who seek refuge.',
      'There is no other refuge; you alone are my refuge.',
      'Therefore, with a compassionate disposition, protect me, protect me, O Janārdana.',
      'May he who is complete in all qualities and free from every defect',
      'Viṣṇu, my supreme friend, be pleased for my joy and welfare.'
    ],
    '46': [
      'Whatever sins have been committed, even in former births,', 'all those perish with every step of circumambulation.',
      'Thousands of crores of sacred waters and hundreds of crores of vows',
      'do not equal even a sixteenth part of a prostration to Nārāyaṇa.',
      'With chest, head, sight, mind, and speech,', 'with feet, hands, and knees: this prostration is called eight-limbed.',
      'Salutations to Ananta, who has a thousand forms,', 'who has a thousand feet, eyes, heads, and mighty arms,',
      'to the eternal Puruṣa of a thousand names,', 'salutations to the one who upholds a thousand crores of ages.',
      'Salutations to the god devoted to sacred learning, to the benefactor of cows and brāhmaṇas,',
      'to the welfare of the world, to Kṛṣṇa, to Govinda: repeated salutations.',
      'To him whose form is auspicious and wondrous, who grants desired aims,',
      'to glorious Veṅkaṭanātha, to Śrīnivāsa: salutations to you.',
      'Salutation, salutation, salutation. I always bow to your feet.',
      'I bow to you again and again, supreme in all noble qualities.'
    ],
    '47': ['May it be an offering to Śrī Kṛṣṇa.']
  });
  Object.keys(reviewed).forEach((id) => {
    let index = 0;
    entries[id].lines.forEach((line) => {
      if (line && line.kind !== 'direction') line.meaning = reviewed[id][index++];
    });
    entries[id].status = 'Exact guide text retained; line meanings and word glosses reviewed against the Sanskrit. Audio wording still requires a final listening check.';
  });
  // In the Puruṣa Sūkta, bhūtāni means beings; step 09 uses the same form
  // in a different ritual context where “spirits” is the appropriate gloss.
  entries['33'].lines.forEach((line) => {
    if (!line || !line.words) return;
    line.words.forEach((word) => {
      if (clean(word.text).toLowerCase() === 'bhūtāni') word.meaning = 'beings';
    });
  });
  // ID 02 was corrected against the timed recording caption, Tantrasāra-
  // Saṅgraha 70 and the cited Kṛṣṇāmṛta-mahārṇava verses. The short phrase
  // following the last printed line remains uncertain in the noisy caption.
  entries['02'].status = 'Aligned to timed caption and Sanskrit editions; the last short phrase and final listening check remain open.';
  const gloryMeanings = [
    'Having known Hari as supreme above all, whoever worships him thus, always and with devotion,',
    'through japa, meditation, and the like finds nothing difficult to attain.',
    'In this dreadful cycle of worldly existence, beset by birth, illness, and fear,',
    'worship of Adhokṣaja alone is a great good fortune.',
    'Of the Lord of all worlds, the God of gods, the bearer of the Śārṅga bow,',
    'direct worship of the Blessed Lord Viṣṇu is the fruit of human birth.',
    'While there is health in the body and vigor in the faculties,',
    'worship Govinda then, and make your lifespan meaningful.'
  ];
  let gloryIndex = 0;
  entries['02'].lines.forEach((line) => { if (line) line.meaning = gloryMeanings[gloryIndex++]; });
  entries['02'].lines[0].words = [
    {text:'sarvottamaṃ',meaning:'supreme above all'}, {text:'hariṃ',meaning:'Hari (object of “having known”)'},
    {text:'jñātvā',meaning:'having known'}, {text:'ya',meaning:'whoever'}, {text:'evaṃ',meaning:'thus'},
    {text:'bhaktipūrvakam',meaning:'with devotion'}
  ];
  entries['02'].lines[1].words = [
    {text:'japadhyānādibhir',meaning:'through japa, meditation, and the other practices'},
    {text:'nityaṃ',meaning:'always'}, {text:'pūjayen',meaning:'one worships (pūjayet)'},
    {text:'nāsya',meaning:'na, not + asya, for him'}, {text:'durlabham',meaning:'difficult to attain'}
  ];
  const gloryChantLines = entries['02'].lines.filter(Boolean);
  gloryChantLines[3].words = [
    {text:'ayam',meaning:'this'}, {text:'eko',meaning:'one/alone'},
    {text:'mahābhāgaḥ',meaning:'great good fortune'}, {text:'pūjyate',meaning:'is worshipped'},
    {text:'yad',meaning:'because/that'}, {text:'adhokṣajaḥ',meaning:'Adhokṣaja, Lord beyond sensory grasp'}
  ];
  gloryChantLines[4].words = [
    {text:'samasta-loka-nāthasya',meaning:'samasta (all) + loka (worlds) + nāthasya (of the Lord)'},
    {text:'deva-devasya',meaning:'deva (gods) + devasya (of the God)'},
    {text:'śārṅgiṇaḥ',meaning:'of the bearer of the Śārṅga bow'}
  ];
  gloryChantLines[5].words = [
    {text:'sākṣād',meaning:'directly'}, {text:'bhagavato',meaning:'of the Blessed Lord'},
    {text:'viṣṇoḥ',meaning:'of Viṣṇu'}, {text:'pūjanaṃ',meaning:'worship'},
    {text:'janmanaḥ',meaning:'of birth'}, {text:'phalam',meaning:'fruit/purpose'}
  ];
  gloryChantLines[6].words = [
    {text:'yāvat',meaning:'as long as'}, {text:'svāsthyaṃ',meaning:'health'},
    {text:'śarīreṣu',meaning:'in the bodies/body'}, {text:'karaṇeṣu',meaning:'in the faculties'},
    {text:'ca',meaning:'and'}, {text:'pāṭavam',meaning:'ability/vigor'}
  ];
  gloryChantLines[7].words = [
    {text:'tāvad',meaning:'then/for that long'}, {text:'arcaya',meaning:'worship (imperative)'},
    {text:'govindam',meaning:'Govinda'}, {text:'āyuṣyaṃ',meaning:'lifespan'},
    {text:'sārthakaṃ',meaning:'fruitful/meaningful'}, {text:'kuru',meaning:'make'}
  ];
  // Spell out dense compounds and audible sandhi at the point of chanting.
  // These notes add the underlying words without changing the recording line.
  const resolved = {
    // Pavilion description (step 22).
    'tapta-jvalat-kāñcana-racitaṃ':'tapta (molten) + jvalat (blazing) + kāñcana (gold) + racita (made of)',
    'tuṅgāṅga-raṅga-sthalaṃ':'tuṅga (lofty) + aṅga-raṅga-sthala (performance hall)',
    'śuddha-sphāṭika-bhitti-kavilasitaiḥ':'śuddha (pure) + sphāṭika (crystal) + bhitti (walls) + kavilasita (shining)',
    'ratna-rāja-khacitaiḥ':'ratna-rāja (finest jewels) + khacita (inlaid)',
    'śaṅkha-padma-dhavalaiḥ':'śaṅkha (conch) + padma (lotus) + dhavala (white)',
    'muktā-jāla-vilambi-maṇṭapa-yutaṃ':'muktā-jāla (pearl nets) + vilambi (hanging) + maṇṭapa-yuta (endowed with a pavilion)',
    'vajra-sopānakaiḥ':'vajra (diamond) + sopānaka (stairways)',
    'nānā-ratna-vinirmitaiś':'nānā-ratna (various jewels) + vinirmita (made)',
    'māṇiky-ujjvala-dīpa-dīpta-vilasat-lakṣmī-vilāsāspadam':'māṇikya-ujjvala-dīpa (bright ruby lamps) + dīpta-vilasat (shining) + lakṣmī-vilāsa-āspada (abode of Lakṣmī’s splendour)',
    'raṅgavalī-dhvaja-ketakī-toraṇaiḥ':'raṅgavalī (floor designs) + dhvaja (flags) + ketakī (ketakī banners) + toraṇa (festoon)',
    'ikṣu-kadalī-pūrṇa-kumbhāṅkurādibhiḥ':'ikṣu (sugarcane) + kadalī (banana plants) + pūrṇa-kumbha (full pots) + aṅkura-ādi (sprouts and the rest)',
    'gīta-vāditra-nṛtyaiś':'gīta (song) + vāditra (instrumental music) + nṛtya (dance)',
    'purāṇa-paṭhanaiḥ':'purāṇa (Purāṇas) + paṭhana (recitation)',
    // Saṅkalpa time, place, and purpose compounds (step 24).
    'dvitīya-parārdhe':'dvitīya (second) + parārdha (half of Brahmā’s life)',
    'śveta-varāha-kalpe':'śveta-varāha (White Boar) + kalpa (aeon)',
    'vaivasvata-manvantare':'vaivasvata (Vaivasvata) + manvantara (Manu period)',
    'aṣṭāviṃśatitame':'aṣṭāviṃśati (twenty-eight) + tama (ordinal)',
    'kali-yuge':'Kali + yuga (age)',
    'prathama-pāde':'prathama (first) + pāda (quarter)',
    'jambū-dvīpe':'Jambū + dvīpa (island-continent)',
    'bhārata-varṣe':'Bhārata + varṣa (region)',
    'śālivāhana-śake':'Śālivāhana + śaka (era)',
    'bauddhāvatāre':'bauddha (Buddha) + avatāra (incarnation)',
    'rāma-kṣetre':'Rāma + kṣetra (sacred place)',
    'śubha-nakṣatra-śubha-yoga-śubha-karaṇa-':'śubha-nakṣatra (auspicious lunar mansion) + śubha-yoga (auspicious yoga) + śubha-karaṇa (auspicious karaṇa)',
    'evaṃ-guṇa-viśeṣaṇa-viśiṣṭāyāṃ':'evaṃ (such) + guṇa-viśeṣaṇa (qualities and attributes) + viśiṣṭa (distinguished)',
    'śrī-bhāratī-ramaṇa-mukhya-prāṇāntargata':'Śrī (revered) + Bhāratī-ramaṇa (beloved of Bhāratī) + Mukhyaprāṇa-antargata (dwelling within Mukhyaprāṇa)',
    'śrī-lakṣmī-nārāyaṇa-preraṇayā':'Śrī Lakṣmī-Nārāyaṇa + preraṇā (prompting)',
    'śrī-lakṣmī-nārāyaṇa-prītyartham':'Śrī Lakṣmī-Nārāyaṇa + prīti-artham (for the pleasure of)',
    'yathā-militopacāra-dravyaiḥ':'yathā-milita (available) + upacāra-dravya (worship materials)',
    'dhyānāvāhanādi-ṣoḍaśopacāra-pūjāṃ':'dhyāna-āvāhana-ādi (beginning with meditation and invocation) + ṣoḍaśopacāra-pūjā (sixteen-service worship)',
    // Dhyāna and ārati compounds (steps 30 and 39).
    'udyad-bhāsvat-samābhāsaś':'udyat (rising) + bhāsvat (shining) + samābhāsa (radiance)',
    'cid-ānandaika-dehavān':'cit-ānanda (consciousness and bliss) + eka-deha (single body)',
    'cakra-śaṅkha-gadā-padma-dharo':'cakra (discus) + śaṅkha (conch) + gadā (mace) + padma (lotus) + dhara (bearer)',
    'lakṣmī-dharābhyām':'Lakṣmī + Dharā (Bhū), the two consorts',
    'sva-mūrti-gaṇa-madhyagaḥ':'sva-mūrti-gaṇa (his own forms) + madhyaga (standing amid)',
    'brahma-vāyu-śivāhīśa-vipaiḥ':'Brahmā + Vāyu + Śiva + ahīśa (serpent-lord) + vipra (learned ones)',
    'nitya-niḥśeṣa-śaktimān':'nitya (eternal) + niḥśeṣa (unlimited) + śaktimān (possessing power)',
    'cakra-śaṅkha-varābhayaiḥ':'cakra (discus) + śaṅkha (conch) + vara (boon) + abhaya (fearlessness)',
    'khaṇḍa-guṇoru-maṇḍalaḥ':'a-khaṇḍa (undivided) + guṇa-uru-maṇḍala (vast sphere of qualities)',
    'sva-bhakta-hārd-occha-tamo-nihantā':'sva-bhakta (his devotees) + hārd (of the heart) + uccha-tamas (deep darkness) + nihantṛ (destroyer)',
    'kṣīṇa-sukhātma-bimbaḥ':'a-kṣīṇa (undiminished) + sukha-ātma-bimba (blissful self-image)',
    'svaiśvarya-kānti-pratataḥ':'sva-aiśvarya (his own sovereignty) + kānti (splendour) + pratata (extended)',
    'sva-bhakta-santāpa-duriṣṭa-hantā':'sva-bhakta (his devotees) + santāpa (suffering) + duriṣṭa (misfortune) + hantṛ (destroyer)',
    'īśa-candramāḥ':'īśa (lords) + candramas (moon)',
    'asaṃkhyoru-balāmbu-pūro':'asaṃkhya (countless) + uru-bala (mighty strength) + ambu-pūra (flood)',
    'guṇocca-ratnākara':'guṇa-ucca (lofty qualities) + ratnākara (ocean of jewels)',
    'sadātma-jñāna-dībhir':'sad-ātma (eternal self) + jñāna-dī (lamps of knowledge)',
    // Completion and prostration compounds (steps 44 and 46).
    'tapaḥ-pūjā-kriyādiṣu':'tapas (austerity) + pūjā (worship) + kriyā-ādi (ritual acts and the rest)',
    'ṣoḍaśopacāra-pūjanena':'ṣoḍaśa-upacāra (sixteen services) + pūjana (worship)',
    'bhāratī-ramaṇa-mukhya':'Bhāratī-ramaṇa (beloved of Bhāratī) + Mukhyaprāṇa',
    'mantra-tantra-svara-varṇa-lopa-doṣa':'mantra (mantra) + tantra (ritual method) + svara (accent) + varṇa (syllable) + lopa (omission) + doṣa (fault)',
    'tīrtha-koṭi-sahasrāṇi':'tīrtha (sacred waters) + koṭi (crore) + sahasra (thousand)',
    'vrata-koṭi-śatāni':'vrata (vows) + koṭi (crore) + śata (hundred)',
    'nārāyaṇa-praṇāmasya':'Nārāyaṇa + praṇāma (prostration)',
    'sahasra-pādākṣi-śiroru-bāhave':'sahasra (thousand) + pāda-akṣi-śiras-uru-bāhu (feet, eyes, heads, and mighty arms)',
    'sahasra-koṭi-yuga-dhāriṇe':'sahasra-koṭi (thousand crores) + yuga (ages) + dhārin (upholder)',
    'brahmaṇya-devāya':'brahmaṇya (devoted to sacred learning) + deva (god)',
    'go-brāhmaṇa-hitāya':'go (cows) + brāhmaṇa (brāhmaṇas) + hita (benefactor)',
    'jagad-dhitāya':'jagat (world) + hita (welfare/benefit)',
    'kalyāṇādbhuta-gātrāya':'kalyāṇa (auspicious) + adbhuta (wondrous) + gātra (form)',
    'kāmitārtha-pradāyine':'kāmita-artha (desired aims) + pradāyin (giver)',
    'samasta-sad-guṇottamaṃ':'samasta (all) + sat-guṇa (noble qualities) + uttama (supreme)',
    'sāgarotpanno':'sāgara (ocean) + utpannaḥ (arisen)',
    'sarva-devaiś':'sarva (all) + devaiḥ (by the gods); final ḥ joins ca',
    'śaṅkhādau':'śaṅkha (conch) + ādau (at the beginning)',
    'candra-daivatyaṃ':'candra (Moon) + daivatya (having as presiding deity)',
    'varuṇa-daivatam':'varuṇa (Varuṇa) + daivata (presiding deity)',
    'gaṅgā-sarasvatī':'Gaṅgā + Sarasvatī',
    'trailokye':'tri (three) + lokya/loka (worlds), in the three worlds',
    'cājñayā':'ca (and) + ājñayā (by command)',
    'tasmāt':'therefore; from that',
    'śaṅkhaṃ':'the conch, object of worship',
    'mahādarāya':'to Mahādara, an epithet of the conch',
    'gandha-puṣpa-tulasī-patrāṇi':'gandha (sandal paste) + puṣpa (flowers) + tulasī-patrāṇi (tulasī leaves)',
    'japadhyānādibhir':'japa (repetition) + dhyāna (meditation) + ādibhiḥ (and similar practices; instrumental plural)',
    'bhaktipūrvakam':'bhakti (devotion) + pūrvakam (preceded/accompanied by)',
    'janma-roga-bhayākule':'janma (birth) + roga (illness) + bhaya (fear) + ākula (beset by)',
    'svastha-śarīraṃ':'svastha (healthy) + śarīra (body)',
    'mitrāvaruṇobhā':'Mitra + Varuṇa + ubhau (both)',
    'indrāgnī':'Indra + Agni, the two gods',
    'suvarṇarajatasrajām':'suvarṇa (gold) + rajata (silver) + sraj (garland): wearing their garlands',
    'lakṣmīmanapagāminīm':'lakṣmīm (Lakṣmī) + anapagāminīm (never departing)',
    'gāmaśvaṃ':'gām (cattle) + aśvam (horse)',
    'puruṣānaham':'puruṣān (people) + aham (I)',
    'aśvapūrvāṃ':'aśva (horses) + pūrvām (preceded by)',
    'hastinādapramōdinīm':'hasti (elephant) + nāda (sound) + pramodinīm (delighted by)',
    'śrīrmā':'śrīḥ (Śrī) + mā (me); may Śrī favor me',
    'sarva-kṣetra-mayo':'sarva (all) + kṣetra (sacred places) + maya (consisting of)',
    'sarva-tīrtha-mayo':'sarva (all) + tīrtha (holy waters) + maya (consisting of)',
    'hari-priyo':'hari (Hari) + priyaḥ (dear to)',
    'pūrṇa-kumbha':'pūrṇa (full) + kumbha (pot)'
  };
  Object.values(entries).forEach((entry) => entry.lines.forEach((line) => {
    if (!line || !line.words) return;
    line.words.forEach((word) => {
      if (resolved[word.text]) word.meaning = resolved[word.text];
    });
  }));
  window.ACHAR_GLOSSES = entries;
})();
