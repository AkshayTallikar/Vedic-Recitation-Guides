// Ṛgvedīya Sandhyāvandana — Mādhva Rig-Veda protocol.
// Text-only (no recordings). Several steps change with the time of day:
// use the Prātaḥ / Mādhyāhnika / Sāyaṃ selector above the list. Sections
// that vary carry a "changes by sandhyā" tag; the {p}/{pe} tokens in the
// saṅkalpa lines are swapped for the selected sandhyā's word by app.js.
(window.GUIDES = window.GUIDES || []).push({
  key: "rvsandhya",
  tabLabel: "Ṛgvedīya Sandhyāvandana",
  noAudio: true,
  title: "Ṛgvedīya Sandhyāvandana",
  subtitle: "The Mādhva Rig-Veda Sandhyāvandana — pick Prātaḥ / Mādhyāhnika / Sāyaṃ above to switch the mantras that change with the time of day",
  source: "https://bhaktideets.org",
  sourceLabel: "source e-book",
  sourceCredit: "Māadhva Sandhyāvandana Paddhati — Prājña Paṭṭada Hari Kumāra Varma (Achyuta Bhakti Deets, 2026) · Ṛgvedīya Sandhyāvandana, pp. 16–33",
  periodLabel: "Sandhyā",
  periods: [
    { key: "pratah", label: "Prātaḥ · morning", word: "prātaḥ", en: "morning" },
    { key: "madhyahnika", label: "Mādhyāhnika · midday", word: "mādhyāhnika", en: "midday" },
    { key: "sayam", label: "Sāyaṃ · evening", word: "sāyaṃ", en: "evening" }
  ],
  sections: [

    // ===================== OPENING =====================
    {
      id: "01", slug: "apavitrah", group: "Opening", page: "16",
      title: "Apavitraḥ — purification shloka",
      mantra:
        "oṃ apavitraḥ pavitro vā sarvāvasthāṃ gato'pi vā |\n" +
        "yassmaret puṇḍarīkākṣaṃ sa bāhyābhyantaraśśuciḥ ||",
      meaning:
        "Whether one is impure or pure, or in whatsoever condition one may be, whoever remembers the lotus-eyed Lord (Puṇḍarīkākṣa, Viṣṇu) becomes pure both within and without. (Padma Purāṇa, Pātāla Khaṇḍa, Adhyāya 80, Shloka 12.)",
      action:
        "Sit down facing the East or North in the morning, and the North during the midday and evening. Chant this shloka first, and then the Guru mantra that follows."
    },
    {
      id: "02", slug: "guru-mantra", group: "Opening", page: "16",
      title: "Guru-vandana (Guru Mantra)",
      mantra:
        "oṃ śrī gurubhyo namaḥ | oṃ paramagurubhyo namaḥ | oṃ ādigurubhyo namaḥ | oṃ mūlagurubhyo namaḥ | oṃ śrīmadānandatīrthabhagavatpādācāryebhyo namaḥ | oṃ vedavyāsāya namaḥ | oṃ bhāratyai namaḥ | oṃ sarasvatyai namaḥ | oṃ vāyave namaḥ | oṃ brahmaṇe namaḥ | oṃ mahālakṣmyai namaḥ | oṃ nārāyaṇāya namaḥ | oṃ haraye namaḥ | mokṣapradaśrīvāsudevāya namaḥ |",
      meaning:
        "Salutations to the Śrī Gurus; to the Parama-guru; to the Ādi-guru; to the Mūla-guru; to Śrīmad Ānandatīrtha Bhagavatpādācārya (Madhvācārya); to Vedavyāsa; to Bhāratī; to Sarasvatī; to Vāyu; to Brahmā; to Mahālakṣmī; to Nārāyaṇa; to Hari; and to Śrī Vāsudeva, the giver of mokṣa.",
      action:
        "Recite the Guru mantra after the purification shloka. If ūrdhvapuṇḍra tilaka has not yet been applied, apply it at least on the forehead (with gopī-candana or another suitable material), as per the instructions given in the Tattvavādi Vaiṣṇava handbook."
    },

    // ===================== ĀCAMANA & PRĀṆĀYĀMA =====================
    {
      id: "03", slug: "acamana", group: "Ācamana & prāṇāyāma", page: "16–17",
      title: "1 · Ācamana",
      mantra:
        "oṃ keśavāya svāhā |\n" +
        "oṃ nārāyaṇāya svāhā |\n" +
        "oṃ mādhavāya svāhā |\n" +
        "(take a little water from the right hand and spill it)\n\n" +
        "oṃ govindāya namaḥ | (wash the right palm with the left palm)\n" +
        "oṃ viṣṇave namaḥ | (wash the left palm with the right palm)\n" +
        "oṃ madhusūdanāya namaḥ | (touch the upper lip)\n" +
        "oṃ trivikramāya namaḥ | (touch the lower lip)\n" +
        "oṃ vāmanāya namaḥ | (touch the right cheek)\n" +
        "oṃ śrīdharāya namaḥ | (touch the left cheek)\n" +
        "oṃ hṛṣīkeśāya namaḥ | (wash both the hands)\n" +
        "oṃ padmanābhāya namaḥ | (touch the feet)\n" +
        "oṃ dāmodarāya namaḥ | (touch the centre of the head with the middle finger of the right hand)\n" +
        "oṃ saṅkarṣaṇāya namaḥ | (touch the tip of the nose with the middle finger of the right hand)\n" +
        "oṃ vāsudevāya namaḥ | (touch the right side of the nose with the index finger and thumb)\n" +
        "oṃ pradyumnāya namaḥ | (touch the left side of the nose with the index finger and thumb)\n" +
        "oṃ aniruddhāya namaḥ | (touch the right eye with the index and middle fingers)\n" +
        "oṃ puruṣottamāya namaḥ | (touch the left eye with the index and middle fingers)\n" +
        "oṃ adhokṣajāya namaḥ | (touch the right ear with the index and ring fingers)\n" +
        "oṃ nārasiṃhāya namaḥ | (touch the left ear with the index and ring fingers)\n" +
        "oṃ acyutāya namaḥ | (touch the navel with the index and little fingers)\n" +
        "oṃ janārdanāya namaḥ | (touch the chest, at the heart, with the palm of the right hand)\n" +
        "oṃ upendrāya namaḥ | (touch the head with the right hand)\n" +
        "oṃ haraye namaḥ | (touch the right shoulder with all fingers of the right hand)\n" +
        "oṃ kṛṣṇāya namaḥ | (touch the left shoulder with all fingers of the right hand)",
      meaning:
        "While sipping water after the first three lines, and while touching the parts of the body during the twenty-four names, one contemplates the respective forms of Viṣṇu — Keśava, Nārāyaṇa, Mādhava, Govinda, Viṣṇu, Madhusūdana, Trivikrama, Vāmana, Śrīdhara, Hṛṣīkeśa, Padmanābha, Dāmodara, Saṅkarṣaṇa, Vāsudeva, Pradyumna, Aniruddha, Puruṣottama, Adhokṣaja, Nārasiṃha, Acyuta, Janārdana, Upendra, Hari and Kṛṣṇa — remembering the Devatās presiding over each organ (Agni at the mouth, Vāyu at the nose, Sūrya at the eyes, Indra at the ears, Nārāyaṇa at the chest and navel, Prajāpati at the shoulders, and Paramātmā at the head).",
      action:
        "Ācamana is always performed twice. Pour a small quantity of water into the 'Brahma-tīrtha' part of the right palm and sip it after each of the first three lines; then take a little water and spill it. Keep the arms and hands within the span of the legs while seated; do not lift the water poured on the palm, and make no noise while sipping — the force of sipping must come from the muscles of the abdomen. Then, reciting the twenty-four names, touch each named part of the body with the fingers of the right hand exactly as indicated (this is the Aṅga-nyāsa)."
    },
    {
      id: "04", slug: "vighna-apaharana", group: "Ācamana & prāṇāyāma", page: "17",
      title: "2 · Vighna-Apaharaṇa",
      mantra:
        "śuklāmbaradharaṃ viṣṇuṃ śaśivarṇaṃ caturbhujaṃ |\n" +
        "prasannavadanaṃ dhyāyet sarvavighnopaśāntaye ||",
      meaning:
        "For the removal of all obstacles, one should meditate upon Viṣṇu, who is clad in white garments, moon-hued, four-armed, and of a gracious countenance.",
      action:
        "With the fists, tap the temples near the forehead about five times while reciting this shloka, with the thought that the spiritual energy from there is dissipating throughout the body."
    },
    {
      id: "05", slug: "pranayama", group: "Ācamana & prāṇāyāma", page: "17",
      title: "3 · Prāṇāyāma",
      mantra:
        "[Nyāsa]\n" +
        "oṃ praṇavasya parabrahma ṛṣiḥ | paramātmā devatā | daivī gāyatrī chandaḥ | saptānāṃ vyāhṛtīnāṃ viśvāmitra-jamadagni-bharadvāja-gautama-atri-vasiṣṭha-kaśyapā ṛṣayaḥ | agni-vāyu-āditya-bṛhaspati-varuṇa-indra-viśvedevā devatāḥ | gāyatrī-uṣṇik-anuṣṭup-bṛhatī-paṅkti-triṣṭup-jagatyaḥ chandāꣳsi | gāyatrī śirasaḥ prajāpatiḥ ṛṣiḥ | brahma-agni-vāyu-ādityā devatāḥ | yajuḥ chandaḥ | prāṇāyāme viniyogaḥ ||\n\n" +
        "[Prāṇāyāma with the Gāyatrī]\n" +
        "oṃ bhūḥ | oṃ bhuvaḥ | oṃ svaḥ | oṃ mahaḥ | oṃ janaḥ | oṃ tapaḥ | oṃ satyam | oṃ tatsaviturvareṇyam | bhargo devasya dhīmahi dhīyo yo naḥ pracodayāt |\n" +
        "oṃ āpojyotīraso'mṛtaṃ brahma bhūrbhuvaḥssvarom ||",
      meaning:
        "In the Nyāsa, the Ṛṣi, Chandas and Devatā of the praṇava and of the seven vyāhṛtis are declared, so that the mantra bears fruit. The prāṇāyāma mantra then invokes the seven vyāhṛtis — bhūḥ, bhuvaḥ, svaḥ, mahaḥ, janaḥ, tapaḥ, satyam (the seven worlds) — followed by the Gāyatrī: 'We meditate upon the adorable effulgence of the Deva Savitṛ; may He impel our intellects.' The closing line affirms that the waters, light, essence, nectar and Brahman pervade the three worlds (bhūḥ, bhuvaḥ, svaḥ) and beyond — Om. (Taittirīya Āraṇyaka, Prapāṭhaka 10, Anuvāka 35, Mantra 2.)",
      action:
        "Prāṇāyāma is done thrice. First perform the Nyāsa — placing the right hand on the head while mentioning the Ṛṣi, on the mouth while mentioning the Chandas, on the heart while mentioning the Devatā, and rotating the hands at the chest for the viniyoga. Then perform rechaka (block the left nostril and exhale through the right), pūraka (block the right nostril and inhale through the left, for twice the duration of rechaka), and kumbhaka (hold the breath for the combined duration of both, while contemplating Paramātmā and chanting the mantra). Brahmacārīs, Sanyāsīs and anyone unmarried use only three fingers — the little finger on the left nostril and the index finger and thumb on the right, with the middle and ring fingers curled into the palm; gṛhasthas use all five fingers. After three rounds, exhale through the right nostril, place the right hand on the right ear remembering Gaṅgā (śrotrācamana), then place the right palm over the left palm on the right thigh (brahmāñjali), and state the saṅkalpa."
    },

    // ===================== SAṄKALPA & MĀRJANA =====================
    {
      id: "06", slug: "sankalpa", group: "Saṅkalpa & mārjana", page: "18–19",
      title: "4 · Saṅkalpa",
      mantra:
        "śrī śubhe śobhane muhūrte viṣṇorājñayā pravartamānasya ādya brahmaṇaḥ dvitīye parārdhe śrī śvetavarāha kalpe vaivasvata manvantare aṣṭāviṃśatitame kaliyuge prathamapāde jambūdvīpe bharatavarṣe bharatakhaṇḍe daṇḍakāraṇye godāvaryāḥ dakṣiṇe pārśve śālīvāhanaśake bauddhāvatāre rāmakṣetre asminvartamānena cāndramānena asya śrī ____ saṃvatsare ____ ayane ____ ṛtau ____ māse ____ pakṣe ____ tithau ____ vāsare ____ nakṣatre śubhayoga śubhakaraṇa evaṅguṇa viśeṣaṇa viśiṣṭāyāṃ śubhatithau |\n" +
        "asmadādigurūṇāṃ śrīmanmadhvācāryāṇāṃ hṛtkamalamadhyanivāsī savitṛnāmaka śrī lakṣmīnārāyaṇa preraṇayā śrī lakṣmīnārāyaṇa prītyarthaṃ {p} sandhyāmupāśiṣye ||",
      meaning:
        "During this auspicious muhūrta, as destined by Śrī Viṣṇu's will, during the second half of Brahmā's lifespan, in the Śvetavarāha kalpa, Vaivasvata manvantara, in the first quarter of the 28th Kali Yuga, at Jambūdvīpa, Bhāratavarṣa, Bhāratakhaṇḍa, at the south of the Godāvarī, towards the coast, during the time of Buddha's avatāra, at the region of Rāma, in this present moment in relation to the lunar movements, in the saṃvatsara (year) called ____, during the ____ ayana, ____ ṛtu, ____ māsa, ____ pakṣa, ____ tithi and ____ vāsara (day), with the ____ nakṣatra (star), may there be an auspicious yoga and karaṇa, with auspicious qualities and everything being specially auspicious. Through us, for the purpose of pleasing Śrī Lakṣmī-Nārāyaṇa who is residing with the name 'Savitṛ' as the Indweller in the heart of our Ādi Guru, Śrī Madhvācārya, I am performing the {pe} sandhyā.",
      action:
        "Seated in brahmāñjali, chant the saṅkalpa, filling in the names of the saṃvatsara (year), ayana, ṛtu (season), māsa (month), pakṣa, tithi, vāsara (day) and nakṣatra as per the pañcāṅga. If in North India, say 'godāvaryāḥ uttare' in place of 'dakṣiṇe pārśve'; near the Western Ghats, say 'paraśurāmakṣetre'. Once this main saṅkalpa has been stated, the additional saṅkalpas mentioned for the later steps are not mandatory."
    },
    {
      id: "07", slug: "marjana", group: "Saṅkalpa & mārjana", page: "19–20",
      title: "5 · Mārjana",
      mantra:
        "āpohiṣṭhetyasya ambarīṣaḥ sindhudvīpa ṛṣiḥ | āpo devatā | gāyatrī chandaḥ | mārjane viniyogaḥ |\n\n" +
        "oṃ āpo hi ṣṭhā mayo bhuvaḥ | tā na ūrje dadhātana | (sprinkle water over the head)\n" +
        "mahe raṇāya cakṣase | yo vaśśivatamo rasaḥ |\n" +
        "tasya bhājayate ha naḥ | uśatīriva mātaraḥ |\n" +
        "tasmā araṅ gamāma vaḥ |\n" +
        "yasya kṣayāya jinvatha | (sprinkle water on the feet)\n" +
        "āpo janayathā ca naḥ | (sprinkle water again on the head)",
      meaning:
        "O water, bestow us bliss by causing this water to flow, bless us with nourishment, like our mothers. We gladly approach you, so that you may guide us to His abode (Śrī Viṣṇu's). Make us pure through the wisdom which grants bhakti.",
      action:
        "Take water in the uddharaṇī with the left hand and, using the ring finger of the right hand, sprinkle water while chanting. Sprinkle over the head while reciting the first seven mantras (down to 'tasmā araṅ gamāma vaḥ'), sprinkle on the feet at 'yasya kṣayāya jinvatha', and sprinkle again on the head at 'āpo janayathā ca naḥ'. The water must reach each body part exactly as the last syllable of each line is completed — neither early nor late."
    },
    {
      id: "08", slug: "mantracamana", group: "Saṅkalpa & mārjana", page: "20–21",
      title: "6 · Mantrācamana",
      meaning: "The mantra for this step changes with the sandhyā — select the time of day above.",
      action:
        "Pour an uddharaṇī full of water into the palm of the right hand, recite the mantra shown for the present sandhyā, and then sip it.",
      periods: {
        pratah: {
          sanskrit: "Prātaḥ · Sūryaśca (night's sins)",
          mantra:
            "sūryaścetyasya mantrasya | nārāyaṇa ṛṣiḥ | sūryamāmanyu manyupatayo rātrirdevatā | prakṛtiśchandaḥ | jalābhimantraṇe viniyogaḥ ||\n\n" +
            "oṃ | sūryaścamāmanyuścamanyupatayaśca manyukṛtebhyaḥ | pāpebhyo rakṣantām | yadrātryā pāpamakārṣam | manasā vācā hastābhyām | padbhyāmudareṇa śiśnā | rātristadavalumpatu | yatkiñca duritaṃ mayi | idamahaṃ māmamṛtayonau | sūrye jyotiṣi juhomi svāhā ||",
          meaning:
            "You are the Master of Sūrya, who is very bright. You are the one who controls Rudra, who is known for his wildness. Protect us from the pāpas which are caused by the ferocity and the initiatives of the Devatās, the pāpas which occurred during the night, be it through the mind, speech, hands, feet, belly or genitals. May any sins in me committed during the night be forgiven by the abhimāni of rātri (night). I offer all these to You, residing in Sūrya, as an oblation, for the welfare of all."
        },
        madhyahnika: {
          sanskrit: "Mādhyāhnika · Āpaḥ punantu (purification)",
          mantra:
            "āpaḥ punantviti mantrasya pūtanāmako nārāyaṇaḥ ṛṣiḥ | āpo devatā | aṣṭī chandaḥ | prāśane viniyogaḥ ||\n\n" +
            "āpaḥ punantu pṛthivīṃ pṛthivī pūtā punātu mām | punantu brahmaṇaspatirbrahma pūtā punātu mām | yaducchiṣṭham abhojyam yad vā duścaritam mama | sarvaṃ punantu mām āpo'satāṃ ca pratigṛhaꣳ svāhā ||",
          meaning:
            "May the waters purify the Earth and may the Earth purify me. May Brahmaṇaspati also be purified and may Brahman purify me. May I be purified from all the demerits of consuming the remnants of others' food and other forbidden articles, or receiving from the wrong people. I offer myself into the fire of enlightenment."
        },
        sayam: {
          sanskrit: "Sāyaṃ · Agniśca (day's sins)",
          mantra:
            "agniśceti mantrasya hiraṇyagarbha ṛṣiḥ | agni-manyu-manyupatyahāni devatāḥ | prakṛtiśchandaḥ | mantrācamane viniyogaḥ |\n\n" +
            "agniścamā manyuśca manyu patayaśca manyukṛtebhyaḥ | pāpebhyo rakṣantām | yadahnā pāpamakārṣam | manasā vācā hastābhyām | padbhyāmudareṇa śiśnā | ahastadavaluṃpatu | yatkiñca duritaṃ mayi | idamahaṃ māmamṛtayonau | satye jyotiṣi juhomi svāhā ||",
          meaning:
            "You are the Master of Agni, who is very bright. You are the one who controls Rudra, who is known for his wildness. Protect us from the pāpas which are caused by the ferocity and the initiatives of the Devatās, the pāpas which occurred during the day, be it through the mind, speech, hands, feet, belly or genitals. May any sins in me committed during the day be forgiven by the abhimāni of daytime. I offer all these to You, residing in Satya, as an oblation, for the welfare of all."
        }
      }
    },
    {
      id: "09", slug: "punarmarjana", group: "Saṅkalpa & mārjana", page: "21–22",
      title: "7 · Punarmārjana",
      mantra:
        "dadhikrāvṇa ityasya vāmadeva ṛṣiḥ | viśvedevā devatāḥ | anuṣṭup chandaḥ | punarmārjane viniyogaḥ ||\n\n" +
        "dadhi krāviṇṇo ākāriṣaṃ jiṣṇoraśvasya vājinaḥ |\n" +
        "surabhi no mukhākaratpraṇa āyūꣳṣi tāriṣat ||",
      meaning:
        "May He — the Foundation, the Master and the conqueror of the universe, the repository of all knowledge in the form of a horse (Hayagrīva), and to whom I offer my salutations — free us from all hindrances to the performance of righteous deeds. (Ṛgveda, Śākala Saṃhitā, Maṇḍala 4, Sūkta 39, Mantra 6; Kṛṣṇa-Yajurveda, Taittirīya Saṃhitā, Kāṇḍa 1, Prapāṭhaka 5, Anuvāka 11, Mantra 4.)",
      action:
        "Repeat the process of mārjana — sprinkling water with the ring finger of the right hand over the head and feet, as before — but begin with this mantra."
    },

    // ===================== ARGHYA-PRADĀNA =====================
    {
      id: "10", slug: "arghya-pradana", group: "Arghya-pradāna", page: "22",
      title: "8 · Arghya-Pradāna",
      mantra:
        "[Saṅkalpa]\n" +
        "pūrvokta evaṅguṇaviśeṣaṇaviśiṣṭāyāṃ śubhatithau savitṛnāmaka sūryāntargatabhāratīramaṇamukhyaprāṇāntargata śrīlakṣmīnārāyaṇapreraṇayā śrīlakṣmīnārāyaṇaprītyarthaṃ {p} sandhyāṅga arghyapradānamahaṃ kariṣye ||\n\n" +
        "[Gāyatrī, split into five parts]\n" +
        "oṃ | bhūḥ bhuvaḥ svaḥ | tat savituḥ vareṇyaṃ | bhargo devasya dhīmahi | dhiyo yo naḥ pracodayāt ||\n" +
        "oṃ sūryāya namaḥ idam arghyam ||",
      meaning:
        "Saṅkalpa: at the auspicious time already specified, impelled by Śrī Lakṣmī-Nārāyaṇa — who abides within Savitṛ (the Sun) and within Bhāratīramaṇa Mukhyaprāṇa — and for His pleasure, I shall perform the offering of arghya as a limb of the {pe} sandhyā. Gāyatrī: We meditate upon the adorable effulgence of the Deva Savitṛ; may He impel our intellects. 'Om, salutations to Sūrya; this arghya is offered.'",
      periods: {
        pratah: {
          action:
            "Perform prāṇāyāma, śrotrācamana and brahmāñjali, and chant the saṅkalpa. Take an uddharaṇī full of water in the right palm (or hold a small cup between the thumb and index finger, keeping the thumbs away from the other fingers), chant the Gāyatrī split into the five parts shown, and pour the water on the ground — or into the arghya-pātra — through the tips of the fingers. If standing in a river or tank, offer the libations with cupped palms. Make three such offerings, making sure the water does not touch the thumbs. Face East while offering the arghyas; if the morning sandhyā has been delayed and the Sun is overhead or in the west, face North or West respectively."
        },
        madhyahnika: {
          action:
            "Perform prāṇāyāma, śrotrācamana and brahmāñjali, and chant the saṅkalpa. Take an uddharaṇī full of water in the right palm (or hold a small cup between the thumb and index finger, keeping the thumbs away from the other fingers), chant the Gāyatrī split into the five parts shown, and pour the water on the ground — or into the arghya-pātra — through the tips of the fingers. If standing in a river or tank, offer the libations with cupped palms. Make three such offerings, making sure the water does not touch the thumbs. Face North while offering the arghyas."
        },
        sayam: {
          action:
            "Perform prāṇāyāma, śrotrācamana and brahmāñjali, and chant the saṅkalpa. Take an uddharaṇī full of water in the right palm (or hold a small cup between the thumb and index finger, keeping the thumbs away from the other fingers), chant the Gāyatrī split into the five parts shown, and pour the water on the ground — or into the arghya-pātra — through the tips of the fingers. If standing in a river or tank, offer the libations with cupped palms. Make three such offerings, making sure the water does not touch the thumbs. Face West while offering the arghyas."
        }
      }
    },
    {
      id: "11", slug: "prayaschitta-arghya", group: "Arghya-pradāna", page: "22–23",
      title: "Prāyaścitta Arghya-Pradāna",
      mantra:
        "arghyatrayānte {p} sandhyākālātīta kramadoṣaparihārārthaṃ caturthārghyapradānam kariṣye |\n\n" +
        "oṃ | bhūḥ bhuvaḥ svaḥ | tat savituḥ vareṇyaṃ | bhargo devasya dhīmahi | dhiyo yo naḥ pracodayāt ||\n" +
        "oṃ sūryāya namaḥ idam arghyam ||",
      meaning:
        "This is an atonement in case one has missed the precise time period for offering arghyas — such as the Sun already having risen in the morning, or already having set in the evening. Saṅkalpa: after the three arghyas, to remove the fault of the sequence (kramadoṣa) caused by exceeding the time of the {pe} sandhyā, I shall offer a fourth arghya.",
      action:
        "Perform prāṇāyāma, śrotrācamana and brahmāñjali. Say the saṅkalpa, then chant the Gāyatrī mantra again and offer another arghya in the same manner as before. (Perform this only if the correct time was exceeded.)"
    },
    {
      id: "12", slug: "devata-tarpana", group: "Arghya-pradāna", page: "23",
      title: "Devatā Tarpaṇa",
      mantra:
        "[During Śukla-pakṣa — the first twelve names, from Keśava]\n" +
        "oṃ keśavaṃ tarpayāmi | oṃ nārāyaṇaṃ tarpayāmi | oṃ mādhavaṃ tarpayāmi | oṃ govindaṃ tarpayāmi | oṃ viṣṇuṃ tarpayāmi | oṃ madhusūdanaṃ tarpayāmi | oṃ trivikramaṃ tarpayāmi | oṃ vāmanaṃ tarpayāmi | oṃ śrīdharaṃ tarpayāmi | oṃ hṛṣīkeśaṃ tarpayāmi | oṃ padmanābhaṃ tarpayāmi | oṃ dāmodaraṃ tarpayāmi |\n\n" +
        "[During Kṛṣṇa-pakṣa — the twelve names from Saṅkarṣaṇa]\n" +
        "oṃ saṅkarṣaṇaṃ tarpayāmi | oṃ vāsudevaṃ tarpayāmi | oṃ pradyumnaṃ tarpayāmi | oṃ aniruddhaṃ tarpayāmi | oṃ puruṣottamaṃ tarpayāmi | oṃ adhokṣajaṃ tarpayāmi | oṃ nārasiṃhaṃ tarpayāmi | oṃ acyutaṃ tarpayāmi | oṃ janārdanaṃ tarpayāmi | oṃ upendraṃ tarpayāmi | oṃ hariṃ tarpayāmi | oṃ śrī kṛṣṇaṃ tarpayāmi |",
      meaning:
        "This is the final step of arghya-pradāna — the tarpaṇa ('satiating') of the Lord in His twelve forms: 'Oṃ, I satiate Keśava… I satiate Nārāyaṇa…' and so on. During Śukla-pakṣa (the waxing fortnight) recite the first twelve of the twenty-four names, starting from Keśava; during Kṛṣṇa-pakṣa (the waning fortnight) recite the twelve starting from Saṅkarṣaṇa.",
      action:
        "First perform ācamana and aṅga-nyāsa again. Then hold cupped palms, chant each of the twelve lines, and pour some water into the arghya-pātra or on the ground after mentioning each name. If necessary one may complete sandhyāvandana up to here, attend to other work, and return for the remaining steps later — though interrupting sandhyāvandana should be strictly avoided as far as possible."
    },

    // ===================== GĀYATRĪ JAPA =====================
    {
      id: "13", slug: "asana", group: "Gāyatrī japa", page: "23–24",
      title: "9 · Gāyatrī Japa — Āsana",
      mantra:
        "pṛthvīti mantrasya merupṛṣṭha ṛṣiḥ | kūrmo devatā | sutalaṃ chandaḥ | āsane viniyogaḥ ||\n\n" +
        "pṛthvi tvayā dhṛtā lokā devi tvaṃ viṣṇunā dhṛtā |\n" +
        "tvaṃ ca dhāraya māṃ devi pavitraṃ kuru cā'sanam ||\n" +
        "māṃ ca pūtaṃ kuru dhare nato'smi tvāṃ sureśvari |\n" +
        "āsane somamaṇḍale kūrmaskandhe upaviṣṭo'smi ||",
      meaning:
        "Pṛthvī, you hold the world, O Devī, and you yourself are held by Viṣṇu. For the purpose of bearing me, please purify my seat. For bearing me, I offer my salutations to you, Sureśvarī. I am seated here, with your seat being Kūrma.",
      action:
        "Perform ācamana and aṅga-nyāsa. Touch the ground, chant these mantras, and sit down. Then perform prāṇāyāma before proceeding to the Nyāsa and Dhyāna."
    },
    {
      id: "14", slug: "gayatri-nyasa", group: "Gāyatrī japa", page: "24–25",
      title: "9 · Gāyatrī Japa — Nyāsa",
      mantra:
        "[Viniyoga]\n" +
        "oṃ asya śrī gāyatri mahā mantrasya viśvamitraḥ ṛṣiḥ | nicṛd-gāyatri chandaḥ | savitā devatā | sandhya vandane jape viniyogaḥ ||\n\n" +
        "[Kara-nyāsa]\n" +
        "oṃ tatsavituḥ aṅguṣṭhābhyāṃ namaḥ | (stroke the thumbs with the index fingers)\n" +
        "oṃ vareṇyaṃ tarjanībhyāṃ namaḥ | (stroke the index fingers from palm to tip with the thumbs)\n" +
        "oṃ bhargo devasya madhyamābhyāṃ namaḥ | (stroke the middle fingers from palm to tip with the thumbs)\n" +
        "oṃ dhīmahi anāmikābhyāṃ namaḥ | (stroke the ring fingers with the thumbs)\n" +
        "oṃ dhiyo yo naḥ kaniṣṭhikābhyāṃ namaḥ | (stroke the little fingers with the thumbs)\n" +
        "oṃ pracodayāt kara-tala-kara-prṣṭhābhyāṃ namaḥ | (touch each palm and then the back of the hands)\n\n" +
        "[Aṅga-nyāsa]\n" +
        "oṃ tatsavituḥ hrdayāya namaḥ | (chest, at the heart)\n" +
        "oṃ vareṇyaṃ śirase svāhā | (top of the head)\n" +
        "oṃ bhargo devasya śikhāyai vaṣaṭ | (the śikhā, at the crown of the back of the head)\n" +
        "oṃ dhīmahi kavacāya huṃ | (cross the arms over the chest, touching the shoulders)\n" +
        "oṃ dhiyo yo naḥ netratrayāya vauṣaṭ | (touch the right and left eyes with the thumb and middle finger, placing the index finger on the centre of the forehead)\n" +
        "oṃ pracodayāt astrāya phaṭ | (clap the hands three times)\n" +
        "oṃ bhūr-bhuvas-suvar-om iti digbandhaḥ | (snap the fingers at the 8 cardinal directions around the head)",
      meaning:
        "The viniyoga declares the Ṛṣi (Viśvāmitra), Chandas (Nicṛd-Gāyatrī) and Devatā (Savitṛ) of the great Gāyatrī mantra and its application in the sandhyā-vandana japa. The kara-nyāsa installs the mantra, syllable by syllable, upon the fingers, and the aṅga-nyāsa upon the limbs, so that the reciter's hands and body are consecrated and the Devatā is invoked before the japa.",
      action:
        "Perform the kara-nyāsa and then the aṅga-nyāsa, touching each finger and each part of the body with the right hand exactly as indicated while chanting each phrase."
    },
    {
      id: "15", slug: "dhyanam", group: "Gāyatrī japa", page: "25",
      title: "9 · Gāyatrī Japa — Dhyānam",
      mantra:
        "dhyeyaḥ sadā savitṛmaṇḍalamadhyavartī nārāyaṇaḥ sarasijāsanasanniviṣṭaḥ |\n" +
        "keyūravān makarakuṇḍalavān kirīṭī hārī hiraṇmayavapuḥ dhṛtaśaṅkhacakraḥ ||\n\n" +
        "oṃ | yo devaḥ savitā'smākaṃ dhiyo dharmādi gocaraḥ |\n" +
        "prerayet tasya yadbhargaḥ tadvareṇyam upāsmahe ||",
      meaning:
        "Ever to be meditated upon is Nārāyaṇa, who dwells in the centre of the orb of the Sun, seated upon a lotus, adorned with armlets, makara ear-rings and a crown, garlanded, of golden form, bearing the śaṅkha and cakra. — The Deva Savitā, who propels our intellect towards dharma and the rest; that most adorable effulgence of His, we worship.",
      action:
        "Remembering the form of Sūrya-Nārāyaṇa (as depicted on the cover of the source book), chant the dhyāna śloka."
    },
    {
      id: "16", slug: "gayatri-japa", group: "Gāyatrī japa", page: "25",
      title: "9 · Gāyatrī Mantra Japa",
      mantra:
        "oṃ | bhūḥ bhuvaḥ svaḥ | tat savituḥ vareṇyaṃ | bhargo devasya dhīmahi | dhiyo yo naḥ pracodayāt ||\n\n" +
        "[Closing dedication]\n" +
        "anena {p} sandhyāṅgagāyatrimantrajapena gāyatrīmantrapratipādyaḥ śrībhāratīramaṇamukhyaprāṇāntargataḥ savitṛnāmaka śrīlakṣmīnārāyaṇaḥ priyatāṃ suprīto varado bhavatu | śrīkṛṣṇārpaṇamastu ||",
      meaning:
        "'We meditate upon the adorable effulgence (vareṇya bhargas) of the Deva Savitṛ; may He impel our intellects (dhiyaḥ).' Closing dedication: 'May Śrī Lakṣmī-Nārāyaṇa — who bears the name Savitṛ, who abides within Bhāratīramaṇa Mukhyaprāṇa, and who is denoted by the Gāyatrī mantra — be pleased by this japa of the Gāyatrī as a limb of the {pe} sandhyā, and, well-pleased, grant boons. May this be an offering to Śrī Kṛṣṇa.'",
      action:
        "Chant the Gāyatrī mantra at least 10 times — or 21, 28, 108 or 1,008 times — splitting it into the parts shown. At the end, perform one tarpaṇa for every 10 counts, then chant the closing dedication, and perform kara-nyāsa again followed by aṅga-nyāsa. (After this, one may perform japa of any other mantra for which one has received upadeśa from a suitable Guru.)"
    },

    // ===================== AṢṬĀKṢARA JAPA =====================
    {
      id: "17", slug: "ashtakshara-nyasa", group: "Aṣṭākṣara japa", page: "25–26",
      title: "10 · Aṣṭākṣara Japa — Saṅkalpa & Nyāsa",
      mantra:
        "[Saṅkalpa]\n" +
        "śrī bhāratīramaṇa mukhyaprāṇāntargata savitṛnāmaka śrī lakṣmīnārāyaṇa preraṇayā savitṛnāmaka śrī lakṣmīnārāyaṇa prītyarthaṃ yathāśakti nārāyaṇa aṣṭākṣaramantrajapaṃ kariṣye ||\n\n" +
        "[Nyāsa]\n" +
        "asya śrī nārāyaṇa aṣṭākṣara mahāmantrasya śrī antaryāmī ṛṣiḥ | daivī gāyatrī chandaḥ | śrī nārāyaṇo devatā | nārāyaṇa aṣṭākṣaramantrajape viniyogaḥ ||\n\n" +
        "oṃ kruddholkāya hṛdayāya namaḥ |\n" +
        "oṃ maholkāya śirase svāhā |\n" +
        "oṃ vīrolkāya śikhāyai vaṣaṭ |\n" +
        "oṃ dyūlkāya kavacāya hum |\n" +
        "oṃ sahasrolkāya astrāya phaṭ |\n" +
        "iti digbandhaḥ |",
      meaning:
        "Saṅkalpa: 'Impelled by Śrī Lakṣmī-Nārāyaṇa (named Savitṛ, abiding within Bhāratīramaṇa Mukhyaprāṇa), and for His pleasure, I shall perform japa of the Nārāyaṇa Aṣṭākṣara mantra to the best of my ability.' The Nyāsa declares the Ṛṣi (Śrī Antaryāmī), Chandas (Daivī Gāyatrī) and Devatā (Śrī Nārāyaṇa) of the eight-syllabled great mantra, and installs its aṅgas, ending with the digbandha (binding of the directions).",
      action:
        "This japa is done only if you have received upadeśa of the Aṣṭākṣara mantra. Chant the saṅkalpa, then perform the Nyāsa — touching the heart, head, śikhā and shoulders, clapping for the astra, and binding the directions."
    },
    {
      id: "18", slug: "ashtakshara-japa", group: "Aṣṭākṣara japa", page: "26–27",
      title: "10 · Aṣṭākṣara Japa — Dhyāna & Japa",
      mantra:
        "[Dhyāna]\n" +
        "udyadbhāsvatsamābhāsaścidānandaika dehavān | cakraśaṅkhagadāpadmadharo dhyeyo'hamīśvaraḥ ||\n" +
        "lakṣmīdharābhyāmāśliṣṭaḥ svamūrtigaṇamadhyagaḥ | brahmavāyuśivāhīśavipaiśśakrādikairapi ||\n" +
        "sevyamāno'dhikaṃ bhaktyā nityaniśśeṣaśaktimān | mūrtayo'ṣṭāvapi dhyeyāḥ cakraśaṅkhavarābhayaiḥ ||\n" +
        "yuktāḥ pradīpavarṇāśca sarvābharaṇabhūṣitāḥ | śaṅkhacakravarābhītihastānyetāni sarvaśaḥ | mūlarūpasavarṇāni kṛṣṇavarṇā śikhocyate ||\n\n" +
        "[Saṅkalpa]\n" +
        "mayi vaiṣṇavatva abhivṛddharthaṃ nārāyaṇāṣṭākṣara mahāmantra japatarpaṇākhyaṃ karma kariṣye |\n\n" +
        "[Closing]\n" +
        "bhagavān savitṛnāmaka śrī lakṣmī nārāyaṇapreraṇayā savitṛnāmaka śrīlakṣmīnārāyaṇa prītyarthaṃ {p} sandhyāṅga śrī nārāyaṇa aṣṭākṣaramantraṃ sampūrṇam | śrī kṛṣṇārpaṇamastu ||",
      meaning:
        "'I meditate on Īśvara, Nārāyaṇa, whose body consists of sat, chit and ānanda, and appears like the rising Sun, and who bears the śaṅkha, cakra, gadā and padma. He is the bearer of Lakṣmī Devī and is surrounded by Brahmā, Vāyu, Garuḍa, Śeṣa, Rudra and the Devatās headed by Indra. He is the Master of all energies, who is to be worshipped with intense bhakti, and who is in the centre of Viśva, Taijasa and the other eight rūpas, with a bright effulgence, adorned by all sorts of ornaments.' Saṅkalpa: 'For the purpose of increasing the Vaiṣṇavatva in me, I shall perform the task of japa and tarpaṇa of the Nārāyaṇa Aṣṭākṣara.'",
      action:
        "Chant the Mūlamantra three times the number of times you chanted the Gāyatrī (for example, if the Gāyatrī was chanted 10 times, chant the Mūlamantra 30 times). After completing the japa, perform one tarpaṇa for every 10 counts, saying 'śrī nārāyaṇaṃ tarpayāmi'. Finally, chant the closing dedication."
    },

    // ===================== UPASTHĀNA & CONCLUSION =====================
    {
      id: "19", slug: "suryopasthana", group: "Upasthāna & conclusion", page: "27–30",
      title: "11 · Sūryopasthāna",
      meaning: "The upasthāna prayer changes with the sandhyā — select the time of day above.",
      action:
        "Rise and face the direction of the Sun (East in the morning, North at midday, West in the evening) and chant the prayer shown for the present sandhyā.",
      periods: {
        pratah: {
          sanskrit: "Prātaḥ · Mitra sūkta",
          mantra:
            "mitrasya mitro janān prasamitra ityeteṣāṃ gāyatrī-triṣṭubhau viśvedevā ṛṣayaḥ | mitro devatā | sūryopasthāne viniyogaḥ ||\n\n" +
            "mitrasya carṣaṇī dhṛta śśravo devasya sānasim | satyam citra śravastamam ||\n" +
            "mitro janāna yātayati prajānan mitro dādhāra pṛthivīm uta dyām | mitraḥ kṛṣṭhīranimiṣā'bhicaṣṭe satyāya havyam dhṛtavad-vidhema ||\n" +
            "prasa mitra marto astu prayasvāna yasta āditya śikṣati vratena | na hanyate na jīyate tvoto nainamaguṃ ho aśnotyantito na dūrāt ||",
          meaning:
            "I praise the name of Sūrya, who is the One supporter of the Earth and Svarga. His name is Satya, easily attained and wonderful to hear. Sūrya, who is the friend of the universe, is omniscient and dispenses the fruits of actions to all mankind. He looks with unclosing eyes on all humans. We offer oblations to Him, for obtaining health. O Mitra and Sūrya, the cause of everything, your worshipper will be protected and will not succumb to diseases or enemies. More sins will not approach them, from far away or near."
        },
        madhyahnika: {
          sanskrit: "Mādhyāhnika · Āsatyena & Sūrya mantras",
          mantra:
            "āsatyenetasya hiraṇya ṛṣiḥ | triṣṭup chandaḥ | udvayamityasya viśvāmitra ṛṣiḥ | aniṣṭup chandaḥ | citraṃ devānāmityādeḥ kutsa ṛṣiḥ | triṣṭup chandaḥ | taccakṣuḥ ityādeḥ vasiṣṭha ṛṣiḥ | anuṣṭup chandaḥ | savitā devatā | sūryopasthāne viniyogaḥ ||\n\n" +
            "oṃ āsatyena rajasā vartamāno niveśayannamṛtaṃ martyaṃ ca | hiraṇyena savitā rathenā'devo yāti bhuvanā vi paśyan ||\n" +
            "udvayaṃ tamasaspari paśyanto jyotiruttaram | devaṃ devatrā sūryamaganma jyotiruttamam ||\n" +
            "udutyaṃ jātavedasaṃ devaṃ vahanti ketavaḥ | dṛśe viśvāya sūryam ||\n" +
            "citraṃ devānām udagādanīkaṃ cakṣurmitrasya varuṇasyāgneḥ | ā prā dyāvā pṛthivī antarikṣaꣳ sūrya ātmā jagatastastuṣaśca ||\n" +
            "taccakṣurdevahitaṃ purastācchukramuccarat || paśyema śaradaśśataṃ jīvema śaradaśśataṃ nandāma śaradaśśataṃ modāma śaradaśśataṃ bhavāma śaradaśśataṃ śṛṇvāma śaradaśśataṃ prabravāma śaradaśśataṃ ajītāsyāma śaradaśśataṃ jyok cā sūryaṃ dṛśe ||",
          meaning:
            "Sūrya, the light of the eyes, oversees all the Devas and mortals as well as all lokas, impelling them to their duties, travelling in a golden chariot. We see the effulgence of Sūrya, who rises and swallows the darkness and protects the Devas. May we attain perfect knowledge. He is the knower of all beings and is borne aloft by the seven rays which are his horses. May Sūrya, who is the eye of Mitra, Varuṇa and Agni, and the embodiment of all Devas, rise high. Sūrya, the very Ātmā of the universe, of all the motile and immotile, pervades the realms of Pṛthivī as well as outer space. Sūrya, who rises in the east, ensures the wellbeing of the gods. May we continue to see for a hundred Śarads (autumns). May we live for a hundred Śarads. May we rejoice for a hundred Śarads. May we enjoy for a hundred Śarads. May we radiate with glory for a hundred Śarads. May we listen for a hundred Śarads. May we speak properly for a hundred Śarads. May we remain undefeated for a hundred Śarads. Thus, may we continue to pursue the path to enlightenment."
        },
        sayam: {
          sanskrit: "Sāyaṃ · Varuṇa sūkta",
          mantra:
            "imaṃ me varuṇa ityasya śunaśmegha ṛṣiḥ | varuṇo devatā | gāyatrī chandaḥ | tattvāyāmi ityasya śunaśmegha ṛṣiḥ | varuṇo devatā | triṣṭup chandaḥ | yacchiddhite ityasya śunaśmegha ṛṣiḥ | varuṇo devatā | gāyatrī chandaḥ | yatkiñcedaṃ ityasya vasiṣṭha ṛṣiḥ | varuṇo devatā | jagatī chandaḥ | kitavāsa ityasya atriḥ ṛṣiḥ | varuṇo devatā | triṣṭup chandaḥ | sāyaṃ sūryopasthāne viniyogaḥ ||\n\n" +
            "imaṃ me varuṇa śrudhī havam adyāca mṛḍaya | tvām avasyurācake ||\n" +
            "tat tvā yāmi brahmaṇā vanda mānas tadā śāste yajamāno havirbhiḥ | aheḍamāno varuṇeha bodhyuruśaguṃsa mā na āyuḥ pramoṣīḥ ||\n" +
            "yacciddhi te viśo yathā pra deva varuṇa vratam | minīmasi dyavidyavi ||\n" +
            "yatkiñcedaṃ varuṇa daivye janebhidrohaṃ manuṣyāṣcaramasi | acittī yat tava dharmā yuyopimā mā nas tasmād enaso deva rīriṣaḥ ||\n" +
            "kitavāso yadri'ripurṇa dīvi yadvāghā satyam uta yanna vidma | sarvā tā viṣya śithireva devāthā te syāma varuṇa priyāsaḥ ||",
          meaning:
            "Varuṇa, listen to my prayers. Be gracious now. I am approaching you, seeking your protection. O Varuṇa, praised by the Vedas, may I take refuge in you, which I aspire, through these oblations. I am offering abundant praises to you. Abstain from your anger now and guide us. Varuṇa, who are highly renowned, answer my prayers even now and do not decrease the duration of our lives. O Varuṇa, as undiscriminating people, we may have neglected the regular daily worship, but such deceit might have been done unwittingly. O Varuṇa, protect us from, and do not punish us for, all that we have done and all the dharmas that we have violated. The blame that is attributed to me unjustly, or the sins which I have intentionally and unintentionally committed — may all these be absolved by you, Varuṇa, and may we all earn your grace."
        }
      }
    },
    {
      id: "20", slug: "samashthyabhivadana", group: "Upasthāna & conclusion", page: "30–31",
      title: "12 · Samaṣṭhyabhivādana",
      mantra:
        "oṃ indrāya namaḥ | (East)\n" +
        "oṃ agnaye namaḥ | (South-East)\n" +
        "oṃ yamāya namaḥ | (South)\n" +
        "oṃ niṛtaye namaḥ | (South-West)\n" +
        "oṃ varuṇāya namaḥ | (West)\n" +
        "oṃ vāyave namaḥ | (North-West)\n" +
        "oṃ kuberāya namaḥ | (North)\n" +
        "oṃ īśānāya namaḥ | (North-East)\n" +
        "oṃ śeṣāya namaḥ | (join the palms and point them downwards)\n" +
        "oṃ brahmaṇe namaḥ | (join the palms and point them upwards)\n\n" +
        "oṃ sarvābhyodevatābhyo namaḥ |\n" +
        "oṃ mātṛbhyo namaḥ |\n" +
        "oṃ pitṛbhyo namaḥ |\n" +
        "oṃ śrī gurubhyo namaḥ |\n\n" +
        "ākāśāt patitaṃ toyaṃ yathā gacchati sāgaram |\n" +
        "sarvadevanamaskāraḥ keśavaṃ pratigacchati ||",
      meaning:
        "Salutations to Indra (East), Agni (South-East), Yama (South), Nirṛti (South-West), Varuṇa (West), Vāyu (North-West), Kubera (North) and Īśāna (North-East); to Śeṣa (below) and to Brahmā (above). Salutations to all the Devatās; to the mothers; to the fathers; to the Gurus. 'Just as raindrops falling from the sky go to the sea, salutations offered to all the Devas go completely to Keśava.'",
      action:
        "Chant the names of the Devatās while facing the respective directions, then join the palms and point them down for Śeṣa and up for Brahmā. Recite the remaining salutations, then chant your pravara, and proceed to the concluding prayers."
    },
    {
      id: "21", slug: "concluding-prayers", group: "Upasthāna & conclusion", page: "31–32",
      title: "Concluding prayers (Sandhyā-abhirakṣā)",
      mantra:
        "yāṃ sadā sarvabhūtāni sthāvarāṇi carāṇi ca |\n" +
        "sāyaṃ prātarnamasyanti sā mā sandhyā'bhirakṣatu ||\n\n" +
        "namo'stvanantāya sahasramūrtaye sahasrapādākṣi śiroru bāhave |\n" +
        "sahasranāmne puruṣāya śāśvate sahasrakoṭiyugadhāriṇe namaḥ ||\n\n" +
        "yasya smṛtyā ca nāmoktyā tapassandhyākriyādiṣu |\n" +
        "nyūnaṃ sampūrṇatāṃ yāti sadyo vande tamacyutam ||\n\n" +
        "mantrahīnaṃ kriyāhīnaṃ bhaktihīnaṃ janārdana |\n" +
        "yatkṛtaṃ tu mayā deva paripūrṇaṃ tadastu me ||",
      meaning:
        "'May the One who is saluted by all living entities, movable and immovable, at dusk and dawn, protect us.' 'Salutations to Ananta, the One with thousands of forms, thousands of feet, eyes, heads and arms, the eternal Puruṣa with thousands of names, who is eternal and bears the thousands of crores of yugas.' 'By remembering whom, or by chanting whose name, during tapas, sandhyā and other activities, any defects are completely annihilated instantly — I propitiate Him, Acyuta.' 'Lacking proper mantras, lacking proper protocol, lacking bhakti, O Janārdana — may that which has been performed by me become complete, O Deva.' (Viṣṇu Saṃhitā, Paṭala 28, Shlokas 87–88.)",
      action:
        "Recite these four shlokas, seeking the protection of Sandhyā Devī and offering the whole rite, with its defects, to the Lord."
    },
    {
      id: "22", slug: "samarpana", group: "Upasthāna & conclusion", page: "31–32",
      title: "Samarpaṇa & conclusion",
      mantra:
        "[Pour arghya water onto the right palm, chant, then pour it out]\n" +
        "anena {p} sandhyāvandanena bhagavān śrīmanmadhvācāryāṇaṃ hṛtkamalamadhyanivāsī anantakalyāṇaguṇaparipūrṇaḥ kṣīrābdhiśāyī nirdoṣānandātmakaḥ bhāratīramaṇamukhyaprāṇāntargata savitṛnāmaka śrī lakṣmīnārāyaṇaḥ prīyatām | prīto varado bhavatu |\n\n" +
        "kāyena vācā manasendriyarvā buddhyātmanā vānusṛtasvabhāvāt |\n" +
        "karomi yadyat sakalaṃ parasmai nārāyaṇāyeti samarpayāmi ||\n\n" +
        "|| śrīkṛṣṇārpaṇamastu ||\n" +
        "oṃ acyutāya namaḥ | oṃ anantāya namaḥ | oṃ govindāya namaḥ |\n" +
        "accyutānantagovindebhyonamaḥ ||",
      meaning:
        "'Through the {pe} sandhyāvandana, may Bhagavān — who resides in the heart of Śrīmat Madhvācārya, is filled with infinite auspicious guṇas, lies down on the ocean of milk, whose Self is defectless and blissful, and who dwells as the Indweller of Bhāratī Devī's husband Mukhya Prāṇa by the name 'Savitṛ' — be pleased, and, well-pleased, grant boons to me.' 'Whatever I do through body, speech, mind, senses, intellect or Ātma, under the influence of my nature, I offer it, in its entirety, to Nārāyaṇa.' (Addendum of the Viṣṇu Sahasranāma; Bhāgavata Purāṇa, Skandha 11, Adhyāya 2, Shloka 36 — quoted by Śrī Madhvācārya in Sadācāra Smṛti, Shloka 16.) 'May this be an offering to Śrī Kṛṣṇa.'",
      action:
        "Pour some arghya water onto the right palm, chant the dedication, and then pour it on the ground or into the arghya-pātra. Recite the kāyena vācā verse and the śrī-kṛṣṇārpaṇa. Finally, perform ācamana and aṅga-nyāsa once more to conclude the sandhyāvandana."
    }

  ]
});
