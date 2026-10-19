"""Scan extracted 119th BILLSTATUS XML dirs for Russia/Ukraine measures; report House floor actions + L000600 cosponsorship."""
import sys, os, glob, re, xml.etree.ElementTree as ET
root = sys.argv[1]
K = re.compile(r'\b(russia\w*|ukrain\w*|putin|kremlin|belarus\w*|nato|zelensk\w*)\b', re.I)
for d in ['x-hr','x-hres','x-hjres','x-hconres']:
    for p in sorted(glob.glob(os.path.join(root, d, '*.xml'))):
        b = ET.parse(p).getroot().find('bill')
        titles = ' || '.join(t.findtext('title') or '' for t in b.iter('item') if t.find('titleType') is not None)
        title = b.findtext('title') or ''
        if not K.search(title + ' ' + titles): continue
        num = (b.findtext('type') or '') + ' ' + (b.findtext('number') or '')
        sp = b.find('sponsors/item'); spn = sp.findtext('fullName') if sp is not None else ''
        cos = [i.findtext('bioguideId') for i in b.findall('cosponsors/item')]
        lw = 'L000600' in cos
        acts = []
        for a in b.findall('actions/item'):
            t = a.findtext('text') or ''
            code = a.findtext('actionCode') or ''
            if re.search(r'passed|agreed to|failed|became public law|signed by president|roll no|record vote|motion to discharge|presented to', t, re.I) or code in ('8000','9000','17000','36000','E40000','E30000'):
                acts.append(f"{a.findtext('actionDate')}: {t[:160]}")
        laws = [l.findtext('number') for l in b.findall('laws/item')]
        if acts or lw:
            print(f"{num} | {title[:110]} | sp {spn} | {len(cos)} cos | LW cosponsor={lw} | laws={laws}")
            for x in acts[:8]: print('    ', x)
