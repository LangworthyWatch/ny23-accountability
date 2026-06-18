# NY-23 Accountability Tracker — Project Status

*Last updated: June 18, 2026*

---

## Site

**Live at:** langworthywatch.org  
**Deployment:** Cloudflare Pages (project `langworthywatch`) via `wrangler` direct upload — auto-deploys at session end via the Stop hook. Migrated off Netlify 2026-06-14 (Netlify credit-wall). `langworthywatch.org` = Cloudflare-proxied CNAME → `langworthywatch.pages.dev`.  
**Repository:** LangworthyWatch/ny23-accountability  
**Git remote:** `https://github.com/LangworthyWatch/ny23-accountability.git`  
**Push method:** `gh auth setup-git` credential helper (LangworthyWatch account, stored in keyring)

> **SSH note:** Deploy key (`id_ed25519_langworthywatch`) is read-only. Port 22 is currently unblocked but HTTPS + `gh auth setup-git` is the reliable push path.

---

## Content: 110 Fact-Checks Published

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

### Verdict Distribution

MISLEADING (most common) · MISSING CONTEXT · CONTRADICTION · DOCUMENTED PATTERN · FALSE · MOSTLY TRUE · NOT SUPPORTED · DEFLECTION

---

## Graphics Pipeline

Scripts in `social-media/` and `~/Downloads/`. Output PNGs → Desktop for posting.

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
| Farm Bill — Senate action | Published; watching | Update when Senate moves |
| FeedMore WNY | Published | Monitor for any Langworthy statement |
| FISA 702 | Published | Update at next reauthorization vote |
| Blackstone → Huizenga | Research complete; NOT published | Needs reframe: carried interest vote + Basel III are clean claims; INVEST Act provision was Ann Wagner's bill, not Huizenga's |
| Jamestown USCP RFI denial | Published | USCP appeal filed 2026-04-26; awaiting response |
| County profiles | 3 of 8 done | Chemung, Cattaraugus, Chautauqua, Erie, Allegany remaining |
| H.R. 6047 veterans loan fees | Drafted + verified; NOT published | Entry in repo as draft: true; needs archive pass + review + publish. Rules votes 342/343 + CBO figures all primary-sourced |
| FEMA Review Council / BRIC | Watching | No Langworthy statement located (checked June 10) on May 7 report, BRIC cancellation, or staffing cuts; Jasper-Troupsburg entry carries the open questions |
| June 10 FB post permalinks | Pending | Minnesota, Marilla, Jasper-Troupsburg entries quote posts verified from screenshots; need permalinks + screenshots archived to static/images/ |
| Economic attribution report (imported 2026-06-11) | Monitoring thresholds | Watch: OTDA county SNAP caseloads (June–Sept first benefit-loss window); NY DOH Medicaid Enrollment Databook; first RHTP disbursement to a named district hospital; NY PSC final NYSEG/RG&E rate orders (~24%/26% requests pending); NY DOL WARN for Jamestown/eSolutions; Essential Plan cliff July 1. Entry candidates remaining: WSKG/H.R. 4 rescissions (clean vote+quote), Essential Plan July 1 response prep |

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
