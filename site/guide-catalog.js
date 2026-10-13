// Display names and archive status live here, separate from preserved source text.
// Titles use plain Roman spelling. Labels use Format (duration or count).
(function () {
  var catalog = {
    achar: {
      title: 'Deva Puja Paddhati', tabLabel: 'Detailed (56 min)',
      subtitle: 'A detailed step by step guide in the Madhva tradition'
    },
    sct: {
      title: 'Deva Puja Paddhati', tabLabel: 'Concise (35 min)',
      subtitle: 'A concise chanted guide in the Madhva tradition'
    },
    nda: {
      title: 'Deva Puja Paddhati', tabLabel: 'Sung (67 min)',
      archived: true, archivedAt: '2026-10-12'
    },
    utm: {
      title: 'Deva Puja Paddhati', tabLabel: 'Uttaradi Matha (99 steps)',
      archived: true, archivedAt: '2026-10-12'
    },
    srisukta: {
      title: 'Sri Sukta Lakshmi Puja', tabLabel: 'Puja (29 steps)',
      subtitle: 'Lakshmi puja with each offering paired to its Sri Sukta verse'
    },
    rvsandhya: {
      title: 'Rig Veda Sandhya Vandanam', tabLabel: 'Sandhya (28 steps)',
      subtitle: 'Morning sandhya with numbered steps, Roman Sanskrit, source text and English directions'
    },
    harivayustuti: {
      title: 'Hari Vayu Stuti', tabLabel: 'Stotra (43 verses)',
      subtitle: 'Vayu Stuti by Trivikrama Panditacharya, preceded by Narasimha Nakha Stuti by Madhvacharya'
    },
    'varalakshmi-complete': {
      title: 'Varada Mahalakshmi Vrata Puja', tabLabel: 'Vrata (42 steps)',
      subtitle: 'Complete worship with Roman Sanskrit and full English translations of Kannada instructions'
    },
    'deva-pooja-four-part-complete': {
      title: 'Deva Puja Paddhati', tabLabel: 'Complete (4 parts)',
      subtitle: 'Complete four part teaching with Roman Sanskrit and full English translations of Kannada instructions'
    },
    panchasukta: {
      title: 'Panchasukta', tabLabel: 'Practice (74 verses)',
      subtitle: 'Five suktas with 74 verse practice clips'
    },
    'ganapati-pooja-complete': {
      title: 'Ganapati Puja', tabLabel: 'Puja (24 steps)',
      subtitle: 'Complete Ganapati worship with Roman Sanskrit and full English translations of Kannada instructions'
    },
    'anantapadmanabha-vrata-complete': {
      title: 'Anantapadmanabha Vrata Puja', tabLabel: 'Vrata (57 min)',
      subtitle: 'Complete Anantapadmanabha vrata with Roman Sanskrit, English instructions and the vrata story'
    },
    'jyeshtha-devi-puja': {
      title: 'Jyeshtha Devi Puja', tabLabel: 'Booklet (30 practice clips)',
      subtitle: 'Roman Sanskrit, English meanings and ritual directions from the 2026 Kannada booklet'
    },
    'saraswati-puja': {
      title: 'Saraswati Puja', tabLabel: 'Complete (51 min)',
      subtitle: 'Avahana, puja and visarjana with Roman Sanskrit, English meanings, contemplation and ritual actions'
    },
    'ayudha-puja': {
      title: 'Ayudha Puja', tabLabel: 'Text (20 steps)',
      subtitle: 'Preparation and puja with Roman Sanskrit, full English explanations, line and word meanings, contemplation and actions'
    },
    'navaratri-nanda-deepa': {
      title: 'Navaratri Nanda Deepa Puja', tabLabel: 'Preparation and Puja (28 min)',
      subtitle: 'Preparation, Roman Sanskrit, line and word meanings, contemplation and ritual actions'
    }
  };
  (window.GUIDES || []).forEach(function (guide) {
    var entry = catalog[guide.key];
    if (!entry) return;
    Object.keys(entry).forEach(function (field) { guide[field] = entry[field]; });
  });
})();
