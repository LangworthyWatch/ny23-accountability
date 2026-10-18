# KIDS Act (H.R. 7757): committee amendments, roll calls, status, design-features check

Research packet, 2026-10-18. Supports triage of Langworthy's Oct 16, 2026 official-page post
(`../screenshots/03-official-kids-act.png`). Does not edit `content/`.

## The post (authorship confirmed)

The screenshot shows the verified **"Congressman Nick Langworthy"** page (the official office page, `RepLangworthy`), stamped "2 days ago" when captured:

> "As a husband and father, helping pass the KIDS Act was personal. The Energy and Commerce Committee I serve on spearheaded this bill to protect children online by restricting addictive design features, strengthening privacy safeguards, empowering parents and holding Big Tech accountable."

We have no post permalink. Facebook posts are login-walled, so this one cannot be archived; the screenshot is the preservation artifact (use `archive_note`).

## 1. The six Democratic amendments (E&C full-committee markup, Mar 5, 2026, event 119031)

All six amend Chairman Guthrie's amendment in the nature of a substitute (ANS), **GUTHRI_008** (`amendments/BILLS-119-HR7757-A000370-Amdt-2.pdf`). The page and line references below are to that ANS. None of the six would have restored a KOSA duty of care in so many words. Five of them change the **knowledge standard** and/or **state preemption**. One adds a ban on forced arbitration.

The ANS baseline is Sec. 2(7): "know" means "to have actual knowledge or to have acted in willful disregard." The ANS preemption sections (106, 221, 237, 244, 304, 407) bar state laws that conflict with the Act, or (in Title I) state laws on the same subject.

| Roll call | Amendment (PDF) | What it would have done | Operative language |
|---|---|---|---|
| 1 | CASTOR_049 (`P000034-Amdt-14`) | Lowers the knowledge standard to constructive knowledge for the whole Act. Rewrites **all six** preemption sections into floor preemption, so states could pass stronger protections. | strike "or to have acted in willful disregard" and insert "or to have knowledge fairly implied on the basis of objective circumstances"; "...shall preempt any State law ... only to the extent that such State law ... conflicts with a provision of this title. Nothing in this title may be construed to prohibit any State from enacting or enforcing a law ... that provides greater protection to children or teens" |
| 2 | LANDSM_071 (`P000034-Amdt-18`) | Same knowledge change. **Strikes the rule of construction in Sec. 213(c)(2) that says the bill does not "impose a duty of care."** Applies floor preemption to the KOSA subtitle (Sec. 221). | "Page 17, line 25, strike '; or' ... Page 18, strike lines 1 through 2" (ANS p.18 lines 1-2: "(2) impose a duty of care on a provider of a covered platform.") |
| 3 | KNOW_01, Soto (`P000034-Amdt-17`) | Same knowledge change. Floor preemption for Title III (social gaming, Sec. 304). | "knowledge fairly implied on the basis of objective circumstances" |
| 4 | MATSUI_041 (`P000034-Amdt-19`) | Same knowledge change. Floor preemption for Title IV (AI chatbots, Sec. 407). | same savings-clause language |
| 5 | MULLCA_062, Mullin (`P000034-Amdt-20`) | Replaces Subtitle B (Safe Messaging for Kids, ANS pp.32-41) with a new version: parental view of DM settings; default DM controls for minors (approve/deny requests, disable DMs, block users, hidden profile); a "covered user" standard that includes knowledge "fairly implied on the basis of objective circumstances"; and floor preemption (new Sec. 235). | "shall provide a parental tool to allow a parent of a covered user to view the covered user's direct messaging control settings"; "As a default setting ... the direct messaging controls ... shall allow a covered user ... to ... Disable any direct messaging feature" |
| 6 | ARBITRATION_01, Dingell (`D000624-Amdt-13`) | Adds Title VII, which voids forced arbitration and class-action waivers for claims about minors' privacy and online safety. | "a predispute arbitration agreement or predispute joint-action waiver that relates to conduct constituting a violation of the privacy or online safety of a minor shall not be valid or enforceable." |

Related but **not** among the six roll calls: AMEND_7757 (`P000034-Amdt-12`), a knowledge change plus Sec. 237 floor preemption. No roll call was taken on it, and we have not determined its disposition.

## 2. Roll-call tallies (from the sheets, not the CSV)

I re-extracted text from the docs.house.gov PDFs (`rollcalls/`). I then counted X marks by column position and checked each count against the printed DISPOSITION line. All seven matched.

| # | Item | Yeas-Nays | Langworthy |
|---|---|---|---|
| 1 | CASTOR_049 | 24-27 | Nay |
| 2 | LANDSM_071 | 24-27 | Nay |
| 3 | KNOW_01 (Soto) | 24-26 | Nay |
| 4 | MATSUI_041 | 24-28 | Nay |
| 5 | MULLCA_062 | 23-29 | Nay |
| 6 | ARBITRATION_01 (Dingell) | 23-27 | Nay |
| 7 | Final passage, as amended | 28-24 | Yea |

All seven votes were along party lines. Every Democrat present voted Yea on the amendments, and on final passage all 24 Democrats, Pallone included, voted **Nay**. Ocasio-Cortez did not vote on #5 or #6.

## 3. Status

- **H.R. 7757** (BILLSTATUS updated 2026-09-08; the congress.gov API showed the same actions on 2026-10-18): passed the House 6/29/2026 under suspension, 267-117 (Roll no. 228). On 7/13/2026 it was received in the Senate and referred to Commerce, Science, and Transportation. **There has been no Senate action since.** The House record shows no committee report. Pallone became the sole cosponsor on 6/23/2026.
- **S. 1748 (KOSA)**: on **8/5/2026** Senate Commerce "ordered to be reported with an amendment in the nature of a substitute favorably." It has not been formally reported, no reported text is posted, and there has been no floor action. Neither bill is law.

## 4. "Restricting addictive design features": the as-passed text (`bill-text/BILLS-119hr7757eh.htm`)

What the engrossed text does:
- **Sec. 2(6)** defines "design feature" to include "infinite scrolling or auto play," usage-based rewards and badges, "notifications and push alerts," appearance-altering filters, and personalized recommendation systems.
- **Sec. 214(a)(1)(D)** requires platforms to give known minors "safeguards to ... Limit design features that encourage compulsive usage." **Sec. 214(a)(3)** makes the most protective setting the **default**. Sec. 214(a)(1)(F) adds an option to opt out of recommendation systems, 214(a)(2) a time-limit option, and 214(b)(2)(D) parental time-viewing and time-restriction tools.
- **Sec. 214(d)(3)** bars user interfaces that obscure, subvert, or impair those safeguards.
- **Sec. 233** (SPY Kids Act) bans market or product research on known minors.

Limits of that language:
- These are default-on safeguards that can be switched off, not bans on any feature.
- "Compulsive usage" (Sec. 212(2)) means use that "substantially limits 1 or more major life activities," a disability standard taken from the ADA.
- The duties apply only to minors the provider "knows" about. In the passed text, "knows" means "know or should have known" for the KOSA subtitle.
- **Sec. 213(c)(2) keeps the clause saying nothing in the section may be construed to "impose a duty of care."**
- Enforcement (Sec. 701) is by the FTC and state attorneys general only. The bill has no private right of action and no limit on forced arbitration.

**Post-markup changes (context):** the House-passed text adopted much of what the rejected amendments sought on knowledge and preemption, but not the duty-of-care or arbitration pieces.
- "Knows" now means "know or should have known" for the KOSA subtitle (Sec. 212(6)), gaming (Sec. 302(4)), and chatbots (Sec. 402(3)). SPY Kids (Sec. 232) and COPPA keep "willful disregard."
- A single **Sec. 704** preempts state law "only to the extent that" it conflicts and protects state laws that provide "greater protection to minors."

## Proposed verdict

**MOSTLY TRUE.** The bill as passed does require default-on limits on engagement design features for known minors, so "restricting addictive design features" is supported. The claim leaves out several things:
- The limits are safeguards that can be switched off, not prohibitions.
- The bill expressly disclaims a duty of care.
- In committee, Langworthy voted against all six Democratic amendments. These included striking the duty-of-care disclaimer, a constructive-knowledge standard, protecting stronger state laws, and a ban on forced arbitration.
- The committee vote was party-line.
- The Senate has not acted, so nothing has been enacted.

The verdict could be framed as MISSING CONTEXT if the entry centers on "holding Big Tech accountable" rather than on design features.

## Gaps

- No permalink or archive for the Oct 16 post. The screenshot is the only artifact.
- The disposition of AMEND_7757 (Amdt-12) and of the Houchin and Schrier amendments has not been determined. The markup transcript (`HMKP-119-IF00-Transcript-20260305.pdf`) has not been read.
- I did not diff the ih and eh texts beyond the sections cited above.
- The congress.gov pages could not be archived (Save Page Now returned nothing). Everything else is listed in `archive-verify.tsv`.
- File-naming note: the event page's "H.R. 7757" text link is named `BILLS-119HR7577ih.pdf`, but its content is H.R. 7757. Don't confuse it with H.R. 7577, the TIP Improvement Act. `SCHRWA_023` is likewise filed under "HR7577."

## Archives

The Wayback snapshots were verified by fetching each one (raw `id_`) and getting a 200 response. **17 of 18 are byte-identical** to the local copy. The event page was checked by content (it contains CASTOR_049 and Vote007). Full list: `archive-verify.tsv`.

**Unverified:** congress.gov `house-bill/7757/all-actions` and `senate-bill/1748/all-actions`. Save Page Now returned no capture for either.
