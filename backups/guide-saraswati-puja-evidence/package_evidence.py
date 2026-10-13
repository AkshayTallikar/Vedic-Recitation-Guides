"""Preserve raw witnesses, checks and a durable standalone preview without credentials."""
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

WORK=Path(__file__).resolve().parent
PROJECT=WORK.parents[1]
SITE=Path('/tmp/vedic-saraswati-guide/site')
DEST=SITE.parent/'backups/guide-saraswati-puja-evidence'
DEST.mkdir(parents=True,exist_ok=True)

def copy(source,target,compressed=False):
    payload=source.read_bytes();target.parent.mkdir(parents=True,exist_ok=True)
    if compressed:
        target=target.with_name(target.name+'.gz')
        payload=gzip.compress(payload,mtime=0)
    target.write_bytes(payload)

for phase in ['avahana','puja','visarjana']:
    root=WORK/phase
    for folder in ['gpt','gpt-fine']:
        copy(root/folder/'chunks.json',DEST/phase/folder/'chunks.json')
        for response in (root/folder).glob('*-transcript.json'):
            value=json.loads(response.read_text())
            if not value.get('text') or value.get('error'):raise ValueError(f'Unsuccessful raw response {response.name}')
            copy(response,DEST/phase/folder/response.name,True)
    copy(root/'source/original.kn-orig.vtt',DEST/phase/'source/original.kn-orig.vtt',True)
    copy(root/'source/media-metadata.json',DEST/phase/'source/media-metadata.json')
    metadata=json.loads((root/'source/youtube-metadata.json').read_text())
    preserved={key:metadata.get(key) for key in ['id','title','channel','channel_id','uploader','upload_date','webpage_url','duration','description']}
    preserved['originalMetadataSha256']=hashlib.sha256((root/'source/youtube-metadata.json').read_bytes()).hexdigest()
    preserved['retainedPrivateMedia']=[{'file':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (root/'source').glob('original.*') if p.suffix in ['.mp3','.webm','.m4a']]
    (DEST/phase/'source/provenance.json').write_text(json.dumps(preserved,ensure_ascii=False,indent=2)+'\n')
    for folder in ['captions','reconciled']:
        for file in (root/folder).iterdir():
            if file.suffix not in ['.json','.txt','.py','.md','.vtt']:continue
            # Raw outputs and exact source text stay byte-identical inside gzip.
            raw=file.suffix in ['.txt','.vtt'] or bool('gpt4o' in file.name or file.name.endswith('-transcript.json'))
            trailing=any(line.rstrip(b' \t')!=line for line in file.read_bytes().splitlines())
            copy(file,DEST/phase/folder/file.name,raw or trailing)

validation=subprocess.check_output(['node','/Users/akshaytallikar/.codex/skills/build-lossless-puja-guides/scripts/validate_lossless_guide.mjs',
    '--data',str(SITE/'data17.js'),'--guide-key','saraswati-puja','--audio-root',str(SITE),
    '--require-spacing','--require-enrichment','--evidence-manifest',str(WORK/'guide-evidence.json')])
(WORK/'validation.json').write_bytes(validation)
for file in ['guide-evidence.json','audio-checks.json','line-cue-checks.json','source-cue-checks.json','ui-checks.json','caption-inventory.json','validation.json','repository-checks.json']:
    copy(WORK/file,DEST/file)
for file in ['build_combined.py','align_line_cues.py','check_source_cues.py','check_ui.cjs','caption_tools.py','package_evidence.py']:
    copy(WORK/file,DEST/file)

(DEST/'README.md').write_text('''# Saraswati Puja source evidence

One guide combines Cno0ngZM6KU (Avahana and preparation), hC8efJAiY2c (puja and third-day bali), and cw2W5gl6Low (Visarjana and Vijayadashami), from CHARANAM PAVITHRAM (Kongu Dwaitha). All three retain independent timelines. The 81 public clips use 250 ms boundary padding, bounded to measured media ends. Original media and signed raw YouTube metadata remain in the private work directory; hashes, stream metadata and stable source metadata are preserved here.

Successful raw API responses and native captions are byte-identical inside gzip files. Each source has overlapping 45-second/5-second-overlap and 180-second/10-second-overlap gpt-transcribe passes; unclear passages have additional short acoustic witnesses. Reconciled source text, Roman text, source ledgers, clause audits and lexical corrections remain separate. Gzip adds .gz to an original evidence filename; decompress to restore the referenced original filename.

Validation proves exact preservation of the complete reconciled source in 81 sections and 210 ordered speech blocks, with 453 Sanskrit line/word meaning rows and evidence-backed Contemplate and Action at every step. It does not certify every acoustic reading as exact. Native caption markers and acoustic model witnesses supply alignment; no human listening interface was available. Shared line intervals are explicitly labelled Passage in the guide. Source-cue checks separately retain nonlexical caption markers and unclassified transitions rather than inventing spoken text or asserting silence.

Specific uncertain readings remain visible. Textual corrections identify the independent Sanskrit witness and preserve raw phonetic evidence. Calendar dates and timing advice belong to the 2025 recordings. All closing teaching is retained, including the food recipe, household implements, Madhva Jayanti, shami observance, teacher offerings and children resuming study.

The local ignored .env stores the transcription key with private permissions. No credential is included in this evidence, guide or commit.
''')

OUT=PROJECT/'output/saraswati-puja';OUT.mkdir(parents=True,exist_ok=True)
shutil.copytree(SITE/'audio17',OUT/'audio17',dirs_exist_ok=True)
template=(SITE.parent/'build/index.template.html').read_text()
first=template.index('<script src="data.js">');last=template.index('</script>',template.index('<script src="app.js">'))+len('</script>')
inline='\n'.join('<script>\n'+(SITE/file).read_text()+'\n</script>' for file in ['data17.js','guide-catalog.js','app.js'])
standalone=template[:first]+inline+template[last:]
standalone=standalone.replace('href="../index.html"','href="https://akshaytallikar.github.io/Vedic-Recitation-Guides/"')
(OUT/'index.html').write_text(standalone)

# Inspect payloads internally without displaying any credential.
key=None
for row in (PROJECT/'.env').read_text().splitlines():
    if row.startswith('OPENAI_API_KEY='):key=row.partition('=')[2].strip().strip('\"\'').encode()
if not key:raise ValueError('Credential unavailable for exclusion audit')
for file in list(DEST.rglob('*'))+[SITE/'data17.js',SITE/'index.html',OUT/'index.html']:
    if not file.is_file():continue
    payload=file.read_bytes()
    if file.suffix=='.gz':payload=gzip.decompress(payload)
    if key in payload:raise ValueError(f'Credential found in intended artifact: {file.name}')
manifest=[{'file':str(file.relative_to(DEST)),'bytes':file.stat().st_size,'sha256':hashlib.sha256(file.read_bytes()).hexdigest()} for file in sorted(DEST.rglob('*')) if file.is_file() and file.name!='package-manifest.json']
(DEST/'package-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'evidenceFiles':len(manifest),'credentialExclusionPassed':True,'standalonePreview':str(OUT/'index.html')}))
