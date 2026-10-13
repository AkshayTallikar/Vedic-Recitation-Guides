import pathlib,importlib.util,subprocess,concurrent.futures,json
R=pathlib.Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location('t',R.parents[1]/'transcribe.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);m.configure_key()
T=[('guru-open',283,335),('madhuparka',520,545),('deity-meditation',358,389),('food-verse',1143,1177),('prayers-open',1360,1427),('prayers-four-arms',1427,1478),('sankalpa-year',149,165)]
def run(t):
 name,a,b=t;p=R/(name+'.mp3');out=R/(name+'-transcript.json')
 if not p.exists():subprocess.run(['ffmpeg','-y','-v','error','-ss',str(a),'-i',str(R.parent/'source/original.mp3'),'-t',str(b-a),'-c:a','libmp3lame','-q:a','2',str(p)],check=True)
 result=m.transcribe((p,out));print(name,'saved',flush=True);return {'id':name,'startSeconds':a,'endSeconds':b,'file':str(out),'result':result}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(run,T))
json.dump(results,open(R/'targeted-transcription-manifest.json','w'),ensure_ascii=False,indent=2)
