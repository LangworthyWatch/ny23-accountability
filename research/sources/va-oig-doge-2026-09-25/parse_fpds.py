import re,glob,csv,html
rows=[]
def g(e,tag,attr=None):
    m=re.search(r'<ns1:'+tag+r'([^>]*)>(.*?)</ns1:'+tag+'>',e,flags=re.S)
    if not m: return ''
    if attr:
        a=re.search(attr+r'="([^"]*)"',m.group(1)); return html.unescape(a.group(1)) if a else ''
    return html.unescape(m.group(2).strip())
seen=set()
for f in sorted(glob.glob('fpds_pages/*.xml')):
    t=open(f,errors='ignore').read()
    for e in re.findall(r'<entry>(.*?)</entry>',t,flags=re.S):
        piid=g(e,'PIID'); mod=g(e,'modNumber'); key=(piid,mod,g(e,'transactionNumber'))
        if key in seen: continue
        seen.add(key)
        pop=re.search(r'<ns1:placeOfPerformance>(.*?)</ns1:placeOfPerformance>',e,flags=re.S)
        pop=pop.group(1) if pop else ''
        rows.append(dict(
            piid=piid, mod=mod, signed=g(e,'signedDate')[:10], effective=g(e,'effectiveDate')[:10], completion=g(e,'ultimateCompletionDate')[:10],
            obligated=g(e,'obligatedAmount'), total_obligated=g(e,'totalObligatedAmount'), total_base_all=g(e,'totalBaseAndAllOptionsValue'),
            contracting_office=g(e,'contractingOfficeID','name'), funding_office=g(e,'fundingRequestingOfficeID','name'),
            pop_state=g(pop,'stateCode'), pop_city=g(pop,'placeOfPerformanceZIPCode','city'), pop_county=g(pop,'placeOfPerformanceZIPCode','county'), pop_zip=g(pop,'placeOfPerformanceZIPCode'),
            pop_cd=g(pop,'placeOfPerformanceCongressionalDistrict'),
            vendor=g(e,'vendorName'), vendor_state=g(e,'vendorLocation') and '', psc=g(e,'productOrServiceCode'), psc_desc=g(e,'productOrServiceCode','description'),
            naics=g(e,'principalNAICSCode'), naics_desc=g(e,'principalNAICSCode','description'), description=g(e,'descriptionOfContractRequirement'),
            initiative=g(e,'initiative','description'), action_type=g(e,'contractActionType','description')))
rows.sort(key=lambda r:r['signed'])
with open('fpds_va_t4c_2025-01-20_to_2026-04-30.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print('rows',len(rows))
import collections
print(collections.Counter(r['signed'][:7] for r in rows))
print(collections.Counter(r['initiative'] for r in rows).most_common(5))
ny=[r for r in rows if r['pop_state']=='NY' or 'NETWORK CONTRACT OFFICE 02' in r['contracting_office'] or 'NETWORK CONTRACT OFFICE 2 ' in r['contracting_office'] or re.search(r'BUFFALO|BATAVIA|BATH|CANANDAIGUA|SYRACUSE|ALBANY',r['funding_office']+r['contracting_office'])]
print('NY-linked rows',len(ny))
for r in ny:
    print(r['signed'],r['piid'],r['mod'],'|',r['contracting_office'],'|',r['funding_office'],'|',r['pop_city'],r['pop_county'],r['pop_state'],r['pop_zip'],'CD',r['pop_cd'],'|',r['vendor'],'|',r['psc_desc'][:50],'|',r['description'][:80],'|',r['obligated'],r['total_obligated'],'|',r['initiative'])
