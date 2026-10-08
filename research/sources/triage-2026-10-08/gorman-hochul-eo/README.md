# Source retention: Langworthy Oct 6, 2026 post on Sheridan Gorman / Trey Gowdy clip / Hochul "first Executive Order"

Retained 2026-10-08 for a fact-check of the Oct 6, 2026 post on the official "Congressman Nick Langworthy" Facebook page.
All pages were pulled with `curl -sL -A "Mozilla/5.0"`; `.txt` files are tag-stripped text of the matching `.html`.
PDF text was extracted with `pdftotext`; two scanned PDFs (Cuomo EO 170 and EO 170.1) were OCR'd with tesseract (`*.ocr.txt`).
The Fox clip was downloaded with `yt-dlp` and transcribed locally with openai-whisper `base.en` (machine transcript; check against the video before quoting).

## Files (what each one is for)

### Hochul Executive Order 1 and the Cuomo immigration orders it carried forward
| File | Source URL | What it establishes |
|---|---|---|
| governor-ny-eo-1-2021-08-24.html / .txt | https://www.governor.ny.gov/executive-order/no-1-review-continuation-and-expiration-prior-executive-orders | Hochul EO No. 1, Aug 24, 2021: "Review, Continuation and Expiration of Prior Executive Orders." Blanket 45-day continuation of all prior governors' EOs to Oct 8, 2021. Does not mention immigration. |
| governor-ny-eo-6-2021-10-08.html / .txt | https://www.governor.ny.gov/executive-order/no-6-continuation-and-expiration-prior-executive-orders | Hochul EO No. 6, Oct 8, 2021: itemized list of prior EOs continued. Item III(t) continues Cuomo EO 170 (Sept 15, 2017, "State Policy Concerning Immigrant Access to State Services"). |
| governor-ny-eo-6.1-2025-01-16.html / .txt | https://www.governor.ny.gov/executive-order/no-61-continuation-and-expiration-prior-executive-orders | Hochul EO No. 6.1, Jan 16, 2025: recites that EO 6 extended EO 170 and orders that EO 170.1 also remains in force. |
| governor-ny-past-executive-orders.html | https://www.governor.ny.gov/past-executive-orders | Index page; source of the EO 170 PDF link. |
| governor-ny-executive-orders-index.html | https://www.governor.ny.gov/executive-orders | Current EO index (most recent page only). |
| cuomo-eo-170-2017-09-15.pdf / .ocr.txt | https://www.governor.ny.gov/sites/default/files/atoms/files/EO%20%23170.pdf | Full text of Cuomo EO 170 (scanned; OCR). |
| hcr-ny-2017-09-15-cuomo-eo170-press-release.html / .txt | https://hcr.ny.gov/governor-cuomo-signs-executive-order-prohibiting-state-agencies-inquiring-about-immigration-status | State press release reproducing EO 170 text (clean text; cross-check for OCR). |
| cuomo-eo-170.1.pdf / .ocr.txt | https://www.governor.ny.gov/sites/default/files/atoms/files/EO_170.1.pdf | Full text of Cuomo EO 170.1, Apr 25, 2018 (judicial-warrant requirement for civil immigration arrests inside state facilities). |
| nyic-2018-cuomo-eo170.1-barring-ice-state-facilities.html / .txt | https://www.nyic.org/?p=3611 | Contemporaneous (Apr 25, 2018) description of EO 170.1. |

### NY statutes: Green Light Law (enacted), New York for All Act (not enacted), Local Cops Local Crimes Act (2026)
| File | Source URL | What it establishes |
|---|---|---|
| nysenate-S1747B-2019-green-light-law.pdf / .txt | https://legislation.nysenate.gov/pdf/bills/2019/S1747B | Bill text, "driver's license access and privacy act" (Green Light Law). |
| nyassembly-S01747-2019-green-light-actions.html / .txt; nyassembly-S01747-2019-green-light-status.html / .txt; nyassembly-A03675-2019-green-light-status.html | https://nyassembly.gov/leg/?default_fld=&leg_video=&bn=S01747&term=2019&Actions=Y (and summary pages) | Action history: A3675B passed Assembly 06/12/2019, passed Senate 06/17/2019, "signed chap.37" 06/17/2019. |
| nysenate-S2235B-2025-new-york-for-all.pdf / .txt | https://legislation.nysenate.gov/pdf/bills/2025/S2235B | New York for All Act bill text (2025-26 session). |
| nyassembly-A03506-2025-new-york-for-all-actions.html / .txt; nyassembly-A03506-2025-new-york-for-all-status.html / .txt | https://nyassembly.gov/leg/?default_fld=&leg_video=&bn=A03506&term=2025&Actions=Y | Action history: referred to codes 01/28/2025; amended/recommitted 06/11/2025 and 02/11/2026. No floor action. Not enacted. |
| cityandstate-2026-01-hochul-not-on-board-ny-for-all.html / .txt | https://www.cityandstateny.com/policy/2026/01/hochul-still-not-board-new-york-all/410637/ | Jan 2026: Hochul had not backed NY for All; protections "currently only exist through executive order or case law." |
| governor-ny-2026-08-25-local-cops-local-crimes-287g-ban.html / .txt | https://governor.ny.gov/news/keeping-new-yorkers-safe-governor-hochul-announces-local-cops-local-crimes-provision-banning | Hochul release, Aug 25, 2026: Local Cops, Local Crimes Act (signed May 2026) 287(g) ban took effect; DOJ suit; what the law does. |
| weny-2026-08-local-cops-local-crimes.html / .txt | https://www.weny.com/news/new-law-bans-nys-law-enforcement-from-working-with-ice/article_facc7354-762f-4a95-afe0-3780a1de0868.html | NY-23-area (Steuben) coverage of the law taking effect. |
| cityandstate-2026-07-partisan-rift-immigration-law.html / .txt | https://www.cityandstateny.com/politics/2026/07/partisan-rift-deepens-over-ny-immigration-law/415007/ | Gorman family at Yorktown event with Blakeman and Lawler; Hochul office statement that the NY law "would not have affected the jail's ability to turn over a detainee to ICE in the case of Sheridan Gorman." |
| news12-2026-07-24-gorman-yorktown-local-cops.html / .txt | https://westchester.news12.com/2026/07/24/families-lawmakers-condemn-gov-hochuls-local-cops-local-crimes-act-outside-yorktown-police-station/4n2EIaaku8OnPiYntcEdan | Jessica Gorman and Lawler quotes; Hochul spokesperson statement. |

### Sheridan Gorman case (Chicago, March 19, 2026)
| File | Source URL | What it establishes |
|---|---|---|
| dhs-2026-03-22-ice-asks-pritzker.html / .txt | https://www.dhs.gov/news/2026/03/22/ice-asks-governor-pritzker-and-chicago-sanctuary-politicians-not-release-criminal | DHS: Medina-Medina "apprehended by the U.S. Border Patrol" May 9, 2023 "and released"; released again June 19, 2023 after Chicago shoplifting arrest; ICE detainer lodged. Calls him a "Venezuelan criminal illegal alien." |
| abc7chicago-medina-charged.html / .txt | https://abc7chicago.com/post/man-charged-murder-loyola-student-sheridan-gorman-expected-court-dhs-says-jose-medina-is-undocumented-imigrant/18754347/ | Charges (first-degree murder, aggravated use of a firearm); failed to appear on retail-theft case, warrant issued; CBP records matched him; Pritzker statement. |
| suntimes-2026-03-24-gorman-immigration.html / .txt | https://chicago.suntimes.com/immigration/2026/03/24/chicago-crime-trump-pritzker-bovino-immigration-midway-blitz-deport-immigration | Sun-Times: "undocumented immigrant from Venezuela"; active warrant in theft case; Illinois Trust Act / Welcoming City context. |
| foxnews-medina-court-tuberculosis.html / .txt | https://www.foxnews.com/us/illegal-immigrant-accused-killing-chicago-college-student-face-court-after-tuberculosis-delay | Mar 27, 2026 detention hearing; defense says he "turned himself in at the Texas border in 2023"; held pending trial; ICE detainer. |
| foxnews-biden-border-released-lack-of-space.html / .txt | https://www.foxnews.com/politics/biden-border-officials-released-alleged-killer-chicago-student-due-lack-space-documents-show | House Judiciary GOP excerpts: El Paso sector; "processed for a Notice to Appear and released on recognizance ... due to lack of space." |
| foxnews-trump-speaks-gorman-family.html / .txt | https://www.foxnews.com/politics/trump-speaks-family-sheridan-gorman-college-student-allegedly-slain-illegal-immigrant | Gorman "a New York native"; Yorktown Heights vigil. |
| foxnews-cnn-msnow-avoid-gorman.html / .txt | https://www.foxnews.com/media/cnn-ms-now-avoid-covering-loyola-student-sheridan-gorman-murdered-illegal-immigrant-in-chicago | Background only. |
| nysenate-J1817-2025-gorman-resolution.pdf / .txt | https://legislation.nysenate.gov/pdf/bills/2025/J1817 | NY Senate memorial resolution: Yorktown Heights, NY; died Thursday, March 19, 2026, age 18; parents Jessica and Thomas Gorman. |
| assembly-slater-gorman-remembrance.html / .txt | https://assembly.ny.gov/mem/Matt-Slater/story/117582 | Assembly resolution Mar 26, 2026; "murdered in Chicago on March 19, 2026." |
| wlsam-2026-10-07-medina-court.html / .txt | https://wlsam.com/2026/10/07/accused-gunman-in-sheridan-gorman-murder-in-court | Oct 7, 2026 status hearing (text extraction captured mostly navigation; see gaps). |

### The Fox clip (Sunday Night in America with Trey Gowdy, Oct 4, 2026)
| File | Source URL | What it establishes |
|---|---|---|
| foxnews-video-6406230109112.html / .txt | https://www.foxnews.com/video/6406230109112 | Fox video page: show "Sunday Night In America With Trey Gowdy," page date October 5, 2026, runtime 6:43, title "Sanctuary city policies aren't protecting communities, they're protecting criminals: Sheridan Gorman's father." |
| foxnews-video-6406230109112-clip.mp4 | same | The clip itself (yt-dlp). |
| foxnews-video-6406230109112-whisper-transcript.srt | same | Whisper base.en transcript of the 6:43 clip. Contains Gowdy's intro line "...someone in our country unlawfully who then committed other offenses" (matches the caption fragment in Langworthy's post). No occurrence of "Hochul." |
| archive-org-FOXNEWSW_20261005_040000.html / .txt; archive-org-FOXNEWSW_20261005_080000.html / .txt; archive-org-metadata-FOXNEWSW_20261005_040000.json; archive-org-search-gowdy-oct2026.json | https://archive.org/details/FOXNEWSW_20261005_040000_Sunday_Night_in_America_With_Trey_Gowdy | Internet Archive TV listing confirming the episode aired Sunday, October 4, 2026 (6:00pm PDT first airing = 9 pm ET; repeats 9 pm and 1 am PDT). |
| townhall-2026-10-05-gorman-gowdy.html / .txt | https://townhall.com/news/amy-curtis/2026/10/05/sheridan-gormans-dad-trey-gowdy-n2684104 | Oct 5, 2026 write-up quoting the Gowdy interview ("On Sunday, they spoke with Trey Gowdy"); embeds the Fox News X post dated October 5, 2026. |

## Wayback Machine saves
Save Page Now was called with `curl -s -I "https://web.archive.org/save/URL"` (batch 1: no Location header returned for any URL) and then with GET (batches 2-3). Per project memory, existence was verified by playback (`https://web.archive.org/web/2/URL` -> 302 to a dated snapshot), not by the availability API. Raw logs: `wayback-save-results-batch1.txt`, `wayback-save-results-batch2.txt`, `wayback-playback-recheck-batch2.txt`, `wayback-save-results-batch3.txt`.

Verified snapshots (playback 302 -> snapshot URL):
- https://www.governor.ny.gov/executive-order/no-6-continuation-and-expiration-prior-executive-orders -> https://web.archive.org/web/20261008160417/https://www.governor.ny.gov/executive-order/no-6-continuation-and-expiration-prior-executive-orders
- https://www.governor.ny.gov/executive-order/no-61-continuation-and-expiration-prior-executive-orders -> https://web.archive.org/web/20260224085154/https://www.governor.ny.gov/executive-order/no-61-continuation-and-expiration-prior-executive-orders
- https://www.dhs.gov/news/2026/03/22/ice-asks-governor-pritzker-and-chicago-sanctuary-politicians-not-release-criminal -> https://web.archive.org/web/20260811044140/https://www.dhs.gov/news/2026/03/22/ice-asks-governor-pritzker-and-chicago-sanctuary-politicians-not-release-criminal
- https://www.foxnews.com/video/6406230109112 -> https://web.archive.org/web/20261006152704/https://www.foxnews.com/video/6406230109112
- https://townhall.com/news/amy-curtis/2026/10/05/sheridan-gormans-dad-trey-gowdy-n2684104 -> https://web.archive.org/web/20261006153019/https://townhall.com/news/amy-curtis/2026/10/05/sheridan-gormans-dad-trey-gowdy-n2684104
- https://westchester.news12.com/2026/07/24/families-lawmakers-condemn-gov-hochuls-local-cops-local-crimes-act-outside-yorktown-police-station/4n2EIaaku8OnPiYntcEdan -> https://web.archive.org/web/20260725015445/https://westchester.news12.com/2026/07/24/families-lawmakers-condemn-gov-hochuls-local-cops-local-crimes-act-outside-yorktown-police-station/4n2EIaaku8OnPiYntcEdan
- https://www.cityandstateny.com/politics/2026/07/partisan-rift-deepens-over-ny-immigration-law/415007/ -> https://web.archive.org/web/20260808162943/https://www.cityandstateny.com/politics/2026/07/partisan-rift-deepens-over-ny-immigration-law/415007/
- https://governor.ny.gov/news/keeping-new-yorkers-safe-governor-hochul-announces-local-cops-local-crimes-provision-banning -> https://web.archive.org/web/20260926123015/https://www.governor.ny.gov/news/keeping-new-yorkers-safe-governor-hochul-announces-local-cops-local-crimes-provision-banning
- https://hcr.ny.gov/governor-cuomo-signs-executive-order-prohibiting-state-agencies-inquiring-about-immigration-status -> https://web.archive.org/web/20260614201947/https://hcr.ny.gov/governor-cuomo-signs-executive-order-prohibiting-state-agencies-inquiring-about-immigration-status
- https://www.governor.ny.gov/executive-order/no-1-review-continuation-and-expiration-prior-executive-orders -> https://web.archive.org/web/20261008160353/https://www.governor.ny.gov/executive-order/no-1-review-continuation-and-expiration-prior-executive-orders
- https://www.foxnews.com/politics/trump-speaks-family-sheridan-gorman-college-student-allegedly-slain-illegal-immigrant -> https://web.archive.org/web/20261008160614/https://www.foxnews.com/politics/trump-speaks-family-sheridan-gorman-college-student-allegedly-slain-illegal-immigrant
- https://www.governor.ny.gov/sites/default/files/atoms/files/EO_170.1.pdf -> https://web.archive.org/web/20261008160712/https://www.governor.ny.gov/sites/default/files/atoms/files/EO_170.1.pdf
- https://www.foxnews.com/politics/biden-border-officials-released-alleged-killer-chicago-student-due-lack-space-documents-show -> https://web.archive.org/web/20261008160959/https://www.foxnews.com/politics/biden-border-officials-released-alleged-killer-chicago-student-due-lack-space-documents-show
- https://abc7chicago.com/post/man-charged-murder-loyola-student-sheridan-gorman-expected-court-dhs-says-jose-medina-is-undocumented-imigrant/18754347/ -> https://web.archive.org/web/20261008161109/https://abc7chicago.com/post/man-charged-murder-loyola-student-sheridan-gorman-expected-court-dhs-says-jose-medina-is-undocumented-imigrant/18754347/
- https://chicago.suntimes.com/immigration/2026/03/24/chicago-crime-trump-pritzker-bovino-immigration-midway-blitz-deport-immigration -> https://web.archive.org/web/20261008161222/https://chicago.suntimes.com/immigration/2026/03/24/chicago-crime-trump-pritzker-bovino-immigration-midway-blitz-deport-immigration
- https://legislation.nysenate.gov/pdf/bills/2025/J1817 -> https://web.archive.org/web/20261008161343/https://legislation.nysenate.gov/pdf/bills/2025/J1817
- https://www.governor.ny.gov/sites/default/files/atoms/files/EO%20%23170.pdf -> https://web.archive.org/web/20260216050823/https://www.governor.ny.gov/sites/default/files/atoms/files/EO%20%23170.pdf
- https://www.nyic.org/2018/04/immigrant-advocates-applaud-gov-cuomo-barring-ice-state-facilities/ -> https://web.archive.org/web/20261008161546/https://www.nyic.org/2018/04/immigrant-advocates-applaud-gov-cuomo-barring-ice-state-facilities/
- https://assembly.ny.gov/mem/Matt-Slater/story/117582 -> https://web.archive.org/web/20261008161636/https://assembly.ny.gov/mem/Matt-Slater/story/117582
- https://www.cityandstateny.com/policy/2026/01/hochul-still-not-board-new-york-all/410637/ -> https://web.archive.org/web/20261008161725/https://www.cityandstateny.com/policy/2026/01/hochul-still-not-board-new-york-all/410637/
- https://nyassembly.gov/leg/?default_fld=&leg_video=&bn=A03506&term=2025&Actions=Y -> https://web.archive.org/web/20261008161832/https://nyassembly.gov/leg/?default_fld=&leg_video=&bn=A03506&term=2025&Actions=Y
- https://nyassembly.gov/leg/?default_fld=&leg_video=&bn=S01747&term=2019&Actions=Y -> https://web.archive.org/web/20261008161921/https://nyassembly.gov/leg/?default_fld=&leg_video=&bn=S01747&term=2019&Actions=Y
- https://www.foxnews.com/us/illegal-immigrant-accused-killing-chicago-college-student-face-court-after-tuberculosis-delay -> https://web.archive.org/web/20260507204923/https://www.foxnews.com/us/illegal-immigrant-accused-killing-chicago-college-student-face-court-after-tuberculosis-delay

Not captured / unconfirmed:
- https://archive.org/details/FOXNEWSW_20261005_040000_Sunday_Night_in_America_With_Trey_Gowdy (Wayback playback 403; archive.org does not archive itself. The item listing JSON/HTML is retained locally instead.)
- https://www.foxnews.com/media/cnn-ms-now-avoid-covering-loyola-student-sheridan-gorman-murdered-illegal-immigrant-in-chicago (background only; not submitted)
- https://wlsam.com/2026/10/07/accused-gunman-in-sheridan-gorman-murder-in-court (not submitted; retained locally)
- https://www.weny.com/... Local Cops article (not submitted; retained locally)
- https://www.foxnews.com/video/6406230109112 clip media itself: not archivable via Wayback; the MP4 and whisper transcript are retained locally.

## Additional file added after the first draft
| File | Source | What it establishes |
|---|---|---|
| archive-org-FOXNEWSW_20261005_040000-full-episode-whisper-transcript.srt | https://archive.org/details/FOXNEWSW_20261005_040000_Sunday_Night_in_America_With_Trey_Gowdy (audio pulled via the clip endpoint in 61 one-minute segments) | Whisper transcript of the full hour. Gorman segment runs ~00:06:26 to ~00:13:00. "Hochul" (rendered "Hochl") appears once, at ~00:51:23, in a separate segment about the Cornell rape case / AG Letitia James, not in the Gorman interview. |
| wlsam-2026-10-07-medina-court.txt | https://wlsam.com/2026/10/07/accused-gunman-in-sheridan-gorman-murder-in-court | Re-extracted article body: Oct 7, 2026 status hearing; "also had an outstanding warrant in a Chicago shoplifting case." |

## Key findings (pointers into the retained text; see the handback report for the full table)
- Hochul EO No. 1 (Aug 24, 2021) is a blanket, time-limited continuation of all prior governors' orders ("shall remain in full force and effect until October 8, 2021"). It names no order and says nothing about immigration or sanctuary. (governor-ny-eo-1-2021-08-24.txt)
- Cuomo EO 170 was continued by name in Hochul EO No. 6 (Oct 8, 2021), item III(t); EO 170.1 was continued by Hochul EO No. 6.1 (Jan 16, 2025). (governor-ny-eo-6-2021-10-08.txt line 161; governor-ny-eo-6.1-2025-01-16.txt)
- EO 170 binds "State entities" (executive agencies and gubernatorially controlled authorities): no inquiry into immigration status except for eligibility or as required by law; no disclosure to federal immigration authorities for civil enforcement unless required by law; state law-enforcement officers may not use resources to apprehend people wanted only for civil immigration violations. It does not bind county/municipal police or jails and does not use the word "sanctuary." (cuomo-eo-170-2017-09-15.ocr.txt; hcr-ny-2017-09-15-cuomo-eo170-press-release.txt)
- No NY statute declares a "sanctuary state." The New York for All Act (S2235B/A3506B) has sat in committee since Jan 2025 (nyassembly-A03506-2025-new-york-for-all-actions.txt). The Green Light Law was signed June 17, 2019 (chap. 37) under Cuomo (nyassembly-S01747-2019-green-light-actions.txt). The Local Cops, Local Crimes Act (287(g) ban) was signed May 2026 and took effect Aug 25, 2026, after the Gorman killing (governor-ny-2026-08-25-local-cops-local-crimes-287g-ban.txt).
- Sheridan Gorman, 18, of Yorktown Heights (Westchester County), was shot and killed in Chicago on March 19, 2026. The accused, Jose Medina-Medina, a Venezuelan national, was apprehended by Border Patrol May 9, 2023 and released (DHS); House Judiciary GOP excerpts say he was "processed for a Notice to Appear and released on recognizance ... due to lack of space" in the El Paso sector; he was arrested for shoplifting in Chicago in June 2023, released, and had an outstanding warrant for failure to appear. No retained source places him in New York or in New York custody at any time. (dhs-2026-03-22-ice-asks-pritzker.txt; foxnews-biden-border-released-lack-of-space.txt; abc7chicago-medina-charged.txt)
- The Fox clip (6:43) never names Hochul. Tom Gorman attributes "wide open" borders to "the Biden administration," says Chicago's sanctuary policies left the accused free, and adds "New York has doubled down on these sanctuary policies." Gowdy's intro says the accused "then committed other offenses" (matches the caption fragment in Langworthy's post). (foxnews-video-6406230109112-whisper-transcript.srt)
