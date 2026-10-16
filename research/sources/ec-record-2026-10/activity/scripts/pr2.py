import re,urllib.request,os,time,html,json
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36'
items=json.load(open('pr/items.json'))
out=[]
for it in items:
    slug=it['path'].split('/')[-1]; f=f'pr/{slug}.html'
    if not os.path.exists(f):
        try: open(f,'w').write(urllib.request.urlopen(urllib.request.Request('https://langworthy.house.gov'+it['path'],headers={'User-Agent':UA}),timeout=60).read().decode('utf-8','replace'))
        except Exception as e: print(slug,e); continue
        time.sleep(0.4)
    s=open(f).read()
    t=html.unescape(re.sub(r'<[^>]+>','\n',re.sub(r'<(script|style|nav|header|footer).*?</\1>','',s,flags=re.S))); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    title=html.unescape(re.search(r'<title>(.*?)</title>',s,re.S).group(1)).split('|')[0].strip()
    m=re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}',t)
    date=m.group(0) if m else ''
    i=t.find(title[:40]); body=t[i:] if i>=0 else t
    j=body.find('###'); body=body[:j] if j>0 else body[:8000]
    ec=bool(re.search(r'Energy (and|&) Commerce|E&C\b|Energy Subcommittee|Health Subcommittee|Environment Subcommittee',body))
    open(f'pr/{slug}.txt','w').write(f"URL: https://langworthy.house.gov{it['path']}\nTITLE: {title}\nDATE: {date}\n\n{body}")
    out.append(dict(slug=slug,url='https://langworthy.house.gov'+it['path'],title=title,date=date,ec=ec))
json.dump(out,open('pr/index.json','w'),indent=1)
import datetime
for o in out:
    if o['ec']: print(o['date'],'|',o['title'][:120])
print(len(out), sum(o['ec'] for o in out), 'earliest', out[-1]['date'])
