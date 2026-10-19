"""Fetch every listed press release; save body text to press/text/<slug>.txt (title, date, url, body)."""
import re, urllib.request, os, time, html, json
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36'
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'press')
os.makedirs(B + '/text', exist_ok=True); os.makedirs(B + '/html', exist_ok=True)
items = json.load(open(B + '/items.json'))
for i in items:
    slug = i['path'].rsplit('/', 1)[-1]; fh = f'{B}/html/{slug}.html'
    if not os.path.exists(fh):
        try:
            open(fh, 'w').write(urllib.request.urlopen(urllib.request.Request('https://langworthy.house.gov' + i['path'], headers={'User-Agent': UA}), timeout=60).read().decode('utf-8', 'replace'))
        except Exception as e: print('fail', slug, e); continue
        time.sleep(0.4)
    s = open(fh).read()
    s2 = re.sub(r'<script.*?</script>|<style.*?</style>|<nav.*?</nav>|<header.*?</header>|<footer.*?</footer>', ' ', s, flags=re.S)
    m = re.search(r'<article.*?</article>', s2, re.S)
    body = m.group(0) if m else s2
    txt = html.unescape(re.sub(r'[ \t]+', ' ', re.sub(r'<(?:p|br|div|li|h\d)[^>]*>', '\n', body)))
    txt = re.sub(r'<[^>]+>', '', txt); txt = re.sub(r'\n\s*\n+', '\n\n', txt).strip()
    d = re.search(r'(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}', txt)
    i['date'] = d.group(0) if d else ''
    open(f'{B}/text/{slug}.txt', 'w').write(f"TITLE: {i['title']}\nDATE: {i['date']}\nURL: https://langworthy.house.gov{i['path']}\n\n{txt}\n")
json.dump(items, open(B + '/items.json', 'w'), indent=1); print('done', len(items))
