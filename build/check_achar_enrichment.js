// Checks content alignment for the 56-minute guide without changing files.
const fs = require('fs');
const vm = require('vm');
const path = require('path');

const root = path.join(__dirname, '..');
const context = {window:{}};
vm.createContext(context);
for (const file of ['site/data.js','site/achar-glosses.js','site/achar-enrichment.js','site/achar-rahasya-map.js']) {
  vm.runInContext(fs.readFileSync(path.join(root,file),'utf8'), context, {filename:file});
}
const guide = context.window.GUIDES.find(g => g.key === 'achar');
const glosses = context.window.ACHAR_GLOSSES;
const visuals = context.window.ACHAR_ENRICHMENT;
const rahasya = context.window.ACHAR_RAHASYA_MAP;
const problems = [];
if (guide.sections.length !== 47) problems.push('Expected 47 recording steps');
for (const step of guide.sections) {
  const id = step.id;
  if (!visuals[id] || !visuals[id].visual || !visuals[id].visual.prompt) problems.push(id + ': no visual prompt');
  if (!fs.existsSync(path.join(root, 'site/step-images/step-' + id + '.webp'))) problems.push(id + ': no generated image');
  if (!rahasya[id]) problems.push(id + ': no Rahasya match audit');
  if (!step.mantra) continue;
  const gloss = glosses[id];
  if (!gloss || !Array.isArray(gloss.lines)) { problems.push(id + ': no gloss lines'); continue; }
  const lines = step.mantra.split('\n');
  if (gloss.lines.length !== lines.length) problems.push(id + ': line count differs');
  lines.forEach((line,i) => {
    const entry = gloss.lines[i];
    if (!line.trim()) { if (entry) problems.push(id + ':' + (i+1) + ' separator differs'); return; }
    if (!entry || entry.text !== line) problems.push(id + ':' + (i+1) + ' text differs');
    if (!entry || !entry.meaning) problems.push(id + ':' + (i+1) + ' no line meaning');
    if (entry && entry.kind !== 'direction') {
      if (!entry.words || !entry.words.length) problems.push(id + ':' + (i+1) + ' no word gloss');
      const chantTokens = line.replace(/\([^)]*\)/g, '').trim().split(/\s+/).filter(token => /[\p{L}]/u.test(token));
      if (entry.words && entry.words.length !== chantTokens.length) problems.push(id + ':' + (i+1) + ' word gloss count differs');
      if (/needs source review|unresolved|\bTBD\b|lexical form/i.test(entry.meaning || '')) problems.push(id + ':' + (i+1) + ' placeholder meaning');
      for (const word of entry.words || []) {
        if (/needs source review|unresolved|\bTBD\b|lexical form/i.test(word.meaning || '')) problems.push(id + ':' + (i+1) + ' placeholder word');
      }
    }
  });
}
if (problems.length) {
  console.error(problems.join('\n'));
  process.exit(1);
}
console.log('47 guide steps, all mantra lines, visual prompts and Rahasya match entries aligned.');
