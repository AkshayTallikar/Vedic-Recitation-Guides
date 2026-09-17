import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const markdownPath = path.join(root, 'site/texts/Jyeshtha-Devi-Puja-Romanized-Sanskrit.md');
const markdown = fs.readFileSync(markdownPath, 'utf8');
const plain = text => text.replace(/\*\*/g, '').replace(/\*/g, '').replace(/`/g, '').trim();
const groups = [...markdown.matchAll(/^## (\d+)\. (.+)\n([\s\S]*?)(?=^## |$(?![\s\S]))/gm)];
if (groups.length !== 13) throw new Error('Expected all 13 manuscript groups');
const pages = {
  1:'3', 2:'3', 3:'4', 4:'4', 5:'5', 6:'5',
  8:'8', 9:'9', 10:'10', 11:'10–11', 12:'11', 13:'11–12'
};
const sections = [];
const titles = {
  1:'Introduction and timing', 2:'Saṅkalpa', 3:'Śaṅkha pūjā',
  4:'Kalaśa sthāpanā and pīṭha pūjā', 5:'Navaśakti pūjā', 6:'Āvāhana',
  9:'Sixteen-knot sacred cord worship', 13:'Vrata narrative'
};

function extractMantra(body, group) {
  const output = [];
  let english = false, lastIndex = -2;
  body.split('\n').forEach((line, index) => {
    if (/^### English Meaning/.test(line)) english = true;
    if (/^### Sanskrit/.test(line)) english = false;
    let selected = null;
    if (!english && /^>/.test(line)) {
      const text = line.replace(/^>\s?/, '').trim();
      if (text && !text.startsWith('*(') && !/^(?:\*)?Meaning:/.test(text)) selected = plain(text);
    }
    if ([4,5,8,9].includes(group)) {
      const match = line.match(/^(?:\d+\.|-)\s+\*\*(.+?)\*\*/);
      if (match) selected = match[1];
    }
    if (selected) {
      if (output.length && index > lastIndex + 1) output.push('');
      output.push(selected);
      lastIndex = index;
    }
  });
  return output.join('\n').trim();
}

function extractMeaning(body, group) {
  const english = body.match(/^### English Meaning:\s*\n([\s\S]*)/m);
  if (english) return plain(english[1].replace(/^>\s?/gm,'').replace(/^---\s*$/gm,''));
  const meanings = [...body.matchAll(/^\*\*Meaning:\*\*\s*([\s\S]*?)(?=^### |^---|$\n?$(?![\s\S]))/gm)]
    .map(match => plain(match[1].split('\n').filter(line => !/^\*\(/.test(line)).join('\n'))).filter(Boolean);
  if (meanings.length) return meanings.join('\n\n');
  if ([4,5,8,9].includes(group)) {
    return body.split('\n').map(line => {
      const match = line.match(/^\s*\*\((Salutations.+)\)\*\s*$/) || line.match(/\*\((Salutations.+)\)\*/);
      return match ? plain(match[1]) : '';
    }).filter(Boolean).join('; ');
  }
  if ([1,13].includes(group)) return plain(body
    .replace(/^\*\(Source:.*\)\*\s*$/gm,'')
    .replace(/^---\s*$/gm,'')
    .replace(/^### (.+):?\s*$/gm,'$1')
    .replace(/^\s*-\s+/gm,'')
    .replace(/^\s+/gm,''));
  return '';
}

for (const match of groups) {
  const group = Number(match[1]);
  const groupTitle = match[2];
  const body = match[3];
  const split = [7,8,10,11,12].includes(group);
  const chunks = split
    ? [...body.matchAll(/^### (.+)\n([\s\S]*?)(?=^### |$(?![\s\S]))/gm)].map(m => ({title:m[1],body:m[2]}))
    : [{title:titles[group] || groupTitle, body}];
  for (const [part, chunk] of chunks.entries()) {
    let mantra = extractMantra(chunk.body, group);
    const meaning = extractMeaning(chunk.body, group).replace(/\s*\(Specially offer 16 sweet fried cakes\/apūpas\)\.?/g, '');
    const id = String(sections.length + 1).padStart(2,'0');
    let title = chunk.title.replace(/^\d+\. /,'').replace(/:\s*$/,'');
    const actions = chunk.body.split('\n').filter(line => /^\*\(/.test(line) && !line.includes('(Source:'))
      .map(line => plain(line).replace(/^\(([\s\S]*)\)[.:]?$/,'$1'));
    if (group === 3) actions.splice(1,0,'Wash the conch while reciting sahasrāra huṃ phaṭ.');
    if (group === 10 && part === 2) actions.push('Especially offer sixteen apūpas (sweet cakes).');
    if (group === 10 && part === 4) {
      mantra = '';
      actions.push('Offer maṅgaḷārati.');
    }
    let page = pages[group];
    if (group === 7) page = part < 2 ? '5' : part < 7 ? '6' : part === 7 ? '6–7' : part < 13 ? '7' : '8';
    if (group === 11) page = part ? '11' : '10–11';
    const section = {
      id, slug:`jyeshtha-${id}`, group:groupTitle.replace(/^\d+\. /,''),
      page, title, mantra, meaning, action:actions.join('\n\n'),
      originalScript:mantra,
      structuredBlocks:mantra ? [{kind:'mantra',sourceOriginal:mantra,text:mantra.replace(/(\|\|)(?=\n\S)/g,'$1\n')}] : [],
      sourceMarkdown:chunk.body
    };
    if (group === 1) section.meaning += '\n\nText note: The Sanskrit follows the printed booklet, including its nonstandard sadgati-prakṛti and araṇyām readings. The invocation meaning interprets the intended fire-stick analogy. Source ellipses are retained. This booklet-based guide has no audio.';
    if (group === 4) section.html = '<figure class="altar-illustration">' +
      '<a href="assets/jyeshtha-devi-altar.png" target="_blank" rel="noopener" aria-label="Open the altar illustration at full size">' +
      '<img src="assets/jyeshtha-devi-altar.png" alt="Illustrative Jyeshtha Devi altar: a kalasha on rice and an eight-petaled lotus beneath a canopy, with a knotted cord, puja bowls, flowers, apupa offering, and a lamp kept clear of cloth." width="1448" height="1086" loading="lazy" decoding="async"></a>' +
      '<figcaption>AI-generated illustrative arrangement, not a prescribed ritual layout. Decorations are optional; follow your family tradition. Count the dora’s sixteen strands and sixteen knots, and the sixteen apūpas, independently. Keep the lamp clear of cloth. Tap the image to view it at full size.</figcaption></figure>';
    sections.push(section);
  }
}

if (sections.length !== 33) throw new Error(`Expected 33 cards, found ${sections.length}`);
if (sections.filter(s => s.mantra).length !== 30) throw new Error('Expected 30 recitation cards');
if (sections.some(s => s.mantra.includes('Meaning:') || s.mantra.includes('Salutations'))) throw new Error('English leaked into recitation');
const guide = {
  key:'jyeshtha-devi-puja', title:'Jyeṣṭhā Devī Pūjā', tabLabel:'Booklet · 33 text steps',
  noAudio:true, hideNotice:true, hideLosslessReferences:true, preserveMeaningLines:true,
  subtitle:'Romanized Sanskrit, English meanings, and ritual directions from the 2026 Kannada booklet',
  source:'texts/jyeshtha-devi-puja-kannada-2026.pdf', sourceLabel:'Kannada source booklet (PDF)',
  sourceCredit:'Pt. Mahidas Achar Joshi · Vishva Madhwa Maha Parishat Granthamala 259 · Śrī Uttarādi Maṭha · 2026',
  structuredMantraLabel:'Sanskrit recitation · IAST',
  sections
};
const output = '// Generated from the reviewed manuscript by scripts/build-jyeshtha-guide.mjs.\n' +
  '(window.GUIDES = window.GUIDES || []).push(' + JSON.stringify(guide,null,2) + ');\n';
fs.writeFileSync(path.join(root,'site/data15.js'), output);
console.log(`Built ${sections.length} Jyeṣṭhā Devī Pūjā cards (${sections.filter(s=>s.mantra).length} recitation cards).`);
