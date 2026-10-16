import re,sys,json,glob,time,urllib.request,os
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
S=sys.argv[1]; out=sys.argv[2]; os.makedirs(out,exist_ok=True)
ids={}
for f in glob.glob(S+'/months/events-*.json'):
    c=f.split('-')[-1][:4]
    for k in json.load(open(f)): ids[k]=c
for eid,c in sorted(ids.items()):
    p=f"{out}/event-{eid}.html"
    if os.path.exists(p): continue
    req=urllib.request.Request(f"https://docs.house.gov/Committee/Calendar/ByEvent.aspx?EventID={eid}",headers={'User-Agent':UA})
    try: s=urllib.request.urlopen(req,timeout=60).read().decode('utf-8','replace')
    except Exception as e: print(eid,e); continue
    open(p,'w').write(s); time.sleep(0.5)
print(len(ids))
