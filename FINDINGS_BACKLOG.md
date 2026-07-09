# LangworthyWatch — Findings Backlog

> Actionable findings, leads, and follow-up tasks surfaced during research
> sessions. Items here are unprocessed — once acted on, move to a fact-check
> entry under content/fact-checks/ or close with a disposition note.

**Last updated:** 2026-07-09

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

### June-24 credit-claim entries (hospital + Jamestown) — permalinks + Wayback retries
- **Date logged:** 2026-06-24
- **Source:** publishing the hospital-radiology and Jamestown-tariffs fact-checks (commit 32cae56)
- **Type:** archive-gap / permalink-pending
- **Priority:** low
- **Detail:** Both entries are live (`draft:false`). Outstanding: (1) **FB permalinks** for the source posts — UPMC/Arnot radiology (June 18-23) and Jamestown Advanced Products (June 22), both auth-gated, need manual capture (same as the scaffold June-16 post). (2) **Wayback retries:** `jamestownadvanced.com/about` and the WGRZ tariff interview both returned 520; the FY27 disclosure page, Post-Journal, and Woodall's archived OK (302). Both entries' `archived_url` frontmatter is still empty.
- **Action:** capture the FB permalinks → add to each entry's Sources; retry the two 520 saves; fill `archived_url`.
- **Status:** open

### Scaffold-law entries — residual source gaps (2026-06-24)
- **Date logged:** 2026-06-24
- **Source:** /tier-a-confirm + /fact-check-review on the three scaffold entries
- **Type:** archive-gap / quote-verification
- **Priority:** medium
- **Detail:** Two residuals after the 2026-06-24 hardening pass: (1) the **original Cilento (NYS AFL-CIO) and LaBarbera quotes** in `2025-12-worker-safety-scaffold-law.md` still lack direct URLs — they're now flanked by a verifiable LaBarbera "beacon" quote (The Real Deal) + a Finkelstein quote (NY State of Politics) and an honest "pending confirmation" note, but the originals are unverified. (2) The **`congress.gov/bill/119th-congress/house-bill/3548` link won't archive** (Wayback returned 520); congress.gov blocks non-browser fetches (see recurring item below). Bill facts themselves are Tier-A via the govinfo BILLSTATUS XML.
- **Action:** (1) Search nysaflcio.org / Building & Construction Trades Council press releases (or news coverage) for the specific federal-bill Cilento/LaBarbera statements; add URLs or soften to the documented positions. (2) Retry the congress.gov Wayback save in a browser, or swap the citation to the govinfo BILLSTATUS URL (already archives cleanly). Everything else cited in the live entries is Wayback-archived (Washington Examiner, The Real Deal, NY State of Politics, Construction Dive, NYCOSH PDF).
- **2026-06-24 UPDATE:** A submitted Cilento/LaBarbera joint statement (nysaflcio.org press release, **11 Mar 2026**) turned out to be about the **CLCPA / clean-energy costs**, NOT the Scaffold Law — it does not contain these quotes. The scaffold-specific Cilento/LaBarbera quotes remain unverified (likely from May 2025 bill-introduction coverage — Times Union — or a 2025 AFL-CIO release). **Recommend:** if the originals can't be located, replace them in the Dec entry with the now-verified Finkelstein (NYSTLA) + LaBarbera "beacon" quotes rather than keep them hedged indefinitely.
- **2026-06-24 RESOLVED (quotes):** Submitter provided the actual source — [Dan Clark, "New York faces new pressure to scrap 140-year-old Scaffold Law," Times Union](https://www.scaffoldlaw.org/news/times-union-new-york-faces-new-pressure-to-scrap-140-year-old-scaffold-law) (reproduced on scaffoldlaw.org). ALL Cilento and LaBarbera quotes confirmed verbatim (incl. "beyond comprehension... undermine workers in his own state"). Hedge removed; the TU article is now cited in the Dec, May, and new entries, and Rep. Espaillat's City & State op-ed (Dec. 23, 2025) added as a sitting-member rebuttal.
- **Status:** resolved (quotes confirmed + cited); only the congress.gov H.R. 3548 Wayback retry (520) is left

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

### Elmira/Chemung Hazlett Building office lease — HELD (reframe-only, do not publish as a "giveaway")
- **Date logged:** 2026-07-01
- **Source:** Susan Wilkes (candidate, Chemung Co. Legislature D7) Facebook video, ~June 29–30 2026 (`https://www.facebook.com/share/v/1Bd5cyiK3K/`); reviewed for LW at a supporter's request. Transcript verified against the House lease docs.
- **Type:** fact-check-lead
- **Priority:** low (hold)
- **Detail:** Two separate lease stories, both already assessed and **not** currently publishable:
  - **(a) City Hall proposed below-market lease** — our entry `2026-06-29-elmira-city-hall-below-market-lease.md` (verdict MISSING CONTEXT) was **published then pulled** (commit `17f205b`; unpublished `b9a2614`; draft dropped `19b6628`; stale URL retired via `_redirects` 301 `4541300`). Recoverable from git history only. Reason it was pulled: the $13.50/sq ft City Hall offer was **withdrawn before signing** — a non-event, no money changed hands.
  - **(b) Wilkes' executed-lease argument** (the video) — attacks the signed Hazlett Building lease ($855/mo, 510 sq ft, ~$20/sq ft): (1) armed guards + magnetometer are an uncharged amenity so the "bona fide arms-length marketplace transaction" certification is false; (2) a 1-yr term is impossible because the 119th Congress ends Jan 2, 2027 (only ~7 mo). **Numbers all verified** against Res. 26-218 (county's own "standard commercial rate" = $855/mo).
- **Why held (not publishing):** The executed lease is **at market rate** (county's own label), so there's no below-market benefit to point at. Hazlett is the **county's own courthouse building** (5th-fl Legislature, 4th-fl courts) — the guards/magnetometer are **courthouse security** present regardless of Langworthy, and the county is the party *receiving* rent, so Wilkes' "reimburse the county for the guards" remedy is misdirected. No public lease listing exists for the space (checked LoopNet/OfficeSpace + county site) — placed by resolution, not a marketplace; that's the one durable *process* point, alongside the impossible 1-yr term. Amplifying a **candidate's** attack also risks LW's nonpartisan posture (same COI logic as the Erie/D11 pause).
- **Action:** Do NOT restore/publish. Drafted a private correction to Wilkes (credit the term defect + no-real-marketplace point; correct the arms-length/reimbursement overstatements) — send that, not a post. If ever revisited, only as a narrow neutral *transparency/process* note (no-marketplace + defective term + existing donor-geography tie in `2026-06-02-district-office-consolidation`), explicitly NOT a giveaway claim.
- **Status:** held

### Scaffold Law — June 16 2026 Facebook post (his own cost framing, on camera)
- **Date logged:** 2026-06-24
- **Source:** user-provided screenshot of Congressman Nick Langworthy FB page, posted **June 16, 2026, 3:00 PM**
- **Type:** fact-check-lead
- **Priority:** high
- **Detail:** Standalone post (not an op-ed share) with Langworthy's own verbatim framing: *"1885. That when New York's old, outdated Scaffold Law was introduced. It causes costs to skyrocket. Families pay the price through higher housing costs, pricier infrastructure, and wasted tax dollars. I'm fighting to end it, and make New York more affordable for everyone."* Over a Spectrum News 1 (Capital Region / "Lake George" weather) clip captioned **"EXPANSION ACT BACK IN 2025."** This is the cleanest primary-source instance of the cost-only framing the three scaffold entries analyze (housing + infrastructure + tax dollars, zero mention of the 140-yr worker fall-protection standard or the 2023 fatality data) — fits the **Semantic Deception** pattern.
- **Action:** **DONE 2026-06-24** — added as the Statement anchor of `2026-06-24-scaffold-law-surface-transportation-reauthorization.md` (verbatim quote + figure `static/images/fact-checks/2026-06-24-scaffold-law-june16-fb-post.png` + Assessment tie-in + Sources entry; builds clean). Permalink supplied by submitter and wired into the entry: `https://www.facebook.com/share/r/1DHMYp6SVZ/` (auth-gated, not independently fetch-verified — eyeball-confirm it opens the June 16 post).
- **Status:** resolved (pending a visual confirm that the FB link opens the right post)

### Scaffold Law — surface-transportation reauthorization watch (Sept 2026)
- **Date logged:** 2026-06-24
- **Source:** /tier-a-confirm + /fact-check-review session, 2026-06-24
- **Type:** data-refresh / story-angle
- **Priority:** high
- **Detail:** Build More NY coalition is pushing to attach H.R. 3548's Scaffold Law preemption to the surface transportation reauthorization that replaces the IIJA, which **expires Sept 30, 2026**. If it gets folded into the must-pass reauth (vs. dying as a standalone in House Judiciary), that's a material status change for all three scaffold entries.
- **Action:** ~Sept 2026, check congress.gov for H.R. 3548 movement and the surface-transportation reauth bill text for any §240/absolute-liability preemption language; update the new entry's Bill Status + verdict framing if it advances. Re-run `/news-scan` on "scaffold law reauthorization" around the IIJA deadline.
- **Status:** open

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

### SAVE Act — constituent vote question (Olean) + false "Feb 2026 re-passage" claim debunked
- **Date logged:** 2026-07-01 · **Type:** verdict/source · **Status:** closed
- **Detail:** Olean constituent asked whether Langworthy voted for the SAVE Act. **Verified via the official House Clerk roll-call XML** (`clerk.house.gov/evs/2025/roll102.xml`): H.R. 22, On Passage, **April 10, 2025, Roll Call 102, 220–208, Langworthy = Yea.** A widely-repeated web claim that the House **re-passed** SAVE on **Feb 11, 2026 (Roll Call 69, 218–213)** is **FALSE** — Roll 69/2026 is actually **S.1383, the Veterans Accessibility Advisory Committee Act** (confirmed via `clerk.house.gov/evs/2026/roll069.xml`). The SAVE Act's only 119th-Congress House passage is the April 2025 vote; June 2026 news is about it being **stalled in the Senate** (conservative push to force action; Langworthy quoted "It's a mess"). Reinforces CLAUDE.md failure mode #1 — an LLM search summary conflated two unrelated roll calls; only the Clerk XML resolved it.
- **Disposition:** Live fact-check URL corrected — canonical slug is **`/fact-checks/2026-02-10-save-act-voter-id/`** (200); the un-dated `/fact-checks/save-act-voter-id/` **404s** (no permalink override; Hugo uses the dated filename). Constituent reply drafted with the dated URL.

### American Legion Post 1280 IRS-casework post (June 19) — considered, DROPPED (do not re-draft)
- **Date logged:** 2026-06-24 · **Type:** fact-check-lead · **Status:** closed (decided against)
- **Why:** Drafted then dropped. The casework claim ($10K penalties waived for the Cassadaga post) is **single-sourced to Langworthy's own post** — no independent corroboration exists (casework isn't public record), so it can't be verified. And there is **no impropriety angle**: congressional IRS casework / penalty abatement is a routine, institutionalized function (IRS Congressional Affairs Program + Taxpayer Advocate Service handle exactly this), and 26 U.S.C. §7217 targets the *executive branch*, expressly exempting taxpayer-forwarded requests. The only fair, verified angle (relief is routine + he voted Yea on OBBBA/Roll 190 rescinding IRS funding) is too thin to carry a standalone entry and risks reading as petty. If ever revisited, do it the Big Flats way (lead with the documented IRS-funding contradiction, verdict CONTRADICTION) — but only with stronger sourcing.

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

### "475 beagles transferred to Big Dog Ranch Rescue by end of August" — verify the claim
- **Date logged:** 2026-07-02 · **Type:** claim-verification · **Status:** open · **Action date:** 2026-09-01
- **Detail:** Langworthy FB post (~mid-June 2026): "Together, we saved the Beagles... the expectation is that the remaining 475 beagles will be transferred to Big Dog Ranch Rescue by the end of August." Checkable on its own timeline. If the transfer did not happen by Sept. 1, the declared victory becomes a fact-check; if it did, note it for fairness in the beagle-priorities entry.

### Pin exact dates + permalinks for the June beagle posts (FB relative timestamps)
- **Date logged:** 2026-07-02 · **Type:** sourcing · **Status:** open
- **Detail:** July 1 sweep counted 21 beagle posts still visible on @RepLangworthy (232-post window, ~mid-April–July 1) but Facebook shows relative dates ("4w", "7w"). The 2026-05-22 priorities entry hedges the two mid-June posts (~Rollins "major win", "Together we saved the Beagles"). Hover-capture the permalinks/timestamps in a browser pass and archive them; upgrade the hedged dates.

### FB sweep gaps (July 1): Roswell/LUNGevity + UPMC Chautauqua $300K + $2.3M airports
- **Date logged:** 2026-07-02 · **Type:** story-lead · **Status:** open
- **Detail:** No corpus entries yet for: (1) June 29 Roswell Park/LUNGevity lung-screening post (commenters raising Medicaid-cut contradiction; Roswell heavily Medicaid-exposed); (2) UPMC Chautauqua $300K training investment (3 posts, "hospital where I was born" framing) vs rural-hospital Medicaid exposure; (3) $2.3M airport funding credit claim (check appropriation + his vote); (4) critical-minerals/China post (need bill number); (5) Air Methods air-ambulance post ("I'm working..." — what legislation?).

### Greece trip: RMSP-paid Crete+Athens, April 11-18 2025 (FD Schedule H) — pull gift-travel filing
- **Date logged:** 2026-07-02 · **Type:** story-lead · **Status:** open
- **Detail:** Langworthy's CY2025 FD (filing 10078337, signed 5/15/2026) Schedule H discloses a Republican Main Street Partnership-sponsored trip: Toronto -> Crete -> Athens -> Toronto, 04/11-04/18/2025, lodging + food included, 0 days at own expense, no family. No news coverage found; not in corpus. Next: pull the per-trip Gift Travel filing from the Clerk (has dollar amounts + Ethics pre-approval), archive, and assess as entry. Per pre-publish rules: the per-trip PDF is the authoritative source for costs.

### Hochul office figure: 127,000 of the Essential Plan losses in the 7 NY GOP districts
- **Date logged:** 2026-07-02 · **Type:** enhancement · **Status:** open
- **Detail:** Per City & State / Hochul's office: 127,000 of the ~450,000 losing Essential Plan coverage live in districts of the 7 NY Republicans who voted for H.R. 1 ("abandoning their own constituents"). Partisan-source figure; attribute clearly if added to 2026-07-01-essential-plan-cliff-450k. Also: final state budget contained NO Essential Plan fix (NYS Focus, 5/28). NY-23-specific number still unpublished; FPI's 26,000 WNY remains closest.

### Liberty Strategies: spouse salary continues on CY2025 FD
- **Date logged:** 2026-07-02 · **Type:** investigation-update · **Status:** open
- **Detail:** New FD 10078337 (CY2025) Schedule C again lists spouse salary from LIBERTY STRATEGIES and STATE OF NEW YORK. Extends the Liberty Strategies FDS thread through CY2025. PDF saved to langworthywatch-staging.

### Sponsored travel: THREE consecutive spring international trips (member-traveler) — pull per-trip PDFs when Clerk server recovers
- **Date logged:** 2026-07-02 · **Type:** story-lead · **Status:** open · **Priority:** high
- **Detail:** Clerk Gift Travel search (primary, queried 7/2) shows Langworthy as member-traveler on: (1) **Israel**, 4/1-4/8/2024, American Israel Education Foundation, filing 500028161; (2) **Greece**, 4/11-4/18/2025, Republican Main Street Partnership, filing 500030908 (FD 10078337 Sch H confirms: lodging+food included, 0 days at own expense); (3) **Ireland/UK**, 3/28-4/4/2026, Republican Main Street Partnership. Plus ~13 staff filings 2023-2026 (incl. Italy/GlobalWIN 5/2025 J. Catalfamo; Mexico/Center Forward 2/2026 W. Smith; Israel/AIEF 2/2026 C. Witman). **Blocker:** the Clerk's gtimages PDF server 404s on ALL per-trip PDFs today (even 2023 docs) — dollar amounts unavailable until it recovers. Retry: https://disclosures-clerk.house.gov/GiftTravelFilings/gtimages/MT/2025/500030908.pdf (+ MT/2024/500028161, and find the 2026 Ireland ID via ViewSearch). Per pre-publish failure mode #2: per-trip PDF is authoritative for traveler/costs; the three member trips above are corroborated by filer name + FD Sch H, not inferred. Entry angle when costs land: DOCUMENTED PATTERN, neutral tone (trips are legal and Ethics-preapproved; document sponsors, costs, and the tele-only-town-hall contrast carefully or not at all).

### Committee-record spin-offs (from the 2026-07-03 "Seat at the Table" entry)
- **Date logged:** 2026-07-03 · **Type:** story-lead · **Status:** ALL 4 DONE · **Priority:** high
- **Update 2026-07-03 (later):** (3) FY2026 Labor-HHS — DONE. The standalone bill (H.R. 5304) never floored; the health-amendment votes rode the CR minibus rule (H. Rept. 119-372, Nov 12 2025): Langworthy Nay on ACA APTC extensions (RV 199/202) + Planned Parenthood strike (RV 200), Yea to report (RV 205). Folded into the committee-record entry as "The Same Pattern, Nine Months Later." (4) E&C markup statement — DONE. He DID speak; used only primary-verified quotes (May 12 2025 House statement "fight relentlessly to protect rural hospitals / proud to help lead that charge"; July 2 2025 floor remarks, CREC H3043). Deliberately did NOT use the BGR third-party markup transcript's "props/fear-mongering" quotes (unverified vs. official video — see the /lesson). Both folded into 2026-07-03-committee-record-medicaid-seat-at-the-table.
- **Detail:** The committee-record fact-check (2026-07-03-committee-record-medicaid-seat-at-the-table) opened four follow-on threads, all resting on his Rules + E&C seats. (1) **Tariffs × Rules** — DONE, published as `2026-07-03-rules-committee-tariff-vote-blockade` (H.Res.211/H.Rept.119-15 RV#37 Nay+#41 Yea; H.Res.313/H.Rept.119-56 RV#54 Nay+#60 Yea; blocked H.J.Res.73 + H.J.Res.91; floor Nay Roll 65 Feb 11 2026). (2) **Energy × E&C** — DONE, folded into `2026-05-23-propane-all-of-the-above-energy` as a "Committee Record" section (E&C RC#5 Yea to advance energy subtitle; Energy Choice Act H.R.3699 reported 24-21; State Energy Accountability Act H.R.3157 reported 27-20). NOTE the "271 projects" is national/40-states, NOT NY-23 — do not re-attribute. (3) **FY2026 Labor-HHS appropriations rules** — STILL OPEN, not yet surveyed for more closed-rule health votes; check each approps special rule at rules.house.gov/legislation. (4) **Did Langworthy speak at the May 13 E&C markup** — STILL OPEN, needs the committee video/transcript (energycommerce.house.gov markup archive / YouTube); would upgrade the E&C section from "voted" to "voted and said X."

### Wayback retry: CRPT-119hrpt106-pt1 (E&C markup report)
- **Date logged:** 2026-07-03 · **Type:** sourcing · **Status:** open
- **Detail:** During the 2026-07-03 committee-record publish, 6 of 7 sources archived to Wayback; `https://www.govinfo.gov/content/pkg/CRPT-119hrpt106/pdf/CRPT-119hrpt106-pt1.pdf` kept returning 429 (rate-limited). Permanent on govinfo regardless. Retry: `curl -s -I "https://web.archive.org/save/https://www.govinfo.gov/content/pkg/CRPT-119hrpt106/pdf/CRPT-119hrpt106-pt1.pdf"`.

### Earmark distribution vs. community need — "does he fund allies or need?" analysis
- **Date logged:** 2026-07-09 · **Type:** story-lead · **Status:** open · **Priority:** medium
- **Detail:** Tested whether Langworthy's DISCRETIONARY earmarks (CPF — the only funding he controls; formula grants are agency-decided) track community need or favor home/allies. Pulled his complete official request record from house.gov (FY24/FY25/FY26 `appropriations-requests` pages — 30 unique in-district projects) + ACS 2024 county demographics. **Findings:** (1) By PROJECT COUNT, requests are broadly need-distributed — the two highest-poverty counties (Cattaraugus 19.1%, Chautauqua 17.4%) are best-served (7 each); mostly water/sewer/public-safety for distressed small municipalities. The earlier "Tioga $0 / 61% Erie" read was an artifact of incomplete inventory (Tioga radio-comms IS in FY26 requests). (2) By DOLLARS (~$28M total in-district CPF; FY24 enacted + FY25-cycle announced/House-passed), **$/capita shows ESSENTIALLY ZERO correlation with county poverty — Pearson r = +0.01.** Erie leads at $93/capita (51% of $) but poor rural Allegany is right behind at $83/capita; dollars track neither need nor pure home-favoritism — they track which localities *applied* plus his two big discretionary picks (Newstead $5M community center + Erie Sheriff $4.2M helicopters, both home county). $/capita ranking: Erie $93, Allegany $83, Schuyler $57, Cattaraugus $49, Steuben $24, Chautauqua $18, **Chemung $5.84 (lowest)**, Tioga $0. (3) **Chemung is the cleanest anomaly** — 3rd-highest poverty (16.3%), 2nd-most populous, but only 1 request (Elmira College, a private college), lowest $/capita (~$6). Eastern county farthest from his Erie base. (4) Out-of-district home-region asks every cycle: Buffalo Niagara Airport (NY-26) + Wendelville Fire (Niagara Co, FY26).
- **Sources:** `langworthy.house.gov/services/appropriations-requests/{community-project-funding-requests-fy24, appropriations-requests-fy25, appropriations-requests-fy26}` (read via browser — house.gov 403s to plain fetch); ACS 2024 5-yr via Census Reporter (B01003/B17001/B19013). FY24 enacted confirmed via press release + Consolidated Approps Act 2024: FeedMore $3M (Hamburg/Erie), Hornell Water $1.25M (Steuben).
- **FY24 enacted amounts NOW PULLED** (Consolidated Approps Act 2024, via his grant-announcements page + press releases): Friendship Water $2M (Alleg), Allegany fairgrounds $425,850 (Alleg), Hornell Water $1.25M (Steuben), Portville Water $1.2M (Catt), West Seneca Water $1,229,360 (Erie), South Dayton Water $500K (Catt), FeedMore WNY $3M (Erie). Dollar table finalized (r=+0.01 above). Note: FY25-26 cycle amounts are "announced/House-passed" per his office; final enactment status varies (Olean PD $1M is House-passed, Senate pending). FY27 request page now also exists.
- **BEFORE any Chemung draft publishes — fairness check (mandatory per the "meetings/photos" + no-motive standards):** confirm WHY Chemung is underserved. Earmarks require a local applicant/sponsor. Did Elmira / Chemung municipalities submit CPF requests that were passed over, or did they simply not apply? Absence may be a local-application gap, NOT his snub. His only Chemung CPF across 3 cycles was Elmira College (a private college); Chemung's municipal needs got smaller FORMULA grants instead (ARC Canal Connector $248,815, July 2025). Draft must document the distribution and explicitly hedge the application question, not impute favoritism.
- **COI:** the sharpest angle (home-county big-dollar tilt) is Erie-centric — hold per D11-candidate COI posture. **The Chemung-underservice angle is COI-clean** and arguably the more defensible published story. Verdict if pursued: MISSING CONTEXT, neutral tone (earmarks are legal; document the distribution, don't impute motive).
