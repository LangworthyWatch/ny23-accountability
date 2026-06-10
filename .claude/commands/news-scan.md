---
name: news-scan
description: Scan the web for recent Langworthy / NY-23 / federal-bills-affecting-NY developments relevant to LangworthyWatch's active work, triage them against existing fact-checks, and produce a dated digest of net-new, actionable items. Use when the user says "scan for news/updates/developments", "what's new on Langworthy", "any developments on [bill or topic]", "check the web for anything relevant", "news scan", or wants a periodic relevance sweep. Derives watch-targets from `content/fact-checks/_index.md` + the curated NY-23 outlet list below, web-searches each, keeps only what is NEW (grep-verified vs existing entries) and on-mission, and routes actionable hits to `/capture-findings`. Web hits are INDICATIVE leads → route to a primary-source pull, never cite as primary.
---

# News Scan — web relevance sweep against the active fact-check corpus

Find recent, on-mission developments and turn them into triaged leads. The hard
part is **relevance + novelty**, not search: derive watch-targets *from the
corpus*, keep only what's genuinely **new** and **in-scope**, and route each hit to
the right next step. **Triage, not truth** — grep-verify novelty, tier honestly
(web = INDICATIVE), respect any HOLD / recusal flags.

> **⚠️ Ported from public-ledger 2026-06-08.** Upstream version is geared toward
> public-ledger's TRIGGER_REGISTRY / FOIA_TRACKER / RIGHT_OF_REPLY infrastructure.
> The LW port is centered on Langworthy press releases, House Clerk roll-call
> votes, federal bills affecting NY state law, and the NY-23 local-press
> outlets curated below.

## Arguments

- no argument → whole-portfolio sweep (top watch-targets, default window: last ~2 weeks)
- a topic / bill / event → focus the sweep there (e.g., "SECURE Data Act updates",
  "Langworthy June 2026", "NY-23 nursing home news")
- a window phrase ("since 2026-05-20", "last month") → override the default window

## Step 1 — Build the watch-target list (from the corpus + curated outlets)

Derive targets so the sweep stays on-mission and de-dupes against what's covered:

```bash
cd /Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker

# Recent published fact-checks (what's already covered)
ls -t content/fact-checks/*.md | head -15

# Recent commits (signals where attention has been)
git log --oneline -10

# Existing index entries (topic coverage)
grep -E '^\| \[' content/fact-checks/_index.md | head -20

# Cross-link any open follow-ups
[ -f FINDINGS_BACKLOG.md ] && grep -A2 "^### " FINDINGS_BACKLOG.md | head -30
```

### Canonical Langworthy/NY-23 watch-targets

These are **always-on** targets — sweep these every run unless the user scopes:

| Target | What to watch | Primary URL |
|---|---|---|
| Langworthy press releases | New statements, votes, credit-claims | https://langworthy.house.gov/media/press-releases |
| Langworthy social (Facebook, X) | Posts that could be fact-checked | facebook.com/CongressmanNickLangworthy + X profile |
| House Clerk roll-call votes | Langworthy's votes since last sweep | https://clerk.house.gov/Votes |
| Federal bills affecting NY law | New cosponsorships / preemption bills | congress.gov advanced search |
| NY State Senate / Assembly | NY laws that federal bills would preempt | nysenate.gov |
| House E&C committee | Hearings on bills Langworthy cosponsors | energycommerce.house.gov |
| House Energy Subcommittee | Same | energycommerce.house.gov/subcommittees |

### NY-23 local-press outlets (priority sources for fact-check leads)

Per `reference_buffalo_journalists` memory — start any Erie / Buffalo / NY-23
story by checking these bylines first:

| Outlet | Beat / strength | County coverage |
|---|---|---|
| Buffalo News | Lorigo+machine beat (Specht); broad WNY | Erie (NY-23 edge) |
| Investigative Post | Oversight (Heaney, Keith); rigorous | Erie + WNY |
| WIVB | FOIL-litigation appetite; TV broadcast | Erie + WNY |
| WRFA | Jamestown radio (Chautauqua) | Chautauqua |
| Post-Journal | Jamestown / Chautauqua daily | Chautauqua |
| WENY | Elmira TV (Chemung / Steuben) | Chemung, Steuben |
| Olean Times Herald | Olean daily | Cattaraugus, Allegany |
| Wellsville Sun | Wellsville daily | Allegany |
| MyTwinTiers | Chemung / Steuben / Tioga TV | Chemung, Steuben, Tioga |
| Fingerlakes1 / FingerLakesDailyNews | Schuyler / Tioga edges | Schuyler, Tioga |
| MyHometownToday | Local digital | Chautauqua, Cattaraugus |
| Spectrum Local News | Western NY TV | All of NY-23 |
| Audacy NewsRadio 930 WBEN | Buffalo radio | Erie + WNY |

Assemble a ranked target list:
- **(a) Recent Langworthy statements / votes / cosponsorships** (highest value)
- **(b) NY state laws that federal preemption bills would override** (pattern context)
- **(c) Specific bills tracked by existing fact-checks** that have new procedural
  action (markups, hearings, floor votes)
- **(d) Press from the NY-23 outlet list above** mentioning Langworthy in the window

**Cap to ~12-15 targets/run** to bound web calls; note what you dropped.

## Step 2 — Scan the web (bounded)

For each target, `WebSearch` (US-only; it's current-month-aware) with a recency-biased
query (entity/topic + "2026" + the event type). `WebFetch` only the 2-3 most
promising results per target to confirm **the development, its date, and the
outlet**. Prefer primary/reputable outlets; skip aggregators/SEO chum. Keep web
calls proportional to the target count (don't fan out unboundedly).

## Step 3 — Triage each hit (the load-bearing step)

For every candidate development:

1. **Novelty (grep-verify):** `grep -rIil "<entity/event>" content/fact-checks/` —
   keep only genuine 0-coverage / materially-newer items. Drop what's already
   covered in an existing fact-check entry.

2. **Relevance:** which Langworthy / NY-23 angle it touches (name it).
   Drop off-mission hits — pure national politics with no NY-23 angle is out.

3. **Tier:** web reporting = **INDICATIVE** — never a primary cite. Note the
   primary source it points to (a filing, vote, press release, bill text) for
   a follow-up pull via `/tier-a-confirm` or `/fec-donor-scan`.

4. **Verdict candidate:** what verdict label (MISLEADING / CONTRADICTION /
   DOCUMENTED PATTERN / MISSING CONTEXT etc.) does this look like at first
   read? Tag for the user — don't commit, but the tag helps prioritize.

5. **Flags:** any conflict-of-interest concern, any recusal-adjacent topic
   (Erie-touching investigations per Beaudoin candidacy disclosure — see
   public-ledger root CLAUDE.md if uncertain).

## Step 4 — Write the digest

Write a dated digest to `langworthy-tracker/research/news-scan-YYYY-MM-DD-{scope}.md`
(create the `research/` directory if it doesn't exist):

```markdown
# News scan — {scope} ({YYYY-MM-DD}, window {since→now})
**Targets scanned:** N (dropped M for cap/COI: …)

## 🚨 Time-sensitive / action-required
- {development} → activates {pending fact-check, FOIL, deadline}. Action: …

## Net-new, on-mission developments
| Date | Development | Outlet | Topic / angle | Candidate verdict | Primary-source pull | Action |
|---|---|---|---|---|---|---|

## Seen but already covered / off-mission (dropped)
- {item} — already in `content/fact-checks/2026-XX-XX-slug.md` / off-mission

## Suggested next steps
1. …
```

## Step 5 — Route

- Offer to `/capture-findings` the actionable rows into `FINDINGS_BACKLOG.md`.
- For high-priority leads (e.g., a new Langworthy statement that contradicts a
  recent vote), offer to spawn `/ny23-fact-check` directly.
- For a hit with a clear primary source, hand to `/tier-a-confirm` or the
  relevant pull (`/fec-donor-scan` for donor questions, House Clerk for votes,
  GovInfo for bill text).

## Cadence

On-demand by default. For recurring runs, compose with **`/schedule`** (cron
remote agent) or **`/loop`** (interval). A weekly portfolio sweep + targeted
sweeps after a major Langworthy press event are the natural cadences.

## Rules

- **Web = INDICATIVE lead, never a primary cite.** Every kept hit names the
  primary source to pull next. A news scan produces *leads*, not corpus claims.
- **Grep-verify novelty** before listing anything as "new" — the corpus already
  covers a lot.
- **Cap the web calls** — 12-15 targets, 2-3 fetches per target.
- **Cite outlet + date** for every hit; flag single-source / partisan outlets.
- **Respect recusal flags** — for Erie-County-touching topics, defer per the
  Beaudoin candidacy protocol in public-ledger root CLAUDE.md. LW work that
  references Erie indirectly (e.g., Langworthy press conferences in Buffalo)
  is generally fine — direct Erie political race coverage is the line.
