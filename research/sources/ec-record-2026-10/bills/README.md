# Langworthy (L000600) legislative record, 119th Congress, with focus on Energy and Commerce

Research only. Nothing under `content/` was edited. Compiled 2026-10-16.

## Data and snapshot

- Source: govinfo BILLSTATUS bulk zips for 119th House `hr`, `hres`, `hjres`, `hconres`
  (`https://www.govinfo.gov/bulkdata/BILLSTATUS/119/<type>/BILLSTATUS-119-<type>.zip`).
  Directory listings saved as `bulk/listing-*.json`. Zip lastModified per listing: hr 16-Oct-2026 13:37,
  hres 13:39, hjres 13:34, hconres 08:42 (govinfo does not state the time zone). Downloaded 2026-10-16 16:14 UTC.
  Latest `<updateDate>` inside the data: **2026-10-16T13:28:56Z**. 12,804 measures parsed (10,833 H.R.).
- `bulk/` is ~234 MB and should not be committed. **Add to `.gitignore`:**
  `research/sources/ec-record-2026-10/bills/bulk/`
- The 50 sponsored-measure XMLs plus H.R. 1047 and H.R. 9019 are copied to `xml/` so the record survives without `bulk/`.
- Scripts: `parse_billstatus.py` (sponsored, cosponsored, flags, summary), `compare_ec.py` (committee comparison).
  Run with `python3 -I <script> bulk .`.
- Cosponsors were read from `<cosponsors><item>`, matching `bioguideId == L000600`.
- Stage flags (`f_*` columns) come only from BILLSTATUS:
  - E&C subcommittee and full-committee markup/reported come from `<committees>` activities.
  - Passed House = LoC action code 8000. Failed House = 9000. Passed Senate = 17000. Enacted = 36000 or `<laws>`.

Outputs: `langworthy-sponsored-119.csv`, `langworthy-sponsored-119-actions.txt` (full action history), `langworthy-cosponsored-119-all.csv`,
`langworthy-cosponsored-119-EC.csv`, `summary-counts.json`, `ec-comparison.txt`, `three-bills-verification.txt`, `power-act-title-search.txt`.

## 1. Sponsored measures: 50 total (42 H.R., 8 H.Res.), 20 referred to E&C

| Bill | Title | Introduced | E&C stage reached | Latest action |
|---|---|---|---|---|
| H.R. 3157 | State Energy Accountability Act | 2025-05-01 | Energy Subcmte markup 6/5/25; full markup 6/25/25 (27-20); **reported** H. Rept. 119-301 | Union Cal. 255, 9/17/25. No floor vote |
| H.R. 3699 | Energy Choice Act | 2025-06-04 | Subcmte markup 11/19/25; full markup 12/3/25 (24-21); **reported** H. Rept. 119-482 | Union Cal. 412, 2/4/26. No floor vote |
| H.R. 4690 | Reliable Federal Infrastructure Act | 2025-07-23 | Subcmte markup 11/19/25 (16-14); full markup 12/3/25 (27-21); **reported** H. Rept. 119-483 | **Passed House 4/22/26, 215-202 (roll 134)**. Referred to Senate EPW 4/27/26 |
| H.R. 7502 | Recycled Materials Attribution Act | 2026-02-11 | CMT Subcmte markup 9/1/26; full markup, ordered reported 9/16/26 (28-0) | Report not yet filed |
| H.R. 10163 | American Quantum Competitiveness Act | 2026-08-27 | CMT Subcmte markup 9/1/26; full markup, ordered reported (amended) 9/16/26 (36-0) | Report not yet filed |
| H.R. 9317 | BUSES Act | 2026-06-15 | Environment Subcmte markup, forwarded by voice vote 7/14/26 | Awaiting full committee |
| H.R. 1421 (E&C secondary to Judiciary), 1617, 1875, 2203, 2560, 5553, 6037, 7366, 9117 (also W&M, Ed&W), 9661, 9806, 10522, 10571, 10628 (also W&M) | various | 2025-02 to 2026-09 | Referral only | Referred |

The 30 measures he sponsored that were not referred to E&C:
- **H.R. 5517** (Northern Border Security Enhancement and Review Act; Homeland). Reported in H. Rept. 119-830; passed the House by voice vote under suspension on 9/16/26; on the Senate calendar.
- **H.R. 7256** (Oversight). Ordered reported 43-0 on 2/4/26; report not filed.
- **H.R. 7065** (Natural Resources). Subcommittee hearing on 3/4/26.
- **Seven special rules from the Rules Committee** (H.Res. 177, 426, 707, 951, 1174, 1345 adopted; **H.Res. 1042 failed 214-217, roll 60, 2/10/26**). He reported these as a Rules member.
- **H.Res. 1176** (committee elections for Kiley and Fuller; adopted 4/15/26).
- **19 other bills** (Agriculture, Ways and Means, Judiciary, T&I, Homeland, Ed&W, Oversight). Referral only.

None of his 50 measures passed the Senate or became law. Full rows are in `langworthy-sponsored-119.csv`.

**Incorporation flags (CRS "Related bill" in `<relatedBills>`; not "contains text", so do not infer):**
- H.R. 1875 is related to H.R. 1 (OBBBA).
- H.R. 289, 291, and 295 are related to H.R. 7567.
- H.R. 6037 has an identical bill, S. 3666.

No sponsored bill carries "Contained in public law" or "text incorporated". BILLSTATUS often misses incorporation, so a text comparison would be needed before saying anything either way. The July 22, 2026 POWER Act discussion draft folds in H.R. 3157 (see section 4). It is not in BILLSTATUS because it has no number.

## 2. E&C-referred cosponsorships

- Total cosponsorships in the 119th: **332**. E&C-referred: **87**. He was an original cosponsor on 15 of the 87 and withdrew from none.
- Outcomes for the 87, by flag (`summary-counts.json`): subcommittee markup 15, full markup 14, reported 13, **passed House 19**, passed Senate 6, **enacted 6**.

**Enacted (6):**
- H.J.Res. 20 (P.L. 119-6), H.J.Res. 35 (119-2), H.J.Res. 87 (119-15), H.J.Res. 88 (119-16), H.J.Res. 89 (119-17). These are CRA disapprovals.
- H.R. 3657, Hydropower Licensing Transparency Act (Schrier, D). P.L. 119-112, 9/25/26.

**Plus one flag:** H.R. 27, HALT Fentanyl Act (cosponsored 1/3/25, original). It passed the House. CRS marks S. 331 as "Contained in public law" (P.L. 119-26).

**Passed the House only (12):**
- Energy: H.R. 26, H.R. 1047 (GRID Power), H.R. 2140, H.R. 3616 (Reliable Power), H.R. 3628
- Consumer and other: H.R. 973, H.R. 979 (AM Radio), H.R. 1266
- Health: H.R. 1262, H.R. 2821, H.R. 3747, H.R. 4541

## 3. Committee assignments (Clerk and House-adopted resolutions)

| Committee | Elected by | Date | Current rank / subcommittees (Clerk) |
|---|---|---|---|
| Energy and Commerce | **H.Res. 21** | **Jan 9, 2025** (start of the 119th) | #25 majority. Subcommittees: Energy (#13), Health (#15), Environment (#11) |
| Oversight and Government Reform | H.Res. 31 | Jan 13, 2025 | #20. No subcommittee listed |
| Rules | H.Res. 38 | Jan 14, 2025 | #6. **Chair, Subcommittee on Legislative and Budget Process** |

Sources:
- Resolution texts: `committee-elections/BILLS-119hres{21,31,38}eh.htm`.
- Clerk records: `clerk/clerk-member-L000600.txt`, `clerk/MemberData-L000600-extract.txt` (MemberData.xml publish-date Oct 1, 2026), and `clerk/clerk-committee-{IF00,IF03,IF14,IF18,RU00,GO00}.txt` (fetched 2026-10-16).
- Subcommittee assignment dates are **not** in Clerk data (gap).

## 4. The three bills in the Oct 15 post (`three-bills-verification.txt`)

**POWER Act**
- Still **no bill**. No House title in the snapshot matches "Permitting Our Way to an Energy Resurgence" (0 files).
- Guthrie (G000558) has introduced no measures since 7/1/26.
- Other House bills share the "POWER Act" name and are unrelated: H.R. 164, 1149, 2074, 2599, and 9019 (Roy, referral only).
- Senate bills were not searched.

**H.R. 1047 (GRID Power Act)**
- Sponsor: Balderson. 17 cosponsors.
- Langworthy cosponsored on **2025-06-17** (not original, not withdrawn).
- Ordered reported 28-23 on 6/25/25 (H. Rept. 119-295). **Passed the House 9/18/25, 216-206, roll 279.**
- Referred to Senate ENR 9/19/25. Identical bill S. 465 had a hearing 4/15/26. Not law.

**H.R. 3157 (State Energy Accountability Act)**
- Sponsor: Langworthy. Status confirmed as above (H. Rept. 119-301, Union Cal. 255, no floor vote).
- File updateDate is 2026-02-04, so nothing has happened since.

## 5. Comparison (`ec-comparison.txt`; H.R. only, same snapshot)

| Group | n | Full E&C markup | Reported | Passed House |
|---|---|---|---|---|
| All E&C-referred | 2,193 | 130 (5.9%) | 109 (5.0%) | 108 (4.9%) |
| Republican-sponsored | 1,057 | 98 (9.3%) | 80 (7.6%) | 81 (7.7%) |
| Langworthy | 20 | 5 (25%) | 3 (15%) | 1 (5%) |

- Only Latta (7) and Evans (6) sponsored more E&C-referred H.R. bills that got a full-committee markup. Langworthy is tied with five others at 5.
- Caveat: the "passed House" row counts bills that skipped markup and passed under suspension.

## Gaps

- BILLSTATUS records almost no E&C **hearings** (1 subcommittee hearing across 2,193 bills), so hearing-stage data is unusable. Subcommittee referrals are also missing for many bills (e.g. H.R. 1875, 9661).
- Incorporation into other laws or packages (including OBBBA) is flagged, not verified.
- The bulk snapshot may lag introductions by a few days. Senate bills were not pulled.
- New files are not Wayback-archived. H.R. 1047 and H.R. 3157 BILLSTATUS and the Clerk IF00 roster were archived 10/15 (`../../triage-2026-10-15/energy/README.md`).
