const assert=require('node:assert/strict');
const fs=require('node:fs');
const crypto=require('node:crypto');
const {chromium}=require('/Users/akshaytallikar/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const work='/Users/akshaytallikar/Vedic Recitation/work/saraswati-pdf-reference';
const base=process.argv[2]||'http://127.0.0.1:8768/';
const script=fs.readFileSync('/tmp/vedic-saraswati-guide/site/data17.js','utf8');
const guide=JSON.parse(script.slice(script.indexOf('.push(')+6,script.lastIndexOf(');')));
const changes=JSON.parse(fs.readFileSync(work+'/applied-corrections.json','utf8'));
(async()=>{
  const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
  try {
    const page=await browser.newPage({viewport:{width:1200,height:900}});
    const errors=[];page.on('pageerror',e=>errors.push(e.message));
    await page.goto(new URL('site/index.html?guide=saraswati-puja&reference-review='+Date.now(),base).href);
    await page.waitForSelector('.card');
    assert.equal(await page.locator('.card').count(),81);
    assert.equal(await page.locator('.chant-line').count(),453);
    assert.equal(await page.locator('.chant').count(),94);
    assert.equal(await page.locator('.spoken-action').count(),116);
    assert.equal(await page.locator('.lbl-c').count(),81);
    assert.equal(await page.locator('.lbl-a').count(),81);
    assert.equal(await page.locator('#tabs .tab').count(),13);
    assert.doesNotMatch(await page.locator('#tabs').innerText(),/Sung \(67 min\)|Uttaradi Matha/);
    for (const p of changes.appliedLineCorrections){
      const s=guide.sections.find(s=>s.id===p.sectionId);
      const b=s.structuredBlocks[p.blockIndex];
      const chantIndex=s.structuredBlocks.slice(0,p.blockIndex+1).filter(b=>b.kind==='mantra').length-1;
      const rowIndex=b.gloss.lines.slice(0,p.lineIndex).filter(Boolean).length;
      const row=page.locator('#sec-'+s.id+' .chant').nth(chantIndex).locator('.chant-line').nth(rowIndex);
      assert.equal(await row.locator('.chant-text').innerText(),p.afterText);
      assert.equal(await row.locator('.chant-meaning').innerText(),p.meaning);
      assert.deepEqual(await row.locator('.gloss-token b').allTextContents(),p.words.map(w=>w.text));
    }
    assert.equal(await page.locator('.pdf-reference a').count(),15);
    const href=await page.locator('#sec-18 .pdf-reference a').getAttribute('href');
    assert.ok(href.endsWith('#page=10'));
    const response=await page.request.get(new URL(href,page.url()).href);
    assert.equal(response.status(),200);
    assert.equal(crypto.createHash('sha256').update(await response.body()).digest('hex'),changes.referencePdfSha256);
    assert.match(await page.locator('#sec-18 .rahasya').innerText(),/Acyuta’s lap/);
    await page.evaluate(()=>document.getElementById('sec-18').scrollIntoView({block:'start',behavior:'instant'}));
    await page.screenshot({path:work+'/reference-desktop.png'});
    await page.setViewportSize({width:390,height:844});
    await page.evaluate(()=>document.getElementById('sec-18').scrollIntoView({block:'start',behavior:'instant'}));
    assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
    await page.screenshot({path:work+'/reference-mobile.png'});
    const s=guide.sections.find(s=>s.id==='18');const line=s.structuredBlocks[1].gloss.lines[0];
    await page.locator('#sec-18 .chant-line').first().locator('.cue-play').click();
    await page.waitForFunction(()=>document.getElementById('audio').readyState>=1&&!document.getElementById('audio').paused);
    const audio=await page.evaluate(()=>({src:document.getElementById('audio').src,time:document.getElementById('audio').currentTime}));
    assert.ok(audio.src.endsWith('/site/'+s.audioFile));
    assert.ok(Math.abs(audio.time-(line.startSeconds-s.audioStartSeconds))<1);
    assert.equal(errors.length,0,errors.join('\n'));
    const report={base,correctedRowsRendered:changes.lineCorrections,lineMeaningRows:453,recitationBoxes:94,instructionBoxes:116,contemplateActionPairs:81,pdfLinks:15,referencePdfHashMatches:true,correctedLineAudioReplay:true,recordedCueOffset:line.startSeconds-s.audioStartSeconds,observedAudioOffset:audio.time,mobileOverflow:false,archivedGuidesHidden:true,pageErrors:errors};
    fs.writeFileSync(work+(base.startsWith('http://127.')?'/ui-checks.json':'/live-ui-checks.json'),JSON.stringify(report,null,2)+'\n');
    console.log(JSON.stringify(report));
  } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exit(1)});
