# Dairy / DMC triage sources (retained 2026-10-08)

Claim under review: Langworthy official FB post, Oct 7, 2026 ("My Dairy Farm Resiliency Act strengthened the Dairy Margin Coverage program. It protects up to 6 million pounds of milk when prices drop or feed costs soar"), linking the Oct 2, 2026 press release.

All files fetched with `curl -sL -A "Mozilla/5.0"` on 2026-10-08 unless noted. `.txt` files are plain-text extractions of the matching `.html` with the source URL at top.

## Retained files

| File | Source URL | Notes |
|---|---|---|
| langworthy-pr-2026-10-02-dairy-dmc.html/.txt | https://langworthy.house.gov/media/press-releases/congressman-langworthy-highlights-expanded-dairy-safety-net-2027-dairy-margin | Oct 2, 2026 press release linked by the FB post |
| press-releases-index.html | https://langworthy.house.gov/media/press-releases | index page used to find the exact URL |
| langworthy-pr-2025-01-critical-legislation-119th.html/.txt | https://langworthy.house.gov/media/press-releases/congressman-nick-langworthy-introduces-critical-legislation-119th-congress | Jan 10, 2025 release introducing H.R. 294 et al.; his own description of DFRA |
| lw-pr-index-p38.html, lw-pr-index-p39.html | https://langworthy.house.gov/media/press-releases?page=38 / ?page=39 | press index covering ~May 24-Jul 14, 2023; no DFRA release (H.R. 4125 was Molinaro's bill) |
| BILLSTATUS-119hr294.xml | https://www.govinfo.gov/bulkdata/BILLSTATUS/119/hr/BILLSTATUS-119hr294.xml | H.R. 294 status (cosponsors parsed from cosponsors/item) |
| BILLS-119hr294ih.htm | https://www.govinfo.gov/content/pkg/BILLS-119hr294ih/html/BILLS-119hr294ih.htm | H.R. 294 introduced text (only text version) |
| BILLSTATUS-118hr4125.xml | https://www.govinfo.gov/bulkdata/BILLSTATUS/118/hr/BILLSTATUS-118hr4125.xml | 118th Congress DFRA, sponsor Molinaro; found by scanning BILLSTATUS 118 hr3950-4250 titles |
| BILLS-118hr4125ih.htm | https://www.govinfo.gov/content/pkg/BILLS-118hr4125ih/html/BILLS-118hr4125ih.htm | H.R. 4125 text (identical operative text to H.R. 294) |
| BILLSTATUS-118hr8467.xml | https://www.govinfo.gov/bulkdata/BILLSTATUS/118/hr/BILLSTATUS-118hr8467.xml | 2024 House farm bill (Thompson); ordered reported 33-21 on 2024-05-24; only "ih" text version exists on govinfo |
| BILLS-118hr8467ih.htm, hr8467-sec1401-dmc-excerpt.txt | https://www.govinfo.gov/content/pkg/BILLS-118hr8467ih/html/BILLS-118hr8467ih.htm | Secs. 1401-1402 (DMC production history 2021-2023; Tier I/II 6,000,000) |
| BILLS-119hr1enr.htm, obbba-sec-dairy-margin-coverage-excerpt.txt | https://www.govinfo.gov/content/pkg/BILLS-119hr1enr/html/BILLS-119hr1enr.htm | Enrolled OBBBA (P.L. 119-21); Sec. 10313 Dairy policy updates |
| BILLSTATUS-119hr1.xml | https://www.govinfo.gov/bulkdata/BILLSTATUS/119/hr/BILLSTATUS-119hr1.xml | H.R. 1 status; relatedBills (29) do not include H.R. 294 |
| clerk-roll145-2025.xml, clerk-roll190-2025.xml | https://clerk.house.gov/evs/2025/roll145.xml ; .../roll190.xml | Langworthy Yea (May 22, 2025) and Aye (Jul 3, 2025) on H.R. 1 |
| fsa-2026-09-30-dmc-2027-enrollment.html/.txt | https://www.fsa.usda.gov/news-events/news/09-30-2026/usda-announces-2027-dairy-margin-coverage-enrollment | USDA FSA release, Sept 30, 2026 |
| fsa-dmc-program-page.html, fsa-news-index.html | https://www.fsa.usda.gov/resources/income-support/dairy-margin-coverage-program-dmc ; https://www.fsa.usda.gov/news-events/news | used to locate the release |
| houseag-news-2025-p5.html | https://agriculture.house.gov/news/documentquery.aspx?Year=2025&Page=5 | listing of May 2025 reconciliation releases |
| houseag-doc7911/7912/7913/7915.html/.txt | https://agriculture.house.gov/news/documentsingle.aspx?DocumentID=7911 (May 12, 2025 text release), 7912 (May 13 markup opening statement), 7913 (May 14 passage statement), 7915 (May 21 stakeholder praise) | Committee's own messaging; 7915 carries NMPF quote on DMC |
| houseag-victories-in-hr1.html/.txt | https://agriculture.house.gov/hr1/ | Committee's H.R. 1 page; no DMC mention |
| nmpf-lauds-house-ag-reconciliation-wayback.html, nmpf-2025-05-14-lauds-house-ag-reconciliation.txt | https://www.nmpf.org/nmpf-lauds-dairy-policy-provisions-in-house-ag-reconciliation-package/ | nmpf.org returns 403 to curl and WebFetch; retrieved via Wayback playback (web.archive.org/web/2025id_/...) |
| midwestfarmreport-2023-06-17-dfra-introduced.html | https://www.midwestfarmreport.com/2023/06/17/dairy-farm-resiliency-act-introduced/ | June 2023 coverage of H.R. 4125 (FarmFirst statement) |
| spectrumnews-2024-05-15-house-farm-bill-dairy.html/.txt | https://spectrumnews1.com/wi/milwaukee/news/2024/05/15/house-farm-bill-dairy | Van Orden framed as cosponsor of the 6M-lb change in the 2024 House farm bill |
| wfbf-obbba-dairy-priorities.html/.txt | https://www.thefarmwi.com/one-big-beautiful-bill-includes-key-dairy-priorities/ | Edge/WI Farm Bureau list of OBBBA dairy provisions |
| dairyherd-obbba-dairy.html/.txt | https://www.dairyherd.com/news/policy/one-big-beautiful-bill-passes-what-does-it-mean-dairy-farmers | July 8, 2025 trade-press explainer |
| wayback-save-log.txt | - | raw output of `curl -s -I https://web.archive.org/save/URL` attempts |

Not retained (blocked): brownfieldagnews.com (Cloudflare 403 on two URLs); congress.gov search (403). BILLSTATUS-118hr5986 was checked and discarded (unrelated bill).

## Wayback status (verified by playback of https://web.archive.org/web/2026id_/URL, 2026-10-08; see wayback-save-log.txt and wayback-playback-check.txt)

Save requests were heavily rate-limited (429s / silent responses / connection refusals). Playback is the test, not the save response.

| URL | Snapshot (playback 200) |
|---|---|
| langworthy.house.gov ... expanded-dairy-safety-net-2027-dairy-margin | https://web.archive.org/web/20261008155908/ (new today) |
| langworthy.house.gov ... introduces-critical-legislation-119th-congress | https://web.archive.org/web/20260210174019/ (pre-existing) |
| BILLSTATUS-119hr294.xml | https://web.archive.org/web/20261008160022/ (new; playback resolved to 20260705032826) |
| BILLS-119hr294ih.htm | https://web.archive.org/web/20261008160142/ (new) |
| BILLSTATUS-118hr4125.xml | https://web.archive.org/web/20261008160423/ (new) |
| BILLS-118hr4125ih.htm | https://web.archive.org/web/20260713115734/ (pre-existing) |
| BILLS-118hr8467ih.htm | https://web.archive.org/web/20261008160601/ (new) |
| BILLS-119hr1enr.htm | https://web.archive.org/web/20260929195846/ (pre-existing) |
| FSA 2027 DMC enrollment release | https://web.archive.org/web/20261008160420/ (new) |
| clerk roll145.xml / roll190.xml | 20260907160954 / 20260926053642 (pre-existing) |
| agriculture.house.gov DocumentID=7911 / 7913 / 7915 | 20260218182907 / 20261008160536 (new) / 20260616183055 |
| nmpf.org lauds-dairy-policy-provisions | https://web.archive.org/web/20260515164221/ (pre-existing; the May 2025 playback used for retention also exists) |
| thefarmwi.com OBBBA dairy priorities | 20260509142247 (pre-existing) |
| dairyherd.com OBBBA explainer | 20250724135703 (pre-existing) |
| spectrumnews1.com 2024-05-15 house-farm-bill-dairy | 20250720131027 (pre-existing) |
| midwestfarmreport.com 2023-06-17 | NO SNAPSHOT (Wayback 404; save requests returned nothing). Local copy retained only. |
| BILLSTATUS-119hr1.xml, BILLSTATUS-118hr8467.xml, agriculture.house.gov/hr1/, FSA DMC program page | not save-requested / not verified |
