# Site audit plan, November 10, 2026

## Principles
1. **One number, one home.** A figure that appears on several pages, such as the PAC share, the missed-vote rate or the in-district share, lives on one canonical page or entry. Every other page links to it rather than restating it. This is how the methodology page drifted to "~44%" while the October 16 entry said 54.6%.
2. **Dated, not undated.** Every evergreen page states its data-as-of date near the top. A dated page that's old is honest. An undated page that's old reads as wrong.
3. **Rebuild on the data calendar.** The post-general FEC report, due December 3, closes the 2025-26 cycle. The State Board of Elections certifies in December. The 119th Congress ends January 3. Rebuild once, after each of those, rather than now and again.

## Correction to the Nov 10 scan
The missed-votes page is current through **July 21, 2026**, using GovTrack aggregates. The "through June 2024" hit was a quarterly row on that page, not its data date. It needs a refresh, not a rebuild.

## Phase 1: this week (small, reader-facing)
- [ ] **Three live 404s.** Published pages link to unpublished drafts. Repoint each:
  - Kentucky JFC entry → Landa draft. Repoint to `2026-05-28-nursing-home-staffing-donations`, which covers the same donor relationship.
  - ACC independent-expenditure entry → AIPAC draft. Repoint to the AIPAC section of `2026-10-31-pre-election-money-filings`.
  - Trump Accounts entry → "real cost" framing draft. Drop the link and keep the text.
- [ ] **Link guard.** Add a check that fails when a published page links to a draft or a missing slug. Put it in `prepublish_lint.py` and run it before every deploy.
- [ ] **Methodology "What local media has not covered" table.** Several rows are stale or wrong:
  - It gives a 3.9% missed-vote rate. The missed-votes page says 3.5%, and argues the headline figure misleads on its own.
  - It gives ~44% PAC dependency. The current figure is 54.6%.
  - Its donor-geography question has since been answered on the site.
  - Its "None" coverage claims are no longer true for the nursing-home money, which the American Prospect has since covered.
  - Fix: label the table as a June 2026 snapshot and replace each figure with a link to its canonical page. Bump "Last updated."
- [ ] **Campaign finance page.** Add a dated note at the top of the federal section saying it covers 2023-24 and linking to the 2025-26 entries (Oct 16, Oct 31, Nov 5). Leave the full rebuild for Phase 2. Leave the IDA section alone, because the related Erie material is under the COI pause.
- [ ] Commit the regenerated `static/data/dashboard.json`.

## Phase 2: after the December 3 post-general FEC report
- [ ] Rebuild the federal section of the campaign finance page for the full 2025-26 cycle from the raw filings. Cover totals, PAC share, in-district share, sectors using the committee-master rule, and top PAC donors. Script it so the next cycle is a single command. Keep 2023-24 as an archived section below it.
- [ ] Same session: replace the "through Oct 14" receipts in the mandate entry and refresh the 2025-26 figures in the health entry.

## Phase 3: December certification and the end of the 119th Congress
- [ ] Mandate entry: swap in the certified results for NY-23 and the five peer districts.
- [ ] Missed-votes page: do one refresh through the final 119th-Congress roll call, early January, using GovTrack aggregates and Clerk rolls for the lame-duck votes.

## Drafts: decisions needed (preliminary recommendations from each hold note)
| Draft | Hold | Recommendation |
|---|---|---|
| 2026-07-25 Landa donor public record | Right of reply owed to a private individual on pending fraud allegations | Retire. The published May 28 entry covers the donor relationship. |
| 2026-07-25 AIPAC money and record | Comment request to his office | Finish only if a comment request goes out. Otherwise retire; the Oct 31 entry covers the money. |
| 2026-07-25 Flag-raising causal claims (NOT SUPPORTED) | Comment request | Retire unless he repeats the claim. |
| 2026-07-31 Local Cops Law sheriff quote | No absolute date for the post | Retire. |
| 2026-08-14 Moog defense credit claim | Permalinks and screenshots | Try the Photos-grid permalink method. If that fails, retire. |
| 2026-06-10 H.R. 6047 veterans loan fees | None; apparently forgotten | Check the bill's status since June, then publish. |
| 2026-10-22 Olean/Ellicottville fire grants (MOSTLY TRUE) | None | Re-verify, then publish; the card and caption are drafted. |
| 2026-04-17 "Real cost" series framing | None | Retire; later entries superseded it. |

"Retire" means deleting the draft file or moving it to `research/retired-drafts/`, and marking any matching social post RETIRED.

## Social drafts
- [ ] In one pass, mark campaign-window captions RETIRED, including closing posts 1-4, the Epstein oversight post and the Reeves Act post. Keep the captions tied to drafts that are being published.

## Upkeep, monthly
- [ ] A freshness report script that lists each evergreen page with its data-as-of date and flags anything over 90 days old, any published-to-draft link, and any canonical figure that appears on a page without a link.

## User-only
- [ ] Revoke the Cloudflare token pasted in an earlier session.
- [ ] Repoint `www.langworthywatch.org` from Netlify to Pages.
- [ ] Send any comment requests for drafts you choose to finish.
