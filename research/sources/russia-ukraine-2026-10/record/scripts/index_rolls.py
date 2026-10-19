"""Index all downloaded roll calls -> rolls_index.csv with Langworthy (L000600) vote."""
import os, glob, csv, xml.etree.ElementTree as ET
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
rows = []
for p in sorted(glob.glob(os.path.join(B, 'clerk-all', '*', 'roll*.xml'))):
    r = ET.parse(p).getroot(); m = r.find('vote-metadata')
    g = lambda t: (m.findtext(t) or '').strip()
    lv = ''
    for rv in r.iter('recorded-vote'):
        l = rv.find('legislator')
        if l is not None and l.get('name-id') == 'L000600': lv = rv.findtext('vote'); break
    tot = m.find('vote-totals/totals-by-vote')
    rows.append(dict(year=p.split(os.sep)[-2], roll=g('rollcall-num'), date=g('action-date'), legis=g('legis-num'),
        question=g('vote-question'), desc=g('vote-desc'), amdt_num=g('amendment-num'), amdt_author=g('amendment-author'),
        result=g('vote-result'), yea=tot.findtext('yea-total') if tot is not None else '', nay=tot.findtext('nay-total') if tot is not None else '',
        langworthy=lv))
with open(os.path.join(B, 'rolls_index_2023_2026.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows))
