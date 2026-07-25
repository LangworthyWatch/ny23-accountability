---
title: "AIPAC and Langworthy: What the Records Actually Show"
date: 2026-07-25
draft: true
hold_reason: "Two items before publish. (1) Send the standard request for comment to Langworthy's office on the trip sponsorship and the bundled contributions, and record the response or the non-response. (2) Run scripts/archive_sources.sh; the Clerk gift-travel PDF and the FEC API queries need Wayback captures. Also decide whether to update content/campaign-finance/_index.md, whose OpenSecrets-sourced AIPAC figure is roughly a third of the primary-source total documented here."
topic: "Campaign Finance"
claim_date: "2022–2026"
source: "FEC OpenFEC API, House Clerk roll calls, GPO BILLSTATUS, House Clerk Gift Travel Filings"
source_url: "https://www.fec.gov/data/candidate/H2NY23133/"
archived_url: ""
archive_note: "All sources are live at stable institutional URLs (api.open.fec.gov, clerk.house.gov, govinfo.gov, disclosures-clerk.house.gov). Wayback captures pending via scripts/archive_sources.sh before publication."
verdict: "DOCUMENTED PATTERN"
tags: ["campaign-finance", "fec", "israel", "aipac", "foreign-policy", "rules-committee", "gift-travel", "pattern"]
counties: ["district-wide"]
---

## Why This Matters for NY-23

Questions about AIPAC and Rep. Langworthy come up constantly, and most of what circulates is a mix of things that are true, things that are overstated, and one thing that is simply false.

So we pulled the primary records: every AIPAC disbursement to his committees from the FEC's own database, every relevant roll call from the House Clerk, the sponsor rosters from the Government Publishing Office, and his sponsored-travel filing from the House Clerk's gift-travel database.

Here is what we found, including the parts that cut against the loudest version of the story.

**Nothing documented here is illegal, and nothing here is an accusation.** Contributions from advocacy groups, bundled fundraising, and Ethics-approved sponsored travel are all lawful and routine. What follows is the record.

---

## Claim 1: "AIPAC's super PAC spent money to get him elected."

### Verdict: FALSE

AIPAC's super PAC is the United Democracy Project. It spent heavily in 2024 congressional races and is the source of most of AIPAC's national reputation for electoral muscle.

It has never spent a dollar on Langworthy's race.

We queried the FEC's independent-expenditure database for his candidate ID (H2NY23133). The result is **zero** — not zero from UDP, but **zero independent expenditures for or against Nick Langworthy from any committee, in any cycle, ever.** No outside group has run so much as a mailer.

If you have seen the claim that UDP bought this seat, it is checkable, and it is wrong.

*Source: FEC OpenFEC API, Schedule E, candidate H2NY23133.*

---

## Claim 2: "AIPAC is one of his biggest donors."

### Verdict: MISSING CONTEXT

This one is more interesting than either side of the argument usually allows, because **AIPAC moves money to candidates two different ways**, and they are not the same thing.

**Way one: the PAC writes a check.** AIPAC's own political action committee has given Langworthy's campaign **$25,000** total, in five $5,000 contributions:

| Cycle | Amount |
|---|---|
| 2022 | $10,000 |
| 2024 | $10,000 |
| 2025 | $5,000 |
| **Total** | **$25,000** |

By itself that is unremarkable. At least 23 other organizations have given him exactly $10,000 through their PACs, including UnitedHealth Group, Koch Inc., the American Hospital Association, and several pilots' unions.

**Way two: AIPAC bundles.** AIPAC also acts as a *conduit* — individual donors write checks that AIPAC collects and forwards, and the money is credited to the individuals rather than to AIPAC. This is where the real volume is: **$76,016** across **75 individual contributions.**

| Channel | Amount |
|---|---|
| Direct AIPAC PAC contributions | $25,000 |
| Bundled through AIPAC as conduit | $76,016 |
| **Total routed via AIPAC** | **$101,016** |

Separately, **NorPAC**, an unaffiliated pro-Israel PAC, bundled **$17,249** to him and gave **$0** directly.

**In plain language:** the check AIPAC writes is ordinary-sized. The money AIPAC *organizes* is about four times larger. Most people arguing about this are arguing about the wrong number.

**How big is that in context?** Across all cycles, money arriving through AIPAC's conduit equals about **3.6%** of the itemized individual contributions to his campaign committee. It is a meaningful share, and it is growing:

| Cycle | Itemized individual $ | Via AIPAC | Share |
|---|---|---|---|
| 2022 | $549,666 | $9,500 | 1.7% |
| 2024 | $818,296 | $34,118 | 4.2% |
| 2026 (partial) | $572,975 | $25,500 | 4.5% |

The bundled contributions are individually modest — median **$1,000**, and only two of the 75 hit the individual maximum. The donors cluster in Nassau County, the Syracuse suburbs, Manhattan, and South Florida. **We are not publishing their names.** They are private citizens making small legal contributions, and naming them would serve no accountability purpose.

*Sources: FEC OpenFEC API, Schedule B disbursements for committee C00797670 (all 84 records) and C00247403; FEC bulk individual-contribution files for committee C00817932.*

**A note on two different totals.** AIPAC's own filings say it routed $76,016 in bundled money. The campaign's filings show $69,118 carrying AIPAC's conduit identifier. The roughly $6,900 gap is three 2024-cycle contributions the campaign itemized without the conduit ID attached, plus contributions too small to require itemization. We report AIPAC's own accounting and disclose the campaign-side figure rather than quietly choosing the larger number.

---

## Claim 3: "He took an AIPAC-funded trip to Israel."

### Verdict: TRUE

From **April 1 to April 8, 2024**, Langworthy traveled Buffalo–Israel–Buffalo on a trip sponsored by the **American Israel Education Foundation (AIEF)**, AIPAC's affiliated charitable foundation, which sponsors congressional travel to Israel.

**Cost to the sponsor: $15,900.02** for Langworthy alone.

| Category | Amount |
|---|---|
| Transportation | $9,112.31 |
| Lodging | $2,340.97 |
| Meals | $1,436.31 |
| Other | $3,010.43 |
| **Total** | **$15,900.02** |

The stated purpose was to meet "the Israeli President, Prime Minister, and other government officials." The delegation was billed as Republican freshmen members of Congress, 16 in total. The itinerary included Nir Oz and the Nova festival site.

**He disclosed it properly.** The trip appears on his House Clerk gift-travel filing (signed April 22, 2024) and again on his CY2024 annual financial disclosure. This is a legal, pre-approved, disclosed trip, and we are documenting it, not alleging anything about it.

**He has talked about the trip publicly. He has never said who paid for it.**

On the House floor on April 10, 2024, two days after returning, he described it directly:

> "Last week, I had the honor to travel to Israel and while in Jerusalem, I, with my colleagues, met with the Goldberg-Polin family, Rachel and Jon Goldberg-Polin, whose son, Hersh, an American citizen, was taken hostage at the Nova Music Festival."

He referenced it again on February 19, 2025, saying he "had the somber privilege of traveling to Israel and visiting Kibbutz Nir Oz."

**Neither time did he name the sponsor.** He issued no press release about the trip. We reviewed all **436 press releases** in his House archive from January 2023 through July 2026: the words "AIPAC" and "American Israel" appear in **none** of them.

**It was also not his first visit.** In floor remarks on November 2, 2023 — five months before this trip — he said: "I have been there. Many of us have been there. We all should go there." We found no earlier travel disclosure and are not asserting when that visit occurred.

**Also on the financial disclosures:** an "Israel Bond" asset appears on all four of his annual House filings (CY2022 through CY2025), valued each year at **$1–$1,000**, income "None." We note it for completeness; at that value it is a token holding, not an investment position.

*Sources: House Clerk Gift Travel Filing 500028161; CY2024 House Financial Disclosure, document 10068912.*

---

## Claim 4: "He just votes the way every Republican votes on Israel."

### Verdict: MISSING CONTEXT

This understates what he did, and it is the most substantive finding here.

**He did not merely vote. He wrote the rule.**

On May 15, 2024, Langworthy personally sponsored **H.Res. 1227**, the House Rules Committee resolution governing floor consideration of **H.R. 8369, the Israel Security Assistance Support Act** — a bill to force the release of arms shipments the Biden administration had paused. He reported the resolution from the Rules Committee, called it up on the floor by direction of the committee, and served as its floor manager.

It was a **closed rule**: no amendments permitted.

He then voted for the previous question (212–201) and for his own rule (212–200), and voted Yes on the underlying bill the next day (224–187).

Sponsorship of a rule is not a party-line vote. It is agenda-setting — deciding what reaches the floor and in what form. We verified the sponsorship directly against the Government Publishing Office's official bill-status record for H.Res. 1227.

**One thing we are not attributing to him:** H.Res. 1160, the rule for the April 2024 supplemental package, was sponsored by Rep. Burgess, not Langworthy.

### The voting record

**The same-day contrast.** On April 20, 2024, the House voted separately on aid to Israel and aid to Ukraine. We pulled both roll calls from the House Clerk:

| Roll call | Bill | His vote | Result |
|---|---|---|---|
| 2024-152 | Israel Security Supplemental Appropriations Act | **Yea** | Passed 366–58 |
| 2024-151 | Ukraine Security Supplemental Appropriations Act | **Nay** | Passed 311–112 |

**Israel aid:** Yes on H.R. 6126 (Nov. 2023), H.R. 7217 (Feb. 2024), H.R. 8034 (Apr. 2024), H.R. 8369 (May 2024).

**War powers:** He voted **No on all six** resolutions that would have required congressional authorization for hostilities against Iran, and No on both Lebanon war-powers resolutions. Two of the Iran resolutions passed over his opposition (215–208 and 214–208).

**Cosponsorships:** 49 confirmed Israel-related cosponsorships across the 118th and 119th Congresses, 23 of them as an original cosponsor, **none withdrawn.** Verified against the official GPO cosponsor rosters, not aggregators.

*Sources: clerk.house.gov roll-call XML; GPO BILLSTATUS bulk data; Congressional Record Vol. 170 No. 84 (May 15, 2024).*

---

## What the Record Does Not Show

*This section exists because the absence of evidence is part of the record, and leaving it out would let readers assume things we cannot document.*

- **No targeted abstention on antisemitism legislation.** He was recorded Not Voting on H.R. 6090, the Antisemitism Awareness Act, on May 1, 2024. We pulled every 2024 roll call from the House Clerk and matched his vote to each one. He missed **all five** votes held on May 1, and every vote on the two session days before it (April 29 and April 30, the latter a 17-vote day). Those absences sit inside a documented spring 2024 stretch in which he missed 35 votes, six of them complete-day absences. It was an absence, not an abstention, and describing it otherwise would be misleading. He was later an **original cosponsor** of the identical 2025 bill, H.R. 1007. Full day-by-day breakdown: [Missed Votes](/missed-votes/).
- **The trip did not cost him any votes either.** The House held no roll call votes between March 22 and April 9, 2024. The April 1–8 trip fell entirely inside a non-voting period.
- **No documented local pressure on this issue.** We searched NY-23 and Buffalo-market outlets for town-hall confrontations, protests, petitions, or open letters about his Israel positions or AIPAC funding. Documented protest activity at his district offices exists, but it concerns Medicaid, Social Security, DOGE, and town-hall access. We found none about Israel.
- **No statement from him about AIPAC.** We reviewed all 436 press releases in his archive. None mentions AIPAC, AIEF, or contributions from pro-Israel groups. He has never publicly addressed the trip's sponsorship.
- **No quid pro quo, and no evidence of one.** Nothing in these records shows a contribution exchanged for a vote, or any communication between AIPAC and his office about any bill.

---

## Verdict: DOCUMENTED PATTERN

The alignment is real and it is documented: **$101,016** routed through AIPAC to his campaign, a **$15,900** AIPAC-affiliate-funded trip to Israel, **49** cosponsorships, consistent Yes votes on Israel aid alongside a No vote on Ukraine aid the same day, No votes on all eight Iran and Lebanon war-powers resolutions, and a **closed rule he personally wrote and floor-managed** to force through an Israel arms bill.

At the same time, two of the loudest claims do not survive contact with the records: **no super PAC has ever spent a dollar on his race**, and AIPAC's direct PAC contribution is an ordinary $25,000 that dozens of other industries match.

The accurate summary is narrower and more durable than the viral one: this is a member whose Israel-related record is unusually active for a backbench freshman, who has taken money organized by AIPAC and travel funded by its affiliate, and who has never been asked about it publicly.

---

## Related Entries

- [The Disclosure Gap: Donations, Legislation, and What the Announcements Leave Out](/fact-checks/2026-06-24-disclosure-gap-donor-pattern/) — the broader donor-to-vote series
- [Rules Committee Gatekeeper Pattern](/fact-checks/2026-07-16-rules-committee-gatekeeper-pattern/) — how he uses the Rules seat
- [Disclosure Asymmetry: Schedule H vs. Gift Travel](/fact-checks/2026-05-04-disclosure-asymmetry-schedule-h-vs-gift-travel/) — the AIEF trip in the context of his travel filings
- [Campaign Finance Overview](/campaign-finance/) — note that page's AIPAC figure is OpenSecrets-sourced and scoped to one cycle

---

## Sources

- FEC OpenFEC API, Schedule B, committee C00797670 (AIPAC PAC): <https://api.open.fec.gov/v1/schedules/schedule_b/>
- FEC OpenFEC API, Schedule E (independent expenditures), candidate H2NY23133
- House Clerk, Roll Call 151, Apr. 20, 2024: <https://clerk.house.gov/Votes/2024151>
- House Clerk, Roll Call 152, Apr. 20, 2024: <https://clerk.house.gov/Votes/2024152>
- GPO BILLSTATUS, H.Res. 1227 (118th): <https://www.govinfo.gov/bulkdata/BILLSTATUS/118/hres/BILLSTATUS-118hres1227.xml>
- House Clerk Gift Travel Filing 500028161: <https://disclosures-clerk.house.gov/gtimages/MT/2024/500028161.pdf>
- Congressional Record, Vol. 169 No. 181, p. H5237 (Nov. 2, 2023)
- Congressional Record, Vol. 170 No. 84, p. H3220 (May 15, 2024)

---

*All data from public primary sources. Sponsored travel is legal and pre-approved by the House Ethics Committee; contributions and bundling are legal and routine. This entry documents the record, not wrongdoing. Methodology available on request.*
