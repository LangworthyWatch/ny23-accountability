---
name: prepublish-lint
description: Scan a fact-check draft for provisional language that reads as finished — "by elimination", "per the report's data", "[link to be added]", TODO/TBD, plus draft:false entries with an unexplained empty archived_url, a generic source_url, or an unresolved hold_reason. Run before flipping draft:false. Trigger when the user says "lint this draft", "is anything unfinished", "prepublish check", "what still needs confirming", or right before publishing/deploying an entry.
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
  literal "placeholder", and a **`hold_reason` still set on a `draft:false`
  entry**.
- **HEDGE** (verify the underlying fact): "almost certainly", "appears to",
  "reportedly/allegedly", and — for `draft:false` entries — an empty
  `archived_url` **with no `archive_note`**, or the generic
  `facebook.com/RepLangworthy` `source_url` (with or without a trailing slash).
- **SOFT** (intended?): `~`, "roughly", "approximately", "estimated" — fine when
  deliberate, flagged in case an approximation is standing in for a known exact
  figure. Also: an empty `archived_url` **that is documented by an
  `archive_note`**, and a leftover pre-publish-checklist comment on a published
  entry.

## The two frontmatter conventions it enforces

Both were added July 2026 after a run of Facebook-sourced entries.

**`archive_note`** — some sources genuinely cannot be archived. Wayback and
archive.today both fail on login-walled Facebook posts (Save Page Now returns a
redirect but never captures; the resulting URL 404s). The project ships these
entries anyway — several published ones carry an empty `archived_url` — so an
empty archive is only a problem when it is *undisclosed*. Setting
`archive_note` to name the real preservation artifact (screenshot on file,
transcript under `research/transcripts/`) downgrades the finding from HEDGE to
SOFT. **Never paste a Wayback URL that does not resolve** — a dead link that
looks like an archive is worse than an honest empty field.

**`hold_reason`** — a deliberate "do not publish yet" flag, carrying the
specific thing still to verify (e.g. "confirm the House sponsor against the
govinfo BILLSTATUS roster"). It pairs with `draft: true`. Shipping it alongside
`draft: false` means an entry went live with a known-open question, so that
combination is a **BLOCK**: resolve the hold, then delete the field.

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
