"""Build the supplied written procedure without losing any source characters."""
import copy
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if len(sys.argv) != 2:
    raise SystemExit('Usage: build_guide.py /absolute/path/to/site-repository')
REPO = Path(sys.argv[1]).resolve()
URL = 'https://www.sumadhwaseva.com/festivals/aashwayuja/ayudha-pooja/'
SOURCE = (HERE / 'source-user.txt').read_text()
assert all(ord(c) <= 0xffff for c in SOURCE), 'Offsets must be converted to UTF-16'
MANTRAS = {}
for name in ('first', 'later'):
    MANTRAS.update(json.loads((HERE / f'mantras-{name}.json').read_text()))

KCONS = dict(zip('ಕಖಗಘಙಚಛಜಝಞಟಠಡಢಣತಥದಧನಪಫಬಭಮಯರಲವಶಷಸಹಳಱ',
    'k kh g gh ṅ c ch j jh ñ ṭ ṭh ḍ ḍh ṇ t th d dh n p ph b bh m y r l v ś ṣ s h ḷ ṟ'.split()))
KVOW = dict(zip('ಅಆಇಈಉಊಋೠಎಏಐಒಓಔ', 'a ā i ī u ū ṛ ṝ e ē ai o ō au'.split()))
KMARK = dict(zip('ಾಿೀುೂೃೄೆೇೈೊೋೌ', 'ā i ī u ū ṛ ṝ e ē ai o ō au'.split()))
DCONS = dict(zip('कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळ',
    'k kh g gh ṅ c ch j jh ñ ṭ ṭh ḍ ḍh ṇ t th d dh n p ph b bh m y r l v ś ṣ s h ḷ'.split()))
DVOW = dict(zip('अआइईउऊऋॠऌएऐओऔ', 'a ā i ī u ū ṛ ṝ ḷ e ai o au'.split()))
DMARK = dict(zip('ािीुूृॄॢेैोौॆ', 'ā i ī u ū ṛ ṝ ḷ e ai o au e'.split()))
def roman(s):
    out = ''; i = 0
    while i < len(s):
        c = s[i]; nxt = s[i+1] if i+1 < len(s) else ''
        if c in KCONS or c in DCONS:
            cons, marks, virama = (KCONS,KMARK,'್') if c in KCONS else (DCONS,DMARK,'्')
            out += cons[c]
            if nxt in marks: out += marks[nxt]; i += 1
            elif nxt == virama: i += 1
            else: out += 'a'
        elif c in KVOW: out += KVOW[c]
        elif c in DVOW: out += DVOW[c]
        elif c in 'ಂं': out += 'ṃ'
        elif c in 'ಃः': out += 'ḥ'
        elif c == 'ँ': out += 'm̐'
        elif c == 'ऽ': out += '’'
        else: out += c
        i += 1
    return out

sections = []; segments = []; cursor = 0; current = None
def section(title, slug, group, contemplate, action):
    global current
    current = dict(id=f'{len(sections)+1:02}', title=title, slug=slug, group=group,
        sourceId='article', source=URL, originalScript='', structuredBlocks=[],
        contemplate=contemplate, action=action,
        guidanceAttribution='Editorial performer guidance based on this section of the supplied article.',
        enrichmentEvidence=dict(contemplate=[], action=[]))
    sections.append(current)

def block_before(marker, kind='action', english=None, key=None, role='instruction', note=None):
    global cursor
    end = SOURCE.index(marker, cursor) if marker is not None else len(SOURCE)
    assert end > cursor, (marker, cursor)
    raw = SOURCE[cursor:end]
    bi = len(current['structuredBlocks']); sid = f'article-{len(segments)+1:03}'
    evidence = dict(sourceId='article', segmentId=sid, startCharacter=cursor, endCharacter=end,
                    basis='Exact character span in the user-supplied article; offsets are UTF-16 code units.')
    b = dict(kind=kind, sourceOriginal=raw, sourceRoman=roman(raw), sourceId='article',
             evidenceReferences=[evidence])
    if kind == 'mantra':
        m = copy.deepcopy(MANTRAS[key]); b['text']=m['text']; b['gloss']=m['gloss']
        b['translationAttribution']='Editorial English translation and Sanskrit lexical analysis of the supplied mantra; displayed repairs are listed separately.'
        b['corrections']=m.get('corrections',[])
        for correction in b['corrections']:
            correction['sourceRomanReading']=roman(correction['sourceReading'])
        notes = m.get('readingNotes',[])
        if note: notes.insert(0,note)
        if notes: b['notes']=' '.join(notes)
    else:
        b['english'] = english if english is not None else raw.strip()
        b['role']=role
        b['translationAttribution']='Original English retained from the supplied article.' if english is None else 'Editorial complete English translation of the supplied Kannada/Devanagari prose.'
        if note: b['notes']=note
    assert not current['structuredBlocks'] or not (current['structuredBlocks'][-1]['kind']==kind=='mantra'), 'Merge adjacent recitation spans'
    current['structuredBlocks'].append(b); current['originalScript'] += raw
    segments.append(dict(id=sid, sourceId='article', startCharacter=cursor, endCharacter=end,
                         sourceOriginal=raw, sectionId=current['id'], blockIndex=bi))
    current['enrichmentEvidence']['contemplate'].append(dict(evidence, interpretation='Source-based editorial contemplation.'))
    current['enrichmentEvidence']['action'].append(dict(evidence, interpretation='Source-based editorial action guidance.'))
    cursor=end

G='Occasion and Preparation'
section('Mahanavami and Ayudha Puja', 'occasion', G,
    'Remember the divine while preparing to worship the implements used in daily life. The article places this observance within the nine days of Dasara.',
    'Read the occasion and scope of the observance. The article specifies Ashwayuja shukla Navami; it does not supply a date for this year.')
block_before('What is Ayudha Pooja?', english='Ayudha puja\nHome › Festivals › Aashwayuja Maasa › Ayudha puja\nWhen is Mahanavami or Ayudha puja celebrated?\n\nAyudha puja is observed on the shukla (bright-fortnight) Navami tithi of Ashwayuja. That day is called Mahanavami.\n\nAyudha puja, or Astra puja, is part of the Dasara festival. On this day, all kinds of implements, weapons and machines that we use should be worshipped.\n\n'+SOURCE[SOURCE.index('“Ayudha Pooja”'):SOURCE.index('What is Ayudha Pooja?')].strip(), role='explanation', note='The final paragraph is the article’s original English. Its statement about merit is the source’s religious teaching.')
section('Meaning of implement worship', 'meaning-of-implement-worship', G,
    'Cultivate gratitude to God for the tools that support your duties, and pray that their use brings benefit without harm.',
    'Read the explanation before choosing the implements for puja. The source describes daily prostration as a custom and includes knives, scissors, stoves, machinery, computers and vehicles.')
block_before('1. This Ayudha', role='explanation')
section('Arjuna and the Shami tree', 'arjuna-and-shami', G,
    'Consider the article’s account of Arjuna recovering his hidden weapons and its association of Vijayadashami with beginning or renewing learning and work.',
    'Read this background account. It gives no additional ritual act for the Ayudha Puja sequence.')
block_before('2. According', role='explanation')
section('Chamundeshwari and her weapons', 'chamundeshwari', G,
    'Reflect on the article’s account of the weapons being set aside and worshipped after Chamundeshwari’s victory.',
    'Read this second background account. The article does not prescribe an additional mantra or physical act here.')
block_before('3.  In ancient', role='explanation')
section('Royal and workshop customs', 'royal-and-workshop-customs', G,
    'Approach the implements of your vocation with the devotion described in the article.',
    'Identify the implements used in your work. This paragraph describes historical and present-day customs; the next step gives preparation instructions.')
block_before('4.  The tools', role='explanation')
section('Prepare the implements and worship space', 'prepare-implements', G,
    'Use the article’s anusandhana: Parvati, Shiva, Saraswati, Bharati and Mukhya Prana are remembered with Sri Lakshmi Narayana as the indwelling Lord. The article’s compressed wording is retained below.',
    'Clean and decorate the implements; arrange them on a clean platform on the preceding evening. On Mahanavami morning, worship the implements alongside the deity images. Place books and musical instruments on the pedestal for worship, and leave them undisturbed that day.',)
block_before('ಪರಮಾತ್ಮನ', role='instruction', note='This is the source’s original English, including its compressed “antargatha” wording. It is not expanded into an additional sankalpa formula. Apply washing and decorative paste appropriately to the material of each implement; the article gives no device-specific method.')
section('The Lord’s weapons and their presiding deities', 'divine-weapons', G,
    'Remember the presiding deities named for the chakra, conch, mace and lotus while directing worship to the Lord and the deities indwelling his weapons.',
    'Read the explanation of daily worship and the four salutations. The article also names the knife, sword, armour and bow, but does not print a separate salutation for each of them.')
block_before('ಚಕ್ರಾಭಿಮಾನಿನ್ಯೈ', english='In our daily puja we worship the Supreme Lord’s weapons and emblems: the chakra, conch, mace, lotus, knife, sword, armour and bow.')
block_before(' ಈ ರೀತಿ', kind='mantra', key='divine_weapons')
block_before('ಸಾಮಾನ್ಯವಾಗಿ', english='In this way, worship the Lord’s weapons and the deities indwelling them.')
section('Include everyday household tools', 'household-tools', G,
    'Remember that the observance extends to implements used every day, beyond the vehicle alone.',
    'Include everyday tools such as the knife, scissors and the fixed cutting blade named in the article, as applicable to your household.')
block_before('ಸಂಕ್ಷಿಪ್ತ', english='Usually people think Ayudha Puja means vehicle puja, and clean and worship their vehicle. But the many implements we use every day, such as knives, scissors and the iḷige maṇi (a fixed household cutting blade), should also be worshipped.')
G='Ayudha Puja Procedure'
section('Begin with the usual preliminaries', 'preliminaries', G,
    'Prepare to make the intention of worship in the actual place and time of performance.',
    'Perform achamana and pranayama according to your established puja paddhati, then state the place and time for the sankalpa. The article names these preliminaries but does not give their complete mantras or motions.')
block_before('ಏವಂಗುಣ', english='Brief Ayudha Puja procedure:\n\nAchamana, pranayama and sankalpa … State the place and time.', note='The ellipsis belongs to the source. No missing preliminary formula has been supplied by this guide.')
section('Sankalpa for protection and welfare', 'sankalpa', G,
    'Intend the welfare, steadiness, health and auspiciousness of your family, and freedom from accidents, weapon injuries and obstacles, as stated in the sankalpa. Remember Sri Durga together with Sri Lakshmi Narayana within Garuda, the presiding deity of the vehicle.',
    'After the place and time portion, recite the published intention below. The vehicle-specific wording is retained; it has not been changed into an invented tool-specific formula.')
block_before('ಆದೌ', kind='mantra', key='sankalpa')
section('Ganapati intention and invocation', 'ganapati-invocation', G,
    'Remember Ganapati in the image or areca nut specified by the article and pray for the removal of obstacles at the beginning of the worship.',
    'Use a Ganapati image or an areca nut in a small vessel. Recite the intention, invocation, welcome and seat offerings, placing mantra akshata while saying these mantras.')
block_before('     ಗಣಪತಿಯ', kind='mantra', key='ganapati_intent')
block_before('   ಶ್ರೀ ಮಹಾಗಣಪತಿಯೇ', english='Contemplate Ganapati in either a Ganapati image or an areca nut placed in a small vessel.')
block_before('   (ಈ ಎಲ್ಲಾ', kind='mantra', key='ganapati_invocation')
block_before('ಪಾದಯೋ:', english='(While saying all these mantras, place mantra akshata.)')
section('Ganapati water offerings', 'ganapati-water', G,
    'Offer the hospitality named in each line: water for the feet, arghya, achamana, madhuparka, another achamana and bathing.',
    'Recite the offerings in their printed order and put the water into the arghya vessel, as the article directs. It does not specify quantities.')
block_before('  (ನೀರನ್ನು', kind='mantra', key='ganapati_water')
block_before('ವಸ್ತ್ರಂ', english='(Put the water into the arghya vessel.)')
section('Ganapati clothing, flowers, incense and lamp', 'ganapati-offerings', G,
    'Offer the clothing, sacred thread, ornament, fragrance and flowers with devotion, followed by incense and the lamp.',
    'Recite the seven printed offerings and present the corresponding items. The article gives no substitute method when an item is unavailable.')
block_before('ನಂತರ ಯಾವುದಾದರೂ', kind='mantra', key='ganapati_offerings')
section('Ganapati fruit offering and prayer', 'ganapati-prayer', G,
    'Ask Ganapati, described here as shining like the rising sun, to remove obstacles from all your undertakings at all times.',
    'Offer any fruit as naivedya, then recite the prayer. Retain the source’s bālasūrya wording.')
block_before('ವಕ್ರತುಂಡ', english='Next, offer any fruit as naivedya.\n\nThen pray:')
block_before('ಶುದ್ಧೀಕರಣ', kind='mantra', key='ganapati_prayer')
section('Purification with water', 'water-purification', G,
    'Contemplate the waters praised as bearers of well-being, nourishment and their most beneficent essence, nurturing like mothers.',
    'Recite the water hymn and sprinkle the vehicle or implement with water from the conch, as directed in the article.')
block_before('ಓಂ ಆಪೋ', english='Purification:')
block_before('ಶಂಖೋದಕದಿಂದ', kind='mantra', key='apo_histha')
block_before('ಆವಾಹನ', english='Sprinkle the vehicle or implement with conch water.')
section('Narayana japa and remembrance of presiding deities', 'narayana-and-presiding-deities', G,
    'Remember Narayana while touching the implement, and contemplate the presiding deities of the tattvas and the matrika forms named by the article. The “tattvanāsikā” deity-class reading is uncertain and is marked below.',
    'Touch the vehicle or implement and repeat the printed Narayana formula twelve times. Then use the listed salutations and contemplate the deity groups; consult your paddhati teacher for the damaged tattvanāsikā reading.')
block_before('ಓಂ ನಮೋ', english='Invocation:')
block_before(' ಎಂದು ದ್ವಾದಶ', kind='mantra', key='narayana_touch')
block_before('ಸರ್ವೇಭ್ಯೋ', english='Repeat this twelve times while touching the vehicle or implement.')
block_before(' ಎಂದು ತತ್ವಾಭಿಮಾನಿ', kind='mantra', key='deity_salutations')
block_before('ಆಯುಧ ಪ್ರಾರ್ಥನ', english='Thus contemplate the presiding deities of the tattvas, the deities, and the matrika forms.', note='The isolated dot printed before the next heading is retained in the original source details.')
section('Ayudha and Kalasha prayers', 'ayudha-and-kalasha-prayers', G,
    'In the Ayudha prayer, attend to the dagger specifically addressed as churikā, asking for protection and peace. In the Kalasha prayer, contemplate the vessel born at the churning of the ocean and request support for the worship.',
    'Read the Ayudha prayer in its stated context. Use the water from the kalasha already employed in deity puja, or worship a new kalasha as the article permits. The second printed set below is a parallel-script reference, not a prescribed second recitation.')
block_before('ಸರ್ವಾಯುಧಾನಾಂ', english='Ayudha prayer:', note='This prayer addresses a dagger (churikā). The guide does not change its addressee to a computer, vehicle or every tool.')
block_before('(ದೇವರಪೂಜೆ', kind='mantra', key='ayudha_prayer')
block_before('ದೇವದಾನವಸಂವಾದೇ', english='(You may use the same kalasha water that was used during deity puja, or you may worship a new kalasha.)\n\nKalasha prayer:')
block_before('आयुध प्रार्थन', kind='mantra', key='kalasha_prayer')
block_before('सर्वायुधानां', english='Ayudha prayer (the article prints the same prayer again in Devanagari):', note='Parallel-script source copy. This is preserved for completeness and does not instruct a second performance.', role='explanation')
block_before('कलश प्रार्थन', kind='mantra', key='ayudha_prayer', note='Parallel Devanagari copy of the Ayudha prayer above; the same reviewed display readings are used.')
block_before('देवदानवसंवादे', english='Kalasha prayer (parallel Devanagari copy):', role='explanation')
block_before('ಷೋಡಚೋಪಚಾರ', kind='mantra', key='kalasha_prayer', note='Parallel Devanagari copy of the Kalasha prayer above; the same reviewed display readings are used.')
section('The abbreviated upachara list', 'upachara-list', G,
    'Offer the services of worship with devotion, following the meditation, invocation and hospitality named in the article.',
    'Follow the printed offering list in order using your established puja method. The article gives an abbreviated list ending in samarpayāmi, rather than a full separate formula and physical method for every offering.')
block_before('ಧ್ಯಾನ,', english='Shodashopachara puja (worship with sixteen services):', note='The heading calls this sixteen services, while the printed list contains seventeen named items. All are retained in source order.')
block_before('ನಂತರ ಹಣ್ಣು ಕಾಯಿ', kind='mantra', key='upacara_list')
section('Naivedya and directional bali', 'naivedya-and-bali', G,
    'Complete the food offering and the directional offering described by the article with the intention of auspiciousness and protection stated in the sankalpa.',
    'Offer fruit and coconut as naivedya. Apply kumkuma water to an ash gourd or lemon and give bali in all directions, following your established household method; the article does not specify a cutting method, portions or a directional mantra.')
block_before('ಯಸ್ಯ ಸ್ಮೃತ್ಯಾ', english='Next, offer fruit and coconut as naivedya. Then apply kumkuma water to an ash gourd or a lemon and give bali in all directions.')
section('Completion and dedication to Krishna', 'completion-and-dedication', G,
    'Remember Achyuta as the one whose remembrance and name complete what is deficient. Ask Ramapati to make the worship complete despite shortcomings in mantra, action and devotion. Dedicate it through your guru and Bharati Ramana Mukhya Prana to Sri Lakshmi Narayana together with Sri Durga.',
    'Recite the completion prayers and closing dedication. The published closing says vāhanapūjā, vehicle worship; this wording and the final kṛṣṇārpaṇam astu are retained.')
# Completion and dedication form one uninterrupted Sanskrit run.
combined = copy.deepcopy(MANTRAS['completion'])
combined['text'] += '\n\n'+MANTRAS['samarpana']['text']
combined['gloss']['lines'] += [None]+copy.deepcopy(MANTRAS['samarpana']['gloss']['lines'])
combined['readingNotes'] += MANTRAS['samarpana']['readingNotes']
combined['corrections'] += MANTRAS['samarpana']['corrections']
MANTRAS['closing_run']=combined
block_before(None, kind='mantra', key='closing_run')

sections[0]['html']='<div class="source-link"><a href="ayudha-puja-source.txt">Read the complete supplied article text</a></div>'
sections[14]['html']='<div class="source-link"><a href="https://lrc.la.utexas.edu/books/rigveda/RV10" target="_blank" rel="noopener">Purification hymn reading reference: Rigveda 10.9.1–3</a></div>'
sections[16]['html']='<div class="source-link"><a href="https://vishvasa.github.io/kalpAntaram/dharmaH/nibandhaH/shUdra-dharmaH/shUdra-kamalAkaraH/mUlam/" target="_blank" rel="noopener">Dagger prayer reading reference: Shudrakamalakara</a> · <a href="https://sa.wikisource.org/wiki/पृष्ठम्:संस्काररत्नमाला_(भागः_१).djvu/१५५" target="_blank" rel="noopener">Kalasha prayer reading reference: Samskararatnamala, printed p. 151</a></div>'

assert len(sections)==20 and cursor==len(SOURCE)
assert ''.join(s['originalScript'] for s in sections)==SOURCE
remaining={c for s in sections for b in s['structuredBlocks'] for c in b['sourceRoman'] if (0x0c80 <= ord(c) <= 0x0cff or 0x0900 <= ord(c) <= 0x097f) and c not in '।॥'}
assert not remaining, f'Unromanized source characters: {remaining}'
guide = dict(key='ayudha-puja', title='Ayudha Puja', tabLabel='Text (20 steps)',
    noAudio=True, renderStructured=True, hideLosslessReferences=True, hideSourceWatchLinks=True,
    structuredSourceLabel='Printed source · Roman text', structuredOriginalLabel='Printed source · Original script', showDisplayCorrections=True,
    source=URL, sourceLabel='Sumadhwa Seva', sourceCredit='Sumadhwa Seva, Ayudha pooja; complete article text supplied by the user',
    subtitle='Preparation and puja with Roman Sanskrit, full English explanations, line and word meanings, contemplation and actions',
    notice='Text guide from the complete supplied article. Printed parallel-script prayers are retained as reference copies. Reading notes identify display corrections and one uncertain deity-class reading. Achamana, pranayama and some offering methods are only named in the source; follow your established paddhati for those details.',
    sources=[dict(id='article', kind='text',url=URL,role='Complete written Ayudha Puja procedure',
        sourceSha256=hashlib.sha256(SOURCE.encode()).hexdigest(), characterCount=len(SOURCE),
        acquisition='User-supplied article text',download='ayudha-puja-source.txt')],
    readingReferences=[
        dict(title='Rigveda 10.9.1–3', url='https://lrc.la.utexas.edu/books/rigveda/RV10', use='Purification hymn reading; no Vedic accent marks added.'),
        dict(title='Shudrakamalakara, weapon-worship prayer',url='https://vishvasa.github.io/kalpAntaram/dharmaH/nibandhaH/shUdra-dharmaH/shUdra-kamalAkaraH/mUlam/',use='Dagger-prayer damaged readings; only the lines selected by the supplied article are used.'),
        dict(title='Samskararatnamala, part 1, printed p. 151',url='https://sa.wikisource.org/wiki/पृष्ठम्:संस्काररत्नमाला_(भागः_१).djvu/१५५',use='Kalasha-prayer damaged readings; additional stanzas are not imported.')],
    sections=sections)
manifest=dict(sources=[dict(id='article',kind='text',url=URL,originalScript=SOURCE)],segments=segments)
write=lambda p,obj:p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
write(HERE/'guide.json',guide); write(HERE/'evidence-manifest.json',manifest)
(REPO/'site/data18.js').write_text('// Complete user-supplied written procedure; source characters and editorial repairs are separate.\n(window.GUIDES = window.GUIDES || []).push('+json.dumps(guide,ensure_ascii=False,indent=2)+');\n')
(REPO/'site/ayudha-puja-source.txt').write_text(SOURCE)
print(json.dumps(dict(sections=len(sections),blocks=len(segments),sourceCharacters=len(SOURCE),
    mantraLines=sum(len(b['gloss']['lines'])-b['gloss']['lines'].count(None) for s in sections for b in s['structuredBlocks'] if b['kind']=='mantra')),indent=2))
