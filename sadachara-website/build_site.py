#!/usr/bin/env python3
"""Build a self-contained index.html for the Sadāchāra shloka collection.
Parses shlokas/*.md (frontmatter + the 4 sections) and embeds everything as JSON
in a single static HTML file. No server needed — open index.html in a browser.
Audio plays from the sibling audio/ directory when a wav exists.
"""
import os, re, json, glob, html

ROOT = os.path.dirname(os.path.abspath(__file__))
SH = os.path.join(ROOT, 'shlokas')
AUDIO = os.path.join(ROOT, 'audio')

def section(body, name):
    m = re.search(r'## ' + re.escape(name) + r'\n\n(.*?)(?:\n\n##|\Z)', body, re.S)
    if not m: return ''
    return m.group(1).strip()

def block_lines(text):
    """Lines of a '> ' quoted block -> list of strings."""
    out = []
    for ln in text.splitlines():
        ln = ln.strip()
        if ln.startswith('>'):
            out.append(ln[1:].strip())
    return out

def parse(path):
    txt = open(path, encoding='utf-8').read()
    fm = re.match(r'^---\n(.*?)\n---\n(.*)$', txt, re.S)
    head, body = fm.group(1), fm.group(2)
    meta = {}
    for line in head.splitlines():
        m = re.match(r'^(\w+):\s*(.*?)\s*$', line)
        if m:
            meta[m.group(1)] = re.sub(r'\s*#.*$', '', m.group(2)).strip()
    rid = int(meta['id'])
    slug = meta['slug']
    wav = f'audio/{rid:03d}-{slug}.wav'
    has_audio = os.path.exists(os.path.join(ROOT, wav))
    return {
        'id': rid,
        'slug': slug,
        'title': meta.get('title', slug),
        'chapter': meta.get('chapter', ''),
        'book_page': meta.get('book_page', ''),
        'meter': meta.get('meter', ''),
        'tts_skip': str(meta.get('tts_skip', '')).lower() == 'true',
        'tts_note': meta.get('tts_note', ''),
        'devanagari': block_lines(section(body, 'Sanskrit (Devanagari)')),
        'iast': block_lines(section(body, 'Transliteration (IAST)')),
        'meaning': section(body, 'English meaning'),
        'action': section(body, 'Action while reciting'),
        'audio': wav if has_audio else None,
    }

data = [parse(f) for f in sorted(glob.glob(os.path.join(SH, '*.md')))]
data.sort(key=lambda d: d['id'])
n_audio = sum(1 for d in data if d['audio'])

# Top-level categories, grouping the book's ~22 granular chapters into a navigable set.
# Each entry's "majors" list matches the chapter text before its first em-dash.
CATEGORIES = [
    ('morning',  'Morning Rituals',      ['Prātaḥsnānātpūrvakarma', 'Snāna vidhiḥ', 'Vastradhāraṇavidhiḥ',
                                           'Gopīcandanadhāraṇam', 'Pañcamudrādhāraṇam']),
    ('sandhya',  'Sandhyāvandanam',      ['Sandhyāvandanam']),
    ('japa',     'Daily Japa & Duties',  ['Daily japa', 'Daily duties', 'Pañcayajña', 'Pitṛyajña']),
    ('puja',     'Deity Pūjā',           ['Lakṣmī pūjā', 'Pūjā prārthanā', 'Pūjā', 'Guru vandana',
                                           'Pūjā samāpana', 'Namaskāra']),
    ('sukta',    'Vedic Sūktas',         ['Vedic sūktas', 'Daily / Lakṣmī pūjā']),
    ('festival', 'Festivals',            ['Festivals']),
    ('close',    'Meals & Rest',         ['Bhojana', 'Śayana', 'Ekādaśī']),
]
_major_to_cat = {major: cid for cid, _label, majors in CATEGORIES for major in majors}
for d in data:
    major = d['chapter'].split('—')[0].strip() or d['chapter']
    d['cat'] = _major_to_cat.get(major, 'other')
_uncategorized = [d['id'] for d in data if d['cat'] == 'other']
assert not _uncategorized, f"Uncategorized shlokas (add their chapter major to CATEGORIES): {_uncategorized}"

DATA_JSON = json.dumps(data, ensure_ascii=False)
CATEGORIES_JSON = json.dumps([{'id': cid, 'label': label} for cid, label, _majors in CATEGORIES], ensure_ascii=False)

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sadāchāra Saṅgrahaḥ — Shlokas</title>
<style>
  :root {
    --bg:#fbf6ec; --card:#fffdf8; --ink:#2c2418; --muted:#8a7a5c;
    --accent:#9a3412; --accent2:#b45309; --line:#e7dcc6; --dev:#7c2d12;
  }
  * { box-sizing:border-box; }
  body { margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
         background:var(--bg); color:var(--ink); line-height:1.55; }
  header { position:sticky; top:0; z-index:10; background:linear-gradient(180deg,#fbf6ec,#fbf6ecf2);
           backdrop-filter:blur(6px); border-bottom:1px solid var(--line); padding:14px 20px; }
  .wrap { max-width:860px; margin:0 auto; }
  .home { display:inline-block; margin-bottom:8px; font-size:.78rem; color:var(--muted);
          text-decoration:none; border:1px solid var(--line); border-radius:20px; padding:2px 11px; background:#fff; }
  .home:hover { color:var(--accent); border-color:var(--accent); }
  h1 { margin:0; font-size:1.35rem; color:var(--accent); letter-spacing:.2px; }
  .sub { color:var(--muted); font-size:.85rem; margin-top:2px; }
  .catbar { display:flex; gap:6px; overflow-x:auto; padding:2px 0 10px; margin:0 0 2px;
            -webkit-overflow-scrolling:touch; scrollbar-width:thin; }
  .catbar::-webkit-scrollbar { height:5px; }
  .cattab { flex:0 0 auto; font-size:.84rem; font-weight:600; padding:7px 14px; border-radius:9px;
            border:1px solid var(--line); background:#fff; color:var(--ink); cursor:pointer;
            white-space:nowrap; text-decoration:none; }
  .cattab .n { color:var(--muted); font-weight:500; font-size:.78em; }
  .cattab.active { background:var(--accent); border-color:var(--accent); color:#fff; }
  .cattab.active .n { color:#fbf6ec; }
  .controls { display:flex; gap:8px; margin-top:10px; }
  #q { flex:1; padding:9px 12px; font-size:1rem; border:1px solid var(--line);
       border-radius:9px; background:#fff; }
  #jump { max-width:42%; padding:9px 10px; font-size:.9rem; border:1px solid var(--line);
          border-radius:9px; background:#fff; color:var(--ink); }
  @media (max-width:560px){ .controls{flex-direction:column;} #jump{max-width:100%;} }
  main { padding:18px 20px 80px; }
  .chapter { color:var(--accent2); font-size:.78rem; text-transform:uppercase; letter-spacing:.8px;
             margin:26px 0 8px; padding-bottom:4px; border-bottom:1px solid var(--line); font-weight:600; }
  .card { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:16px 18px;
          margin:10px 0; box-shadow:0 1px 2px #00000008; }
  .card-head { display:flex; align-items:baseline; gap:8px; flex-wrap:wrap; }
  .num { color:var(--muted); font-variant-numeric:tabular-nums; font-size:.82rem; }
  .title { font-weight:650; font-size:1.05rem; }
  .badge { font-size:.68rem; color:var(--muted); border:1px solid var(--line); border-radius:20px;
           padding:1px 8px; background:#fff; }
  .dev { font-size:1.28rem; color:var(--dev); margin:12px 0 6px; line-height:1.85;
         font-family:"Noto Serif Devanagari","Kohinoor Devanagari",serif; }
  .iast { font-style:italic; color:#6b5d44; font-size:.95rem; margin:0 0 10px; }
  .label { font-size:.7rem; text-transform:uppercase; letter-spacing:.6px; color:var(--accent2);
           font-weight:600; margin:10px 0 2px; }
  .meaning { font-size:.96rem; }
  .action { font-size:.9rem; color:#5c5038; }
  audio { width:100%; margin-top:12px; height:34px; }
  .noaudio { margin-top:10px; font-size:.78rem; color:var(--muted); font-style:italic; }
  .hidden { display:none; }
  footer { text-align:center; color:var(--muted); font-size:.78rem; padding:30px 20px; }
  mark { background:#fde68a; color:inherit; padding:0 1px; border-radius:2px; }
  .chips { display:flex; gap:6px; margin-top:9px; flex-wrap:wrap; }
  .chip { font-size:.78rem; padding:4px 11px; border:1px solid var(--line); border-radius:20px;
          background:#fff; color:var(--muted); cursor:pointer; user-select:none; }
  .chip.active { background:var(--accent); color:#fff; border-color:var(--accent); }
  .pill { font-size:.66rem; padding:1px 8px; border-radius:20px; font-weight:600; white-space:nowrap; }
  .pill.audio { background:#dcfce7; color:#166534; }
  .pill.render { background:#fef3c7; color:#92400e; }
  .pill.external { background:#e5e7eb; color:#4b5563; }
  @media print {
    @page { margin:14mm; }
    body { background:#fff; color:#000; font-size:11pt; }
    header, footer, .controls, .chips, .catbar, .pill, audio, .noaudio, .home { display:none !important; }
    header { position:static; }
    main { padding:0; max-width:100%; }
    .chapter { color:#000; border-bottom:1.5px solid #000; margin:14pt 0 6pt;
               break-after:avoid; page-break-after:avoid; }
    .card { border:none; box-shadow:none; padding:6pt 0; margin:0 0 8pt;
            break-inside:avoid; page-break-inside:avoid; border-bottom:1px solid #ddd; }
    .num, .badge { color:#555; }
    .dev { color:#000; font-size:15pt; line-height:1.7; }
    .iast { color:#333; }
    .label { color:#000; }
    .title { font-size:12pt; }
  }
</style>
</head>
<body>
<header><div class="wrap">
  <a class="home" href="../index.html">&larr; All guides</a>
  <h1>Sadāchāra Saṅgrahaḥ &middot; Shlokas</h1>
  <nav class="catbar" id="catbar"></nav>
  <div class="sub" id="stat"></div>
  <div class="controls">
    <input id="q" type="search" placeholder="Search title, Sanskrit, meaning, chapter…" autocomplete="off">
    <select id="jump" title="Jump to section"><option value="">Jump to section…</option></select>
  </div>
  <div class="chips" id="chips">
    <span class="chip active" data-st="all">All</span>
    <span class="chip" data-st="audio">♪ Has audio</span>
    <span class="chip" data-st="render">⏳ To render</span>
    <span class="chip" data-st="external">External / text-only</span>
    <span class="chip" id="printBtn" title="Print the shlokas currently shown" style="margin-left:auto">⎙ Print</span>
  </div>
</div></header>
<main class="wrap" id="list"></main>
<footer>Vidwan T. P. Vishnumurthy Acharya &middot; Raghavendra Trust, Udupi (2010) &middot; generated from source markdown</footer>
<script>
const DATA = __DATA__;
const CATEGORIES = __CATEGORIES__;
const list = document.getElementById('list');
const stat = document.getElementById('stat');
const q = document.getElementById('q');
const jump = document.getElementById('jump');
const catbar = document.getElementById('catbar');
const BASE_TITLE = document.title;

// category bar: "All" + each category, each a real link (#cat=id) so it's a shareable,
// back-button-friendly URL that shows only that category's cards.
function catCount(id){ return DATA.filter(d => id ? d.cat===id : true).length; }
function hashCat(){ const m = location.hash.match(/cat=([a-z]+)/); return m ? m[1] : null; }
let catFilter = hashCat();

function renderCatbar(){
  catbar.innerHTML = '';
  const tabs = [{id:null, label:'All'}, ...CATEGORIES];
  for (const t of tabs){
    const a = document.createElement('a');
    a.className = 'cattab' + (catFilter===t.id ? ' active' : '');
    a.href = t.id ? ('#cat='+t.id) : '#';
    a.innerHTML = esc(t.label) + ' <span class="n">' + catCount(t.id) + '</span>';
    catbar.appendChild(a);
  }
}
function applyCatTitle(){
  const label = CATEGORIES.find(c=>c.id===catFilter)?.label;
  document.title = label ? (label + ' — ' + BASE_TITLE) : BASE_TITLE;
}
window.addEventListener('hashchange', ()=>{
  catFilter = hashCat();
  applyCatTitle();
  window.scrollTo(0,0);
  renderCatbar();
  render(q.value);
});

// stable chapter -> anchor-id map, in book order
const chapters = [];
const chapterId = {};
for (const d of DATA){ if (!(d.chapter in chapterId)){ chapterId[d.chapter] = 'ch-' + chapters.length; chapters.push(d.chapter); } }
// group dropdown options by major section (text before the first em-dash)
let curGroup = null, groupEl = null;
for (const ch of chapters){
  const major = ch.split('—')[0].trim() || ch;
  if (major !== curGroup){ groupEl = document.createElement('optgroup'); groupEl.label = major; jump.appendChild(groupEl); curGroup = major; }
  const sub = ch.includes('—') ? ch.split('—').slice(1).join('—').trim() : ch;
  const o = document.createElement('option'); o.value = chapterId[ch]; o.textContent = sub || ch; groupEl.appendChild(o);
}

function statusOf(d){ return d.audio ? 'audio' : (d.tts_skip ? 'external' : 'render'); }
const PILL = {audio:'♪ audio', render:'⏳ to render', external:'external'};
let stFilter = 'all';
function esc(s){ return (s||'').replace(/[&<>]/g, c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c])); }
function fmt(s){
  // lightweight markdown for meaning/action: strip leading blockquote, **bold**, *italic*
  s = (s||'').replace(/^\s*>\s?/gm, '');
  s = esc(s);
  s = s.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  s = s.replace(/\*([^*]+)\*/g, '<em>$1</em>');
  s = s.replace(/\n+/g, '<br>');
  return s;
}

function render(filter){
  filter = (filter||'').trim().toLowerCase();
  list.innerHTML = '';
  let shown = 0, lastChap = null;
  for (const d of DATA){
    if (catFilter && d.cat !== catFilter) continue;
    const st = statusOf(d);
    if (stFilter !== 'all' && st !== stFilter) continue;
    const hay = (d.title+' '+d.chapter+' '+d.meaning+' '+d.action+' '+d.devanagari.join(' ')+' '+d.iast.join(' ')).toLowerCase();
    if (filter && !hay.includes(filter)) continue;
    shown++;
    if (d.chapter !== lastChap){
      const h = document.createElement('div'); h.className='chapter'; h.id=chapterId[d.chapter]; h.textContent=d.chapter; list.appendChild(h); lastChap=d.chapter;
    }
    const c = document.createElement('div'); c.className='card';
    let audioHtml;
    if (d.audio) audioHtml = `<audio controls preload="none" src="${d.audio}"></audio>`;
    else if (d.tts_skip) audioHtml = `<div class="noaudio">${esc(d.tts_note || 'Vedic sūkta — audio sourced separately (model does not render svara).')}</div>`;
    else audioHtml = `<div class="noaudio">Audio not yet rendered.</div>`;
    c.innerHTML =
      `<div class="card-head"><span class="num">#${String(d.id).padStart(3,'0')}</span>`+
      `<span class="title">${esc(d.title)}</span>`+
      `<span class="pill ${st}">${PILL[st]}</span>`+
      (d.meter?`<span class="badge">${esc(d.meter)}</span>`:'')+
      (d.book_page?`<span class="badge">p${esc(d.book_page)}</span>`:'')+`</div>`+
      `<div class="dev">${d.devanagari.map(esc).join('<br>')}</div>`+
      `<div class="iast">${d.iast.map(esc).join('<br>')}</div>`+
      `<div class="label">Meaning</div><div class="meaning">${fmt(d.meaning)}</div>`+
      (d.action?`<div class="label">While reciting</div><div class="action">${fmt(d.action)}</div>`:'')+
      audioHtml;
    list.appendChild(c);
  }
  const scope = catFilter ? DATA.filter(d=>d.cat===catFilter) : DATA;
  const nA = scope.filter(d=>statusOf(d)==='audio').length;
  const nR = scope.filter(d=>statusOf(d)==='render').length;
  const nE = scope.filter(d=>statusOf(d)==='external').length;
  const catLabel = CATEGORIES.find(c=>c.id===catFilter)?.label;
  stat.textContent = (catLabel ? `${catLabel} — ` : '') +
    `${scope.length} shlokas · ${nA} with audio · ${nR} to render · ${nE} external/text-only`
    + (filter||stFilter!=='all' ? `  —  showing ${shown}` : '');
}
q.addEventListener('input', e=>render(e.target.value));
document.getElementById('printBtn').addEventListener('click', ()=>window.print());
document.getElementById('chips').addEventListener('click', e=>{
  const chip = e.target.closest('.chip'); if(!chip || chip.id==='printBtn') return;
  stFilter = chip.dataset.st;
  document.querySelectorAll('.chip').forEach(c=>c.classList.toggle('active', c===chip));
  render(q.value);
});
jump.addEventListener('change', e=>{
  const id = e.target.value; if(!id) return;
  let needsRender = false;
  if (q.value){ q.value=''; needsRender = true; }              // clear any active search
  if (catFilter){ history.replaceState(null,'',location.pathname+location.search); catFilter=null; renderCatbar(); applyCatTitle(); needsRender = true; } // clear any active category
  if (needsRender) render('');
  const el = document.getElementById(id);
  if (el){ const top = el.getBoundingClientRect().top + window.scrollY - 84; window.scrollTo({top, behavior:'smooth'}); }
  e.target.selectedIndex = 0;                   // reset back to placeholder
});
applyCatTitle();
renderCatbar();
render('');
</script>
</body>
</html>
"""

out = HTML.replace('__DATA__', DATA_JSON).replace('__CATEGORIES__', CATEGORIES_JSON)
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(out)
print(f'Built index.html: {len(data)} shlokas, {n_audio} with audio.')
