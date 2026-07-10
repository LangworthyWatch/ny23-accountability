# NY-23 Accountability Tracker — Project Status

*Last updated: July 10, 2026*

---

## Site

**Live at:** langworthywatch.org  
**Deployment:** Cloudflare Pages (project `langworthywatch`) via `wrangler` direct upload — auto-deploys at session end via the Stop hook. Migrated off Netlify 2026-06-14 (Netlify credit-wall). `langworthywatch.org` = Cloudflare-proxied CNAME → `langworthywatch.pages.dev`.  
**Repository:** LangworthyWatch/ny23-accountability  
**Git remote:** `https://github.com/LangworthyWatch/ny23-accountability.git`  
**Push method:** `gh auth setup-git` credential helper (LangworthyWatch account, stored in keyring)

> **SSH note:** Deploy key (`id_ed25519_langworthywatch`) is read-only. Port 22 is currently unblocked but HTTPS + `gh auth setup-git` is the reliable push path.

---

## Content: 132 Fact-Checks Published

### Topics Covered

| Series / Topic | Entries | Status |
|---|---|---|
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
| Essential Plan cliff (July 1) | **Published 7/2** (MOSTLY TRUE) + cross-refs in beagle/town-hall entries | Watch Aug 30 QHP enrollment deadline; Hochul 127k-in-GOP-districts figure logged for possible add |
| June 25 tele-town hall | **Published 7/2** (MISLEADING, "hospitals aren't going anywhere") + full disclaimered transcript in /documents/ | Remaining town-hall claims to check: 11% refunds, Virginia CDL crash attribution, 70k nurses figure |
| Liberty Strategies | **Published 7/2** (MISSING CONTEXT; office no-response by 7/1 deadline noted; $1 FEC total corrected; two-firms chronology + stocks-TRUE contrast added) | COELIG FOIL arc continues; update entry if office responds |
| Sponsored travel pattern | Research logged 7/2 (Israel 4/2024, Greece 4/2025, Ireland/UK 3-4/2026 — member-traveler, primary-confirmed) | Clerk gtimages PDF server 404s on all docs; retry for dollar amounts, then entry |
| Beagle "475 by end of August" claim | Logged with Sept 1 action date | Verify transfer happened; entry count now 30 (manual, screenshot-archived) |
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
