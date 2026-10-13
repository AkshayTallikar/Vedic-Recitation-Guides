from pathlib import Path
import importlib.util,json,subprocess,concurrent.futures
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
spec=importlib.util.spec_from_file_location('puja_transcribe',BASE.parent/'transcribe.py');api=importlib.util.module_from_spec(spec);spec.loader.exec_module(api);api.configure_key()
TARGETS=[('kapila',308.56,346.47),('saraswati',640.24,678.88),('book-invocation',722.,759.04),('pratishtha',847.36,895.04)]
def run(item):
 name,a,z=item;audio=HERE/(name+'-review.mp3');out=HERE/(name+'-gpt4o.json')
 if not audio.exists():subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-ss',str(a),'-i',str(BASE/'source/original.mp3'),'-t',str(z-a),'-map','0:a:0','-c:a','libmp3lame','-q:a','3',str(audio)],check=True)
 if out.exists():return {'name':name,'cached':True}
 status,response=api.request_transcription(audio,'gpt-4o-transcribe')
 if status!=200:raise RuntimeError('HTTP '+str(status))
 out.write_bytes(response);return {'name':name,'status':status,'characters':len(json.loads(response).get('text',''))}
(HERE/'acoustic-hotspots-manifest.json').write_text(json.dumps([{'name':n,'sourceId':'avahana','startSeconds':a,'endSeconds':z,'model':'gpt-4o-transcribe','file':n+'-gpt4o.json'} for n,a,z in TARGETS],indent=2))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:
 for r in p.map(run,TARGETS):print(json.dumps(r),flush=True)
