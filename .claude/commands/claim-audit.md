---
name: claim-audit
description: Audit a fact-check draft for misattribution — correctly-sourced facts attached to the WRONG neighbor (wrong program, district, vote, date, or list). Catches the recombination error class that /fact-check-review and /source-attribution-check miss. Use after writing or editing any LangworthyWatch entry, before publish. Trigger when the user says "audit the claims", "check attributions", "did I attach facts to the right program/district", "claim audit", or after a Write/Edit on a fact-check entry that mixes similar entities (Medicaid/SNAP, two roll calls, multiple at-risk lists, counties).
---

# /claim-audit

Most fact-check errors on this beat are **not** fabrications. They're
*recombination errors*: a true, sourced fact gets attached to the wrong
neighbor — the Medicaid work requirement labeled SNAP, a vote's margin swapped
between Roll Call 145 and 190, "five NY-23 counties" when one is Yates. The
fact is right; the **join** is wrong.

This is a blind spot for the other reviewers:
- `/source-attribution-check` finds claims with **no** citation.
- `/fact-check-review` checks that a cited source **says** what's claimed.
- **This skill** checks that each fact is attached to the **right entity** — the
  thing neither of those catches, because the citation exists and the source is
  real; only the join is wrong.

The reason errors live here is *fluency*: in flowing prose, "this figure → this
program" reads as authoritative whether or not the join was checked. The fix is
to **break the prose into a table**, because a misattribution that's invisible in
a sentence is obvious in a grid.

## Input

The path to the fact-check markdown file. If none was given, ask which file.

## Process

1. **Read the entry**, then **read the landmines reference**:
   `.claude/references/ny23-landmines.md`. It lists the confusable pairs on this
   beat (Medicaid≠SNAP, RC145 vs RC190, Public Citizen vs FPI hospital lists,
   $212M vs the Medicaid cut, OCR 627/172/112, committees, NY-23 county set).

2. **Atomize the draft into a claim table.** This is the core of the skill — do
   not skip to prose judgment. One row per load-bearing assertion:

   | # | Subject (program / vote / place / person / list) | Assertion (figure / date / action) | Cited source in entry | Confusable with? (landmines) | Join OK? |
   |---|---|---|---|---|---|

   Fill "Confusable with?" from the landmines file whenever the subject is one
   of the known-adjacent entities. That column is where you slow down.

3. **Check every flagged join.** For the scriptable subjects, use the
   deterministic verifier rather than reasoning about it — it removes you (and
   your fluency) from the loop:
   ```bash
   python .claude/scripts/verify_fact.py rollcall <year> <num> <surname>
   python .claude/scripts/verify_fact.py county <name> [name ...]
   python .claude/scripts/verify_fact.py cosponsor <congress> <type> <num> <surname>
   ```
   For program/list/date joins (Medicaid vs SNAP, Public Citizen vs FPI), check
   the assertion against the matching row in the landmines table.

4. **Tail with the lint:**
   ```bash
   python .claude/scripts/prepublish_lint.py <file>
   ```
   to catch provisional language ("by elimination," "[link to be added]") that
   reads as finished.

5. **Report.** Group findings:
   - **Critical — wrong join:** a fact attached to the wrong program / district /
     vote / list / date. Give the row, what it says, what it should say, and the
     deterministic check that proves it.
   - **Recommended:** ambiguous attribution, a confusable pair used without the
     distinguishing detail, an approximation standing in for a known figure.
   - **Clean:** note which confusable pairs you checked and found correctly joined
     (so the user knows the landmines were actually walked, not skipped).

6. **Do NOT auto-edit.** Present findings; apply only what the user approves.

## What good looks like

- Every Medicaid/SNAP, RC145/RC190, Public-Citizen/FPI, and county claim in the
  draft appears as a row with its "Confusable with?" cell filled and a verdict.
- District/vote/cosponsor joins were checked with `verify_fact.py`, not asserted
  from memory.
- The report says explicitly what was checked and found correct, not just what
  was wrong.

## What failure looks like

- Judging the draft in prose without building the table (the table is what
  defeats the fluency blindness — skipping it reproduces the original error).
- "Looks consistent" without running a single `verify_fact.py` check.
- Re-flagging missing citations (that's `/source-attribution-check`'s job) instead
  of focusing on wrong joins.

## When a new landmine appears

If the audit finds (or nearly finds) a misattribution at a pair **not** in the
landmines file, add it — that file is the institutional memory for this error
class, and the next audit is only as good as it is.

## Related

- `/source-attribution-check` — finds claims missing citations (run first).
- `/fact-check-review` — verifies cited sources say what's claimed (run after).
- `/verify-fact` — the deterministic checks this skill calls.
- `/prepublish-lint` — provisional-language scan (this skill runs it at the tail).
- `.claude/references/ny23-landmines.md` — the confusable-pairs reference.
