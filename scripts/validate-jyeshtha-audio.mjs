import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import vm from 'node:vm';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const validator = process.argv[2];
if (!validator || !fs.existsSync(validator)) throw new Error('Pass the installed skill’s validate_verse_audio_guide.mjs path.');
const context = { window:{GUIDES:[]} };
vm.runInNewContext(fs.readFileSync(path.join(root,'site/data15.js'),'utf8'), context);
const guide = context.window.GUIDES.find(g => g.key === 'jyeshtha-devi-puja');
assert.equal(guide.sections.length,33);
assert.equal(guide.practiceMode,'repeat3');
assert.equal(guide.hideSourceWatchLinks,true);
const recitations = guide.sections.filter(section => section.originalScript);
assert.equal(recitations.length,30);
for (const section of guide.sections.filter(section => !section.originalScript)) {
  assert.ok(!section.audio && !section.audioFile, `Instruction-only card ${section.id} must remain text-only.`);
}
for (const section of recitations) {
  assert.equal(section.syntheticAudio,true);
  assert.equal(section.mantra,section.originalScript);
  assert.equal(section.sourceVideo,'https://huggingface.co/prathoshap/vagdhenu');
}
// The skill's verse validator expects every card to be a recitation. Validate
// the 30 recitations separately while preserving the three instruction cards.
const temporary = fs.mkdtempSync(path.join(os.tmpdir(),'jyeshtha-audio-validation-'));
try {
  const fixture = path.join(temporary,'recitations.js');
  const recitationGuide = {...guide,sections:recitations.map(section => ({
    ...section,audioFile:path.join(root,'site',section.audioFile)
  }))};
  fs.writeFileSync(fixture,`(window.GUIDES=window.GUIDES||[]).push(${JSON.stringify(recitationGuide)});\n`);
  const result = spawnSync(process.execPath,[validator,root,fixture,guide.key],{stdio:'inherit'});
  if (result.error) throw result.error;
  assert.equal(result.status,0,'Verse-audio validation failed.');
  console.log('33 ritual cards preserved: 30 playable recitations and 3 instruction-only cards.');
} finally {
  fs.rmSync(temporary,{recursive:true,force:true});
}
