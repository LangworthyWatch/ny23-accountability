# Post-election format pilot, November 13 to December 11, 2026

## What is being tested
- **Cadence:** a weekly roundup every Friday, plus two entry posts a week.
- **Templates:** v2 card theme, `social-media/lib/card_v2.py`: (A) one number, (B) what he said beside the record, (C) the weekly roundup.
- **Palette:** navy as the brand; amber for the finding; slate for the fair case; gray for context; red only for FALSE.
- **Captions:** 600 to 1,000 characters, leading with the finding, with the entry carrying the detail.
- **Tags:** "HELD UP" when a claim of his checks out; "IN HIS FAVOR" when a record cuts his way.

## Status of the four steps (Nov 11)
1. Mockups: done. research/style-refresh-2026-11/ holds the three templates, a colorblind sheet with the current-style card for comparison, and the contrast results.
2. **Picked Nov 11: v2.2** (white framed panel, navy bands, party-neutral palette). CLAUDE.md, /social-post and the house-style memory are updated. The caption rule gained a narrow exception: HELD UP posts lead with the held-up finding.
3. Term tracker: drafted at content/term-tracker/_index.md (draft, with hold_reason). Baseline in research/term-tracker-2026-11/.
4. Pilot: week 1 is ready, with social-media/weekly_2026_11_13_* and social-media/comments_limited_* (both DRAFT).

## Schedule
| Week | Friday roundup | Entry posts (2) |
|---|---|---|
| 1 | Nov 13 | comments-limited (B, ready); Workforce Pell (B with HELD UP, ready) |
| 2 | Nov 20 | from new material |
| 3 | Nov 27 (Thanksgiving week; post Saturday if better) | from new material |
| 4 | Dec 4 | the Dec 3 FEC post-general report (A or B) |
| Review | Dec 11 | compare metrics, decide |

## Weekly routine
1. **Votes.** Open clerk.house.gov in the built-in browser and run `scripts/weekly_votes.browser.js` with FROM set to the first roll call of the week. Save the JSON to research/sources/votes-YYYY-MM-DD/.
2. **His pages.** Look over both Facebook pages for the week's posts and any checkable claims. Crop captures to the post.
3. **What we checked.** List the week's new entries and updates.
4. **In his favor or held up.** Include one item whenever the week has one. Never invent one.
5. **Build and post.** Build the card from template C, keep the caption at or under 1,000 characters, and post on Friday.

## Measuring
Fill in `metrics.csv` from Facebook Insights, about 7 days after each post. Baseline: the posts from October 26 to November 9, 2026, in the old style, entered with type `old`. Decision at the review:
- Keep the new templates if median reach per post and median shares per post are at least as high as the baseline. If they're lower, find out why before dropping them; for example, roundups may reach fewer people but get more clicks.
- Keep the weekly roundup if it's sustainable (about an hour a week) and its clicks hold steady or grow.
