# Energy triage (Oct 15, 2026): L4, L5, L7, L8 + screenshot 08

Research only. Nothing under `content/` was edited. Verdicts are proposals. Whisper output is machine
transcription; where a word was checked against burned-in captions or the full debate SRT it says so.

## Speaker / authorship (failure mode 6)

| Post | Page | Speaker(s) in the clip | Evidence |
|---|---|---|---|
| L5 (Oct 9) | campaign "Nick Langworthy" | **Langworthy only** (WETM debate 23:21-24:29). No Gies audio in the 61 s clip. | `../videos/L5.txt`; `../hochul-record/frames/L5_*.jpg`; `debate-srt-excerpt-21m18s-23m20s.srt` |
| L7 (Oct 8) | campaign | 0-4 s **Gies** (lower third "DR. AARON GIES"), then 4-27 s **Langworthy** (lower third "REP. NICK LANGWORTHY") | `L7-frames-1fps.jpg`, `L7-whisper-base-en.srt`. Whisper "Hocho" = "HOCHUL" per burned caption |
| L4 (Oct 14) | campaign | **Bruce Blakeman**, Spectrum gubernatorial debate Oct 13 (not Langworthy) | `../hochul-record/README.md` |
| L8 (Oct 13) | official "Congressman Nick Langworthy" | Langworthy on WBEN (per post); host line "electric snow blowers" | `../videos/L8.txt` (voice not independently matched) |
| 08 (Oct 15) | official page, text | n/a | `../screenshots/08-official-energy-commerce-bills.png` |

## Q1. What Gies said at the Oct 6 WETM debate

Full SRT `../../debate-2026-10-06/debate-audio.srt`; excerpt saved as `debate-srt-excerpt-21m18s-23m20s.srt`.
Speaker turns checked against video frames (`debate-frames-21m40s-23m25s.jpg`, `debate-frames-22m26s-22m41s-1fps.jpg`):
Gies on camera 21:40; Langworthy 22:15-22:38 (lower third 22:34-22:36); Gies from 22:39; moderator 23:08; Langworthy 23:25.

Gies, 21:20-22:11:
> "Increasing global exports of liquefied natural gas would not bring down prices in Western New York and the Southern Tier. ... This is why I oppose Nick Langworthy's signature piece of legislation, the Energy Choice Act, because by banning the bans, as he said, it would force consumers to pay natural gas prices forever, whatever the gas company wants to charge for them. I am for giving people more control over where they get their energy and how much they pay for it."

Langworthy, 22:11-22:37: "He opposes the Energy Choice Act ... He believes that you should be mandated to be in an all-electric home. I don't. ... it's a matter of life and death for us to have redundancy in the way we heat our homes ..."

Gies, ~22:37-23:06 (attributed by the camera cut at 22:39 and by the moderator's follow-up "you say keep it at the state level"; the 1-2 s boundary is inferred):
> "I also believe that the state's climate law is too aggressive, and I will never support things like bans on wood-burning stoves or propane or no more hookups for natural gas. But that should be dealt with at the state level. We do not need a federal ban that would prohibit states from doing anything to diversify our energy mix."

Moderator: "if the state mandates only one form of power, is that a good or a bad thing?" Gies: "That would be a bad thing. We need a diversified energy mix."

**How the clips are edited.** L7 opens on Gies's sentence without "This is why" and cuts before "because by banning the bans ... whatever the gas company wants to charge", then splices to Langworthy's rebuttal and ends at 22:37, about 2 seconds before Gies says he "will never support" bans on propane or new gas hookups. L5 contains no Gies audio.

- "My opponent OPPOSES [the Energy Choice Act]" (L7): **accurate**. He said it.
- "now you know my opponent supports [Hochul's gas and propane ban]" (L5): **contradicted** by Gies's own words in the same exchange.

## Q2. NY All-Electric Buildings Act (Energy Law 11-104(6)-(8); Exec. Law 378(19))

- Text (current; nysenate "most recent revision 2025-04-04"; subdivisions 6-8 identical to the Aug 2025 capture): `nysenate-ENG-11-104-via-wayback-20261015.txt` (lines ~85-170).
  - Code "shall prohibit the installation of fossil-fuel equipment and building systems" in **new** buildings of 7 stories or fewer (except commercial/industrial over 100,000 sq ft) on or after **Dec 31, 2025**; all new buildings after **Dec 31, 2028**.
  - "Fossil-fuel equipment" = equipment "that uses fossil-fuel for combustion". That covers propane as well as natural gas. Wood is not a fossil fuel, so wood stoves are not covered.
  - Sub. 7(a): does **not** apply to existing buildings, "including ... the installation or continued use and maintenance of fossil-fuel equipment ... including as related to cooking equipment".
  - Sub. 7(b) exemptions: emergency backup/standby power; manufactured homes; manufacturing, commercial food establishments, labs, car washes, laundromats, hospitals, critical infrastructure, **agricultural buildings**, fuel cells, crematoria. 7(e) exemption where the grid cannot reasonably serve (PSC decides).
- Enactment: 2023 state budget (NY1, `ny1-2025-11-12-ny-agrees-delay-aeba.txt`, secondary). The Part/chapter citation was **not** pulled from a primary source.
- Litigation and current status:
  - NDNY dismissed the challenge on Aug 21, 2025. **Stipulation and Order, Nov 18, 2025** (`ndny-mulhern-dkt75-stipulation-order-2025-11-18.pdf`, para. 2-4): the effective date of the implementing code rules (19 NYCRR 1240.6, Subpart 1229-2) "is hereby suspended" pending the appeal and any cert petition. The suspension ends **120 days after the Second Circuit mandate** if no cert petition is timely filed.
  - **Second Circuit affirmed on June 30, 2026**: EPCA does not preempt (`2dcir-mulhern-gas-v-mosley-2026-06-30.pdf`). Rehearing en banc denied **Aug 26, 2026** (`ca2-25-2041-dkt86-order-denying-en-banc-2026-08-26.pdf`). Mandate issued **Sept 2, 2026** (CourtListener docket, `courtlistener-ca2-25-2041-docket-search-2026-10-15.json`).
  - Computed: 120 days after Sept 2, 2026 = **Dec 31, 2026**. The cert deadline (90 days from the en banc denial) = **Nov 24, 2026**. A timely cert petition would extend the suspension. **No cert petition found** (CourtListener has no SCOTUS docket; RECAP coverage is incomplete, so this is not proof of absence).
  - **As of Oct 15, 2026 the ban is not in effect for anyone.** Earliest possible effect is about Jan 1, 2027.

## Q3. Fracking

- DEC Findings Statement, **June 2015** (`dec-hvhf-findings-statement-2015-06.pdf`, p.42): the agency selects "No Action", so "high-volume hydraulic fracturing will be prohibited in New York State." Governor: Cuomo.
- Statute: ECL 23-0501(3)(a) (`nysenate-ENV-23-0501-via-wayback.txt`, lines 177-184) says "No permits shall be issued" for wells using HVHF (300,000+ gallons of water) or CO2 fracturing, added by "the chapter of the laws of 2020". The 2020 chapter number and signing date were not separately pulled. Cuomo was governor.
- CLCPA signed **July 18, 2019, chap. 106** (`nysenate-bill-2019-S6599-clcpa-via-wayback.txt`). Hochul was Lieutenant Governor under Cuomo (`governor-ny-gov-aboutlieutenantgovernor-20210317.txt`, Mar 2021 capture; her start date is not in that page). She became governor in Aug 2021, after all three actions.
- Conventional drilling is still legal and permitted. DEC well data (data.ny.gov `szye-wmt3`, saved JSON):
  - Oil Development permits: 52 in 2024 and 58 in 2025. Since Jan 2024: 111 in Cattaraugus and 1 in Steuben, both NY-23. 2026 permits are mostly "Not Listed"/"Confidential" type in Cattaraugus and Allegany.
  - **Gas** development/extension/wildcat permits: 101 in 2010, 23 in 2011, then 0-3 a year, the last in 2017. The collapse predates both the 2015 findings and Hochul.

## Q4. NY vs PA prices (EIA)

| Measure | NY | PA | US | File |
|---|---|---|---|---|
| Residential electricity 2025 (c/kWh) | 26.39 | 19.30 | 17.30 | `eia-epm-archive-february2026.txt` L10711-10712 (Table 5.6.B YTD Dec 2025) |
| Residential electricity YTD Jul 2026 | 29.38 | 21.04 | 18.19 | `eia-epm-table-5_6_b-jul2026.txt` |
| Residential natural gas 2025 ($/Mcf) | 17.58 | 15.04 | 15.34 | `eia-ng-residential-price-by-state-a.txt` |
| Residential natural gas Feb / Jul 2026 | 16.42 / 30.86 | 14.49 / 28.73 | 14.95 / 26.45 | `eia-ng-residential-price-by-state-m.txt` |


The statewide NY figure includes Con Edison (36.74 c/kWh bundled residential in 2025). Upstate utilities, from EIA-861 2025 bundled residential revenue divided by sales (`eia861-2025-ny-pa-utility-residential-prices.txt`, agent-computed):

| Utility | c/kWh |
|---|---|
| NYSEG | 22.59 |
| RG&E | 22.01 |
| National Grid (Niagara Mohawk) | 19.89 |
| FirstEnergy PA | 18.77 |
| PPL | 18.60 |
| PECO | 18.02 |
| Duquesne | 23.47 |

PA is cheaper, but the upstate gap is about 6-20%, not the statewide 37%.

## Q5. CLCPA

- Signed by Cuomo on July 18, 2019 (above).
- **Hochul weakened it in the FY2027 budget.** Current ECL 75-0109(1) (`nysenate-ENV-75-0109-via-wayback-20261015.txt`, "most recent revision (from 2026-05-29)"): DEC regulations are now due "No later than December thirty-first, two thousand twenty-eight", designed to "achieve, to the maximum extent feasible and cost effective, a sixty percent reduction ... by two thousand forty" and comply with the 2050 limit only. 75-0107 still lists the 2030 limit (`nysenate-ENV-75-0107-via-wayback-20261015.txt`).
- Secondary context (law-firm and academic, not primary): `gtlaw-2026-05-ny-budget-amends-clcpa.txt`, `columbia-climate-law-blog-2026-06-05-clcpa-rollback.txt`.
- "Want to take it nationwide": **nothing concrete found.** No primary document shows Hochul or Albany Democrats seeking a national CLCPA or all-electric mandate.

## Q6. Energy Choice Act, H.R. 3699 (`BILLSTATUS-119hr3699.xml`, updated 2026-09-23)

Nothing has changed since the Feb 25 entry:
- Last action: Feb 4, 2026, reported (H. Rept. 119-482), Union Calendar No. 412. **No House floor vote.**
- 157 cosponsors (154 R, 3 D), none added after Feb 4, 2026, none withdrawn.
- It is not law, so it "protects" nothing yet.

## Q7. Screenshot 08 bills

- **E&C membership**: Clerk roster lists Langworthy as #25 on the majority side (`clerk-committee-IF00-roster.txt` L265).
- **POWER Act**: a Guthrie **discussion draft** released July 22, 2026 (`ec-power-act-release-2026-07-22.txt`). It bundles 19 bills and is described as speeding "construction of the pipelines, power generation, electricity transmission". It includes GRID Power Act and Langworthy's SEAA.
  - No bill number found. H.R. 9019 "POWER Act" is an unrelated Chip Roy water/energy reporting bill (`BILLSTATUS-119hr9019.xml`).
  - The Sept 2, 2026 E&C markup covered nuclear and Clean Air Act bills, not the package (`ec-markup-2026-09-02-guthrie-opening.pdf`).
- **GRID Power Act, H.R. 1047**: sponsor Balderson. Langworthy is a **cosponsor** (June 17, 2025, per `<cosponsors><item>`). FERC rule to prioritize dispatchable interconnection (CRS summary in XML). Passed the House **Sept 18, 2025, 216-206, roll 279**, Langworthy **Yea** (`clerk-roll279-2025-hr1047.xml`). Referred to Senate ENR on Sept 19, 2025; no further action.
- **State Energy Accountability Act, H.R. 3157**: Langworthy is **sponsor**; cosponsors Evans (original) and Balderson. Ordered reported 27-20 on June 25, 2025; H. Rept. 119-301 on Sept 17, 2025; Union Calendar 255. **No floor vote.**
  - Text (`BILLS-119hr3157rh.txt`) adds PURPA 111(d)(22). States with an "intermittent energy policy" must "consider and make a determination" whether to adopt a public evaluation of reliability, rates, and emergency performance. It is a consider-and-determine standard, not a flat mandate.
- **This week**: no committee meetings Oct 11-17 (`docs-house-committee-calendar-week-2026-10-11.txt`). Last House roll call of 2026 is No. 314 on Sept 16 (`clerk-roll314-2026-last-vote.xml`; 315 does not exist). Nothing on these bills happened this week. A Senate bipartisan permitting bill was reported introduced in early October (search result only, **not verified**).

## Wayback (verified by playback: 200 + expected text, Oct 15, 2026)

| Snapshot | Checked for |
|---|---|
| https://web.archive.org/web/20261015202226/https://www.nysenate.gov/legislation/laws/ENG/11-104 | "seven stories" |
| https://web.archive.org/web/20261015202119/https://www.nysenate.gov/legislation/laws/ENV/75-0109 | "December thirty-first, two thousand twenty-eight" |
| https://web.archive.org/web/20261015202528/https://www.nysenate.gov/legislation/laws/ENV/75-0107 | "2050: 15% of 1990" |
| https://web.archive.org/web/20250306150052/https://www.nysenate.gov/legislation/laws/ENV/23-0501 | "high-volume hydraulic" |
| https://web.archive.org/web/20250118012856/https://www.nysenate.gov/legislation/bills/2019/S6599 | "signed chap.106" |
| https://web.archive.org/web/20261015203540/https://dos.ny.gov/system/files/documents/2026/07/decision-mulhern-gas-v.-mosley-2d-cir.pdf | "AFFIRM" |
| https://web.archive.org/web/20261015203729/https://storage.courtlistener.com/recap/gov.uscourts.nynd.140479/gov.uscourts.nynd.140479.75.0_1.pdf | "120 days after" |
| https://web.archive.org/web/20261015203835/https://storage.courtlistener.com/recap/gov.uscourts.ca2.4c5fbab7-9ae9-4276-8d05-4b42e5bdf354/gov.uscourts.ca2.4c5fbab7-9ae9-4276-8d05-4b42e5bdf354.86.0.pdf | "rehearing" |
| https://web.archive.org/web/20261015203942/https://extapps.dec.ny.gov/docs/materials_minerals_pdf/findingstatehvhf62015.pdf | "No Action" |
| https://web.archive.org/web/20261015204051/https://www.eia.gov/dnav/ng/ng_pri_sum_a_EPG0_PRS_DMcf_a.htm | "17.58" |
| https://web.archive.org/web/20261015204209/https://www.eia.gov/dnav/ng/ng_pri_sum_a_EPG0_PRS_DMcf_m.htm | "30.86" |
| https://web.archive.org/web/20261015204449/https://www.eia.gov/electricity/monthly/archive/february2026.pdf | "26.39" |
| https://web.archive.org/web/20261015203056/https://www.govinfo.gov/bulkdata/BILLSTATUS/119/hr/BILLSTATUS-119hr3699.xml | "Energy Choice Act" |
| https://web.archive.org/web/20261015202643/https://www.govinfo.gov/bulkdata/BILLSTATUS/119/hr/BILLSTATUS-119hr3157.xml | "State Energy Accountability Act" |
| https://web.archive.org/web/20261015202520/https://www.govinfo.gov/bulkdata/BILLSTATUS/119/hr/BILLSTATUS-119hr1047.xml | "Langworthy" |
| https://web.archive.org/web/20261015204731/https://www.govinfo.gov/content/pkg/BILLS-119hr3157rh/html/BILLS-119hr3157rh.htm | "intermittent energy policy" |
| https://web.archive.org/web/20261015203203/https://clerk.house.gov/evs/2025/roll279.xml | "GRID Power Act" |
| https://web.archive.org/web/20261015203309/https://clerk.house.gov/evs/2026/roll314.xml | "Retire through Ownership" |
| https://web.archive.org/web/20261015203425/https://energycommerce.house.gov/posts/chairman-guthrie-releases-power-act-to-lower-electricity-costs-for-american-families | "State Energy Accountability Act" |
| https://web.archive.org/web/20261015204559/https://clerk.house.gov/committees/IF00 | "LANGWORTHY" |

**Not verified, do not cite:** the EIA EPM Table 5.6.B grapher capture (20261015204334) played back without "29.38", probably an EIA error page. Cite the local file for YTD-July 2026, or re-archive it. The data.ny.gov SODA queries, CourtListener API JSON, and EIA-861 zip were not archived; the local copies are the record. Submission log: `wayback-save-log.txt`.

## Proposed verdicts

- **L5** "my opponent supports [Hochul's gas and propane ban]": **FALSE**. In the same exchange Gies said he "will never support" bans on propane or new gas hookups. The clip contains no Gies audio. Calling it a "ban" without saying new construction only, existing homes exempt, and not yet in effect is MISSING CONTEXT.
- **L7** "My opponent OPPOSES [the Energy Choice Act]": **TRUE**. The post as a whole is **MISLEADING**:
  - The clip cuts Gies's reason and stops about 2 s before his anti-ban statement.
  - "He believes you should be mandated to be in an all-electric home" is contradicted by Gies.
  - The ECA is not law and "protects" nothing yet.
- **L4** "Kathy Hochul bans it [natural gas drilling]": **FALSE ATTRIBUTION / MISLEADING**.
  - The HVHF ban came from Cuomo's DEC (2015) and a 2020 statute signed while Hochul was Lieutenant Governor.
  - Conventional drilling is still legal, and DEC keeps permitting oil wells in Cattaraugus.
  - "PA ... cheaper energy": TRUE (statewide 26.39 vs 19.30 c/kWh; gas $17.58 vs $15.04/Mcf, 2025). The upstate gap is smaller.
  - "because of her failed energy policies": NOT SUPPORTED as causation.
- **L8**:
  - "made their green new deal the law of the land in NY": MISSING CONTEXT. The CLCPA was signed by Cuomo in 2019; Hochul's own 2026 budget weakened it.
  - "now they want to take it nationwide": **NOT SUPPORTED**.
- **08**: **MOSTLY TRUE**.
  - E&C seat confirmed. Descriptions broadly match the bill texts and summaries.
  - None of the three is law. POWER Act is an unintroduced Guthrie discussion draft. Langworthy is a cosponsor (not sponsor) of GRID Power and sponsor of SEAA, which never got a floor vote.
  - Nothing happened on any of them this week.

## Gaps

- AEBA 2023 chapter/Part citation and the 2020 HVHF chapter number/date: no primary source retrieved.
- Cert petition status in Mulhern (deadline Nov 24, 2026) is unconfirmed.
- POWER Act formal introduction cannot be ruled out by title search alone.
- Hochul's LG start date has no primary source on file.
- No primary source for Hochul's own "remains committed" statement.
- L8: the voice was not independently matched.
- Winter Storm Elliott figures (L5/L7) are handled in `../hochul-record/elliott/` and `../../debate-2026-10-06/claims/L16-*`.
