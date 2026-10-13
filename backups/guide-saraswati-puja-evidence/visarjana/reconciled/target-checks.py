import sys,json,subprocess,concurrent.futures
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import transcribe
transcribe.configure_key()
out=Path(__file__).resolve().parent
windows=[('dismissal',43,79),('madhva',126,147),('shami-one',160,177),('shami-two',191,216),('shami-three',217,244),('charity',283,303)]
def run(w):
 name,start,end=w;p=out/(name+'.mp3');j=out/(name+'-gpt4o.json')
 subprocess.run(['ffmpeg','-v','error','-y','-ss',str(start),'-i',str(out.parent/'source/original.mp3'),'-t',str(end-start),'-c:a','libmp3lame',str(p)],check=True)
 status,body=transcribe.request_transcription(p,'gpt-4o-transcribe')
 if status==200:j.write_bytes(body)
 else:j.write_text(json.dumps({'httpStatus':status}))
 return name,status
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for r in ex.map(run,windows):print(r,flush=True)
(out/'target-checks-manifest.json').write_text(json.dumps([{'id':n,'startSeconds':s,'endSeconds':e,'model':'gpt-4o-transcribe'} for n,s,e in windows],indent=2))
