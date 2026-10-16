import json,urllib.request,os,time,re,html,sys
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36'
pk=[];mark='*'
while True:
    body=json.dumps({"query":"collection:(CHRG) AND congress:119 AND Langworthy","pageSize":100,"offsetMark":mark}).encode()
    d=json.load(urllib.request.urlopen(urllib.request.Request("https://api.govinfo.gov/search?api_key=DEMO_KEY",data=body,headers={'Content-Type':'application/json'}),timeout=60))
    pk+= [(r['packageId'],r.get('dateIssued'),r['title']) for r in d['results']]
    if not d['results'] or d.get('offsetMark') in (None,mark): break
    mark=d['offsetMark']
    if len(pk)>=d['count']: break
print(len(pk))
os.makedirs('chrg',exist_ok=True)
out=[]
for p,dt,ti in pk:
    f=f'chrg/{p}.htm'
    if not os.path.exists(f):
        try: open(f,'wb').write(urllib.request.urlopen(urllib.request.Request(f'https://www.govinfo.gov/content/pkg/{p}/html/{p}.htm',headers={'User-Agent':UA}),timeout=90).read())
        except Exception as e: print(p,e); continue
        time.sleep(0.3)
    t=html.unescape(open(f,errors='replace').read())
    ec='COMMITTEE ON ENERGY AND COMMERCE' in t[:6000].upper()
    turns=len(re.findall(r'\n\s*Mr\. Langworthy\. ',t))
    recog=len(re.findall(r'recognize[s]?\s+(?:the gentleman from New York,\s+)?Mr\. Langworthy',t))
    sub=re.search(r'SUBCOMMITTEE ON ([A-Z ,]+)',t[:6000])
    out.append(dict(pkg=p,date=dt,title=ti,ec=ec,subcommittee=sub.group(1).strip() if sub else 'FULL COMMITTEE',langworthy_speaker_turns=turns,chair_recognitions=recog))
json.dump(out,open('chrg-index.json','w'),indent=1)
for o in sorted(out,key=lambda o:o['date']):
    if o['ec']: print(o['date'],o['pkg'],o['subcommittee'][:30],'turns',o['langworthy_speaker_turns'],'recog',o['chair_recognitions'],'|',o['title'][:70])
