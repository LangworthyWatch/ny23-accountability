# Session Failure Log

Append-only. One section per session. Purpose is pattern detection across
sessions, not blame — a one-off slip is not worth logging, a failure that took
multiple attempts or a real course correction is.

---

## Session: 2026-09-01

**Project:** langworthy-tracker (NY-23 Accountability Tracker)

### Failures

**Research / verification**
- govinfo search API: returned a confident exact `count` (64 granules) that was incomplete — it missed three Extensions of Remarks outright, and on a spot-checked day (2026-07-21) returned zero of the seven granules that actually name Langworthy → abandoned the API for discovery and swept all 45 full-issue CREC PDFs instead (keyless `/content/pkg/.../pdf/`).
- govinfo `DEMO_KEY`: assumed 30 req/hour, actual limit is **10** → exhausted it mid-task; switched to keyless `/content/pkg/` endpoints, which have no limit.
- House Clerk roll-call XML: parsed `<totals-by-party>` (the Republican row) instead of `<totals-by-vote>`, producing implausible tallies like "214-0" for a previous-question vote → re-parsed from `<totals-by-vote>`; true figure 214-211.
- Erie County fine amount: took "$6,000 daily" from an Investigative Post article; the county's own Consumer Protection page says **"$1,000.00 to $5,000.00 per day"** → used the primary source. Named-outlet reporting is not a substitute for the ordinance.
- `pdftotext -layout` on CREC: layout mode interleaves the Record's three columns and garbles sentences → use plain `pdftotext` (reading order) for CREC.

**Accuracy in published/committed text**
- Gatekeeper entry: wrote "eight days earlier"; the committee reported June 8 and the floor debate was June 9, i.e. **one day** → corrected before commit. Date math by hand, every time.
- Gatekeeper entry: described three Jan. 6 record votes as all barring settlement payments to people convicted of assaulting officers; only RV 358 says that (RV 357 is the Judgment Fund, RV 359 is pardoned offenders later reconvicted) → narrowed to "restricting settlement or Judgment Fund payments connected to January 6."
- Gatekeeper entry: called the floor amendment "the same amendment" as committee RV 358; the floor text names DOJ as payer → hedged to "substantively the same measure" with the difference stated.
- **FINDINGS_BACKLOG Flock lead: claimed ALPRs saturate NY-23 without consulting `.claude/references/ny23-landmines.md` §7.** NY-23's Erie share is the Southtowns only; Buffalo, Cheektowaga, West Seneca and Lackawanna are NY-26, so nearly every jurisdiction in the source reporting is outside the district → caught during wrap and corrected (`18735fe`). This is the "correct fact, wrong neighbor" failure the landmines file exists to prevent. **The `content/fact-checks/` pre-publish hook does not fire on `FINDINGS_BACKLOG.md`, so nothing prompted the check.**

**Tooling**
- `scripts/archive_sources.sh`: accepted a file argument and silently ignored it (`extract_urls()` hardcoded the corpus glob), so every run submitted **1,224 URLs** → exhausted the Wayback rate limit mid-run; nine newly cited URLs remain unarchived. Fixed in `f6c8112`; a single entry now yields 17.
- Social card v1: put green on the "0" panel, inverting the house color logic (green reads as the good column, and the zero was the damning number), and collided two text runs in the left panel → rebuilt on the documented claim-left / record-right convention.
- Two `nohup … &` background jobs died silently with empty output when the parent shell exited → use the harness's `run_in_background`, or foreground with a generous timeout.
- Anchor verification: regex assumed `id="..."`; Hugo's minifier emits unquoted `id=...`, so a working in-page anchor was briefly reported as broken → verification tooling needs to match the *minified* output, not the source.
- `ls archive_log_*.txt`: zsh aborted the command on the unmatched glob before it ran (caught by the null-result guard) → quote the pattern or use `find -name`.
- `tac`: not present on macOS → `git log --reverse`.

**Environment (not self-inflicted, logged for pattern)**
- Cloudflare Pages deploy failed at 1,541/1,549 files with an opaque `Failed to upload files` → retry resumed from the uploaded set and completed in 5s.
- `git push` failed with `Could not resolve host: github.com`; `cloudflare.com` also unreachable, i.e. the machine was offline → deferred push via a wait-for-connectivity loop; landed ~3 min later.
- Chrome MCP refused an Investigative Post URL ("Could not verify this site's safety category") → in-app browser fetched it fine.
- Wayback Save Page Now returned 429/302/520 throughout the session → nine URLs still unarchived; retry when the window resets.

---
