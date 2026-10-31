# FEC update, compiled 2026-10-31 (since the Oct 16 "who funds him" entry, which ran through Sept 30)

Source files: raw electronic filings from docquery.fec.gov/dcdev/posted/{id}.fec, parsed with the
scratch parser (field positions verified by dumping indexed rows; F65 amount at [17], SA amount at
[20], SA purpose at [22]; conduit memo rows identified as SA11AI rows with no last name). OpenFEC
(DEMO_KEY) used only for the filings list and committee IDs; its schedule_a index had not yet
processed the October filings on this date (0 rows returned; positive control: filings list OK).
ZIP-to-district: Census tab20_cd11920_zcta520_st36.txt (cols 1 and 8), same method as the Q3 entry.

## Langworthy for Congress (C00817932)
Pre-general F3, file 2035999, filed Oct 22, covers Oct 1-14, 2026:
- receipts $53,220.25; disbursements $597,785.48; cash on hand Oct 14 $1,994,176.70 (Sept 30: $2,563,741.93)
- individuals $26,220.25 (itemized $25,700.00, unitemized $520.25); party $1,000; PACs $26,000
- of the $25,700 itemized, $17,350 (67.5%) arrived earmarked through AIPAC's PAC (18 rows, $17,350
  less RJC $250 and WinRed $500 = AIPAC $16,600 by purpose text; conduit memo rows AIPAC 18, RJC 1,
  WinRed 1). Donor ZIPs: NY-23 entirely $1,750 (6.8%), NY-23 split $5,100 (19.8%), NY other
  district $18,850 (73.3%), out of state $0. Matthew Cherry $3,500 reattributed (-$3,500) to Danielle Cherry.
- PACs: AICPA $5,000; SpaceX PAC $5,000; UPS PAC $5,000; BASF $2,500; Barona Band of Mission Indians
  $2,500; AbbVie, American Supply Assn, Lyondell, Meat Institute, NRA Victory Fund, Vertex $1,000 each
- spending: Strategic Media Placement Inc. (Delaware, OH) $551,000 "MEDIA BUY" Oct 9; Nassau County
  Republican Committee $25,000 "POLITICAL CONTRIBUTION" Oct 9; IFA Holdings LLC (Arlington, VA)
  $22,900 survey research Oct 2; Capelianis Consulting $10,000; D&D Printing $6,081.66
- cycle through Oct 14 (F3 cols 59-72): receipts $2,616,962.18 (OpenFEC totals say $2,675,792.78 incl.
  other receipts); total contributions $2,301,824.09; individuals $1,055,235.44 (itemized $977,878.96);
  PACs $1,239,026.65 = 53.8% of contributions; disbursements $622,785.48 this period, cycle operating
  $1,649,085.50

48-hour notices (F6) Oct 15-29, nine filings (2028285, 2029171, 2034981, 2040605, 2041130, 2041550,
2042927, 2044078, 2044669), 45 rows, no duplicates: $79,500.00
- individuals $37,500 (24): NY-23 entirely $3,500 (Olson, Lakewood $2,500; Tuber, Hamburg $1,000);
  NY-23 split $2,500 (Crane, Elma); NY other district $19,000 (mostly Westchester, Rochester);
  out of state $12,500. Self-described lobbyists $5,500 (Redl/Salt Point $3,000; Nichols $1,500;
  Pickering/Mehlman $1,000). Two "INFORMATION REQUESTED" (Wright $1,000, McWane $3,500).
- committees/orgs $42,000 (21): COLEPAC $5,000; LPL Financial PAC $5,000; American Chemistry Council
  $4,000; Seneca Nation of Indians $3,500; Cement PAC, Heidelberg Materials, Morgan Stanley,
  Republican Italian American Committee $2,500 each; ICBA $2,000; Phillips Lytle LLP $1,500;
  $1,000 each: APCIA, Assn for Accessible Medicines, State Farm, FishPAC, Mike Ranzenhofer for
  State Senate, Florio Perrucci (law firm), Pharmavite, EggPAC, SoyPAC, AGC, GSK

## Aaron Gies for Congress (C00910125), H6NY23559
Pre-general F3, file 2037600, Oct 1-14: receipts $94,066.32; disbursements $270,790.07; COH $54,077.18.
Individuals $85,316.32 (itemized $63,657; unitemized $21,659.32); PACs $8,750 (all local Democratic
committees + two small PACs). Itemized donor ZIPs: NY-23 entirely 84.9%, split 2.6%, NY other 5.1%,
out of state 7.4%. Spending: Parkside Group mailers $137,986.72 + door hangers $5,022; Balduzzi Group
advertising $87,500; Meta $7,200. Cycle: contributions $706,396.31; individuals $682,646.31; PACs $23,750.
48-hour notices: 2033428, 2037644 (re-files the same six rows), 2042312; deduped by (date, amount, name)
= 10 rows, $20,910 (incl. AFT $5,000, Allegany County Matters $3,000).

## Comparisons (Oct 1-14)
Raised: Gies $94,066 vs Langworthy $53,220. Spent: Langworthy $597,785 vs Gies $270,790.
Cash on hand Oct 14: $1,994,177 vs $54,077 (36.9 to 1). Cycle contributions: $2.30M vs $0.71M.
PAC share of cycle contributions: 53.8% vs 3.4%. In-district share of itemized individual money this
period: Langworthy 26.7% (entirely+split), Gies 87.5%.

Files: filings.json, totals.json, gies-*.json, *.fec, parse-langworthy.txt, parse-gies.txt
