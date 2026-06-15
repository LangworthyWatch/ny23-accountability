---
description: Verify a fact-check entry against its cited primary sources. Catches the five failure modes documented in CLAUDE.md.
---

# /fact-check-review

You have been asked to verify a fact-check entry against its cited primary sources before publication. This is the pre-publish review step documented in CLAUDE.md (the "Pre-Publish Review" section).

The argument to this command is the path to the fact-check markdown file. If no argument was provided, ask the user which file to review.

## What you are checking for

Five specific failure modes that have caused real corrections in this project:

1. **Tool summaries treated as primary-source quotes.** Any number, dollar figure, or quoted sentence in the entry that came from a WebSearch tool summary rather than the actual primary document is suspect. The fix is to fetch the primary document yourself and verify the cited number/quote appears there exactly as the entry says.

2. **Inferred relationships from form fields that don't carry them.** Specifically: the House Clerk's Gift Travel Filings index shows the *filer* of a sponsored-travel form, not the traveler. Any sentence in the entry that names a relationship (spouse, child, staff member) without an explicit source is suspect.

3. **Atmospheric detail without a source.** Any date, vintage, age, or background descriptor that isn't traceable to a specific cited URL is suspect. Examples: "the helicopter had been in service since the 1970s" was added without any source — it was speculation that turned out to be wrong.

4. **Conflated numbers from different snapshots.** Any derived number (a difference, ratio, percentage, or "shortfall") that combines two numbers from different sources or different time-points is suspect. Examples: subtracting an "original total invoice" from a "remaining balance after partial payments" produces a meaningless shortfall figure.

5. **Membership/affiliation claims taken from aggregators or pattern-matching.** Any "X is a cosponsor of," "X serves on," "X signed," or "X endorsed" claim must be verified against the authoritative roster (the congress.gov bill **cosponsors** list; the actual letter PDF) — not GovTrack/billsponsor, and not inferred because similar entities qualify. The fix is to fetch the authoritative roster yourself and confirm the named person is actually on it. Symptom: a cosponsor/member/signatory claim that "fits the pattern" (e.g., a NY Republican on a bipartisan NY bill) but was sourced to an aggregator at less-than-confirmed status. (Caught June 13, 2026 — a false H.R. 6644 cosponsorship claim.) **Deterministic check:** `python .claude/scripts/verify_fact.py cosponsor <congress> <type> <num> <surname>` reads the govinfo BILLSTATUS roster directly — use it instead of an aggregator.

## Process

1. **Read the entry.** Use the Read tool on the file path provided.

2. **Extract the verifiable claims.** Make a list of:
   - Every URL cited in the Sources section
   - Every direct quote (in `> "..."` blockquotes or with quotation marks)
   - Every dollar figure, percentage, count, or date in the body
   - Every relationship claim (spouse, staff, member, etc.) about named individuals
   - Every derived figure that requires arithmetic across sources

3. **Dispatch a verification agent.** Use the Agent tool with `subagent_type: general-purpose` (NOT in background — you need the result before responding to the user). Brief the agent with:
   - The fact-check file path
   - The list of verifiable claims you extracted
   - Instructions to fetch each cited URL and verify each quote/number/date appears there
   - Instructions to flag any claim that cannot be verified, AND any claim that would benefit from explicit hedging (e.g., "almost certainly" instead of stating an inference as fact)
   - Time budget: ~20-30 minutes

4. **Read the agent's report.** Categorize findings into:
   - **Confirmed:** quote/number verified at the cited source
   - **Mismatch:** the source says something different from what the entry says
   - **Unsourced:** the entry asserts a claim that has no traceable source in the cited URLs
   - **Inference stated as fact:** the entry uses definitive language for something the source supports only as an inference
   - **Internal contradiction:** two parts of the entry contradict each other (e.g., Point 1's math contradicts Point 3's claim)

5. **Internal-consistency pass.** Independently re-read the entry as a hostile copy editor:
   - For every numbered point in any verdict/findings section, check that Point N's math doesn't contradict Point N+1's claim
   - For every "X days after Y" or "X months before Y" claim, do the date math by hand
   - For every dollar figure, confirm it appears in the cited source AND is described the same way (gross vs. net, total vs. remaining, encumbered vs. available)

6. **Propagation sweep (when this review covers a CORRECTION).** If the entry changed a figure, date, quote, status, or framing that could appear elsewhere, grep the whole corpus for sibling copies *before* declaring the fix done. The single most common error class in `public-ledger/docs/governance/ERROR_LOG.md` is a corrected claim left **stale in a sibling file** (its examples: a wrong EIN propagated ~9× across the corpus; a matcher fix left stale in the book chapter). A live correction in one file plus the old version in another is an internal contradiction across the *published* site.

   Sweep both prose and downstream consumers — the old value/phrasing AND the entity name:
   ```bash
   cd /Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker
   grep -rin -E '<old figure>|<old phrasing>|<entity>' content/ social-media/
   ```
   Check `content/fact-checks/`, `content/state-of-the-district/`, `content/correspondence/`, the social-card generators in `social-media/`, and any generated graphic data. Ignore substring false positives (e.g. "fa**bric**" / "fa**bric**ated" matching a `BRIC` sweep — itself the un-IDF'd-matcher class the same ERROR_LOG warns about). Report every sibling carrying the old claim as a **Critical** finding (internal contradiction), with the exact file:line. Also run `/propagation-sweep` standalone for an ad-hoc sweep outside a full review.

7. **Report.** Output a structured findings list to the user:
   - **Critical (must fix before publishing):** mismatches, unsourced claims, internal contradictions
   - **Recommended (should fix):** inferences stated as fact, missing hedging, unclear scoping
   - **Nice-to-have:** stylistic or organizational improvements

   For each finding, include:
   - The specific line or paragraph in the entry
   - What the source actually says (with quote + URL if a fetch was possible)
   - Suggested edit

8. **Do NOT auto-edit the file.** Present findings and let the user decide which to apply. After they approve a set of edits, you can apply them. (Exception: once the user has approved a correction, applying the *same* verified fix to the stale siblings the propagation sweep found is part of completing that correction.)

## What success looks like

A pre-publish review where:
- All five failure modes have been actively checked for, with explicit notes on what was checked
- Any number/quote/date that couldn't be verified is flagged for the user, not silently approved
- Internal contradictions (the kind that tripped up the helicopter fact-check before publication) are surfaced clearly
- Edits are proposed but not auto-applied

## What failure looks like

- "Looks good!" without actually fetching any cited URL
- Trusting a WebSearch tool's summary as if it were a primary-source quote (this is what the four failure modes were caused by in the first place)
- Auto-editing the file without showing the user the proposed changes first
- Silently approving an unsourced atmospheric detail because it sounds plausible

## Related skills

This is the deep source-verification gate. Around it:

- `/source-attribution-check` — finds claims missing citations (run **before** this).
- `/claim-audit` — catches the *recombination* error class this review doesn't target: a correctly-sourced fact attached to the **wrong neighbor** (Medicaid labeled SNAP, a county that isn't NY-23, the wrong roll call). Run it on any entry that mixes confusable entities.
- `/verify-fact` — deterministic primary-source checks (`verify_fact.py`) for roll-call votes, NY-23 county membership, and cosponsorship. Prefer it over "by elimination" and aggregators.
- `/prepublish-lint` — quick provisional-language scan (`prepublish_lint.py`) before flipping `draft:false`.
- `.claude/references/ny23-landmines.md` — the confusable-pairs + NY-23 county reference that `/claim-audit` walks.

## Reference

The five failure modes are documented in `CLAUDE.md` under the "Pre-Publish Review" section. See that section for the full context on why each one matters.
