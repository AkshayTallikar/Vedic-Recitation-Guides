import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import vm from 'node:vm';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const root=path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const load=file=>{
  const context={window:{GUIDES:[]}};
  vm.runInNewContext(fs.readFileSync(file,'utf8'),context);
  return JSON.parse(JSON.stringify(context.window.GUIDES[0]));
};
const original=load(path.join(root,'site/data15.js'));
const fixture=fs.mkdtempSync(path.join(os.tmpdir(),'jyeshtha-generator-test-'));
try {
  for(const folder of ['scripts','site/texts','site/audio15']) fs.mkdirSync(path.join(fixture,folder),{recursive:true});
  for(const file of ['scripts/build-jyeshtha-guide.mjs','site/texts/Jyeshtha-Devi-Puja-Romanized-Sanskrit.md']) {
    fs.copyFileSync(path.join(root,file),path.join(fixture,file));
  }
  const clips=original.sections.filter(s=>s.mantra).map(s=>({id:s.id,originalScript:s.originalScript,
    audioFile:`audio15/${s.id}.test`,duration:14.5}));
  for(const clip of clips) fs.writeFileSync(path.join(fixture,'site',clip.audioFile),'explicit non-audio test fixture');
  fs.writeFileSync(path.join(fixture,'site/audio15/manifest.json'),JSON.stringify({provenance:{type:'test-fixture'},clips}));
  const result=spawnSync(process.execPath,[path.join(fixture,'scripts/build-jyeshtha-guide.mjs')],{encoding:'utf8'});
  assert.equal(result.status,0,result.stderr);
  const updated=load(path.join(fixture,'site/data15.js'));
  assert.equal(updated.sections.length,33);
  assert.equal(updated.sections.filter(s=>s.audio).length,30);
  assert.equal(updated.practiceMode,'repeat3');
  assert.equal(updated.hideSourceWatchLinks,true);
  for(const old of original.sections) {
    const card=updated.sections.find(s=>s.id===old.id);
    for(const field of ['title','mantra','originalScript','structuredBlocks','sourceMarkdown','html']) {
      assert.deepEqual(card[field],old[field],`Changed lossless content ${old.id}.${field}`);
    }
    if(!old.mantra) assert.ok(!card.audio && !card.audioFile);
    if(old.id!=='02') assert.equal(card.action,old.action);
    if(old.id!=='01') assert.equal(card.meaning,old.meaning);
  }
  console.log('PASS: 33 cards, 30 audio bindings, 3 instruction cards, exact Sanskrit and source/layout preservation.');
} finally {
  fs.rmSync(fixture,{recursive:true,force:true});
}
