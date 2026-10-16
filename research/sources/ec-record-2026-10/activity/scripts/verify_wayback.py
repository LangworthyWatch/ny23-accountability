import sys,subprocess,urllib.request,re,tempfile,os
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36'
for line in open(sys.argv[1]):
    parts=line.strip().split('|')
    if len(parts)<3 or not parts[2]: print('NO-SNAPSHOT',parts[0]); continue
    u,k,snap=parts
    import time; time.sleep(20)
    raw=re.sub(r'/web/(\d+)/',r'/web/\1id_/',snap)
    try:
        r=urllib.request.urlopen(urllib.request.Request(raw,headers={'User-Agent':UA}),timeout=120); d=r.read(); code=r.status
    except Exception as e: print('FAIL',snap,e); continue
    if d[:4]==b'%PDF':
        f=tempfile.NamedTemporaryFile(suffix='.pdf',delete=False); f.write(d); f.close()
        txt=subprocess.run(['pdftotext',f.name,'-'],capture_output=True,text=True).stdout
        if len(txt.split())<30:
            subprocess.run(['pdftoppm','-r','200','-png','-f','1','-l','2',f.name,f.name],capture_output=True)
            import glob
            txt=''.join(subprocess.run(['tesseract',p,'stdout'],capture_output=True,text=True).stdout for p in sorted(glob.glob(f.name+'*.png')))
    else: txt=d.decode('utf-8','replace')
    ok=code==200 and k.lower() in txt.lower()
    print('VERIFIED' if ok else 'UNVERIFIED',code,snap,'|',k)
