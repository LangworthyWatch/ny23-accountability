# LangworthyWatch — Findings Backlog

> Actionable findings, leads, and follow-up tasks surfaced during research
> sessions. Items here are unprocessed — once acted on, move to a fact-check
> entry under content/fact-checks/ or close with a disposition note.

**Last updated:** 2026-06-16

---

## Next Session — start here

**2026-06-14 (evening): all three prior carry-forward tasks advanced — OCR entry is LIVE; Schuyler drafted; SOTD/FEMA locked + staged.** Remaining carry-forward below.

1. **Post the State of the District Q2 carousel + the FEMA card** — *only the human Facebook-posting step remains.*
   - **Pre-post lock SATISFIED:** RC145 read verbatim — Langworthy = **Yea** (`clerk.house.gov/evs/2025/roll145.xml`, recorded-vote table L000600; only GOP Nays = Davidson-OH, Massie-KY). Backbone card "VOTED AYE ×2" + figures verified accurate.
   - Assets confirmed present: carousel (cover · numbers · backbone · counties) + `jasper_troupsburg_fema_award.png` in `social-media/`; post text on Desktop (`state_of_district_q2_post_text.txt`, `jasper_troupsburg_post_text.txt`). **Just needs posting to Facebook** (no automation available).

2. **Schuyler county profile — DRAFTED, pending review.**
   - File: `content/fact-checks/2026-06-14-schuyler-county-hospital-at-risk.md` (`draft:true`). Hook confirmed: **Schuyler Hospital (Montour Falls, Cayuga Health) named on Public Citizen's at-risk list** — [Fingerlakes1, Apr 21 2026](https://www.fingerlakes1.com/2026/04/21/schuyler-newark-hospitals-flagged-as-at-risk-amid-looming-medicaid-cuts/) + [citizen.org/big-ugly-threat](https://www.citizen.org/article/big-ugly-threat/) (both Wayback-archived). Both Aye votes verbatim-confirmed; reconciled to the $212M RHTP entry (no conflicting Medicaid figure); full committee list (Oversight + E&C + Rules). Builds clean.
   - **Next:** run `/fact-check-review`; then flip `draft:false`, add to `_index.md`, deploy.

3. **OCR entry — PUBLISHED + LIVE** (`2026-06-14-ocr-collapse-disabled-students.md`, `draft:false`, deployed via wrangler 2026-06-14, **verified 200 on apex**; in `_index`).
   - (a) ✅ **NY 627/1 CONFIRMED** vs the HELP "Justice Denied" PDF (Figure 2, p.7 — NY = 627 pending / 1 agreement, total across all types). Hedge removed; Figure 2 cited; [report PDF](https://www.sanders.senate.gov/wp-content/uploads/04.24.26-Justice-Denied-How-Trumps-Office-for-Civil-Rights-Reached-a-12-Year-Low-in-Protecting-Students-from-Discrimination_FINAL.pdf) linked + archived.
   - (b) ✅ Elmira (Jan 9) permalink secured ([WENY](https://www.weny.com/news/dept-of-education-returning-education-to-the-states-tour/article_90989b40-2c71-4f4d-98d7-47abd8968530.html) + WBNG + ed.gov) + archived. **STILL TO DO (polish): the AAPD (May 18) Facebook permalink** — auth-gated, needs manual capture; then replace the generic `source_url`.
   - (c) thepublicledgers.org OCR investigation **NOT yet published** — scaffold note kept; CRDC remains the cited primary; add the link when it lands.
   - Per-source Wayback snapshots captured this session (log: `/tmp/wayback_archive_2026-06-14.log`): Justice Denied PDF, WENY, Fingerlakes1, citizen.org, roll145.xml. **GAO + WBNG blocked/pending — re-run.**

**Uncommitted at session end (in `langworthy-tracker` submodule):** OCR entry (draft:false + NY 627/1 + WENY links), `_index.md` (OCR row), new Schuyler draft, this backlog update. Live site already updated via wrangler; git not yet committed/pushed (use `gh auth switch --user LangworthyWatch` before pushing).

---

## Posted to Social / Post Queue

<!-- Running record of what's been shared to social vs. ready-but-unposted. Update as posts go out; "UNCONFIRMED" = post material exists on disk but posting not verified. -->

| Item | Card / text | Live entry? | Social status |
|---|---|---|---|
| State of the District — Q2 2026 | **text + carousel** (cover · by-the-numbers · federal-squeeze · county heat-ranking) | yes (live) | **READY to post** |
| Jasper-Troupsburg FEMA ($60.5M, MOSTLY TRUE) | card + text ready | yes — corrected version **live** | **READY to post** |
| Minnesota 50-state fraud | card + text on disk | yes | **POSTED** (confirmed 2026-06-14) |
| Marilla "voted to defund" | card + text on disk | yes | **POSTED** (confirmed 2026-06-14) |
| Fraud-prevention package (MISSING CONTEXT) | none yet | yes (live) | needs card + text if sharing |
| NAHB "Defender of Housing" (MISSING CONTEXT) | none yet | yes (live) | needs card + text if sharing |

---

## Priority Findings

<!-- High-value leads that could become fact-check entries or unblock investigations -->

### Two reviewed fact-checks — LIVE (deployed via Cloudflare Pages 2026-06-14)
- **Date logged:** 2026-06-13 (resolved-live 2026-06-14)
- **Source:** June 11–12 Langworthy FB posts → /ny23-fact-check → /fact-check-review
- **Type:** fact-check-lead
- **Priority:** medium (live; polish remaining)
- **Detail:** `2026-06-13-fraud-prevention-package.md` and `2026-06-13-nahb-defender-of-housing.md` (both MISSING CONTEXT) are published and **now live** at langworthywatch.org — the Netlify credit-wall was bypassed by migrating to Cloudflare Pages. The Jasper-Troupsburg FEMA relocation correction is also live. Verified 200 on the apex.
- **Action (polish only — no longer deploy-blocked):** (1) swap each generic `source_url` for the real FB permalink + add screenshots to `static/images/fact-checks/`; (2) Wayback-archive the cited sources + populate `archived_url`; (3) optionally make social cards + post text for the two new entries if sharing.
- **Status:** open — polish only (entries live)

## Source / Data Quality Issues

<!-- Wayback archive failures, FOIL responses pending, primary sources that need re-fetching -->

### Audit 2026-06-15: ~48 source-gated findings (recommended tier) — need a primary source before fixing
- **Date logged:** 2026-06-16
- **Source:** `AUDIT_2026-06-15_fact-check.md` (RECOMMENDED section) + the 6-agent remediation pass
- **Type:** source-gap (bulk)
- **Priority:** low–medium (none are live falsehoods; each is an attribution/figure that needs a citation, a hedge already in place, or removal if no source surfaces)
- **Context:** The audit's hard + soft + self-contained recommended fixes are DONE and live (commits `cee7d7d` → `0b98291`). These items were left unchanged by the remediation agents because the fix needs a primary source neither in the entry nor in the audit. For each: find the source → apply the audit's prescribed fix + Wayback-archive; OR hedge/remove per the group-C default if none surfaces. Full per-item issue/evidence/fix is in `AUDIT_2026-06-15_fact-check.md` under each `### <slug>`.

  **A. Dead / homepage-only URLs → working link + Wayback archive:**
  - `2025-12-energy-policy-oil-gas` — Langworthy quotes on bare homepages; need full-path URLs
  - `2025-12-infrastructure-credit` — FingerLakes1 404 (dead-source); USDA RD 36% / 31.7% staffing-cut figures need a source
  - `2026-02-08-big-flats-ssa-doge` — Buffalo News "I fully support Musk's mission" quote → Wayback URL
  - `2026-02-08-steuben-rural-impact-summary` — WSKG $5M SNAP-admin / Wheeler quote / VA-OIG report URLs
  - `2026-02-08-allegany-county-grants-accord` — ACCORD/Allegany Hope URL; "highest poverty rate in NY" Census/NYS cite
  - `2026-03-08-defense-suppliers-visit` — Chautauqua County IDA SKF case study (600+ / $75M) URL + archive
  - `2026-06-06-langworthy-secure-data-act-hr8413` — `archived_url` points to the wrong doc; archive the coalition support-letter page
  - `2026-06-10-minnesota-fraud-50-state-claim` — empty `archived_url`; FB permalinks/screenshots
  - `2026-02-09-snap-rural-impact-summary` — CBO pub 61461 Wayback snapshot for `archived_url`
  - `2026-02-08-steuben-ice-cooperation` — `source_url` set to WSKG; `archived_url` still pending (Wayback `/save` timed out — retry)

  **B. Figure attributed to an org but not in the cited doc → that org's specific report/release:**
  - `2025-05-medicaid-coverage-cuts` — $185/mo MSP + "10% of enrollees"; per-hospital margins (Cuba 42%, Arnot-Ogden 42%, UPMC Chautauqua 37% / -17.4%, Westfield -59.1%) via Fiscal Policy Institute Fig 1 / Table 1
  - `2025-11-aca-subsidies-false-claim` & `2026-01-14-ptc-pivot` — Chautauqua premium figures ($104.30 / $212.26) + 6,300 enrollees → Gillibrand press release (senate.gov 404s)
  - `2026-02-25-largest-tax-cut-claim` — ITEP "over 70% to top quintile"
  - `2026-03-21-agriculture-week-family-farms` — winery counts (11,450→11,107; 343 closures)
  - `2026-05-30-drug-pricing-reform-claim` — CBO §71203 score ($4.9B→$8.8B, Oct 2025)
  - `2026-05-29-corning-manufacturing-credits-obbba` — Hemlock $325M CHIPS Act funding (Jan 2025), NIST/Commerce
  - `2026-05-20-scaffold-law-infrastructure-expansion-act` — insurance differential study (8–10% vs 2–4%)
  - `2026-04-16-actblue-subpoena-compliance` — ActBlue ~$4B figure; subpoena timeline dates
  - `2026-06-02-district-office-consolidation` — Public Citizen "45 NY hospitals at risk" / St. James report
  - `2026-02-20-scotus-tariff-ruling` — NY Fed pass-through (94% / 0.6%); BEA deficit ($1.24T / $901.5B / 78%)
  - `2026-02-state-preemption-pattern` — Meta $3.1M via CA Chamber; Harvard Chan PDF 404 → archive
  - `2025-11-rural-hospitals-medicaid` — reattributed to Becker's-via-Observer-Today; add a direct Becker's link if available

  **C. Quote → primary statement to verify:**
  - `2025-12-worker-safety-scaffold-law` & `2026-05-20-scaffold-law-infrastructure-expansion-act` — Cilento (NYS AFL-CIO) / LaBarbera (Building & Construction Trades) statement URLs
  - `2026-02-28-epic-fury-statement` — DNI 2025 ATA "not pursuing a nuclear weapon"; Oman FM "within reach"; Schumer/Jeffries "illegal regime-change war"
  - `2026-03-07-mullin-dhs-appointment` — Blumenthal quote attribution
  - `2026-03-05-sexual-misconduct-vote` — Massie / $17M attribution; Oversight subpoena vote record
  - `2026-01-21-hernandez-pardon` — "at least 83 killed in Caribbean strikes" source (appears 3×)

  **D. Vote / record confirmation → clerk.house.gov, CBO, bill text:**
  - `2026-02-02-shutdown-defund-ice` — $75B ICE/reconciliation figure (CBO score / H.R.1 section)
  - `2026-04-17-obbba-working-families` — $1,700 refundable CTC cap (IRS / bill text)
  - `2026-04-30-bigbrother-fisa-car-surveillance` — OBBBA surveillance $ ($2.77B / $673M / $5.2B) per P.L. 119-21 / CBO
  - `2025-10-government-shutdown-aca` — Langworthy non-signing of the Dec ACA discharge petition + "failed by one vote" margin (clerk roster)
  - `2026-03-21-ida-donor-exemption-pattern` — ECIDA 30 vs 32 beneficiaries; OSC audit S9-15-70 (URL 404'd)
  - `2026-03-08-biden-immigration-10-million` — FY2021 70.7% removal/expulsion/detention CBP/DHS stat
  - `2025-12-farm-bill-victory` — mirror the farm-workforce fix (dairy = H.R. 295/294; maple = H.R. 293; drop "Market-Driven Inventory System")

- **Action:** as sources surface (often the human's own press-release/news links), apply the audit's prescribed fix + Wayback-archive. The **A** group is the fastest (mostly just relocating a working URL). Operational leftover: regenerate the nursing-home social card PNG (`social-media/create_nursing_home_donations_card.py` script already corrected to "CMS RIA ~$43B"; the PNG still needs re-running, and that card carries ~6 pre-existing em-dashes to scrub on regen).
- **Status:** open

### Wayback archive run for the two 2026-06-13 drafts
- **Date logged:** 2026-06-13
- **Source:** background archive job (`/tmp/archive_drafts_2026-06-13.log`)
- **Type:** archive-gap
- **Priority:** medium
- **Detail:** 2026-06-13 Wayback run captured **7 of 20** (302): clerk evs XML roll065 + roll190, langworthy.house.gov press release, fec.gov C00000901, govinfo bill-text + Federal Register, nahb.org award page. **13 timed out** (000, 60s limit / archive.org throttling — not permanent): congress.gov ×2 (always blocks), gao.gov ×2, oversight.house.gov, govtrack, the clerk `/Votes/` human pages ×2, and 5 nahb.org blog/press URLs.
- **Action:** at publish, re-run archiving for the 13 timeouts and populate each entry's `archived_url` + per-source Wayback links. **TIP (validated 2026-06-13):** the clerk `/Votes/2026NNN` human pages time out, but `/evs/YYYY/rollNNN.xml` archives reliably — cite the evs XML form (now done in both 2026-06-13 entries). For congress.gov (always blocked), archive the govinfo BILLSTATUS/bill-text equivalent instead.
- **Status:** open

### congress.gov blocks non-browser fetches (recurring)
- **Date logged:** 2026-06-13
- **Source:** both 2026-06-13 verification passes
- **Type:** source-quality
- **Priority:** low
- **Detail:** congress.gov (and cbo.gov) return HTTP 403 to WebFetch/curl (Akamai). Bill/vote facts must be verified via clerk.house.gov roll-call XML, govinfo BILLSTATUS/bill-text XML, the relevant committee release, or GovTrack — never an LLM search summary.
- **Action:** standing note; prefer clerk XML / govinfo for bill verification.
- **Status:** open

## Follow-Up Tasks

<!-- Scheduled work tied to a specific date or an external dependency -->

### Publish polish for the two 2026-06-13 entries (now live)
- **Date logged:** 2026-06-13 (updated 2026-06-14)
- **Source:** this session
- **Type:** fact-check-lead (publish polish)
- **Priority:** medium
- **Done:** `_index` table updated · Senate status confirmed (H.R. 7892 → Senate HELP, H.R. 8312 awaiting referral) · `draft:false` · deployed (live via Cloudflare Pages).
- **Remaining:**
  1. Secure Facebook permalinks + screenshots — fraud-package quotes 3 posts (June 11–12), NAHB quotes 1 post (June 11). Save screenshots to `static/images/fact-checks/`; replace each generic `source_url`; populate `archived_url`.
  2. Wayback-archive the cited sources (see the archive-gap item) and add per-source links.
- **Status:** open — permalinks + archiving outstanding

## Fact-Check Leads

<!-- New Langworthy statements, votes, or actions worth a standalone entry -->

### Ashford / West Valley Demonstration Project meeting (watch item)
- **Date logged:** 2026-06-13
- **Source:** Langworthy FB post (~June 12, 2026) — meeting with Ashford Town Supervisor John Pfeffer re: West Valley Demonstration Project, rural education, infrastructure
- **Type:** fact-check-lead
- **Priority:** low
- **Detail:** West Valley (Cattaraugus) is a DOE nuclear-waste cleanup site. Possible angle: do his appropriations votes match the "key role in NY-23's energy and environmental future" framing? Niche/local — park unless cleanup funding becomes a live vote.
- **Action:** monitor for a West Valley / DOE EM appropriations vote; pull his record if one lands.
- **Status:** open

### Tooling enhancement — port pas2/oth transfer logic into the shared FEC library
- **Date logged:** 2026-06-13
- **Source:** sector_donor_scan.py fix + fec_duckdb review
- **Type:** tooling
- **Priority:** low
- **Detail:** The shared `~/projects/public-ledger/scripts/lib/fec_duckdb.py` is indiv-file-only — it has no committee-transfer (pas2/oth) scanner. The corrected pas2/oth recipient+dedup logic currently lives only in LangworthyWatch's `scripts/sector_donor_scan.py`. Optional: add a `scan_committee_transfers()` helper to the shared library so the correct semantics live in the canonical place (cross-project change; public-ledger repo).
- **Action:** if/when convenient, add `scan_committee_transfers()` to fec_duckdb.py; decompress `pas222/oth22/oth24` for full historical transfer coverage.
- **Status:** open

## Closed / Resolved

<!-- Findings acted on this session — kept for audit trail -->

### H.R. 6644 cosponsorship claim (false) — caught and removed
- **Date logged:** 2026-06-13 · **Type:** verdict/source · **Status:** closed
- **Detail:** A draft asserted Langworthy cosponsored H.R. 6644 (sourced to GovTrack at MEDIUM confidence). /fact-check-review fetched the congress.gov cosponsor list — sponsor French Hill + 31 cosponsors, Langworthy not among them. Sentence removed; Claim 2 still stands on the LIHTC/Roll 190 vote.
- **Disposition:** Added failure mode #5 (membership claims from aggregators) to CLAUDE.md, `/fact-check-review`, and `/ny23-fact-check`.

### sector_donor_scan.py pas2 donor/recipient inversion — fixed + validated
- **Date logged:** 2026-06-13 · **Type:** tooling-bug · **Status:** closed
- **Detail:** The PAC-transfer query filtered `cmte_id` (donor) == Langworthy, returning $0 incoming. Fixed to filter `other_id` (recipient), scan pas2 + oth, include all 5 committees, dedupe, and guard missing files. Validated: reproduces NAHB BUILD-PAC → Langworthy. Documented the oth/leadership-PAC gap + 5-committee list in `/fec-donor-scan`.

### NAHB BUILD-PAC $16,500 — fully confirmed via FEC API
- **Date logged:** 2026-06-13 · **Type:** donor-pattern · **Status:** closed
- **Detail:** $16,500 across 5 gifts (2022–2026), incl. $5,000 to Circle the Wagons leadership PAC, confirmed against the live FEC API (Schedule B for C00000901). The previously-uncertain 2022 $2,500 gift (un-decompressed bulk files) is confirmed.

### Site migrated Netlify → Cloudflare Pages (deploy unblocked)
- **Date logged:** 2026-06-14 · **Type:** infra · **Status:** closed
- **Detail:** Netlify hit a hard account credit/quota wall (deploys 403'd; live site frozen at June 11). Migrated to **Cloudflare Pages** (project `langworthywatch`) via `wrangler` direct upload — sidesteps both the credit wall and the flagged-GitHub-account problem (no Git integration needed). `langworthywatch.org` (apex + www→apex redirect) now served by Cloudflare; everything Netlify had stuck went live at once (verified 200). Added `layouts/404.html` + `static/_headers`, switched the Stop-hook auto-deploy to wrangler, updated CLAUDE.md + deploy memory, gitignored `.wrangler/`.
- **Deploy cmd:** `rm -rf public && hugo --gc --minify && wrangler pages deploy public --project-name=langworthywatch --branch=main --commit-dirty=true`
