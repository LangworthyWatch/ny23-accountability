import re,sys,json,csv
S=sys.argv[1]; outcsv=sys.argv[2]
links=json.load(open(S+'/votelinks.json'))
rows=[]
for o in links:
    fn=o['url'].split('/')[-1][:-4]
    t=open(f"{S}/votepdf/{fn}.txt",errors='replace').read()
    lines=t.split('\n')
    g=lambda p: (re.search(p,t,re.S) or [None,''])[1]
    rc=g(r'ROLL CALL VOTE #\s*(\d+)')
    bill=re.sub(r'\s+',' ',g(r'BILL:\s*(.*?)\n\s*\n'))
    amd=re.sub(r'\s+',' ',g(r'AMENDMENT:\s*(.*?)\n\s*\n'))
    disp=re.sub(r'\s+',' ',g(r'DISPOSITION:\s*(.*?)\n\s*\n'))
    hdr=[l for l in lines if 'REPRESENTATIVE' in l and 'YEAS' in l]
    vote='NOT LISTED' if 'ROLL CALL VOTE' in t else ('NOT A ROLL CALL (summary/amendment doc)' if t.strip() else 'NO TEXT (scanned PDF)')
    if hdr:
        h=hdr[0]; y=h.find('YEAS'); n=h.find('NAYS'); p=h.find('PRESENT'); rs=h.find('REPRESENTATIVE',p)
        for l in lines[lines.index(h)+1:]:
            if re.search(r'\bLangworthy\b',l):
                k=l.find('Langworthy'); seg_end=rs if rs>0 else len(l)
                if k>seg_end-5:  # on right side (unexpected)
                    vote='RIGHTSIDE?'; break
                xs=[m.start() for m in re.finditer(r'\bX\b',l[:seg_end])]
                if not xs: vote='Not voting'
                else:
                    x=xs[0]; d={'Yea':abs(x-y-1),'Nay':abs(x-n-1),'Present':abs(x-p-3)}
                    vote=min(d,key=d.get)
                break
        else:
            if vote=='NOT LISTED': vote='Not on roster (not a member of this panel)'
    yeas=g(r'(\d+) yeas'); nays=g(r'(\d+) nays')
    rows.append(dict(date=o['date'],committee=o['comm'],event_id=o['eid'],rollcall=rc,docs_house_desc=o['desc'],bill=bill,amendment=amd,disposition=disp,yeas=yeas,nays=nays,langworthy=vote,pdf=o['url']))
with open(outcsv,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
from collections import Counter
print(Counter(r['langworthy'] for r in rows))
print(Counter((r['committee'][:35],r['langworthy']) for r in rows))
