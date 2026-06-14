# LangworthyWatch — Findings Backlog

> Actionable findings, leads, and follow-up tasks surfaced during research
> sessions. Items here are unprocessed — once acted on, move to a fact-check
> entry under content/fact-checks/ or close with a disposition note.

**Last updated:** 2026-06-14

---

## Posted to Social / Post Queue

<!-- Running record of what's been shared to social vs. ready-but-unposted. Update as posts go out; "UNCONFIRMED" = post material exists on disk but posting not verified. -->

| Item | Card / text | Live entry? | Social status |
|---|---|---|---|
| State of the District — Q2 2026 | **card + text ready** (created 2026-06-14) | yes | posting now (digest card + post text built; Zach noted an earlier link share) |
| Jasper-Troupsburg FEMA ($60.5M, MOSTLY TRUE) | card + text ready | corrected version pending deploy | **READY** — hold until the corrected entry deploys |
| Minnesota 50-state fraud | card + text on disk | yes | UNCONFIRMED — verify whether posted |
| Marilla "voted to defund" | card + text on disk | yes | UNCONFIRMED — verify whether posted |
| Fraud-prevention package (MISSING CONTEXT) | none yet | pending deploy | needs card + text; live-blocked |
| NAHB "Defender of Housing" (MISSING CONTEXT) | none yet | pending deploy | needs card + text; live-blocked |

---

## Priority Findings

<!-- High-value leads that could become fact-check entries or unblock investigations -->

### Two reviewed fact-checks published in repo; awaiting Netlify deploy to go live
- **Date logged:** 2026-06-13 (updated 2026-06-14)
- **Source:** June 11–12 Langworthy FB posts → /ny23-fact-check → /fact-check-review
- **Type:** fact-check-lead
- **Priority:** high
- **Detail:** `2026-06-13-fraud-prevention-package.md` and `2026-06-13-nahb-defender-of-housing.md` (both MISSING CONTEXT) are published (`draft: false`), added to the _index table, dashboard regenerated (109), committed + pushed. NOT live — Netlify deploy is 403-blocked (account billing). The Jasper-Troupsburg FEMA entry was also corrected (relocation + $5M mitigation) and is in the same deploy-pending state. source_url for the new entries is the generic facebook.com/RepLangworthy (Minnesota precedent) pending permalinks.
- **Action:** (1) clear Netlify billing → re-run `cd langworthy-tracker && netlify deploy --prod --dir public --site 68d48ede-fc40-4afc-9fdb-cb9f72737f02`, then verify the three URLs live; (2) swap in FB permalinks + Wayback-archive sources; (3) make social cards + post text for the two new entries if they'll be shared.
- **Status:** open — live-blocked on Netlify

## Source / Data Quality Issues

<!-- Wayback archive failures, FOIL responses pending, primary sources that need re-fetching -->

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

### Publish steps for the two 2026-06-13 drafts (blocked on user-supplied permalinks)
- **Date logged:** 2026-06-13
- **Source:** this session
- **Type:** fact-check-lead (publish)
- **Priority:** high
- **Detail / checklist:**
  1. Secure Facebook permalinks + screenshots — fraud-package quotes 3 posts (June 11–12), NAHB quotes 1 post (June 11). Save screenshots to `static/images/fact-checks/`; replace each `source_url`; populate `archived_url`.
  2. Update `content/fact-checks/_index.md` summary table with both entries (only after flipping to published — draft pages don't build in production, so don't add them to the index while `draft: true`).
  3. Re-confirm Senate status of H.R. 7892 / H.R. 8312 (received in Senate June 11; H.R. 7892 → Senate HELP; H.R. 8312 awaiting referral as of June 13).
  4. Flip `draft: false`, commit, push (gh-HTTPS LangworthyWatch), then `netlify deploy --prod` (auto-deploy still dead per deploy memory).
- **Action:** blocked on Facebook permalinks from the user; the rest is mechanical once those land.
- **Status:** open

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
