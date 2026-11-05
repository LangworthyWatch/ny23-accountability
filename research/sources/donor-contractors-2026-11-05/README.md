# Donors and federal health programs (compiled Nov 5, 2026)

Question (user, Nov 5): how many of his donors receive federal contracts? Scoped first to the health sector.

## Inputs
- PAC receipts 2025-26: ../fec-2026-q3/cycle-2026-committee-donors.txt (LfC C00817932 + Circle the Wagons C00827881, non-memo SA11B/C, through Q3 2026 / M9). 359 rows, $1,276,689.
- PAC receipts 2024 and 2022: prior_cycle_pac_receipts.json (OpenFEC schedule_a, contributor_type=committee, DEMO_KEY; 2024 = both committees; 2022 = LfC). Line 11 non-memo rows used.
- Sponsor names/types: FEC committee master files bulk/cm.txt (2026), bulk/cm24/cm.txt, bulk/cm22/cm.txt (field 13 CONNECTED_ORG_NAME, field 12 ORG_TP: C corporate, L labor, M membership, T trade, V coop, W corp w/o stock).
- Individual donors' employers 2025-26: employers_cycle2026.json (SA11AI rows, LfC only, memo rows excluded, 680 rows, $687,983 itemized).
- Federal awards: USAspending API, spending_by_category/recipient, FY2023-FY2026 (2022-10-01..2026-09-30), contracts A/B/C/D and grants 02-05; family sums by name token in health_sponsors_usaspending_family.json (manual review needed; see false-positive notes below). The recipient_parent_duns category does not exist (404).
- NY Medicaid managed care enrollment, Sept 2026: nydoh-mmc-enrollment-2026-09.xlsx (NYS DOH monthly report).
- His assignments: clerk-MemberData.xml (GO00 Oversight full committee, no subcommittee; IF00 E&C with IF03 Energy, IF14 Health, IF18 Environment; RU00 Rules, chair RU02 Legislative and Budget Process).
- House Rules 119th: house-rules-119.pdf/.txt (Rule X cl.1(n)(6) "including Federal procurement"; cl.4(c)(2) "may at any time conduct investigations of any matter").
- Oversight PBM report July 23, 2024: oversight-pbm-report-2024-07.pdf, release oversight-pbm-release-2024-07-23.html.
- PBM votes: H.R. 5378 Roll 708 Dec 11, 2023 Yea (320-71); H.R. 10545 Roll 517 Dec 20, 2024 Yea (366-34); H.R. 7148 Roll 53 Feb 3, 2026 Yea (concur, 196-21?) -- NOTE roll 53 totals printed yea 196 nay 21: re-verify totals before citing. BILLSTATUS-118hr5378.xml, -118hr10545.xml, -119hr7148.xml retained. E&C chairman release on PBM enactment: ec-guthrie-pbm-signed-2026.html.
- His press releases Apr 2025-Sep 2026 (149, ../ec-record-2026-10/activity/press-releases): PBM mentions in 3 (CHECK Act Jun 3, 2026; American Relief Act Dec 20, 2024; Springville Jul 11, 2025). Zero mentions: Medicare Advantage, UnitedHealth, Elevance, Centene, Fidelis, Maximus, dialysis.

## Pilot results
- pilot_pacs_usaspending.json: naive name match, many false positives (Koch->Heckler & Koch, BofA->TD Bank, Corning->Corning Powersports, AIPAC->Israel Aerospace). Not publishable.
- pilot_pacs2_sponsor_usaspending.json: sponsor-name match. 128 corporate-sponsored PACs $418,500; 65 token-matched to a contract recipient $233,000.
- health_pac_rows_2024_2026.json: one regex, both cycles. 2026: 63 contributions $193,000 = 15.1% of PAC money. 2024: 55 contributions $85,250 = 9.5%. Pharma/device corporate $5,500 -> $62,000; insurers/program contractors $25,250 -> $44,000; provider/trade/member assns $54,500 -> $87,000. New in 2026: Amgen, Pfizer, Biogen, DaVita, Labcorp, AstraZeneca, Edwards, Lilly, Alnylam, BioMarin, BMS, Genentech.
- Family contract totals (health_sponsors_usaspending_family.json), reviewed: Optum Public Sector $81.3B (UnitedHealth; TRICARE), Health Net Federal Services $8.57B (Centene; TRICARE), Maximus $6.0B, McKesson $44.9B, Pfizer $1.83B, Wellpoint Federal Solutions $1.01B (Elevance), DaVita $965M, Novitas $912M + First Coast $266M (GuideWell MACs), Siemens Medical $901M, Abbott $793M, Amgen $560M, Roche $496M, Labcorp $447M + $8M, Merck $197M, Genentech $139M, Edwards $108M, US Renal Care $96M. FALSE POSITIVES to ignore: Highmark Marine/Erectors, Anthem Surgical/Air, Bayer Construction, Fidelis Sustainability/-BBD. Zero in USAspending (state Medicaid contracts, not federal awards): MVP, Molina, Highmark health, Centene parent, BCBSA.

## Final figures used in the entry (2026-11-05-health-industry-money-committee-seat)
- Health PAC money by cycle (one regex, see health_pac_rows_2024_2026.json + 2022 from prior_cycle_pac_receipts.json with cm22): 2022 $6,000/203,224 = 3.0%; 2024 $85,250/895,436 = 9.5%; 2026 $193,000/1,276,689 = 15.1%. Pharma/device C-type: 0 / 5,500 / 62,000. Insurers+program contractors: 1,000 / 25,250 / 44,000. Assns: 5,000 / 54,500 / 87,000. SIEMENS excluded from the health regex (ambiguous sponsor).
- Per-parent PAC $ 2024/2026: Centene 1,000/1,000; UnitedHealth 10,000/6,000; Highmark 2,250/3,000 (2022 1,000); Molina 0/2,000; MVP 4,000/7,000; Elevance 3,500/10,000; BCBSA 2,000/5,500; Maximus 0/1,000; GuideWell 0/1,000.
- NY DOH Sept 2026 Table IIa, eight counties (county label forward-filled; Erie whole-county): total 259,558; Fidelis 123,120; Independent Health 60,653; Highmark WNY 33,926; Molina 26,428; UnitedHealthcare 9,622; Excellus 5,809. Donor-parent plans 193,096 = 74.4%. Outside Erie 87,512, all donor-parent plans (Fidelis 68,579, Highmark 9,893, Molina 5,546, UHC 3,494). nydoh-mmc-ny23-sept2026.json.
- Roll calls (Clerk XML via browser): 708/2023 Yea, 320-71; 517/2024 Yea, 366-34; 53/2026 Yea, 217-214 (concur in Senate amendments). First-match <yea-total> in the XML is a party subtotal; use <totals-by-vote>.
- E&C appointment release Dec 13, 2024 retained (langworthy-named-ec-2024-12-13.html); quote "unparalleled opportunity to influence" verified in retained text.
- Fidelis/Centene: fideliscare-home.html footer "FIDELIS and FIDELIS CARE are trademarks of Centene Corporation".
