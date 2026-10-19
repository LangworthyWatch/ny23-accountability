"""Second pass: re-verify UNVERIFIED rows by raw playback (id_), re-save undated ones slowly."""
import csv, re, time, urllib.request, os
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36'
P = os.path.dirname(os.path.abspath(__file__)) + '/../wayback/wayback-verified.tsv'
def fetch(u, t=120):
    r = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': UA}), timeout=t)
    return r.status, r.geturl(), r.read().decode('utf-8', 'replace')
rows = list(csv.reader(open(P), delimiter='\t')); hdr, rows = rows[0], rows[1:]
for r in rows:
    url, snap, status, expect, note = r
    if status == 'VERIFIED': continue
    m = re.search(r'/web/(\d{14})/', snap)
    if not m:
        try:
            st, final, body = fetch('https://web.archive.org/save/' + url, 180)
            m = re.search(r'/web/(\d{14})/', final)
        except Exception as e: r[4] = note + f' resave:{e}'
        time.sleep(20)
    if m:
        raw = f'https://web.archive.org/web/{m.group(1)}id_/{url}'
        try:
            st, final, body = fetch(raw)
            if st == 200 and expect.lower() in re.sub(r'\s+', ' ', body).lower():
                r[1] = f'https://web.archive.org/web/{m.group(1)}/{url}'; r[2] = 'VERIFIED'; r[4] = 'verified via id_ raw playback'
        except Exception as e: r[4] = note + f' raw:{e}'
    print(r, flush=True); time.sleep(15)
with open(P, 'w', newline='') as f:
    w = csv.writer(f, delimiter='\t'); w.writerow(hdr); w.writerows(rows)
