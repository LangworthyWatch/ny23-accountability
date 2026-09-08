# Pharmacy address list, NY, geocoded to 119th-Congress districts (Sept 4, 2026)

`pharmacy-closure-list-ny-2026-09-04-cd119.csv` — 74 New York addresses from WGRZ, "Rite Aid closing list nears 500 locations: See full list of stores set to close" (2025; https://www.wgrz.com/article/news/nation-world/rite-aid-closing-list-full-list-of-locations-2025/507-0cf47398-3d82-46c4-89c4-55e37ede9c56), retained as `wgrz-rite-aid-closing-list-2025.pdf` (browser save, Sept 4, 2026) with extracted text alongside, run through the Census Bureau geocoder (`geocoding.geo.census.gov`, benchmark Public_AR_Current, vintage Current_Current) to obtain county and 119th-Congress district. 19 fall in NY-23.

Notes:
- Three addresses did not geocode (1000 Pennsylvania Ave, Elmira; 12208 NY-16, Yorkshire; 1604 Route 9, Wappingers Falls); their district is assigned from county alone, and the `method` column says so.
- NY-23 includes a sliver of Niagara County (Town of Pendleton and part of the Town of Lockport), confirmed by geocoding Pendleton town hall; 6616 Lincoln Ave, Lockport is CD 23. CLAUDE.md's eight-county list omits this sliver; use the district boundary for GIS work.
- The Erie County line splits nearby addresses: both Hamburg locations are NY-23, West Seneca and Buffalo are NY-26; Akron (Newstead) and Clarence are NY-23.

Source retention: WGRZ and its TEGNA sister sites block automated retrieval (403) and Wayback would not capture the page (520); the PDF in this folder is the retained copy.

## Bankruptcy docket note (Sept 8, 2026)

The 154-store exhibit reviewed from screenshots on Sept 8 is the **Initial Closing Stores** list attached to the **Interim Order authorizing store closing sales, Doc 121, filed Oct 17, 2023, In re Rite Aid Corporation, Case No. 23-18993 (MBK), Bankr. D.N.J.** — i.e., the **first** (2023) Rite Aid Chapter 11, not the May 2025 case the WGRZ list tracks. Its New York rows are Brooklyn (2), Floral Park, Flushing, Levittown, Oceanside, Valley Stream, Bay Shore, Bellmore, Copiague, East Northport, Huntington Station, Medford, Oyster Bay, West Patchogue, Port Jefferson Station, Smithtown, plus 2887 Harlem Rd Cheektowaga (NY-26), 2453 Elmwood Ave Kenmore (NY-26), and 1567 Penfield Rd Rochester (NY-25). **Zero NY-23 stores in this initial wave.** Screenshots only; the exhibit PDF has not been retained.

Implication for the pharmacy-desert layer: NY-23 Rite Aid losses span two cases — later closing notices in 23-18993 (2023–24 waves) and the full wind-down in the 2025 case — so the docket route requires the union of every closing schedule from both. The NYSED licensed-pharmacy registry diff remains the simpler base layer; docket schedules are for labeling and dating the Rite Aid subset.
