# NY-23 Accountability Tracker — Project Status

*Last updated: August 31, 2026*

---

## Site

**Live at:** langworthywatch.org  
**Deployment:** Cloudflare Pages (project `langworthywatch`) via `wrangler` direct upload — auto-deploys at session end via the Stop hook. Migrated off Netlify 2026-06-14 (Netlify credit-wall). `langworthywatch.org` = Cloudflare-proxied CNAME → `langworthywatch.pages.dev`.  
**Repository:** LangworthyWatch/ny23-accountability  
**Git remote:** `https://github.com/LangworthyWatch/ny23-accountability.git`  
**Push method:** `gh auth setup-git` credential helper (LangworthyWatch account, stored in keyring)

> **SSH note:** Deploy key (`id_ed25519_langworthywatch`) is read-only. Port 22 is currently unblocked but HTTPS + `gh auth setup-git` is the reliable push path.

---

## Content: 155 Fact-Checks Published

### Topics Covered

| Series / Topic | Entries | Status |
|---|---|---|
| July 25 donor + veterans batch (**3 held for right of reply**) | 3 | Drafted 2026-07-25, all `draft:true` + `hold_reason` — Landa donor public record (DOCUMENTED PATTERN; 2 ProPublica investigations, 2 NY AG fraud suits naming him, HHS OIG audit, his own dismissed defamation suit); AIPAC money and record (DOCUMENTED PATTERN; $25K direct + $76,016 bundled = $101,016 from AIPAC's own Schedule B, **zero** super-PAC independent expenditures ever, and he personally sponsored + floor-managed H.Res. 1227, the closed rule for an Israel arms bill); veterans impact (DOCUMENTED PATTERN; 7 war-powers votes all Nay, DCAS casualty count revised *downward*, H.R. 9237 §108 future-claim rating cuts, VA backfill freeze, research staffing −5.1%, and his seat on Oversight). **Three published figures corrected this session** — see below |
| **Corrections issued 2026-07-25** | 2 | Landa contribution total **$68,700 → $55,000** (FEC memo entries were being summed as separate gifts; propagated to 8 files incl. 3 live entries + 2 cards). Missed-votes page rebuilt: its table summed to 69 against a header of 66, and a "Late 2024 Spike (8.2–8.9%)" was fabricated from bad data when the real figures were 0.8% and 0.0%; two causal claims about campaign season removed as speculation. Both carry dated public Correction sections |
| July 21-22 Facebook-post batch (transcript-verified) | 2 | Complete 2026-07-22 — Stock trading ban sell-loophole (MISLEADING: H.R. 7008 cosponsor bans buying, not selling; bill sponsor Steil conceded "accurate but misleading" at the Rules Cmte. hearing; Section 3 Voter ID rider confirmed against the actual RCP2 bill text); Chautauqua mental-health grant announced twice, 1,037 days apart (MISSING CONTEXT, resolved from a 7/17 draft). Both used direct video/hearing transcription (yt-dlp+Whisper, youtube-transcript-api) rather than news paraphrase |
| July 16-17 Facebook-post batch (transcript-verified) | 8 | Complete 2026-07-17 — Nick Shirley fraud-video amplification (MISSING CONTEXT), Canada wildfire smoke "policy choice" (MISLEADING), BUSES Act (MOSTLY TRUE), critical-minerals hearing (MOSTLY TRUE), biosimilars H.R. 9661 (MOSTLY TRUE), FFA/CAREERS Act (MOSTLY TRUE), Allegany water 3rd-announcement (DOCUMENTED PATTERN), rural-health-fund Centralus repeat (MISSING CONTEXT). Established FB-reel + YouTube transcription workflow (yt-dlp + Whisper / youtube-transcript-api); transcripts under research/transcripts/ |
| Rules Committee gatekeeper (synthesis: Medicaid, tariffs, veterans, Epstein) | 1 | Complete 2026-07-16 (DOCUMENTED PATTERN); Epstein oversight-record entry also expanded w/ full vote + attendance record |
| NY Utility Rates (data investigation) | 12 | Complete |
| IDA donor-to-exemption pattern | 3 | Complete; 74 donors documented |
| One Big Beautiful Bill / OBBBA | 4 | Complete (SNAP, working families, WFTC, real-cost framing) |
| Iran war / Operation Epic Fury (Feb 28 statement, DHS pivot, cost vs. cuts) | 3 | Complete — cost-vs-cuts entry added 2026-06-18 (DOCUMENTED PATTERN) |
| Minnesota fraud (hearing claims + comparative + 50-state/stayed-buried) | 3 | Complete |
| Immigration framing (incl. Marilla "voted to defund") | 4 | Complete |
| FEMA / disaster recovery (Jasper-Troupsburg $60.5M, MOSTLY TRUE + BRIC context) | 1 | Complete — watching for his position on Review Council / BRIC |
| Farm Bill (SNAP, House Ag, telehealth, USDA cuts) | 1 (4 sections) | Complete — update when Senate acts |
| Scotland trip / "service over self" | 1 | Complete |
| FeedMore WNY earmark vs. cuts | 1 | Complete — monitor for Langworthy statement |
| "Big Brother" / FISA 702 | 1 | Complete — update at next reauthorization |
| DHS security incidents | 1 | Complete |
| ActBlue subpoena framing | 1 | Complete |
| Jamestown USCP RFI | 1 | Appeal filed 2026-04-26; awaiting response |
| Healthcare / CEO hearing | 1 | Complete |
| SAVE Act (voter ID) | 1 | Complete |
| SW Flight 2094 | 1 | Complete |
| County rural impact profiles | 3 | Steuben, Tioga, Schuyler complete; 5 counties not started |
| Scaffold Law §240 (worker safety, Infrastructure Expansion Act, reauthorization rider) | 3 | Complete — Dec/May entries hardened + reauthorization entry added 2026-06-24; primary-sourced (NYCOSH, Times Union/Dan Clark, City & State/Espaillat) |
| Credit-claiming vs. record (FY27 hospital radiology *requests*; Jamestown tariff tour) | 2 | Added 2026-06-24 — MISLEADING + MISSING CONTEXT |
| Disclosure Gap (donor→action series framing; ties Seneca/nursing-home/Corning/NAHB/Energy Choice + district-office geography) | 1 | Added 2026-06-24 — DOCUMENTED PATTERN |
| Rules Committee closed-rule pattern (Medicaid "Seat at the Table" incl. E&C markup + 5 closed rules; tariff-termination blockade; HR 9237 veterans vote) | 3 | Added 2026-07-03 — DOCUMENTED PATTERN; by-name committee votes from H. Rept. 119-5/-106/-113/-152/-179/-372/-707; VA + propane entries updated with the committee record |
| Buffalo July 4 fireworks / Somali flag | 1 | Added 2026-07-02 — MISLEADING |
| Northern Border Security Enhancement and Review Act (H.R. 5517: reporting/review bill vs. "enforcement" branding; GAO staffing findings) | 1 | Added 2026-07-06 — MISSING CONTEXT; verified vs. govinfo BILLSTATUS + GAO testimony |

### Verdict Distribution

MISLEADING (most common) · MISSING CONTEXT · CONTRADICTION · DOCUMENTED PATTERN · FALSE · MOSTLY TRUE · NOT SUPPORTED · DEFLECTION

---

## Graphics Pipeline

Scripts in `social-media/` and `~/Downloads/`. Output PNGs → Desktop for posting.

**Card toolkit (added July 2026):** new cards import `social-media/lib/card.py` — shared house-style primitives (brand bar, gold verdict badge, panel, bulleted column, kicker, footer, photo hero), logical-1080 coordinates with optional supersampling, and an em-dash guard in `save()`. The `/social-post` command builds a caption + card together in the scorecard format (headline-first, verdict-matched) with the ≤2200-char and em-dash checks. Canonical cards are **light 1080×1080**; the "1200×1100" spec below is legacy.

**Card audit step (added 2026-07-22):** `/social-post` Step 5 now requires reading the actual rendered PNG and checking it against the two strongest precedent cards (`beagle_count_contrast_card.png`, `shared_earmarks_card.png`) for stat-first design (one big glanceable number, not quote-dense panels), no dead space before the footer, and correct color logic. Added after a first-pass Chautauqua-grant card led with two paragraph-of-quotes panels and had to be redesigned around a hero stat ("1,037 days apart"). New scripts: `create_insider_trading_sell_loophole_card.py`, `create_chautauqua_grant_repeat_card.py`.

**Standard format:**
- Size: 1200 × 1100–1220px
- Background: `#F5F7FA` (light gray)
- Header bar: `#1E3A5F` (navy), white text, `LANGWORTHYWATCH.ORG`
- Two-column: green-tinted left ("what he says/does"), red-tinted right (contrast)
- Verdict bar: gold (`#D69E2E`) on cream, bold verdict label + one-line summary
- Footer: navy bar, `langworthywatch.org · NY-23 Accountability · All sources public record`
- Font: Arial Bold for headers/labels, Impact for large numbers, Arial for body

**Active scripts (`social-media/`, June 10 batch):**
- `create_minnesota_50state_card.py` → `minnesota_50state_claim.png`
- `create_marilla_defund_card.py` → `marilla_defund_claim.png`
- `create_jasper_troupsburg_card.py` → `jasper_troupsburg_fema_award.png` (first MOSTLY TRUE / green-badge card)
- `create_epic_fury_cost_card.py` → `epic_fury_cost_vs_cuts.png` (house-style 1080×1080; Epic Fury cost vs. cuts, DOCUMENTED PATTERN — added 2026-06-18)
- `create_scaffold_cost_vs_safety_card.py` → `scaffold_cost_vs_safety.png` (house-style 1080×1080; Scaffold Law cost pitch vs. safety law, MISSING CONTEXT — added 2026-06-24)
- `create_disclosure_gap_card.py` → `disclosure_gap_donor_pattern.png` (house-style 1080×1080; donor→action pattern, DOCUMENTED PATTERN — added 2026-06-24)
- `create_responsiveness_card.py` → `responsiveness_you_spoke.png` (house-style 1080×1080; "You spoke. I listened." responsiveness asymmetry — added 2026-06-24)

**Active scripts (`~/Downloads/`):**
- `create_scotland_service_graphic.py` → `langworthy_scotland_service.png`
- `create_feedmore_graphic.py` → `langworthy_feedmore.png`
- `create_farmbill_snap_graphic.py` → `langworthy_farmbill_snap.png`
- `create_houseag_graphic.py` → `langworthy_houseag_claim.png`
- `create_telehealth_graphic.py` → `langworthy_telehealth_budget.png`
- `create_usda_cuts_graphic.py` → `langworthy_usda_cuts.png`
- `create_bigbrother_graphic.py` → `langworthy_bigbrother_fisa.png`
- `create_minnesota_fraud_graphic.py` → `langworthy_minnesota_fraud.png`

---

## Active Investigation Threads

| Thread | Status | Next step |
|---|---|---|
| Landa / nursing-home donor | **Drafted 7/25**, held | Send right of reply to Benjamin Landa's representatives (spokesman of record: Mark Weiss) + Langworthy's office; 10 business days. Excluded-as-unverified list is in FINDINGS_BACKLOG — do not reintroduce from a search summary |
| AIPAC money and record | **Drafted 7/25**, held | Request for comment + Wayback archiving. Also decide whether to rescope `content/campaign-finance/_index.md`, whose OpenSecrets AIPAC figure ($31,550, 2024 only) is ~1/3 of the primary-source cross-cycle total |
| Veterans: war, casualty count, VA system | **Drafted 7/25**, held. Full source-verification pass run 7/26 across all sections; ~15 corrections applied (see below) | **DoD response to the 12-senator Hirono letter due 7/30** — reminder scheduled. Then request for comment; MBA Q2 foreclosure refresh mid-Aug. Rebranding thread and a new VA home-loan foreclosure section are now INTEGRATED, not pending |
| Buffalo flag posts / causal-claim pattern | **Drafted 7/26**, held (`2026-07-25-flag-raising-posts-causal-claims`, NOT SUPPORTED) | Deduped against the live 7/2 Buffalo entry after a propagation sweep found it already covered the same posts. Remaining gate: request for comment. All four post screenshots filed |
| Essential Plan cliff (July 1) | **Published 7/2** (MOSTLY TRUE) + cross-refs in beagle/town-hall entries | Watch Aug 30 QHP enrollment deadline; Hochul 127k-in-GOP-districts figure logged for possible add |
| June 25 tele-town hall | **Published 7/2** (MISLEADING, "hospitals aren't going anywhere") + full disclaimered transcript in /documents/ | Remaining town-hall claims to check: 11% refunds, Virginia CDL crash attribution, 70k nurses figure |
| Liberty Strategies | **Published 7/2** (MISSING CONTEXT; office no-response by 7/1 deadline noted; $1 FEC total corrected; two-firms chronology + stocks-TRUE contrast added) | COELIG FOIL arc continues; update entry if office responds |
| Sponsored travel pattern | Research logged 7/2 (Israel 4/2024, Greece 4/2025, Ireland/UK 3-4/2026 — member-traveler, primary-confirmed) | Clerk gtimages PDF server 404s on all docs; retry for dollar amounts, then entry |
| Beagle "475 by end of August" claim | Logged with Sept 1 action date | Verify transfer happened; entry count now 30 (manual, screenshot-archived) |
| Newstead $5M shared earmark | **Published 8/15** (MISSING CONTEXT; comment-request absence disclosed on the page) | Update the entry if the office ever responds to the joint-request question |
| Local Cops ICE quote | **Drafted 7/31**, held (`2026-07-31-local-cops-law-sheriff-quote`, MISSING CONTEXT) | Quote is Sheriff Todd Hood's, not Langworthy's, and accurately reproduced; the same interview has Hood saying operations do not change. Gates: no absolute timestamp established (relative timestamps only), request for comment. Source confirmed as the CAMPAIGN page, ChairmanNickLangworthy |
| Office communications spending | **Published 8/6** as an update to the tele-town hall entry; dataset at `/data/office_communications_spending.csv` | 13 quarters of House disbursements: $623,882 advertising vs $281,795 on 38 tele-town halls. Re-check when Apr-Jun 2026 SOD publishes. NEGATIVE findings recorded: no franking blackout violation (60-day rule, all buys outside), no official/campaign vendor overlap |
| State of the District, 8/6/26 | **LEAD, single-source, unverified** (FINDINGS_BACKLOG 8/6) | Wellsville Sun says he delivered it "to a private audience at a location undisclosed to the public." Now retrospectively checkable. Needs his office's own announcement + a second outlet before use; a State of the District address is a speech, not a town hall |
| Moog "millions for Moog" | **Drafted 8/14 via background agent, verified 8/15, held** (`2026-08-14-moog-defense-credit-claim`, MISSING CONTEXT). Card+caption built, caption carries DO-NOT-POST | Gates: FB permalinks; whether the $7M photonics transfer survived into the P.L. 119-75 explanatory statement (printed ~Jan 21 2026, not yet located); ALPA article archive (Cloudflare 520); office chance to produce Artemis/control-systems documentation |
| Aug 12 "delivered" list, 10-of-10 | **Complete 8/15.** All ten classified; instances 5-6 added to the May 20 grants entry (live); full scorecard card+caption cut and committed | Post-ready. Aggregate: 6 of 10 agency grants, 2 clean (Jasper-Troupsburg, Elmira College), 2 shared earmarks |
| Teamsters endorsement / labor record | **Published 8/28** (MISSING CONTEXT) + card/caption | Two votes June 9: Nay on the discharged rule (RC 215, 5:30pm), Yea on the bill (RC 216, 7:05pm); did NOT sign petition 119-19 (verified against the Clerk's list, 211D+7R); $0 Teamsters PAC money; 0 of 358 sponsored/cosponsored measures is a trucking bill. Corrected three claims from circulating research on the page |
| ACC IE / H.R. 7502 (mass balance) | **Published 8/26** (MISSING CONTEXT) + card/caption | $95,900 FEC Form 5, only outside money in NY-23; ACC's $1M program, all four House recipients on E&C; Q3 2025 LDA named the bill pre-introduction. Comment-request absence disclosed on page |
| NYCBS oncology money / H.R. 9661 | **Published 8/28** (DOCUMENTED PATTERN) + row on donor map card | $55,137 ($40,137 bundles + $15,000 Conquering Cancer PAC; third check 15 days pre-introduction); ~$2.4M national program (Politico 10/2024 anchor); fair reading at full strength (FDA policy predates, Paul's S.1414, bipartisan). Watch: H.R. 9661 BILLSTATUS markup catch-up; COA Q3 LDA due Oct |
| Donor/bill map card (5 rows) | Card + caption ready 8/28 | Roundup: Energy Choice $107,263 / RMAA $95,900 / Safer Skies $113,500 / Seneca $10,100 / Biosimilars $55,137; every row has a published entry |
| Preemption entry: NPA addendum | **Updated 8/28** (live) | NPA PAC $5,000 on 3/26/2026, seven weeks post-introduction of H.R. 7366; NPA sued NY over the very law the bill preempts (dismissed 4/2024). Litigant-to-donor sequence; candidate for its own card |
| Seneca entry: business cluster | **Updated 8/28** (live) | +$7,500: three Seneca-territory tobacco businesses, $2,500 each, same day (8/7/2025); ownership explicitly left open. Nursing-home entry's wrong FEC candidate ID (H2NY23133 -> H2NY23228) also fixed |
| september-house-watch (scheduled task) | **Created 8/31**, Tuesdays 9am | Nine triggers (CR, H.R. 1834, H.R. 9393 text, FLCA/S.1414 Senate, H.R. 9661 record, IIJA/Scaffold, FY27 approps, DHS expo, roll sweep); log-only, self-expires ~Oct 6. First digest 8/31: baseline roll 285; one erroneous flag (veterans Roll 282) caught and retracted same day |
| DHS expo / "left hates law and order" | Logged 8/28, action date 9/2 | Official-page post; expo relocated to USCG Buffalo; venue offered no-ICE hosting. Hold for second instance |
| Lake Erie wind / utility bills | **Published 8/21** (MISLEADING) + card/caption | Campaign-page posts from the 8/18 Hamburg rally with Blakeman and CAWTILE. Gates carried forward: permalinks for the 8/19 3:01 PM and 8/20 posts (screenshots only); campaign never asked which Lake Erie project the posts mean. Blakeman data-center-moratorium section added from his own NY1 quotes |
| NY Harbor capsizing / immigration framing | **Published 8/21** (MISSING CONTEXT) + card/caption | Built on the sworn SDNY complaint (26 MAG 3226, local copy in research/sources). Complaint never mentions immigration and "reckless" is not the charge. Office comment request drafted at `research/briefs/2026-08-21-office-request-capsizing.md` but **not sent**; append any response |
| Trump Accounts "every American child" | **Published 8/21** (MISSING CONTEXT) + card/caption | $1,000 is citizen children born 2025-2028 only; NY-23 birth-cohort table from NY DOH Table 7 + Census. JCT score resolved to $15.2B via JCX-35-25 (Brookings' $2.3B was contributions only). CRS R48910 and the Tax Notes ITIN piece were unretrievable and are not cited |
| CHECK Act "price tags" | **Published 8/21** (MISSING CONTEXT) + card/caption | H.R. 9117: zero cosponsors, no action since 6/3, absent from both E&C markups. Nothing in it posts a price before care. Contrast is Roll Call 11 (Nay) + NY State of Health premium data. Open: whether CHECK Act text was folded into the H.R. 9393 substitute — reported text not yet published on govinfo; recheck when it is |
| FB sweep leads (7/2) | Logged | Roswell/LUNGevity (commenters raising Medicaid contradiction), UPMC Chautauqua $300K x3, $2.3M airports, critical minerals, Air Methods |
| Farm Bill — Senate action | Published; watching | Update when Senate moves |
| FeedMore WNY | Published | Monitor for any Langworthy statement |
| FISA 702 | Published | Update at next reauthorization vote |
| Blackstone → Huizenga | Research complete; NOT published | Needs reframe: carried interest vote + Basel III are clean claims; INVEST Act provision was Ann Wagner's bill, not Huizenga's |
| Jamestown USCP RFI denial | Published | USCP appeal filed 2026-04-26; awaiting response |
| County profiles | 3 of 8 done | Chemung, Cattaraugus, Chautauqua, Erie, Allegany remaining |
| H.R. 6047 veterans loan fees | Drafted + verified; NOT published | Entry in repo as draft: true; needs archive pass + review + publish. Rules votes 342/343 + CBO figures all primary-sourced |
| FEMA Review Council / BRIC | Watching | No Langworthy statement located (checked June 10) on May 7 report, BRIC cancellation, or staffing cuts; Jasper-Troupsburg entry carries the open questions |
| Scaffold Law reauthorization | Published (3 entries) | Watch ~Sept 2026: whether H.R. 3548 §240 preemption gets attached to the surface-transportation reauthorization before the IIJA expires Sep 30 (logged in FINDINGS_BACKLOG); also UPMC/Arnot FY27 CPF requests — revisit if a FY27 approps bill passes |
| June 10 FB post permalinks | Pending | Minnesota, Marilla, Jasper-Troupsburg entries quote posts verified from screenshots; need permalinks + screenshots archived to static/images/ |
| Economic attribution report (imported 2026-06-11) | Monitoring thresholds | Watch: OTDA county SNAP caseloads (June–Sept first benefit-loss window); NY DOH Medicaid Enrollment Databook; first RHTP disbursement to a named district hospital; NY PSC final NYSEG/RG&E rate orders (~24%/26% requests pending); NY DOL WARN for Jamestown/eSolutions; Essential Plan cliff July 1. Entry candidates remaining: WSKG/H.R. 4 rescissions (clean vote+quote), Essential Plan July 1 response prep |
| Rules Committee closed-rule pattern | **Published 7/3** (3 entries, DOCUMENTED PATTERN) | Complete: "Seat at the Table" (E&C markup — he voted to advance the Medicaid subtitle + spoke defending it, primary-verified quotes; 5 closed rules incl. Nov 2025 CR minibus RV 195/199/200/202/205), tariff-vote blockade (H.Res.211/313), HR 9237 veterans (RV 369/373). Backlog: browser-archive CRPT-119hrpt106-pt1 + 119-372 to Wayback |
| HR 9237 attribution correction | **Fixed 7/3** | A House Veterans' Affairs Committee GOP post was initially misattributed to Langworthy; pulled the live entry (_redirects 301) + reframed around his actual Rules vote. Lesson logged to shared LESSONS.md (verify a quote's author before publishing) |
| "Secured" earmark credit-claiming (CPF, past-tense) | **Published 7/9** (Olean PD, DOCUMENTED PATTERN) + card/post | Third instance of announcing not-yet-funded FY27 CPF requests as "secured/delivered" (Feb FY2026 credit-claim → June UPMC/Arnot radiology → July Olean $1M). Olean corrected 7/9 to **USDA Rural Development** vehicle (not CJS); single federal request, 1959 station. Revisit all three if a FY27 approps bill passes or gets zeroed |
| Liberty Strategies / Erin Langworthy FDS (donor-disclosure) | Held draft + right-of-reply sent | Entry `2026-06-24-liberty-strategies-disclosure` is **draft:true**; right-of-reply submitted via the House web form June 24 (response requested July 1); scheduled task `publish-liberty-strategies-disclosure` finalizes + publishes **July 2** (asks for the response status first). Federal-only client revenue (Reed/Jacobs/Singletary, $103,604.99); NYS BOE shows no vendor income; Liberty Opinion Research (Nick's prior firm, Erie clients) is COI-paused and stays out. **Do NOT publish before the reply window.** Workspace: `imported-from-public-ledger/erin-baker-2026-05-02/` |

---

## Workflow

### New Fact-Check

```bash
cd langworthy-tracker
# Create file
# content/fact-checks/YYYY-MM-DD-descriptive-slug.md
# Archive all source URLs before publishing:
curl -s -I "https://web.archive.org/save/[URL]"
# Build and verify
hugo server -D
# Commit and push
git add content/fact-checks/YYYY-MM-DD-slug.md content/fact-checks/_index.md
git commit -m "feat: add [topic] fact-check"
git push origin main
```

### New Graphic

```bash
# Write script to ~/Downloads/create_[topic]_graphic.py
# Run it
python3 ~/Downloads/create_[topic]_graphic.py
# Output: ~/Downloads/langworthy_[topic].png
# Copy to Desktop for posting
cp ~/Downloads/langworthy_[topic].png ~/Desktop/
```

### Push (if credential helper needs re-setup)

```bash
gh auth setup-git
git push origin main
```

---

## Content Standards (summary)

- All sources must be archived via Archive.org before publishing
- No speculation, no opinion presented as fact
- Verdict labels from approved taxonomy only
- County tags required for district-specific entries
- Cross-links to related entries at bottom
- "In plain language:" summaries after data-heavy sections
- Cite thepublicledgers.org for IDA/subsidy underlying data (not raw data on LW)

---

## Cost

- Hosting: $0 (GitHub Pages)
- Domain: ~$12/year (langworthywatch.org)
- Analytics: Google Analytics (free tier)
- Donations: Donorbox (fee on donations only)
