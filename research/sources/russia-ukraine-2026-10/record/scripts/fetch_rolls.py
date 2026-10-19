"""Download all House Clerk roll-call XMLs for given years into clerk-all/YYYY/rollNNN.xml."""
import sys, os, urllib.request, concurrent.futures as cf, time
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'clerk-all')
def get(y, n):
    p = os.path.join(BASE, str(y), f'roll{n:03d}.xml')
    if os.path.exists(p) and os.path.getsize(p) > 500: return (y, n, 'cached')
    url = f'https://clerk.house.gov/evs/{y}/roll{n:03d}.xml'
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 research'}), timeout=30) as r:
                b = r.read()
            if b'<rollcall-vote' not in b: return (y, n, 'missing')
            os.makedirs(os.path.dirname(p), exist_ok=True); open(p,'wb').write(b); return (y, n, 'ok')
        except urllib.error.HTTPError as e:
            if e.code == 404: return (y, n, '404')
            time.sleep(2)
        except Exception: time.sleep(2)
    return (y, n, 'fail')
for y, mx in [(int(a.split(':')[0]), int(a.split(':')[1])) for a in sys.argv[1:]]:
    with cf.ThreadPoolExecutor(8) as ex:
        res = list(ex.map(lambda n: get(y, n), range(1, mx+1)))
    from collections import Counter
    print(y, Counter(r[2] for r in res))
