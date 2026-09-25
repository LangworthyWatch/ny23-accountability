import subprocess, sys, os, re, concurrent.futures as cf
Q='CONTRACTING_AGENCY_ID:3600 REASON_FOR_MODIFICATION:"F" SIGNED_DATE:[2025/01/20,2026/04/30]'
def fetch(start):
    out=f'fpds_pages/page_{start:06d}.xml'
    if os.path.exists(out) and os.path.getsize(out)>700: return start, out
    for attempt in range(4):
        r=subprocess.run(['curl','-s','-A','Mozilla/5.0','-G','https://www.fpds.gov/ezsearch/FEEDS/ATOM','--data-urlencode','FEEDNAME=PUBLIC','--data-urlencode','q='+Q,'--data-urlencode',f'start={start}','-o',out],capture_output=True)
        if os.path.exists(out) and os.path.getsize(out)>300: break
    return start, out
start=0; batch=50; total=0
while True:
    starts=list(range(start,start+batch*10,10))
    with cf.ThreadPoolExecutor(6) as ex: res=list(ex.map(fetch,starts))
    counts=[]
    for s,out in res:
        t=open(out,errors='ignore').read(); n=t.count('<entry>'); counts.append(n)
    total+=sum(counts); print('range',start,'->',start+batch*10,'entries',sum(counts),'cum',total,flush=True)
    if counts[-1]==0 and sum(counts[-5:])==0: break
    start+=batch*10
    if start>20000: break
print('DONE total',total)
