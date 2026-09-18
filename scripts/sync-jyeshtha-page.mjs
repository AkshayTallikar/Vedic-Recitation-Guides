// Focused rebuild: preserve the current page shell and every other guide.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root=path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const page=path.join(root,'site/index.html');
const html=fs.readFileSync(page,'utf8');
const scripts=[...html.matchAll(/<script>\n([\s\S]*?)\n<\/script>/g)];
assert.equal(scripts.length,14,'Expected thirteen guide blocks and the app block.');
const guide=scripts.at(-2),app=scripts.at(-1);
assert.ok(guide[1].startsWith('// Generated from the reviewed manuscript by scripts/build-jyeshtha-guide.mjs.'));
assert.ok(guide[1].includes('"key": "jyeshtha-devi-puja"'));
assert.ok(app[1].includes('var requestedGuide = new URLSearchParams(window.location.search)'));
const replacement=filename=>'<script>\n'+fs.readFileSync(path.join(root,'site',filename),'utf8')+'\n</script>';
const updated=html.slice(0,guide.index)+replacement('data15.js')+
  html.slice(guide.index+guide[0].length,app.index)+replacement('app.js')+
  html.slice(app.index+app[0].length);
fs.writeFileSync(page,updated);
console.log('Synced Jyeṣṭhā guide and app; all other guide blocks and the page shell preserved.');
