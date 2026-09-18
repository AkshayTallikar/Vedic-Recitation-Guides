// Combine downloaded stages after a notebook runtime replacement.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
const inputs=process.argv.slice(2).map(p=>path.resolve(p));
assert.ok(inputs.length>=2,'Pass two or more extracted checkpoint directories.');
const records=new Map();
const files=new Map();
const diagnostics=new Map();
for(const input of inputs) {
  for(const record of JSON.parse(fs.readFileSync(path.join(input,'manifest.json'),'utf8'))) {
    const previous=records.get(record.id);
    if(previous) {
      assert.equal(record.originalScript,previous.originalScript);
      assert.equal(record.textSha256,previous.textSha256);
      assert.deepEqual(record.units,previous.units);
    }
    const wave=path.join(input,`jyeshtha-${record.id}.wav`);
    if(fs.existsSync(wave)) {
      assert.ok(record.duration>0,`Missing completed duration for ${record.id}`);
      records.set(record.id,record);
      files.set(record.id,{input,wave});
    } else if(!previous) records.set(record.id,record);
  }
  const diagnosticFile=path.join(input,'asr-diagnostics.json');
  if(fs.existsSync(diagnosticFile)) for(const diagnostic of JSON.parse(fs.readFileSync(diagnosticFile,'utf8'))) {
    const previous=diagnostics.get(diagnostic.file);
    if(previous) assert.equal(previous.reference,diagnostic.reference);
    diagnostics.set(diagnostic.file,diagnostic);
  }
}
assert.equal(records.size,30);
assert.equal(files.size,30,'Incomplete checkpoints: keep rendering the missing cards.');
const output=fs.mkdtempSync(path.join(os.tmpdir(),'jyeshtha-combined-drafts-'));
fs.mkdirSync(path.join(output,'units'));
for(const [id,{input,wave}] of files) {
  fs.copyFileSync(wave,path.join(output,path.basename(wave)));
  const record=records.get(id);
  for(let index=0;index<record.units.length;index++) {
    const stem=`jyeshtha-${id}-${String(index+1).padStart(2,'0')}`;
    for(const extension of ['wav','json','log']) {
      const source=path.join(input,'units',`${stem}.${extension}`);
      if(extension==='log' && !fs.existsSync(source)) continue;
      fs.copyFileSync(source,path.join(output,'units',`${stem}.${extension}`));
    }
  }
}
fs.writeFileSync(path.join(output,'manifest.json'),JSON.stringify([...records.values()].sort((a,b)=>a.id.localeCompare(b.id)),null,2)+'\n');
if(diagnostics.size) fs.writeFileSync(path.join(output,'asr-diagnostics.json'),JSON.stringify([...diagnostics.values()].sort((a,b)=>a.file.localeCompare(b.file)),null,2)+'\n');
console.log(output);
