"""Extract amendments (sponsor, purpose, description, roll no.) from 118th BILLSTATUS files; flag Ukraine/Russia ones."""
import sys, glob, re, xml.etree.ElementTree as ET
K = re.compile(r'ukrain|russia|putin|nato|belarus|zelensk', re.I)
for f in sorted(glob.glob(sys.argv[1] + '/BILLSTATUS-118hr*.xml')):
    b = ET.parse(f).getroot().find('bill')
    for a in list(b.iter('amendment')):
        num = (a.findtext('type') or '') + ' ' + (a.findtext('number') or '')
        sp = a.find('sponsors/item'); spn = sp.findtext('fullName') if sp is not None else ''
        txt = ' '.join(filter(None, [a.findtext('purpose'), a.findtext('description')]))
        rolls = sorted(set(re.findall(r'Roll no\. (\d+)', ' '.join((x.findtext('text') or '') for x in a.iter('item')))))
        if K.search(txt):
            print(f.split('/')[-1], num, '|', spn, '| rolls', rolls, '|', txt[:400])
