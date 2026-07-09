# CLAUDE.md - Project Guide for AI Assistants

## Project Overview

**NY-23 Accountability Tracker** (https://langworthywatch.org) is a Hugo static site documenting statements and actions by Rep. Nick Langworthy (R-NY-23) using public records.

**Purpose:** Present facts side-by-side - what was said vs. what was done. No speculation, no opinion presented as fact.

**Tech Stack:**
- Hugo static site generator
- Custom theme (no Ananke dependency)
- CSS in `assets/css/bundle.css` (concatenated custom properties system)
- **Netlify hosting** at langworthywatch.org (NOT GitHub Pages, despite legacy `.github/workflows/hugo.yml` and the GitHub Pages config that still exists for the repo). The DNS-active CDN is Netlify Edge.
- Donorbox for donations
- Google Analytics for traffic

---

## Content Standards (CRITICAL)

### All entries MUST include:
1. **Primary sources** - Link to congress.gov, official websites, archived pages
2. **Archive.org URLs** - All sources archived for permanence
3. **Complete context** - Full quotes with dates and circumstances
4. **Factual accuracy** - Claims verified against multiple official sources
5. **"Why this matters" intro** - For complex topics, explain local relevance upfront
6. **Plain language summaries** - After data/tables, add "In plain language:" explanations
7. **County tags** - Add `counties: ["steuben", "chemung"]` for filtering
8. **Cross-links** - Link to related fact-checks at bottom of entries

### All entries must NOT:
- Make accusations of criminal conduct
- Speculate about motives or intentions
- Present opinion as fact
- Use anonymous or unverifiable sources
- Selectively edit quotes to change meaning

### Meetings and photos are not endorsements (fairness standard, added 2026-06-27)

A constituent, business, union, or advocacy group meeting with — or photographed with — the Representative is exercising access to federal representation, **not** endorsing his record; groups often meet precisely because they disagree. Accountability attaches to how Langworthy *frames* the meeting in his own messaging, never to the party who showed up. Never imply a group endorses him from a meeting or photo. Where the group's own public record contradicts his framing (e.g., the Cystic Fibrosis Foundation publicly opposing the bill he voted for), cite that record. Public-facing version: `content/methodology/_index.md` §5.

### Verdict Labels (for fact-checks)
Use these standardized verdicts:
- **TRUE** - Claim is accurate
- **MOSTLY TRUE** - Accurate but missing context
- **MISLEADING** - Technically accurate but creates false impression
- **MOSTLY FALSE** - Mostly inaccurate with minor accurate elements
- **FALSE** - Claim is factually incorrect
- **FALSE ATTRIBUTION** - Claim attributes something to wrong source/cause
- **CONTRADICTION** - Statement conflicts with documented actions
- **DEFLECTION** - Response avoids addressing the actual question
- **NON-RESPONSIVE** - Constituent concern not addressed
- **MISSING CONTEXT** - Key information omitted that changes meaning
- **DOCUMENTED PATTERN** - Recurring behavior established by multiple instances
- **NOT SUPPORTED** - Claim lacks evidence

### NY-23 Counties (for county tags)
Allegany, Cattaraugus, Chautauqua, Chemung, Erie, Schuyler, Steuben, Tioga

---

## Directory Structure

```
langworthy-tracker/
├── content/
│   ├── _index.md                    # Homepage content
│   ├── privacy.md                   # Privacy notice
│   ├── fact-checks/
│   │   ├── _index.md                # Fact-checks section index with summary table
│   │   ├── YYYY-MM-DD-slug.md       # Individual fact-checks
│   │   ├── _template-*.md           # Templates (draft: true)
│   │   └── example-entry.md         # Example (draft: true)
│   ├── correspondence/
│   │   ├── _index.md                # Correspondence section index
│   │   ├── submit.md                # Submission form page
│   │   └── letters/
│   │       ├── _TEMPLATE.md         # Letter template
│   │       └── YYYY-MM-DD-topic.md  # Individual letters
│   ├── votes/
│   │   └── _index.md                # Voting record (links to Congress.gov)
│   ├── missed-votes/
│   │   └── _index.md                # Missed votes summary
│   ├── campaign-finance/
│   │   └── _index.md                # Campaign finance data
│   └── methodology/
│       └── _index.md                # Site methodology and standards
├── static/
│   ├── css/custom.css               # Custom styles
│   ├── documents/                   # PDFs (letters, responses)
│   ├── images/
│   │   └── fact-checks/             # Screenshots for fact-checks
│   └── CNAME                        # Domain config
├── layouts/
│   ├── baseof.html                  # Base template (includes skip link)
│   ├── index.html                   # Homepage template
│   ├── _partials/
│   │   └── head-additions.html      # Analytics + custom CSS
│   └── shortcodes/
│       ├── correspondence-form.html # Letter submission form
│       └── document-form.html       # Document submission form
├── hugo.toml                        # Hugo configuration
└── themes/ananke/                   # Theme (don't modify directly)
```

---

## Adding Content

### New Fact-Check

1. Create file: `content/fact-checks/YYYY-MM-DD-descriptive-slug.md`

2. Use this frontmatter:
```yaml
---
title: "Short descriptive title"
date: YYYY-MM-DD
draft: false
topic: "Healthcare|Economy|Veterans|Immigration|Rule of Law|etc"
claim_date: "Month DD, YYYY"
source: "Press Release|Facebook Post|Constituent Letter Response|Interview|etc"
source_url: "https://original-source-url"
archived_url: "https://web.archive.org/web/..."
---
```

3. Structure:
```markdown
## Statement
**Source:** [Source type], [Date]
> "Exact quote here"

---

## Congressional Record / The Facts
[Verified data from official sources]

---

## Context
[Additional relevant information]

---

## Questions This Raises
1. [Question based on documented facts]

---

## Sources
* [Source name]: [URL]

---

**Note:** This entry documents publicly available information...
*Last updated: Month DD, YYYY*
```

4. If including images:
   - Save to `static/images/fact-checks/YYYY-MM-DD-slug-description.png`
   - Use Hugo figure shortcode with alt text:
   ```
   {{< figure src="/images/fact-checks/YYYY-MM-DD-slug-description.png" alt="Descriptive alt text" caption="Caption text" >}}
   ```

5. Archive all URLs via Wayback Machine:
   ```bash
   curl -I "https://web.archive.org/save/[URL]"
   ```

### New Correspondence Letter

1. Copy PDF to: `static/documents/YYYY-MM-DD-topic-response.pdf`

2. Create file: `content/correspondence/letters/YYYY-MM-DD-topic.md`

3. Use this frontmatter:
```yaml
---
title: "Topic - Response Status"
date: YYYY-MM-DD
draft: false
topic: "Healthcare|Immigration|Veterans|etc"
contact_date: "YYYY-MM-DD"
contact_method: "Email|Phone|Mail|Website Form"
response_received: "No Response Yet|Form Letter|Substantive Response"
days_waiting: 0
---
```

4. Include:
   - Contact information summary
   - Constituent's letter (redacted)
   - Response text (if received)
   - Link to PDF: `[Download PDF](/documents/YYYY-MM-DD-topic-response.pdf)`
   - Related fact-check link if applicable

### Updating Section Index Pages

When adding new content, update the relevant `_index.md`:
- **Fact-checks:** Update summary table in `content/fact-checks/_index.md`
- **Correspondence:** Update metrics and patterns in `content/correspondence/_index.md`

---

## Hugo Commands

```bash
# Development server (includes drafts)
hugo server -D

# Production build
hugo

# New content from archetype
hugo new fact-checks/YYYY-MM-DD-slug.md
```

---

## Git Workflow

1. Always work on `main` branch (deploys to GitHub Pages)
2. Commit messages should be descriptive
3. Include `Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>` in commits
4. Push triggers automatic deployment

```bash
git add [files]
git commit -m "$(cat <<'EOF'
Brief description

Detailed explanation if needed

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
EOF
)"
git push
```

---

## Important Files to Know

| File | Purpose |
|------|---------|
| `hugo.toml` | Site config, menu, analytics ID |
| `content/fact-checks/_index.md` | Summary table of all verdicts |
| `content/correspondence/_index.md` | Metrics and patterns |
| `static/css/custom.css` | All custom styling |
| `layouts/baseof.html` | Skip link, main template |
| `layouts/index.html` | Homepage with recent entries |

---

## Common Tasks

### Archive a URL
```bash
curl -s -I "https://web.archive.org/save/[URL]" | grep -i location
```

### Check for draft files (won't publish)
```bash
grep -l "draft: true" content/**/*.md
```

### Verify internal links
Check that `/fact-checks/slug/` and `/correspondence/letters/slug/` paths exist.

### Update correspondence metrics
Count letters: `ls content/correspondence/letters/*.md | grep -v "_TEMPLATE" | wc -l`

---

## Accessibility Requirements

- All images must have descriptive `alt` text
- Use semantic headings (h2, h3) in order
- Forms have associated labels
- Links are underlined and have visible focus states
- Skip-to-content link exists in baseof.html

---

## What NOT to Do

1. **Don't create files without reading existing examples first**
2. **Don't publish without archive URLs** - All sources must be archived
3. **Don't editorialize** - Present facts, let readers conclude
4. **Don't modify theme files** - Override in `layouts/` instead
5. **Don't commit sensitive data** - Redact personal info from letters
6. **Don't use speculation** - Only document what can be verified
7. **Don't add emojis** - Keep professional tone

---

## Redaction Guidelines

When processing constituent letters:
- Remove full names (use "Ms. [Redacted]" or initials)
- Remove addresses, phone numbers, email addresses
- Remove any identifying personal details
- Keep: dates, topics, office responses, tracking codes

---

## Quality Checklist

Before committing new content:
- [ ] Frontmatter complete and accurate
- [ ] All URLs archived via Archive.org
- [ ] Images have alt text
- [ ] Personal info redacted from letters
- [ ] Sources cited with links
- [ ] No speculation or opinion
- [ ] Related content cross-linked
- [ ] Section index updated if needed

---

## Pre-Publish Review (CRITICAL — added 2026-05-06)

**Why this section exists:** During a May 2026 audit pass, four recurring failure modes were caught in fact-check drafts *before* publication. Each had to be corrected after a careful reader spotted the issue. The patterns are predictable enough to enforce as a checklist. Run the `/fact-check-review <file>` slash command before committing any new fact-check, OR walk through this list manually. (A fifth mode — membership/affiliation claims taken from aggregators — was added after a June 13, 2026 review; a sixth — quotes attributed to a named person without confirmed authorship — after a July 3, 2026 correction.)

### The six failure modes to actively check for

1. **Tool summaries treated as primary-source quotes.** When a WebFetch on the source article fails (timeout, 403, paywall), do **not** silently substitute a WebSearch tool's summary or paraphrase as if it were the actual quote. The right move is to retry, dispatch a research agent, or omit the specific number/quote. Search summaries are *paraphrases by an LLM* — they are not citations. Symptom to watch for: a number cited in the fact-check that you cannot point to in the actual primary document.

2. **Inferred relationships from form fields that don't carry them.** The House Clerk's Gift Travel Filings index shows the *filer* of a sponsored-travel form, not the *traveler* and not the relationship to the Member. Inferring "spouse" or "staff" from the filer name is a guess. The authoritative source is the per-trip filing PDF itself. Symptom: any sentence that names a relationship (spouse, child, staff member) without an explicit source.

3. **Atmospheric detail without a source.** Adding "the helicopter had been in service since the 1970s" or similar background-color claims to make an entry read better is a credibility liability if the detail is wrong. If you cannot point to a specific cited source for a date, age, or descriptive fact, either find one or remove the detail. Symptom: a date, vintage, age, or descriptor in the entry body that you didn't see in the linked sources.

4. **Conflated numbers from different snapshots.** Subtracting an "original total invoice" from a "remaining balance after partial payments" produces a meaningless "shortfall." Always confirm that two numbers being compared (or used in arithmetic) refer to the same point in time and the same scope. Symptom: any derived figure (a difference, a ratio, a percentage) that requires combining two numbers from different sources or different time-points.

5. **Membership/affiliation claims taken from aggregators or pattern-matching.** Any "X is a cosponsor of," "X serves on," "X signed the letter," or "X endorsed" claim must be verified against the *authoritative* roster — for cosponsors, the congress.gov bill **cosponsors** list; for letter signatories, the actual letter PDF — **not** a secondary aggregator (GovTrack, billsponsor) and **not** inferred because *similar* entities qualify. These errors are categorical (the person isn't on the list at all), not imprecisions, and they look plausible, which is why they survive a casual read. Symptom: a cosponsor/member/signatory claim that "fits the pattern" but was never checked against the primary roster. Caught June 13, 2026: a draft asserted Langworthy cosponsored H.R. 6644 (sourced to GovTrack, flagged MEDIUM confidence); the congress.gov cosponsor list showed sponsor French Hill + 31 cosponsors — two *other* NY Republicans, but not Langworthy. Fix: verify at draft-time (cosponsorship is one congress.gov `/cosponsors` call), hedge it in the body if unverified, or omit it — never state it flat at less-than-confirmed.

6. **Quote attributed to a named person without confirmed authorship.** (Added July 3, 2026.) Any sentence that puts words in a specific person's mouth — "X posted," "X said," "X wrote" — must have the *author* confirmed from a primary artifact: the actual post, a clear screenshot of it, an archived URL, or the official account handle. **"Reads like their post" or "sounds like their politics" is not confirmation.** Symptom: a quoted statement attributed to the subject whose only source is a third-party-forwarded screenshot, a search summary, or an assumption about who is speaking. When a research agent explicitly flags authorship as unconfirmed, treat it as **blocking** — do not publish until the account is confirmed; if it can't be, hold the entry or attribute generically ("a post circulating from [best-known source]"). Caught July 3, 2026: a "misleading veterans" post was attributed to Langworthy and published; it was actually the **House Veterans' Affairs Committee GOP** account (he isn't even on that committee). The live entry had to be pulled, `_redirects`-301'd, and reframed around his actual Rules-vote record. This is the sixth mode and the reason the shared `LESSONS.md` carries "Verify a quote's AUTHOR before attributing it and publishing."

### Internal-consistency check

Before publishing, re-read the entry as a hostile copy editor:

- For every numbered point in a verdict section, check that the math in Point N doesn't contradict the math in Point N+1. (Example: Point 1 says "county money alone covered the purchase," Point 3 then says "Burke's contribution was the reason the county had enough." Those contradict.)
- For every quoted sentence, confirm the quote appears verbatim at the linked URL.
- For every dollar figure, confirm it appears in the cited source AND is described the same way (gross vs net, total vs remaining, encumbered vs available).
- For every "X days after Y" or "X months before Y" claim, do the date math by hand — these are easy to be off by one.

### When in doubt, hedge

If a finding rests on an inference (filer = staff, "almost certainly," "likely," "appears to be"), say so explicitly in the entry body. Inferences hedged honestly are defensible. Inferences stated as facts are credibility liabilities.

### How to invoke the review

```
/fact-check-review content/fact-checks/2026-MM-DD-slug.md
```

The slash command (defined in `.claude/commands/fact-check-review.md`) walks an Explore-style verification agent through the five failure modes against the entry. Use it before every commit to `content/fact-checks/`.

---

## Slash commands available in this project

Ten slash commands live under `.claude/commands/` (plus `/wrap` at the project root). The core ones work together as a fact-check pipeline:

| Command | When to use | Output |
|---|---|---|
| `/ny23-fact-check [topic]` | **Create** a new fact-check entry from a claim, statement, vote, or constituent letter | Drafted entry under `content/fact-checks/YYYY-MM-DD-slug.md` with `draft: true` and the right frontmatter / verdict structure |
| `/source-attribution-check [file]` | **Find unsourced claims** in a draft — quotes without attribution, statistics without citations, "experts say" without naming experts | Structured list of attribution gaps; non-blocking |
| `/tier-a-confirm [list-or-file]` | **Promote Tier-B claims to Tier-A** — parallelize verbatim-quote verification across 3-6 agents, each fetching a primary source. Run when a draft cites WebSearch summaries instead of primary documents | Per-claim status grid (CONFIRMED / PARTIAL / NEGATIVE / DEFERRED) + suggested edits to the draft entry |
| `/fact-check-review [file]` | **Pre-publish verifier** — runs the five-failure-mode checklist (see section above) | Critical / Recommended / Nice-to-have findings list; do NOT auto-edit |
| `/fec-donor-scan [name-or-cmte]` | **FEC donor + committee lookup** via the shared DuckDB index at `~/data/public-ledger/federal/fec/fec_index.duckdb`. Sub-second queries replacing 3-8 min grep | Donor rollup tables with cycle / committee / amount / N transactions |
| `/capture-findings [topic-or-mode]` | **Backlog tracking** for follow-ups that aren't doable now — Q2 FEC drops, Wayback retries, pending FOILs, story leads | Append to `FINDINGS_BACKLOG.md` with type / priority / action-date |
| `/news-scan` | **Web relevance sweep** — scan for new Langworthy / NY-23 / federal-bill developments, triage vs. existing entries, keep only net-new on-mission items | Dated digest; actionable hits routed to `/capture-findings` |
| `/campaign-graphic-brief [goal]` | **Accessible design spec** for a social card, produced before design work begins | Spec (not the graphic) for the `social-media/create_*_card.py` Pillow script |
| `/social-post [entry-or-topic]` | **Caption + card** for a fact-check in the house scorecard format (headline-first, verdict-consistent); runs the ≤2200-char and em-dash checks; builds the card on `social-media/lib/card.py` | A ready-to-post caption (with char count) + a rendered PNG (Desktop copy) |
| `/accessibility-audit [path/url]` | **WCAG 2.1 AA audit** of the Hugo site + social cards, mapped back to source files | Findings by severity, mapped to templates / CSS / content / cards |
| `/wrap` (project root) | Session wrap — closing summary | One-shot |

### Standard fact-check pipeline

1. `/ny23-fact-check [topic]` → drafts the entry
2. Manual research + drafting in the entry
3. `/source-attribution-check` → finds unsourced claims
4. `/tier-a-confirm` → promotes Tier-B claims to Tier-A via parallel agents
5. `/fact-check-review` → runs the five-failure-mode checklist
6. Apply Critical / Recommended findings; re-run `/fact-check-review` if substantive changes made
7. `scripts/archive_sources.sh` → archive cited URLs to Wayback
8. Update `content/fact-checks/_index.md` summary table
9. Flip `draft: false`, commit (`feat(...)`), push — Stop hook deploys to Cloudflare Pages
10. `/capture-findings` → log any follow-up items (Q2 data, Wayback retries, related leads)

### Notes on the ported commands (2026-06-08)

`/ny23-fact-check`, `/tier-a-confirm`, `/fec-donor-scan`, `/source-attribution-check`,
and `/capture-findings` were ported from public-ledger on 2026-06-08. The
upstream versions reference public-ledger paths (`research/kb/`, `CLAIMS.md`,
`FINDINGS_BACKLOG.md` at the PL root). The LW versions reference the
LW equivalents (`content/fact-checks/`, `content/fact-checks/_index.md`,
`langworthy-tracker/FINDINGS_BACKLOG.md`). `/fact-check-review` is native
to LW (added 2026-05-06).

---

## Entry Types and Patterns

### 1. Single-Claim Fact-Checks
Standard format: Statement > Data > Context > Questions > Sources. Use for individual claims from Facebook posts, press releases, constituent letters.

### 2. Multi-Claim Fact-Checks
For posts containing multiple distinct claims (e.g., SAVE Act with 3 claims). Structure each claim with its own verdict, then assign an overall verdict. Example: `2026-02-10-save-act-voter-id.md`

### 3. County Impact Profiles
Format established by Steuben (`2026-02-08-steuben-rural-impact-summary.md`) and Tioga (`2026-02-10-tioga-county-federal-impact.md`). Structure:
- **"Why This Matters for NY-23"** intro (brief, sets local relevance)
- **"What keeps rural systems running"** scene-setter
- **A/B/C impact sections** with italic preambles and "In plain language:" summaries
- **"What is still unaddressed"** table (signals restraint and seriousness)
- **Representation gap** section (town halls, votes, quotes)
- Key clarifier: distinguish county administration from federal causation
- Verdict: typically MISSING CONTEXT

### 4. Companion Summaries
Shorter entries that synthesize data from a parent fact-check for a specific audience (e.g., SNAP rural impact, Medicaid rural impact, VA rural impact). Link back to parent entry.

### Rural Framing Treatment
When applying to existing entries:
- Add "Why this matters in a rural district" intro paragraph
- Restructure into A/B/C impact buckets with italic preambles
- Add "In plain language:" translations after data-heavy sections
- Add "What is still unaddressed" table
- Add cross-links to companion/related entries
- Add county tags and verdict frontmatter fields

### Documented Rhetorical Patterns
Reference these when entries fit established patterns:
1. **Create the Problem, Blame Someone Else** — vote for cuts, blame consequences on others
2. **Take Credit for Opposition's Work** — announce grants from programs he didn't create
3. **Semantic Deception** — technically true framing that creates false impressions ("No SNAP cuts," "$31,500 tax free," "election integrity")
4. **Deflect to Biden/Democrats** — redirect constituent concerns
5. **Form Letter Non-Responses** — praise policy constituent opposed

---

## Facebook Graphics

### Production
- Python/Pillow scripts saved to `~/Downloads/create_[topic]_graphic.py`
- Output PNGs saved to `~/Downloads/`
- Standard dimensions: 1200x1100 or 1200x1200
- Dark theme (`#1e1e34` background), Impact font for numbers, Arial for text
- Two-column comparison format: green-tinted left ("What's claimed") vs. red-tinted right ("What the data shows")
- Evidence boxes at bottom with color-coded fills
- Verdict bar in gold/amber
- Footer: LangworthyWatch.org + sources + full fact-check URL

### Design Principles (from iterative feedback)
- Lead with what sounds reasonable before revealing the gap
- Use neutral dashes (not red X marks) for assumption labels
- Soften language in assumption lists (e.g., "seems straightforward" not "everyone can easily comply")
- Desaturate tradeoff/impact boxes to maintain visual hierarchy
- Put conservative sources first in source lines (Cato, Heritage before Brennan)
- Bump footer text contrast for mobile readability
- $15/month or dominant stat should visually dominate the right column
- Verdict tone: factual, not snarky — maximize cross-aisle shareability
- **No em dashes (—) in rendered card text.** They read as an AI tell and undercut the hand-made, factual feel. Replace contextually with a colon, comma, parentheses, period, or the middle dot (·) the design already uses. Hyphens in compound modifiers ('Medicaid-exposed') and arrows (→) are fine; only the em dash is the problem. (June 2026: the SOTD Q2 carousel was scrubbed of all 13; verify new/edited cards with `grep -F "—" social-media/create_*.py` before regenerating.)

### Facebook Post Text
- Lead with the popular/reasonable framing
- Use arrow bullets (→) not dashes
- **No em dashes (—) in post text**, for the same AI-tell reason; use a colon, comma, period, or parentheses instead
- Include specific dollar figures and data points
- End with full fact-check URL
- Tone: factual, not partisan — goal is "I support X, but this bill goes further than people think"

### Roundup / multi-claim post format (added July 2026, from supporter feedback)

Multi-claim and "scorecard" posts were burying the lede behind an appearance of precision. Lead with the verdict; the post's job is to be legible in ~10 seconds, with the receipts one click away on the entry.

- **Headline first** — the takeaway in one line (e.g., "128 fact-checks. His claims held up as accurate 4 times.").
- **Then scannable triplets:**
  ```
  CLAIM: <his quoted words>
  VERDICT: <label>
  <one sentence of the documented reality>
  ```
- **Verdict labels MUST match the published entry.** Never upgrade "Misleading" to "False" for punch — the mismatch is exactly what a hostile reader clicks through to catch, and the project's pitch is "check the record." Consistency is the credibility armor.
- **Framing precision:** say "held up as accurate N times," NOT "only X% completely accurate" ("not completely accurate" misreads as "false"; most verdicts are Missing Context / Misleading, not False).
- **Close** with "don't take our word for it, check his own votes and words" + the URL.

---

## Git and Deployment

### Push Method (Updated April 2026)

Use HTTPS with the `gh` credential helper — this is the reliable path:

```bash
# One-time setup (if needed):
gh auth setup-git

# Standard push:
git push origin main
```

Remote is set to HTTPS: `https://github.com/LangworthyWatch/ny23-accountability.git`

**Why not SSH:** The deploy key (`id_ed25519_langworthywatch` in `~/.ssh/config`) is read-only. Port 22 is currently unblocked but the `gh` credential helper (LangworthyWatch account, stored in keyring) is more reliable. Do not revert to SSH remote unless the credential helper stops working.

### Deploy Path — Cloudflare Pages (migrated 2026-06-14)

**The site is hosted on Cloudflare Pages** (project `langworthywatch`, served at `langworthywatch.pages.dev`), fronting `langworthywatch.org`. Migrated off Netlify on 2026-06-14 after Netlify hit a hard account credit/quota wall (deploys returned `JSONHTTPError: Forbidden`). Cloudflare Pages' free tier + `wrangler` **direct upload** sidesteps that **and** the flagged-GitHub-account problem — no Git integration; we build locally and upload `public/`.

**DNS:** `langworthywatch.org` is a Cloudflare-proxied CNAME → `langworthywatch.pages.dev` (zone in the Cloudflare account `airboat-webcast.5u@icloud.com`, ID `3b752cee282808bcfcebc84aaea9a1c3`). The MX/SPF/DKIM (Cloudflare Email Routing) + Google-verification TXT records are email-only — leave them.

**Manual deploy:**

```bash
cd /Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker
rm -rf public && hugo --gc --minify     # rm -rf: Hugo won't delete stale files; a prior `hugo -D` can leak draft pages into public/
npx -y pagefind --site public           # builds the /search/ full-text index into public/pagefind/ (must run after hugo, before deploy)
export CLOUDFLARE_ACCOUNT_ID=3b752cee282808bcfcebc84aaea9a1c3
wrangler pages deploy public --project-name=langworthywatch --branch=main --commit-dirty=true
```

wrangler is authenticated via `wrangler login` (OAuth, user-level creds). Re-run `wrangler login` if it lapses.

**Claude Code project hook:** the Stop hook (`.claude/scripts/auto-deploy.sh`) clean-builds + `wrangler pages deploy`s at session end when HEAD has changed (tracked in `.wrangler/last_deployed_sha`). So commits auto-deploy to Cloudflare Pages from the local session.

**Migration gotchas (already handled):** Pages needs `layouts/404.html` (the custom theme emitted none, so missing paths soft-200'd to the homepage) and `static/_headers` (ports the old netlify.toml security headers). Always clean-build (`rm -rf public`) before deploy.

*(Legacy/inert: Netlify site `68d48ede-fc40-4afc-9fdb-cb9f72737f02` is credit-blocked; the `.github/workflows/*` files no longer matter; `www.langworthywatch.org`'s CNAME may still point at Netlify and need repointing to Pages.)*

### Verifying a page is live

```bash
curl -sSI -m 10 "https://langworthywatch.org/fact-checks/<slug>/" | head -1
# Expect: HTTP/2 200
```

**Do not assume `git push` is sufficient.** Always verify the page is live afterward via the curl above OR by checking the most recent Netlify deploy (`netlify api listSiteDeploys --data='{"site_id":"68d48ede-fc40-4afc-9fdb-cb9f72737f02","per_page":1}'` — `commit_ref` should match the latest pushed commit).

### Repository
- Remote repo name: `LangworthyWatch/ny23-accountability` (not `langworthy-tracker`)
- Local directory: `langworthy-tracker/` (submodule within parent `Langworthywatch/`)
- Branch: `main` (deploys to GitHub Pages on push)

---

## County Coverage Status

| County | Profile Entry | Status |
|--------|--------------|--------|
| Steuben | `2026-02-08-steuben-rural-impact-summary.md` | Complete — rural framing applied |
| Tioga | `2026-02-10-tioga-county-federal-impact.md` | Complete |
| Allegany | `2026-02-08-allegany-county-grants-accord.md` | Partial (grants focus) |
| Chemung | — | Not started |
| Cattaraugus | — | Not started |
| Chautauqua | — | Not started |
| Erie | — | Not started (partial district overlap) |
| Schuyler | — | Not started |

---

## Cross-Site Pattern: IDA Data → The Public Ledgers

For IDA/subsidy data, cite [thepublicledgers.org](https://thepublicledgers.org) rather than hosting raw data on LangworthyWatch. Reason: LW carries a candidate identity (political framing); TPL is a journalism platform (credibility framing). Two fact-checks establish this pattern:

- `2026-03-21-ida-donor-exemption-pattern.md` — cites TPL for 74-donor/$246K/$66.2M data
- `2026-03-21-obbba-ida-vote.md` — cites TPL for county-level dashboards

Use LW to document the *legislative record* (votes, reform gaps, Langworthy's specific actions); use TPL for underlying data.

---

## Contact

- Site email: langworthywatch@gmail.com
- Repository: LangworthyWatch/ny23-accountability (private)
- Domain: langworthywatch.org

---

*Last updated: April 30, 2026*
