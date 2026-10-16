import re,sys,json,glob
S=sys.argv[1]; idx={r['eid']:r for r in json.load(open(S+'/event-index.json'))}
out=[]
for eid,r in idx.items():
    lines=[l.strip() for l in open(f"{S}/evtxt/{eid}.txt").read().split('\n')]
    for i,l in enumerate(lines):
        m=re.search(r'\[(http[^\]]*Vote\d+[^\]]*\.pdf)\]',l)
        if m:
            desc=lines[i-1]
            out.append(dict(eid=eid,date=r['date'],comm=r['comm'],event=r['title'],desc=desc,url=m.group(1)))
json.dump(out,open(S+'/votelinks.json','w'),indent=1)
print(len(out))
from collections import Counter
print(Counter((o['date'],o['comm'][:30]) for o in out))
