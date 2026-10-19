"""Save each target to Wayback (SPN), then verify by playback: snapshot fetch returns 200 and contains expected text."""
import sys, os, re, time, urllib.request, csv
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36'
B = os.path.dirname(os.path.abspath(__file__)) + '/../wayback'
def fetch(u, t=90):
    r = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': UA}), timeout=t)
    return r.status, r.geturl(), r.read().decode('utf-8', 'replace')
out = []
for line in open(B + '/targets.tsv'):
    url, expect = line.rstrip('\n').split('\t')
    snap = ''; note = ''
    try:
        st, final, body = fetch('https://web.archive.org/save/' + url, 180)
        m = re.search(r'/web/(\d{14})/', final)
        if m: snap = f'https://web.archive.org/web/{m.group(1)}/{url}'
    except Exception as e: note = f'save:{e}'
    if not snap: snap = f'https://web.archive.org/web/2026/{url}'
    time.sleep(5)
    ok = False
    for attempt in range(3):
        try:
            st, final, body = fetch(snap, 120)
            ok = st == 200 and expect.lower() in re.sub(r'\s+', ' ', body).lower()
            m = re.search(r'/web/(\d{14})', final)
            if m: snap = f'https://web.archive.org/web/{m.group(1)}/{url}'
            break
        except Exception as e: note += f' play:{e}'; time.sleep(10)
    out.append([url, snap, 'VERIFIED' if ok else 'UNVERIFIED', expect, note.strip()])
    print(out[-1], flush=True); time.sleep(5)
with open(B + '/wayback-verified.tsv', 'w', newline='') as f:
    w = csv.writer(f, delimiter='\t'); w.writerow(['url', 'snapshot', 'status', 'expected_text', 'note']); w.writerows(out)
