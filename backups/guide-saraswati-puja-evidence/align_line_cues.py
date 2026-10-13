"""Align Roman display lines to native caption markers; retain confidence/evidence."""
import difflib
import json
import re
import unicodedata

CONS=dict(zip('ಕಖಗಘಙಚಛಜಝಞಟಠಡಢಣತಥದಧನಪಫಬಭಮಯರಲವಶಷಸಹಳ',['k','kh','g','gh','ṅ','c','ch','j','jh','ñ','ṭ','ṭh','ḍ','ḍh','ṇ','t','th','d','dh','n','p','ph','b','bh','m','y','r','l','v','ś','ṣ','s','h','ḷ']))
VOWELS=dict(zip('ಅಆಇಈಉಊಋೠಎಏಐಒಓಔ',['a','ā','i','ī','u','ū','ṛ','ṝ','e','ē','ai','o','ō','au']))
SIGNS=dict(zip('ಾಿೀುೂೃೄೆೇೈೊೋೌ',['ā','i','ī','u','ū','ṛ','ṝ','e','ē','ai','o','ō','au']))
def roman(text):
    out='';i=0
    while i<len(text):
        c=text[i]
        if c in CONS:
            out+=CONS[c]
            if i+1<len(text) and text[i+1] in SIGNS:out+=SIGNS[text[i+1]];i+=1
            elif i+1<len(text) and text[i+1]=='್':i+=1
            else:out+='a'
        else:out+=VOWELS.get(c,{'ಂ':'ṁ','ಃ':'ḥ','ಽ':'’','್':''}.get(c,c))
        i+=1
    return out

def norm(text):
    text=text.replace('ṛ','ri').replace('ṝ','ri').replace('ṅ','n').replace('ñ','n').lower()
    return re.sub('[^a-z]','',unicodedata.normalize('NFD',text).encode('ascii','ignore').decode())

def align(block,events,duration):
    lines=[x for x in block.get('gloss',{}).get('lines',[]) if x and x.get('kind')!='direction']
    selected=[e for e in events if e['end']>block['startSeconds'] and e['start']<block['endSeconds'] and not re.search(r'\[.*?\]',e['text'])]
    text='';positions=[]
    for ei,e in enumerate(selected):
        t=norm(roman(e['text']));text+=t;positions.extend([ei]*len(t))
    target=''.join(norm(line['text']) for line in lines)
    mapping={}
    for match in difflib.SequenceMatcher(None,target,text,autojunk=False).get_matching_blocks():
        for j in range(match.size):mapping[match.a+j]=match.b+j
    records=[];offset=0
    for line in lines:
        length=len(norm(line['text']))
        hits=[mapping[x] for x in range(offset,offset+length) if x in mapping]
        score=len(hits)/length if length else 0
        existing_start=line.get('startSeconds');existing_end=line.get('endSeconds')
        independently_resolved=(isinstance(existing_start,(int,float)) and isinstance(existing_end,(int,float))
            and block['startSeconds']<=existing_start<existing_end<=min(block['endSeconds'],duration)
            and not line.get('sharedPassageCue'))
        if independently_resolved:
            # Reconciler-selected native boundaries take precedence over fuzzy ASR matching.
            line.setdefault('timingStatus','Native caption boundaries selected during independent source reconciliation; not human listening')
            line.setdefault('timingEvidence',{'source':'source-local reconciliation and native VTT boundary audit'})
        elif hits and score>=0.64:
            first=selected[positions[min(hits)]];last=selected[positions[max(hits)]]
            start=max(block['startSeconds'],first['start']);end=min(block['endSeconds'],duration,last['end'])
            if end>start:
                line['startSeconds']=start;line['endSeconds']=end
                line['timingStatus']='Matched native caption markers against reconciled text; ASR alignment, not human listening'
                line['timingEvidence']={'source':'native Kannada VTT embedded markers','matchFraction':round(score,3),'cueIndices':list(dict.fromkeys(selected[positions[h]]['source']['cueIndex'] for h in hits))}
                line.pop('sharedPassageCue',None)
        else:
            line['timingStatus']='Shared recorded passage interval; individual line could not be resolved from captions'
            line['sharedPassageCue']=True
        records.append({'text':line['text'],'start':line.get('startSeconds'),'end':line.get('endSeconds'),'matchFraction':round(score,3),'sharedPassage':bool(line.get('sharedPassageCue')),'preservedReconcilerCue':independently_resolved})
        offset+=length
    return records
