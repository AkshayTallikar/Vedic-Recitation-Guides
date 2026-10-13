import pathlib,re,json,html
R=pathlib.Path(__file__).resolve().parent
text=(R.parent/'source/original.kn-orig.vtt').read_text()
def sec(s):
 h,m,x=s.split(':');return int(h)*3600+int(m)*60+float(x)
events=[];cues=[]
for i,p in enumerate(text.split('\n\n')):
 lines=p.splitlines();ti=next((j for j,l in enumerate(lines) if '-->' in l),None)
 if ti is None:continue
 a,b=re.findall(r'(\d\d:\d\d:\d\d\.\d\d\d)',lines[ti])[:2];a,b=sec(a),sec(b)
 texts=[l.strip() for l in lines[ti+1:] if l.strip()]
 cues.append({'index':i,'start':a,'end':b,'text':html.unescape(re.sub('<[^>]+>','', ' '.join(texts)))})
 if b-a<=.03 or not texts:continue
 line=texts[-1]
 parts=re.split(r'<(\d\d:\d\d:\d\d\.\d\d\d)>',line);at=a
 for j in range(0,len(parts),2):
  word=html.unescape(re.sub('<[^>]+>','',parts[j])).strip();end=sec(parts[j+1]) if j+1<len(parts) else b
  if word:events.append({'start':at,'end':end,'raw_word':word,'raw_cue_ref':{'source_file':'original.kn-orig.vtt','cue_index':i,'startSeconds':a,'endSeconds':b}})
  at=end
json.dump({'source_file':'original.kn-orig.vtt','timing_method':'Actual embedded VTT markers, latest caption line only; short redisplay cues skipped','events':events},open(R/'native-word-events.json','w'),ensure_ascii=False,indent=2)
json.dump(cues,open(R/'caption-cues.json','w'),ensure_ascii=False,indent=2)
rows=[]
for c in cues:
 if c['end']-c['start']<=.03:continue
 local=[e for e in events if e['raw_cue_ref']['cue_index']==c['index']]
 rows.append(f"{c['start']:.3f}–{c['end']:.3f} "+' '.join(e['raw_word'] for e in local))
(R/'caption-reading-aid.txt').write_text('\n'.join(rows))
print('\n'.join(rows))
