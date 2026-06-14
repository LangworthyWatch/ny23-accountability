---
name: propagation-sweep
description: After correcting a published claim (figure, date, quote, status, framing) in LangworthyWatch, sweep the whole corpus for the SAME claim in sibling files so the fix doesn't leave a stale, contradicting copy elsewhere. Use when the user says "did this propagate", "check siblings", "sweep for that figure", or right after applying a correction. Complements /fact-check-review (single-file verify) and /source-attribution-check (single-file missing-citation).
---

# Propagation sweep

A correction is not done until its **propagated copies** are fixed too. The single most common
error class in the cross-project ledger `public-ledger/docs/governance/ERROR_LOG.md` is a
corrected claim left **stale in a sibling file** — its examples include a wrong Federalist
Society EIN propagated ~9× across the corpus, and a matcher fix left stale in a book chapter.
On a *published* site, a fixed claim in one file plus the old version in another is a live
self-contradiction.

## When to use

- Immediately after applying any correction to a published entry (figure, dollar amount, date,
  quoted text, program status, entity name, or framing).
- Standalone, when the user wants to confirm a number/claim isn't duplicated stale elsewhere.
- As Step 6 of `/fact-check-review` (this is the reusable version of that step).

## Arguments

`$ARGUMENTS` = the thing that changed. Ideally give both the OLD value/phrasing and the entity,
e.g. `"$5B BRIC"` or `"BRIC canceled / no longer exists"` or `"Federalist Society EIN 53-0219498"`.
If no argument, ask what was corrected (old → new) and derive search terms from the OLD side.

## Process

1. **Derive search terms from the OLD (now-wrong) value**, not the new one — you're hunting the
   stale copies. Include: the old number(s) in a few formats (`$5B`, `$5 billion`, `5,000`),
   the old phrasing/status words, and the entity name.

2. **Sweep prose AND downstream consumers:**
   ```bash
   cd /Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker
   grep -rin -E '<old-term-1>|<old-term-2>|<entity>' content/ social-media/
   ```
   Cover: `content/fact-checks/`, `content/state-of-the-district/`, `content/correspondence/`,
   the social-card generators in `social-media/`, and any generated graphic data/JSON. Cards and
   dashboards are real propagation targets — a figure baked into a PNG script or `dashboard.json`
   is just as published as the prose.

3. **Filter false positives.** Substring noise is common and is itself the un-IDF'd-`MATCHER`
   class from the ERROR_LOG — e.g. a `BRIC` sweep matches "fa**bric**" / "fa**bric**ated". Read
   each hit in context; only count genuine references to the corrected claim.

4. **Report each real sibling** as `file:line` with the stale text and the corrected value it
   should carry. Flag it as an internal contradiction with the file already fixed.

5. **Fix the siblings with the SAME verified correction** (once the user has approved the
   original fix) — re-cite the same primary sources; do not re-derive. Then re-run the Hugo
   build to confirm the stale phrasing is gone from the rendered pages:
   ```bash
   hugo --source . --destination /tmp/lw_propcheck --gc --minify 2>&1 | grep -E 'Pages|ERROR'
   grep -rc '<old phrasing>' /tmp/lw_propcheck/<changed-page>/index.html   # expect 0
   ```

6. **If the corrected claim is a headline figure**, note it for the `ERROR_LOG.md` discipline:
   the public-ledger ledger logs `wrong → right` with the fix commit. (LangworthyWatch has no
   ERROR_LOG of its own yet; if the user wants one, mirror that format.)

## Notes

- Sweep on the OLD value; report against the NEW value.
- This is a content-integrity check, not a citation check — pair with `/source-attribution-check`
  (missing citations) and `/fact-check-review` (cited-source verification).
- Don't auto-fix siblings before the underlying correction itself is approved; once it is,
  fixing the stale copies is part of completing that same correction.
