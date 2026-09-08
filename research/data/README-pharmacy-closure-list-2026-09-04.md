# Pharmacy address list, NY, geocoded to 119th-Congress districts (Sept 4, 2026)

`pharmacy-closure-list-ny-2026-09-04-cd119.csv` — 74 New York addresses supplied by the user on Sept 4, 2026 (source list not yet identified in the file; add the originating document when known), run through the Census Bureau geocoder (`geocoding.geo.census.gov`, benchmark Public_AR_Current, vintage Current_Current) to obtain county and 119th-Congress district. 19 fall in NY-23.

Notes:
- Three addresses did not geocode (1000 Pennsylvania Ave, Elmira; 12208 NY-16, Yorkshire; 1604 Route 9, Wappingers Falls); their district is assigned from county alone, and the `method` column says so.
- NY-23 includes a sliver of Niagara County (Town of Pendleton and part of the Town of Lockport), confirmed by geocoding Pendleton town hall; 6616 Lincoln Ave, Lockport is CD 23. CLAUDE.md's eight-county list omits this sliver; use the district boundary for GIS work.
- The Erie County line splits nearby addresses: both Hamburg locations are NY-23, West Seneca and Buffalo are NY-26; Akron (Newstead) and Clarence are NY-23.
