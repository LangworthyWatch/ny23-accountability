# Term tracker baseline (Nov 11, 2026)
- `bipartisan_baseline.py <bulk-dir> <refresh-dir>`: H.R. bills only, from govinfo BILLSTATUS; withdrawn cosponsorships excluded; a bill's own title is the `<title>` immediately before `<titles>`.
- Bulk from Oct 16, 2026 (`../sources/ec-record-2026-10/bills/bulk/x-hr`, 10,833 files), plus 1,507 files new or changed since then (`billstatus-refresh-2026-11-11/`, from the govinfo JSON listing by lastModified).
- Result: he sponsored 42 bills; 28 have at least one Democratic cosponsor; 24 have a Democratic original cosponsor; none became law. He has cosponsored 297 bills, 58 of them Democrat-sponsored (19.5%), 17 of those as an original cosponsor. Detail is in bipartisan_baseline.txt and .json.
- The quotes on the page were checked against the audio of the campaign-page clips (camp-wivb-mandate.txt, camp-weny-aisle.txt in ../sources/triage-2026-11-11/videos/, posted Nov 5, 2026, uploader 100063640063617).
