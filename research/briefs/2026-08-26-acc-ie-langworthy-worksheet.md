# Worksheet: ACC independent expenditure + H.R. 7502 (pulled 2026-08-26)

## FEC Schedule E, verified via OpenFEC API
Committee C90011578, AMERICAN CHEMISTRY COUNCIL, INC — "Independent expenditure filer (not a committee)", Washington DC, Form 5.

Langworthy row: $95,900 | expenditure_date 2026-08-21 | support (S) | payee ORANGE AGENCY |
description "STREAMING BROADCAST" | category "Advertising Expenses" | file_number 2009256 |
transaction_id F57.000003 | amendment_indicator N | sub_id 4082120261584450029 |
image https://docquery.fec.gov/cgi-bin/fecimg/?202608219903376915

## ACC's complete 2026-cycle IE program (deduplicated)
Raw API returns duplicate rows for Palmer and Guthrie (x2 each); deduplicating by
(candidate, date, amount) yields six unique expenditures summing to EXACTLY $1,000,000.00,
which is itself corroboration that the dedupe is correct. Do NOT cite the raw sum.

| Candidate | Amount | Date | Committee role (House Clerk MemberData.xml, pub. July 6 2026) |
|---|---|---|---|
| Husted, Jon (R-OH) | $385,242 | 2026-08-21 | U.S. Senator |
| Sullivan, Dan (R-AK) | $219,476 | 2026-08-06 | U.S. Senator |
| Palmer, Gary (R-AL-6) | $131,018 | 2026-05-05 | E&C (IF00); subs IF02, IF03, IF18 |
| Langworthy, Nick (R-NY-23) | $95,900 | 2026-08-21 | E&C (IF00); subs IF03 Energy, IF14 Health, IF18 Environment; also Oversight + Rules |
| Evans, Gabe (R-CO-8) | $88,088 | 2026-08-21 | E&C (IF00); subs IF03, IF17 Commerce/Manufacturing/Trade, IF18 |
| Guthrie, Brett (R-KY-2) | $80,276 | 2026-05-05 | **E&C CHAIR** |
| **TOTAL** | **$1,000,000.00** | | All four House recipients sit on Energy and Commerce |

Three of the six ($385,242 + $95,900 + $88,088) are dated 2026-08-21, the same day ACC
issued its press release announcing the Langworthy ad.

## H.R. 7502, Recycled Materials Attribution Act of 2026
Sponsor Langworthy. Introduced 2026-02-11. 12 cosponsors (7 R, 5 D). Referred to House
Energy and Commerce. No further action as of 2026-08-26.
Sections: 1 short title; 2 definitions; **3 Recognition of mass balance accounting for
recycled content claims**; 4 recycled content claims; 5 enforcement by FTC; 6 preemption;
7 savings provision. Text mentions "mass balance" 10x, "Green Guides" 2x, FTC 6x.
Contains NO instance of "advanced recycling", "chemical recycling", or "pyrolysis".

## Accuracy guardrails for the entry
- Independent expenditures are legally independent. No evidence of coordination exists or
  is alleged. State this explicitly.
- The bill is bipartisan (7R/5D) and recycled-content labeling confusion is a real problem
  that consumer advocates also want solved. Concede this early.
- Langworthy is NOT on IF17 (Commerce, Manufacturing and Trade), the subcommittee that
  handles FTC matters. Evans is. Do not imply he sits on the subcommittee of jurisdiction.
- The $600K Chautauqua Lake claim from the Aug 7 luncheon was correctly hedged
  ("advancing", "working to bring") — pending, not secured. Record as a NON-instance of
  the credit-claiming pattern.
- Energy Choice Act "157 cosponsors including three Democrats" (Aug 7) verified TRUE:
  govinfo BILLSTATUS shows 157 (154 R, 3 D: Gonzalez TX-34, Gray CA-13, Golden ME-2).

## The raw FEC Form 5 (primary document, saved locally)
`research/sources/fec-f5-acc-langworthy-2026-08-21.fec`
Retrieved from https://docquery.fec.gov/dcdev/posted/2009256.fec (the docquery PDF/image
endpoints 403 to non-browser clients; the .fec source file does not).

Header: F5N | C90011578 | "AMERICAN CHEMISTRY COUNCIL, INC" | 655 New York Ave, NW,
Washington DC 20001 | coverage 2026-08-21 through 2026-09-03 | filing total $569,230.00 |
signed Lubin, Aimee, 2026-08-21.

All three line items are to the same vendor, Orange Agency, 107 S. West Street #506,
Alexandria VA 22314, all dated 2026-08-21, all purpose code 004, all "S" (support):

| Txn | Candidate | Office | Amount | Description |
|---|---|---|---|---|
| F57.000001 | Husted, Jon | S-OH | $385,242 | "Streaming, Digital, Broadcast" |
| F57.000002 | Evans, Gabe | H-CO08 | $88,088 | "Streaming, Digital, Broadcast" |
| F57.000003 | Langworthy, Nick | H-NY23 | $95,900 | "Streaming, Broadcast" |
| | | | **$569,230** | single filing total |

The remaining $430,770 of the $1,000,000 program is the earlier Palmer, Guthrie
(both 2026-05-05) and Sullivan (2026-08-06) expenditures, filed separately.
