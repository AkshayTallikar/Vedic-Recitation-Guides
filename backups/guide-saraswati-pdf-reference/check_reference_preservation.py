"""Require exact recorded-source, layout, guidance and audio preservation for this edit."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess

WORK=Path(__file__).resolve().parent
SITE=Path('/tmp/vedic-saraswati-guide/site')
before=json.loads((WORK/'baseline-guide.json').read_text())
script=(SITE/'data17.js').read_text()
after=json.loads(script[script.index('.push(')+6:script.rindex(');')])
changes=json.loads((WORK/'applied-corrections.json').read_text())
selected={(p['sectionId'],p['blockIndex'],p['lineIndex']) for p in changes['appliedLineCorrections']}
changed_blocks={(sid,bi) for sid,bi,li in selected}
changed_sections={sid for sid,bi in changed_blocks}
guidance_updates={p['sectionId']:p for p in changes['sectionUpdates']}
old_meta={k:v for k,v in before.items() if k!='sections'}
new_meta={k:v for k,v in after.items() if k not in ['sections','referenceSources']}
assert old_meta==new_meta,'Unrelated guide metadata changed'
assert len(before['sections'])==len(after['sections'])==81
line_count=0
for old,new in zip(before['sections'],after['sections']):
    assert old['id']==new['id']
    old_fields=copy.deepcopy(old);new_fields=copy.deepcopy(new)
    for fields in [old_fields,new_fields]:
        fields.pop('structuredBlocks')
        if old['id'] in changed_sections:
            fields.pop('mantra')
            fields.pop('html',None)
        if old['id'] in guidance_updates:
            fields.pop('contemplate');fields.pop('guidanceReferences',None);fields.pop('enrichmentEvidence',None)
    assert old_fields==new_fields,('Unrelated section fields changed',old['id'])
    if old['id'] in changed_sections:assert new['html'].startswith(old.get('html','')) and 'class="source-link pdf-reference"' in new['html']
    if old['id'] in guidance_updates:
        update=guidance_updates[old['id']]
        assert old['contemplate']==update['before'] and new['contemplate']==update['after']
        key='enrichmentEvidence' if 'enrichmentEvidence' in old else 'guidanceReferences'
        assert new[key]['contemplate'][:-1]==old[key]['contemplate']
        assert new[key]['action']==old[key]['action']
    assert len(old['structuredBlocks'])==len(new['structuredBlocks'])
    for bi,(ob,nb) in enumerate(zip(old['structuredBlocks'],new['structuredBlocks'])):
        if (old['id'],bi) not in changed_blocks:
            assert ob==nb,('Untouched block changed',old['id'],bi)
        else:
            assert ob['kind']==nb['kind']=='mantra'
            of={k:v for k,v in ob.items() if k not in ['text','gloss','notes']}
            nf={k:v for k,v in nb.items() if k not in ['text','gloss','notes','referenceCorrections']}
            assert of==nf,('Recorded block fields changed',old['id'],bi)
            assert [bool(t.strip()) for t in ob['text'].split('\n')]==[bool(t.strip()) for t in nb['text'].split('\n')],('Line split changed',old['id'],bi)
            assert {k:v for k,v in ob['gloss'].items() if k!='lines'}=={k:v for k,v in nb['gloss'].items() if k!='lines'}
            assert len(ob['gloss']['lines'])==len(nb['gloss']['lines'])
            for li,(ol,nl) in enumerate(zip(ob['gloss']['lines'],nb['gloss']['lines'])):
                if (old['id'],bi,li) not in selected:assert ol==nl
                else:
                    assert {k:v for k,v in ol.items() if k not in ['text','meaning','words']}=={k:v for k,v in nl.items() if k not in ['text','meaning','words','referenceReview']},('Cue or attribution changed',old['id'],li)
        line_count+=len([l for l in nb.get('gloss',{}).get('lines',[]) if l])
assert line_count==453
for row in json.loads((WORK.parent/'saraswati-puja/audio-checks.json').read_text()):
    assert hashlib.sha256((SITE/row['file']).read_bytes()).hexdigest()==row['sha256'],row['file']
validation=subprocess.check_output(['node','/Users/akshaytallikar/.codex/skills/build-lossless-puja-guides/scripts/validate_lossless_guide.mjs',
    '--data',str(SITE/'data17.js'),'--guide-key','saraswati-puja','--audio-root',str(SITE),
    '--require-spacing','--require-enrichment','--evidence-manifest',str(WORK.parent/'saraswati-puja/guide-evidence.json')])
report={'passed':True,'correctedLines':len(selected),'sourceCharacters':sum(len(s['originalScript']) for s in after['sections']),
    'learningLines':line_count,'sections':81,'audioHashesUnchanged':81,'allSourceOriginalAndSourceRomanUnchanged':True,
    'allSourceCuesAndClipOriginsUnchanged':True,'allEnglishInstructionsAndActionsUnchanged':True,
    'lineSplitsAndStanzaSeparatorsPreserved':True,'onlyApprovedLearningCorrectionsApplied':True,
    'strictValidation':json.loads(validation)}
(WORK/'preservation-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
