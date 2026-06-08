---
name: tier-a-confirm
description: Promote a list of Tier-B claims (from a news article, secondary analysis, or WebSearch summary) to Tier-A (primary-source confirmed) via parallel agents. Use when the user says "promote these claims to Tier-A", "confirm at primary source", "verify these against the primary docs", or when a fact-check draft cites claims that came from WebSearch summaries rather than direct primary-source fetches. For LangworthyWatch, this is the right tool BEFORE flipping a fact-check entry from draft to published — it parallelizes verbatim-quote verification across 4-8 agents.
---

# Tier-A Confirm

The canonical pattern for promoting Tier-B (WebSearch summary / news /
secondary-source) claims to Tier-A (primary-source-confirmed) via parallel
agents. Each agent writes a per-item closure note with explicit
CONFIRMED / PARTIAL / NEGATIVE / DEFERRED status.

> **⚠️ Ported from public-ledger 2026-06-08.** The upstream version is geared
> toward research/kb/ outputs and CLAIMS.md promotion. For LangworthyWatch,
> the equivalent flow is:
> - Tier-B claims live in a draft fact-check entry under `content/fact-checks/`
> - Tier-A confirmations get folded BACK into that entry (verbatim quotes,
>   primary-source URLs), not into a separate KB
> - Completion criteria: every `>` blockquote in the entry is verbatim from a
>   fetched primary document, and every dollar figure / date / count traces to
>   a Sources block URL

> **The June 2026 SECURE Data Act fact-check is the canonical worked example.**
> Three batches of Tier-A confirmations ran in this session: (1) GPO XML
> extraction of Sec. 12/13/14/15 verbatim text, (2) nysenate.gov S9088A action
> history (vote tally, dates), (3) corrected FEC donor scan (pas2 direction
> fix). All three started as Tier-B (WebSearch summary) findings that needed
> primary-source confirmation before publication.

## When to use

- A `/ny23-fact-check` draft cites claims that came from WebSearch summaries
  rather than direct fetches of primary documents
- A `/fact-check-review` report flags Failure Mode #1 (tool summaries treated
  as primary-source quotes) on multiple items
- The user wants to verify multiple specific facts at primary source before
  publishing — e.g., "confirm the H.R. 8413 cosponsor list, the NY S9088
  vote tally, and the CalPrivacy quote against their actual documents"
- Before flipping `draft: false` on any entry with 3+ blockquoted "verbatim"
  passages

Don't use for:
- Single-claim confirmation (just spawn one Agent or use WebFetch directly)
- Generic fact-checking (use `/ny23-fact-check` instead)

## Arguments

`$ARGUMENTS` is the claim-source + claim-list specification. Examples:

- "promote the top 5 Tier-A candidates from the SECURE Data Act draft"
- "verify these 3 claims: (1) Langworthy cosponsorship of HR 8413,
  (2) NY S9088A passed 51-10 on June 3 2026, (3) CalPrivacy 'step backwards'
  quote"
- "tier-a confirm — every blockquote in 2026-06-06-langworthy-secure-data-act-hr8413.md"

Parse out:
- **claim_source**: draft entry path / inline list / review-agent output
- **claim_list**: 3-8 claims to confirm in parallel (cap at 8)
- **target_entry**: which fact-check the confirmations should fold back into

## Step 1 — Extract the claim list

If the source is a draft entry, grep for blockquotes (`> "..."`) and for
specific numeric assertions in tables / body text. Print the claim list to
the user; ask which subset to run if there are >8 (the skill caps at 8 agents).

If the source is a review-agent report, pull the items it flagged as Critical
or Recommended with "verify against primary source" notes.

If the source is inline, just enumerate the claims provided.

## Step 2 — Group claims by primary-source domain

Some claims share a primary-source domain and can be combined into a single
agent. Examples for LW work:

- Multiple Sections of a single bill (Sec. 12 + 13 + 15 of H.R. 8413) → one agent fetching the GPO XML once
- Multiple action items from one nysenate.gov bill page (sponsor, status, vote tally, dates) → one agent
- Multiple Langworthy press releases → one agent walking langworthy.house.gov
- Multiple roll-call votes → one agent on `clerk.house.gov/Votes`
- Multiple FEC PACs (filtering Langworthy's incoming pas2) → one agent running the DuckDB query

Aim for 3-6 agents covering all claims (don't run 1 claim per agent when
several share a source).

## Step 3 — Spawn the agents in parallel

For each claim group, spawn a `general-purpose` agent:

```
Agent(
  subagent_type: "general-purpose",
  description: "{Topic} Tier-A confirmation",
  run_in_background: true,
  prompt: """
    Tier-A primary-source confirmation pulls. Working dir:
    /Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker.

    Context: Draft fact-check at `content/fact-checks/{slug}.md` cites
    {N} items from secondary sources that need primary-source confirmation
    before publication.

    {N} items to confirm:

    1. **{Claim 1}** — pull {specific primary source: GPO bill PDF/XML,
       House Clerk roll-call XML, nysenate.gov action history, FEC bulk,
       CalPrivacy PDF, etc.}. Confirm: {specific facts to verify}.

    2. **{Claim 2}** — ...

    Process for each item:
    - Fetch the primary document (WebFetch the URL; for GovInfo PDFs and
      similar, the depot may already have them at /tmp/ from prior sessions)
    - For House Clerk roll-call votes, fetch the XML at clerk.house.gov/evs/...
    - For FEC bulk data, run a Python+DuckDB read-only query against
      ~/data/public-ledger/federal/fec/fec_index.duckdb (see /fec-donor-scan)
    - For NY state bills, fetch the nysenate.gov bill page action history
    - Quote exact language verbatim — character-for-character match required
      for CONFIRMED status
    - Note URL, fetch timestamp, and any document revision/version IDs
    - If primary source not retrievable within 2-3 attempts (403, paywall,
      timeout), mark "Tier-A confirmation deferred — primary source not
      retrievable; pull options: [list options]"

    Output: ONE structured report with per-item sections:
      - Tier-B claim being tested (verbatim from the draft entry)
      - Primary sources pulled
      - Tier-A status [CONFIRMED / PARTIAL / NEGATIVE / DEFERRED]
      - Quoted verbatim language from primary source
      - Suggested edit to the draft entry (if any change needed)

    Constraints:
    - DO NOT edit the fact-check entry directly
    - DO NOT modify content/fact-checks/_index.md
    - DO NOT commit
    - Only return the report

    Report under 400 words: (a) status grid, (b) most material finding,
    (c) any claim that came back NEGATIVE (most important — these are
    corrections, not confirmations).
  """
)
```

Send all agents in a SINGLE message with multiple `Agent` tool-use blocks.

## Step 4 — Consolidate the status grid

When all agents return, compile a single status table for the user:

| Claim | Tier-A status | Verbatim primary-source quote / value |
|-------|---------------|---------------------------------------|
| {Claim 1} | ✅ CONFIRMED | {key verbatim fact} |
| {Claim 2} | ⚠️ PARTIAL | {what's confirmed + what's deferred} |
| {Claim 3} | ❌ NEGATIVE | {what the primary source actually says, contradicting the draft} |
| {Claim 4} | ⏸️ DEFERRED | {what's needed to close} |

## Step 5 — Apply confirmations to the draft entry

For each CONFIRMED item:
- Replace the Tier-B language in the draft with the verbatim primary-source
  quote (with the URL added to Sources block if new)
- Add a parenthetical citation pointing at the exact subsection / section ID

For each NEGATIVE item:
- **This is the most important class to surface.** A NEGATIVE means the draft
  is WRONG and would have been published wrong without this step. Flag it
  prominently to the user and propose the corrected language.

For each PARTIAL or DEFERRED:
- Hedge the language in the draft entry (e.g., "per [secondary source]" or
  "as of [date when WebFetch was attempted]")
- Add a TODO comment in the entry body so future reviewers know it needs
  re-confirmation
- Flag what additional primary-source pull is needed in your summary

## Step 6 — Re-run /fact-check-review

After applying the confirmations to the draft entry, re-run `/fact-check-review`
on the updated entry to verify the Tier-A round didn't introduce new issues.

## Heuristics

- **3-6 agents max.** Beyond 6 the consolidation overhead exceeds the
  parallelism benefit.
- **Group claims by primary-source domain** (Step 2) to maximize signal per
  agent.
- **Each agent's report is self-contained.** No agent should require another
  agent's output.
- **CONFIRMED requires verbatim quote.** "Secondary source repeats the claim"
  is not CONFIRMED — that's PARTIAL.
- **NEGATIVE findings are the most important class.** They contradict the
  draft and prevent publishing wrong facts. Don't bury them.
- **DEFERRED is fine** when WebFetch is sandbox-denied or the primary source
  is paywalled — log the URL + needed access mechanism and hedge the draft
  language accordingly.

## Anti-patterns

- **Don't auto-edit the draft entry from a sub-agent.** Sub-agents return a
  report; the main session decides what to apply.
- **Don't flip `draft: false` based on this skill alone.** This skill confirms
  individual quotes; `/fact-check-review` checks for internal contradictions,
  unsourced details, and other failure modes. Both must pass.
- **Don't run >8 agents in parallel.** Throttling + consolidation overhead
  defeats the purpose.
- **Don't skip the status grid (Step 4).** It's the user-facing summary.

## Related skills

- `/ny23-fact-check` — the entry-creation skill upstream of this one
- `/fact-check-review` — the canonical pre-publish verifier (run this AFTER
  Tier-A confirmation is folded in)
- `/source-attribution-check` — finds unsourced claims (run this BEFORE
  Tier-A confirmation; together they cover the two failure modes)
- `/fec-donor-scan` — the right tool for any FEC donor claim in a Tier-A queue
