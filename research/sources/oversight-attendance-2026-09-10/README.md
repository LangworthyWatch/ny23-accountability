# Langworthy attendance at House Oversight Committee proceedings, 119th Congress (compiled Sept 10, 2026)

**Scope.** Per the House Clerk's MemberData.xml (retrieved Sept 10, 2026), Rep. Langworthy sits on the Committee on Oversight and Government Reform (rank 20 of 26 Republicans; 47 members, 26 R / 21 D) and holds **no Oversight subcommittee seat** (his subcommittees are Energy and Commerce: Energy, Health, Environment; Rules: Legislative and Budget Process). The committee's two task forces (Declassification of Federal Secrets; Defending Constitutional Rights and Exposing Institutional Abuses) list their members on oversight.house.gov; he is on neither (page texts retained here as `oversight-house-gov-task-force-*.txt`). So the relevant record is **full-committee** hearings and markups only.

## Files

| File | What it is |
|---|---|
| `oversight_hearings_attendance.csv` | Every 119th-Congress Oversight transcript on govinfo whose caption is the full committee or one of its task forces (21), with the "Present:" roster and his status. `body` column separates full committee (12) from task force (9). |
| `oversight_markup_votes.csv` | One row per recorded-vote sheet posted on docs.house.gov for every full-committee Oversight event (161 sheets across 19 events with votes, plus 7 events with none), with the question, his mark (Aye / No / Not voting), the printed tally, and a parse check. |
| `oversight_vote_sheets_text.txt` | Text layer of all 161 vote sheets (`pdftotext -layout`), so every mark can be checked without re-downloading. |
| `oversight_events_docs_house_gov.json` | The 26 full-committee events (event ID, date, h1 label, vote-sheet URLs) found by sweeping docs.house.gov daily calendar pages, Jan 3, 2025 through Sep 9, 2026. |
| `clerk_floor_votes_on_key_dates.json` | House floor roll calls on each date he missed an Oversight hearing or cast no markup votes, with his recorded floor vote on each (Clerk EVS XML). |
| `govinfo-chrg-119-house-package-ids.txt` | The 602 CHRG package IDs enumerated from the govinfo sitemaps. |

## Hearings

**Method.** Hearings have no formal attendance roll. Every published transcript opens with a roster ("Present: Representatives …") of members who attended at any point. We enumerated every 119th-Congress House hearing transcript on govinfo via the CHRG sitemaps (602 packages), fetched each header, kept those captioned "before the Committee on Oversight and Government Reform" (or one of its task forces), dropped errata reprints, and parsed the roster sentence. One transcript (Jan 15, 2025) is PDF-only and was parsed from the PDF. The 12 full-committee hearings match one-for-one the 12 "Hearing:" events on the docs.house.gov calendar for the same period.

**Result.** 12 full-committee hearings with published transcripts (Jan 15, 2025 through Mar 4, 2026): **present at 7, absent at 5.**

| Date | Hearing | Members listed | Langworthy |
|---|---|---|---|
| Jan 15, 2025 | Stay-at-Home Federal Workforce | 39 | present |
| Feb 5, 2025 | Rightsizing Government | 46 | present |
| Feb 25, 2025 | GAO 2025 High Risk List (1:00 PM) | 36 | absent |
| Mar 5, 2025 | Sanctuary City Mayors | 46 | present |
| Apr 9, 2025 | Restoring Trust in FDA (10:00 AM) | 34 | absent |
| Jun 5, 2025 | Federal Government in the Age of AI (10:00 AM) | 42 | absent |
| Jun 10, 2025 | 23andMe bankruptcy sale (10:00 AM) | 33 | absent |
| Jun 12, 2025 | Sanctuary State Governors | 44 | present |
| Sep 18, 2025 | Oversight of the District of Columbia | 46 | present |
| Dec 17, 2025 | Full Committee Member Day (9:00 AM) | 4 | absent |
| Jan 7, 2026 | Fraud and Misuse of Federal Funds in Minnesota, Part I | 45 | present |
| Mar 4, 2026 | Fraud and Misuse of Federal Funds in Minnesota, Part II | 46 | present |

**Same-day context for the five absences** (docs.house.gov calendar; E&C transcripts; Clerk floor votes):
- Feb 25, 2025: Energy and Commerce full-committee markup, 10:30 AM. He voted on 2 of 4 recorded votes at the Oversight business meeting that began 12:45 PM (see markups) and on all 5 floor votes (1:58 PM onward).
- Apr 9, 2025: Energy and Commerce full-committee hearing (its transcript's roster does **not** list him either) and a Rules Committee meeting on the Senate amendment to H.Con.Res. 14 (he sits on Rules; Rules publishes no roster). Voted on all 7 floor votes (4:02 PM onward). He did vote at the Oversight markup continuation that day (2 of 2).
- Jun 5, 2025: Energy and Commerce Energy Subcommittee markup, 10:00 AM (same hour; no transcript). Voted on all 4 floor votes (4:41 PM onward).
- Jun 10, 2025: Energy Subcommittee hearing on the DOE budget, 10:00 AM; its transcript roster lists him present. Rules Committee met at 2:00 PM on H.R. 4. Voted on all 4 floor votes.
- Dec 17, 2025: Member Day, 9:00 AM; only 4 of 47 members appeared. Voted on all 9 floor votes (10:52 AM onward).

## Markups and recorded votes

**Method.** Business meetings record roll-call votes and the committee posts a sheet per vote on docs.house.gov (`CRPT-119-GO00-VoteNNN-YYYYMMDD.pdf`). We swept every weekday's calendar page (Jan 3, 2025 through Sep 9, 2026), kept the 26 events whose committee is Oversight and Government Reform with no subcommittee, and downloaded all 161 posted sheets. Each sheet was parsed positionally (pdfplumber): his row is located by name and any X in the Republican Aye / No / Present columns is read; sheets with no mark in his row are "Not voting." As a check, every sheet's parsed Aye and No counts were re-derived and compared with the printed "Roll Call Totals" line: 160 of 161 match. The one exception (Feb 5, 2025, Vote 1) has the 19 Democratic marks printed in the Aye column while the totals line says 19 Nays; his row is blank on that sheet either way. House rules in the 119th Congress do not allow proxy voting in committee, so "Not voting" means he was not in the room for that roll call.

**Result, markups only** (13 markups, 145 recorded votes): **voted on 76, not voting on 69.**

| Date | Markup (first item) | Roll calls | Aye | No | Not voting |
|---|---|---|---|---|---|
| Feb 25, 2025 | Authorization and Oversight Plan | 4 | 2 | 0 | 2 |
| Mar 25, 2025 | H.R. 1295 Reorganizing Government Act and 7 other bills; H.Res. 186/187 | 26 | 0 | 0 | **26** |
| Apr 9, 2025 | H.Res. 187/186 (continuation) | 2 | 2 | 0 | 0 |
| Apr 30, 2025 | **FY2025 Budget Reconciliation Committee Print** (Oversight's portion of what became H.R. 1, the One Big Beautiful Bill Act); H.Res. 264 | 28 | 0 | 0 | **28** |
| May 21, 2025 | H.R. 580 Unfunded Mandates and 8 others | 9 | 9 | 0 | 0 |
| Sep 10, 2025 | H.R. 5183 DC Home Rule Improvement and DC crime package | 22 | 16 | 6 | 0 |
| Dec 2, 2025 | H.R. 151 Equal Representation Act and 12 others | 13 | 12 | 1 | 0 |
| Jan 21, 2026 | Contempt resolutions (William J. Clinton; Hillary R. Clinton) | 4 | 2 | 2 | 0 |
| Feb 4, 2026 | H.R. 7274 FASC Improvement and 8 others | 9 | 9 | 0 | 0 |
| Mar 18, 2026 | H.R. 6916 Federal Program Integrity and Fraud Prevention and 8 others | 9 | 0 | 0 | **9** |
| Apr 29, 2026 | H.R. 8463 Pre-Payment Fraud Prevention and 8 others | 9 | 9 | 0 | 0 |
| May 20, 2026 | H.R. 8096 Duplication Scoring Act and 5 others | 6 | 2 | 0 | 4 |
| Jul 22, 2026 | H.R. 6610 Pharmacists Fight Back and 3 others | 4 | 4 | 0 | 0 |

Also: Jan 14, 2025 organizational meeting, 8 roll calls, voted on all 8. Recorded votes taken during hearings (motions to subpoena or table): 7 across five hearings; he voted on 4 (Sep 18, 2025 Aye; Mar 4, 2026 No x3) and was not voting on 3 (Feb 5, 2025 and Jan 7, 2026, hearings at which the transcript lists him present, so he was there at some point but not at the vote; Jun 5, 2025, hearing he did not attend).

**Same-day context for the three markups where he cast no votes:**
- Mar 25, 2025 (markup 10:00 AM, 26 roll calls): Energy Subcommittee hearing on grid reliability, 10:15 AM; its transcript lists him present. Voted on all 3 floor votes (1:54 PM onward).
- Apr 30, 2025 (markup 10:00 AM, 28 roll calls on the reconciliation print and amendments): Energy Subcommittee hearing, 10:15 AM; its transcript lists him present. Voted on both floor votes (5:40 PM, 5:49 PM). The Oversight reconciliation markup was the committee's vote on the federal-employee retirement and FEHB provisions later enacted in H.R. 1, which he voted for on the floor (Roll Call 190, July 3, 2025).
- Mar 18, 2026 (markup 10:00 AM, 9 roll calls): Health Subcommittee hearing, 10:15 AM (no transcript published yet). Voted on all 4 floor votes (5:13 PM onward).
- Partial days: Feb 25, 2025 (2 of 4; E&C full-committee markup 10:30 AM) and May 20, 2026 (2 of 6; E&C Health Subcommittee hearing 2:00 PM; 11 floor votes from 1:03 PM).

## Caveats
- Transcripts publish with a lag of weeks to months; hearings after March 2026 with no transcript yet are not counted. The docs.house.gov calendar shows no further full-committee hearings between Mar 4 and Sep 9, 2026, but the calendar can lag or omit reschedules. The denominator is "hearings with published transcripts," cross-checked against the calendar.
- The roster records who appeared at any point, not for how long.
- Absence from an Oversight event can reflect a simultaneous Energy and Commerce or Rules Committee proceeding; the same-day rows above list what is documented, and floor votes only establish he was in Washington that day.
- Event kinds come from the docs.house.gov event page heading ("Hearing:", "Markup of", "Meeting:"). Vote sheets are as posted by the committee; any unposted roll call would not appear here.
- "Not voting" on a sheet is inferred from the absence of a mark in his row on the committee's own sheet. Spot checks of the retained text layer are encouraged before quoting any single vote.
