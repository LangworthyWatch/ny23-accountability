---
name: ny23-fact-check
description: Create or edit a fact-check entry for LangworthyWatch.org. Use when the user wants to create or edit a fact-check entry, mentions Langworthy, NY-23, or accountability tracker content, has a constituent letter / press release / public statement to fact-check, or says `/ny23-fact-check` with a topic or claim. Complements `/fact-check-review` (which verifies an already-drafted entry against primary sources before publication).
---

# NY-23 Accountability Tracker — Fact-Check Creator

Create, edit, and validate fact-check entries for the NY-23 Accountability Tracker
(LangworthyWatch.org). This Hugo-based civic fact-checking site compares
Rep. Nick Langworthy's public statements against the congressional record using
exclusively primary government sources.

> **Where this skill lives:** `langworthy-tracker/.claude/commands/ny23-fact-check.md`.
> Companion: `/fact-check-review` (same directory) — that one is the pre-publish
> verifier. Use `/ny23-fact-check` to CREATE the entry, `/fact-check-review` to
> VERIFY it before flipping `draft: false`.

## Arguments

`$ARGUMENTS` describes the claim or topic. Examples:
- "SNAP benefits claim from March 2026 newsletter"
- "constituent letter response about Medicaid"
- "voting record contradiction on government shutdowns"
- "IDA tax break donor-beneficiary pattern"

---

## Step 1: Select template variant

| Variant | When to use | Opening section |
|---------|------------|-----------------|
| **A — Standard claim** | Single statement to fact-check | `## Statement` |
| **B — Local impact** | Policy with measurable district effect | `## Why This Matters for NY-23` |
| **C — Pattern analysis** | Recurring behavior across multiple instances | `## Overview` |

Most entries use Variant A. Use B when CBO scores, grant data, or program
enrollment numbers can be localized to the district. Use C only for aggregate
analyses (campaign finance patterns, rhetoric vs. actions overviews).

## Step 2: Write Hugo frontmatter

Use this format (matches existing LW conventions per
`langworthy-tracker/CLAUDE.md`):

```yaml
---
title: "Short descriptive title with the verb-phrase contradiction in plain language"
date: 2026-MM-DD
draft: true                # flip to false only after /fact-check-review passes
topic: "Healthcare|Economy|Veterans|Immigration|Rule of Law|Consumer Protection / Privacy|Transparency|etc"
claim_date: "Month DD, YYYY"
source: "Press Release|Facebook Post|Constituent Letter Response|Interview|Press Conference|Weekly Update|etc"
source_url: "https://original-source-url"
archived_url: "https://web.archive.org/web/..."
verdict: "VERDICT_LABEL"
tags: ["topic-tag", "bill-number", "policy-area"]
counties: ["allegany", "cattaraugus", "chautauqua", "chemung", "erie", "schuyler", "steuben", "tioga"]
---
```

### Title convention

Format: `"Topic: Verb-phrase describing what's going on"`.

Examples drawn from existing live entries:
- `"SECURE Data Act: Langworthy Cosponsors Federal Bill That Would Preempt the New York Privacy Law the State Senate Just Passed"`
- `"Federal Preemption Pattern: Three Bills, One Playbook"`
- `"Big Brother Has No Place Spying on You — Posted While Voting to Extend Warrantless Surveillance"`

### Counties (lowercase slugs, full list when district-wide)

`allegany`, `cattaraugus`, `chautauqua`, `chemung`, `erie`, `schuyler`, `steuben`, `tioga`

For district-wide entries, use all eight. (Older entries used the literal string
`["district-wide"]` — that has been replaced with the eight-county list per the
2026-06-06 SECURE Data Act fix.)

### Topic field

Use a single string (not a list). The site's filter logic reads this as a
string. Examples that appear in live entries:
`Healthcare`, `Consumer Protection / Privacy`, `Energy / Utility Costs`,
`Transparency`, `Rule of Law`, `Disability & Medicaid`.

### Source types

Constituent Letter Response, Facebook Post, Press Release, Press Conference,
Weekly Update from Congressman Nick Langworthy, DOGE website, Conservative Party
Mailer, Campaign Text Messages, Local news coverage, Floor Speech, Multiple
Constituent Letter Responses, Multiple Press Releases, Bill Cosponsorship,
Committee Hearing, Roll Call Vote.

## Step 3: Write the entry body

Read 1-2 recent live entries before drafting to match the project's tone.
Recommended templates:

- **Variant A standard claim:** `content/fact-checks/2026-04-30-bigbrother-fisa-car-surveillance.md`
- **Variant B local impact:** `content/fact-checks/2026-02-25-energy-choice-act.md`
- **Variant C pattern:** `content/fact-checks/2026-02-state-preemption-pattern.md` or
  `content/fact-checks/2026-06-06-langworthy-secure-data-act-hr8413.md`

### Variant A — Standard claim fact-check

```markdown
## Statement

**Source:** [Source Type], [Date]

> "[Exact quote — verbatim from the source, blockquote format]"

---

## Congressional Record / The Facts

[Verified data from official sources. Use specific bill numbers, roll-call
numbers, CBO scores. Quote primary sources verbatim where possible.]

---

## Context

[Additional information for the full picture. Include what the claim omits,
relevant timeline, and any competing interpretations.]

---

## Questions This Raises

1. [Question based on documented facts — not accusations]
2. [Second question]

---

## Sources

- [Source description](URL)
- [Source description (archived)](https://web.archive.org/web/YYYYMMDD/URL)

---

**Note:** This entry documents publicly available information from [type of source].
Readers may draw their own conclusions.

*Last updated: Month DD, YYYY*
```

### Variant B — Local impact opening

Add an opening section before the Statement block:

```markdown
## Why This Matters for NY-23

[Open with district-specific data: enrollment numbers, dollar amounts,
facility counts, jobs affected. Use county names. After data-heavy sections,
add "In plain language:" translations.]

---

## Statement

[same structure as Variant A]
```

Variant B header variations (use whichever fits):
- `## Why This Matters for NY-23` (district-wide policy)
- `## Why this matters in a rural district` (healthcare, services)
- `## What [Program] does in NY-23` (specific program)
- `## What [Facility] means to the region` (local institution)

### Variant C — Pattern analysis

```markdown
## Statement

[Brief framing of the pattern — list the N instances]

## Why This Matters for NY-23

[How the pattern affects district residents]

## The Pattern: [Descriptor]

[Table or list of instances with consistent structure]

## Bill-by-Bill (or Instance-by-Instance) Analysis

### 1. [Name]
[Description, framing, industry support, sources]

### 2. [Name]
...

## Summary Table

| Instance | Target | Beneficiary | Framing |
|---|---|---|---|

## Questions This Raises

## Sources

## Related Fact-Checks
```

## Step 4: Apply verdict

LW's CLAUDE.md lists these as the **canonical verdict labels**:

- **TRUE** — Claim is accurate
- **MOSTLY TRUE** — Accurate but missing context
- **MISLEADING** — Technically accurate but creates false impression
- **MOSTLY FALSE** — Mostly inaccurate with minor accurate elements
- **FALSE** — Claim is factually incorrect
- **FALSE ATTRIBUTION** — Claim attributes something to wrong source/cause
- **CONTRADICTION** — Statement conflicts with documented actions
- **DEFLECTION** — Response avoids addressing the actual question
- **NON-RESPONSIVE** — Constituent concern not addressed
- **MISSING CONTEXT** — Key information omitted that changes meaning
- **DOCUMENTED PATTERN** — Recurring behavior established by multiple instances
- **NOT SUPPORTED** — Claim lacks evidence

### Decision flow

1. Is there a specific, falsifiable claim? → TRUE / MISLEADING / MOSTLY FALSE / FALSE / NOT SUPPORTED
2. Does a stated position conflict with a recorded action? → CONTRADICTION
3. Is credit or blame assigned to the wrong actor? → FALSE ATTRIBUTION
4. Is this a constituent response that dodges the question? → NON-RESPONSIVE / DEFLECTION
5. Does the same behavior repeat across 3+ instances? → DOCUMENTED PATTERN
6. Is key qualifying information omitted? → MISSING CONTEXT

> **A note on additional verdict labels.** The upstream public-ledger version
> of this skill listed more verdict labels (PARTIALLY SUPPORTED, SUBSTANTIALLY
> ACCURATE, INCONSISTENT, MISSING ATTRIBUTION, CONFLICT OF INTEREST,
> NO IN-PERSON TOWN HALLS, MULTIPLE). LW's CLAUDE.md does NOT formally list
> these. If you need one of them, either (a) update CLAUDE.md first and get
> user approval, or (b) use the closest canonical label and explain the
> nuance in the Assessment body.

## Step 5: Cite sources

### Source registry — canonical formats

**Congress.gov:**
```
[H.R. XXXX — Bill Title](https://www.congress.gov/bill/XXXth-congress/house-bill/XXXX)
```
Vote citations: `Roll Call NNN, [Date]` — link to House Clerk XML where possible.

**GPO-authenticated bill text (best primary source):**
```
[H.R. XXXX introduced text — GPO PDF](https://www.govinfo.gov/content/pkg/BILLS-XXXhrXXXXih/pdf/BILLS-XXXhrXXXXih.pdf)
```

**FEC:**
```
Committee: Langworthy For Congress (C00817932)
JFC: Langworthy Congressional Victory Committee (C00832188)
Candidate ID: H2NY23228
[FEC Filing](https://www.fec.gov/data/committee/C00817932/)
```

**CBO:** `[CBO Score: Report Title](URL) — [Key figure]`

**House Clerk roll-call vote:** `[Roll Call NNN](https://clerk.house.gov/evs/YYYY/rollNNN.xml)`

**Langworthy press releases:** `https://langworthy.house.gov/media/press-releases/...`

**Public Ledgers cross-reference:** When IDA data is relevant, link to
`https://thepublicledgers.org/ida/states/ny/` rather than re-hosting raw data.

### Archive.org requirement

Every external source link MUST be archived before publication. Run
`scripts/archive_sources.sh` for full-corpus archiving, or curl
`https://web.archive.org/save/[URL]` for individual URLs. CLAUDE.md mandates
this; missing `archived_url` should block publication.

**Gov / Cloudflare-protected sources do not archive via curl.** `congress.gov`
(CRS reports, bill pages) and `fema.gov` return Cloudflare `520` / Akamai `403`
to both `curl` and the Wayback save endpoint — `archive_sources.sh` will silently
fail to capture them. Archive these from a real **browser** (open in Chrome →
submit via web.archive.org's Save Page Now), then confirm a fresh snapshot via
`https://archive.org/wayback/available?url=<url>`. This is also how you should
*read* these sources for verification: WebFetch/curl get 403, so open them in
Chrome and confirm quotes/figures against the actual document — never cite a
search-tool summary for a `congress.gov`/`fema.gov` fact.

## Step 6: Quality gate checklist

Before flipping `draft: false`, verify:

- [ ] Every claim has at least one primary government source (not news coverage alone)
- [ ] Verdict matches decision tree criteria
- [ ] All external links archived via Archive.org with snapshot URLs
- [ ] Counties tag matches all affected geographic areas
- [ ] Source metadata block present (type + date)
- [ ] Related entries cross-linked bidirectionally
- [ ] No unattributed statistics — every number has a source citation
- [ ] Title follows "Topic: Verb-phrase" convention
- [ ] Assessment / verdict explicitly stated with reasoning
- [ ] **`/fact-check-review <file>` has been run and Critical findings addressed**
- [ ] Update `content/fact-checks/_index.md` summary table with the new entry

## Correspondence-to-fact-check pipeline

When converting a constituent letter response into a fact-check:

1. **Identify the constituent's question** — what was actually asked?
2. **Read the response** — does it address the question directly?
3. **Check the congressional record** — does the response match voting/action history?
4. **Select verdict:**
   - Response dodges question entirely → NON-RESPONSIVE
   - Response redirects to unrelated topic → DEFLECTION
   - Response contains factual claims → run through accuracy verdicts
   - Response claims credit for others' work → FALSE ATTRIBUTION
5. **Use Variant A template** with `source: "Constituent Letter Response, [Date]"`
6. **Quote the response** in the Statement section (blockquote format)
7. **Cross-reference** with other constituent letter entries for pattern documentation

## Do NOT

- Use secondary sources (news articles) as the sole basis for a verdict
- Apply FALSE when MISLEADING or MISSING CONTEXT is more accurate
- Create entries without checking the congressional voting record
- Publish without archiving all source links
- Skip the `/fact-check-review` step before flipping `draft: false`
- Use DOCUMENTED PATTERN for fewer than 3 instances
- Forget bidirectional cross-linking with related entries
- Make accusations of criminal conduct or speculate about motives (per CLAUDE.md)
- State a membership/cosponsorship/signatory/relationship claim ("X is a cosponsor," "X signed," "X serves on") as a flat fact unless verified against the *authoritative* roster (congress.gov `/cosponsors`, the actual letter PDF) — never an aggregator like GovTrack. If unverified, hedge it in the body or omit it (CLAUDE.md Pre-Publish Review, failure mode #5)
