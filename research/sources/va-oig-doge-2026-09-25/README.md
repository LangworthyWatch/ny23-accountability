# VA OIG "Review of Contracts Terminated for Convenience" (25-03033-230, Sept 22, 2026) and what it says about WNY / NY-23 VA facilities

Retained 2026-09-25 in response to a VoteVets post (Bluesky, ~Sept 24 afternoon) that summarized the report as
DOGE "wreckage" at the VA. Question asked: how does this land on the VA facilities that serve NY-23?

## Trigger post
- `votevets-bluesky-post-2026-09-24.txt` — verbatim post text as rendered; links the Stars and Stripes story.
  The Facebook copy was not visible logged-out (page shows only the newest post).

## The report itself
- `vaoig_review_page.html` — publication page (issue date Sept 22, 2026; 0 recommendations; IG Mason recused).
- `vaoig-25-03033-230_final.pdf` / `.txt` — full report, 21 pp (pdfplumber text).
  Key figures, all from the .txt: 2,210 contract actions reviewed; **435 terminated for convenience, ~$1.1B total
  contract value** (value = full agreed cost, NOT savings; does not net out amounts already paid or settlement costs);
  100 additional actions terminated then reinstated (~$1.1B value); 1,675 never terminated; 267 settlements completed,
  150 no-cost, 117 with **$10.6M** in settlement costs; May 16, 2025 list to Congress claimed 446 actions /
  **$120.9B**, of which only 357 were actually terminated and none of the 16 "$1B+" items exceeded $150M (one
  reported at $21B was ~$74M); July 3, 2025 list claimed 1,667, actual terminations 366 (17 reinstated), and
  it included 974 supply actions and 151 healthcare actions (e.g., nursing-home orders) that were never terminated;
  Feb 21, 2025 order gave offices <11 hours to review 1,049 actions; VA senior advisers and DOGE reps ordered
  terminations Feb 25, 2025 "regardless of the incomplete reviews"; the initial list was built from NAICS/PSC codes
  by VA's CMSO, **not** a DOGE AI program (p. 4). **The OIG did not assess impact on veterans or services** and
  did not review the April 13, 2026 corrected list.
- **No facility, VISN, or state breakdown anywhere in the report.** grep for New York / Buffalo / Bath /
  Canandaigua / Batavia / Syracuse / 528 / VISN 2 returns nothing.

## Coverage and reactions (retained page text)
- `stripes_com_*.txt` (Hersey, Sept 23, 2026) — VA press secretary Quinn Slaven: "no negative impact whatsoever";
  Blumenthal: "haphazard."
- `militarytimes_com_veterans_2026_09_24_*.txt` (Oliverio, Sept 24) — the $1.1B-is-not-savings framing; settlement $10.6M.
- `govexec_com_*.txt` — Sept 2026 GovExec piece (nav junk at top; article text after).
- `einpresswire_com_*.txt` — Blumenthal statement (via EIN, senate.gov copy not located).
- `king_senate_gov_*.txt`, `senate_vets_file_85FA465D.pdf/.txt` — the June 13, 2025 King/Blumenthal request letter.
- `veterans_senate_gov_2025_6_*.txt` — June 2025 spotlight forum release (655 contracts per SVAC minority staff).
- `propublica_org_article_*.txt` — the two June 6, 2025 ProPublica stories on the DOGE "MUNCHABLE" AI tool.

## Facility-level evidence for WNY / NY-23 (the part the report does not provide)

### A. FPDS pull of every VA "terminate for convenience" action, Jan 20, 2025 – Apr 30, 2026
- Method: FPDS ezsearch ATOM feed, `q=CONTRACTING_AGENCY_ID:3600 REASON_FOR_MODIFICATION:"F" SIGNED_DATE:[2025/01/20,2026/04/30]`,
  10 entries/page, 120 pages (`fpds_pages/`, `fetch_fpds.py`, `parse_fpds.py`) → `fpds_va_t4c_2025-01-20_to_2026-04-30.csv`.
- **1,193 unique actions** (356 in March 2025 alone). 538 carry the FPDS "EO: Radical Transparency About Wasteful
  Spending" initiative tag (EO 14222), the closest public marker for the DOGE wave, but the tag is not applied consistently.
- **36 actions with a New York place of performance or issued by Network Contract Office 2** (VISN 2). By NY-23-serving facility:
  - **Buffalo VAMC**: (1) Jan 30, 2025, Maintenance Matrix LLC, service maintenance on an Axiom Artis imaging system,
    deobligation $22,666.56 (contract's completion date was Jan 31, 2025, i.e., it was ending anyway); tagged EO 14222;
    DOGE's wall of receipts claims $116,053 "savings" on it. (2) May 30, 2025, University Emergency Medical Services Inc.,
    ED physician/APP staffing contract, mod P00015 deobligated $1,060,908.58 **on the day before the contract's
    May 31, 2025 completion date** ($20.0M obligated over its 2020–2025 life) — reads as an end-of-contract closeout,
    not a DOGE cut; not on the DOGE list. (3) Sept 3, 2025, Alliant Enterprises, AquaCare service, -$2,833
    (vendor no longer able to perform, per the description). (4) Dec 30, 2025, Getinge Cardiohelp service plan,
    -$6,012, "due to FDA recall of disposables."
  - **Canandaigua VAMC**: May 16, 2025 CSIC Solutions electrical testing, -$27,455, "defect in technical evaluation";
    July 8, 2025 Sierra 7, portable-broadband "Plum case" service, -$4,475 (DOGE claims $13,425 savings);
    Apr 22, 2026 chiller water testing closeout.
  - **Rochester (Finger Lakes)**: Feb 20, 2026, Prometheus Federal Services, gastroenterology, -$1,173,036.80
    (award terminated before any obligation; outside the OIG window).
  - **Bath VAMC, Batavia VAMC, and the Jamestown / Dunkirk / Olean / Springville / Elmira / Wellsville clinics: zero
    terminate-for-convenience actions by place of performance.** No NY row has a place-of-performance CD of 23.
- Caveat that must travel with this: the DOGE-wave terminations were overwhelmingly national and VISN-level
  consulting/IT/research contracts whose place of performance is DC, Virginia or Maryland (DOGE VA rows: VA 301,
  DC 143, MD 86). Any effect on WNY veterans from, e.g., cancer-registry or PTSD-center support contracts would not
  show up as a Buffalo or Bath place of performance. Absence here = no *local* contract was cut, not no effect.

### B. DOGE "wall of receipts" VA rows (`doge_data/`)
- `doge_scrape_contracts_latest.csv` (m-nolan/doge-scrape, 20,912 rows, scrapes Apr–May 2025) → `doge_va_contracts_latest.csv`
  (1,058 VA rows). 29 NY-linked rows; upstate VISN 2 items: Buffalo Axiom Artis maintenance ($116,053 claimed),
  Canandaigua Plum case ($13,425), Syracuse food-service consulting ($40,334 value, $0 savings), Syracuse EasyVista,
  Albany EHRM design (Triple C, $1.55M claimed; signed Oct 17, 2024, before DOGE existed).
- **One NY-23 business on the list**: Encorus Group Engineering, P.C., Springville (Erie County), A-E services for a
  dietetics upgrade at VA Connecticut (West Haven), DOGE claimed $143,054 savings. FPDS (`fpds_encorus_36C24124C0070.xml`)
  shows the contract was **never terminated**: mods in May 2025, Mar 2026, May 2026 and a July 9, 2026 mod adding
  $160,236.54. A local instance of the GAO finding (GAO-26-108615) that wall-of-receipts savings are unsupported.
- `doge-contracts-2025-03-18.csv` — early gist snapshot (6 VA rows), kept for provenance.

### C. Staffing, the better-documented WNY effect (OIG, not contracts)
- `vaoig-25-01135-196-final.pdf/.txt` — OIG FY2025 severe occupational staffing shortages (Aug 12, 2025), Appendix D:
  **VA Western New York (Buffalo, 528): 4 clinical + 6 nonclinical = 10**; **VA Finger Lakes (Bath, 528A6): 34 + 15 = 49**.
  Buffalo's four clinical: Anesthesiology, Medical Oncology, Psychology, Social Work. National: 4,434, +50% over FY2024's 2,959.
  Footnote 2: OIG did not assess the Deferred Resignation Program's effect.
- `vaoig-26-01046-271_-_final.pdf/.txt` — OIG FY2026 report (Sept 11, 2026), Appendix C: **Buffalo 22 + 6 = 28**;
  **Finger Lakes 23 + 4 = 27**. Buffalo's FY2026 clinical list includes Hematology/Oncology, Psychiatry, Neurology,
  Neurosurgery, Geriatrics, Radiology, inpatient RN, OR RN, nurse anesthetist, LPN, nursing assistant. National 4,712.
  Both reports: self-reported by facility officials, not validated by OIG; "severe shortage" ≠ vacancies.
- `federalnewsnetwork_com_*.txt` (Jan 2026) — AFGE's Mary Jean Burke: most facilities on track to lose 2–5% of
  psychologists in 2026, "locations, including Seattle and Buffalo," on track for "double-digit" attrition. Union claim; not VA data.
- `buffalonews/` — headlines/teasers only (paywalled body): Aug 7, 2025 "The VA said it is terminating most union
  contracts. It affects about 400 Buffalo nurses"; Aug 17, 2025 severe-shortage story; Aug 1, 2025 Batavia CLC report.
- `oig_deficiencies-care-batavia-*.txt`, `vaoig-24-02930-175_-_final.pdf/.txt` — OIG July 31, 2025: deficiencies at the
  Batavia CLC contributed to a resident's death; 10 recommendations; provider staffing found inadequate. Events are
  early 2024 (pre-DOGE); do not attribute to DOGE.
- `wgrz-2025-03-13-va-potential-cuts-wny.txt` — Langworthy's March 13, 2025 quotes ("We would not do something that
  would put patients at risk"; Collins "a thoughtful leader"); Gillibrand's counter.
- `yahoo_com_news_veteran_affairs_facility_bath_*.txt` — WETM Feb 2025: Bath probationary dismissals, "a small number."
- `schumer_senate_gov_*.txt` — Apr 16, 2025 Canandaigua event (crisis-line workers fired and rehired).
- `va_gov_western_new_york_health_care_about_us_.txt`, `va_gov_finger_lakes_about.txt` — facility rosters
  (VA WNY: Buffalo + Batavia + 9 CBOCs incl. Dunkirk, Jamestown, Olean, Springville; Finger Lakes: Bath + Canandaigua
  + Elmira, Wellsville, Rochester, Wellsboro clinics; "over 33,000 Veterans").

## Wayback (2026-09-25)
SPN accepted (HTTP 200) for the OIG page, OIG PDF, Stripes, Military Times, Bluesky, FNN and the FY2026 staffing PDF —
first successful SPN responses since Sept 15. Playback verified: OIG contracts PDF
(`web.archive.org/web/20260923150202/…vaoig-25-03033-230_final.pdf`, a Sept 23 capture). OIG page and Stripes
returned 404 on playback 20 s later; re-check before citing an archive URL. `wayback_attempts_2026-09-25.txt`.

## Bottom line for an entry (not yet written)
The OIG report is a process-and-accuracy finding (DOGE-driven, rushed, inaccurate reporting to Congress), not a
harm finding; it explicitly did not evaluate impact on veterans. Public procurement data shows **no DOGE-wave contract
termination at any NY-23-serving VA site**; the two Buffalo/Canandaigua items DOGE claimed were a $22,667 deobligation on
an expiring maintenance order and a $4,475 broadband-device service. The documented WNY effects in 2025–26 run through
**staffing**, not contracts: Buffalo's OIG-reported severe shortages went 10 → 28 in one year and Bath's stayed at 49 → 27,
with oncology, psychiatry and inpatient nursing on Buffalo's list. Langworthy's on-record position (Mar 13, 2025) was
that cuts would not put patients at risk; he has no public statement on the contract cancellations or the Sept 22 report.
