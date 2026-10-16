import re,sys,urllib.request,urllib.parse,http.cookiejar
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders=[('User-Agent',UA)]
url="https://docs.house.gov/Committee/Committees.aspx"
s=op.open(url).read().decode('utf-8','replace')
f={}
for n,v in re.findall(r'<input type="hidden" name="([^"]+)" id="[^"]*" value="([^"]*)"',s): f[n]=v
f['__EVENTTARGET']='ctl00$MainContent$DropDownListCommittees'
f['ctl00$MainContent$DropDownListCommittees']='IF00'
r=op.open(url,urllib.parse.urlencode(f).encode())
out=r.read().decode('utf-8','replace'); print(r.geturl(),len(out))
open(sys.argv[1],'w').write(out)
