---
name: prepublish-lint
description: Scan a fact-check draft for provisional language that reads as finished — "by elimination", "per the report's data", "[link to be added]", TODO/TBD, plus draft:false entries with an empty archived_url or a generic source_url. Run before flipping draft:false. Trigger when the user says "lint this draft", "is anything unfinished", "prepublish check", "what still needs confirming", or right before publishing/deploying an entry.
---

# /prepublish-lint

The risk at publish isn't a wrong number — it's a *provisional* claim that looks
identical to a verified one once it's in prose. "Confirmed by elimination,"
"per the report's state-by-state data," "[link to be added]" are honest
placeholders that quietly become load-bearing the moment `draft:false` ships.
This is a deterministic scan that produces a confirm-or-cut punch list.

```bash
python .claude/scripts/prepublish_lint.py <path-to-entry.md>
```

## What it flags

- **BLOCK** (confirm or cut before publishing): "by elimination", "per the
  report's data", `[link to be added]`, `[citation needed]`, TODO / TBD / FIXME,
  literal "placeholder".
- **HEDGE** (verify the underlying fact): "almost certainly", "appears to",
  "reportedly/allegedly", and — for `draft:false` entries — an empty
  `archived_url` or the generic `facebook.com/RepLangworthy` `source_url`.
- **SOFT** (intended?): `~`, "roughly", "approximately", "estimated" — fine when
  deliberate, flagged in case an approximation is standing in for a known exact
  figure. Also notes a leftover pre-publish-checklist comment on a published entry.

It blanks out HTML comments before scanning the prose, so a pre-publish checklist
that legitimately *quotes* these words doesn't self-trigger.

## How to use the output

Non-blocking by design — it flags, you decide. Walk the **BLOCK** items first;
each one is something that should be confirmed against a source or cut before the
entry goes live. **HEDGE** items mean "go verify the fact, then state it plainly
or hedge it honestly." **SOFT** items are usually fine.

Run this at the tail of `/claim-audit`, or standalone right before flipping
`draft:false` and deploying.

## Exit codes

`0` = clean, `1` = findings, `2` = error.

## Related

- `/claim-audit` — runs this at the tail of its pass.
- `/fact-check-review` — the deeper source-verification gate; this lint is the
  quick provisional-language pass that precedes it.
