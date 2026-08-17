#!/usr/bin/env python3
from __future__ import annotations
import csv, json, os, re, time, unicodedata, urllib.error, urllib.parse, urllib.request
from pathlib import Path

API='https://api.elevenlabs.io'
OUT=Path('audition_out')
OUT.mkdir(exist_ok=True)
KEY=(os.getenv('ELEVENLABS_API_KEY') or os.getenv('XI_API_KEY') or '').strip()
MODELS=['eleven_v3','eleven_multilingual_v2']
FMT='mp3_44100_128'

def safe(s):
    s=unicodedata.normalize('NFKD',s)
    s=''.join(c for c in s if not unicodedata.combining(c)).encode('ascii','ignore').decode()
    return re.sub(r'[^A-Za-z0-9._-]+','_',s).strip('._-')[:70] or 'voz'

def req_json(url):
    r=urllib.request.Request(url,headers={'xi-api-key':KEY,'Accept':'application/json'})
    with urllib.request.urlopen(r,timeout=60) as x:
        return json.loads(x.read().decode())

def all_voices():
    out={}; token=None
    while True:
        q={'page_size':100,'include_total_count':'true','sort':'name','sort_direction':'asc'}
        if token: q['next_page_token']=token
        d=req_json(API+'/v2/voices?'+urllib.parse.urlencode(q))
        for v in d.get('voices') or []:
            vid=str(v.get('voice_id') or '').strip()
            if not vid: continue
            labels=v.get('labels') or {}
            out[vid]={
                'voice_id':vid,'name':str(v.get('name') or vid),
                'gender':str(labels.get('gender') or ''),
                'accent':str(labels.get('accent') or ''),
                'category':str(v.get('category') or ''),
                'description':str(v.get('description') or labels.get('description') or labels.get('use_case') or '')
            }
        if not d.get('has_more'): break
        token=d.get('next_page_token')
        if not token: break
    def g(v):
        x=v['gender'].lower()
        return 0 if x=='male' else 2 if x=='female' else 1
    def pt(v):
        t=' '.join(v.values()).lower()
        return 0 if any(z in t for z in ('brazil','brasil','portugu','pt-br')) else 1
    return sorted(out.values(), key=lambda v:(g(v),pt(v),v['name'].casefold(),v['voice_id']))

def tts(v,text,model):
    url=f"{API}/v1/text-to-speech/{urllib.parse.quote(v['voice_id'])}?output_format={FMT}"
    data=json.dumps({'text':text,'model_id':model},ensure_ascii=False).encode()
    r=urllib.request.Request(url,data=data,method='POST',headers={'xi-api-key':KEY,'Content-Type':'application/json','Accept':'audio/mpeg'})
    with urllib.request.urlopen(r,timeout=180) as x:
        raw=x.read()
    if len(raw)<1000: raise RuntimeError(f'audio pequeno: {len(raw)} bytes')
    return raw

def main():
    if not KEY:
        (OUT/'STATUS.txt').write_text('BLOQUEADO: GitHub Secret ELEVENLABS_API_KEY/XI_API_KEY não está disponível. Nenhuma chamada TTS foi feita.\n',encoding='utf-8')
        print('NO_SECRET')
        return
    voices=all_voices()
    print('VOICES',len(voices))
    rows=[]
    for i,v in enumerate(voices,1):
        gender=v['gender'].lower(); tag='M' if gender=='male' else 'F' if gender=='female' else 'U'
        fn=f"{i:03d}_{tag}_{safe(v['name'])}_{v['voice_id']}.mp3"
        text=f"{v['name']}. Vim para te ajudar, Fábio."
        ok=False; errs=[]; used=''
        for model in MODELS:
            for attempt in range(2):
                try:
                    raw=tts(v,text,model)
                    (OUT/fn).write_bytes(raw); used=model; ok=True; break
                except urllib.error.HTTPError as e:
                    body=e.read().decode('utf-8','replace')[:600]
                    errs.append(f'{model} HTTP {e.code}: {body}')
                    if e.code==429: time.sleep(3*(attempt+1))
                    else: break
                except Exception as e:
                    errs.append(f'{model}: {e}'); time.sleep(1.5*(attempt+1))
            if ok: break
        rows.append({**v,'order':i,'tag':tag,'status':'TTS_OK' if ok else 'TTS_FAIL','model':used,'sample':fn if ok else '','error':' || '.join(errs)[:1500]})
        print(f"{i:03d}/{len(voices):03d}", 'OK' if ok else 'FAIL', tag, v['name'], used)
    (OUT/'voice_catalog.json').write_text(json.dumps({'voices':rows},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    fields=['order','tag','voice_id','name','gender','accent','category','description','status','model','sample','error']
    with (OUT/'voice_catalog.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
    ok=sum(r['status']=='TTS_OK' for r in rows)
    (OUT/'STATUS.txt').write_text(f'VOICES_LISTED={len(rows)}\nTTS_OK={ok}\nTTS_FAIL={len(rows)-ok}\nORDER=male,unknown,female\nPHRASE=<NAME>. Vim para te ajudar, Fábio.\n',encoding='utf-8')
if __name__=='__main__': main()
