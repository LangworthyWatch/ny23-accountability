# Langworthy on House Energy and Commerce, 119th Congress: committee activity record

Pulled Oct 16, 2026. This is research only; nothing under `content/` was edited. It covers markups, recorded committee votes, amendments he offered, subcommittee seats, hearing participation, and E&C-related press releases. His sponsored and cosponsored bills (govinfo BILLSTATUS) are covered by a separate agent and are not repeated here.

## Sources and method

- **docs.house.gov Committee Repository.** `ByComm.aspx?Code=IF00` returns 404 to curl. The month calendar is ASP.NET postback-driven, so `scripts/months.py` walked `Calendar/ByMonth.aspx?Code=<code>` back 23 months for IF00 (full committee) and for IF02, IF03, IF14, IF16, IF17 and IF18 (subcommittees). That found 135 events from Jan 2025 to Oct 2026, listed in `docs-house-ec-events-2025-2026.csv`, with page text in `docs-house/event-pages/`.
  - Every E&C hearing date with a govinfo transcript appears in this event list (0 missing), which suggests the event list is complete.
- **Roll calls.** Each event's "Votes" section links per-vote PDFs (`CRPT-119-IFxx-VoteNNN-date.pdf`). We downloaded all 280 to `docs-house/rollcall-pdfs/`, ran pdftotext, and used OCR for 4 scanned files. `scripts/parsevotes.py` reads the X column on the "Mr. Langworthy" row, and the output is `ec-recorded-votes-119.csv`. A spot-check of 8 random Yea/Nay rows plus every "Not voting" row against the PDF text matched in every case.
- **Vote summaries.** 30 vote-summary PDFs are in `docs-house/vote-summaries/`. Most are scanned, so their `.txt` versions are OCR and imperfect.
- **Subcommittee seats.** The Clerk pages for each subcommittee are in `clerk/`. The committee's member page is `ec-site/representative-langworthy.*` and the subcommittee pages are `ec-site/subcommittee-*`.
- **Hearing transcripts.** The govinfo search API (`DEMO_KEY`, query `collection:CHRG congress:119 Langworthy`) returned 127 packages, 46 of them E&C. Speaker turns were counted by matching lines that begin `Mr. Langworthy.`. The table is `ec-hearing-transcripts-govinfo.csv`, and the 12 transcripts where he speaks are in `govinfo-hearings/`.
- **Press releases.** We pulled langworthy.house.gov press releases from Nov 2024 to Oct 2026: 148 releases across 15 listing pages. They are saved in `press-releases/` (one `.txt` per release plus `index.json`).

## 1. Recorded committee votes

**Full committee: 221 roll calls with per-member tallies posted, from Feb 25, 2025 to Sept 16, 2026. Langworthy: 92 Yea, 107 Nay, 22 not voting.** He missed 22 of 221, about 10%.

The 22 missed votes fall on 7 markup days:

| Date | Missed |
|---|---|
| Feb 25, 2025 | 6 (all Democratic amendments to the Oversight Plan; RC #8 failed **23-23**) |
| Jan 21, 2026 | 5 (RC #16-20) |
| Sept 16, 2026 | 5 (RC #1, 4, 5, 15, 16) |
| June 25, 2025 | 3 (RC #15 H.R. 3617 final; RC #19-20 H.R. 1949 LNG) |
| Apr 29, 2025 | 1 |
| May 13, 2025 | 1 |
| Mar 5, 2026 | 1 (H.R. 3149 App Store Accountability final) |

**His subcommittees: 40 roll calls with tallies posted. Energy: 27 (13 Yea, 14 Nay). Environment: 13 (7 Yea, 6 Nay). He missed 0.** The Health subcommittee posted no per-member roll calls.

Key votes:

- **H.R. 1047, GRID Power Act**, final passage June 25, 2025: 28-23, Yea.
- **H.R. 3157, SEAA**, June 25, 2025: 27-20, Yea.
- **H.R. 3699, Energy Choice Act**, Dec 3, 2025: 24-21, Yea.
- **H.R. 4690**, Dec 3, 2025: 27-21, Yea.
- **H.R. 7502, Recycled Materials Attribution Act** (his bill), Sept 16, 2026, RC #3: Yea.
  - **The two official committee documents disagree on the tally.**
    - The roll-call PDF (`CRPT-119-IF00-Vote003-20260916`) says "28 Ayes and 19 Nays", and its member grid shows Democrats in the Nay column.
    - The committee's own Vote Summary (SD007, checked visually against the page image, not OCR) says "Agreed to, 28 Yeas – 0 Nays".
    - The summary also gives 25-0 for H.R. 6832. Treat the summary tallies as unreliable, and do not cite a margin without flagging the conflict.
- **May 13, 2025 reconciliation markup** (Title IV committee print): RC #38 and #39 transmit motions, 30-24, Yea. He voted Nay on Democratic amendments, including RC #33-37.

**Gaps:**

- **July 20, 2026 (29 bills) and Sept 2, 2026 (10 bills) full-committee markups** posted only vote summaries, not per-member roll calls. The summaries show recorded votes (for example 49-0, 39-10, 24-21, and 26-22 on BUSES H.R. 9317). His votes there are unknown.
- Sept 16, 2026 has 15 of 16 roll calls posted. Dec 10, 2025 Environment RC #1 links to an amendment text instead of a tally.
- Committee report H. Rept. 119-482 prints its vote tables as "[GRAPHIC(S) NOT AVAILABLE]".

## 2. Amendments he offered

The only amendments found are two, both on his own bills, at the **Nov 19, 2025 Energy Subcommittee markup**. The source is the vote summary `docs-house/vote-summaries/118694-HMKP-119-IF03-20251119-SD5029.txt`, whose "Sponsor" column names the offeror.

- **MA_01 to H.R. 3699, Energy Choice Act**: "Strike section 2(b)". Agreed to by voice vote.
  - The minority views in H. Rept. 119-482 (fetched from govinfo and saved here) (`CRPT-119hrpt482.txt`) say a subcommittee amendment stripped the bill's definition of "energy". That appears to be this amendment, but section 2(b) was not checked against the bill text.
- **ANS_HR4690_01**, an amendment in the nature of a substitute to **H.R. 4690**. Agreed to by voice vote, and the bill was then forwarded 16-14.

The amendment PDFs themselves say "OFFERED BY M_. ____", so attribution rests on the summary. The filenames carry bioguide L000600, but the same repository tags minority amendments "A000370", so the filename ID alone is not proof.

No full-committee amendment by Langworthy was found in any event page or any parsed roll call or summary. The OCR'd summaries are imperfect.

## 3. Subcommittees and hearings

**Subcommittee seats: Energy, Environment, and Health.** The Clerk lists him on IF03 at #13, IF18 at #11 and IF14 at #15, and the E&C member page lists the same three. His own Dec 5, 2025 release says "Energy and Environment subcommittees" and does not mention Health.

**No official hearing attendance record exists.** docs.house.gov lists witnesses but not attending members, and the transcripts do not take attendance. The only evidence of participation is that he spoke.

govinfo has published 46 E&C transcripts, covering hearings through Mar 26, 2026; 2026 coverage lags. **He spoke at 12 of them:**

| Subcommittee | Transcripts published | Hearings where he spoke | Hearings with transcripts where he did not speak |
|---|---|---|---|
| Energy | 12 | 9 | Pipeline safety (Jul 22, 2025 and Mar 4, 2026), Winter Storm Fern (Mar 17, 2026) |
| Environment | 6 | 1 (Jan 22, 2025) | 5 |
| Health | 5 | 3 (Feb 6, 2025; Apr 1, 2025; Jan 8, 2026) | 2 |

Energy hearings where he spoke:

- Feb 5, 2025
- Mar 5, 2025
- Mar 25, 2025
- Apr 30, 2025
- June 10, 2025 (questioning the Energy Secretary on the DOE budget)
- Sept 9, 2025
- Sept 16, 2025 (Energy Choice Act and Reliable Federal Infrastructure Act legislative hearing)
- Dec 2, 2025

No speaker turns were found at full-committee hearings (Apr 9, 2025; Dec 12, 2025 Member Day). Not speaking is **not** proof of absence. First-sentence excerpts are in the CSV.

Separately, docs.house.gov lists two hearings with his bills on the agenda:

- H.R. 1617, Sept 18, 2025, Communications and Technology
- H.R. 9117, CHECK Act, June 10, 2026, Health

## 4. E&C-related press releases (claims to check)

| Date | Title (short) | What it claims |
|---|---|---|
| 2024-12-13 | Named to E&C | Appointed; "first member of Congress in modern history to represent the Southern Tier counties on this ... committee" |
| 2025-02-27 | Broadband permitting | Introduced Wireless Resiliency and Flexible Investment Act |
| 2025-03-07 | Medicaid Provider Screening Accountability Act | Introduced, with co-lead Morelle |
| 2025-05-02 | SEAA | Introduced H.R. 3157 |
| 2025-05-12 | Reconciliation statement | "as the only Republican from New York serving on the Energy and Commerce Committee, I was proud to help lead that charge" on rural hospitals and Medicaid. The Clerk roster lists no other NY Republican (only Tonko, Clarke and Ocasio-Cortez). "Help lead" is not documented in the markup record. |
| 2025-06-05 / 06-20 | Energy Choice Act | Introduced; press conference |
| 2025-07-23 | Reliable Federal Infrastructure Act | Introduced |
| 2025-08-29 | $5.1M pipeline safety grant | Announces a PHMSA grant; describes himself as on E&C |
| 2025-11-19 | Energy Choice passes subcommittee | "passed out of the House Energy Subcommittee". The vote was by voice (summary SD5029). |
| 2025-12-05 | Energy Choice passes E&C | "passed out of the ... Committee, clearing the final hurdle". Roll call 24-21 on Dec 3. "140 bipartisan co-sponsors" |
| 2025-12-29 | CMS rural hospital funds | "As a member of ... E&C, I was proud to help advance the policies that made this investment possible". He voted for the May 13 reconciliation transmit motions. |
| 2026-02-04 | Dietary Supplement Regulatory Uniformity Act | Introduced |
| 2026-05-08 | Give Kids a Chance Act | "proud to throw my full support behind". Enacted in the FY2026 omnibus. His cosponsorship was not checked here. |
| 2026-06-03 | CHECK Act | Introduced |
| 2026-06-16 | BUSES Act (with Gottheimer) | Introduced; "expected to receive consideration" at E&C. It was later reported Sept 2 by 26-22 per the summary, which lists him as a sponsor. |
| 2026-06-30 | KIDS Act passage | Statement only |
| 2026-07-15 / 10-02 | Biosimilars bills | Introduced |
| 2026-07-21 | FLOWS Act (hydropower) | Introduced |
| 2026-08-31 | American Quantum Competitiveness Act | Introduced. The OCR of the Sept 16 summary appears to list Langworthy against H.R. 10163 (36-0). Verify. |
| 2026-09-04 | $76.2M rural health | "When **we created** the Rural Health Transformation Program". This is a credit claim for an OBBBA provision. |

These releases claim credit for committee outcomes in the 2025-11-19, 2025-12-05, 2025-05-12, 2025-12-29 and 2026-09-04 entries. Search for releases claiming hearing questioning: none found.

## 5. The Oct 15, 2026 post

**The full text was not found.**

- Desktop screenshot 08 shows three bullets and then the reaction bar, with no "See more".
- Mobile screenshot 2 shows the top of a fourth ⚡ line (an enlarged crop shows partial glyphs only; the text cannot be read).
- No matching text appears in press releases (the only Oct 15 release is about Chemung sewer funding) or on the langworthy.house.gov homepage.
- X syndication returned HTTP 429.

**Open question:** was the fourth line added by an edit, or is it hidden behind truncation on desktop?

## Wayback

See `wayback-verified.txt`. Only snapshots that played back with 200 and the expected text are listed there.
