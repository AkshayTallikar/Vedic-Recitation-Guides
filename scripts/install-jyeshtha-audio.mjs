// Install notebook-generated practice drafts without rewriting the manuscript.
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const drafts = path.resolve(process.argv[2] || '');
assert.ok(process.argv[2], 'Pass the extracted notebook draft directory.');
const records = JSON.parse(fs.readFileSync(path.join(drafts,'manifest.json'),'utf8'));
const diagnosticsPath = path.join(drafts,'asr-diagnostics.json');
const diagnostics = JSON.parse(fs.readFileSync(diagnosticsPath,'utf8'));
assert.equal(records.length,30);
assert.ok(diagnostics.length >= 30);
const context = {window:{GUIDES:[]}};
vm.runInNewContext(fs.readFileSync(path.join(root,'site/data15.js'),'utf8'),context);
const sections = context.window.GUIDES.find(g=>g.key==='jyeshtha-devi-puja').sections;
const destination = path.join(root,'site/audio15');
fs.mkdirSync(destination,{recursive:true});
function command(executable,args) {
  const result=spawnSync(executable,args,{encoding:'utf8'});
  if(result.error) throw result.error;
  assert.equal(result.status,0,result.stderr);
  return result.stdout;
}
function probe(file) {
  return JSON.parse(command('ffprobe',['-v','error','-show_streams','-show_format','-of','json',file]));
}
function syllables(text) {
  const letters=Array.from(text);
  return letters.filter((letter,index)=>{
    const point=letter.codePointAt(0);
    return (point>=0x0905 && point<=0x0914) ||
      (point>=0x0915 && point<=0x0939 && letters[index+1]!=='्');
  }).length;
}
const clips=[];
for(const record of records) {
  const section=sections.find(s=>s.id===record.id);
  assert.equal(record.originalScript,section.originalScript);
  assert.equal(record.textSha256,crypto.createHash('sha256').update(section.originalScript).digest('hex'));
  const input=path.join(drafts,`jyeshtha-${record.id}.wav`);
  const output=path.join(destination,`jyeshtha-${record.id}.mp3`);
  const source=probe(input);
  assert.equal(source.streams[0].channels,1);
  assert.equal(Number(source.streams[0].sample_rate),24000);
  assert.ok(Math.abs(Number(source.format.duration)-record.duration)<0.01);
  if(!fs.existsSync(output)) command('ffmpeg',['-v','error','-n','-i',input,'-codec:a','libmp3lame','-q:a','2',output]);
  const encoded=probe(output);
  const duration=Number(encoded.format.duration);
  assert.ok(duration>0 && Math.abs(duration-record.duration)<0.1);
  const units=record.units.map((unit,index)=>{
    const name=`jyeshtha-${record.id}-${String(index+1).padStart(2,'0')}.wav`;
    const diagnostic=diagnostics.find(d=>d.file===name);
    assert.ok(diagnostic,`Missing diagnostic ${name}`);
    const unitDuration=Number(probe(path.join(drafts,'units',name)).format.duration);
    assert.equal(diagnostic.reference,unit.padas.join(' '));
    const count=syllables(diagnostic.reference);
    assert.ok(unitDuration>=Math.max(0.3,count*0.12),`Suspiciously short recitation ${name}: ${unitDuration}s for ${count} syllables.`);
    return {sourceFile:name,start:0,end:unitDuration,meter:unit.meter,reference:diagnostic.reference,
      diagnosticCer:diagnostic.cer,reviewRequired:true};
  });
  clips.push({id:record.id,title:record.title,originalScript:record.originalScript,textSha256:record.textSha256,
    audioFile:`audio15/${path.basename(output)}`,duration,sourceDuration:record.duration,sourceWindows:units});
}
const provenance={
  type:'synthetic-practice',ttsModel:'https://huggingface.co/prathoshap/vagdhenu',
  asrModel:'https://huggingface.co/prathoshap/sushrota-sanskrit-asr',
  asrCheckpoint:'sushrota_sanskrit_asr_v13b.nemo',
  voiceCheckpoint:'voice_steer_ema_2026-06-17.pt',vocoderCheckpoint:'voc_bigvgan_EMA_2026-06-11.pth',
  rendererSha256:'b751b782f21277811f57adcfc40927164eee9a41413e15ea76e195cd38741956',
  settings:{steps:64,speed:0.9,cfgStrength:3,seed:50,autocast:false,sampleRate:24000,interUnitGap:0.65},
  asrLoading:'Original preprocessor, encoder and CTC tensors restored strictly; Sanskrit slice 4096–4351, blank 5632.',
  credit:'Prathosh A P, Indian Institute of Science, Bengaluru; Vāgdhenu, IndicF5 and NVIDIA BigVGAN.',
  warning:'AI-generated practice, not priest recordings or authoritative traditional pronunciation, metre or Vedic accents. ASR is diagnostic, not certification; human pronunciation review remains required.',
  sankalpa:'Both printed weekday alternatives are read separately. Supply the actual weekday and information omitted by the booklet’s ellipses.'
};
fs.writeFileSync(path.join(destination,'manifest.json'),JSON.stringify({provenance,clips},null,2)+'\n');
const evidence=path.join(root,'build/jyeshtha-audio-work');
fs.mkdirSync(evidence,{recursive:true});
fs.copyFileSync(diagnosticsPath,path.join(evidence,'asr-diagnostics.json'));
console.log(`Installed ${clips.length} synthetic practice clips, preserving all manuscript text.`);
