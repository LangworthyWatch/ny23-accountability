---
name: capture-findings
description: Capture actionable findings, leads, and follow-up tasks from research sessions, donor scans, news monitoring, and fact-check work into a structured backlog so they don't fall off. Use after any analysis that surfaces leads (e.g., new bills to fact-check, donor patterns worth investigating, Wayback URLs that need re-archiving, FOIL responses to follow up on, Q2 FEC/LDA data drops scheduled for a future date). Trigger when the user says "capture this", "log these findings", "what did we find", "save these results", "add to backlog", "track this lead", or after a research session produces follow-ups that aren't doable immediately.
---

# Capture Findings

Research sessions, donor scans, and fact-check drafts constantly surface
actionable items — new statements to fact-check, donor patterns worth tracking,
URLs that need Wayback re-archiving, data drops that won't land until a
specific future date. These findings disappear into terminal scroll history
unless they're captured immediately.

> **⚠️ Ported from public-ledger 2026-06-08.** The upstream version writes to
> public-ledger's `FINDINGS_BACKLOG.md` and cross-references public-ledger's
> CLAIMS.md and TRIGGER_REGISTRY.md. For LangworthyWatch, the equivalents are
> `langworthy-tracker/FINDINGS_BACKLOG.md` (create it if it doesn't exist)
> and cross-references to `content/fact-checks/_index.md` and
> `langworthy-tracker/CLAUDE.md`.

## Arguments

`$ARGUMENTS` can be:
- A topic or workstream name → extract findings from its recent outputs
- "review" → show the current findings backlog
- "triage" → prioritize and assign findings to fact-check workstreams
- A specific finding to log → add it directly
- No argument → scan recent git changes and session context for uncaptured findings

## The findings backlog

The backlog lives at
`/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/FINDINGS_BACKLOG.md`.

If the file doesn't exist, create it with this structure:

```markdown
# LangworthyWatch — Findings Backlog

> Actionable findings, leads, and follow-up tasks surfaced during research
> sessions. Items here are unprocessed — once acted on, move to a fact-check
> entry under content/fact-checks/ or close with a disposition note.

**Last updated:** YYYY-MM-DD

---

## Priority Findings

<!-- High-value leads that could become fact-check entries or unblock investigations -->

## Source / Data Quality Issues

<!-- Wayback archive failures, FOIL responses pending, primary sources that need re-fetching -->

## Follow-Up Tasks

<!-- Scheduled work tied to a specific future date — Q2 FEC/LDA drops, pending committee hearings, etc. -->

## Fact-Check Leads

<!-- New Langworthy statements, votes, or actions worth a standalone fact-check -->

## Closed / Resolved

<!-- Findings that have been acted on — keep for audit trail -->
```

## Step 1 — Identify findings

Findings come from several sources. Check whichever are relevant:

### Recent fact-check work
- Did a draft surface a Tier-B claim that needs Tier-A confirmation later?
- Did a `/fec-donor-scan` reveal a donor pattern worth a separate entry?
- Did `/fact-check-review` flag a Recommended item that wasn't applied?
- Did a Wayback archive run return 520/523 for URLs that need retry?

### Recent git changes
```bash
git log --oneline -5
git diff HEAD~3 --stat -- content/fact-checks/
```

### Current session context
If the user just wrapped a research session, extract findings from the
visible work — new bills cited, new committee hearings scheduled,
data sources that need re-pull at a future date.

### Common finding types to look for

| Type | Signal | Example |
|------|--------|---------|
| **Fact-check lead** | New Langworthy statement / vote / action | "Langworthy posted Facebook re: AI safety regs — could be MISLEADING" |
| **Data refresh** | A primary source whose Q2/Q3 data isn't out yet | "Q2 LDA filings on H.R. 8413 drop 2026-07-20" |
| **Donor pattern** | FEC scan revealed a cross-sector alignment | "21 SECURE Data Act endorser-coalition PACs gave $270K to Langworthy" |
| **Archive gap** | Wayback save returned 520/523 | "8 secondary URLs from SECURE Data Act entry need re-archiving" |
| **FOIL pending** | Submitted FOIL has a response-due date | "COELIG FOIL — Erin Baker disclosure due 2026-06-02" |
| **Story angle** | Pattern with journalistic value | "4 federal preemption initiatives in 5 months — all target NY law" |
| **Cross-link gap** | Existing entry should link to a new one but doesn't | "2026-02-state-preemption-pattern needs SECURE Data Act 4th row" |
| **Pattern trigger** | Threshold approaching (e.g., DOCUMENTED PATTERN requires 3+) | "2 instances of credit-claiming for autosignature programs — needs 3rd" |
| **Verdict mismatch** | An entry's verdict label might warrant downgrade/upgrade after new data | "Tioga rural-impact MISSING CONTEXT may need DOCUMENTED PATTERN after RHTP data" |

## Step 2 — Structure each finding

Each finding entry should include:

```markdown
### [Short title]
- **Date logged:** YYYY-MM-DD
- **Source:** [session, script, or workstream that produced it]
- **Type:** [fact-check-lead | data-refresh | donor-pattern | archive-gap | foil-pending | story-angle | cross-link-gap | pattern-trigger | verdict-mismatch]
- **Priority:** [high | medium | low]
- **Detail:** [1-3 sentences describing the finding]
- **Action:** [specific next step — what to do, ideally with a date]
- **Status:** open
```

## Step 3 — Classify and file

Place each finding in the appropriate section of FINDINGS_BACKLOG.md:

- **Priority Findings** → high-priority fact-check leads, story angles, pattern triggers
- **Source / Data Quality Issues** → archive gaps, broken primary-source URLs, FOIL response-handling
- **Follow-Up Tasks** → scheduled work tied to a specific date (Q2 FEC drop, Q2 LDA drop, committee hearing dates)
- **Fact-Check Leads** → new Langworthy statements / votes / actions worth a standalone entry

## Step 4 — Cross-reference

For each finding, check:

1. **Is it already known?** Search FINDINGS_BACKLOG.md and
   `content/fact-checks/_index.md` to avoid duplicates.

2. **Does it affect a published entry?** If a finding changes the math /
   verdict / sources of any published entry, flag it as high priority and
   suggest the user open `/ny23-fact-check` to update.

3. **Is it tied to a specific date?** If yes, format the action item with
   the date so the next session can pick it up at the right moment.

## Step 5 — Report

Print a summary of what was captured:

```
## Findings Captured

| # | Title | Type | Priority | Action date |
|---|-------|------|----------|-------------|
| 1 | ... | ... | ... | ... |

Added N findings to FINDINGS_BACKLOG.md
Existing entries that may need updates: [list or "none"]
Date-triggered items: [list with dates or "none"]
```

## When to use "review" mode

When called with "review", show the current backlog organized by priority,
with counts:
- How many open findings total
- How many per type
- How many high-priority items
- Which findings are oldest (might be stale)
- Which have a date trigger in the next 14 days
- Suggest which to act on next

## When to use "triage" mode

When called with "triage":
1. Read all open findings
2. Re-evaluate priorities based on what's actually shipped recently
3. Suggest which findings to close (already resolved by recent fact-check work)
4. Suggest which to escalate (became more relevant due to new statements / votes)
5. Group related findings that could be addressed together in one fact-check entry

## Examples of LW-specific findings worth capturing

From the 2026-06-06 SECURE Data Act session:

1. **Q2 LDA filings on H.R. 8413** — data-refresh, due 2026-07-20, action:
   re-query Senate LDA and update donor section of the entry.
2. **Q2 FEC PAC transfers** — data-refresh, due 2026-07-15, action:
   re-run `/fec-donor-scan` on Langworthy committees, update donor section
   if material change.
3. **8 secondary URLs returned 520/523 from Wayback** — archive-gap, action:
   re-run `scripts/archive_sources.sh` in 24-48h, swap `archived_url` to GPO
   PDF snapshot once indexed.
4. **EPIC hearing testimony transcript** — source-quality, action: pull from
   E&C committee hearing page once posted (~1-2 weeks post-hearing), replace
   the hedged EPIC quote in the SECURE Data Act entry with verbatim.
5. **`fec-donor-scan` direction bug uncovered** — pattern-trigger /
   cross-link-gap, action: audit existing donor sections in published entries
   for the same wrong-direction query pattern (esp. nursing-home-staffing-donations,
   corning-manufacturing-credits-obbba, ida-donor-exemption-pattern).
