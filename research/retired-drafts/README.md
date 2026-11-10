# Retired drafts

Fact-check drafts that were never published and were retired in the November 10, 2026 audit. They are kept for the record and for possible revival. Hugo does not build this folder.

| Draft | Why it was held | Why it was retired |
|---|---|---|
| 2026-07-25-landa-donor-public-record | Right of reply owed to Benjamin Landa, a private individual, over pending civil fraud allegations | The published May 28 entry (`2026-05-28-nursing-home-staffing-donations`) covers the donor relationship. The rest concerns a private person and would need a right-of-reply process. |
| 2026-07-25-aipac-money-and-record | Comment request to his office on the trip sponsorship and the bundled contributions | No comment request was sent. The money is covered in `2026-10-31-pre-election-money-filings`. The trip-sponsorship angle is the one piece that's unique here. |
| 2026-07-25-flag-raising-posts-causal-claims | Comment request | July posts. Revive only if he repeats the claim. |
| 2026-07-31-local-cops-law-sheriff-quote | No absolute date for the post; the screenshot shows only "4h" | The date can't be established. The screenshot the draft references was never saved to static/. |
| 2026-08-14-moog-defense-credit-claim | Three items: post permalinks, whether the $7M PIC transfer survived into enacted FY26 defense funding, an ALPA archive. Plus a comment request. | Too much open work for an August claim, and it needs a comment request. |
| 2026-04-17-real-cost-series-framing | None | A series-framing piece superseded by later entries. |

Images moved here: one flag-raising screenshot (2026-07-25-mamdani-post.png). The other (2026-07-25-buffalo-flag-post-jul2.png) stays in static/ because the published July 2 Buffalo fireworks entry uses it. The matching social captions are marked RETIRED in their first line. Safety 301s were added in static/_redirects for the slug URLs the July captions used (landa-donors, aipac-record, flag-claims), in case any of those captions were posted.

To revive one: move it back to `content/fact-checks/`, resolve its `hold_reason`, delete that field, run `prepublish_lint.py`, and add an index row.
