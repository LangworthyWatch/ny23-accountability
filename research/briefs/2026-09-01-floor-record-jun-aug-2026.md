---
record_type: research_brief
slug: langworthy-floor-record-jun-aug-2026
status: complete_primary_sourced
audit_tier_current: 1
subject:
  name: Nick Langworthy
  role: U.S. Representative, NY-23
window:
  start: 2026-06-01
  end: 2026-09-01
  record_coverage_through: 2026-08-27   # last CREC issue published as of 2026-09-01
method: exhaustive_full_text_congressional_record
compiled: 2026-09-01
---

# Floor record, June 1 – September 1, 2026

## Method (and why it is not the govinfo search API)

Every Congressional Record issue in the window — **45 issues, CREC-2026-06-01 through
CREC-2026-08-27** — was downloaded as the complete daily issue PDF from govinfo
(`https://www.govinfo.gov/content/pkg/CREC-YYYY-MM-DD/pdf/CREC-YYYY-MM-DD.pdf`, keyless),
converted to text, and scanned for every `Mr. LANGWORTHY.` speaker mark. 46 marks were
found and each was classified by hand.

**The govinfo search API was tried first and is incomplete — do not rely on it alone.**
A search for `collection:CREC AND "Langworthy"` over the window returned 64 granules.
An exhaustive granule-by-granule audit of a single day (2026-07-21, all 102 House
granules fetched and grepped) found **7 granules naming him that the search returned
zero of**. Across the window the search missed **three Extensions of Remarks entirely**
(Boyde 6/3, Byers 6/3, Post-Journal 7/21). The full-issue PDF sweep is the reliable method.

Denominator from GovTrack (keyless): **20 House recorded-voting days** in the window;
he cast **94 of 94 votes — no missed votes, no "present."**

---

## The finding

| | Count |
|---|---|
| House recorded-voting days in window | 20 |
| Roll-call votes cast / eligible | 94 / 94 |
| **Speeches actually delivered on the House floor** | **1** (June 9) |
| Extensions of Remarks (submitted in writing, *not* spoken) | 7 |
| Days on which he spoke on the floor | 1 of 20 |

The Record itself draws the spoken/submitted line explicitly: Extensions carry the
notice *"Matter set in this typeface indicates words inserted or appended, rather than
spoken, by a Member of the House on the floor."* Seven of his eight appearances are of
that kind. **Do not describe Extensions of Remarks as floor speeches.**

### The one floor speech — June 9, 2026, H. Res. 1345 (pages H4004–H4006)

Managing the rule for the Committee on Rules. 12 speaking turns, ~2,964 words, of which
~2,600 are substantive (the rest are yielding time). Verbatim text saved to
`research/sources/crec-2026-06-09-hres1345-langworthy-floor.txt`.

H. Res. 1345 was a **closed rule** covering four measures — H.R. 8312 (Fraud Prevention
and Accountability Act), H.R. 8464 (Stopping Fraudulent Payments Act), H. Res. 1335
(condemning fraud), and **S. 2 (Secure America Act)**, the CBP/ICE funding
reconciliation bill. Roughly half his floor time was spent on immigration and border
enforcement rather than the fraud bills the rule was named for.

He also **moved the previous question**, which is what foreclosed the minority's
alternative: Ms. Scanlon's amendment would have made in order a Raskin amendment barring
DOJ from using taxpayer funds for settlement payments to individuals convicted of
assaulting police officers on January 6, 2021. That amendment text is printed in the
Record inside his own final turn.

### The seven Extensions of Remarks (submitted, not spoken)

| Date | Subject | County |
|---|---|---|
| 2026-06-03 | Timothy T. Boyde, retiring County Administrator | Allegany |
| 2026-06-03 | Maj. Andrew D. Byers, KIA Kunduz 2016, road dedication | Erie (Clarence) |
| 2026-06-09 | Corning Incorporated, 175th anniversary | Steuben |
| 2026-06-10 | Ric Dimpfl, 75th birthday, volunteer fire service | Erie (Hamburg) |
| 2026-06-23 | Town of Hornby bicentennial | Steuben |
| 2026-06-25 | Watkins Glen International, America 250 | Schuyler |
| 2026-07-21 | The Post-Journal (Jamestown), 200 years | Chautauqua |

All seven are ceremonial. **None** addresses a policy matter, a vote, or a constituent
concern. Six of the eight NY-23 counties appear; Cattaraugus and Tioga do not.

---

## Follow-up candidates (ranked; none verified beyond what is stated)

**1. Sequel to the Rules Committee gatekeeper entry — strongest.**
`/fact-checks/2026-07-16-rules-committee-gatekeeper-pattern/` documents how he *votes* in
committee on closed rules. June 9 is the same behavior in his **own words on the floor**,
defending a closed rule on four measures and moving the previous question to block the
Jan. 6 settlement-funds amendment. Primary text is already in hand. This is an update to
the existing entry, not a new entry.

**2. "No new laws have been passed. We are enforcing the laws on the books."**
Verified against primary source: he voted **Yea** on the Laken Riley Act (House Clerk
roll call 23, Jan. 22, 2025 — `https://clerk.house.gov/evs/2025/roll023.xml`), which
became **P.L. 119-1** on Jan. 29, 2025. He invokes Laken Riley's parents by name later in
the same speech. **Fair counterpoint that must be carried:** the Laken Riley Act governs
detention/removal of aliens charged with certain crimes, not border-crossing authority,
so he may mean no new *border* statute. Frame narrowly or not at all — do not run this as
a flat "false."

**3. "In April, southern border apprehensions were 94 percent lower than the monthly
average experienced under the Biden administration."** Tier-B as it stands. Needs a CBP
primary pull (which April; which Biden months form the "monthly average"; apprehensions
vs. encounters — he uses both words in the same passage). Do not publish the number
without pinning the denominator.

**4. Cattaraugus County stabbing.** *"Just last week, a violent stabbing occurred in
Cattaraugus County involving an illegal immigrant"* — with Cattaraugus Sheriff/ICE Buffalo
cooperation. Unverified. Relates to
`/fact-checks/2026-04-10-immigration-crime-victims-list/`, where a prior victims list
included a case with no murder charge filed. Verify before use; name no individual.

**5. Corning ER vs. the OBBBA manufacturing-credit entry.** The 6/9 Extension praises
Corning as "the beating heart of the Southern Tier's economy" nine days before
`/fact-checks/2026-05-29-corning-manufacturing-credits-obbba/`'s subject matter. Possible
"praise vs. vote" pairing — low priority, and the fairness standard applies: Corning is
not endorsing him by being praised.

**6. Volume itself.** One floor speech across 20 session days, alongside 100% vote
attendance, is a documentable fact but a weak entry on its own — floor time is allocated
by leadership, and low floor volume is unremarkable for a rank-and-file member. Publish
only as context inside another entry, never as a standalone "he never speaks" claim.

---

## Caveats

- Record coverage ends **2026-08-27**. The House voted **2026-08-31** (2 roll calls, both
  Yea); that issue was not yet published as of 2026-09-01. Re-run for that day before
  citing the window as closed.
- This brief covers the **floor** record only. Committee statements (Rules, and the
  6/24 critical-minerals hearing already in `research/transcripts/`) are separate.
- August 10, 13, 17, 20, 24, 27 were pro forma; no votes, no speeches by anyone.
