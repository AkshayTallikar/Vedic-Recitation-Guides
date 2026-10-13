"""Apply reviewed display/learning corrections while preserving the recorded guide."""
import copy
import hashlib
import json
from pathlib import Path

WORK=Path(__file__).resolve().parent
CHECKOUT=Path('/tmp/vedic-saraswati-guide')
BASELINE=json.loads((WORK/'baseline-guide.json').read_text())
GUIDE=copy.deepcopy(BASELINE)
SECTIONS={s['id']:s for s in GUIDE['sections']}
PDF=Path('/Users/akshaytallikar/Downloads/Vedavyasa_Sarasvati_Puja_English_IAST.pdf')
PDF_HASH=hashlib.sha256(PDF.read_bytes()).hexdigest()

def add_note(existing,note):
    if isinstance(existing,list):return existing+[note]
    return (str(existing)+'\n'+note).strip() if existing else note

def main():
    reviews=[json.loads((WORK/name).read_text()) for name in ['review-dhyanas.json','review-presence.json']]
    proposals=[p for review in reviews for p in review.get('proposals',[])]
    for p in proposals:
        if 'pdfPage' not in p:p['pdfPage']=p['reference']['pdfPage']
        if 'pdfPassage' not in p:p['pdfPassage']=p['reference']['passage']
        if 'acousticEvidence' not in p:p['acousticEvidence']={'witnesses':p.get('sourceWitnesses',[]),'basis':'Stored acoustic transcription witnesses; no new human listening or audio timing claim.'}
    peer=json.loads((WORK/'peer-review.json').read_text())
    assert peer.get('complete'), 'Independent review must be complete before applying corrections'
    refinements=peer.get('dhyanaDecisions',[])+peer.get('presenceDecisions',[])
    selected=[];rejected=[]
    for p in proposals:
        decision=next((d for d in refinements if d.get('sectionId')==p['sectionId'] and d.get('lineIndex')==p['lineIndex']
            and d.get('blockIndex',p['blockIndex'])==p['blockIndex']),None)
        assert decision, ('Missing independent reference decision',p)
        if decision['decision'].startswith('reject'):
            rejected.append({'proposal':p,'decision':decision,'resolution':'Keep the already primary-supported baseline meaning and gloss unchanged.'})
            continue
        assert decision['decision'].startswith('accept'), ('Unapproved reference proposal',p)
        if decision.get('suggestedMeaning') and not (p['sectionId']=='13' and p['lineIndex']==0):p['meaning']=decision['suggestedMeaning']
        adjustments=decision.get('wordAdjustments',decision.get('wordAdjustment',{}))
        for word in p['words']:
            if word['text'] in adjustments:word['meaning']=adjustments[word['text']]
        if p['sectionId']=='12' and p['lineIndex']==1:
            p['meaning']='Bearing discus and conch, accompanied by the beloved, with radiance surpassing ten million suns and supreme power.'
        if decision.get('suggestedMeaning') or adjustments:p['peerRefinement']=decision
        selected.append(p)
    proposals=selected
    applied=[];coordinates=set()
    for p in proposals:
        key=(p['sectionId'],p['blockIndex'],p['lineIndex'])
        if key in coordinates:raise ValueError(f'Duplicate proposal {key}')
        coordinates.add(key)
        s=SECTIONS[p['sectionId']];b=s['structuredBlocks'][p['blockIndex']]
        line=b['gloss']['lines'][p['lineIndex']]
        assert line and line['text']==p['beforeText'],key
        tokens=[t for t in p['afterText'].split() if t.strip('|।॥.,!?;:')]
        assert [w['text'] for w in p['words']]==tokens,key
        assert p['meaning'].strip() and all(w['meaning'].strip() for w in p['words']),key
        # Preserve all existing blank separators and the exact printed learning-line split.
        rows=b['text'].split('\n');nonblank=[i for i,t in enumerate(rows) if t.strip()]
        gloss_nonblank=[i for i,l in enumerate(b['gloss']['lines']) if l]
        row_index=nonblank[gloss_nonblank.index(p['lineIndex'])]
        assert rows[row_index]==p['beforeText'],key
        rows[row_index]=p['afterText'];b['text']='\n'.join(rows)
        previous=copy.deepcopy(line)
        line.update(text=p['afterText'],meaning=p['meaning'],words=p['words'])
        reference={'file':'backups/guide-saraswati-pdf-reference/Vedavyasa_Sarasvati_Puja_English_IAST.pdf',
            'sha256':PDF_HASH,'page':p['pdfPage'],'passage':p['pdfPassage'],
            'role':'User-supplied textual reference compared with the recording witnesses; not new timing authority.'}
        line['referenceReview']={'reference':reference,'beforeText':p['beforeText'],'afterText':p['afterText'],
            'notes':p['notes'],'confidence':p.get('confidence','reference-supported'),
            'acousticEvidence':p.get('acousticEvidence',{}),'audioCuePreserved':True}
        record=dict(p,previousLearningLine=previous,reference=reference)
        b.setdefault('referenceCorrections',[]).append({'lineIndex':p['lineIndex'],'before':p['beforeText'],
            'after':p['afterText'],'page':p['pdfPage'],'notes':p['notes']})
        applied.append(record)
    for s in GUIDE['sections']:
        changed=[b for b in s['structuredBlocks'] if b.get('referenceCorrections')]
        for b in changed:
            summaries=[f"PDF p. {r['page']}: {r['notes']}" for r in b['referenceCorrections']]
            b['notes']=add_note(b.get('notes'), 'Text reference review: '+' '.join(summaries))
        if changed:
            s['mantra']='\n\n'.join(b['text'] for b in s['structuredBlocks'] if b['kind']=='mantra')
            pages=sorted({r['page'] for b in changed for r in b['referenceCorrections']})
            label='Mantra reference (PDF '+('page ' if len(pages)==1 else 'pages ')+', '.join(map(str,pages))+')'
            s['html']=s.get('html','')+'<div class="source-link pdf-reference"><a href="../backups/guide-saraswati-pdf-reference/Vedavyasa_Sarasvati_Puja_English_IAST.pdf#page='+str(pages[0])+'" target="_blank" rel="noopener">'+label+'</a></div>'
    section_changes=[]
    for review in reviews:
        for p in review.get('sectionUpdates',[]):
            if 'pdfPage' not in p:p['pdfPage']=p['reference']['pdfPage']
            if 'pdfPassage' not in p:p['pdfPassage']=p['reference']['passage']
            s=SECTIONS[p['sectionId']];field=p['field']
            assert field=='contemplate' and s[field]==p['before'],p
            s[field]=p['after'];section_changes.append(p)
            evidence=s.get('enrichmentEvidence',s.get('guidanceReferences'))
            evidence['contemplate'].append({'reference':'User-supplied Vedavyasa and Sarasvati PDF',
                'file':'backups/guide-saraswati-pdf-reference/Vedavyasa_Sarasvati_Puja_English_IAST.pdf',
                'page':p['pdfPage'],'passage':p['pdfPassage'],'basis':'Supplementary contemplation corrected to match the textually reconciled meditation.'})
    GUIDE['referenceSources']=[{'id':'vedavyasa-sarasvati-pdf-reference','title':'Vedavyasa and Sarasvati Puja English IAST',
        'file':'backups/guide-saraswati-pdf-reference/Vedavyasa_Sarasvati_Puja_English_IAST.pdf','sha256':PDF_HASH,
        'reviewedPages':sorted({p['pdfPage'] for p in proposals}),
        'basis':'Selected textual corrections only; recorded repetitions, unmatched variants, original source text and audio cues are retained.'}]
    output='// Three original recording timelines; selected mantra readings reviewed against the supplied PDF.\n(window.GUIDES = window.GUIDES || []).push('+json.dumps(GUIDE,ensure_ascii=False,indent=2)+');\n'
    (CHECKOUT/'site/data17.js').write_text(output)
    report={'referencePdfSha256':PDF_HASH,'appliedLineCorrections':applied,'sectionUpdates':section_changes,
        'lineCorrections':len(applied),'affectedSections':sorted({p['sectionId'] for p in proposals}),
        'rejectedProposals':rejected,
        'limits':'Textual/acoustic-witness comparison, not new human listening certification; all recorded source strings and audio intervals unchanged.'}
    (WORK/'applied-corrections.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k in ['lineCorrections','affectedSections','limits']}))

if __name__=='__main__':main()
