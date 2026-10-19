"""Fetch langworthy.house.gov press-release listing pages; collect (date,title,path)."""
import re, urllib.request, os, time, html, json, sys
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36'
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'press', 'listing')
os.makedirs(D, exist_ok=True)
def get(u): return urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': UA}), timeout=60).read().decode('utf-8', 'replace')
items = []
for p in range(0, 80):
    f = f'{D}/list-{p:02d}.html'
    if not os.path.exists(f):
        try: open(f, 'w').write(get(f'https://langworthy.house.gov/media/press-releases?page={p}'))
        except Exception as e: print('fail', p, e); break
        time.sleep(0.5)
    s = open(f).read()
    found = 0
    for m in re.finditer(r'<a[^>]+href="(/media/press-releases/[^"?#]+)"[^>]*>(.*?)</a>', s, re.S):
        path, t = m.group(1), html.unescape(re.sub(r'<[^>]+>|\s+', ' ', m.group(2))).strip()
        if t and path not in [i['path'] for i in items]: items.append({'path': path, 'title': t, 'page': p}); found += 1
    dates = re.findall(r'(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, (\d{4})', re.sub(r'<[^>]+>', ' ', s))
    if found == 0 or (dates and all(d < '2023' for d in dates)): print('stop at', p, found, dates[-1:] if dates else ''); break
json.dump(items, open(f'{D}/../items.json', 'w'), indent=1); print(len(items), 'items')
