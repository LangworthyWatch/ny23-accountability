import re,sys,json,html,urllib.request,urllib.parse,http.cookiejar
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders=[('User-Agent',UA)]
url="https://docs.house.gov/Committee/Calendar/ByMonth.aspx?Code="+sys.argv[2]
s=op.open(url).read().decode('utf-8','replace')
events={}
outdir=sys.argv[1]
for i in range(23):
    title=re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December) (\d{4})',re.sub(r'<[^>]+>',' ',s))
    ids=re.findall(r'ByEvent\.aspx\?EventID=(\d+)',s)
    # capture text near event links
    for m in re.finditer(r'<a[^>]*ByEvent\.aspx\?EventID=(\d+)[^>]*>(.*?)</a>',s,re.S):
        events.setdefault(m.group(1),html.unescape(re.sub(r'<[^>]+>|\s+',' ',m.group(2))).strip())
    print(title.group(0) if title else '?', len(set(ids)))
    open(f"{outdir}/{sys.argv[2]}-month-{i:02d}.html","w").write(s)
    f={}
    for n,v in re.findall(r'<input type="hidden" name="([^"]+)" id="[^"]*" value="([^"]*)"',s): f[n]=v
    f['__EVENTTARGET']='ctl00$MainContent$LinkButtonMonthPrevious'; f['__EVENTARGUMENT']=''
    s=op.open(url,urllib.parse.urlencode(f).encode()).read().decode('utf-8','replace')
json.dump(events,open(f"{outdir}/events-{sys.argv[2]}.json","w"),indent=1)
print(len(events))
