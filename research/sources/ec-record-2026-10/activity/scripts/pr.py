import re,urllib.request,os,time,html,json
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36'
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60).read().decode('utf-8','replace')
os.makedirs('pr',exist_ok=True)
items=[]
for p in range(0,46):
    f=f'pr/list-{p:02d}.html'
    if not os.path.exists(f): open(f,'w').write(get(f'https://langworthy.house.gov/media/press-releases?page={p}')); time.sleep(0.4)
    s=open(f).read()
    for m in re.finditer(r'href="(/media/press-releases/[^"]+)"',s): 
        if m.group(1) not in [i['path'] for i in items]: items.append({'path':m.group(1),'page':p})
    dates=re.findall(r'(\d{1,2}/\d{1,2}/\d{4}|(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4})',re.sub(r'<[^>]+>',' ',s))
    if dates and any(d.endswith('2024') for d in dates[-3:]): print('reached 2024 at page',p); break
json.dump(items,open('pr/items.json','w'),indent=1); print(len(items))
