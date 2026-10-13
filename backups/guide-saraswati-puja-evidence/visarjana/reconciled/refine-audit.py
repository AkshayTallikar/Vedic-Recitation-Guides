import json
from pathlib import Path
D=Path(__file__).resolve().parent
S=json.loads((D/'sections.json').read_text())
# Preserve source-language self-repairs and clarify competing acoustic readings.
b=S[5]['structuredBlocks'][-1];b['notes'].append('Fine GPT reads aṣṭāṅgakuṃkumadinda, coarse GPT reads aṣṭāṅga namaskāradinda, targeted GPT-4o reads a compressed …aśnāguṃkumadinda, while native captions give turmeric/kumkuma. The turmeric/kumkuma reading is provisional; an additional bodily gesture is not securely established.')
S[5]['verifyNotes']+=b['notes'][-1:]
b=S[9]['structuredBlocks'][0];b['sourceOriginal']=b['sourceOriginal'].rstrip()+' ಈ, ';b['sourceRoman']=b['sourceRoman'].rstrip()+' ī, ';b['english']+=' This—'
# Tighten uncertain canonical forms to actual acoustic readings.
for s in S:s['originalScript']=''.join(b['sourceOriginal'] for b in s['structuredBlocks'])
(D/'sections.json').write_text(json.dumps(S,ensure_ascii=False,indent=2));source=''.join(s['originalScript'] for s in S);(D/'complete-source.txt').write_text(source);(D/'complete-roman.txt').write_text(''.join(b['sourceRoman'] for s in S for b in s['structuredBlocks']))
G=json.loads((D/'evidence-manifest.json').read_text());lookup={b['segmentId']:b for s in S for b in s['structuredBlocks']}
for g in G['segments']:g['sourceOriginal']=lookup[g['id']]['sourceOriginal']
G['sources'][0]['originalScript']=source
(D/'evidence-manifest.json').write_text(json.dumps(G,ensure_ascii=False,indent=2));(D/'aligned-segments.json').write_text(json.dumps(G['segments'],ensure_ascii=False,indent=2))
U=[{'segmentId':b['segmentId'],'startSeconds':b['startSeconds'],'endSeconds':b['endSeconds'],'notes':b['notes']} for s in S for b in s['structuredBlocks'] if b.get('notes')]
(D/'uncertainty-inventory.json').write_text(json.dumps(U,ensure_ascii=False,indent=2))
