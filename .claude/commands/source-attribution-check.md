---
name: source-attribution-check
description: Flag unattributed quotes, claims, and statistics in fact-check or correspondence content. Use after writing or editing any LangworthyWatch journalism content (.md in content/fact-checks/ or content/correspondence/). Complements `/fact-check-review` — that one verifies cited primary sources; this one finds claims that are missing citations entirely. Trigger when the user says "check attribution", "find unsourced claims", or after a Write/Edit on a fact-check entry.
---

# Source attribution check

After writing or editing a fact-check entry or correspondence letter, scan
for unattributed information that requires sources.

## When to use

- After drafting a new fact-check entry, before `/fact-check-review`
- After editing an existing entry (especially adding numbers or quotes)
- When the user pastes a draft and asks "is anything unsourced?"

## What to detect

### Unattributed quotes

Look for quotation marks without attribution:

```
❌ "This policy will help thousands of families."
✅ "This policy will help thousands of families," Langworthy said in [source, date].
```

### Unattributed statistics

Numbers and percentages without sources:

```
❌ Crime dropped 15% last year.
✅ Crime dropped 15% last year (FBI Uniform Crime Reporting, 2025).

❌ Most Americans support the policy.
✅ 67% of Americans support the policy (Gallup, March 2026).
```

### Unattributed claims

Factual assertions that need sourcing:

```
❌ The company has been losing money for years.
✅ The company reported losses in 5 consecutive quarters (SEC 10-Q filings, 2024-2025).
```

### Patterns to flag

- Quotes without "said," "wrote," "per [source]," "according to," or similar attribution
- Statistics without source citation
- "Studies show..." without naming the study
- "Experts say..." without naming experts
- "Critics argue..." without naming critics
- Dates / counts / dollar figures in body text not traceable to a Sources block entry

## Output format

If issues found, return a structured list:

```
⚠️ Attribution check found N issues:

Line 42: Quote needs attribution — who said this?
> "It's a fundamental violation of consumer protection."

Line 67: Statistic "$840 billion" needs source citation
> ...cut $840 billion from Medicaid...

Line 89: "Experts argue..." — which experts?
> Many experts argue this would chill investment.

Run `/fact-check-review` next if these are resolved.
```

## Non-blocking

This skill provides warnings only. The user decides whether attribution is
needed in context (some facts in summary tables don't need inline citation
if the Sources block at the bottom covers them).

## Skip conditions

Skip this check for:
- Template files (`_template-*.md`)
- Example files (`example-entry.md`)
- Files with `draft: true` that are clearly very early sketches
- The site's `_index.md` summary tables (which are by design terse)

## Context awareness

Some claims don't need explicit attribution:

- **Commonly known public facts** ("Langworthy represents NY-23")
- **Observable facts visible in the cited source** (e.g., the date of a press
  release that's already linked in the Sources block)
- **Direct narration of a documented vote** ("voted YES on H.R. NNNN") when
  the roll-call is cited

Focus on claims where a reader would reasonably ask "says who?" — and on
specific numbers that don't appear in the cited primary sources.

## Anti-patterns

- Don't flag a claim that's clearly sourced in the next sentence or paragraph
- Don't flag generic narration that doesn't carry a numeric or quoted assertion
- Don't auto-edit the file — only report flags to the user

## Related

- `/fact-check-review` — verifies that ALREADY-cited sources actually say what
  the entry attributes to them (verbatim quote check). Run AFTER this skill
  is clean.
- `/ny23-fact-check` — the entry-creation skill. This skill is what to run
  after a draft from `/ny23-fact-check` is written.
