# Wayback archive status (verified by playback, 2026-10-19)

Playback test: fetch snapshot, require HTTP 200 and the listed needle text in the body. Availability API not used as evidence.

| key | original | snapshot | playback | needle found |
|---|---|---|---|---|
| wh-eo | https://www.whitehouse.gov/presidential-actions/2026/10/implementing-the-lindsey-o-graham-sanctioning-russia-and-iran-act-of-2026/ | https://web.archive.org/web/20261019151646/https://www.whitehouse.gov/presidential-actions/2026/10/implementing-the-lindsey-o-graham-sanctioning-russia-and-iran-act-of-2026/ | 200 | yes (`Section 115 of the Graham Act`) |
| ofac-gl135 | https://ofac.treasury.gov/media/937216/download | https://web.archive.org/web/20261013134703/https://ofac.treasury.gov/media/937216/download | 200 | yes (`GENERAL LICENSE NO. 135`) |
| reuters-usnews | https://www.usnews.com/news/world/articles/2026-10-15/exclusive-order-to-limit-starshield-for-ukraine-came-from-inside-white-house-sources-say | https://web.archive.org/web/2026/https://www.usnews.com/news/world/articles/2026-10-15/exclusive-order-to-limit-starshield-for-ukraine-came-from-inside-white-house-sources-say | 404 | NO (`No such request`) |
| cnn-waiver | https://www.cnn.com/2026/10/16/europe/us-ukraine-russia-sanctions-intl-hnk | https://web.archive.org/web/20261019184612/https://www.cnn.com/2026/10/16/europe/us-ukraine-russia-sanctions-intl-hnk | 200 | yes (`national interests of the United States`) |
| abc-waiver | https://abcnews.com/Politics/trump-signs-order-waiving-graham-act-sanctions-russia/story?id=137341529 | https://web.archive.org/web/20261019151643/https://abcnews.com/Politics/trump-signs-order-waiving-graham-act-sanctions-russia/story?id=137341529 | 200 | yes (`every operative section`) |
| cnn-starshield | https://www.cnn.com/2026/10/16/politics/ukraine-trump-russia-starlink | https://web.archive.org/web/20261019184750/https://www.cnn.com/2026/10/16/politics/ukraine-trump-russia-starlink | 200 | yes (`it wasn’t me`) |
| kyivpost-rubio | https://www.kyivpost.com/post/87400 | https://web.archive.org/web/20261019184913/https://www.kyivpost.com/post/87400 | 200 | NO (`categorically false`) |
| mediaite-telegraph | https://www.mediaite.com/media/news/musk-pitched-cuts-to-ukraines-starshield-direct-to-trump-who-then-agreed-report/ | https://web.archive.org/web/20261019185110/https://www.mediaite.com/media/news/musk-pitched-cuts-to-ukraines-starshield-direct-to-trump-who-then-agreed-report/ | 200 | yes (`agreed`) |
| yougov-54596 | https://yougov.com/en-us/articles/54596-support-military-aid-ukraine-higher-than-military-aid-israel-april-17-20-2026-economist-yougov-poll | https://web.archive.org/web/20261019185255/https://yougov.com/en-us/articles/54596-support-military-aid-ukraine-higher-than-military-aid-israel-april-17-20-2026-economist-yougov-poll | 200 | yes (`62% of Americans sympathize more with Ukraine`) |
| yougov-daily | https://yougov.com/en-us/daily-results/20261014-00d1b-1 | https://web.archive.org/web/20261019185327/https://yougov.com/en-us/daily-results/20261014-00d1b-1 | 200 | yes (`5531`) |
| kyivpost-pos | https://www.kyivpost.com/analysis/80717 | https://web.archive.org/web/20261019185442/https://www.kyivpost.com/analysis/80717 | 200 | yes (`Public Opinion Strategies`) |
| langworthy-pr | https://langworthy.house.gov/media/press-releases | https://web.archive.org/web/20261019185637/https://langworthy.house.gov/media/press-releases | 200 | yes (`Chemung County Sewer`) |

## Failures / notes
- **reuters-usnews:** Save Page Now returned no capture on the first pass and HTTP 523 on the retry (2026-10-19). There is **no verified snapshot**. Retry later. The local retained text is `raw/reuters-usnews-starshield.txt` (Browser pane).
- **kyivpost-rubio:** the snapshot returns 200 but is a 23 KB shell page with no article text (no "Rubio" or "Starshield"). Treat it as **not archived**. Retry, or try archive.today. The local retained text is `raw/kyivpost-rubio.txt` (curl, 2026-10-19).
- **ofac-gl135:** the verified snapshot is a pre-existing capture from 2026-10-13. Its content matches.
- Not attempted: Telegraph (blocked to us), AP and Reuters direct pages (blocked), NBC/Hill/RFE-RL/CNBC/Moscow Times/Newsweek/Pew/Chicago Council (secondary; local copies are in `raw/`).
