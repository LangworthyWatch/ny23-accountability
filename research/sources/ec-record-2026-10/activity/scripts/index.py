import re,sys,glob,os,json,subprocess
S=sys.argv[1]
rows=[]
for f in sorted(glob.glob(S+'/events/*.html')):
    eid=re.search(r'event-(\d+)',f).group(1)
    s=open(f).read()
    t=re.sub(r'<(script|style).*?</\1>','',s,flags=re.S); t=re.sub(r'<a[^>]*href="([^"]+)"[^>]*>',r' [\1] ',t); t=re.sub(r'<[^>]+>','\n',t); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    i=t.find('JavaScript is required'); t=t[i:]
    open(f"{S}/evtxt/{eid}.txt","w").write(t)
    lines=[l.strip() for l in t.split('\n') if l.strip()]
    kind=lines[2] if len(lines)>2 else ''
    title=lines[3] if len(lines)>3 else ''
    m=re.search(r'(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday), (\w+ \d+, \d{4})',t)
    date=m.group(2) if m else ''
    comm=lines[4] if len(lines)>4 else ''
    rows.append(dict(eid=eid,kind=kind,title=title,comm=comm,date=date,votes=len(re.findall(r'(?i)vote',t)),lang=len(re.findall(r'(?i)langworthy|L000600',t))))
json.dump(rows,open(S+'/event-index.json','w'),indent=1)
for r in rows: print(r['eid'],r['date'],'|',r['kind'][:40],'|',r['title'][:70],'|',r['comm'][:40],'| v',r['votes'],'L',r['lang'])
