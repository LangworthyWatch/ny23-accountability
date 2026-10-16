# Triage 2026-10-15: COLA / Working Families Tax Cuts / Celiac Safety Act

Research only. Nothing under `content/` was edited. Posts are on the official page "Congressman Nick Langworthy" (authorship confirmed from screenshots `../screenshots/05`, `07`, `09`, all of which show the verified official page header).

## Verified Wayback snapshots (playback checked 2026-10-15: HTTP 200 plus the expected string)

| Source | Snapshot | String checked |
|---|---|---|
| SSA press release, 2026-10-14 (2027 COLA) | https://web.archive.org/web/20261015144246/https://www.ssa.gov/news/en/press/releases/2026-10-14.html | "increase by $75 per month" |
| SSA press release, 2025-07-03 ("nearly 90%") | https://web.archive.org/web/20250814180230/https://www.ssa.gov/news/en/press/releases/2025-07-03.html | "nearly 90% of Social Security" |
| TPC TaxVox, "Correcting the SSA...", 2025-07-09 | https://web.archive.org/web/20250719092939/https://taxpolicycenter.org/taxvox/correcting-social-security-administration-about-big-budget-bill | "fewer than half of older adults" |
| CRS R48613 (Aug 1, 2025) | https://web.archive.org/web/20261015202837/https://www.congress.gov/crs_external_products/R/PDF/R48613/R48613.1.pdf | "was not changed by P.L. 119-21" |
| White House CEA, 88% claim | https://web.archive.org/web/20260909173858/https://www.whitehouse.gov/releases/2025/07/no-tax-on-social-security-is-a-reality-in-the-one-big-beautiful-bill/ | "88%" |
| IRS FS-2025-03 (deductions) | https://web.archive.org/web/20260907200808/https://www.irs.gov/newsroom/working-families-tax-cuts-tax-deductions-for-working-americans-and-seniors | "Maximum annual deduction is $12,500" |
| H.R. 9048 text (GPO) | https://web.archive.org/web/20261015202519/https://www.govinfo.gov/content/pkg/BILLS-119hr9048ih/html/BILLS-119hr9048ih.htm | "Celiac Safety Act of 2026" |
| Cong. Record 2026-10-13, House "Additional Sponsors" | https://web.archive.org/web/20261015202304/https://www.congress.gov/119/crec/2026/10/13/172/160/modified/CREC-2026-10-13-pt1-PgH6041.htm | "Langworthy and Mr. Fuller" |

**Not archived:** the WGRZ article (curl 403; SPN 520 every attempt), its Yahoo syndication (SPN 429 then 520), and the congress.gov H.R. 9048 cosponsors page (SPN 429 then 520). The SSA 2027 COLA fact sheet could not be retrieved: ssa.gov returns 403, there is no Wayback capture, and archive.ph shows a CAPTCHA. See `spn_attempts.tsv`.

## A. COLA post (Oct 15)

- **SSA announced the 2027 COLA on Oct 14, 2026.** It is 3.6%, and "On average, Social Security retirement benefits will increase by $75 per month" (`ssa-press-release-2026-10-14.txt`). Both of his numbers match. WGRZ's "projected" wording is out of date. The article ran Oct 14 at 22:48 UTC, after the announcement. **Gap:** the fact sheet with before/after average benefit amounts was not obtained.
- **WGRZ article:** https://www.wgrz.com/article/money/erie-county-seniors-say-social-security-increase-wont-keep-pace-with-costs/71-4659d26e-4f5d-4a3f-ae00-3f78bde2d98d. The text was retained from the Yahoo syndication (`wgrz-cola-article-text.txt`, byline Chelsea Swift). Langworthy's written statement appears there verbatim and matches the graphic.
- **"eliminated taxes on Social Security":** P.L. 119-21 never amends IRC §86. A full-text search of the enrolled bill finds no "section 86" or "Social Security benefit" (`obbba-secs-...txt` header). CRS R48613 says the §86 determination "was not changed by P.L. 119-21". It also says the deduction "is not limited to Social Security beneficiaries" and is "not a tax credit". It is not available to the roughly 20.2% of beneficiaries under 65 (13.6M of 67.1M, Dec 2023, Table 4). TPC says the deduction benefits "fewer than half of older adults", and it estimates about half of recipients still pay some tax on benefits. SSA's own Jul 3, 2025 release said "nearly 90%... will no longer pay federal income taxes on their benefits". That release carries a Jul 7 correction notice, and TPC (Jul 9) called the claim untrue.
- **"$6,000 more relief":** $6,000 is the deduction amount, not the tax saved. At the 10/12/22% brackets it is worth $600/$720/$1,320 for one person, or $1,200/$1,440/$2,640 for a couple where both are 65+. It is worth $0 to anyone with no taxable income. It phases out between $75k and $175k (single) or $150k and $250k (joint) and covers tax years 2025-2028 only (`senior-deduction-tax-value.txt`).
- **Existing entries:** `2025-12-social-security-tax.md` = MISLEADING (the "88%" claim). `2026-09-09-town-hall-social-security-tax-credit.md` = MISLEADING (he called the deduction a "credit"; 82% vs 88%). New in this post: the "$6,000 more relief" framing, which puts a deduction amount next to a cash COLA figure; the flat word "eliminated"; and the "middle class" qualifier. **Error spotted in the Dec 2025 entry (not fixed here):** it says the deduction is "on their Social Security benefits" and calls it a "3-year lifespan (starting 2026)". It is a general age-65 deduction for tax years 2025-2028.
- **Proposed verdict:** COLA figures = TRUE. "Eliminated taxes on Social Security" plus "$6,000 more relief" = MISLEADING.

## B. Working Families Tax Cuts post (Oct 14)

Sources: `obbba-secs-70101-70104-70201-70202.txt`, `irs-fs-2025-03-obbba-deductions.txt`.

- **No tax on tips (§70201):** this is a deduction capped at $25,000, phasing out above $150k/$300k MAGI. It requires an occupation the IRS lists as customarily tipped, excludes specified service trades or businesses (SSTB), requires an SSN, requires joint filing if married, and ends after TY2028. Payroll tax still applies because §224 is an income-tax deduction only. MISSING CONTEXT.
- **No tax on overtime (§70202):** only the FLSA premium portion (the "half" of time-and-a-half) is deductible. Cap $12,500 ($25,000 joint), phase-out above $150k/$300k, SSN required, ends after TY2028. MISSING CONTEXT.
- **Larger CTC (§70104):** $2,000 becomes $2,200, permanent and indexed after 2025. The refundable cap stays at $1,400 (indexed). The new §24(h)(7) requires the child's SSN and at least one parent's work-eligible SSN. MOSTLY TRUE.
- **Expanded senior relief (§70103):** a $6,000 deduction for TY2025-2028. TRUE as worded.
- **Higher standard deduction (§70102):** $15,750 single / $31,500 joint for 2025, permanent. TRUE.
- **Overall:** MOSTLY TRUE / MISSING CONTEXT. Every item exists. The post omits that three of them are temporary, capped deductions.

## C. Celiac Safety Act post (Oct 13)

- **Bill:** H.R. 9048, 119th Congress, "Celiac Safety Act of 2026". Sponsor Rep. Emanuel Cleaver (D-MO-5), original cosponsor McCollum (D-MN-4). Introduced 2026-05-29 and referred to Energy and Commerce. No further action as of 2026-10-15 (`BILLSTATUS-119hr9048.xml`, `congressgov-api-hr9048.json`).
- **What it does:** amends FD&C Act §201(qq) to add "gluten-containing grain" (wheat, rye, barley, and their crossbred hybrids) to the major food allergens. It takes effect 18 months after enactment (`BILLS-119hr9048ih.txt`). It is an allergen-labeling bill. It does not address the "gluten-free" claim standard.
- **Cosponsors:** 51 (44 D, 7 R: Fitzpatrick, Van Drew, Kiggans, Weber, Rulli, Lawler, Pfluger). Last addition 2026-09-08. **Langworthy is NOT listed** in either govinfo BILLSTATUS (updated 2026-09-09) or the live congress.gov API (`congressgov-api-hr9048-cosponsors.json`, pulled 2026-10-15, count 51). The House "Additional Sponsors" lists for Oct 6, 9, and 13 contain no H.R. 9048 entry. On Oct 13 Langworthy was added to H.R. 7815 (the Red Star Service Banner Act), not H.R. 9048 (`CREC-2026-10-13-additional-sponsors.txt`). A separate check of his full cosponsored-bills list via the member API was not completed: DEMO_KEY was rate-limited, and the auto-mode classifier blocked reading the stored API key.
- **Bipartisan?** Yes, nominally: 7 of the 51 cosponsors are Republicans. Langworthy is not one of them yet.
- **WBEN clip (`../videos/L9.txt`, Whisper):** a caller describes relatives with gluten sensitivity. Langworthy ties the bill to "truth in labeling" and the MAHA agenda with Secretary Kennedy, calls Cleaver "a liberal Democrat not someone I typically work with", says it is "a no-brainer", and notes that he sits on Energy and Commerce. He does not say on air that he has cosponsored the bill. His E&C seat is his own statement and was not verified here.
- **Proposed verdict:** NOT SUPPORTED, for now. Re-check the congress.gov cosponsors list and the next House Record before publishing, because a signing on or after Oct 13 would appear in the next session's Record. If he is added later, the claim becomes TRUE (the post would have run ahead of the paperwork).
