# Fact-Check Site Audit — 2026-06-15

Multi-agent audit of 110 published entries. **233 confirmed findings** (90 entries); adversarial pass rejected 30 false positives.

- Hard criticals (proven errors: factual / contradiction / misattribution / dead-source): **73**
- Soft criticals (flagged 'unsupported' — could not verify, likely sourcing gaps): **35**
- Recommended (hedging / scope / stale): **125**

---

## HARD CRITICALS (proven, fixable bugs) — grouped by entry


### 2024-08-va-healthcare-shortfall

- **[factual-error]** Introduced H.R. 7256 — Federal Workforce Early Separation Incentives Act
  - issue: H.R. 7256 in the 118th Congress is the 'U.S.-South Africa Bilateral Relations Review Act,' sponsored by Rep. John James (R-MI-10). Langworthy is neither the sponsor nor a cosponsor. The bill number is wrong, and the attributed sponsorship is false.
  - evidence: govinfo BILLSTATUS for BILLSTATUS-118hr7256.xml: title='U.S.-South Africa Bilateral Relations Review Act', sponsor='Rep. James, John [R-MI-10]', 7 cosponsors listed — Langworthy not among them. Verified via verify_fact.py cosponsor script.
  - fix: Remove or correct the H.R. 7256 claim. Identify the correct bill number for the Federal Workforce Early Separation Incentives Act (if Langworthy introduced such a bill, it is under a different number), or remove the claim entirely if no verified bill exists.

- **[factual-error]** counties frontmatter tag includes 'yates'; intro text references 'Yates County' as if it is a district county in NY-23
  - issue: Yates County is NOT in NY-23. The county tags frontmatter incorrectly lists 'yates' alongside the actual NY-23 counties. The intro paragraph implies Yates County is in the district by saying veterans in 'Allegany County or Yates County' use Bath VA, conflating the VA's service catchment area with the congressional district.
  - evidence: verify_fact.py county yates returns: 'NOT IN NY-23 <-- trap'. NY-23 counties are Allegany, Cattaraugus, Chautauqua, Chemung, Erie (partial), Schuyler (partial), Steuben (partial), Tioga. Bath VA serves Yates County residents but Yates is not in the district.
  - fix: Remove 'yates' from the counties frontmatter tag. In body text, clarify that Yates County is served by Bath VA but is not part of NY-23 — e.g., 'Bath VA serves a seven-county catchment area that extends beyond NY-23, including Yates County (NY) and counties in Pennsylvania.'

- **[internal-contradiction]** By February 2026, signatories had grown to 501 (271 named, 184 anonymous)
  - issue: 271 named + 184 anonymous = 455, not 501. The stated breakdown does not add up to the claimed total — a 46-person internal discrepancy.
  - evidence: Arithmetic: 271 + 184 = 455. Entry states total of 501. One of the three numbers (total, named count, or anonymous count) is wrong.
  - fix: Recheck the primary source for the February 2026 signatory count. Correct either the total or the named/anonymous breakdown to be internally consistent.


### 2025-05-medicaid-coverage-cuts

- **[misattribution]** Center on Budget and Policy Priorities: Up to 15 million more uninsured by 2034
  - issue: The only CBPP source cited in the Sources section is 'Rural Health Fund Will Do Little to Offset Harm' (cbpp.org/blog/rural-health-fund-will-do-little-to-offset-harm-to-rural-providers-in-republican-megabill) — a blog post about rural provider impact, not a CBPP coverage-loss analysis. The '15 million' figure is not supported by the cited CBPP source. CBPP published separate analyses projecting ~14.7 million or ~15 million losing coverage, but those are not linked here. This is a claim sourced to the wrong CBPP document.
  - evidence: Entry Sources list: 'Center on Budget and Policy Priorities: Rural Health Fund Will Do Little to Offset Harm' links to a rural provider impact post. The table in Section C pins '15 million more uninsured by 2034' to CBPP with no direct link to a CBPP coverage analysis. The cited rural health fund post does not contain that figure (fetch returned 403, but the post topic is categorically different).
  - fix: Replace the CBPP source with the correct CBPP coverage-loss publication (e.g., cbpp.org analysis projecting 14–15 million uninsured), or remove the 15 million figure from the CBPP row if a direct CBPP source cannot be located. The rural health fund citation can stay but should not be used to support the 15 million figure.


### 2025-08-veterans-support

- **[internal-contradiction]** September 2025: Initial Funding Vote — Langworthy vote: NO (on bill that included full military/VA funding). Reason for NO vote: Bill included ACA subsidy extensions.
  - issue: Internal contradiction with three sibling entries. The shutdown ACA entry (2025-10-government-shutdown-aca.md), the rhetoric-vs-actions overview (2025-12-rhetoric-vs-actions-overview.md), and the shutdown-defund-ice entry (2026-02-02-shutdown-defund-ice.md) all record the September 2025 vote as YES — Langworthy voted FOR the GOP 'clean' spending bill that omitted ACA extensions; Senate Democrats blocked it, causing the shutdown. This entry inverts the mechanics: it says he voted NO on a bill WITH ACA extensions, framing him as the one who blocked military funding. Those are opposite votes with opposite causation narratives.
  - evidence: 2025-10-government-shutdown-aca.md: 'September 2025: Clean Spending Bill — Langworthy vote: YES … Democrats rejected it, leading to shutdown.' 2025-12-rhetoric-vs-actions-overview.md: 'September 2025: The Clean Funding Bill — Langworthy vote: YES.' 2026-02-02-shutdown-defund-ice.md table: 'September 2025 | House CR | YES | Passed House, failed Senate.' All three contradict the audit entry's 'Langworthy vote: NO.'
  - fix: Align with sibling entries: Langworthy voted YES on the House GOP 'clean' CR (no ACA extensions); the Senate Democratic caucus rejected it, triggering the shutdown. The CONTRADICTION verdict may still stand — he voted for a shutdown-triggering strategy while making pro-veteran statements — but the vote direction and causal framing must be corrected.


### 2025-09-salt-tax-relief

- **[factual-error]** Langworthy voted for a 'September 2025' tax package that 'did NOT include SALT deduction increase' and 'preserved $10,000 cap'
  - issue: No such September 2025 tax package exists. The only major tax legislation Langworthy voted on was H.R.1 (OBBBA), which passed the House on May 22, 2025 (RC145) and he concurred with the Senate amendment on July 3, 2025 (RC190). The entire 'Early September / Mid-September / Late September' timeline in the entry is fabricated or based on a bill that does not exist. Clerk roll-call search through RC280 (through Nov 2025) found no separate tax package vote.
  - evidence: clerk.house.gov RC145 (H.R.1, May 22 2025, Langworthy Yea) and RC190 (H.R.1 Senate amendment concurrence, Jul 3 2025, Langworthy Aye). Roll calls 220-285 (Sep-Nov 2025) contain no tax package vote.
  - fix: Either identify the specific roll call being referenced with its actual date and bill number, or withdraw the entry. If the intent was to cover OBBBA, correct all dates and the SALT/corporate-rate characterization.

- **[factual-error]** The tax package Langworthy voted for contained 'No meaningful SALT relief' and 'Preserved $10K cap'
  - issue: Directly contradicts established fact. OBBBA (H.R.1, P.L. 119-21, the only major tax bill Langworthy voted on) raised the SALT cap from $10,000 to $40,000. This is confirmed by the site's own fact-checks (2026-02-25-largest-tax-cut-claim.md and 2026-04-17-obbba-working-families.md), both of which state 'SALT cap raised from $10,000 to $40,000.' The entry's CONTRADICTION framing collapses entirely if OBBBA did include SALT relief.
  - evidence: Site's own 2026-02-25-largest-tax-cut-claim.md line 119: 'SALT cap raised from $10,000 to $40,000'; 2026-04-17-obbba-working-families.md confirms the same. The $40K SALT raise was a core OBBBA provision.
  - fix: The central CONTRADICTION claim is unsupported. If OBBBA raised the SALT cap to $40K (which it did), the entry's framing needs to be reconsidered entirely or replaced with a nuanced analysis of whether the $40K cap was sufficient for NY-23 constituents.

- **[factual-error]** The tax package reduced the corporate tax rate from 21% to 15%
  - issue: OBBBA did not reduce the corporate tax rate. The corporate rate remained at 21%. A 15% corporate rate was proposed during negotiations but was not enacted. This figure appears to be from a negotiating position, not the final law.
  - evidence: No enacted legislation reduced the corporate rate to 15% in 2025. The site's own 2026-02-25-largest-tax-cut-claim.md lists OBBBA provisions and does not mention a corporate rate reduction. The 21%->15% cut was discussed but dropped.
  - fix: Remove or correct this claim. The OBBBA's major business provision was permanent 100% bonus depreciation and a 23% pass-through deduction, not a corporate rate cut.


### 2025-10-government-shutdown-aca

- **[factual-error]** 151,000 NY-23 households on SNAP faced benefit disruptions
  - issue: The cited WSKG article states the 151,000 figure covers three congressional districts — NY-23, NY-24, and NY-19 — not NY-23 alone. The entry presents it as a NY-23-only figure throughout (headline section, Context section, and 'In Plain Language'). This overstates the district-specific impact by attributing a tri-district total to a single district.
  - evidence: WSKG article (https://www.wskg.org/regional-news/2025-11-14/governing-means-putting-your-country-first-rep-langworthy-on-longest-shutdown-in-us-history) states: 'SNAP serves 151,000 households across three congressional districts: NY23, NY24 and NY19.'
  - fix: Replace '151,000 NY-23 households' with '151,000 households across NY-23, NY-24, and NY-19' (or the NY-23-only subset if a district-specific figure can be sourced).

- **[internal-contradiction]** Timeline step 4 (December 2025 ACA vote) followed by step 5 (November 14, 2025 shutdown end)
  - issue: The numbered timeline lists 'Dec 2025: Langworthy votes against bipartisan ACA fix' as step 4 and 'Nov 14, 2025: Finally votes to reopen government' as step 5. December follows November, so step 5 precedes step 4 chronologically. The numbering implies step 4 occurred before step 5, reversing the actual sequence.
  - evidence: Entry lines 99-100: step 4 = 'Dec 2025' and step 5 = 'Nov 14, 2025'. November precedes December; step 5 should come before step 4 in chronological ordering.
  - fix: Reorder: step 4 = Nov 14 reopening vote; step 5 = Dec ACA discharge petition vote.


### 2025-10-rural-hospitals-pure-fiction

- **[factual-error]** Federal Medicaid spending in rural areas estimated to decline by $155 billion over 10 years under OBBBA
  - issue: Both cited sources (KFF and FactCheck.org) state the rural Medicaid spending decline is $137 billion over 10 years, not $155 billion. No source in the entry supports the $155B figure.
  - evidence: KFF article (cited): 'federal Medicaid spending in rural areas is estimated to decline by $137 billion.' FactCheck.org (cited): 'lower federal Medicaid spending in rural areas by $137 billion over 10 years.' The $155B figure does not appear in either cited source.
  - fix: Replace '$155 billion' with '$137 billion' in both the table row and the paragraph below it. The figure appears twice: in the OBBBA Impact table ('Rural Medicaid spending decline | $155 billion') and in the KFF Analysis paragraph ('Federal Medicaid spending in rural areas estimated to decline by $155 billion over 10 years under OBBBA').

- **[internal-contradiction]** RHTP offsets only 37% of the $137 billion in rural Medicaid spending cuts... Federal Medicaid spending in rural areas estimated to decline by $155 billion
  - issue: Internal contradiction: the same section uses $137B and $155B as the rural cut total in adjacent sentences. If the base is $137B, 37% offset math is approximately correct ($50B/$137B = 36.5%). If the base were $155B the offset would be ~32%, not 37%. The two figures cannot both be correct.
  - evidence: Lines 133-134 of the entry: 'RHTP offsets only 37% of the $137 billion in rural Medicaid spending cuts over a decade' and 'Federal Medicaid spending in rural areas estimated to decline by $155 billion over 10 years under OBBBA' appear in consecutive bullet points in the same KFF Analysis block.
  - fix: Standardize on $137B (the figure from the cited KFF and FactCheck.org sources) throughout. Remove the $155B figure.


### 2025-11-rural-hospitals-medicaid

- **[misattribution]** Bill reduced federal health funding to rural areas by an estimated $155 billion over 10 years (Kaiser Family Foundation analysis)
  - issue: Misattribution of figure to KFF. The KFF article cited (kff.org/medicaid/how-might-federal-medicaid-cuts-in-the-enacted-reconciliation-package-affect-rural-areas/) states the rural Medicaid decline is $137 billion, not $155 billion. The $155B figure appears in the Observer Today op-ed (Andrea Hatfield, Dec 2025), which may be citing a different scope or a different KFF piece. The entry's Congressional Record section explicitly attributes '$155 billion' to 'Kaiser Family Foundation analysis,' but the KFF URL in the sources does not support that number.
  - evidence: KFF article fetched: 'federal Medicaid spending in rural areas is estimated to decline by $137 billion.' Observer Today op-ed fetched: '$155 billion over a decade … Kaiser Family Foundation analysis.' The entry credits KFF for $155B, but KFF's own article says $137B.
  - fix: Change the $155B figure to $137B (KFF's actual stated figure for rural Medicaid cuts) and attribute the $155B figure to the Observer Today op-ed if that sourcing is preferred. Recalculate the net math: -$137B + $50B = -$87B, not -$105B. Update 'one-third' framing: $50B / $137B ≈ 36%, still roughly one-third but should note the approximation.

- **[internal-contradiction]** Net impact: -$105 billion to rural healthcare (and repeated in 'The Math' and 'In Plain Language' sections)
  - issue: Derived from the $155B cut figure, which is not supported by the KFF source as noted above. If the correct rural Medicaid cut is $137B (per KFF), the net is -$87B, not -$105B. This is an internal consistency error flowing from the sourcing error above.
  - evidence: KFF states $137B rural cut. $50B RHTP offset. $137B - $50B = $87B net loss, not $105B.
  - fix: Correct to -$87 billion once the $155B figure is resolved. The calculation appears three times (Congressional Record section, 'The Math' table, and 'In Plain Language') — all three must be updated.


### 2025-12-energy-policy-oil-gas

- **[factual-error]** Langworthy has a '3% lifetime environmental score' (stated in the title, Why This Matters section, Context section, and In Plain Language section)
  - issue: The League of Conservation Voters scorecard at the cited URL (https://www.lcv.org/congressional-scorecard/moc/nick-langworthy) shows a lifetime score of 2%, not 3%. The error appears four times in the entry including the title.
  - evidence: LCV scorecard fetched directly returns: 'Lifetime Score: 2%'. The entry's cited source URL (scorecard.lcv.org/moc/nick-langworthy, which redirects to the lcv.org page) is the same source — it does not support the 3% figure.
  - fix: Replace '3%' with '2%' in the title, Why This Matters paragraph, Context section (point 2), and In Plain Language section. Update the title slug if desired.


### 2025-12-infrastructure-credit

- **[internal-contradiction]** Newstead Community Center ($5,000,000, Erie County) listed as an earmark where 'He can legitimately take credit' with no qualification
  - issue: The companion entry (2026-02-11-fy2026-appropriations-credit.md, also updated Feb 11 2026) establishes that Newstead was a joint House-Senate earmark with Schumer and Gillibrand, and that sole credit is 'MISLEADING.' The main body was not updated to reflect this finding; it still presents Newstead as a legitimate sole-credit earmark. This contradicts the companion entry published the same day.
  - evidence: Companion entry lines 100-118: 'Verdict: ACCURATE on funding — MISLEADING on sole credit.' Town Supervisor quoted: 'working in a bi-partisan effort with Senator Schumer.' Main body line 65: 'He can legitimately take credit for these.' (referring to Newstead among others).
  - fix: Add a qualifier to the Newstead row in the 'What Langworthy CAN Legitimately Claim Credit For' table (e.g., 'Note: joint with Schumer/Gillibrand — see Feb 2026 update') or move Newstead to a separate 'Bipartisan earmarks' row. The Feb 2026 update section already points to the companion entry, but the main body table remains uncorrected.


### 2025-12-medicaid-immigration

- **[factual-error]** Dec 2024 | Blamed 'illegal immigrants' for healthcare costs | Voted for bill cutting rural hospital funding (Pattern table, line 100)
  - issue: No Dec 2024 House vote exists matching 'bill cutting rural hospital funding.' The bill that cuts Medicaid/rural hospital funding (H.R. 1, OBBBA) passed May 22, 2025 (RC145, confirmed Aye), not December 2024. All Dec 2024 roll calls checked via clerk.house.gov (RC480-RC517) show no healthcare/rural hospital cut legislation. The Dec 2024 row in the pattern table conflates a 2025 vote with a 2024 date.
  - evidence: clerk.house.gov roll calls for Dec 2024 (RC480-RC517) — no bill cutting rural hospital funding identified. RC145 (May 22 2025) confirmed as OBBBA Langworthy=Yea. RC517 (Dec 20 2024) = H.R. 10545 American Relief Act (CR), Langworthy=Yea — unrelated to rural hospital cuts.
  - fix: Remove or correct the Dec 2024 row. The OBBBA vote belongs in May 2025. If there is a specific Dec 2024 action being referenced (e.g., a campaign statement), the 'Actual Impact' column must not say 'Voted for bill' since no matching vote occurred in Dec 2024.

- **[misattribution]** Cuts $911 billion from Medicaid over 10 years (lines 81, 98, 121) — implicitly attributed to CBO via the CBO citation on line 159
  - issue: The companion entry (2025-05-medicaid-coverage-cuts.md, line 48) explicitly attributes the $911B figure to a KFF estimate, not CBO. The audited entry lists CBO as the only source in the sources section and places the $911B bullet immediately before a 'per CBO' tag that applies to the 1.3M dually eligible figure — creating a false impression that CBO produced the $911B number. CBO's own Medicaid spending-reduction figure for H.R. 1 differs by version and scope; $911B is not the standard CBO headline figure.
  - evidence: 2025-05-medicaid-coverage-cuts.md line 48: '| Federal Medicaid spending reduction | **$911 billion** (KFF estimate) |'. Audited entry line 81-82: '- Cuts **$911 billion from Medicaid** over 10 years\n- Reduces coverage for **1.3 million dually eligible** seniors and people with disabilities (per CBO)'. CBO direct fetch blocked (HTTP 403).
  - fix: Add '(KFF estimate)' attribution to the $911B bullet to match the source. Do not imply CBO produced this figure. Alternatively, use the CBO-attributed Medicaid net-outlay-reduction figure with a direct CBO citation.


### 2025-12-pharmacy-crisis-pbm-reform

- **[internal-contradiction]** Reform has been stripped from legislation three times at Trump's direction. (lines 35, 202); also 'PBM reform has been stripped from legislation three times' (In Plain Language section)
  - issue: Internal contradiction: the entry documents only TWO removals (December 2024 American Relief Act; July 2025 OBBB). The December 2025 section correctly says 'it was Trump who had it removed—twice' (line 121). No third removal bill is identified or sourced anywhere in the entry. The 'three times' count in lines 35 and 202 is unsupported by the entry's own timeline.
  - evidence: Line 121 uses 'twice'; lines 35 and 202 use 'three times'. Timeline sections are labeled 'First Removal' and 'Second Removal' only; no Third Removal section exists. The December 2025 section describes Langworthy returning to advocacy, not a third stripping event.
  - fix: Either document and source a third removal (e.g., a December 2025 spending bill), or change 'three times' to 'twice' in lines 35 and 202 to match the documented record and line 121.

- **[misattribution]** Langworthy joined a caucus focused on 'affordable healthcare' immediately after voting for a bill that: Cut $911 billion from Medicaid (reducing healthcare access) / Let ACA subsidies expire (raising premiums for 6,300+ NY-23 residents) (lines 158–161, MAHA Caucus Contradiction section)
  - issue: Misattribution / internal contradiction. The 'bill' referred to by the MAHA section is the American Relief Act (H.R. 10545, Dec 20, 2024) — a stopgap continuing resolution. That bill did not cut Medicaid by $911 billion or allow ACA subsidies to expire. Those provisions were in OBBB (H.R. 1), signed July 4, 2025 — approximately 6.5 months after the MAHA Caucus founding. The section pins OBBB consequences to the wrong bill.
  - evidence: RC 517 (Dec 20, 2024) confirms the American Relief Act is H.R. 10545 — a continuing/government-funding resolution. The $911B Medicaid figure is sourced in the corpus consistently to OBBB (see 2025-05-medicaid-coverage-cuts.md and 2026-01-24-ceo-hearing-premiums.md). OBBB was not passed until RC 190 (July 3, 2025). The MAHA Caucus was founded December 30, 2024, before OBBB existed.
  - fix: Either (a) reframe the MAHA section to note the contradiction surfaced when OBBB passed 6+ months later, or (b) change 'immediately after voting for a bill that' to reference OBBB, with a separate timeline note that MAHA was founded before OBBB. The $911B Medicaid and ACA subsidies bullet points must not be attributed to the American Relief Act.


### 2025-12-rhetoric-vs-actions-overview

- **[factual-error]** "I will never let Americans go to the back of the line behind undocumented people" — presented as a direct Langworthy quote from the Westfield event (Oct 8, 2025), sourced to Observer Today.
  - issue: The Observer Today article does not contain this quote. The actual quote in that article is: "I'll be damned if the people of Western New York and the Southern Tier are put at the back of the line to people while people who aren't legally in this country are paid for in full." The entry presents a substantially different paraphrase as a verbatim direct quote.
  - evidence: WebFetch of https://www.observertoday.com/news/top-stories/2025/10/langworthy-discusses-health-care-in-westfield-visit/ returned the actual quote; it does not match the entry's version.
  - fix: Replace with the actual quote from the Observer Today article, or bracket the paraphrase to signal it is a summary rather than a verbatim quote.


### 2025-12-social-security-tax

- **[misattribution]** The Tax Foundation and other groups estimated approximately 88% of Social Security recipients would see 'some benefit' from the deduction.
  - issue: Misattribution. Neither Tax Foundation article cited in the Sources section contains the 88% figure. The Newsweek article (also cited) attributes 88% to 'the White House.' The Towerpoint Wealth article (the primary cited source) attributes it to 'SSA.' Attributing this figure to 'Tax Foundation' is unsupported by any cited source.
  - evidence: Newsweek (cited): '...will raise the percentage of seniors who don't pay taxes on Social Security to 88 percent, according to the White House.' Towerpoint Wealth (cited): 'The SSA has cited that 88 percent of seniors will no longer pay federal income tax on their benefits.' Both Tax Foundation articles fetched return no 88% figure.
  - fix: Change attribution from 'The Tax Foundation and other groups' to 'the White House (per Newsweek) / SSA (per Towerpoint Wealth)' or simply 'Administration estimates.'

- **[factual-error]** Single seniors with income over $75,000 / Married couples with income over $150,000: 'No benefit from this provision.'
  - issue: Overstates the income cutoff. The Tax Foundation article (cited) clarifies the deduction phases out — it is not a cliff. Single filers above $75K receive a reduced (partially phased-out) deduction until $175,000; joint filers receive a reduced deduction until $250,000. Framing it as 'no benefit' for anyone above $75K/$150K is factually incorrect.
  - evidence: Tax Foundation (taxfoundation.org/blog/obbba-senior-deduction-tax-relief/, cited): 'The deduction will phase out at a 6 percent rate when modified adjusted gross income exceeds $75,000 for single filers and $150,000 for joint filers. The deduction is fully phased out at $175,000 for single filers and $250,000 for joint filers.'
  - fix: Replace 'No benefit from this provision' with 'Reduced or no benefit — the deduction phases out between $75,000–$175,000 (single) and $150,000–$250,000 (joint filers).'


### 2025-12-worker-safety-scaffold-law

- **[misattribution]** Industry argument: Scaffold Law adds 5-10% to construction insurance costs; reform could save $2 billion
  - issue: Misattribution and source conflation. The 5-10% cost figure and the $2 billion figure both come from Langworthy's own press release, not from an industry source. The press release states the law 'increases total construction costs between 5 and 10%' and that enactment 'will save at least $2 billion in federal tax dollars over the next 10 years' — a federal spending projection, not an insurance cost saving. Framing both as 'Industry argument' misattributes the claim's origin and mischaracterizes the $2 billion as an insurance cost saving rather than a federal taxpayer savings projection.
  - evidence: Langworthy press release (langworthy.house.gov): 'It is estimated that the scaffold law increases total construction costs between 5 and 10%' and 'Enactment of this law will save at least $2 billion in federal tax dollars over the next 10 years.' FingerLakes1 source corroborates: 'Langworthy's office projects that the Infrastructure Expansion Act could save taxpayers over $2 billion in federal spending over the next decade.' No independent industry source cited.
  - fix: Attribute the 5-10% and $2 billion figures to Langworthy's office/press release, not to 'Industry.' Clarify that $2 billion refers to projected federal spending savings over 10 years, not insurance cost savings.


### 2025-12-year-end-newsletter

- **[factual-error]** Reliable Federal Infrastructure Act (H.R. 4690) — 'Still in first stage of legislative process'; 'Committee action: NONE - has NOT been reported out'; 'has not cleared the committee process'
  - issue: BILLSTATUS-119hr4690.xml confirms the full Energy and Commerce Committee held a markup on December 3, 2025, and voted 27-21 to report the bill — the same day as H.R. 3699's markup. This is BEFORE the newsletter was issued (December 28) and before this entry was published (December 30). The bill was formally reported with H. Rept. 119-483, Part I on February 4, 2026. The entry's entire central factual claim — that only 2 of 3 bills passed committee, making Langworthy's newsletter inaccurate — is factually wrong. Langworthy's newsletter claim that all three bills were reported out of committee was accurate.
  - evidence: govinfo BILLSTATUS-119hr4690.xml: '2025-12-03 [Committee]: Ordered to be Reported by the Yeas and Nays: 27 - 21'; '2025-12-03 [Committee]: Committee Consideration and Mark-up Session Held'; '2025-11-19 [Committee]: Forwarded by Subcommittee to Full Committee (Amended) by the Yeas and Nays: 16 - 14'
  - fix: Retract or substantially rewrite the central claim. All three bills were reported out of committee by December 3, 2025. The verdict should be revised to reflect that Langworthy's newsletter claim was accurate for H.R. 4690 as well. Remove the ❌ 'INACCURATE' designation for H.R. 4690 and the 'Two accomplishments overstated as three' bottom line.

- **[internal-contradiction]** 'RHTCP provides $14B in tax credits over 10 years' and 'This offsets only 37% of the $911B in Medicaid cuts'
  - issue: Two compounded errors: (1) The newsletter graphic references the $50B Rural Health Transformation Program (RHTP, OBBBA §50301), not a '$14B RHTCP.' Sibling fact-checks in this corpus consistently cite $50B for the RHTP. A '$14B Rural Hospital Tax Credit Program' does not appear in sibling entries and may be a draft-era or phantom figure. (2) The 37% offset figure (from KFF) is derived as $50B RHTP ÷ $137B in rural Medicaid cuts, not $14B ÷ $911B. 14/911 = ~1.5%, not 37%. The two figures used together are internally inconsistent and do not reproduce the cited 37% ratio. The $911B figure is the total Medicaid reduction from OBBBA; the rural slice KFF analyzed is $137B. Mixing them attributes a rural-offset ratio to a total-program cut.
  - evidence: sibling entry 2026-06-02-rural-health-transformation-212m.md: 'a $50 billion, five-year fund created by Section 50301 of the One Big Beautiful Bill Act'; 'RHTP offsets only about 37%' of '$137 billion over ten years' (KFF). Entry under audit uses '$14B' and '$911B' with the same '37%' — 14/911 ≈ 1.5%, not 37%.
  - fix: Replace '$14B in tax credits' with '$50B Rural Health Transformation Program (RHTP).' Replace '$911B in Medicaid cuts' with '$137B in rural Medicaid cuts (KFF estimate)' when applying the 37% offset ratio. If the total $911B cut is cited separately for context, it must not be paired with the 37% offset figure.


### 2026-01-10-jamestown-office-closure

- **[misattribution]** The Post-Journal reported the office reopened after 'investigation concluded and protests in the area subsided.' (line 37, presented as a direct quote from the Post-Journal)
  - issue: This string is presented in quotation marks as if it is verbatim Post-Journal text, but the actual Post-Journal language is: 'once the investigation had gone for about a week, and things had cooled down around a protest that was held in the area, we reopened operations.' Two material differences: (1) 'investigation concluded' vs. 'investigation had gone for about a week' — the source does not say the investigation ended, only that time passed; (2) 'protests in the area subsided' (plural, ongoing) vs. 'a protest that was held in the area' (singular, past event). The entry also uses 'protests in the area subsided' without quotes in five other places (lines 17, 80, 96, 119, 235), consistently converting a single past protest into multiple ongoing protests.
  - evidence: WebFetch of Post-Journal reopening article returned: 'once the investigation had gone for about a week, and things had cooled down around a protest that was held in the area, we reopened operations.' Entry line 37 quotes this as: 'investigation concluded and protests in the area subsided.'
  - fix: Replace the fabricated composite quote on line 37 with the actual Post-Journal language in quotation marks: 'once the investigation had gone for about a week, and things had cooled down around a protest that was held in the area, we reopened operations.' Update the five unquoted paraphrases (lines 17, 80, 96, 119, 235) to use singular 'a protest' rather than plural 'protests' to match the source.


### 2026-01-14-ptc-pivot

- **[factual-error]** No Tax on Tips: 'Capped at $25,000; phases out above $160K (single)/$320K (married); requires employer certification'
  - issue: The income phaseout thresholds for the tips deduction are wrong. The enacted law (H.R.1 as signed July 4, 2025) sets the cutoff at $150,000 for single filers and $300,000 for married filing jointly — not $160K/$320K. The $160K/$320K figures appear to reflect an earlier House-passed version, not the final Senate-amended law. The site's own April 2026 entry (2026-04-25-said-vs-record-april-posts.md) correctly states '$150,000 ($300,000 joint)' for tips/overtime phaseouts. Additionally, the enacted law restricts eligibility to 68 specified occupations (a worker-side occupation requirement), which is distinct from 'employer certification.'
  - evidence: Wikipedia on One Big Beautiful Bill Act: 'Workers earning under $150,000 can deduct up to $25,000 annually in tips.' Site's own 2026-04-25-said-vs-record-april-posts.md line 116: 'Both deductions phase out for taxpayers with modified AGI over $150,000 ($300,000 joint).' The entry's $160K/$320K figures appear in no authoritative source for the enacted bill.
  - fix: Replace '$160K (single)/$320K (married)' with '$150K (single)/$300K (married filing jointly)' and replace 'requires employer certification' with 'restricted to 68 specified occupations' per the enacted law.


### 2026-01-24-ceo-hearing-premiums

- **[factual-error]** OBBB added $4.5 trillion to the deficit over 10 years (primarily tax cuts)
  - issue: The $4.5 trillion figure is the gross tax revenue reduction from OBBBA, not the net deficit increase. CBO scores the net deficit increase at $3.4 trillion over 10 years, because spending reductions (~$1.4T including Medicaid/SNAP) partially offset the $4.5T revenue loss. The entry presents the revenue figure as a deficit figure, which overstates it by roughly $1.1 trillion.
  - evidence: Tax Foundation, Bipartisan Policy Center, and CRFB all confirm: OBBBA reduces revenues by ~$4.5T but net deficit increase is ~$3.4T (CBO). The entry says 'added $4.5 trillion to the deficit.'
  - fix: Change to: 'OBBB reduced federal revenues by approximately $4.5 trillion over 10 years while adding roughly $3.4 trillion to the deficit (CBO), as spending cuts offset part of the tax reduction.'


### 2026-02-02-shutdown-defund-ice

- **[factual-error]** December 19, 2024: Langworthy voted NO on H.R. 10545, a continuing resolution that would have prevented a Christmas shutdown. The bill passed 366-34.
  - issue: Langworthy did NOT vote NO on H.R. 10545. Clerk of the House roll call 517 (December 20, 2024) shows he voted YEA on H.R. 10545, which passed 366-34. He also voted YEA (not NO) on the prior attempt, H.R. 10515, on December 19, 2024 (roll 516, which failed 174-235). There is no record of a NO vote by Langworthy on any December 2024 CR or shutdown-related bill. The 366-34 total is correct, but his vote direction is wrong. This factual error invalidates the entire basis for the 'FALSE' verdict on Claim 1 ('always opposed to shutdowns').
  - evidence: clerk.house.gov/evs/2024/roll517.xml: H.R. 10545, Dec 20 2024, Langworthy = Yea (passed 366-34). clerk.house.gov/evs/2024/roll516.xml: H.R. 10515, Dec 19 2024, Langworthy = Yea (failed 174-235). No Langworthy Nay vote found on any Dec 2024 CR.
  - fix: Correct Langworthy's vote to YEA on H.R. 10545 (December 20, not December 19). The 'FALSE' verdict on Claim 1 needs to be reconsidered — his own quote ('But that doesn't mean signing off on a bloated spending bill') may still show conditionality, but the vote record no longer supports it. Either find a different documented instance where he voted against a CR, or revise Claim 1's verdict and supporting evidence.


### 2026-02-04-minneapolis-renee-good

- **[internal-contradiction]** Langworthy quote: "a violent rioter weaponized her vehicle in an attempt to run over law enforcement officers"
  - issue: The quote attributed to Langworthy in this fact-check does not match the quote in the companion correspondence letter at /content/correspondence/letters/2026-02-04-minneapolis-renee-good.md, which reads: "a rioter who weaponized her vehicle against federal law enforcement officers conducting an operation to arrest an illegal alien." One of these is inaccurate. Both claim to be from the same constituent letter response (tracking code YRWKLY-7LYJ2). The fact-check quote also includes "in an attempt to run over law enforcement officers" which does not appear in the correspondence file's version.
  - evidence: Fact-check line 29 vs. correspondence letter lines 26-30. Both documents reference the same response (YRWKLY-7LYJ2). The two quoted versions of the letter differ substantially.
  - fix: Pull the actual PDF at /static/documents/2026-02-04-minneapolis-renee-good-response.pdf and reconcile both entries to the verbatim text. One of the two quote versions is wrong.


### 2026-02-08-steuben-credit-claiming-pattern

- **[factual-error]** SNAP work requirements expanded from ages 18-54 to ages 18-64
  - issue: The pre-OBBBA SNAP ABAWD work-requirement upper age was 18-49, not 18-54. Two authoritative sibling entries (content/fact-checks/2025-12-snap-cuts.md and content/fact-checks/2026-02-09-snap-rural-impact-summary.md) both state the expansion was from ages 18-49 to ages 18-64. The 'from' age is off by 5 years.
  - evidence: content/fact-checks/2025-12-snap-cuts.md line 78: 'H.R. 1 extends work requirements from ages 18-49 to ages 18-64'; content/fact-checks/2026-02-09-snap-rural-impact-summary.md line 39: 'The bill extends work requirements from ages 18-49 to ages 18-64'
  - fix: Change 'ages 18-54 to ages 18-64' to 'ages 18-49 to ages 18-64' (line 196).


### 2026-02-09-medicaid-rural-impact-summary

- **[factual-error]** $155 billion in rural Medicaid cuts (used throughout the entry, and the basis for saying RHTP replaces 37% of cuts)
  - issue: KFF's estimate for federal Medicaid spending decline in rural areas under OBBBA is $137 billion, not $155 billion. KFF states: 'federal Medicaid spending in rural areas could decrease by $137 billion over 10 years.' The 37% offset figure ($50B RHTP / $137B cuts ≈ 36.5%) is mathematically consistent only with $137B. Using $155B makes the ratio ~32%, not 37% — so the entry's two key claims ($155B and 37%) are internally inconsistent. The $155B figure likely propagated from an internal inconsistency in the sibling entry (2025-10-rural-hospitals-pure-fiction.md lines 114 and 133), which uses both $137B and $155B in the same section. FactCheck.org (cited in sources) also confirms the $137B KFF figure.
  - evidence: KFF 'How Might Federal Medicaid Cuts Affect Rural Areas?' (fetched): 'federal Medicaid spending in rural areas could decrease by $137 billion over 10 years—about $87 billion more than is appropriated for the rural health fund.' FactCheck.org (fetched): '$137 billion over 10 years' is the KFF rural figure; $50B/$137B ≈ 37%. Sibling entry 2025-10-rural-hospitals-pure-fiction.md line 133 also confirms '$137 billion' as the basis for the 37% calculation.
  - fix: Replace '$155 billion' with '$137 billion' everywhere it appears (lines 17, 52, 54, 85, 96, 99). The 37% figure is correct when paired with $137B and should be kept.


### 2026-02-09-va-rural-impact-summary

- **[factual-error]** The VA shed approximately 30,000 positions nationally between January and June 2025
  - issue: The parent entry (2024-08-va-healthcare-shortfall.md) explicitly states the VA 'scaled back to ~30,000 reductions, primarily through attrition, shedding roughly 17,000 positions between January and June 2025.' The 30,000 figure was the revised target plan, not the actual positions shed by June 2025. The summary entry presents the target as the realized number, overstating actual losses by roughly 2x for that period.
  - evidence: Parent entry line 70: 'VA ultimately scaled back to ~30,000 reductions, primarily through attrition, shedding roughly 17,000 positions between January and June 2025.' Summary entry line 35: 'The VA shed approximately 30,000 positions nationally between January and June 2025.'
  - fix: Change to: 'The VA shed roughly 17,000 positions nationally between January and June 2025, under a plan to reduce the workforce by approximately 30,000 through attrition and hiring freezes.'

- **[internal-contradiction]** The Lincoln Declaration was signed by 501 current and former VA clinicians (271 named, 184 anonymous)
  - issue: 271 + 184 = 455, not 501. The component counts do not add up to the stated total. This internal arithmetic contradiction is propagated from the parent entry and appears in both files.
  - evidence: Entry line 61: '501 current and former VA clinicians (271 named, 184 anonymous).' 271 + 184 = 455. The same inconsistency appears in the parent entry at /content/fact-checks/2024-08-va-healthcare-shortfall.md line 74.
  - fix: Reconcile the numbers: either correct 501 to 455, correct one of the component counts to match 501 (e.g., 271 named + 230 anonymous = 501), or remove the component breakdown if the exact split is uncertain.


### 2026-02-20-scotus-tariff-ruling

- **[factual-error]** Trump's tariffs cost the average household ... a projected $1,300 in 2026
  - issue: Tax Foundation projects $700 per household in 2026, not $1,300. The $700 figure covers the remaining Section 232 and Section 122 tariffs after the IEEPA tariffs were struck down. The $1,300 figure does not appear in the cited source.
  - evidence: Tax Foundation tariff research page states: 'We estimate the Section 232 tariffs will create an average tax burden of $600, and the temporary Section 122 tariffs will increase it to $700 for 2026.' No $1,300 figure found.
  - fix: Correct to '$700 per household in 2026' — and note this reflects the post-ruling landscape (IEEPA tariffs voided).


### 2026-02-25-nyseg-rate-hike-silence

- **[misattribution]** Riley introduced three utility bills, listing H.R. 1355 (Weatherization Enhancement and Readiness Act) as one of them.
  - issue: H.R. 1355 was introduced by Rep. Paul Tonko (NY-20) on 2025-02-13, not by Riley. Riley is one of 21 cosponsors. The section header reads 'Three utility bills:' with the framing that these are Riley's bills, but H.R. 1355 belongs to Tonko. Riley sponsored only H.R. 5487 and H.R. 6590.
  - evidence: govinfo BILLSTATUS-119hr1355.xml: sponsor = Rep. Tonko, Paul [D-NY-20]; cosponsors include Rep. Riley, Josh [D-NY-19]. BILLSTATUS-119hr5487.xml and BILLSTATUS-119hr6590.xml both confirm Riley as sponsor.
  - fix: Remove H.R. 1355 from the list of Riley's introduced bills, or reframe the row to read 'Cosponsor: Weatherization Enhancement and Readiness Act (H.R. 1355)' introduced by Tonko. Adjust the '3 bills introduced' claim to '2 bills introduced, 1 cosponsored' or keep as 3 but describe the distinction accurately.


### 2026-02-25-sotu-2026-claims

- **[factual-error]** 84% of fentanyl seizures occur at legal ports of entry, not between ports
  - issue: The Cato Institute article cited as the source for this figure (the Cato blog post on US citizens at ports of entry, FY2019-2024) reports 88% of all fentanyl seized at ports of entry (FY2015-2024), not 84%. The entry uses 84% three times (lines 165, 195, 227) and in the Questions section, all attributed to the same Cato source. The 84% figure may come from a different source or time window, but it does not match the cited Cato document.
  - evidence: Cato article fetched: 'US citizens comprised 80 percent... 88 percent of all fentanyl was seized at ports of entry from fiscal year 2015 to 2024.' Entry repeatedly states '84%' and cites the Cato article as the source. The Cato link title itself reads '80% of Fentanyl Crossers at Ports of Entry' — inconsistent with the 84% figure in the body.
  - fix: Correct '84%' to '88%' (the figure Cato reports for FY2015-2024) throughout, or source the 84% figure to the American Immigration Council fact sheet or CBP data and attribute it accurately.

- **[factual-error]** CDC reported a 30.6% decline in fentanyl deaths from 2023 to 2024
  - issue: CDC Data Brief No. 549 (cited as the source) reports a 35.6% decline in overdose deaths involving synthetic opioids (including fentanyl) from 2023 to 2024 (from 22.2 to 14.3 per 100,000). The entry states 30.6%, which does not match the cited CDC document.
  - evidence: CDC DB 549 fetched: '35.6% decline in overdose deaths involving synthetic opioids other than methadone from 2023 to 2024, dropping from 22.2 to 14.3 deaths per 100,000.' Entry states '30.6% decline in fentanyl deaths from 2023 to 2024.'
  - fix: Correct '30.6%' to '35.6%' and verify the exact metric (synthetic opioids vs. fentanyl-specific). The underlying point — that the decline began before Trump took office — remains valid regardless of the exact figure.


### 2026-02-telephone-town-hall

- **[factual-error]** On December 19, 2024, Rep. Langworthy voted NO on H.R. 10545, the continuing resolution that would have prevented the government shutdown. The CR failed 174-235.
  - issue: Triple error. (1) The 174-235 failed vote on December 19, 2024 was on H.R. 10515 (Roll 516), not H.R. 10545. The entry's source_url points to H.R. 10545, a different bill that passed 366-34 on December 20. (2) Langworthy voted YEA — not NO — on H.R. 10515 (Roll 516, Dec 19). (3) Langworthy also voted Yea on H.R. 10545 (Roll 517, Dec 20). He did not vote NO on either bill. The entire factual basis for the FALSE verdict on Claim 1 is wrong: Langworthy voted in favor of both the failed and the passed CR, not against either.
  - evidence: clerk.house.gov Roll 516: H.R. 10515, Dec 19 2024, Failed 174-235, Langworthy = Yea. Roll 517: H.R. 10545, Dec 20 2024, Passed 366-34, Langworthy = Yea. Verified via verify_fact.py rollcall 2024 516 langworthy and rollcall 2024 517 langworthy.
  - fix: Claim 1 needs a complete rewrite. The correct record is that Langworthy voted YEA on the Dec 19 CR (H.R. 10515, failed 174-235) and YEA on the Dec 20 CR (H.R. 10545, passed 366-34). If the entry intends to document that a shutdown still occurred after the initial CR failed, the framing must change entirely. The FALSE verdict cannot stand as written — Langworthy voted for the CR, not against it.


### 2026-03-05-sexual-misconduct-vote

- **[factual-error]** Republicans 319 Yes (Buried Resolution) / 38 No; Democrats 38 Yes / 27 No (Roll Call 83 table)
  - issue: The Republican Yes count of 319 is wrong; actual is 175. The Democratic Yes count of 38 is wrong; actual is 182. The entry's table appears to have assigned nearly all Yes votes to Republicans, as 319 + 38 = 357 total Yes votes, suggesting the author erroneously collapsed all Yea votes into the R column. Confirmed against clerk.house.gov/evs/2026/roll083.xml: R Yea=175, R Nay=38; D Yea=182, D Nay=27. Roll Call's reporting also states '182 Democrats joining 175 Republicans' voted for the motion to refer.
  - evidence: clerk.house.gov/evs/2026/roll083.xml: totals-by-party Republican yea-total=175 nay-total=38; Democratic yea-total=182 nay-total=27; Grand total Yea=357 Nay=65.
  - fix: Correct the table: Republicans 175 Yes / 38 No; Democrats 182 Yes / 27 No. Also update the inline text 'Langworthy was among the 38 Republicans who voted against their party leadership's position' — that count (38 R Nay) is correct and can stay.


### 2026-03-08-biden-immigration-10-million

- **[internal-contradiction]** Outcomes table: 'Removed, expelled, or detained at initial processing — ~2.8 million' alongside 'Title 42 expulsions alone (entire Biden term) — ~3 million'
  - issue: Internal contradiction: Title 42 expulsions are a subset of removals/expulsions/detentions, but the entry assigns Title 42 alone (~3M) a figure larger than the entire 'removed/expelled/detained' row (~2.8M). A subset cannot exceed the parent category. The FactCheck.org source (through Oct 2023) reports 3.7M total repatriations — already higher than the entry's 2.8M removed/expelled/detained row even before the Biden term ended. These three table rows appear to use inconsistent scopes or snapshots, and they do not sum to the 10.8M encounter total in any coherent way.
  - evidence: FactCheck.org (Feb 2024, through Oct 2023): '3.7 million' total DHS repatriations vs. entry's ~2.8M 'removed/expelled/detained' row; Title 42 expulsions (~3M) cannot be a subset of ~2.8M.
  - fix: Reconstruct the outcomes table from a single consistent source and snapshot. Title 42 expulsions should either be folded into the 'removed/expelled' row (not listed separately) or the parent row corrected upward. The MPI Title 42 postmortem or DHS OHSS published final-term totals would be appropriate sources.


### 2026-03-09-dhs-security-incidents

- **[internal-contradiction]** The shooting ... killed three people and injured 15 others.
  - issue: The entry body says '15 others' injured, but the cited KUT Radio source (title and body both) reports 14 hospitalized. The KUT article title is literally 'Three dead, 14 hospitalized in potential act of terrorism in downtown Austin.' The entry's own sources list reproduces that title correctly (line 138), creating an internal inconsistency: body says 15, cited source says 14.
  - evidence: KUT Radio source title at line 138: '3 dead, 14 hospitalized'. Entry body at line 35: 'injured 15 others'. KUT article content fetched confirms 14 hospitalized.
  - fix: Change '15 others' to '14 others' (or 'at least 14') to match the cited KUT source.


### 2026-03-10-great-lakes-award

- **[factual-error]** LCV lifetime score: 6%
  - issue: The LCV scorecard (lcv.org/congressional-scorecard/moc/nick-langworthy/456892) shows Langworthy's lifetime score as 2%, not 6%. The 6% figure is his 2023 annual score only. The entry conflates a single-year score with the lifetime score in two places: the bullet point and the summary section.
  - evidence: WebFetch of https://www.lcv.org/congressional-scorecard/moc/nick-langworthy/456892 returned: Lifetime Score 2%; 2023 annual score 6%; 2024 annual score 0%; 2025 annual score 0%.
  - fix: Change both instances of '6% lifetime' to '2% lifetime' and note that the 2023 annual score was 6%.


### 2026-03-14-nys-utility-rates-data-investigation

- **[internal-contradiction]** New York's electricity rates are 49.7% above the national average. NY pays 26.49 cents/kWh vs. the U.S. average of 16.83 cents/kWh — a gap of 49.7%.
  - issue: Internal contradiction: (26.49 - 16.83) / 16.83 = 57.4%, not 49.7%. The 49.7% figure is arithmetically inconsistent with the specific rate figures cited in the same sentence. The 49.7% figure likely originates from a different time-period snapshot than the 26.49/16.83 pair — a derived-number failure from combining two different snapshots. EIA March 2025 data (NY=25.45, US=17.09) yields a 48.9% gap, which is closer to the stated 49.7% but does not match the cited rates.
  - evidence: Python: (26.49 - 16.83) / 16.83 = 57.4%. EIA Electric Power Monthly March 2026 data: NY March 2025 = 25.45 c/kWh, US = 17.09 c/kWh (48.9% gap — consistent with ~49.7% but inconsistent with the 26.49/16.83 pair). The intro paragraph and Section 2 cite the same 49.7% figure but against incompatible rate values.
  - fix: Reconcile the rate figures and the percentage from the same EIA time period. If the 49.7% gap figure is drawn from 2024 annual averages, cite those rates (not 26.49/16.83). If 26.49/16.83 is used, the gap must be stated as ~57%.

- **[internal-contradiction]** NY households pay $658/year more than the national average at typical usage (7,200 kWh/year).
  - issue: Using the cited rates of 26.49 and 16.83 c/kWh, the correct annual cost difference is (26.49 - 16.83) × 7200 / 100 = $695.52, not $658. The $658 figure is consistent with a US rate of ~17.35 c/kWh rather than 16.83 — again suggesting the dollar figure and the cited rates come from different data points.
  - evidence: Python: (26.49 - 16.83) × 7200 / 100 = $695.52. To produce $658, the US rate would need to be ~17.35 c/kWh. The entry cites 16.83 c/kWh as the US average in the same section.
  - fix: Recalculate using a single consistent rate pair. Either update $658 to $696 (using the cited 26.49/16.83), or source the $658 and 49.7% figures from their actual EIA snapshot and cite those rates instead.


### 2026-03-14-seneca-nation-law-enforcement-act

- **[factual-error]** Sen. Jerry Moran (R-KS) received $8,500 from Seneca Nation of Indians in 2025
  - issue: FEC API (schedule A, contributor_name=seneca+nation+of+indians) shows three contributions to Moran committees on July 15, 2025: $5,000 to Moran Victory Committee (C00616268) + $3,500 to Moran for Kansas (C00458315) + $1,500 to Moran for Kansas = $10,000 total. The entry states $8,500, which does not match any single combination of these records.
  - evidence: FEC API: api.open.fec.gov/v1/schedules/schedule_a/?contributor_name=seneca+nation+of+indians — Moran Victory Committee 2025-07-15 $5,000; Moran for Kansas 2025-07-15 $1,500 and $3,500. Total = $10,000 not $8,500.
  - fix: Change the Moran row to show $10,000 (or break it into two rows: $5,000 to Moran Victory Committee and $5,000 to Moran for Kansas [$1,500 + $3,500]), with date July 15, 2025.


### 2026-03-21-ida-donor-exemption-pattern

- **[factual-error]** Erie County Republican Chair (2010–2018)
  - issue: End year is wrong. Wikipedia (ballotpedia.org/Nick_Langworthy corroborated by Wikipedia) shows Langworthy served as Erie County Republican Chair from May 2010 through September 2019, not 2018. The entry understates the tenure by roughly one year.
  - evidence: Wikipedia: 'In office May 2010 – September 2019' as Erie County Republican Chair.
  - fix: Change '(2010–2018)' to '(2010–2019)'.

- **[factual-error]** NYS Republican State Chair (2019–2022)
  - issue: End year is wrong. Langworthy served as NYS Republican State Chair from July 1, 2019 through March 23, 2023, not 2022. The entry understates the tenure by roughly one year.
  - evidence: Wikipedia: 'July 1, 2019 – March 23, 2023' as NYS Republican State Chair.
  - fix: Change '(2019–2022)' to '(2019–2023)'.


### 2026-03-21-obbba-ida-vote

- **[dead-source]** source_url: https://www.govtrack.us/congress/votes/119-2025/h175
  - issue: The cited GovTrack URL points to Roll Call 175 (H.Res. 537, June 24 2025 — a Motion to Table), not to the H.R. 1 passage vote. Roll Call 145 (May 22 2025) is the correct vote. The GovTrack URL for that vote would be govtrack.us/congress/votes/119-2025/h145. The archived_url in frontmatter also captures the wrong roll number. The vote facts themselves (date, tally, Langworthy YES) are all correct per clerk.house.gov roll145.xml; only the hyperlinked source is wrong.
  - evidence: clerk.house.gov/evs/2025/roll145.xml: H R 1, 22-May-2025, Passed 215-214, Langworthy = Yea. clerk.house.gov/evs/2025/roll175.xml: H RES 537, 24-Jun-2025, On Motion to Table.
  - fix: Change source_url to https://www.govtrack.us/congress/votes/119-2025/h145 and update archived_url accordingly.


### 2026-03-21-pay-tsa-act

- **[factual-error]** December 19, 2024: Langworthy voted NO on H.R. 10545, a continuing resolution that would have prevented a government shutdown. The bill passed 366–34 and the government stayed open despite his no vote.
  - issue: Langworthy voted YEA on H.R. 10545, not NO. clerk.house.gov Roll Call 517 (December 20, 2024) shows his vote as Yea. The 34 Nays were all far-right Republicans (Banks, Biggs, Boebert, Burchett, etc.) — Langworthy was not among them. Additionally, the vote occurred on December 20, not December 19 (December 19 was Roll Call 516 for the failed H.R. 10515, on which Langworthy also voted Yea). This error appears at lines 61, 79, 125, 134, 146, and 180, and in the Sources section ('Congress.gov: H.R. 10545 vote record (December 19, 2024) — Langworthy: NO'). The same error propagates from the sibling entry 2026-02-02-shutdown-defund-ice.md, where this 'no vote' was first documented and rated FALSE.
  - evidence: clerk.house.gov Roll Call 517 (2024): H.R. 10545 'American Relief Act, 2025', December 20, 2024, Passed 366-34. Langworthy (R-NY) = Yea. Roll Call 516 (2024): H.R. 10515, December 19, 2024, Failed 174-235. Langworthy (R-NY) = Yea. There is no roll call where Langworthy voted Nay on either December 2024 CR.
  - fix: Correct every reference to a Langworthy 'no vote' on H.R. 10545 to reflect that he voted YEA. Update the date from December 19 to December 20. Reassess the CONTRADICTION verdict and the quoted rationale ('a bloated spending bill'), which was likely made in the context of the Dec 19 failed vote (H.R. 10515 with DOGE provisions) but is paired here with a vote he actually supported. The sibling entry 2026-02-02-shutdown-defund-ice.md also needs the same correction.


### 2026-03-28-shutdown-immigration-scapegoating

- **[factual-error]** Alex Pretti was killed 'in February' (line 53: 'Renee Good (killed January 7, 2026) and Alex Pretti (February)')
  - issue: Alex Pretti was killed on January 24, 2026 — not in February. Wikipedia's article on the 2026 shutdowns explicitly states the first 2026 partial shutdown was triggered 'following the killing of Alex Pretti by Customs and Border Protection (CBP) agents on January 24, 2026.'
  - evidence: Wikipedia: '2026 United States Federal Government Shutdowns' — 'the killing of Alex Pretti by Customs and Border Protection (CBP) agents on January 24, 2026'
  - fix: Change 'Alex Pretti (February)' to 'Alex Pretti (January 24, 2026)'.

- **[internal-contradiction]** Body text (line 53) says the first DHS-specific shutdown started on 'January 30' ('The two DHS-specific shutdowns (January 30 and February 14 onward)')
  - issue: Internal inconsistency: the shutdown table two paragraphs later correctly lists January 31 as the start date, which matches Wikipedia ('shutdown procedures at midnight on Saturday, January 31'). The 'January 30' in the body text is wrong.
  - evidence: Entry table (line 77): 'January 31 – February 3, 2026 | ~4 days'. Wikipedia: 'the Office of Management and Budget said they would begin shutdown procedures at midnight on Saturday, January 31.'
  - fix: Change 'January 30' in line 53 to 'January 31' to match the table and the Wikipedia source.


### 2026-04-10-immigration-crime-victims-list

- **[factual-error]** Victor Antonio Martinez-Hernandez was convicted of Rachel Morin's rape and murder 'on April 14, 2026 — four days after this post.'
  - issue: The entry's own cited CBS Baltimore source states the conviction was on 'Monday, April 14, 2025' — a year before the April 10, 2026 post date, not four days after. The entry has the wrong year for the conviction date. April 14, 2025 was indeed a Monday; April 14, 2026 is a Tuesday, which further confirms 2025 is correct.
  - evidence: CBS Baltimore source (cbsnews.com/baltimore/news/maryland-rachel-morin-murder-trial-victor-martinez-hernandez/) returned: 'Conviction Date: Monday, April 14, 2025.' April 14, 2026 is a Tuesday, not a Monday.
  - fix: Change 'on April 14, 2026 — four days after this post' to 'on April 14, 2025 — nearly a year before this post.' The 'CONFIRMED' label is still accurate; only the date and the 'four days after' framing are wrong.

- **[internal-contradiction]** Context section states: 'Five cases involve convictions for murder by an undocumented person. One (Nungaray) involves pending charges. One (Hamilton) involves someone who entered through formal CBP processing. One (Bos) involves no murder charge.' (5+1+1+1 = 8)
  - issue: Internal arithmetic error: 5+1+1+1 = 8 but the post names only 7 people. Hamilton cannot simultaneously be in the 'five convictions' bucket and a separate 'CBP processing' bucket without double-counting. If Hamilton is excluded from convictions, the convictions are Riley, Morin, Tibbetts = 3 (plus Gorman, who is charged not convicted). If Hamilton is included in convictions, the total is still only 7 with no room for a separate Hamilton category. The 'five' figure is overstated regardless of how Hamilton is categorized.
  - evidence: Seven names listed: Gorman (charged), Riley (convicted), Morin (convicted), Nungaray (pending), Tibbetts (convicted), Hamilton (convicted, CBP entry), Bos (no murder charge). Maximum defensible conviction count is 4 (Riley, Morin, Tibbetts, Hamilton) or 3 if Hamilton is placed in its own category. 'Five' is not supportable from the seven names.
  - fix: Correct the Context breakdown to: 'Three cases involve convictions for murder (Riley, Morin, Tibbetts). One (Gorman) involves a pending murder charge. One (Nungaray) involves pending capital murder charges. One (Hamilton) involves a conviction for someone who entered via formal CBP processing as a minor. One (Bos) involves no murder charge and an officially undetermined cause of death.' — total = 7.


### 2026-04-30-feedmore-earmark-vs-cuts

- **[misattribution]** "Proud to deliver for WNY families" — attributed to Langworthy in the side-by-side comparison table under March 2024
  - issue: This phrase does not appear in the cited Post-Journal source. The actual Langworthy quote in that article is: "I'm proud to secure $3 million for Feedmore WNY's new building in Hamburg to give them the space they need to continue their important work and provide more food to those who need it." The table presents the fabricated paraphrase in quotation marks as if it is a direct quote, which it is not.
  - evidence: Post-Journal source (https://www.post-journal.com/news/community/2024/03/langworthy-secures-3-million-for-feedmore-wny/) fetched and confirmed — the phrase 'Proud to deliver for WNY families' does not appear. The table entry uses quotation marks, implying a verbatim quote.
  - fix: Replace the fabricated quote in the table with the actual Langworthy quote from the source, or rephrase as a paraphrase without quotation marks (e.g., Praised his role in securing funding for WNY families).


### 2026-05-04-sugar-industry-trips-howard-center

- **[misattribution]** The piece quotes Harrison Weber, Executive Director of the Red River Valley Sugarbeet Growers Association, on the program's purpose: [block quote] "to build a new bench of loyal allies on Capitol Hill"
  - issue: The phrase 'to build a new bench of loyal allies on Capitol Hill' is NOT a direct quote from Weber. Per the Howard Center article, it appears in the article's own narrative prose: 'For the sugar industry, the trips are a chance to build a new bench of loyal allies on Capitol Hill for key policy battles every five years.' Weber's only actual direct quote in the piece is: 'The trip[s] are designed for solely educational purposes.' The entry formats this as a block-quote attributed to Weber and calls it 'the core of this fact-check,' which is a fundamental misattribution — the entry is presenting the journalist's characterization as the industry executive's own admission.
  - evidence: WebFetch of https://cnsmaryland.org/2024/11/01/sugar-industry-pays-for-house-trips-to-help-safeguard-subsidies/ confirms: 'bench/loyal/allies' phrase appears in article narrative prose, not in quotation marks; Weber's only direct quote is the 'educational purposes' statement.
  - fix: Replace the block-quote with an attribution to the Howard Center article's framing, e.g.: 'The Howard Center described the program's purpose as providing "a chance to build a new bench of loyal allies on Capitol Hill."' Remove the attribution to Weber. Weber's actual quote ('designed for solely educational purposes') should be noted separately as his on-record characterization.


### 2026-05-18-aapd-medicaid-disability-contradiction

- **[factual-error]** Forty disability organizations sent opposition letters before Langworthy's May 18 meeting.
  - issue: ProPublica says 'some 40 Down syndrome organizations' sent a letter to SSA Commissioner Bisignano. The entry broadens this to 'forty disability organizations,' which overstates the scope — these were specifically Down syndrome advocacy groups, not a broader coalition of disability organizations.
  - evidence: ProPublica article (fetched): 'Some 40 Down syndrome organizations recently sent a letter to Bisignano expressing their opposition to the planned change.' The entry says 'Forty disability organizations sent opposition letters.'
  - fix: Change 'Forty disability organizations' to 'Some 40 Down syndrome organizations' to match the cited ProPublica source.


### 2026-05-20-federal-grants-credit-claiming-may2026

- **[factual-error]** Pattern table row for Feedmore entry lists the earmark amount as '$250K'
  - issue: The Feedmore entry (2026-04-30-feedmore-earmark-vs-cuts.md) clearly states the earmark was '$3 million' — confirmed by the Post-Journal source headline 'Langworthy Secures $3 Million For FeedMore WNY.' The audited entry understates the amount by a factor of 12.
  - evidence: 2026-04-30-feedmore-earmark-vs-cuts.md line: 'Langworthy secured a $3 million federal earmark for FeedMore WNY in the FY2024 appropriations bill.' Also: entry title '$3M Earmark Press Conference.'
  - fix: Change '$250K' to '$3M' in the pattern table row for the Feedmore entry.

- **[misattribution]** Pattern table describes the Feedmore entry as 'Claimed credit while cutting SNAP by $295B'
  - issue: The Feedmore entry (2026-04-30-feedmore-earmark-vs-cuts.md) uses '$186.7 billion' for the SNAP cut figure, not $295B. The $295B figure appears in the separate SNAP-focused entries (2025-12-snap-cuts.md, 2026-02-09-snap-rural-impact-summary.md) and likely reflects a different CBO scoring window or scope. Attributing $295B to the Feedmore entry is a misattribution that contradicts the linked source.
  - evidence: 2026-04-30-feedmore-earmark-vs-cuts.md: 'the largest cut to the Supplemental Nutrition Assistance Program (SNAP) in U.S. history — $186.7 billion over 10 years per Congressional Budget Office scoring.' The $295B figure does not appear in that entry.
  - fix: Change '$295B' to '$186.7B' in the pattern table row for the Feedmore entry, to match what that entry actually says. If $295B is the correct CBO figure for a different time window, cite it to the SNAP entry, not the Feedmore entry.


### 2026-05-23-propane-all-of-the-above-energy

- **[factual-error]** Langworthy voted against the IRA. Every Republican in the House voted against it; every Democrat voted for it (House vote: 220–207, August 12, 2022).
  - issue: Langworthy was not a Member of Congress on August 12, 2022, when the IRA passed. He won the Republican primary on August 24, 2022 (after the IRA vote) and was sworn in January 3, 2023. The NY-23 seat was vacant at the time of the IRA vote — Tom Reed had resigned in May 2022. Langworthy cast no vote on the IRA. The 220-207 tally is accurate for the vote itself, but attributing a 'Nay' to Langworthy is factually false.
  - evidence: clerk.house.gov/evs/2022/roll420.xml confirms IRA date = 12-Aug-2022; Langworthy does not appear in the roll call. Wikipedia confirms Langworthy assumed office January 3, 2023. Republican primary was August 24, 2022 — after the vote.
  - fix: Remove 'Langworthy voted against the IRA.' He was not in Congress when it passed. The entry can note that he has opposed the IRA's clean energy provisions rhetorically and voted to repeal them via the OBBBA, but cannot state he voted against the IRA itself. Consider noting that his predecessor's seat was vacant for this vote.

- **[factual-error]** House Roll Call 461 (August 12, 2022): Inflation Reduction Act — Langworthy voted Nay (cited as source 2)
  - issue: Roll Call 461 is the wrong bill. RC 461 (September 29, 2022) is the SBIR and STTR Extension Act (S 4900), not the IRA. The IRA was Roll Call 420 (August 12, 2022). The cited clerk.house.gov URL is incorrect and links to a wholly different piece of legislation.
  - evidence: clerk.house.gov/evs/2022/roll461.xml: measure = S 4900, description = SBIR and STTR Extension Act, date = 29-Sep-2022. The IRA is clerk.house.gov/evs/2022/roll420.xml: measure = H R 5376, date = 12-Aug-2022.
  - fix: Correct the roll call citation to RC 420. But more importantly, the underlying 'voted against' claim must be removed — Langworthy was not in Congress for either roll call.


### 2026-05-29-corning-manufacturing-credits-obbba

- **[factual-error]** Hemlock Semiconductor — approximately 50% co-owned by Corning, with Shin-Etsu Handotai as the other major partner — produces semiconductor-grade polysilicon in Clarksburg, Tennessee.
  - issue: Hemlock Semiconductor's active polysilicon production is in Hemlock, Michigan — not Clarksburg, Tennessee. The Tennessee plant (near Clarksville, not Clarksburg) briefly opened in 2012 but was permanently closed in December 2014 due to industry oversupply. Additionally, Corning's ownership stake is approximately 80.5%, not ~50%; Shin-Etsu Chemical owns ~19.5%. The entry misstates both the operating location and the ownership percentage.
  - evidence: Wikipedia (Hemlock Semiconductor article) cites the company's own 2020 Corning disclosure: Corning owns 80.5%, Shin-Etsu Chemical owns 19.5%. Headquarters listed as Hemlock, Michigan. Tennessee plant permanently closed December 2014. HSC website (hscpoly.com) shows contact address: 12334 Geddes Road, Hemlock, Michigan 48626.
  - fix: Change 'Clarksburg, Tennessee' to 'Hemlock, Michigan'. Change 'approximately 50% co-owned by Corning' to 'approximately 80% owned by Corning (80.5% per a 2020 Corning disclosure)'. Remove reference to Shin-Etsu Handotai as 'other major partner' — it is a minority shareholder at ~19.5% (Shin-Etsu Chemical is the correct parent entity). Also remove Tennessee from the timeline and map.

- **[misattribution]** The Section 45X manufacturing credit for semiconductors, boosted by OBBBA from 25% to 35%, applies to this [Hemlock] operation.
  - issue: The 25%-to-35% credit boost is in Section 48D (the Advanced Manufacturing Investment Credit, a CHIPS Act facility-investment credit), not Section 45X (the Advanced Manufacturing Production Credit). Section 45X has no percentage-based semiconductor credit — it covers solar-grade polysilicon at $3/kg and critical minerals at 10%. The statutory change is in Section 70308 of P.L. 119-21, amending IRC §48D(a). The entry misidentifies the credit by section number throughout.
  - evidence: P.L. 119-21 §70308 reads: 'Section 48D(a) is amended by striking 25 percent and inserting 35 percent.' IRC §45X (checked via uscode.house.gov) contains no percentage-based semiconductor credit — only dollar-per-unit amounts for solar components and 10% for critical minerals. The 45X phase-out/restriction section (§70514) does not reference any 25%-to-35% change.
  - fix: Replace '45X' with '48D' in the semiconductor credit claim. Correct to: 'The Section 48D Advanced Manufacturing Investment Credit for semiconductor facilities, boosted by OBBBA from 25% to 35%...' Note that 48D applies to capital investment in semiconductor fabrication facilities, not per-unit production — which may affect how it applies to Hemlock's operations. The entry's claim that Section 45X is the relevant credit for Hemlock's polysilicon production credit should be re-examined; 45X does cover solar-grade polysilicon ($3/kg) but that is separate from semiconductor-grade polysilicon.


### 2026-05-30-drug-pricing-reform-claim

- **[factual-error]** Approximately 1.8 million Medicare beneficiaries are projected to be affected [by Round 2 / the 15 drugs effective January 1, 2027]
  - issue: The 1.8 million beneficiaries figure is the Round 3 (2028 drugs) count, not Round 2. Per KFF's 'Key Facts About Medicare Drug Price Negotiation,' 1.8 million is explicitly tied to the 15 drugs selected for 2028 (total gross Medicare spending $27B, November 2024–October 2025). KFF provides no beneficiary count for Round 2 (the 2027 drugs). The entry conflates a Round 3 enrollment figure with Round 2.
  - evidence: KFF page: 'Total gross Medicare spending on these 15 drugs between November 2024 and October 2025 was $27 billion, with 1.8 million Medicare beneficiaries using these medications during that time' — explicitly the Round 3 (2028) drug cohort. Round 2 has no stated beneficiary count on the KFF page. Checked: https://www.kff.org/medicare/key-facts-about-medicare-drug-price-negotiation/
  - fix: Remove or correct the 1.8 million beneficiary figure. Either source a Round 2-specific beneficiary count from a CMS primary source (if available), or remove the figure entirely and note that a Round 2 beneficiary count has not been publicly reported.


### 2026-06-02-chautauqua-snf-cluster

- **[internal-contradiction]** Two displacement events totaling **106+ residents and 113+ jobs**
  - issue: The '106+' resident figure is wrong. The body states Lutheran displaced 49 residents and Absolut Care displaced 66 residents — combined total 115 residents, not 106. The '106' figure matches Lutheran's staff count (106 staff affected), not a resident count. The figure has been transposed into the wrong category. Additionally '113+ jobs' captures only Absolut Care's 113 jobs and omits Lutheran's 106 staff, making the combined job-loss figure at least 219, not 113.
  - evidence: Body text: Lutheran Social Services — '49 residents displaced, 106 staff affected'; Absolut Care of Westfield — '66 residents displaced; 113 jobs lost'. 49+66=115 residents; 106+113=219 jobs. Verdict says '106+ residents and 113+ jobs'.
  - fix: Correct the verdict to read: 'Two displacement events totaling 115+ residents and 219+ staff/jobs' (or break out: 49 residents + 106 staff from Lutheran; 66 residents + 113 jobs from Absolut Care).


### 2026-06-02-district-office-consolidation

- **[factual-error]** Two-thirds of all individual-donor money to Langworthy ($843,783, or 74% of the $1.02M-county-mapped total) comes from two counties — Erie and Niagara
  - issue: The percentage is wrong and the sentence contains an internal contradiction. Erie ($685,485) + Niagara ($158,298) = $843,783 (sum verified correct). The county-mapped table totals $1,022,225. $843,783 / $1,022,225 = 82.5%, not 74%. Additionally, the same sentence calls the figure both 'two-thirds' (= 66.7%) and '74%' — those two fractions contradict each other, and neither matches the actual 82.5%.
  - evidence: Arithmetic: 685485 + 158298 = 843783; table column sum = 1,022,225; 843783/1022225 = 0.825. The entry's own table is the source — no external fetch needed.
  - fix: Change the sentence to: 'More than four-fifths of all individual-donor money to Langworthy ($843,783, or 83% of the $1.02M-county-mapped total) comes from two counties — Erie and Niagara.' Remove 'Two-thirds.'

- **[internal-contradiction]** The single largest concentration of Chemung-resident donors — $16,255 — works for Corning Incorporated
  - issue: The stated $16,255 subtotal does not match the sum of the eight donor rows listed immediately below it. Summing the table: Hal Nelson $9,000 + Stefan Becker $3,505 + Andrew Beck $1,250 + Philip Cowley $1,250 + Ron Verkleeren $1,000 + David Velasquez Jr. $505 + Kathryn Schrock $500 + Chad Keenan $500 = $17,510. The discrepancy is $1,255.
  - evidence: Row-by-row arithmetic from the entry's own table: [9000, 3505, 1250, 1250, 1000, 505, 500, 500] sums to 17,510, not 16,255.
  - fix: Either correct the stated subtotal to $17,510 (if all rows are accurate) or identify and correct the row(s) with wrong figures.


### 2026-06-02-rural-health-transformation-212m

- **[factual-error]** only two Republicans defected (Davidson, Massie)
  - issue: Warren Davidson (OH) voted Aye on Roll Call 190 — he was NOT a defector. The two Republican No votes were Brian Fitzpatrick (PA) and Thomas Massie (KY), per clerk.house.gov/evs/2025/roll190.xml.
  - evidence: curl https://clerk.house.gov/evs/2025/roll190.xml parsed: Davidson (R-OH) = Aye; Fitzpatrick (R-PA) = No; Massie (R-KY) = No. Republican Nays: 2 (Fitzpatrick, Massie only).
  - fix: Change '(Davidson, Massie)' to '(Fitzpatrick, Massie)' at line 111.


### 2026-06-06-langworthy-secure-data-act-hr8413

- **[factual-error]** $270,500 across 21 PACs whose organizations signed the SECURE Data Act endorser-coalition letter have contributed to Rep. Langworthy's two campaign committees across the 2024 and 2026 cycles. Per-PAC figures: Charter $35K, Cox $25K, Comcast/NBC $16K, Verizon $14K, AT&T $12K, NCTA $13K, T-Mobile $6K, Int'l Franchise $24K, NAR $18K, Walmart $16K, National Restaurant $15K, AHLA $4K, NACS $4K, Marathon $20K, Chevron $20K, ExxonMobil $12K, Energy Marketers $9K, Google $2K, BSA $1.5K.
  - issue: Every per-PAC dollar figure except BSA ($1,500) is exactly 2x the amount in the FEC bulk data files. The query methodology (joining pas224/pas226 against both cm24 and cm26 for committee names) produces one row per cm-file match, doubling every contribution because each PAC appears in both cm24.txt and cm26.txt. Verified against FEC bulk data directly: Charter actual=$17,500, Cox=$12,500, Comcast=$8,000, Verizon=$7,000, AT&T=$6,000, NCTA=$6,500, T-Mobile=$3,000, Int'l Franchise=$12,000, NAR=$9,000, Walmart=$8,000, National Restaurant=$7,500, AHLA=$2,000, NACS=$2,000, Marathon=$10,000, Chevron=$10,000, ExxonMobil=$6,000, Energy Marketers=$4,500, Google=$1,000. Correct grand total for those 19 named PACs is approximately $135,250, not $270,500.
  - evidence: Direct query of /Users/zachbeaudoin/data/public-ledger/federal/fec/pas224.txt and pas226.txt filtered to Langworthy committee IDs C00817932 and C00832188. Every named PAC (except BSA) shows exactly half the entry's stated amount. Root cause: all PACs appear in both cm24.txt and cm26.txt, so a join against both produces 2 rows per contribution.
  - fix: Re-run the FEC query joining against a deduplicated committee master (UNION rather than UNION ALL on cm24/cm26, or join on a single file). Correct the grand total to approximately $135,250 and update every per-PAC figure to its actual amount.

- **[internal-contradiction]** Retail sector total: $77,000 (from Int'l Franchise $24K + NAR $18K + Walmart $16K + Natl Restaurant $15K + AHLA $4K + NACS $4K).
  - issue: Internal arithmetic inconsistency. The six named Retail-sector PAC figures sum to $81,000 ($24K+$18K+$16K+$15K+$4K+$4K), not $77,000 as stated in the sector total. Additionally, the four sector subtotals ($121K+$77K+$61K+$3.5K=$262.5K) do not match the claimed grand total of $270,500 (a $8,000 gap), which implies 2 additional unnamed PACs at roughly $4,000 each — but those PACs are not identified.
  - evidence: Sum of six retail-sector PAC figures listed in the entry: 24000+18000+16000+15000+4000+4000=81000, not 77000. Sum of all sector totals: 121000+77000+61000+3500=262500, not 270500.
  - fix: Correct the Retail sector subtotal to $81,000 (or revise individual PAC figures). Reconcile sector subtotals with the grand total and identify the 2 unnamed PACs that account for the $8,000 gap, or revise the grand total to match the sum of stated sectors.


### 2026-06-10-jasper-troupsburg-fema-award

- **[factual-error]** intermediate FEMA obligations to the district (over $5.6 million in 2022, $6.5 million subsequently)
  - issue: The $6.5M figure is a combined school-district-plus-county award, not a district-only figure. The sourced Schumer release (August 19, 2025) shows $6,563,318 total: $2,946,315 to Jasper-Troupsburg CSD and $3,617,003 to Steuben County for road repair (County Route 129 retaining wall/pavement). The entry phrases this as obligations 'to the district,' which overstates the district's share of that release by more than 2x.
  - evidence: Schumer release sourced at the second advocacy-history bullet (schumer.senate.gov) confirms the $6.5M split: $2,946,315.09 (Jasper-Troupsburg CSD) + $3,617,003.17 (Steuben County). The entry's parenthetical groups both amounts as 'obligations to the district.'
  - fix: Change to: 'over $5.6 million in 2022 for the school district, and a subsequent $6.5 million combined award (roughly $2.95 million to the district, $3.6 million to Steuben County for road repair) in August 2025.' Or simply drop the $6.5M from the district-only framing and cite both releases accurately.


### 2026-06-10-minnesota-fraud-50-state-claim

- **[internal-contradiction]** "The DOJ indicted 79 defendants and secured roughly 65 convictions" (Questions This Raises, line 103)
  - issue: Internal contradiction with the Claim 1 body (line 56), which states "at least 77 defendants indicted" and "more than 50 have been convicted." The entry's own comment block (line 166) explicitly notes that the earlier draft figures "79 indicted / ~65 convicted" were corrected in the body because they "came from search summaries and could not be confirmed in fetchable primary sources" — but the Questions section was not updated, leaving the stale, uncorrected figures live. The KSTP source (the cited primary for these numbers) confirms "more than 50 convicted" but does not give a total defendant count; the DOJ "77th defendant" press release title supports "at least 77." Neither sourced figure supports "79" or "65."
  - evidence: Line 56: "at least 77 defendants indicted" / "more than 50 have been convicted"; Line 103: "79 defendants" / "roughly 65 convictions"; Line 166 comment: "earlier draft figures '25 warrants / 79 indicted / ~65 convicted / 41.5 years' corrected — they came from search summaries and could not be confirmed in fetchable primary sources"; KSTP fetch confirms "more than 50 convicted" only.
  - fix: Update line 103 to match the sourced figures already in the body: "The DOJ has indicted at least 77 defendants and secured more than 50 convictions" (or whatever figures the sourced DOJ/KSTP releases support). Remove "79" and "roughly 65" — the comment block already acknowledges these are unverifiable.


---

## SOFT CRITICALS (unsupported — needs sourcing or removal)


### 2025-08-veterans-support

- **[unsupported]** Direct quote attributed to an unnamed veteran: 'He shows up on Veterans Day to shake our hands, but his vote kept the government shut down while active duty troops weren't getting paid. That's not supporting veterans.' Attributed to Olean Times Herald interview. Direct quote attributed to VFW Post 527 in Hornell: 'You can't claim to support the military and then vote to shut down their paychecks.'
  - issue: Both quotes lack a verifiable primary source. The frontmatter has empty source_url and archived_url fields. The Sources section cites only the Olean Times Herald homepage (not a specific article URL) and lists 'Veterans of Foreign Wars (VFW): Statements on shutdown impact' with no URL or archive link. Neither quote can be confirmed against a primary document.
  - evidence: Frontmatter: source_url: '' and archived_url: ''. Sources section links to https://www.oleantimesherald.com/ (homepage only, not the specific article). No URL or archive link for VFW Post 527 Hornell statement. No direct URL to any article containing either quote.
  - fix: Locate and archive the specific Olean Times Herald article containing the veteran quote (Nov 11, 2025 issue per the entry's own dating). For the VFW Post 527 statement, obtain a written record, meeting minutes, or press release and archive it. If primary sources cannot be located, remove the verbatim quotes and paraphrase with a hedged attribution.


### 2025-09-salt-tax-relief

- **[unsupported]** Corporate tax cuts cost 'estimated $1.8 trillion cost over 10 years'; CBO publication 61387 cited
  - issue: The cited CBO source (cbo.gov/publication/61387) returns HTTP 403 and cannot be verified. The $1.8T figure does not match known OBBBA cost estimates: JCT estimated total net tax cuts at $4.5T; CBO estimated $4.1T in additional borrowing. No verified source for $1.8T as the cost of the 'corporate tax cut component' specifically.
  - evidence: CBO publication URL returns 403. Existing site fact-checks cite JCT $4.5T and CBO $4.1T for the full bill, not $1.8T for corporate provisions alone.
  - fix: Replace with a verifiable, archived CBO or JCT estimate tied to a specific provision, with a working source URL.

- **[unsupported]** Langworthy quote: 'New York families are being crushed by high taxes. We need to restore the SALT deduction to give our constituents relief.'
  - issue: No archive URL, no specific article title, and no direct link to the primary source for this quote. The source fields in frontmatter are empty (source_url: '', archived_url: ''). The attributed sources (WGRZ Buffalo, Roll Call) are listed only with homepage URLs, not specific articles. Cannot verify the quote appears in any cited source.
  - evidence: Frontmatter source_url and archived_url are both empty strings. Source links go to wgrz.com and rollcall.com homepages only, not specific articles. No archive.org URL provided for either source.
  - fix: Provide a specific article URL and archive.org backup for each cited source. If the quote cannot be sourced to a primary document, remove it.

- **[unsupported]** Constituent quote from WGRZ Buffalo: 'He told us SALT was his priority, then he voted for a bill that gave corporations billions while we're still capped at $10,000.'
  - issue: No specific WGRZ article URL or archive link. The only WGRZ source listed is the homepage. This constituent quote cannot be traced to any primary source. Additionally, the quote's premise ('still capped at $10,000') is factually incorrect given that OBBBA raised the SALT cap to $40,000.
  - evidence: Source URL in entry is wgrz.com (homepage only). No specific article title or archive URL. The quote's embedded factual claim about the $10K cap persisting is inconsistent with OBBBA's actual SALT provision.
  - fix: Link to the specific WGRZ article and its archive.org copy, or remove the quote. Correct the embedded factual error about the SALT cap level.

- **[unsupported]** Roll Call noted Langworthy was among House Republicans who 'publicly lobbied for SALT relief but voted for the package without it when leadership applied pressure'
  - issue: The Roll Call source is cited only as the homepage (rollcall.com), with no specific article, no date, no headline, and no archive URL. This paraphrase cannot be verified. Given that OBBBA did include a $40K SALT cap, the Roll Call framing as described ('package without [SALT relief]') would itself be inaccurate.
  - evidence: Roll Call source in entry links to rollcall.com homepage only. No specific article identified. WebFetch of rollcall.com current homepage shows no matching article.
  - fix: Link to the specific Roll Call article with archive URL, or remove the attribution.


### 2025-10-government-shutdown-aca

- **[unsupported]** "We must ensure critical services continue and our military families don't miss a paycheck."
  - issue: The cited WSKG article does not contain this quote. The only Langworthy quotes confirmed by that source are 'Governing means putting your country first, putting the taxpayers first' and 'You keep the lights on in the government for the American people, and that's what responsible leadership looks like.' The military paycheck quote is not sourced to any linked primary document.
  - evidence: WebFetch of WSKG (the entry's sole primary source for Langworthy quotes) returned no military paycheck statement. The entry lists only WSKG and WLEA as sources for his public statements; the WLEA article covers September 2023 CR votes only, not 2025.
  - fix: Remove or bracket the military-families quote until a primary source URL (press release, transcript, or contemporaneous news article) is identified and cited.


### 2025-10-rural-hospitals-pure-fiction

- **[unsupported]** Individual hospital operating margins: Westfield -59.1%, Upper Allegheny/Olean General -31.1%, Schuyler Hospital -23.1%, UPMC Chautauqua -17.4%, Cuba Memorial negative, Arnot-Ogden negative, with specific Medicaid dependency percentages (UPMC 37%, Cuba Memorial 42%, Arnot-Ogden 42%)
  - issue: These per-hospital margin figures are attributed to the Fiscal Policy Institute, but the cited FPI article does not contain individual hospital operating margins or specific Medicaid dependency percentages for named facilities. FPI only reports that '8 out of 12 hospitals rely on Medicaid funding' at an aggregate level.
  - evidence: WebFetch of fiscalpolicy.org/new-york-hospitals-will-close-under-the-one-big-beautiful-bill-act confirmed: 'The document does not list any hospital operating margins... does not provide individual hospital percentages.' The table in Section A appears to be sourced elsewhere (likely CHQPR or HANYS data) but no citation is given for the specific figures.
  - fix: Add an explicit source citation for the per-hospital margin and Medicaid dependency data (e.g., CHQPR state-level hospital data or HANYS). Do not attribute these figures to FPI since they do not appear in that report.


### 2025-11-aca-subsidies-false-claim

- **[unsupported]** "There's some people that make $300,000 or $400,000 a year that are somehow leveraging that into free health care. I don't agree with that."
  - issue: The entry's frontmatter `source_url` links to the WSKG article, and the statement header reads 'Reported by: WSKG, WRFA-LP Jamestown.' The $300K/$400K quote does NOT appear in the WSKG article (fetched: WSKG contains only a general quote about 'shoveling money'). The quote is confirmed in the WRFA article (https://www.wrfalp.com/rep-langworthy-not-committing-to-voting-on-aca-enhanced-tax-credits-extension/). The WSKG URL should not be the primary `source_url` for this quote; it is a dead source for this specific claim.
  - evidence: WebFetch of WSKG URL returned no mention of $300K/$400K or free health care claim. WebFetch of WRFA URL confirmed exact quote.
  - fix: Change `source_url` in frontmatter to the WRFA URL (https://www.wrfalp.com/rep-langworthy-not-committing-to-voting-on-aca-enhanced-tax-credits-extension/). The WSKG article can remain as an additional source in the Sources section.

- **[unsupported]** Over 6,300 residents in NY-23 are enrolled in the ACA marketplace (per KFF)
  - issue: The figure is attributed to KFF, but both KFF links cited are (1) the interactive premium calculator (user-input tool with no published enrollment counts) and (2) a national-average premium article. Neither source contains NY-23 enrollment figures. The 6,300 number has no verifiable citation in the entry.
  - evidence: WebFetch of KFF calculator URL confirmed it is an individual estimator with no county or district enrollment data. WebFetch of the KFF premium article confirmed it provides national-level analysis only, no NY-23 or Chautauqua figures.
  - fix: Replace KFF citation with the actual source for the 6,300 figure (likely CMS/HHS state-level marketplace enrollment report or KFF state health facts enrollment table). If the figure came from Gillibrand's office, cite that explicitly.


### 2025-12-farm-workforce

- **[unsupported]** Introduced H.R. 3550 (Market-Driven Inventory System) - dairy pricing
  - issue: H.R. 3550 does not belong to Langworthy in either the 118th or 119th Congress. In the 118th, H.R. 3550 is the 'Safe Interactions Act' (disability org grants), sponsored by Rep. Susan Wild (D-PA-7). In the 119th, H.R. 3550 is sponsored by Rep. Nancy Mace (R-SC-1). No verified Langworthy dairy pricing bill carries this number. The bill number appears to be fabricated or incorrectly assigned.
  - evidence: govinfo BILLSTATUS-118hr3550.xml: sponsor Rep. Wild, title 'Safe Interactions Act of 2023'. BILLSTATUS-119hr3550.xml: sponsor Rep. Mace.
  - fix: Remove or correct H.R. 3550. Identify Langworthy's actual dairy-related bill number before publishing, or remove the bill number claim entirely.

- **[unsupported]** Introduced H.R. 3638 - maple syrup producer support
  - issue: H.R. 3638 does not belong to Langworthy in either the 118th or 119th Congress. In the 118th, H.R. 3638 is 'Protecting Federal Funds from Human Trafficking and Smuggling Act of 2023', sponsored by Rep. Lance Gooden (R-TX-5). In the 119th, H.R. 3638 is sponsored by Rep. Robert Latta (R-OH-5). No verified Langworthy maple syrup bill carries this number.
  - evidence: govinfo BILLSTATUS-118hr3638.xml: sponsor Rep. Gooden, title 'Protecting Federal Funds from Human Trafficking and Smuggling Act of 2023'. BILLSTATUS-119hr3638.xml: sponsor Rep. Latta.
  - fix: Remove or correct H.R. 3638. Identify Langworthy's actual maple syrup bill number before publishing, or remove the bill number claim entirely.


### 2025-12-rhetoric-vs-actions-overview

- **[unsupported]** "I won't answer to small angry groups" — presented as a direct Langworthy quote, attributed as a "Response to constituents requesting face-to-face forums." No source cited.
  - issue: No source is cited for this quote in the entry. The fuller and differently-worded actual quote appears only in a sibling entry (2026-02-10-tioga-county-federal-impact.md): "I will not answer to a small and angry group of constituents that are constantly harping on this topic," spoken in response to AFSCME members protesting at his Corning office — a different context than "constituents requesting face-to-face forums." The condensed version presented here is an unsourced paraphrase displayed as a verbatim direct quote.
  - evidence: grep across entire content directory finds the full/actual version only in content/fact-checks/2026-02-10-tioga-county-federal-impact.md (AFSCME protest context). The audited entry has no URL, no citation, and a materially different wording.
  - fix: Cite the primary source (news article or video), use the full actual wording from the Tioga entry, and correct the context attribution to the Corning office AFSCME protest.

- **[unsupported]** OBBBA SNAP table row: "Benefit costs shift to states with error rates above 6% | ~$1.2B annually to NY"
  - issue: The $1.2B annually figure has no cited source in this entry and appears in no other entry or source file in the corpus. The SNAP cuts entry (2025-12-snap-cuts.md) does not mention a $1.2B annual figure for NY. This specific number is unsourced and unverifiable from the entry's own citations.
  - evidence: grep -rn '1.2 billion|1.2B|1,200.*million|1.2.*annually' across all content returns only this line in the audited entry. The cited source list for the SNAP section does not include a URL that would contain this figure.
  - fix: Add a primary source (CBO score, CBPP analysis, or state DOL estimate) that supports the $1.2B NY-specific annual figure, or remove/hedge this claim until sourced.


### 2025-12-snap-cuts

- **[unsupported]** FeedMore WNY (serving Western New York) reported a 16% increase in food assistance need in 2024.
  - issue: The cited WKBW article does not contain a '16% increase in 2024' figure. The article's only percentage is a '46% increase in people served since 2021.' The 16% figure appears nowhere in the cited source.
  - evidence: WKBW article (the entry's own cited source) states: 'The growing demand marks a 46% increase in people served since 2021—excluding emergency response efforts.' No 16% figure appears in the article text.
  - fix: Replace '16% increase in food assistance need in 2024' with '46% increase in people served since 2021' (per WKBW/FeedMore WNY), or source the 16% figure to a different primary document.


### 2025-12-worker-safety-scaffold-law

- **[unsupported]** Construction worker deaths in New York (2023): 74 fatalities (48% increase from prior year); Falls from heights account for 40%+ of fatalities
  - issue: No source is cited for these statistics anywhere in the entry. The FingerLakes1 article and Langworthy press release — the two primary cited sources — contain none of these figures. No BLS, OSHA, or DOL citation is provided. These figures appear in the 'Safety Context' and 'In Plain Language' sections without attribution.
  - evidence: FingerLakes1 article (fetched): no mention of 74 fatalities, 48% increase, or 40%+ falls. Langworthy press release (fetched): no mention of these figures. Entry contains no source citation for the Safety Context statistics block. BLS/OSHA pages returned 403, making independent verification impossible, but the entry itself provides no cited source.
  - fix: Add a specific primary source (BLS CFOI report, NYSDOL fatality data) for the 74 fatalities / 48% increase / 40%+ falls figures, or remove them until sourced.


### 2026-02-08-steuben-ice-cooperation

- **[unsupported]** Local news coverage documented Steuben County residents publicly opposing proposed cooperation agreements between the county and federal immigration enforcement. One article headline stated: 'We are all afraid.'
  - issue: The entire entry's central factual claim rests on a single local news article that is completely unsourced. The source link goes only to the mytwintiers.com homepage (not a specific article URL), both source_url and archived_url frontmatter fields are empty strings, mytwintiers.com returns HTTP 403 to all fetch attempts, and no other file in the corpus corroborates the story or the quoted headline. The claim is asserted as documented fact with no working, verifiable source. Per the site's own standards, all sources must be archived via Wayback Machine.
  - evidence: source_url: "" and archived_url: "" in frontmatter (lines 8-9). Sources section links only to https://www.mytwintiers.com/ (homepage). mytwintiers.com returns HTTP 403 to all WebFetch attempts. No corroborating reference in any other corpus file.
  - fix: Locate the specific mytwintiers.com article URL, archive it via Wayback Machine (curl -I https://web.archive.org/save/[URL]), populate source_url and archived_url in frontmatter, and update the Sources section link to point to the specific article rather than the domain homepage.


### 2026-02-10-save-act-voter-id

- **[unsupported]** 21+ million U.S. citizens do not have readily accessible documentary proof of citizenship
  - issue: No specific primary source is cited for this figure. The sources list says 'U.S. Census Bureau: Citizenship documentation accessibility data' with no URL, no report title, no year, and no ACS table reference. The Brennan Center's cited report ('Debunking the Voter Fraud Myth') was verified via WebFetch and does not contain this figure. This is a high-impact claim presented as a specific count with no verifiable citation.
  - evidence: WebFetch of https://www.brennancenter.org/our-work/research-reports/debunking-voter-fraud-myth confirmed: 'The report does not cite a figure of 21 million citizens lacking readily accessible documentary proof of citizenship.' The sources section lists no URL for the Census claim.
  - fix: Either cite the specific source (e.g., a GAO report, a specific Brennan Center study on ID availability, or the frequently-cited NYU Brennan Center '21 million' figure from their 2006 report 'Citizens Without Proof') with a direct URL and archive link, or soften to a hedged estimate with proper attribution.


### 2026-02-10-tioga-county-federal-impact

- **[unsupported]** Governor Hochul's office estimates 66,000 people in Langworthy's district will lose healthcare coverage under the law.
  - issue: This district-level figure is not verifiable from the cited source (Hochul's office OBBBA analysis). The primary Hochul press release (governor.ny.gov/news/numbers-republican-big-ugly-bill...) provides NY-23 data only for hospital employment losses (759) and economic activity ($320M) — not coverage loss by district. No URL is cited for this specific 66,000 figure. The figure appears nowhere else on the site. The sourced Hochul statewide figure is 1.5 million New Yorkers, but no methodology for the district-level 66,000 derivation is provided or linked.
  - evidence: WebFetch of governor.ny.gov press release confirmed it contains NY-23 hospital employment/economic impact data (759 jobs, $320M activity) but no 66,000 coverage loss figure for the district. The sources section lists only 'Governor Hochul's Office: OBBBA healthcare coverage impact estimates' with no URL. The figure appears in no other site entry.
  - fix: Add the URL of the specific Hochul analysis that yields the 66,000 district figure, or replace with the verifiable statewide figure (1.5 million New Yorkers) and note no district-level breakdown has been published by the Governor's office.


### 2026-02-20-scotus-tariff-ruling

- **[unsupported]** Tax Foundation calculated that Trump's tariffs constituted the largest U.S. tax increase as a share of GDP since 1993
  - issue: Tax Foundation does not say 'since 1993.' Their published analysis ranks the tariffs as the '20th largest tax increase since 1940,' with the relevant metric being 0.31% of GDP in 2026. The 'since 1993' framing is not supported by the cited source.
  - evidence: Tax Foundation tariff research page (https://taxfoundation.org/research/all/federal/tariffs/) states: 'newly imposed and scheduled tariffs will increase federal tax revenues by $98 billion in 2026, or 0.31 percent of GDP, ranking as the 20th largest tax increase since 1940.' No 'since 1993' claim found.
  - fix: Change to 'ranked as the 20th largest tax increase since 1940' or remove the comparative framing and cite the exact GDP percentage.

- **[unsupported]** The Tax Foundation estimated the now-voided IEEPA tariffs would have raised $1.4 trillion over a decade
  - issue: The Tax Foundation does not publish a $1.4 trillion decade-revenue estimate for IEEPA tariffs. Their page references ~$166 billion in IEEPA tariff refund liability and ~$958 billion in combined Section 232+122 decade revenue. The $1.4 trillion figure is unsupported by the cited source.
  - evidence: Tax Foundation tariff research page lists conventional revenue estimates of $934.1B (Section 232) and $23.7B (Section 122) for 2026-2035, totaling ~$957.8B. The $1.4 trillion figure does not appear on the page.
  - fix: Remove or replace the $1.4 trillion figure with a sourced estimate, or attribute to a different source (e.g., Penn Wharton or CBO) if one of them published that projection.


### 2026-02-28-epic-fury-statement

- **[unsupported]** Iranian Supreme Leader Ayatollah Ali Khamenei was confirmed killed.
  - issue: No specific source is cited for this claim. The entry's source table lists only 'CENTCOM initial release,' 'CENTCOM via USNI News,' and 'CBS News / CENTCOM' for the casualty figures, but none of those cover the Khamenei death. The frontmatter source_url and archived_url both point to the CENTCOM press releases index page, not to any specific release confirming Khamenei's death. This is the highest-stakes factual assertion in the 'What Happened' section and it has no traceable primary source citation.
  - evidence: Lines 39: 'Iranian Supreme Leader Ayatollah Ali Khamenei was confirmed killed.' Sources section (lines 195–201) cites only the CENTCOM press releases index, USNI News homepage, CBS News homepage, Politico homepage, and Just Security homepage — no specific article confirming Khamenei's death.
  - fix: Add a direct citation (specific URL and archive URL) for the source that confirms Khamenei's death. If no single CENTCOM release confirms this, cite the specific news outlet and article that reported it. If the confirmation is from multiple converging reports, name them explicitly.


### 2026-02-telephone-town-hall

- **[unsupported]** His standalone floor vote (H.R. 4405 on Nov 18, 2025) came only after 271 House members had already voted YES.
  - issue: The '271 members had already voted YES' figure is unsupported and appears to be wrong. The Nov 18, 2025 floor vote on H.R. 4405 (Roll 289) passed 427-1 — not 271 yes votes. There is no prior recorded House vote where 271 members voted yes on H.R. 4405. The '271' may be a confusion with discharge petition signatures (H.Res. 867) or some other number, but the entry presents it as a prior floor-vote tally without any source.
  - evidence: clerk.house.gov Roll 289: H.R. 4405 Epstein Files Transparency Act, Nov 18 2025, Passed 427-1, Langworthy = Aye. No prior floor vote found. The '271' figure has no sourced basis in the entry.
  - fix: Remove or correct the '271 House members had already voted YES' claim. The actual floor vote total was 427-1. If the intent is to note a discharge petition, cite the number of petition signatories separately and with a source, and do not conflate it with a prior YES vote tally.


### 2026-03-08-defense-suppliers-visit

- **[unsupported]** Source: Facebook Post, approximately March 8, 2026 (with source_url and archived_url both blank).
  - issue: The entry's primary source — the Facebook post containing the quote — has no URL and no archive link. The source_url and archived_url frontmatter fields are both empty. Without a linked or archived source, the verbatim quote (including the misspelling 'Astonics' and 'Elma') cannot be independently verified. This is the foundational claim of the entire fact-check.
  - evidence: Frontmatter lines 8-9: source_url: "" and archived_url: ""
  - fix: Add the direct Facebook post URL (or screenshot) and archive it via Archive.org. Per site standards (CLAUDE.md), all sources must be archived. If the post was deleted, note that and provide the archive.org snapshot.


### 2026-03-14-seneca-nation-law-enforcement-act

- **[unsupported]** The lobbying pattern table shows 'Oneida Indian Nation | $3,500 | May 2025' as a row in a section introduced as showing Seneca Nation of Indians contributions
  - issue: The table header says 'FEC records show the Seneca Nation of Indians gives strategically' — but the Oneida Indian Nation row is a separate tribal entity, not a Seneca Nation contribution. More critically, FEC records for Oneida Indian Nation show no $3,500 contribution in May 2025; the earliest Oneida Indian Nation FEC records visible are from 2026. The date and amount are unverified and the inclusion in a Seneca Nation table is structurally misleading, even though the cell note says 'Separate tribe.'
  - evidence: FEC API: api.open.fec.gov/v1/schedules/schedule_a/?contributor_name=oneida+indian+nation — no records found for May 2025. Earliest records are 2026. The table section heading attributes all rows to Seneca Nation of Indians giving pattern.
  - fix: Remove the Oneida Indian Nation row from this table entirely, or move it to a clearly separate section with its own FEC citation. If the $3,500 May 2025 figure cannot be sourced to an FEC record, do not publish it.


### 2026-03-21-ida-donor-exemption-pattern

- **[other]** County-Level Data section links Greene County, Nassau County, Rensselaer County, and Onondaga County as county scorecards
  - issue: None of these four counties are in NY-23. Greene County is in the Hudson Valley; Nassau is Long Island; Rensselaer is in the Albany area; Onondaga is in the Syracuse area. Presenting them under a heading 'County-Level Data' in a NY-23 accountability entry, with no explanation that they are outside the district, is misleading. Only Erie and Tioga in that list are actually NY-23 counties.
  - evidence: NY-23 canonical counties per CLAUDE.md: Allegany, Cattaraugus, Chautauqua, Chemung, Erie (partial), Schuyler (partial), Steuben (partial), Tioga. Greene/Nassau/Rensselaer/Onondaga appear on no canonical NY-23 county list.
  - fix: Remove or clearly label out-of-district counties. The section should only present NY-23 counties, or explicitly state these are provided as statewide comparators.


### 2026-04-07-wftc-refund-claims

- **[unsupported]** IRS data shows approximately 4.6 million filers claimed the tips deduction — not 5.7 million — overstating by approximately 24%
  - issue: The entry's counter-figure of ~4.6 million is not present in its cited sources. The two IRS filing season statistics pages (March 27 and April 3) contain no tip or overtime filer counts at all — confirmed by direct fetch. The Bipartisan Policy Center source the entry does cite states 'around five million tax units' for tips, which is materially closer to Langworthy's 5.7M than to the entry's rebuttal figure. The entry's '~4.6 million' appears to be unsourced, and the 'OVERSTATED' verdict it delivers against Langworthy may itself be using an unsupported lower bound.
  - evidence: WebFetch of https://www.irs.gov/newsroom/filing-season-statistics-for-week-ending-march-27-2026 and the April 3 equivalent both returned no tip/overtime filer data. WebFetch of https://bipartisanpolicy.org/explainer/whats-driving-higher-tax-refunds-in-2026/ (a cited source) states 'around five million tax units' for tips deduction — not 4.6 million.
  - fix: Replace the '~4.6 million' counter-figure with the ~5 million estimate from the BPC source the entry already cites, or identify the actual primary IRS source for the specific count. If 4.6M came from a specific IRS WFTC statistics page not currently cited, add that citation.

- **[unsupported]** IRS data showed approximately 20 million filers claimed the overtime deduction — not 23 million — overstating by approximately 15%
  - issue: The entry's counter-figure of ~20 million is not present in its cited IRS filing season statistics pages (which contain no overtime filer counts). The BPC source the entry cites states the Tax Policy Center estimates 'around 17 million tax units' for overtime — not 20 million. The entry's own rebuttal figure (~20M) is itself approximately 18% higher than what the entry's own cited source actually says (~17M).
  - evidence: WebFetch of https://bipartisanpolicy.org/explainer/no-tax-on-overtime-in-2026/ (cited in entry) states 'The Tax Policy Center estimates that 17 million filers will benefit from the deduction.' WebFetch of https://bipartisanpolicy.org/explainer/whats-driving-higher-tax-refunds-in-2026/ (also cited) states 'around 17 million tax units' for overtime. Neither supports ~20 million.
  - fix: Replace the '~20 million' counter-figure with ~17 million (the Tax Policy Center/BPC estimate from the entry's own cited sources), and note this is a prospective estimate rather than confirmed IRS filing data. Alternatively, identify the actual primary IRS source for a 20M filing-season count and add that citation.


### 2026-04-17-obbba-working-families

- **[unsupported]** The Congressional Budget Office estimated these provisions will result in approximately 10 million people losing health coverage by 2034.
  - issue: Cannot verify the '10 million' figure or '2034' year against the CBO source. CBO returns HTTP 403. The source URL is listed but has no archive URL (marked TODO). Widely-reported CBO estimates for the enacted OBBBA Medicaid provisions cite figures in the 7-8 million range for Medicaid specifically; '10 million' may reflect total uninsured increase including ACA marketplace and other provisions combined, or may reflect a different CBO baseline. The entry does not specify what population or coverage categories this figure covers. The claim is unverifiable as cited.
  - evidence: CBO URL (https://www.cbo.gov/publication/61387) returns HTTP 403. Archive URL is marked TODO — no backup source available. The IRS source cited in frontmatter does not cover Medicaid.
  - fix: Fetch the CBO score directly or cite the specific table/line item. Clarify whether 10 million is total uninsured increase or Medicaid-only. Add archive URL. If the confirmed figure is lower (e.g., 7.6M Medicaid-only), update the text.

- **[unsupported]** The Urban Institute projected 22.3 million households would lose some or all SNAP benefits.
  - issue: No source URL is provided (marked TODO). Cannot verify the 22.3 million figure. The Brookings article (a cited secondary source) references Urban Institute for '3.3 million families with children' losing SNAP benefits — a very different and much smaller number. The 22.3 million figure may refer to all households affected in any way (including partial reductions), while 3.3 million may be families with children facing full loss, but without the primary Urban Institute report there is no way to confirm scope, definition, or that the figures are not being conflated.
  - evidence: Source listed as 'Urban Institute / CNBC' with no URL (TODO placeholder). Brookings fetch returned '3.3 million families with children' as the Urban Institute figure, not 22.3 million. The two numbers are not reconciled.
  - fix: Locate the primary Urban Institute report, confirm the 22.3 million figure and its definition (all affected households vs. full-loss households), add the URL and archive URL. If 22.3 million includes partial reductions, add a qualifier: 'lose some or all benefits.'

- **[unsupported]** The IRS page (source_url and archived_url in frontmatter) is cited as the primary source, but the entry's core load-bearing claims — CTC refundable cap of $1,700, Child Care Credit 50% rate, Dependent Care FSA cap of $7,500 and effective date — are not present on that IRS page.
  - issue: The IRS 'One Big Beautiful Bill Provisions' page covers Trump Accounts and the Adoption Credit. It does not address the Child Tax Credit, Child and Dependent Care Credit, or Dependent Care FSA provisions that make up Claims 1-3. All actual sources for those claims (H&R Block, Poppins Payroll, Seyfarth Shaw, Western CPE) are listed with TODO placeholders — no URLs or archive URLs. The entry's most specific and consequential claims have no verifiable primary source linked.
  - evidence: IRS page fetch confirms: 'Child Tax Credit and Child Care Credit: Not mentioned on this page' and 'Dependent Care FSA: Not mentioned on this page.' All four other source entries for these claims have no URLs (TODO).
  - fix: Replace or supplement the frontmatter source_url with a source that actually covers CTC, CDCTC, and FSA provisions (e.g., the IRS FAQs or the bill text itself). Fill in TODO URLs for H&R Block, Seyfarth Shaw, Poppins Payroll, and Western CPE sources, and add archive URLs per site standards.


### 2026-04-30-farmbill-snap-context

- **[unsupported]** 3 million Americans projected to lose SNAP
  - issue: The cited CBPP source does not support the '3 million' figure. The CBPP brief states approximately 4 million will see benefits 'terminated or cut substantially,' and about 2.4 million will be cut in a typical month under the work-requirement expansion. No single '3 million' total appears in the source.
  - evidence: CBPP 'By the Numbers' page fetched directly: '~4 million people will see benefits terminated or cut substantially'; '~2.4 million people will be cut from SNAP in a typical month.' The entry's '3 million' matches neither figure.
  - fix: Replace '3 million' with the sourced figure. Options: '4 million will see benefits terminated or cut substantially' or 'approximately 2.4 million cut in a typical month under expanded work requirements' — attribute directly to CBPP with the specific framing used.

- **[unsupported]** ~19,000 NY-23 residents projected to lose SNAP (CBPP estimate)
  - issue: The CBPP source cited ('By the Numbers') contains no district-level data for NY-23. The ~19,000 figure is attributed to 'CBPP estimate' but the CBPP brief has no Congressional-district breakdown. This is an unsourced figure presented as a named-source estimate.
  - evidence: CBPP 'By the Numbers' page fetched directly: 'The document contains no district-specific data for New York's 23rd Congressional District. State-level information is referenced as available elsewhere, but no NY-23 figures appear in this particular policy brief.'
  - fix: Either locate the specific CBPP or Food Research & Action Center district-level tool that produced the ~19,000 figure and cite that URL directly, or remove the figure until a primary source is identified. Do not attribute district-level estimates to a national brief that does not contain them.


### 2026-04-30-scotland-trip-service-claim

- **[unsupported]** Speaker Johnson had canceled his own international trip during the same period.
  - issue: No citation is provided for this claim, and none of the three cited sources (TMZ, Political Wire, Semafor) mention it. This is a specific comparative fact used to sharpen the contrast section and needs an explicit source.
  - evidence: TMZ article confirmed: no mention of Johnson cancellation. Political Wire article confirmed: no mention. Semafor article confirmed: no mention. Entry provides no citation for this claim.
  - fix: Add a citation (news article or official statement) documenting Johnson's trip cancellation, or remove the claim until sourced.


### 2026-05-20-halt-act-collins-causal-claim

- **[unsupported]** Persons held beyond 15 days must be transferred to a Residential Rehabilitation Unit providing 6 hours/day of programming and 1 hour of recreation
  - issue: The NYSBA source (cited in the entry as source 2) states the RRU requires 'at least four hours of out-of-cell time daily, which includes at least two hours of therapeutic programming and two hours of recreation.' The entry's figures — 6 hours programming and 1 hour recreation — conflict with the entry's own cited source on both counts. No other cited source supports the 6-hour / 1-hour breakdown.
  - evidence: NYSBA (nysba.org/the-halt-act-and-solitary-confinement-in-new-york-state/): '...at least four hours of out-of-cell time daily, which includes at least two hours of therapeutic programming and two hours of recreation.' Entry states: '6 hours/day of programming and 1 hour of recreation.'
  - fix: Correct to: 'at least 4 hours/day of out-of-cell time, including 2 hours of therapeutic programming and 2 hours of recreation' per the NYSBA source. Verify against NY Correction Law § 137 text before publishing.


### 2026-05-28-nursing-home-staffing-donations

- **[unsupported]** CBO estimated the provision's cost to operators at approximately $23 billion; that figure represents the staffing investment the industry would have been required to make.
  - issue: CBO scores federal budget impact (savings to Medicare/Medicaid), not industry compliance costs. Framing $23B as 'cost to operators' inverts CBO's scoring logic. The figure may be real but the attribution to CBO as measuring 'operator costs' is almost certainly wrong — the CMS Regulatory Impact Analysis, not CBO, estimates industry compliance costs. CBO.gov is blocked so the $23B cannot be verified at all, and no source URL is cited in the entry for this figure.
  - evidence: CBO.gov blocked by Cloudflare captcha — figure unverifiable. CBO's standard output is federal-budget impact, not industry cost. The entry's own source note ('CBO estimated the provision's cost to operators') conflates federal budget scoring with regulatory compliance costing. The graphic script (social-media/create_nursing_home_donations_card.py) uses the same framing: 'CBO: ~$23B cost to operators that won't be required' — the framing propagated from the entry.
  - fix: Identify the actual CBO OBBBA cost estimate for Section 71111 (likely expressed as federal Medicaid/Medicare savings from not having to reimburse better-staffed facilities). If the $23B is from the CMS Regulatory Impact Analysis or an AHCA analysis of industry costs, attribute it to the correct source. Add a source URL. If the figure cannot be sourced to CBO, remove the CBO attribution.


---

## RECOMMENDED


### 2024-08-va-healthcare-shortfall

- **[factual-error]** VA reported projected $15 billion shortfall for FY2025
  - issue: The cited Roll Call source (July 26, 2024) reports the $15B figure as a combined shortfall split across two fiscal years: $2.9B for the remainder of FY2024 and $12B for FY2025. Attributing the entire $15B to FY2025 alone misrepresents the source.
  - evidence: Roll Call (cited source): 'Nearly $15 billion combined shortfall — $2.9 billion for the remainder of fiscal year 2024 [and] $12 billion for fiscal year 2025.' The FY scope in the entry collapses two fiscal years into one.
  - fix: Change to: 'VA reported a combined projected shortfall of approximately $15 billion — $2.9 billion for the remainder of FY2024 and $12 billion for FY2025.'

- **[unsupported]** Congress passed emergency $12 billion supplemental funding (September 2024)
  - issue: The $12B figure in the cited Roll Call source is the FY2025 appropriations gap, not an emergency supplemental. The actual emergency supplemental passed by Congress in September 2024 addressed the $2.9B FY2024 shortfall. The cited source (July 2024) predates any congressional action and does not confirm a $12B supplemental was passed.
  - evidence: Roll Call (July 26, 2024): describes the $12B as the FY2025 appropriations gap; no supplemental had been passed as of the article date. The VA emergency supplemental enacted in September 2024 was approximately $2.9B for FY2024, not $12B. The $12B supplemental claim is unverified by the cited source.
  - fix: Correct to reflect what actually passed: 'Congress passed an emergency $2.9 billion supplemental for VA's FY2024 shortfall (September 2024). The FY2025 gap of $12 billion remained subject to the regular appropriations process.' Add a source other than the July 2024 Roll Call article to verify what Congress actually enacted.


### 2025-05-medicaid-coverage-cuts

- **[unsupported]** 1.4 million low-income Medicare beneficiaries (over 10% of enrolled population) will lose MSP coverage, increasing out-of-pocket costs by at least $185/month
  - issue: The $185/month figure and the '10% of enrolled population' framing have no cited source in the entry body or sources list. The CBO publication (cbo.gov/publication/61461) is cited for coverage loss numbers broadly, but the entry does not demonstrate that the CBO score contains the $185/month figure specifically. No source is provided for this dollar figure.
  - evidence: Sources section lists CBO for coverage estimates generally; no source is cited for $185/month or the 'over 10%' MSP enrollment fraction. CBO publication 61461 returned 403 and could not be verified. This specific dollar figure likely comes from a separate analysis (possibly KFF or CBPP on MSP impact) that is not cited.
  - fix: Add a specific citation for the $185/month out-of-pocket cost increase figure and cite the total MSP enrollment figure used to derive the '10%' claim.

- **[unsupported]** Hospital Medicaid dependency and operating margin figures (Cuba Memorial 42%, Arnot-Ogden 42%, UPMC Chautauqua 37% / -17.4%, Westfield Memorial -59.1%) attributed to Fiscal Policy Institute
  - issue: The Fiscal Policy Institute source (fiscalpolicy.org) is cited for 'NY hospital Medicaid dependency data,' but a fetch of that page returned only aggregate state/district-level data — the specific per-hospital percentages and margins were in a table image that was not legibly rendered. These hospital-level figures cannot be confirmed as sourced from that document.
  - evidence: WebFetch of fiscalpolicy.org/new-york-hospitals-will-close-under-the-one-big-beautiful-bill-act returned: 'The report does not contain Medicaid dependency percentages or operating margins for Cuba Memorial Hospital, Arnot-Ogden, UPMC Chautauqua, or Westfield Memorial Hospital... only aggregate data at the state and congressional district levels.' The table referenced exists as an image. The same figures appear in a sibling entry (2025-10-rural-hospitals-pure-fiction.md) where they are also attributed to Fiscal Policy Institute.
  - fix: Add a secondary citation (e.g., a direct Fiscal Policy Institute table link or screenshot) that makes the per-hospital figures verifiable. Or note the table is in FPI's Figure 1/Table 1 at a specific page reference.


### 2025-07-18-epstein-files-transparency

- **[unsupported]** After blocking the binding amendment, Republicans drafted their own non-binding resolution requesting Epstein file release — Result: Resolution passed
  - issue: The July 18 YES vote was a Rules Committee vote to advance H.Res. 589 (9-4), not a full House floor passage. WRFA (the entry's own primary source) describes it as the Rules Committee approving the resolution 'to move forward.' The word 'passed' in the result line, without clarification that this was only a committee vote to advance the resolution, overstates what occurred. H.Res. 589 does not appear in any floor roll call at clerk.house.gov through December 2025.
  - evidence: WRFA article states: 'House Resolution 589 was approved to move forward by a vote of 9 to 4.' Clerk.house.gov floor roll calls for July 18, 2025 (rolls 203-212) show H.R. 4016 (DoD appropriations) and H.Res. 590, not H.Res. 589. No floor vote on H.Res. 589 appears anywhere in the 2025 record through roll 362 (Dec 18, 2025).
  - fix: Change 'Result: Resolution passed' to 'Result: Rules Committee voted 9-4 to advance H.Res. 589 for potential floor consideration' to accurately reflect that this was a committee action, not a House passage.

- **[unsupported]** Rep. Thomas Massie (R-KY), who voted for actual release, called the Republican resolution a 'stunt' that 'forces the release of NOTHING.'
  - issue: The parenthetical 'who voted for actual release' (i.e., that Massie voted YES on the Democratic amendment) is an inference not confirmed by the cited WRFA source. WRFA quotes only Massie's social media post criticizing the Republican resolution; it does not report how Massie voted on the Democratic amendment. This relationship is stated as fact without a cited source.
  - evidence: WRFA article only reports: 'Republican Representative Thomas Massie calling it a stunt and posting on social media.' No statement in the WRFA article or any other cited source confirms Massie voted for the Democratic amendment. The entry lists no source establishing Massie's vote on the Democratic amendment.
  - fix: Either add a source confirming Massie's vote on the Democratic amendment (e.g., a Rules Committee roll call record), or remove 'who voted for actual release' and replace with 'who publicly criticized the resolution as insufficient.'


### 2025-08-veterans-support

- **[missing-hedge]** 'The Bath VA Medical Center in Steuben County serves 33,000+ veterans across seven counties.' (Framed in 'Why This Matters for NY-23' section.)
  - issue: The seven-county count is accurate per the Bath VA catchment (Allegany, Chemung, Schuyler, Steuben, Yates in NY; Tioga and Potter in PA), but three of those seven counties are not in NY-23: Yates County NY (verify_fact.py returns NOT IN NY-23), Tioga County PA, and Potter County PA. Presenting this figure without qualification in a 'Why This Matters for NY-23' framing implies all seven counties are within the district. A prior entry (2026-q2 state-of-the-district) was explicitly corrected to say 'four NY-23 counties' after this misattribution risk was flagged.
  - evidence: verify_fact.py county yates -> NOT IN NY-23 (trap). Q2 state-of-district update note: 'Bath VA catchment verified via va.gov (Allegany/Chemung/Schuyler/Steuben/Yates NY + Tioga/Potter PA → four NY-23 counties; verify_fact.py county confirmed Yates NOT NY-23).' The audit entry does not include this qualifier.
  - fix: Add 'four in NY-23' parenthetical: 'serves 33,000+ veterans across seven counties (four in NY-23, plus Yates County NY and two Pennsylvania counties).'


### 2025-09-salt-tax-relief

- **[dead-source]** Tax Foundation analysis shows NY-23 households earning $75K-$200K pay $2,000-$5,000 more annually due to SALT cap
  - issue: The cited Tax Foundation URL (taxfoundation.org/research/all/federal/salt-deduction-cap-congress/) returns HTTP 404. The specific NY-23 district-level figures ($2,000-$5,000 range for $75K-$200K income bracket) cannot be confirmed from the cited source.
  - evidence: WebFetch of the cited Tax Foundation URL returned HTTP 404 Not Found.
  - fix: Locate and archive a working Tax Foundation (or IRS Statistics of Income) source that provides district-level SALT cap impact, or revise the figure range to what can be verified.


### 2025-10-government-shutdown-aca

- **[unsupported]** Langworthy 'did not sign discharge petition' on the December ACA vote and it 'failed by one vote'
  - issue: The Gray DC article confirms the family-of-four premium figure ($263 to $560) and the 113%/24 million figure, but does not mention Langworthy's name or his specific role. The claim that he personally did not sign the discharge petition and that it failed by exactly one vote is not verified by any cited source.
  - evidence: WebFetch of Gray DC article (localnewslive.com, Dec 17 2025): article does not mention Langworthy. The discharge petition vote count and Langworthy's participation are sourced to 'Gray DC News, WSKG' without a specific article link confirming those details.
  - fix: Link to a specific source (e.g., Clerk.house.gov discharge petition roster or contemporaneous news article) naming Langworthy's non-participation and the one-vote margin.


### 2025-10-rural-hospitals-pure-fiction

- **[internal-contradiction]** Frontmatter verdict: MISLEADING; body verdict: MOSTLY FALSE
  - issue: The frontmatter field `verdict: MISLEADING` conflicts with the body assessment which declares `Verdict: MOSTLY FALSE`. Two different verdicts are published for the same entry.
  - evidence: Line 10: `verdict: "MISLEADING"`. Line 169: `**Verdict: MOSTLY FALSE**`.
  - fix: Align both to a single verdict. The body argument (that the 'pure fiction' claim is contradicted by independent data) supports MISLEADING or MOSTLY FALSE — pick one and apply it to both the frontmatter and the body text.


### 2025-11-aca-subsidies-false-claim

- **[unsupported]** Single person in Chautauqua County earning $65,000: premiums increase $104.30/month ($1,252/year); Family of four earning $130,000: premiums increase $212.26/month ($2,547/year) — per Sen. Gillibrand's office
  - issue: The body attributes these specific county-level figures to 'Sen. Gillibrand's office,' but the Sources section contains no citation to Gillibrand's office at all. These figures appear as floating assertions without a verifiable citation path.
  - evidence: Checked all five sources listed in the entry. None link to a Gillibrand press release, report, or data sheet. The KFF articles do not contain county-specific figures.
  - fix: Add a direct citation to the Gillibrand press release or data sheet from which these figures were drawn. If unavailable, note they are derived estimates and link to the methodology (e.g., KFF calculator inputs used).


### 2025-11-rural-hospitals-medicaid

- **[unsupported]** 25 rural hospitals in New York State (51%) are at risk of closure; 16 hospitals could close within 2-3 years
  - issue: The entry attributes these figures to 'healthcare analysts' without naming the source. The Observer Today op-ed (which is cited) does contain these figures and attributes them to Becker's Hospital Review. KFF does not contain these figures. The vague attribution 'healthcare analysts' overstates the sourcing.
  - evidence: Observer Today fetch: 'Becker's Hospital Review data referenced … approximately 25 rural hospitals in New York State (51%) face closure risk, with 16 of them (33%) potentially closing within 2-3 years.' KFF article does not mention these figures.
  - fix: Replace 'According to healthcare analysts' with 'According to Becker's Hospital Review data (as cited in the Observer Today)' to accurately identify the source. Add a note that this is secondary-source attribution.


### 2025-12-energy-policy-oil-gas

- **[unsupported]** Direct quotes attributed to Langworthy — 'un-American assault on our freedom, on our pocketbooks, but most importantly on our safety' and the PFAS response quote — are sourced to WRFA-LP, WNY News Now, and WSKG
  - issue: The source URLs provided are bare domain homepages (e.g., https://wrfalp.com/, https://www.wnynewsnow.com/) with no article path, making it impossible to confirm the quotes appear in those sources or were said in the context described. No archive URLs are present for any source.
  - evidence: All four news source links in the Sources section point to root domains only. Site standards (CLAUDE.md) require archive.org URLs for all sources; none are present for any source in this entry.
  - fix: Link directly to the specific articles (with full paths), archive each via Wayback Machine, and add the archived_url frontmatter field. Verify the PFAS quote context — the entry attributes it to a press conference but the source is not linked to a specific item.


### 2025-12-farm-bill-victory

- **[unsupported]** Chautauqua County: 75% of grape crop destroyed / Estimated $220 million in losses (April 2024 frost)
  - issue: The sources listed for these figures are 'Observer Today,' 'Post-Journal,' and 'CCE Chautauqua County' — but no URLs are provided for any of these sources in the Sources section. These figures appear in the entry body without a hyperlink to the underlying report or article. The claims are unverifiable from the cited sources as written.
  - evidence: Lines 89-90 state '75% of grape crop destroyed' and '$220 million in losses' but the Sources section (lines 200-204) lists only outlet names without URLs for these local sources. No archive.org link is provided.
  - fix: Add direct URLs (and archive.org copies) for the Observer Today, Post-Journal, or CCE Chautauqua County sources that report the 75% and $220 million figures.

- **[unsupported]** H.R. 3550 (dairy pricing formula) and H.R. 3638 (maple syrup producer support) are Langworthy-sponsored bills included in the Farm Bill text
  - issue: These bill numbers are stated as fact with no source URL. The Sources section does not link to congress.gov pages for H.R. 3550 or H.R. 3638, unlike H.R. 8359 (GRAPE Act) which has a cited link. The bill numbers and their attribution to Langworthy cannot be confirmed from the entry's own cited sources.
  - evidence: Lines 58-59 list H.R. 3550 and H.R. 3638 with descriptions but no source URLs. The Sources section (lines 196-198) links only to the GRAPE Act (H.R. 8359) and its 119th Congress reintroduction, not to the dairy or maple syrup bills.
  - fix: Add congress.gov links for H.R. 3550 and H.R. 3638 confirming Langworthy sponsorship and inclusion in H.R. 8467 text.


### 2025-12-farm-workforce

- **[unsupported]** Per USDA Labor Department data, approximately 49% of U.S. farmworkers are undocumented
  - issue: The attribution 'USDA Labor Department data' is a hybrid of two separate agencies (USDA and DOL). The cited USDA NASS Farm Labor Survey does not track immigration or documentation status — it collects wages and hours only. The 49% undocumented figure originates from the DOL National Agricultural Workers Survey (NAWS), not USDA NASS. The cited source does not support the stated figure.
  - evidence: WebFetch of https://www.nass.usda.gov/Surveys/Guide_to_NASS_Surveys/Farm_Labor/ confirmed: 'does not provide statistics on the percentage of farmworkers who are undocumented or unauthorized.' The 49% figure is plausible from DOL NAWS historical surveys but is not attributable to the USDA NASS source cited.
  - fix: Change attribution to 'Per U.S. Department of Labor, National Agricultural Workers Survey (NAWS)' and remove the USDA NASS citation from the labor-status statistic. The NASS citation is appropriate only for wage/employment figures.


### 2025-12-infrastructure-credit

- **[unsupported]** USDA Rural Development staffing claims: 'eliminated 36% of USDA Rural Development staff in 2025' and 'Voted for budgets proposing 31.7% reduction in Rural Development staffing (FY26)'
  - issue: Neither figure has a cited primary source in the Sources section. They appear as stated facts in the case study narrative (lines 170-171) and in the 'Why This Matters' intro (line 20), but the Sources section lists only Langworthy press releases, federal program pages, local news, and the IIJA. No OMB document, USDA staffing report, or budget line is cited.
  - evidence: Sources section (lines 244-258) contains no reference to a staffing cut source. The 31.7% and 36% figures are repeated three times in the entry body without attribution.
  - fix: Add a source citation for both figures — e.g., the FY2026 Trump budget request table for USDA Rural Development (31.7%) and a DOGE/OMB announcement or news report confirming the 36% staff reduction figure.

- **[dead-source]** FingerLakes1.com article cited as: 'Finger Lakes Railway awarded $3.8 million federal grant for track upgrades' (June 11, 2025) at https://www.fingerlakes1.com/2025/06/11/finger-lakes-railway-federal-grant/
  - issue: The URL returns HTTP 404. The cited local news article that provides the key 'previously announced during the Biden administration' quote — central to the Case Study 2 argument — is a dead link and could not be verified.
  - evidence: WebFetch returned HTTP 404 Not Found for the cited URL. The quote 'Though the project was previously announced during the Biden administration, it had not been funded until now' is load-bearing to the entry's argument but sourced only to this dead URL.
  - fix: Archive the article via Wayback Machine and replace the source URL with the archived version. If the article has been removed, note '(article no longer available; archived at [URL])' and consider whether an alternate source can confirm the Biden-administration-origination claim.


### 2025-12-medicaid-immigration

- **[other]** source_url in frontmatter: https://www.congress.gov/bill/104th-congress/house-bill/3734 listed as the URL for 'Press Release, House Energy and Commerce Committee Reconciliation Bill'
  - issue: The frontmatter source_url and archived_url both point to PRWORA (H.R. 3734, 104th Congress, 1996 welfare reform law), not to Langworthy's press release or the reconciliation bill. PRWORA is correctly cited in the Sources section as federal law background, but it should not occupy the primary source_url field, which templates reserve for the statement source.
  - evidence: GovInfo API confirmed BILLS-104hr3734 = PRWORA P.L. 104-193 (Personal Responsibility and Work Opportunity Reconciliation Act of 1996). The source field says 'Press Release, House Energy and Commerce Committee Reconciliation Bill' — a different document entirely.
  - fix: Replace source_url with the Langworthy.house.gov press release URL (May 12, 2025) or the Wellsville Sun op-ed URL. Move the PRWORA URL to the Sources section only.

- **[unsupported]** 45% of NY rural hospitals at immediate risk of closure (CHQPR analysis) (line 86)
  - issue: The cited URL (chqpr.org/downloads/Rural_Hospitals_at_Risk_of_Closing.pdf) returns an image-based PDF that is not machine-readable. The figure cannot be confirmed from the cited source. CHQPR's homepage cites 30% nationally with no NY-specific figure visible. The 45%/23-hospital NY figure is corroborated by a sibling entry (2025-10-rural-hospitals-pure-fiction.md) which cites ruralhospitals.chqpr.org instead.
  - evidence: WebFetch of chqpr.org PDF returned binary image data with no readable text. CHQPR homepage shows 30% national figure only. Corpus entry 2025-10-rural-hospitals-pure-fiction.md uses same 45%/23-hospital NY figure with different source URL (ruralhospitals.chqpr.org).
  - fix: Update source URL to ruralhospitals.chqpr.org (the interactive CHQPR tool) to match the sibling entry that successfully resolves this figure.

- **[dead-source]** Medicaid covers approximately 25-30% of rural hospital revenue (line 87)
  - issue: Cited to KFF 'Medicaid's Role in Rural America' issue brief, but that URL (kff.org/medicaid/issue-brief/medicaids-role-in-rural-america/) returns HTTP 404. The specific 25-30% range cannot be verified from the cited source. The sister entry (2025-05-medicaid-coverage-cuts.md) cites individual NY-23 hospitals with 37-42% Medicaid dependency, which is higher than the 25-30% cited here.
  - evidence: WebFetch of https://www.kff.org/medicaid/issue-brief/medicaids-role-in-rural-america/ returned HTTP 404. Sibling entries cite 37-42% for specific NY-23 hospitals, which is inconsistent with the 25-30% general figure used here.
  - fix: Find an active URL for this KFF figure, or update to the current KFF page URL. Consider whether a more specific NY-23 hospital Medicaid dependency figure (37-42%) would be more accurate than the national 25-30% range.


### 2025-12-pharmacy-crisis-pbm-reform

- **[unsupported]** $911 billion from Medicaid and 6,300+ NY-23 residents (ACA subsidies) cited in the MAHA Caucus section without a source
  - issue: These two specific figures appear in the MAHA Caucus Contradiction bullet list; the only source cited for that section is the Langworthy MAHA press release. Neither figure is footnoted or sourced inline in this section, leaving them unsupported as written here (even though the $911B figure is sourced in other entries).
  - evidence: Lines 160–161 contain the figures; line 163 cites only the Langworthy press release for the entire section. No KFF, CBO, or KFF/RAND source is cited here.
  - fix: Add inline citations for both figures — e.g., 'KFF estimate' for $911B and the source used in 2026-01-24-ceo-hearing-premiums.md for the 6,300 ACA figure.


### 2025-12-rhetoric-vs-actions-overview

- **[unsupported]** OBBBA SNAP table row: "Administrative cost-sharing drops from 50% to 25% | ~$200M shifted to counties"
  - issue: The 50%-to-25% admin cost-share change is supported in sibling entries (2026-02-09-snap-rural-impact-summary.md). However, the ~$200M statewide figure has no cited source in this entry and does not appear in any source file in the corpus. The sibling SNAP summary cites only a Steuben County estimate of 'up to $5 million.' The $200M statewide figure is unverifiable from the entry's citations.
  - evidence: grep -rn '200M|200 million' across content returns only this entry and a Rural Health Transformation entry where $200M is an average RHTP award, not a SNAP admin figure. No source URL is provided.
  - fix: Cite the source for the $200M statewide estimate (CBPP, state budget office, or legislative analysis), or replace with the documented Steuben County figure of 'up to $5M' and note statewide estimates vary.

- **[unsupported]** "Analysis showed most Western New York hospitals would receive little or no funding" from the Rural Health Transformation Fund. Source listed as: "State health department analysis, local hospital eligibility reviews."
  - issue: No URL or specific source is cited. The vague attribution 'State health department analysis, local hospital eligibility reviews' is insufficient to verify. No document by this description appears in the corpus. The Fiscal Policy Institute article (cited elsewhere in the entry) focuses on hospital closures, not RHTP eligibility distributions.
  - evidence: WebFetch of the Fiscal Policy Institute article confirmed it does not address RHTP eligibility or Western New York hospital qualification rates. No other sourced entry in the corpus makes this specific claim about WNY RHTP eligibility.
  - fix: Cite a specific primary source (HHS eligibility criteria, HANYS analysis, or state DOH guidance) that documents WNY hospital exclusion from RHTP, or soften the claim to reflect that the fund's eligibility restrictions meant not all district hospitals qualified.


### 2025-12-snap-cuts

- **[factual-error]** H.R. 1 extends work requirements from ages 18-49 to ages 18-64.
  - issue: The current SNAP ABAWD (Able-Bodied Adults Without Dependents) work requirement upper bound is 54 (those 55+ are currently exempt), not 49. CBPP confirms '1.6 million adults aged 18 to 54' are currently subject to requirements, and that the expansion targets 'older adults aged 55 through 64.' Stating the current ceiling as 49 understates the existing scope of the requirement.
  - evidence: CBPP (citing CBO): 'Expanding SNAP's harsh, ineffective, and red tape-laden work requirement to more SNAP recipients, including older adults and parents with children 7 and older…CBO estimates…3.2 million adults in a typical month, including 1 million older adults aged 55 through 64.' CBPP text also lists 'adults aged 18 to 54' as the current subject population.
  - fix: Change 'extends work requirements from ages 18-49 to ages 18-64' to 'extends work requirements from ages 18-54 (current ABAWD rule) to ages 18-64, adding 1 million adults aged 55-64 who were previously exempt.'

- **[unsupported]** CBO projects 2.4 million people nationally will lose SNAP coverage in a typical month.
  - issue: CBPP's analysis of the same CBO score reports 3.2 million adults losing SNAP in a typical month from the work requirement expansion alone. The 2.4 million figure does not appear in the entry's cited CBPP or Urban Institute sources and cannot be verified from available primary documents (CBO returns HTTP 403). May be a stale pre-passage estimate or cover a different subset of provisions.
  - evidence: CBPP (citing CBO, House-passed bill): 'roughly 3.2 million adults in a typical month' cut off under work requirement expansion. The entry's 2.4M figure is attributed to CBO but is not confirmed by the cited sources; CBPP's CBO-sourced figure is higher.
  - fix: Replace '2.4 million' with '3.2 million' (the CBO figure as cited in CBPP's analysis of the final House-passed bill), or add a note that an earlier estimate was 2.4 million and cite its specific source/vintage.


### 2025-12-social-security-tax

- **[unsupported]** According to Social Security Administration data and tax policy analysis: Approximately 64% of Social Security beneficiaries already paid no federal income tax on their benefits before this law.
  - issue: The SSA source URL cited (ssa.gov/benefits/retirement/planner/taxes.html) returns HTTP 403 and cannot be verified. The 64% figure appears in the Newsweek article without source attribution. No directly verifiable primary source confirms this figure from the entry's cited URLs. The claim is asserted as SSA data but the SSA page is unreachable.
  - evidence: Newsweek states '64 percent of seniors already don't pay taxes on Social Security benefits' with no source cited. SSA URL returns 403. No other cited source contains this figure. The figure may be accurate but the primary citation cannot be confirmed.
  - fix: Add the specific SSA publication or CBO/Tax Policy Center report that contains the 64% figure, or attribute to Newsweek as the immediate source and note its origin is unattributed there.


### 2025-12-worker-safety-scaffold-law

- **[misattribution]** The Langworthy quote is sourced to the FingerLakes1 article listed as the primary source_url
  - issue: The attributed quote ('My hope is that this law, if enacted, will finally force Albany to reform this law, saving millions each year in construction costs...') does NOT appear in the FingerLakes1 article. The FL1 article quotes Langworthy only as: 'This bill is urgently needed to preempt this broken liability standard on federally funded projects and get New York building again.' The actual 'My hope' quote is from the official Langworthy.house.gov press release, which is separately listed as a source but is not the frontmatter source_url.
  - evidence: WebFetch of fingerlakes1.com/2025/05/21/scaffold-law-reform-infrastructure-bill/ returned only the 'urgently needed to preempt' quote from Langworthy. The 'My hope is that this law' quote was confirmed in the langworthy.house.gov press release via curl. The entry's frontmatter source_url points to FL1, not the press release.
  - fix: Update source_url to point to the official press release (langworthy.house.gov), or note that the quote is from the press release rather than the FL1 article. The quote itself is accurate.

- **[unsupported]** Mario Cilento and Gary LaBarbera quotes are attributed to named statements
  - issue: The Cilento quote ('We strongly oppose this bill...It would invalidate vital safety protections...It's beyond comprehension...') and LaBarbera quote are not verifiable from any fetchable source. The entry cites 'New York State AFL-CIO: Statement on Infrastructure Expansion Act' and 'Building and Construction Trades Council: Statement' — but neither URL is provided for these sources, and neither the FL1 article nor the Langworthy press release contains these quotes. The statements may exist but are unverifiable without URLs.
  - evidence: FingerLakes1 article and Langworthy press release (both fetched) contain no mention of Cilento or LaBarbera. Sources section lists the organizations but provides no URLs for the actual statements. AFL-CIO website homepage (nysaflcio.org, fetched) showed no relevant 2025 press releases.
  - fix: Add direct URLs to the AFL-CIO and Building Trades Council statements so readers can verify the Cilento and LaBarbera quotes. Without URLs these are effectively unverifiable.


### 2025-12-year-end-newsletter

- **[unsupported]** The source_url in frontmatter links to H.R. 3699 congress.gov, but the documented source is 'Weekly Update from Congressman Nick Langworthy, December 28, 2025'
  - issue: The frontmatter source_url points to congress.gov/bill/119th-congress/house-bill/3699/all-info (the bill page), not to the newsletter itself. The archived_url field is empty. The newsletter is the primary source being fact-checked and has no direct URL or archive link.
  - evidence: Frontmatter: source_url = 'https://www.congress.gov/bill/119th-congress/house-bill/3699/all-info'; archived_url = ''. Entry body: 'Forwarded to LangworthyWatch, December 29, 2025' — no public URL or archive for the newsletter.
  - fix: If the newsletter is an email without a public URL, note 'copy on file' in the sources section. The source_url should reference the newsletter or be left blank; using a bill URL as the source_url for a newsletter fact-check is misleading.


### 2026-01-14-ptc-pivot

- **[unsupported]** Premium increase figures: 'Single person in Chautauqua County earning $65,000: premiums increase $104.30/month ($1,252/year); Family of four earning $130,000: premiums increase $212.26/month ($2,547/year); Over 6,300 NY-23 residents enrolled in ACA marketplace'
  - issue: These three figures are sourced to 'Sen. Gillibrand's office and KFF' without a direct URL to the underlying Gillibrand press release or a KFF county-level dataset. KFF's main marketplace enrollment page provides only state-level totals (210,704 for all of NY). The primary source for the Chautauqua-specific dollar figures is not linkable or archived in the entry. If the Gillibrand press release is the primary source for the county-level premium estimates and the 6,300 enrollee figure, a working archived URL should be cited.
  - evidence: KFF state-indicator page returns only statewide NY enrollment. The Gillibrand press release URL (senate.gov) returned HTTP 404 when fetched. The entry lists no archived URL for the Gillibrand source.
  - fix: Add a working or archived URL for the Sen. Gillibrand press release that is the primary source for the Chautauqua County premium figures and the 6,300 NY-23 enrollee count. If the press release is no longer available, note the source as 'archived' and link to a Wayback Machine snapshot.


### 2026-01-21-hernandez-pardon

- **[unsupported]** The Trump administration was carrying out lethal strikes on suspected drug vessels in the Caribbean, killing at least 83 people
  - issue: This figure appears twice in the entry (body and 'In Plain Language' section) but has no corresponding source URL in the sources list. The listed sources cover the pardon, autopen report, Hernandez biography, and SDNY conviction — none link to reporting on Caribbean maritime strikes. This is an unsourced statistic presented as established fact.
  - evidence: Sources section lists AP News, NPR, PBS NewsHour, Reuters, TIME, InSight Crime, and DOJ — none reference Caribbean drug vessel strike reporting. No URL provided for the 83-killed figure.
  - fix: Add a direct source URL for the 83-killed claim (e.g., the specific Reuters or AP article reporting this figure) or hedge with 'according to [outlet]' with a linked citation.


### 2026-01-22-one-year-real-results

- **[factual-error]** January 2025 inflation ~2.7-2.8% (Biden handoff point); 'Total decline under Biden ~6.3 percentage points'
  - issue: BLS CPI January 2025 was 2.99% YoY (not 2.7-2.8%). The entry appears to use a PCE or earlier estimate. Using the correct 3.0% figure, the Biden-era decline from peak is ~6.1 pp (9.1 to 3.0), not ~6.3 pp as the table claims. Additionally, with 3.0% as the starting point and 2.70% as the Nov 2025 endpoint, Trump's first-year CPI change was approximately -0.3 pp — a slight decline, not 'essentially flat / 0.1 pp.' The directional argument (Biden drove the decline) remains fully valid; only the magnitude and 'flat' characterization are slightly off.
  - evidence: BLS CUSR0000SA0: Jan 2024 = 309.698, Jan 2025 = 318.961 → YoY = 2.99%. Nov 2024 = 316.528, Nov 2025 = 325.063 → YoY = 2.70%.
  - fix: Correct Jan 2025 CPI to ~3.0% in the analysis section and the summary table. Update Biden decline to ~6.1 pp. Update Trump year-1 change to ~-0.3 pp and revise 'essentially flat' to 'roughly flat (fell about 0.3 percentage points)' — which still supports the attribution argument without the small factual error.

- **[unsupported]** Tax cut GDP% comparison table: ERTA 2.89% of GDP, TCJA 0.90% of GDP, OBBBA ~1.2-1.5% of GDP
  - issue: No specific source is cited for these percentage-of-GDP figures in the sources section. Independent calculation (JCT-scored TCJA ~$1.46T over 2018-2027 / ~$240T cumulative GDP) yields ~0.60-0.71%, not 0.90%. The TCJA figure may be drawn from a source using a different scoring window or baseline, but that source is not identified. The ERTA 2.89% figure is consistent with some academic comparisons (e.g., Tax Policy Center historical analyses) but is also unsourced. Reuters and CRFB fetch attempts failed; these figures could not be independently confirmed against the cited sources.
  - evidence: JCT scored TCJA at ~$1.46T (2018-2027). CBO 10-year GDP projection for 2018-2027 was approximately $210-240T. $1,460B / $220T = ~0.66%. The entry's 0.90% figure implies a substantially lower GDP denominator (~$162T) not supported by standard CBO baselines.
  - fix: Add a specific citation (e.g., Tax Policy Center or CBO historical comparison) for the GDP-share figures, or add a hedge noting that the exact percentages depend on the scoring methodology and baseline used. Alternatively, soften 'TCJA: 0.90%' to '~0.7-0.9% (varies by methodology)' to reflect the range across credible sources.


### 2026-01-24-ceo-hearing-premiums

- **[misattribution]** Commonwealth Fund: 21.7% average [premium increase]
  - issue: The 21.7% benchmark premium increase figure originates from Urban Institute, not the Commonwealth Fund. The Commonwealth Fund cited the Urban Institute figure in a January 2026 blog post, but did not produce it independently. Attributing it to 'Commonwealth Fund' is a misattribution.
  - evidence: Search results confirm: Urban Institute published 'Understanding the Extraordinary Increase in ACA Premiums in 2026' with the 21.7% figure; Commonwealth Fund blog post 'Putting the Extraordinary ACA Premiums Increase in Perspective' (Jan 15, 2026) discusses the Urban Institute finding.
  - fix: Change 'Commonwealth Fund: 21.7% average' to 'Urban Institute: 21.7% average (benchmark silver plans)' and update the Sources section accordingly.

- **[unsupported]** 725,000 people with incomes 400-500% FPL lose subsidy eligibility entirely
  - issue: This specific figure cannot be confirmed from any primary source. KFF and other sources identify approximately 1.6 million total enrollees above 400% FPL who received enhanced credits, and note 400-500% FPL represented 3% of 2025 sign-ups, but the '725,000' number does not appear in KFF, Urban Institute, or other cited research. No source is cited for this figure in the entry.
  - evidence: KFF enrollment tracker: 400-500% FPL group = ~3% of 2025 sign-ups; KFF notes ~1.6M total above 400% FPL lost enhanced eligibility. The 725,000 subset figure for 400-500% FPL specifically appears in no searchable primary source.
  - fix: Either source this figure to a specific KFF or CBO document, or replace with the confirmed figure: approximately 1.6 million enrollees above 400% FPL lost subsidy eligibility.


### 2026-01-31-childcare-freeze

- **[missing-hedge]** The entry quotes Langworthy saying 'over $8.5 billion in federal taxpayer dollars were misused' in the Minnesota fraud, and lists the DOJ Feeding Our Future press release as a source for the prosecution.
  - issue: The entry's own cited DOJ URL slug reads 'guilty-250-million,' and Wikipedia confirms the federal charge figure is ~$250 million (with estimates up to $350 million). The $8.5 billion figure appears to be the House Oversight Committee's broader pandemic-fraud estimate across multiple Minnesota programs, not the Feeding Our Future prosecution specifically. The entry quotes Langworthy's $8.5 billion claim, lists both the DOJ URL and the Oversight Committee release as sources, but never flags that the figure is ~34x the DOJ prosecution amount or explains where the $8.5 billion comes from. A reader following the DOJ link will find $250 million, not $8.5 billion — the entry's analysis should note this discrepancy.
  - evidence: DOJ press release URL slug: 'federal-jury-finds-feeding-our-future-mastermind-and-co-defendant-guilty-250-million'. Wikipedia on Feeding Our Future: '$250 million is the figure most commonly cited in federal charges'; higher estimates up to ~$350 million; a disputed '$9 billion' figure exists but is described as contested. Neither source supports $8.5 billion as the established Feeding Our Future prosecution amount.
  - fix: Add a note in the Claim analysis section that Langworthy's '$8.5 billion' figure does not match the DOJ prosecution amount (~$250 million for Feeding Our Future). If the $8.5 billion comes from the House Oversight Committee's broader Minnesota pandemic-relief audit, that scope should be defined and distinguished from the Feeding Our Future criminal case.


### 2026-02-02-shutdown-defund-ice

- **[factual-error]** January 30, 2026: Shutdown begins (in the timeline table)
  - issue: Wikipedia's article on the 2026 United States federal government shutdowns places the first shutdown start as January 31, not January 30. The entry's timeline lists 'January 29: Democrats block DHS funding bill' and 'January 30: Shutdown begins', but the shutdown would begin after funding lapses at midnight — which would make it January 31.
  - evidence: Wikipedia (2026 United States federal government shutdowns): 'January 31 – February 3' for the first shutdown period.
  - fix: Change 'January 30' to 'January 31' in the shutdown start row of the timeline table.

- **[unsupported]** ICE already received $75 billion over four years through the Republican reconciliation bill passed in July 2025
  - issue: No cited source for this figure appears in the entry's sources list, and it could not be verified from the cited H.R. 1 bill status XML or any other available source. The $75 billion figure, if used to argue the appropriations dispute is not 'really' about defunding ICE, is a load-bearing claim that requires a primary source citation.
  - evidence: Entry cites 'Congress.gov: H.R. 1 (One Big Beautiful Bill Act)' but provides no section reference or CBO score confirming this figure. The govinfo BILLSTATUS XML for H.R. 1 (119th Congress) does not surface this dollar amount in its metadata.
  - fix: Add a direct citation to the CBO score or a specific section of H.R. 1 confirming the $75 billion figure, or replace with a verifiable figure from the CBO cost estimate for H.R. 1 immigration provisions.


### 2026-02-04-minneapolis-renee-good

- **[unsupported]** Renee Good 'had just dropped her son off at school' at the time of the shooting
  - issue: This detail appears multiple times in the entry (lines 37, 161) and is load-bearing context contradicting the "violent rioter" label. None of the entry's cited sources confirm it. FactCheck.org (the only source that loaded successfully) describes her as "driving an SUV that appeared to be partially blocking traffic on a residential street" with no mention of a school drop-off. MPR News describes her as "an observer" during the ICE operation. No source is cited for this specific biographical detail.
  - evidence: FactCheck.org source describes Good driving an SUV blocking traffic; MPR News calls her "an observer." Neither mentions dropping her son at school. No citation in the entry for this detail.
  - fix: Add a direct citation to a news source that establishes the school drop-off detail, or hedge with "reported to have" and cite the source. If no source supports it, remove the detail.


### 2026-02-07-campaign-finance-patterns

- **[missing-hedge]** 2024 table: three rows (Individual $889,804 + PAC $856,664 + Small donors ~$67,000) against a total of $1,931,076
  - issue: The three rows sum to $1,746,468, leaving $184,608 unaccounted. The FEC API shows the missing categories are: transfers from other authorized committees ($167,256), political party contributions ($8,147), and other receipts ($511 + $8,695 offsets). The table presents three rows without noting that they do not represent all receipt categories, creating a false impression that Individual + PAC + Small = 100% of receipts. The PAC percentage (44.4%) is correctly calculated against the full total, but the table's structure implies the rows are exhaustive.
  - evidence: FEC API 2024 cycle: transfers_from_other_authorized_committee=167255.98, political_party_committee_contributions=8147.00, other_receipts=510.75, offsets_to_operating_expenditures=8694.84. Individual+PAC total from table = 1,746,468 vs receipts = 1,931,076.
  - fix: Add a footnote to the 2024 table: 'Table shows primary receipt categories. Excludes $167,256 in transfers from other authorized committees and $8,658 in party/other receipts. Percentages are of total receipts.'


### 2026-02-07-steuben-flooding-mitigation

- **[unsupported]** $9.5 million in FEMA disaster recovery funding for Steuben County, attributed to a Langworthy press release dated August 25, 2025
  - issue: The entry's primary sourced dollar figure has no verifiable URL. The frontmatter source_url field is empty. The sources list cites only the root domain 'langworthy.house.gov' with no page path and no archive URL. The FEMA table combines obligations from two separate disasters (DR-4625-NY from 2021 and DR-4825-NY from 2024) spanning three years — it is unverifiable whether a single Langworthy press release actually announced all three items together at $9.5M, or whether the entry aggregated obligations from multiple sources and attributed them to one press release.
  - evidence: Frontmatter: source_url is empty string. Sources section: 'Langworthy press release: $9.5M FEMA disaster recovery for Steuben County (August 25, 2025)' links to 'https://langworthy.house.gov/' (root domain only, no path). No archive URL. fetch of langworthy.house.gov/press-releases returned 403.
  - fix: Add the specific press release URL (with path) and an archive.org snapshot. If the $9.5M figure was aggregated from FEMA's PA database rather than from a single press release, revise the attribution to reflect that — and note which individual items Langworthy actually announced.

- **[unsupported]** FEMA flood maps are 'meant to be reassessed every five years'
  - issue: This is presented as an established fact but FEMA's Risk MAP program is a rolling, continuous process with no binding 5-year statutory or regulatory reassessment mandate. The claim has no citation in the entry. Presenting an unsourced procedural norm as a fixed federal requirement overstates the case.
  - evidence: No source cited in the entry for the 'every five years' assertion. FEMA's Risk MAP program documentation does not establish a hard 5-year update cycle.
  - fix: Either cite the specific FEMA program guidance or policy document that establishes a reassessment target/cycle, or soften to 'FEMA's Risk MAP program aims to update maps on a rolling basis' without the 5-year figure.

- **[unsupported]** The Jasper-Troupsburg superintendent specifically thanked Sen. Schumer for the FEMA funds
  - issue: Specific attribution of a named person's statement with no citation URL. This is a load-bearing claim used to undercut Langworthy's credit-taking, but the sources section includes no article or document where this attribution appears.
  - evidence: Sources list does not include any article citing the Jasper-Troupsburg superintendent's statement. No URL or archive link provided for this attribution.
  - fix: Add a citation to the specific news article, press release, or school district statement where the superintendent's thanks to Schumer is documented.


### 2026-02-08-allegany-county-grants-accord

- **[internal-contradiction]** The Olean Times Herald reported Langworthy announcing '$2.5 million in combined grants for Allegany County'
  - issue: Internal inconsistency: the Head Start grant alone is listed at ~$2.6 million in this entry, which exceeds the $2.5M 'combined' figure attributed to the Olean Times Herald. Either the two news sources cover different sets of grants (not explained), or the $2.5M and $2.6M figures cannot both be accurate for the same set of announcements. The entry presents both without resolving the apparent contradiction.
  - evidence: Entry line 68: 'The Olean Times Herald reported Langworthy announcing $2.5 million in combined grants for Allegany County.' Entry line 33: '$2.6 million in federal grants for Head Start projects' — Head Start alone exceeds the reported combined total.
  - fix: Clarify that the Olean Times Herald's $2.5M figure covers a different set of grants (or a different fiscal year/announcement cycle) than the itemized grants in this entry, or verify/correct the figure.

- **[unsupported]** 'Allegany County has one of the highest poverty rates in New York State'
  - issue: No source is cited for this claim. It is stated as fact but is unsupported in the entry's sources section.
  - evidence: Lines 100 and 118 make this claim; the sources section (lines 136-146) contains no link or citation for Allegany County poverty rate data.
  - fix: Add a citation to U.S. Census Bureau ACS data or a New York State agency source confirming Allegany County's poverty rate ranking.

- **[unsupported]** ACCORD Corporation 'suspended services following a presidential executive order' (sourced to Allegany Hope)
  - issue: The 'Allegany Hope' source is listed without any URL, making it unverifiable. All other sources in the entry link to specific outlets. The ACCORD suspension is a significant factual claim — characterizing the specific executive order and mechanism — resting on a dead/unlinked source.
  - evidence: Line 142: '* Allegany Hope: "ACCORD suspends Allegany County services following Presidential executive order"' — no hyperlink provided, unlike every other source. Line 90 attributes the claim to 'Allegany Hope reporting.'
  - fix: Add the URL for the Allegany Hope article, or archive it via Wayback Machine. If a URL cannot be found, note the source as 'print/local outlet' and add a secondary verifiable source (e.g., ACCORD's own communications or a larger regional outlet).


### 2026-02-08-big-flats-ssa-doge

- **[unsupported]** DOGE — a caucus Langworthy co-founded
  - issue: The intro calls DOGE 'a caucus Langworthy co-founded'; the body uses the softer 'founding member.' These are different claims. 'Co-founded' implies Langworthy was among a core group of creators; 'founding member' is broader. The Buffalo News source is paywalled; langworthy.house.gov returned 403. Neither primary source was independently verified in this audit. The distinction matters for precision.
  - evidence: Intro: 'DOGE — a caucus Langworthy co-founded.' Body uses 'founding member' consistently. Buffalo News article (primary source for the founding-member claim) is behind a paywall and returned a redirect to a tollbit paywall; langworthy.house.gov press releases page returned HTTP 403. Claim unverifiable from primary sources in this audit.
  - fix: Standardize to 'founding member' throughout (the softer, more defensible formulation) and ensure the Buffalo News article is archived with a wayback URL so the claim is traceable.

- **[unsupported]** Langworthy: 'I fully support Musk's mission and I look forward to helping him achieve his goals' (Buffalo News, February 2025)
  - issue: This direct quote is the load-bearing evidence for the CONTRADICTION verdict. The cited source (Buffalo News) is paywalled and could not be independently verified in this audit. No archive URL is provided in the entry's frontmatter (archived_url is empty) or sources section.
  - evidence: source_url and archived_url frontmatter fields are both empty strings. WebFetch of the Buffalo News URL returned a 302 redirect to a tollbit paywall. No Wayback Machine link is present.
  - fix: Add a web.archive.org URL for the Buffalo News article so the quote is traceable. If an archive does not exist, note 'quote reported by Buffalo News; paywall; no archive available' and consider citing a secondary source that quotes the same statement.


### 2026-02-08-steuben-credit-claiming-pattern

- **[stale]** CBO estimates: ~$186.7 billion in SNAP reductions over ten years (citing CBO pub 61387, May 2025)
  - issue: The entry cites CBO pub 61387 for the SNAP figure. The authoritative SNAP cuts entry (2025-12-snap-cuts.md) cites CBO pub 61461 (the enacted-bill score) and reports $295 billion in SNAP spending reductions over 2026-2034. Publication 61387 appears to be either the pre-enactment House-passed score or the Distributional Effects report, not the Budgetary Effects of the enacted bill. The $186.7B figure is likely from a superseded or different-scope CBO document. The two figures ($186.7B vs $295B) are not reconciled anywhere in the entry.
  - evidence: content/fact-checks/2025-12-snap-cuts.md (source_url: cbo.gov/publication/61461) reports $295 billion; content/fact-checks/2026-04-17-obbba-working-families.md (citing 61387) says 'approximately $186 billion' — the same publication difference appears across the tracker
  - fix: Replace the CBO SNAP figure with $295 billion sourced to CBO pub 61461 (the enacted-bill Budgetary Effects score), consistent with the SNAP cuts and SNAP rural impact entries. If $186.7B is from a distinct CBO table (e.g., only outlays for SNAP benefits, excluding admin), add a note clarifying scope.

- **[stale]** CBO estimates: ~$1.06 trillion in Medicaid spending reductions over ten years (citing CBO pub 61387, May 2025)
  - issue: The entry cites pub 61387 for the Medicaid figure of $1.06 trillion. The rural-hospitals entry (2025-10-rural-hospitals-pure-fiction.md), which cites the enacted-bill score pub 61461, reports $1.02 trillion for Medicaid/CHIP cuts. The $40 billion gap may reflect Senate amendments between the House-passed score and the enacted bill. Using the pre-enactment score for a bill that has already been enacted and scored is a stale-source issue.
  - evidence: content/fact-checks/2025-10-rural-hospitals-pure-fiction.md line 112: '| Medicaid/CHIP cuts | $1.02 trillion |' citing CBO pub 61461; audited entry line 195 cites pub 61387 for '$1.06 trillion'
  - fix: Update the Medicaid figure to $1.02 trillion and the source citation from pub 61387 to pub 61461 (cbo.gov/publication/61461), consistent with the rural-hospitals and medicaid-coverage-cuts entries.


### 2026-02-08-steuben-ice-cooperation

- **[missing-hedge]** Broader Pattern table: 'Votes for OBBBA (SNAP/Medicaid cuts) | Steuben County warns of $5M loss'
  - issue: The $5M figure, sourced in the sibling entry (2026-02-08-steuben-credit-claiming-pattern.md, attributed to WSKG reporting), refers specifically to a loss of SNAP administration funds, not a general OBBBA SNAP/Medicaid cut impact total. The table's compressed framing implies the $5M is the county-level impact of the OBBBA SNAP/Medicaid cuts broadly, which overstates what the figure actually measures.
  - evidence: Sibling entry line 151: 'WSKG reported Steuben County expects a loss of up to $5 million in SNAP administration funds between 2026 and 2027.' The ICE cooperation entry table does not qualify that this is SNAP admin funding, not a direct benefit-cut figure.
  - fix: Qualify the table cell to read 'Steuben County warns of up to $5M loss in SNAP administration funds' or add a footnote clarifying the $5M is SNAP admin funding per WSKG reporting.


### 2026-02-08-steuben-rural-impact-summary

- **[unsupported]** Sources section cites only homepage URLs for WSKG (https://wskg.org/) and VA OIG (https://www.va.gov/oig/) rather than specific articles or reports
  - issue: The load-bearing claims — $5M SNAP administration loss, county manager Jack Wheeler quote, VA OIG 50% staffing shortage figure — are attributed to WSKG and VA OIG but the source entries link only to homepages, not specific pages. Both URLs returned 404 when fetched directly at guessed article paths, and the homepage did not surface the relevant articles. The specific WSKG article and VA OIG report number are not cited, making the claims unverifiable by readers.
  - evidence: Source block lines 99 and 101 of the entry: "WSKG: [SNAP administration funding impact](https://wskg.org/)" and "VA OIG: [FY2025 staffing shortage report](https://www.va.gov/oig/)". Both are homepage-only citations. WebFetch of wskg.org returned homepage content with no matching article. VA OIG URL 404'd.
  - fix: Replace homepage citations with specific article URLs and archive them via Wayback Machine. The VA OIG report number (cited in sibling entries as the FY2025 occupational staffing shortages report) should be identified and linked directly.


### 2026-02-09-medicaid-rural-impact-summary

- **[misattribution]** Governor Hochul's office projects 1.5 million New Yorkers will lose Medicaid coverage
  - issue: The Governor's office projection is for 1.5 million New Yorkers losing health care coverage broadly, not Medicaid specifically. The entry attributes the 1.5M figure exclusively to Medicaid loss. The Governor's page groups Medicaid and other coverage (e.g., Essential Plan) together without separating the Medicaid component.
  - evidence: Governor's office page (fetched): '1.5 Million New Yorkers Will Lose Health Care Coverage' — page does not specify how many lose Medicaid vs. other coverage types.
  - fix: Change 'Governor Hochul's office projects 1.5 million New Yorkers will lose Medicaid coverage' to 'Governor Hochul's office projects 1.5 million New Yorkers will lose health coverage' (removing the word 'Medicaid').


### 2026-02-09-snap-rural-impact-summary

- **[factual-error]** The CBO projects this will reduce SNAP spending by $295 billion over 10 years
  - issue: The CBO scoring window for H.R. 1 is FY2026–2034 — 9 years, not 10. CBPP confirms 'through 2034.' The parent fact-check (2025-12-snap-cuts.md) correctly states '2026–2034.' Saying '10 years' overstates the window.
  - evidence: CBPP (https://www.cbpp.org/research/food-assistance/house-reconciliation-bill-proposes-deepest-snap-cut-in-history-would-take): 'cut nearly $300 billion from SNAP through 2034'; parent entry says 'over 2026–2034.' Summary entry says 'over 10 years.'
  - fix: Change 'over 10 years' to 'over 2026–2034' (or 'over nine years') in Section 1 and the Verdict paragraph.

- **[unsupported]** The Urban Institute estimates 5.4 million people could lose benefits monthly
  - issue: The source URL provided is the Urban Institute homepage (https://www.urban.org/) — not a specific publication. This is a specific numeric claim sourced to a homepage rather than a primary document. The URL in the parent entry (https://www.urban.org/research/publication/expanded-snap-work-requirements-would-reduce-benefits-millions-families) returned HTTP 404, making the primary source unverifiable.
  - evidence: Entry sources section lists 'Urban Institute: [SNAP Work Requirements Analysis](https://www.urban.org/) (2025)' — this links only to the homepage. WebFetch of the specific URL from the parent entry returned 404. The 5.4 million figure cannot be confirmed against a retrievable primary source.
  - fix: Replace the homepage URL with the specific Urban Institute publication URL. If that URL is dead, archive it via Wayback Machine or replace with CBPP or CBO work-requirement analysis that can be verified.

- **[misattribution]** Source URL in frontmatter points to CBO publication 61387
  - issue: The frontmatter source_url is https://www.cbo.gov/publication/61387, which the parent fact-check identifies as the 'Distributional Effects of H.R. 1' report — not the main budget score. The $295 billion SNAP figure comes from the CBO budget score at publication 61461 (or the committee-stage version 61420). The summary entry's primary source URL is the wrong CBO document for the headline claim.
  - evidence: Parent entry (2025-12-snap-cuts.md) frontmatter source_url is https://www.cbo.gov/publication/61461 and sources section lists /61387 separately as 'Distributional Effects.' The summary entry uses /61387 as its sole frontmatter source_url but cites /61387 in its sources section correctly as the distributional effects doc while claiming it is the budget-score source.
  - fix: Change frontmatter source_url to https://www.cbo.gov/publication/61461 (the SNAP budget score). Update archived_url to match.


### 2026-02-09-va-rural-impact-summary

- **[factual-error]** counties: [steuben, allegany, chemung, schuyler, yates, erie] (frontmatter tag)
  - issue: Yates County is NOT in NY-23. The county verification script confirms 'yates -> NOT IN NY-23'. CLAUDE.md explicitly warns that a VA catchment area including an NY-23 county is NOT the same as NY-23 counties. Bath VA's catchment includes Yates (NY) but this is a healthcare service boundary, not a congressional district boundary. Tagging the entry with Yates as a county served implies Langworthy's constituents are affected in that county.
  - evidence: Script output: 'yates -> NOT IN NY-23  <-- trap'. CLAUDE.md: 'A VA catchment or BOCES that includes an NY-23 county is NOT all NY-23 counties.' The parent entry's Bath VA coverage table (line 137) correctly notes Yates as part of the facility's geographic service area without claiming it is an NY-23 county.
  - fix: Remove 'yates' from the counties frontmatter tag. The body text referencing Bath's 'seven counties' service area (which includes Yates and PA counties) is acceptable geographic context, but the county tag should only list NY-23 counties: steuben, allegany, chemung, schuyler, erie (partial).


### 2026-02-10-save-act-voter-id

- **[misattribution]** Cato Institute finding described as rate is 'infinitesimally small'
  - issue: The cited Cato article (https://www.cato.org/blog/noncitizens-dont-illegally-vote-detectable-numbers) does not use the phrase 'infinitesimally small.' The actual language is 'no good evidence' of noncitizens voting in large numbers and 'not in detectable numbers' (from the headline). The entry puts a phrase in the Cato source that does not appear there.
  - evidence: WebFetch of the cited Cato URL returned: 'The article does not use the term "infinitesimally small." Instead, it characterizes noncitizen voting through these specific phrases: "no good evidence", "not in detectable numbers"'
  - fix: Replace 'Rate is "infinitesimally small"' in the table with language the source actually uses, e.g., 'No evidence of voting "in detectable numbers"' — or quote the headline directly.

- **[misattribution]** 83% of Americans support requiring proof of citizenship to vote (intro and Claim 2 verdict)
  - issue: The cited Pew Research study (August 2025) measures support for 'requiring all voters to show government-issued photo identification to vote' — not documentary proof of citizenship. The SAVE Act requires birth certificates, passports, or naturalization certificates, which is a materially higher bar than a photo ID. The entry conflates the two in the intro ('roughly 83% of Americans support requiring identification to vote') and in Claim 2 ('find that roughly 80-85% of Americans support requiring some form of identification or proof of citizenship to vote'). The 83% figure is real but applies to photo ID, not proof-of-citizenship documents.
  - evidence: WebFetch of the Pew URL confirmed: '83% specifically measures support for "requiring all voters to show government-issued photo identification to vote." The survey does not appear to ask separately about "proof of citizenship."'
  - fix: Clarify that the 83% figure applies to photo ID requirements, not proof-of-citizenship documentary requirements specifically. Add a note that polling on the SAVE Act's specific documentary requirement (as opposed to photo ID) has not been conducted or shows different results.


### 2026-02-10-tioga-county-federal-impact

- **[misattribution]** Rep. Nick Langworthy voted for the OBBBA on May 22, 2025, calling it 'a generational win for the American people.'
  - issue: The 'generational win' quote is misattributed to the May 22 vote (RC145). All other sourced site entries place this language in Langworthy's July 8, 2025 Olean Times Herald op-ed, published after the final House passage vote on July 3, 2025 (RC190, 218-214). The two votes are distinct: RC145 was original House passage; RC190 was concurrence in Senate amendment (final enactment). The Tioga entry collapses them and pins the quote to the wrong date.
  - evidence: RC145 confirmed May 22 2025 via clerk.house.gov/evs/2025/roll145.xml. RC190 confirmed July 3 2025 via clerk.house.gov/evs/2025/roll190.xml. The 'generational win' quote is attributed to a July 8 Olean Times Herald op-ed in 2026-06-02-rural-health-transformation-212m.md, 2026-05-29-corning-manufacturing-credits-obbba.md, 2026-05-28-nursing-home-staffing-donations.md, and 2026-05-18-aapd-medicaid-disability-contradiction.md — all of which cite RC190 and the post-July 3 statement. No sourced site entry links 'generational win' to the May 22 vote.
  - fix: Either separate the two votes (noting Langworthy voted Aye on both RC145/May 22 and RC190/July 3) or move the 'generational win' quote to the July 3 final passage context, matching the sourced entries.

- **[internal-contradiction]** ...a claim [rated misleading](/fact-checks/2025-05-medicaid-coverage-cuts/) based on CBO projections of 1.3 million dually eligible individuals losing Medicaid nationally.
  - issue: The linked fact-check (2025-05-medicaid-coverage-cuts.md) carries verdict 'FALSE', not 'misleading'. The Tioga entry characterizes the linked entry's verdict as 'misleading' which understates the finding.
  - evidence: grep 'verdict:' 2025-05-medicaid-coverage-cuts.md returns: verdict: "FALSE"
  - fix: Change 'rated misleading' to 'rated FALSE' to match the actual verdict of the linked fact-check.


### 2026-02-11-fy2026-appropriations-credit

- **[factual-error]** H.R. 6938 Senate vote: 'Senate 80-13' (in the Two Bills table)
  - issue: The Senate passed H.R. 6938 80-13 is incorrect. Senate Roll Call Vote 11 (119th Congress, 2nd Session, January 15, 2026) shows the actual vote was Yeas 82 – Nays 15 – Not Voting 3. The entry's figures are off by 2 on both sides.
  - evidence: Senate.gov Roll Call Vote 119-2-11: https://www.senate.gov/legislative/LIS/roll_call_lists/roll_call_vote_cfm.cfm?congress=119&session=2&vote=00011 — Yeas 82, Nays 15, Not Voting 3, on H.R. 6938 'consolidated appropriations for fiscal year ending September 30, 2026,' passed January 15, 2026.
  - fix: Change 'Senate 80-13' to 'Senate 82-15' in the Two Bills table row for H.R. 6938 / P.L. 119-74.


### 2026-02-20-energy-costs-dunkirk

- **[factual-error]** His lifetime League of Conservation Voters score is 3%
  - issue: LCV website (lcv.org/congressional-scorecard/moc/nick-langworthy) shows his lifetime score as 2%, not 3%. Annual scores: 2025=0%, 2024=0%, 2023=6%. The 2024 score of 0% stated elsewhere in the same sentence is correct.
  - evidence: Fetched lcv.org scorecard page directly: 'Lifetime Score: 2%'. Annual breakdown: 2025 0%, 2024 0%, 2023 6%. Score may have been 3% at an earlier snapshot but current published value is 2%.
  - fix: Change '3%' to '2%' to match the current LCV published lifetime score.


### 2026-02-20-scotus-tariff-ruling

- **[unsupported]** The New York Fed's February 12, 2026 analysis found a 94% pass-through rate, meaning a 10% tariff resulted in foreign exporters cutting prices by just 0.6%
  - issue: The NY Fed URL (newyorkfed.org/regional-economy) returned HTTP 403; the specific February 12, 2026 analysis and the 94% pass-through / 0.6% price-cut figures could not be verified from the cited source. The math also appears internally inconsistent: a 94% pass-through rate means 94% of a tariff is passed to consumers, which would imply foreign exporters absorb only ~6% — not that they cut prices by 0.6% on a 10% tariff (which would be a 6% absorption rate expressed as 0.6 percentage points, not 0.6%). The framing conflates pass-through rate with exporter price response.
  - evidence: NY Fed URL returned 403 Forbidden; figure unverifiable from cited source. The internal description of what '94% pass-through' means (foreign exporters cutting prices by 0.6%) is also inconsistent with standard pass-through definitions.
  - fix: Link directly to the specific NY Fed paper or Liberty Street Economics post with the February 12, 2026 date, and clarify the pass-through definition (high pass-through = most cost falls on domestic consumers, not exporters).

- **[unsupported]** U.S. goods trade deficit hit an all-time record of $1.24 trillion in 2025, up 2.1% from 2024 ... goods-and-services deficit of $901.5 billion ... 78% larger than the pre-tariff 2016 baseline of $504.8 billion
  - issue: The cited BEA URL (bea.gov/data/intl-trade-investment/international-trade-goods-and-services) only displayed April 2026 monthly data when fetched; it did not contain 2025 annual totals, 2024 annual totals, or a 2016 baseline figure. These figures and the derived '78% larger' comparison cannot be verified from the cited source as it stands.
  - evidence: BEA page fetch returned only April 2026 monthly data ($55.9B deficit for that month). Annual 2025 goods deficit, goods-and-services deficit, 2024 comparator, and 2016 baseline of $504.8B are not present on the linked page.
  - fix: Link to the specific BEA trade news release (e.g., the February 2026 annual release) rather than the general data landing page, so figures can be directly verified.


### 2026-02-25-largest-tax-cut-claim

- **[factual-error]** American Taxpayer Relief Act (2012) reduced revenue by ~1.6% of GDP
  - issue: The Tax Foundation article (the cited primary source) reports the 2012 American Taxpayer Relief Act at -1.78% of GDP, which rounds to ~1.8%, not ~1.6%. The entry rounds it down to match the 1964 figure, understating the 2012 cut.
  - evidence: Tax Foundation (https://taxfoundation.org/blog/obbba-largest-tax-cut-in-american-history/) gives these figures: 1981 = -2.89%, 1945 = -2.67%, 1948 = -1.87%, 2012 = -1.78%, 1964 = -1.60%, OBBBA = -1.40%. Entry shows 2012 as '~1.6%', same as 1964.
  - fix: Change 2012 figure in the table from '~1.6%' to '~1.8%'. Also correct the row order: the Tax Foundation ranks 2012 (1.78%) above 1964 (1.60%), but the entry lists 1964 before 2012, implying 1964 was the larger cut.

- **[unsupported]** Over 70% of net tax cuts go to the richest fifth of Americans (ITEP)
  - issue: The cited ITEP article (https://itep.org/trump-obbba-taxes-lower-for-the-rich-tariffs/) does not appear to contain a '70%' figure for the richest fifth. The ITEP article focuses on the top 1% receiving $1 trillion and on the top 5% threshold for the tariff-offset finding. The 70% figure is unverifiable from the cited source.
  - evidence: ITEP fetch summary: article mentions '$1 trillion tax cut for the richest 1%' and 'all but the richest Americans are paying higher taxes' — no mention of a 70% share for the top quintile. This figure may come from a different ITEP publication or from TPC/Yale Budget Lab.
  - fix: Either cite the specific ITEP document that contains the 70% figure (with direct URL), or attribute this figure to the source that actually publishes it (e.g., Tax Policy Center or Yale Budget Lab), or remove if it cannot be sourced.


### 2026-02-25-sotu-2026-claims

- **[factual-error]** U.S. citizens account for approximately 81% of all fentanyl smuggling arrests at the southwest border (FY2019-2024), per the Cato Institute
  - issue: The Cato Institute article cited states '80 percent' (6,123 of 7,569 individuals), not 81%. The Cato source link in the footnotes also says '80%'. The entry uses 81% in the body (line 166), the summary passage (line 195), and the Questions section (line 227).
  - evidence: Cato article fetched: 'US citizens comprised 80 percent of individuals caught with fentanyl during border crossings at ports of entry from 2019 to 2024.' Entry says 81%. The source URL anchor text in the entry's own Sources section also says '80%'.
  - fix: Change '81%' to '80%' in lines 166, 195, and 227 to match the cited Cato source.


### 2026-02-28-dhs-shutdown-epic-fury

- **[internal-contradiction]** CISA had only ~900 of ~2,200 working during the shutdown; CISA lost ~1,000 of ~3,400 employees to DOGE; CISA was at 38% of optimal staffing
  - issue: Internal inconsistency across three CISA figures drawn from different sources and timeframes. The table gives a post-DOGE baseline of ~2,200, but the paragraph implies ~3,400 minus ~1,000 = ~2,400 post-DOGE — a 200-person discrepancy. Additionally, '38% of optimal staffing' (sourced to TechCrunch) combined with a pre-DOGE total of ~3,400 yields ~1,292 working, not ~900. The only reading that reconciles the numbers is 38% of current (~2,400) = ~912 ≈ 900, but the phrase 'optimal staffing' most naturally refers to the pre-DOGE capacity. These are derived numbers combining two different snapshots from two different sources.
  - evidence: Table (line 69): '~900 of ~2,200 working.' Paragraph (line 116): '~1,000 of ~3,400 employees' lost to DOGE. TechCrunch source confirmed '38% staff levels' but did not provide the 900/2,200 breakdown. Federal News Network (cited for 1,000-of-3,400) returned HTTP 403 and could not be verified.
  - fix: Reconcile CISA workforce figures: pick a single consistent baseline (pre-DOGE vs. post-DOGE) and label it clearly. If the table's ~2,200 is post-DOGE current headcount, the paragraph should say 'from a pre-DOGE workforce of ~3,400' and not imply ~2,400 remains. The '38%' figure should specify what baseline it is a percentage of.

- **[unsupported]** Cyber defense training was cut by $45 million; the election security program was completely eliminated
  - issue: Neither figure appears in the TechCrunch article cited as the source for this paragraph. TechCrunch confirmed '38% staff levels' and general program cuts (counter-ransomware initiative, secure software development efforts) but did not mention the $45 million training cut or complete elimination of the election security program.
  - evidence: TechCrunch fetch (techcrunch.com/2026/02/25/us-cybersecurity-agency-cisa-reportedly-in-dire-shape-amid-trump-cuts-and-layoffs/) confirmed 38% figure and general program losses but did not contain the $45M figure or 'election security program completely eliminated.' No other source is cited for these specifics.
  - fix: Add a primary source for the $45 million training cut and election security program elimination, or add a hedge ('reportedly' / 'according to [source]') with the correct citation.


### 2026-02-28-epic-fury-statement

- **[unsupported]** U.S. intelligence assessments from 2025 concluded that Iran was not currently pursuing a nuclear weapon.
  - issue: No source URL is provided for this intelligence assessment claim. The sources section (lines 195–201) cites only homepages and index pages — none is a specific intelligence document or news article about the 2025 DNI threat assessment. This is a load-bearing fact in the 'MISLEADING' verdict for Claim 3 (the 'numerous chances to deescalate' analysis).
  - evidence: Lines 82–83: 'U.S. intelligence assessments from 2025 concluded that Iran was not currently pursuing a nuclear weapon.' No source URL in the Sources section links to the specific document.
  - fix: Cite the specific intelligence document — likely the 2025 Annual Threat Assessment of the U.S. Intelligence Community (DNI) — with its URL and an archive link.

- **[unsupported]** Oman's foreign minister described a deal as 'within reach.'
  - issue: No source is cited for this quote. The entry invokes Oman's foreign minister's characterization to support the 'MISLEADING' verdict on Claim 3 (active diplomacy at time of strikes), but the quote has no attributed source URL.
  - evidence: Lines 82: 'Oman's foreign minister described a deal as "within reach."' No source in the Sources section covers this claim.
  - fix: Add the specific news article or official statement where Oman's foreign minister made this characterization, with archive URL.

- **[unsupported]** Several briefed Democrats — including Senate Minority Leader Schumer and House Minority Leader Jeffries — subsequently called the strikes an 'illegal, regime-change war.'
  - issue: The quote is attributed to Schumer and Jeffries but no source URL is provided. This direct quote is a load-bearing fact for the Claim 5 analysis that the Gang of 8 briefing produced partisan division, not consensus.
  - evidence: Lines 112–113: 'Several briefed Democrats — including Senate Minority Leader Schumer and House Minority Leader Jeffries — subsequently called the strikes an "illegal, regime-change war."' No source URL in the Sources section.
  - fix: Add a direct citation (press release, news article, or official statement) for this quote from Schumer and/or Jeffries, with archive URL.


### 2026-02-state-preemption-pattern

- **[unsupported]** Meta reportedly spent $3.1 million on AI lobbying through the California Chamber of Commerce alone.
  - issue: The only source cited for the AI lobbying section is the Read Sludge article, which does not contain this figure. The article mentions Meta employing 63 lobbyists on AI and Meta spending $65M on super PACs, but not a $3.1M California Chamber figure. No separate source is cited for this specific claim.
  - evidence: Read Sludge article (cited) confirmed via WebFetch — Meta $3.1M/California Chamber of Commerce claim not present in that article. No alternative source cited in the entry.
  - fix: Locate and cite the primary source for the $3.1M California Chamber of Commerce figure, or remove the claim until sourced.

- **[dead-source]** The Harvard T.H. Chan School of Public Health PDF (cited) supports: from 2004-2015, nearly 1,000 people aged 25 and under experienced severe health conditions linked to dietary supplements, including 166 hospitalizations and 22 deaths.
  - issue: The cited Harvard PDF URL returns HTTP 404 and could not be retrieved. The figures (nearly 1,000, 166 hospitalizations, 22 deaths) are load-bearing health statistics that cannot be confirmed against the cited primary source.
  - evidence: WebFetch of https://content.sph.harvard.edu/wwwhsph/sites/1267/2021/02/Restricting-Sale-of-Weight-Loss-and-Muscle-Building-Supplements.pdf returned HTTP 404.
  - fix: Re-archive the PDF via Wayback Machine and update the URL to the archived version, or substitute a working URL to the same document (Harvard Chan SPH publication page or PubMed).


### 2026-02-telephone-town-hall

- **[factual-error]** Frontmatter counties list includes 'niagara' alongside the NY-23 counties.
  - issue: Niagara County is flagged as an EDGE case — a small NY-23 sliver — by the county verification script. The entry describes Rep. Langworthy's 'monthly telephone town hall broadcast to residents across NY-23's nine counties' but then lists nine counties that include Niagara, which is not a recognized NY-23 county (it is predominantly NY-26). The CLAUDE.md county list for NY-23 does not include Niagara.
  - evidence: verify_fact.py county niagara returns 'EDGE — small NY-23 sliver; VERIFY before asserting'. CLAUDE.md lists NY-23 counties as: Allegany, Cattaraugus, Chautauqua, Chemung, Erie, Schuyler, Steuben, Tioga. Niagara is not in that list.
  - fix: Remove 'niagara' from the counties frontmatter tag and from the body description ('nine counties'). The town hall would cover eight NY-23 counties, not nine.


### 2026-03-05-sexual-misconduct-vote

- **[unsupported]** approximately $17 million in settlements paid from the Congressional Office of Compliance fund — a figure cited by Rep. Thomas Massie (R-KY) based on House records
  - issue: The $17M figure and its attribution to Massie are unverifiable from the cited sources. Three cited sources (NBC News, The Hill, Roll Call) all returned HTTP 403 or did not mention the dollar figure or Massie attribution. No primary House record or CRS report is cited to anchor this figure.
  - evidence: Roll Call article fetched did not mention a dollar figure. NBC News and The Hill returned HTTP 403. No primary document (e.g., OOC annual report, Massie floor statement) is linked in the entry.
  - fix: Add a direct citation to Massie's floor statement or the Office of Compliance report that contains the $17M figure, or hedge with 'reportedly' and link to a source that explicitly carries the figure and attribution.

- **[unsupported]** His office also confirmed he voted in the House Oversight Committee to subpoena the Ethics Committee records
  - issue: This claim is sourced only to 'his office' with no public primary source (committee vote record, press release URL, or committee report) cited. Sourcing a factual claim solely to the subject's own office without a corroborating public record flags as inference-stated-as-fact.
  - evidence: No committee vote record, press release link, or independent report is cited to support this claim; it rests entirely on an undocumented 'office confirmed' statement.
  - fix: Link to Langworthy's press release or a House Oversight Committee record confirming the subpoena vote, or add 'according to his office' with an archived URL.


### 2026-03-07-mullin-dhs-appointment

- **[unsupported]** Sen. Richard Blumenthal (D-CT) and other Senate Democrats explicitly suggested that replacing the polarizing Kirstjen Nielsen-era figure with a new nominee could create conditions for renewed negotiations.
  - issue: The Blumenthal attribution is not supported by any cited source. The CBS News article (cited) mentions only Schumer (NO) and Fetterman (YES); the NPR source was unreachable. No source in the entry contains a Blumenthal statement about Mullin easing negotiations. Additionally, referring to Noem as a 'Kirstjen Nielsen-era figure' is odd framing — Nielsen left DHS in 2019, and Noem is not a Nielsen-era holdover; the phrasing appears to mean 'polarizing like Nielsen' but reads as misidentification.
  - evidence: Cited CBS News article (https://www.cbsnews.com/news/kristi-noem-out-as-secretary-of-homeland-security-markwayne-mullin/) mentions Schumer and Fetterman but not Blumenthal. No other cited source covers the Blumenthal statement. The NPR article (https://www.npr.org/2026/03/05/nx-s1-5737554/markwayne-mullin-homeland-security-kristi-noem-trump) timed out and could not be verified.
  - fix: Add a specific citation for the Blumenthal statement (news article or Senate press release quoting him). Separately, clarify the 'Nielsen-era figure' phrase — Noem is Trump's second-term DHS Secretary, not a Nielsen holdover; if the intent is to draw a parallel to Nielsen's polarizing reputation, state that explicitly.


### 2026-03-08-biden-immigration-10-million

- **[unsupported]** 'In Biden's first year, 70.7% of encounters resulted in expulsion, deportation, or detention.'
  - issue: No inline citation is provided for this specific statistic. FactCheck.org reports a 57% removal rate and 35% release rate on a cumulative basis (different time window), but no source in the entry's bibliography explicitly attributes the 70.7% figure to FY2021 specifically.
  - evidence: No footnote or parenthetical source link attached to the 70.7% figure. FactCheck.org (the closest cited source) uses different percentages for the full term.
  - fix: Add an inline citation to the CBP or DHS OHSS FY2021 enforcement statistics that support the 70.7% figure, or remove if unverifiable.

- **[unsupported]** 'Nearly 4.4 million total repatriations (expulsions + removals + voluntary returns) — more than any single presidential term since George W. Bush.'
  - issue: The figure is not directly verifiable from any cited source that was fetchable. The closest accessible source (FactCheck.org, through Oct 2023) cites 3.7M repatriations, not 4.4M. The MPI 'Biden deportation record' source returns HTTP 403. The 4.4M may be accurate for the full Biden term (Jan 2021–Jan 2025), but the current entry provides no direct citation to a primary source that can be checked.
  - evidence: MPI source URL returns 403; FactCheck.org shows 3.7M through Oct 2023 only. The entry's narrative text does not attach an inline citation to the 4.4M figure specifically.
  - fix: Cite a specific DHS or CBP enforcement statistics page that shows the full-term repatriation total, or add a hedging note that the figure covers the partial term through the FactCheck.org snapshot date.


### 2026-03-08-defense-suppliers-visit

- **[unsupported]** According to the Chautauqua County IDA, the Falconer facility employs over 600 people with a payroll exceeding $75 million.
  - issue: Specific figures (600+ employees, $75M payroll) are attributed to the Chautauqua County IDA, but the entry's source_url is blank, the sources section links only to the generic chautauquacounty.com domain (no specific case study or page), and the IDA page returns 404. These numbers appear sourced to a general domain rather than a cited primary document. Cannot confirm the figures appear in any linked or archived source.
  - evidence: source_url field is empty; sources section cites chautauquacounty.com with no path; IDA page at chautauquacountyny.gov/departments/planning_and_economic_development/ida/ returns 404.
  - fix: Add a specific URL and archived URL to the Chautauqua County IDA case study or press release that states the 600+ / $75M figures. If no primary source can be found, replace with a hedged estimate and a verifiable source (e.g., company press release, local news report).

- **[unsupported]** The actual combined WNY employment across these three companies likely exceeds 3,000–4,000 workers — three to four times the 'over 1,000' figure cited.
  - issue: This derived estimate is presented as a likely fact but is computed from vague characterizations in the entry itself ('several thousand,' 'several hundred+') without citing any primary source. The range 3,000–4,000 is an editorial calculation with no cited basis, which creates a false impression of precision. The entry also does not define the geographic or role scope for Moog ('several thousand in the Buffalo-Niagara region' vs. NY-23 only).
  - evidence: The table lists Moog as 'Several thousand' and Astronics as 'Several hundred+' — both without sources. The 3,000-4,000 figure is a sum of these uncited characterizations.
  - fix: Either cite primary sources (annual reports, state labor data, local news) for each company's WNY headcount, or soften the language to 'substantially more than 1,000' without specifying a range. Clarify geographic scope (NY-23 vs. broader Buffalo-Niagara region).


### 2026-03-09-dhs-security-incidents

- **[unsupported]** The FBI's Joint Terrorism Task Force joined the investigation based on indicators found on the suspect and in his vehicle, including clothing referencing Allah and an Iranian flag design.
  - issue: The specific detail — 'clothing referencing Allah and an Iranian flag design' — is not supported by any of the cited sources that were fetchable. The KUT source says only 'indicators on the subject and in his vehicle that indicate potential nexus to terrorism' without specifying what those indicators were. The FBI primary source (fbi.gov) returned HTTP 403 and could not be confirmed. The CNN source returned HTTP 451. This specific, vivid detail is asserted as fact with no verifiable citation, and is particularly load-bearing because it shapes the reader's understanding of the terrorism nexus.
  - evidence: KUT source (fetched) mentions only generic 'indicators' — no Allah clothing or Iranian flag. FBI source (403 forbidden). CNN source (451 unavailable). No cited source verifiably contains these specific items.
  - fix: Either hedge this sentence ('reportedly including...') and add a specific URL that confirms these details, or remove the specifics and use the language the KUT source actually supports: 'indicators on the suspect and in his vehicle suggesting a potential terrorism nexus.'


### 2026-03-14-nys-utility-rates-data-investigation

- **[factual-error]** Annual lobbying spend by energy entities nearly tripled from $3.4 million (2011) to $8.4 million (2024).
  - issue: $8.4M / $3.4M = 2.47x — approximately 2.5x, not 3x (tripled). 'Nearly tripled' implies approaching 3x; 2.5x is a 20% overstatement of the growth multiple.
  - evidence: Python: 8.4 / 3.4 = 2.47x. 'Tripled' or 'nearly tripled' requires approaching 3.0x.
  - fix: Change to 'more than doubled' or 'grew 2.5-fold' — both accurate for the 3.4→8.4 progression.

- **[factual-error]** Of that, $62.9 million (87.7%) was specifically identified as related to rate cases and energy policy.
  - issue: 62.9 / 75.7 = 83.1%, not 87.7%. The percentage does not match the dollar figures cited in the same sentence. This is either an arithmetic error or one of the two figures (62.9M or 75.7M) is wrong.
  - evidence: Python: 62.9 / 75.7 × 100 = 83.1%. For 87.7% to be correct, the rate-related figure would need to be ~66.4M (not 62.9M), or the total would need to be ~71.7M (not 75.7M).
  - fix: Recheck the source figures. If $62.9M and $75.7M are both correct from JCOPE disclosures, the percentage should read 83.1%. If 87.7% is correct, one of the dollar figures is wrong.


### 2026-03-21-agriculture-week-family-farms

- **[unsupported]** ~424 estates (1.0% of ~40,883 projected deaths) would owe tax if TCJA had expired
  - issue: The 424-estates count and '40,883 projected deaths' figure were not found in either cited primary source (USDA ERS or OSU Extension). The OSU source confirms the 0.3%→1.0% percentage shift but gives no count of 424. The 40,883 deaths figure appears to be an internal derivation (1.0% of 40,883 ≈ 408, not 424), and neither the numerator nor the denominator was verified against a cited source.
  - evidence: OSU Extension (fetched): confirms '0.3%' and '1.0%' but does not give the raw estate counts. USDA ERS (fetched): gives 41,104 deaths (not 40,883) for the 2024 analysis. Neither source was found to contain '424 estates' or '40,883 projected deaths.'
  - fix: Cite a specific source for the 424-estate count and the 40,883 deaths figure, or replace the count with the percentage only (0.3% → 1.0%) which is supported by the OSU source.

- **[unsupported]** Total U.S. wineries fell from 11,450 to approximately 11,107 in 2025 — a loss of 343 wineries, nearly one closure per day
  - issue: The cited source (Wine Industry Insight newsletter) does not contain these specific figures — it aggregates external articles and only mentions a Gallo facility closure with 93 jobs. The specific winery-count figures (11,450 → 11,107, 343 closures) could not be verified in the cited primary source. The source appears to be a search-summary/aggregator linking to underlying news articles rather than a primary data source.
  - evidence: WebFetch of cited Wine Industry Insight URL returned no numerical winery count data; the page is a newsletter that links to NYT and other articles. The 11,450 / 11,107 / 343 figures do not appear in the fetched content.
  - fix: Identify and link to the primary data source (e.g., Wine Institute, Silicon Valley Bank annual report, or USDA NASS winery count) that contains the 11,450 and 11,107 figures, or hedge with 'according to [specific source]' rather than stating as fact.


### 2026-03-21-ida-donor-exemption-pattern

- **[internal-contradiction]** ECIDA Audit: '100% approval rate on all 30 projects reviewed' and '14 of 32 project owners missed job creation targets'
  - issue: Internal inconsistency: 30 projects are said to have been reviewed (yielding 100% approval), but the missed-targets denominator shifts to 32 project owners. If only 30 projects were reviewed, the denominator for missed targets should be 30 or fewer, not 32. The entry never explains the discrepancy.
  - evidence: Entry lines 59–63: '100% approval rate on all 30 projects reviewed' vs. '14 of 32 project owners missed job creation targets'. The OSC audit URL returned 404, so the underlying audit could not be consulted to resolve which number is correct.
  - fix: Confirm from the actual Comptroller audit report (OSC S9-15-70) whether 30 or 32 is the correct project/owner count, and use a consistent denominator throughout.

- **[unsupported]** Greene County has the highest per-household burden in New York State ($11,073)
  - issue: This figure is unsupported by the cited source. The Public Ledgers page for Greene County (thepublicledgers.org/ida/counties/ny/greene/) does not display a per-household burden figure, and the NY state index page does not rank counties by per-household burden. The $11,073 figure cannot be verified from the cited URL and appears to have no accessible primary source citation.
  - evidence: WebFetch of thepublicledgers.org/ida/states/ny/ and /ida/counties/ny/greene/ found no per-household burden data displayed. The state page lists total subsidies ($221.3M for Greene) but no per-household figure or ranking by per-household burden.
  - fix: Either link to the specific methodology page where the $11,073 per-household figure is calculated, or remove the claim. If retained, note it is a derived figure from ACS household estimates divided into total exemptions.


### 2026-03-21-obbba-ida-vote

- **[unsupported]** $776 million in property tax exemptions, 74 IDA beneficiaries donated $246,951, $66.2 million in exemptions held by those donors, $268 in public subsidy per $1 donated — all attributed to thepublicledgers.org/ida/states/ny/
  - issue: The cited URL (thepublicledgers.org/ida/states/ny/) shows only a state-level overview ($13.9B for all of NY, 6,446 companies). None of the district-specific figures appear there. The source URL is a general landing page, not a page that surfaces these specific NY-23/Langworthy crossref numbers. The figures are internally consistent with the sibling entry (2026-03-21-ida-donor-exemption-pattern.md) but are sourced to a URL that does not contain them.
  - evidence: WebFetch of thepublicledgers.org/ida/states/ny/ returned only state aggregate data. NY-23-specific figures (74 donors, $246,951, $66.2M, $268/dollar) do not appear at that URL.
  - fix: Replace the cited URL with a direct link to the county or district-level page on The Public Ledgers that actually contains the crossref analysis, or add a note that these figures derive from the methodology documented at the sibling entry (2026-03-21-ida-donor-exemption-pattern.md) which links to downloadable CSVs.


### 2026-04-10-immigration-crime-victims-list

- **[unsupported]** Sheridan Gorman's case is grouped implicitly among the 'five convictions' in the Context section, though the case review says only that Medina was 'charged with first-degree murder.'
  - issue: A murder charge is not a conviction. Gorman was killed March 19, 2026; the post is dated April 10, 2026 — only 22 days later. No conviction could have occurred by that date. Including Gorman in a 'convictions' count conflates charge with conviction.
  - evidence: Case review section says 'Jose Medina, charged with first-degree murder' — not convicted. The Context section's 'five convictions' implicitly requires Gorman to be counted as a conviction to reach five.
  - fix: Move Gorman into a 'pending charges' bucket alongside Nungaray, or give it its own line in the Context summary. Make clear that Gorman is charged, not convicted.


### 2026-04-16-actblue-subpoena-compliance

- **[factual-error]** WinRed 'processes comparable donation volumes' to ActBlue's ~$4 billion
  - issue: WinRed processed approximately $1.8 billion in 2024 (Wikipedia/FEC-sourced figure), less than half of ActBlue's claimed ~$4 billion. Describing these as 'comparable donation volumes' is inaccurate — the gap is material, not marginal.
  - evidence: Wikipedia's WinRed article states it 'processed $1.8 billion in donations from 4.5 million small-dollar donors' in the 2024 cycle. The entry claims ActBlue's 2024 volume was 'approximately $4 billion.' A 2:1 ratio is not 'comparable.'
  - fix: Replace 'comparable donation volumes' with an accurate statement such as 'substantial, though smaller, donation volumes' and cite both figures with sources.

- **[unsupported]** ActBlue's '2024 processing volume was approximately $4 billion'
  - issue: No source URL is provided — the source citation has a TODO placeholder. This specific dollar figure cannot be verified against any cited primary document in the entry.
  - evidence: All 7 sources in the entry's Sources section carry '<!-- TODO: archive URL -->' placeholders. The $4 billion figure appears to be sourced from an aggregator or general knowledge, not a linked primary source.
  - fix: Add a verifiable source (FEC filings or ActBlue's own annual data) with an archived URL before publishing or treating this figure as confirmed.

- **[unsupported]** The full investigation timeline (April 2, 2025 initial request; June 25, July 22, September 4, 2025 subpoena dates)
  - issue: Every source cited for these specific dates has a TODO placeholder. None of the five specific timeline dates in the table can be traced to a linked primary document.
  - evidence: Sources section lists CBS News, Just The News, National News Desk, and committee press releases — all with '<!-- TODO: archive URL -->' annotations. Without linked sources the timeline cannot be independently confirmed.
  - fix: Archive and link the committee press releases and news articles that document each subpoena date before treating the timeline as verified.


### 2026-04-17-obbba-working-families

- **[unsupported]** The refundable portion (of the CTC) is capped at $1,700.
  - issue: This specific figure ($1,700 refundable cap) is a load-bearing technical claim with no linked primary source. The IRS source does not cover it. All other sources for CTC are TODO placeholders. The $1,700 figure is widely reported and plausible, but without a verifiable URL it cannot be confirmed as cited.
  - evidence: No source URL covers this claim. IRS page confirmed to not mention CTC. Other CTC sources have no URLs.
  - fix: Add a direct citation — IRS CTC FAQ or bill text section — that confirms the $1,700 refundable cap under OBBBA.


### 2026-04-30-bigbrother-fisa-car-surveillance

- **[unsupported]** S. 4465 — FISA Section 702, 45-day extension
  - issue: The extension period '45 days' cannot be confirmed. The closest related bill in govinfo (S.4444) extends 'through May 21, 2026' — only 21 days from the April 30 enactment date of S.4465. The actual extension end date embedded in S.4465's House amendment text is not accessible (congress.gov returns 403). The entry states '45 days' as a fact without a cited source for this specific duration.
  - evidence: govinfo BILLSTATUS-119s4465.xml: related bill S.4444 titled 'extend...through May 21, 2026'; S.4465 became P.L.119-87 on April 30, 2026. No related bill in the XML shows a 45-day (June 14) end date. Congress.gov returns 403.
  - fix: Verify the actual end date in the enrolled bill text and replace '45-day extension' with the confirmed end date (e.g., 'through [date]') or add a source citation for the 45-day figure.

- **[unsupported]** $2.77 billion for AI-powered Autonomous Surveillance Towers, $673 million for biometric entry-exit systems, $5.2 billion for ICE modernization including real-time facial recognition and fingerprint databases (OBBBA / P.L.119-21)
  - issue: These three dollar figures appear in the entry with no source cited in the Sources section. No URL or document is listed that a reader could check to verify these appropriation amounts.
  - evidence: Entry sources section lists six items, none of which cover H.R.1 / OBBBA appropriations figures. The OBBBA paragraph has no inline or footnote citation.
  - fix: Add a citation to the enrolled bill text (P.L.119-21), CBO cost estimate, or a credible news summary that lists these specific dollar amounts.


### 2026-04-30-minnesota-fraud-comparative

- **[unsupported]** Minnesota's COVID-era unemployment fraud rate was less than 1% — among the lowest in the country. The national average was 11–15% (GAO). Republican-led states were worst: Kansas (25% fraudulent) and Louisiana (17% fraudulent).
  - issue: The Kansas 25% and Louisiana 17% state-level UI fraud rates are presented as facts sourced to the cited GAO report (GAO-23-106696), but that report explicitly covers only national-level estimates (11–15%) and does not contain state-level breakdowns. The state-specific figures come from separate state audits (Kansas Legislative Audit; Louisiana state officials) that are not cited anywhere in the entry. The figures themselves are accurate but are unsourced as written.
  - evidence: GAO-23-106696 (fetched): 'The document does not provide specific fraud rate information for Kansas, Louisiana, or any individual states.' Kansas 25% and Louisiana 17% confirmed via web search from state-level audits not cited in the entry.
  - fix: Add citations for each state figure (Kansas: Kansas Legislative Audit; Louisiana: Louisiana state officials per published reporting) or clarify that the GAO citation covers only the national 11–15% range and the state figures come from separate sources.

- **[misattribution]** Georgia | Medicare — fraudulent genetic testing via kickbacks | $463 million | Republican (Kemp)
  - issue: The Georgia $463M Medicare fraud was perpetrated by a private lab owner (Minal Patel / LabSolutions LLC) through a scheme of fake telemarketing and kickbacks to telemedicine companies — a federal enforcement action against private actors with no documented state government oversight failure or role by Gov. Kemp's administration. Listing it in a table headed 'Governor at Time' alongside Arizona (Ducey administration warned and did not act) and Mississippi (Bryant was a central figure) implies comparable state-level responsibility that is not established for Georgia.
  - evidence: DOJ press release (via web search): 'Georgia Man Sentenced for $463M Genetic Testing Scheme' identifies Minal Patel of Atlanta operating a private lab enrolled with Medicare. No mention of state government involvement or Kemp administration warnings. The Arizona and Mississippi comparison cases both have documented state-official failures; Georgia does not.
  - fix: Either remove the Georgia row from the table or add a footnote clarifying this was a private-actor federal fraud with no state oversight failure linked to Kemp's administration, distinguishing it from the Arizona and Mississippi cases.

- **[unsupported]** HHS called it 'the largest fraud scheme to have targeted a single demographic group in recent U.S. history.'
  - issue: This quote is attributed to HHS but no HHS source is cited. The only Arizona source listed is the ProPublica article. No search results confirm this exact quote as originating from HHS. It may be a paraphrase from a news article rather than a direct HHS statement.
  - evidence: ProPublica article is the only Arizona source cited. Web search for HHS 'largest fraud scheme' 'single demographic group' returned no HHS press release or statement matching this attribution. The quote could not be traced to a primary HHS source.
  - fix: Add a direct citation to the HHS press release or statement containing this quote, or reattribute to whichever source (ProPublica, DOJ, or news outlet) actually used this language.


### 2026-04-30-scotland-trip-service-claim

- **[unsupported]** TSA agents — federal employees who screened Langworthy's departure — were working without pay.
  - issue: The cited sources say federal workers generally were going unpaid but do not specifically identify TSA agents. The TMZ article says 'FEMA, Coast Guard, and other agencies' employees lacked pay; the Political Wire piece says 'federal workers go unpaid.' Stating specifically that TSA agents were working without pay is an inference not directly supported by the cited sources. Under a DHS partial shutdown TSA status depends on which accounts lapsed; it should be hedged or sourced specifically.
  - evidence: TMZ article names FEMA and Coast Guard specifically, not TSA. Political Wire says 'federal workers' generically. Semafor does not address pay status of specific agencies. No source specifically confirms TSA agents were unpaid during this shutdown.
  - fix: Either cite a source that specifically confirms TSA agents worked without pay during this DHS shutdown period, or broaden the language to 'federal workers' consistent with the cited sources.

- **[unsupported]** In prior cycles, the organization's affiliated super PAC has been substantially funded by labor union PACs (International Union of Operating Engineers: $500,000; United Brotherhood of Carpenters: $500,000; LIUNA: $325,000).
  - issue: The entry cites 'Republican Main Street Partnership — ProPublica Nonprofit Explorer (EIN: 59-1828852)' as the source, but ProPublica's Nonprofit Explorer covers 501(c)(4) IRS Form 990 filings, which do not disclose donors (as the entry itself notes two paragraphs earlier). Super PAC contribution data lives in FEC records, not ProPublica nonprofit filings. The specific dollar figures could not be verified against the cited source. The source reference is either wrong (should be FEC) or the figures are drawn from an unstated source.
  - evidence: ProPublica Nonprofit Explorer confirmed to show RMSP 990 data (CEO pay confirmed). 990 filings for 501(c)(4) organizations do not disclose donors. FEC super PAC committee search for 'main street partnership' returned no matching result via available search. The entry cites ProPublica as the source for these PAC figures but that source cannot contain them.
  - fix: Replace the citation with the correct FEC committee filing or OpenSecrets page that documents these specific contributions. If the figures cannot be sourced to an FEC filing, remove them or hedge as 'according to [source]'.


### 2026-05-04-sugar-industry-trips-howard-center

- **[misattribution]** Weber is described throughout as 'Executive Director of the Red River Valley Sugarbeet Growers Association' and as 'the executive who runs the trip program'
  - issue: The trip program is run through the Red River Valley Sugarbeet Education Foundation (RRVSEF), not the Growers Association. Weber's role at RRVSEF is 'Director' (not Executive Director). His Executive Director title applies to the Growers Association. The entry's description 'the executive who runs the trip program' ties his Growers Association title to RRVSEF's program, conflating the two organizations. The RRVSEF is the entity that actually sponsors and files the trip disclosures (the entry's own table lists 'Red River Valley Sugarbeet Education Foundation' as a co-sponsor).
  - evidence: Howard Center article states Weber is 'director of the Red River Valley Sugarbeet Education Foundation and executive director of the Red River Valley Sugarbeet Growers Association.' The trip-sponsor entity in the entry's own table is RRVSEF.
  - fix: Identify Weber with both titles: 'Harrison Weber, Director of the Red River Valley Sugarbeet Education Foundation and Executive Director of the Red River Valley Sugarbeet Growers Association.' When saying he 'runs the trip program,' note it operates through RRVSEF.


### 2026-05-06-helicopter-funding-credit-claim

- **[unsupported]** The Erie County Comptroller's November 2025 letter stated the project 'is contingent on the County receiving $4.5 million in federal aid' and that '(The final secured amount came in $300,000 below the contingency target — $4.2M instead of $4.5M.)'
  - issue: The $4.5M contingency figure is sourced exclusively to the WGRZ November 2025 article (which timed out and could not be verified) and to the Comptroller's letter text. WKBW, which covers the same November 2025 Comptroller warning, only references $4.2M as the federal funding figure throughout — no mention of $4.5M. If the Comptroller's letter actually cited $4.2M (not $4.5M), the '$300,000 below the contingency target' framing is unsupported. This is a specific derived claim with a single unverifiable source.
  - evidence: WKBW article (same Comptroller story): 'Federal funding sought: $4.2 million' — no $4.5M figure appears. WGRZ November 2025 article timed out; could not confirm the $4.5M figure from the Comptroller's letter text.
  - fix: Confirm the exact dollar figure in the Comptroller's November 2025 letter. If the letter says $4.2M, remove the '$300,000 below contingency' framing. If it truly says $4.5M, note the discrepancy between the letter and public reporting.


### 2026-05-18-aapd-medicaid-disability-contradiction

- **[factual-error]** ProPublica reported the SSI rule '18 days before Langworthy's meeting' (the update note and the body both say '18 days before').
  - issue: April 29, 2026 to May 18, 2026 is 19 days, not 18. The date arithmetic is off by one.
  - evidence: Python date calculation: date(2026,5,18) - date(2026,4,29) = 19 days. The update note at the top of the entry and the body paragraph both state '18 days before.'
  - fix: Replace '18 days before' with '19 days before' in both the update note and the body paragraph.

- **[unsupported]** Cuts of up to $330/month — approximately one-third of the average $994 benefit — for up to 400,000 SSI recipients.
  - issue: The $994 figure is the SSI benefit of the specific individual profiled (Shy'tyra Burton), not a national average. The entry presents it as 'the average $994 benefit,' which is not supported by the cited ProPublica source. The $330/month and 400,000-recipient figures are confirmed.
  - evidence: ProPublica (fetched): 'For Burton, now 22, the $994 monthly benefit is lifesaving but not enough to completely support herself on her own.' The article does not describe $994 as an average SSI benefit.
  - fix: Remove the word 'average' or replace '$994' with a cited national-average figure from SSA. Could read: 'cuts of up to $330/month — approximately one-third of a typical benefit' or cite SSA's published average SSI payment.


### 2026-05-20-federal-grants-credit-claiming-may2026

- **[unsupported]** H.R. 1 (OBBBA) 'reduced SAMHSA community mental health block grants and restructured child care and development funding'
  - issue: This factual assertion is stated without a source citation in the entry. CBO publication 61461 (the only source cited) returned HTTP 403 and could not be verified. No other entries in the tracker corroborate a specific SAMHSA community mental health block grant reduction. The child care restructuring claim is similarly unsourced in context.
  - evidence: Instance 2 OBBBA context paragraph cites no source for the SAMHSA reduction claim. CBO.gov returned 403; claim unverifiable from cited sources.
  - fix: Add a specific citation (bill section number, CBO table, or SAMHSA appropriations comparison) for the SAMHSA block grant reduction claim, or hedge it ('reportedly reduced' / 'proposed to reduce') until a primary source is cited.


### 2026-05-20-halt-act-collins-causal-claim

- **[factual-error]** The HALT Act was signed by Governor Cuomo in April 2021
  - issue: The NYSBA source cited in the entry gives the signing date as March 31, 2021 — which is in March, not April. The NY Senate press release (also cited) confirms the bill was signed but does not give an explicit month; NYSBA is the more specific source and places it in March.
  - evidence: NYSBA source (nysba.org/the-halt-act-and-solitary-confinement-in-new-york-state/) states: 'Governor Andrew Cuomo signed the HALT Act into law on March 31, 2021.' The entry says 'April 2021.'
  - fix: Change 'signed by Governor Cuomo in April 2021' to 'signed by Governor Cuomo on March 31, 2021.'


### 2026-05-20-scaffold-law-infrastructure-expansion-act

- **[unsupported]** New York insurance costs for contractors: 8–10% of project costs, vs. 2–4% in comparative negligence states
  - issue: These specific insurance cost percentage differentials appear in the entry without a verifiable primary source in the cited references. The Finger Lakes 1 article (the most relevant accessible citation) mentions lower insurance premiums generally but provides no specific percentage figures. The Washington Examiner op-ed URL (source 2) returned HTTP 404. These figures may originate from industry advocacy materials not cited.
  - evidence: Finger Lakes 1 article (fetched at 2025/05/21 URL) confirms 5–10% construction cost figure and $2B+ savings but gives no specific insurance percentage differentials. Washington Examiner URL returned 404.
  - fix: Cite the specific source for the 8–10% vs. 2–4% insurance differential (e.g., a specific industry study or press release), or hedge with 'according to [source]' with a working link.

- **[unsupported]** Gary LaBarbera, Council President, Building and Construction Trades Council of Greater New York — opposition statement
  - issue: Source 6 for LaBarbera's opposition statement has no URL, is listed as 'archive pending,' and no quote is directly attributed. The entry attributes a specific argument to LaBarbera ('simultaneously attacks worker safety protections and state sovereignty') but does not cite a primary source or direct quote. This is inference from an unsourced reference.
  - evidence: Source 6 in the entry: 'Building and Construction Trades Council of Greater New York — opposition statement — archive pending' — no URL provided.
  - fix: Add the URL to the opposition statement (e.g., a press release or news report quoting LaBarbera directly). If no direct quote exists, soften to 'the Council has argued' without attributing specific phrasing to LaBarbera by name.


### 2026-05-28-nursing-home-staffing-donations

- **[unsupported]** Facilities with CMS abuse icon: 106 of 106 (100%)
  - issue: A 100% abuse-icon rate across a 106-facility network is extraordinary — the national rate is roughly 15–20% of nursing homes. This claim is stated as bare fact with no direct URL to the CMS Care Compare data that produced it. The entry attributes it to 'CMS Care Compare April 2026 snapshot' but provides no link, and the figure is inherently surprising enough to require either a source link or a hedge noting it is an unusually high rate.
  - evidence: CMS Care Compare abuse icon appears for facilities with abuse/neglect/exploitation citations in the past 3 years; national incidence is ~15-20%. A 100% rate across all 106 facilities in a single operator's network would be an extraordinary finding. The entry provides no URL or methodology note explaining what specific CMS data field was used to classify 'abuse icon' presence. The April 2026 snapshot cannot be re-verified.
  - fix: Add a footnote or parenthetical explaining what the CMS abuse icon means and noting that 100% incidence is highly unusual nationally. Add a direct link to the CMS Care Compare or ownership data source. Alternatively, clarify whether 'abuse icon' here refers to the standard Care Compare red icon or a different CMS data field.


### 2026-05-29-corning-manufacturing-credits-obbba

- **[unsupported]** Hemlock received $325 million in CHIPS Act funding in January 2025.
  - issue: This figure and date could not be verified via primary source — the Commerce/NIST press release URL returned HTTP 403. The claim is plausible (Hemlock has received CHIPS Act awards) but cannot be confirmed from primary sources attempted. Note: Hemlock's active facility is in Michigan (not Tennessee, per finding above), which is consistent with CHIPS Act-funded Michigan polysilicon expansion.
  - evidence: WebFetch of commerce.gov press release returned HTTP 403. No alternative primary source was accessible. Wikipedia references a $375 million Michigan expansion investment from 2022 (state-level), which is distinct from any federal CHIPS Act award.
  - fix: Archive the CHIPS Act award announcement and cite the direct NIST/Commerce.gov press release URL in the entry. If the $325M figure came from a secondary source, note the primary source. Verify the January 2025 date against the original announcement.


### 2026-05-30-drug-pricing-reform-claim

- **[unsupported]** The Congressional Budget Office initially scored §71203 at approximately $4.9 billion in reduced Medicare savings over ten years; CBO revised the estimate upward to $8.8 billion in October 2025.
  - issue: Neither the Fierce Healthcare source (which cited these figures) nor Health Affairs Forefront nor the Morgan Lewis blog post was accessible for verification (HTTP 403 on all three). The CBO score figures and the October 2025 revision date cannot be confirmed from accessible sources.
  - evidence: Fierce Healthcare URL returned HTTP 403. Health Affairs Forefront URL returned HTTP 403. Morgan Lewis blog did not contain CBO scoring data per fetch. No accessible primary source confirms the $4.9B initial or $8.8B revised estimate or the October 2025 revision date.
  - fix: Add a direct link to the CBO score document (e.g., the CBO cost estimate for H.R. 1 / OBBBA) or the specific CBO letter/table where the $4.9B and $8.8B figures appear. The Federal Register or CBO.gov direct URL would be more durable than trade-press summaries.


### 2026-06-02-district-office-consolidation

- **[unsupported]** Bradford Regional Medical Center's OB services were previously consolidated to Olean General in 2019
  - issue: The cited source (WPSU, Feb. 18, 2026) states that Kaleida Health moved surgeries and OBGYN care to Olean but does not mention the year 2019. The '2019' date is unsupported by the cited primary source.
  - evidence: WPSU article fetched: 'they've already moved other services to Olean, New York about half an hour away, including surgeries and OBGYN care' — no year given.
  - fix: Remove '2019' or source it to a document that explicitly states that year (e.g., a prior Bradford Regional or Kaleida press release).

- **[unsupported]** 45 NY hospitals identified as at-risk of closure, including St. James (Hornell, Steuben County)
  - issue: No source URL for the '45 NY hospitals' figure appears in the Sources section. The CLAUDE.md audit landmines note attributes this figure to Public Citizen (446 national / 45 NY, Schuyler named) — but Public Citizen is not listed as a source in this entry, and the entry omits Schuyler from its named examples.
  - evidence: Sources section lists: FEC files, Facebook, WETM, WYDC, Buffalo News, WPSU, NY DOL, FOIL response, Jamestown Post-Journal. No Public Citizen or Fiscal Policy Institute citation.
  - fix: Add the Public Citizen report URL as a source, confirm St. James (Hornell) appears on that list, and verify Schuyler is not dropped from context since the source names it.

- **[missing-hedge]** Niagara County is 'Langworthy's home county' and 'not even inside the new NY-23'
  - issue: The home-county attribution is correct: Langworthy lives in Pendleton, Niagara County (confirmed via Wikipedia). However, the verify_fact.py county script flags Niagara as 'EDGE — small NY-23 sliver; VERIFY before asserting.' The blanket assertion that Niagara is 'not even inside the new NY-23' may be imprecise if a small portion of Niagara falls within the district boundary.
  - evidence: verify_fact.py county niagara returns: 'EDGE — small NY-23 sliver; VERIFY before asserting'. Wikipedia confirms Pendleton, Niagara County as Langworthy's home.
  - fix: Hedge the claim: 'Niagara County (Langworthy's home county) contributes only a small sliver — if any — to NY-23.' Avoid the absolute 'not even inside.'


### 2026-06-02-grape-belt-refresco-federal-response

- **[unsupported]** one grower estimated 2025 economic impact at around $5 million
  - issue: This figure does not appear in any of the cited sources checked (Erie News Now, Post-Journal, WENY). No source in the entry's citation list is tied to this specific figure.
  - evidence: Erie News Now article: no $5M figure found. Post-Journal 'Grape Growers Lose Contract' article: no $5M figure found. WENY article: no $5M figure found. The claim has no traceable citation among the listed sources.
  - fix: Either identify and cite the specific source (e.g. a grower interview or CCE report) where the $5M figure appears, or remove the figure.


### 2026-06-02-rural-health-transformation-212m

- **[internal-contradiction]** A Dunkirk Observer Today commentary in December 2025 — 'Rural hospital funding far from restored' — observed that Langworthy called RHTP 'one of the largest federal investments in our history' while noting that the same OBBBA's Medicaid cuts mean 'RHTP temporarily replaces only one-third of funding lost to permanent cuts.'
  - issue: The Observer Today commentary (Andrea Hatfield) was published December 1, 2025 — 28 days before CMS announced the RHTP awards on December 29, 2025. The piece could not have been reacting to the December 29/30 announcement. The entry's placement of this citation inside the 'Offset Math' section implies it was a response to the award announcement, which is chronologically impossible. The Langworthy quote in that piece likely references his July 2025 OBBBA passage statements, not the December press release.
  - evidence: Observer Today URL path is /2025/12/ and the related entry 2025-11-rural-hospitals-medicaid.md cites the archived URL (web.archive.org/web/20251222205213/...) and explicitly notes 'Dec 1, 2025'. CMS RHTP awards were announced December 29, 2025 per the entry itself (line 17).
  - fix: Clarify that the Observer Today commentary predates the December 29/30 RHTP announcement by nearly four weeks; the Langworthy quote it attributes came from his earlier statements about OBBBA (July 2025), not the December press release. Add date '(Dec. 1, 2025)' to the prose citation and note it discussed anticipated RHTP impacts before the awards were made.


### 2026-06-06-langworthy-secure-data-act-hr8413

- **[unsupported]** The complete 57-signatory list ... is at the U.S. Chamber URL in Sources. [Sources lists: 'U.S. Chamber of Commerce — support letter for H.R. 8413' at https://www.uschamber.com/technology/support-for-h-r-8413-secure-data-act]
  - issue: The URL cited as containing the 57-signatory trade-association coalition list (also used as the frontmatter archived_url) is actually a different letter: a state-and-local chambers of commerce support letter with approximately 229 signatories. The 57-association industry coalition list is at the second Chamber URL in Sources: https://www.uschamber.com/technology/business-associations-welcome-federal-data-privacy-legislation. The 57 count itself is confirmed correct at that second URL, but the in-text sourcing pointer and frontmatter archived_url point to the wrong document.
  - evidence: WebFetch of https://www.uschamber.com/technology/support-for-h-r-8413-secure-data-act returned a letter from state and local chambers (~229 signatories). WebFetch of https://www.uschamber.com/technology/business-associations-welcome-federal-data-privacy-legislation returned exactly 57 trade-association signatories matching the entry's sector table.
  - fix: Change the frontmatter archived_url to archive https://www.uschamber.com/technology/business-associations-welcome-federal-data-privacy-legislation (the 57-association coalition). In the body text, replace 'the U.S. Chamber URL in Sources' with a direct reference to the 'coalition welcome statement' URL, which is already listed as a second source entry.


### 2026-06-10-jasper-troupsburg-fema-award

- **[unsupported]** The federal government's principal pre-disaster mitigation grant program, Building Resilient Infrastructure and Communities (BRIC), had made more than $4.6 billion available since fiscal year 2020
  - issue: The Association of State Floodplain Managers article (cited in the entry's own Sources section) states the program 'has allocated more than $5 billion for investment in mitigation projects' — a materially different figure. The entry attributes $4.6B to CRS IN12609 (which returns HTTP 403 and cannot be directly verified here). Without access to the CRS document, it is unclear whether $4.6B covers only FY2020–FY2023 while the ASFPM $5B+ includes later rounds, or whether one figure is wrong. The entry does not explain the discrepancy between its own cited sources.
  - evidence: ASFPM source (floods.org, cited in entry) states 'more than $5 billion.' Entry states 'more than $4.6 billion' attributed to CRS IN12609 (inaccessible via web fetch, 403). The HTML comment notes the figure was updated from $5B to $4.6B per CRS but does not reconcile the discrepancy with the ASFPM citation that remains in the Sources section.
  - fix: Clarify the scope: if CRS $4.6B covers FY2020–FY2023 only, say so explicitly (e.g., 'more than $4.6 billion for FY2020–FY2023 rounds, per CRS IN12609'). Alternatively, use 'more than $4.6 billion' with a note that figures vary by source and scope, or adopt the higher ASFPM figure and update the text.


### 2026-06-10-minnesota-fraud-50-state-claim

- **[unsupported]** Archived URL field is empty (frontmatter line 9: archived_url: "")
  - issue: The entry has no archive.org URL for the Facebook post source, and the comment at line 163 acknowledges that the Facebook post permalinks have not yet been archived or added. The source_url field also points to the representative's general Facebook page rather than the specific posts. This violates the site's content standard requiring all sources to be archived.
  - evidence: Line 9: archived_url: "". Lines 163–164 comment: "Replace source_url with the two Facebook post permalinks and archive them; add post screenshots to static/images/fact-checks/ (both posts verified verbatim from screenshots in-session)."
  - fix: Add Facebook post permalinks to source_url (or add a second source field), archive both posts via Wayback Machine, and populate archived_url. Add screenshots to static/images/fact-checks/ per the comment's own TODO.


### 2026-06-14-ocr-collapse-disabled-students

- **[factual-error]** New York had 627 pending cases and just 1 resolution agreement in 2025 (Figure 2, HELP Justice Denied report)
  - issue: The extractable Appendix Table 1 of the Senate HELP 'Justice Denied' report (the only tabular data readable from the PDF) shows NY* = 626 pending cases, not 627. The entry's inline draft note also says 627 citing Figure 2 (a chart/graphic whose pixel data did not extract). The one-number discrepancy may reflect a rounding or rendering difference between Figure 2 and Appendix Table 1, but the verifiable primary-source table contradicts the published claim.
  - evidence: HELP Justice Denied Appendix Table 1 (extracted via pdfminer): NY* pending cases = 626, resolution agreements = 1. Entry states 627. The entry's comment says confirmed against 'Figure 2, p.7' — Figure 2 is a bar chart and its data did not extract as text.
  - fix: Verify the Figure 2 chart number in the PDF visually. If Figure 2 shows 627 and Table 1 shows 626, cite the table (626) or note the discrepancy. If both show 626, correct to 626.

- **[misattribution]** Restraint and seclusion of disabled (IDEA) students concentrated in NY-23's regional programs — specifically naming Cattaraugus-Allegany-Erie-Wyoming BOCES
  - issue: Wyoming County is NOT in NY-23 (confirmed by the county verification script). The entry frames CAE-Wyoming BOCES as one of 'NY-23's regional programs' without noting that Wyoming County falls outside the district. Three of the four counties (Cattaraugus, Allegany, and Erie-partial) are in NY-23, so the BOCES data is relevant, but the framing overstates geographic fit. A reader may infer all four counties served are NY-23 counties.
  - evidence: County script: wyoming -> NOT IN NY-23. cattaraugus -> IN NY-23, allegany -> IN NY-23, erie -> IN NY-23 (PARTIAL). The entry says these are 'NY-23 regional programs' without qualification.
  - fix: Add a parenthetical: 'Cattaraugus-Allegany-Erie-Wyoming BOCES (which serves Cattaraugus, Allegany, Erie, and Wyoming counties — the first three overlapping NY-23)' or otherwise note that Wyoming County is outside the district.
