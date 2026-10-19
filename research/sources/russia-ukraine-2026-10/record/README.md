# Langworthy (L000600) Russia/Ukraine record, 2022-2026

This is research only. Nothing under `content/` was edited. Compiled 2026-10-19.

## Files

| Path | What it is |
|---|---|
| `clerk-all/YYYY/rollNNN.xml` | Every House Clerk roll-call XML for 2023 (1-724), 2024 (1-517), 2025 (1-362) and 2026 (1-314). 1,917 votes, about 177 MB. **Do not commit. Add `research/sources/russia-ukraine-2026-10/record/clerk-all/` to `.gitignore`.** 2026 stops at roll 314 (Sept 16). Roll 315 and later return a Clerk error, and the Clerk site says the House is out until Oct 22. |
| `rolls_index_2023_2026.csv` | Index of all 1,917 votes, with Langworthy's vote taken from `name-id="L000600"`. |
| `langworthy-russia-ukraine-votes.csv` + `clerk/` | The 49 Russia/Ukraine-relevant votes, with copies of their XML files. |
| `amendments-118-ukraine-russia.txt`, `amendments-119-ukraine-russia.txt` | Amendment purposes from govinfo BILLSTATUS `<amendments>`, matched to roll numbers. |
| `billstatus-119-russia-ukraine-scan.txt` | 119th measures with Russia/Ukraine in the title: floor actions and whether L000600 cosponsored. Bills were read from `<cosponsors><item>`. |
| `bills/` | BILLSTATUS XML for H.R. 5334, 2548, 2913 and 36, H.Res. 518 and 1530, and the 118th bills. Enrolled H.R. 5334 text (`BILLS-119hr5334enr.*`), H.R. 2548 as introduced, Rules reports H. Rept. 118-466 and 119-825. |
| `press/` | All 454 langworthy.house.gov press releases from Jan 3, 2023 to Oct 15, 2026 (`items.json`, plus `html/` and `text/`). |
| `crec/` | Congressional Record granules: Feb 14, 2024 (H603) and the debates on H.R. 5692, H.R. 8035, H.R. 2913 and H.R. 5334. |
| `news/` | City & State, Feb 28, 2022 (text retained). Buffalo News, May 2024 (paywalled; see below). |
| `oversight/` | docs.house.gov Oversight (GO00) calendar scrape. It is incomplete: only 29 events were captured. |
| `wayback/wayback-verified.tsv` | Wayback captures, each checked by playback (HTTP 200 plus the expected text). |
| `scripts/` | `fetch_rolls.py`, `index_rolls.py`, `scan_billstatus.py`, `amdts.py`, `amdts119.py`, `pr_list.py`, `pr_fetch.py`, `wayback.py`. Run them with `python3`. |

## 1. Statements

| Date | Venue / author | Quote | Verification |
|---|---|---|---|
| 2022-02-24 | NYGOP release (NYGOP FB page; also his own "Nick Langworthy" FB page) | "This is a dark day for the democratic world... Biden's weakness and ineptitude have led us to this moment... every moment that goes by without severe consequences is a threat to the entire globe." | Screenshots 01 and 07 only. No URL. Not archived. He was a private citizen and NYGOP chair at the time. |
| Late Feb 2022 (City & State article dated 2022-02-28) | NYGOP convention speech, as reported by City & State | "We need to start acting like the Ukrainians"; also "If anyone thinks that Russia would have invaded the Ukraine if this last presidential election went differently, you've got another thing coming." | Reporter's quotes; text in `news/cityandstate-2022-02-convention.txt`. |
| 2023-02-22 | "Nick Langworthy" FB page. This is likely the campaign page `ChairmanNickLangworthy`; the screenshot shows the page name but no handle. | "This is what happens when America projects weakness on the world stage." | Screenshot 02 only. **Confirm which page carried it before attributing (failure mode 6).** |
| 2023-03-15 | "Congressman Nick Langworthy" (verified official page) | "American weakness invites aggression... Russia & China are watching us, testing us and growing more emboldened by the day." | Screenshot 03 only. Not archived. |
| 2024-02-14 | House floor, rule debate on H.R. 7176 | "At a time when the President is pushing for more funding for Ukraine, it is disingenuous that he is turning around and forcing our allies to rely on Russia for natural gas." | **Congressional Record** 170 CR H603-H610 (`crec/`). His press release of Feb 15, 2024 has the prepared text ("funding to Ukraine"). NOLA (screenshot 05) quotes the same line. |
| 2024-04-22 | Official newsletter excerpt on langworthy.house.gov | "I could not in good conscience vote for the $60 billion aid bill as it was crafted... Putin is a thug and a butcher, and Ukraine is right to defend itself... I would have supported legislation that purely provided munitions with direct oversight." His stated reasons: $7.85B for Ukrainian government salaries and pensions; a $9.85B "loan" the President could forgive; $113B already sent; tracking and corruption concerns; $34.5T debt; the border. | `press/text/rep-langworthys-weekly-newsletter-votes-foreign-aid.txt` |
| 2024-05-20 | Buffalo News | The FB card headline reads "Langworthy, Tenney opposed aid for Ukraine..." but the page `<title>` is "Western New York reps in Congress oppose Ukraine aid bill". | **Paywalled.** The body is served obfuscated, and we did not decode it. The only readable line is "...Western New York's two Republican members of Congress did nothing to help it get there." Do not quote the article beyond that. Use his own newsletter for his reasons. |
| 2024-06-14 | Press release (NDAA FY25) | The bill "ensures our military is ready to counter threats from China, Russia, and Iran" | `press/text/` |
| 2025-2026 | Press releases | **None** of the 454 releases mention Ukraine, Russia, Putin, NATO or Zelensky after Nov 2024. That includes his votes on H.R. 2913 (Nay) and H.R. 5334 (Yea). Word-boundary grep. | `press/text/` |

No floor remarks by him appear in the debate granules for H.R. 5692, H.R. 8035/H.Res. 1160, H.R. 2913/H.Res. 518, or H.R. 5334/H.Res. 1530. We searched for "Mr. LANGWORTHY".

## 2. Votes

See `langworthy-russia-ukraine-votes.csv`. These are the key ones.

| Date | Measure | Roll | LW | Result |
|---|---|---|---|---|
| 2023-04-17 | H.Res. 240, condemning Russian downing of US drone | 2023-184 | Yea | 410-0 |
| 2023-07-13 | NDAA FY24 Greene amdt: strike $300M USAI | 2023-303 | No | Failed 89-341 |
| 2023-07-13 | NDAA FY24 Gaetz amdt: prohibit security assistance to Ukraine | 2023-304 | No | Failed 70-358 |
| 2023-07-13 | NDAA FY24 Ogles amdt: strike lend-lease extension | 2023-307 | No | Failed 71-360 |
| 2023-07-13 | Greene amdt: strike Ukraine Center of Excellence study / Davidson amdt: Ukraine strategy report | 2023-305 / 306 | Aye / Aye | Failed |
| 2023-09-27 | Defense approps (H.R. 4365) Biggs amdt: cut USAI by $300M | 2023-432 | **Aye** | Failed 104-330 |
| 2023-09-27 | H.R. 4365 Gaetz amdt: prohibit security assistance to Ukraine | 2023-438 | **Aye** | Failed 93-339 |
| 2023-09-28 | SFOPS (H.R. 4665) Greene amdts: prohibit Ukraine assistance / drawdowns | 2023-473 / 474 | Aye / Aye | Failed |
| 2023-09-28 | H.R. 5692, $300M Ukraine Security Assistance and Oversight Supplemental | 2023-503 | **Nay** | Passed 311-117 |
| 2023-12-14 | NDAA FY24 conference report | 2023-723 | Yea | 310-118 |
| 2024-03-19 | H.Res. 149, condemning abduction of Ukrainian children | 2024-88 | Yea | 390-9 |
| 2024-04-19 (report date) | **Rules Cmte** record vote 218: report rule H.Res. 1160 (all four supplementals) | H.Rept. 118-466 | Yea | 9-3 |
| 2024-04-19 | H.Res. 1160 (rule) | 2024-142 | Yea | 316-94 |
| 2024-04-20 | H.R. 8038 (REPO for Ukrainians Act, TikTok, Iran sanctions) | 2024-145 | Yea | 360-58 |
| 2024-04-20 | H.R. 8035 amdts: Spartz (drawdown) / Greene (zero out) / Cammack (strip non-military) | 2024-147 / 148 / 149 | Aye / No / Aye | Failed |
| 2024-04-20 | **H.R. 8035 Ukraine Security Supplemental** | 2024-151 | **Nay** | Passed 311-112-1 (enacted via H.R. 815, P.L. 118-50) |
| 2024-06-13 / 06-27 | Greene amdts barring Ukraine aid (NDAA FY25; Defense approps FY25) | 2024-261 / 324 | Aye / Aye | Failed |
| 2025-05-05 | H.R. 36 MEGOBARI Act (Georgia) | 2025-116 | Yea | 349-42 |
| 2025-07-18 / 09-10 | Greene amdts barring Ukraine aid (H.R. 4016; NDAA FY26) | 2025-209 / 255 | **No** / **No** | Failed |
| 2026-06-03 | Motion to discharge H.Res. 518 (Ukraine Support Act rule) | 2026-200 | Nay | 218-204 |
| 2026-06-04 | H.Res. 518 / **H.R. 2913 Ukraine Support Act** | 2026-206 / 207 | Nay / **Nay** | Passed 226-195 (pending in Senate) |
| 2026-07-21 | NDAA FY27 Crane amdt: bar USAI | 2026-264 | No | Failed 76-350 |
| 2026-09-15 | H.Res. 1530 (rule incl. H.R. 5334) | 2026-299 / 300 | Yea / Aye | 214-211 |
| 2026-09-16 | **H.R. 5334, concur in Senate amdts (Graham Sanctioning Russia and Iran Act)** | 2026-308 | **Yea** | 262-159. **P.L. 119-111** |

## 3. The sanctions bill named in screenshot 06 (a third-party post; not his statement)

**H.R. 5334**, "Lindsey O. Graham Sanctioning Russia and Iran Act of 2026" (Division A). The vehicle was the SEED Act. The House passed the SEED Act by voice vote on 4/27/26. The Senate replaced it with the sanctions text, 86-11 on 8/7/26. The House concurred on 9/16/26, roll 308, 262-159, **with Langworthy voting Yea**. The bill was presented on 9/17 and **signed 9/18/26, P.L. 119-111**.

§115 is the general waiver. It reads, verbatim: "(a) In General.--The President may, subject to subsection (b), waive the application of any sanctions provision with respect to a foreign person, any restriction with respect to a person, or any duty under this title. (b) Reports Required.--(1) In general.--Before issuing a waiver under subsection (a), the President shall submit to Congress--(A) a certification in writing that the issuance of the waiver is in the national interests of the United States; and (B) a report explaining the basis for the certification."

§115 has no congressional-review period. By contrast, §117 makes termination subject to a 30-day review (60 days in July-September) and a joint resolution of disapproval. §110(c), §113(b) and §114 add narrower carve-outs. §203 sunsets Division A after 5 years.

Related records:
- **Rules Cmte, 9/14/26 (H. Rept. 119-825):** record vote 413 was on a Meeks amendment to change the waiver standard to "vital to the national security of the United States." It was defeated 3-7. **Langworthy did not vote** on that motion or on any of record votes 411-414.
- **H.R. 2548** (Fitzpatrick, Sanctioning Russia Act of 2025): Langworthy **cosponsored it on 11/25/2025**. As introduced, it had only a §17(d) tariff waiver: "one time for a period of not more than 180 days," requiring a "national security interests" finding, and barred for certain countries.
- "A month later, to the day" would be 10/18/26 if counted from signing, or 10/16 if counted from House passage. Whether any EO matches is for the other agent's waiver research.

## 4. Oversight Committee (119th)

- No Oversight hearing, markup, or letter on Russia, Ukraine or sanctions was found.
- The Russia sanctions bills H.R. 2548, 6856, 2622, 8718, 10076 and 10828 were referred to Oversight, but BILLSTATUS shows only "Referred To" for each. There was no Oversight action.
- The docs.house.gov scrape is incomplete (29 events), and a full-text grep of it found no hits. The govinfo CHRG search was rate-limited (DEMO_KEY 429). **This is an open gap.**

## 5. Gaps

- Facebook posts 02, 03, 07 and the NYGOP release are documented by screenshot only. They have no URLs and are not archived; use `archive_note`. Post 02's page needs confirming.
- The Buffalo News article is paywalled, so its quotes of him are unverified.
- We could not find the NOLA article URL. The quote is verified via the Congressional Record instead.
- We did not retrieve signer lists for the discharge petitions (Meeks No. 6; Fitzpatrick H.Res. 1067).
- 118th-Congress cosponsorships of Russia/Ukraine measures were not scanned. The 119th scan shows H.R. 2548 as his only one, and he sponsored none.
- Rules Committee record votes on the 2023 rules (H. Rept. 118-142, 118-216) were not pulled.

## 6. Wayback status (`wayback/wayback-verified.tsv`)

These are **verified by playback** (HTTP 200 plus the expected text):
- April 22, 2024 newsletter: https://web.archive.org/web/20261019185752/https://langworthy.house.gov/media/press-releases/rep-langworthys-weekly-newsletter-votes-foreign-aid
- Feb 15, 2024 LNG remarks: https://web.archive.org/web/20261019185940/https://langworthy.house.gov/media/press-releases/rep-langworthy-highlights-disastrous-consequences-bidens-halt-lng-exports
- H. Rept. 118-466: https://web.archive.org/web/20261019190916/https://www.govinfo.gov/content/pkg/CRPT-118hrpt466/html/CRPT-118hrpt466.htm
- Buffalo News: https://web.archive.org/web/20261019191606/https://buffalonews.com/news/local/government-politics/article_b54eb150-1472-11ef-819d-1fa5862acee2.html. This confirms only that the page exists, since the body is paywalled.

Everything else is **UNVERIFIED**, because Wayback returned 429 or 520 on save and on playback. That covers the CR H603 page, enrolled H.R. 5334, H. Rept. 119-825, all Clerk roll XMLs and City & State. Some rows carry a 14-digit timestamp from the SPN redirect, but that is not proof the capture exists. **Do not cite them** until `python3 scripts/wayback_reverify.py` has been re-run and they flip to VERIFIED. Local primary copies of all of them are saved in `clerk/`, `bills/`, `crec/` and `news/`.
