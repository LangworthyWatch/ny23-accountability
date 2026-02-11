# CLAUDE.md - Project Guide for AI Assistants

## Project Overview

**NY-23 Accountability Tracker** (https://langworthywatch.org) is a Hugo static site documenting statements and actions by Rep. Nick Langworthy (R-NY-23) using public records.

**Purpose:** Present facts side-by-side - what was said vs. what was done. No speculation, no opinion presented as fact.

**Tech Stack:**
- Hugo static site generator
- Custom theme (no Ananke dependency)
- CSS in `assets/css/bundle.css` (concatenated custom properties system)
- GitHub Pages deployment
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

### Facebook Post Text
- Lead with the popular/reasonable framing
- Use arrow bullets (→) not dashes
- Include specific dollar figures and data points
- End with full fact-check URL
- Tone: factual, not partisan — goal is "I support X, but this bill goes further than people think"

---

## Git and Deployment

### SSH Configuration
Port 22 to GitHub is frequently blocked. Use the port 443 SSH config:
```bash
# If push fails on port 22, set remote to use port 443:
git remote set-url origin git@github-langworthy-443:LangworthyWatch/ny23-accountability.git
git push
```

SSH hosts configured in `~/.ssh/config`:
- `github-langworthy` — port 22 (often blocked)
- `github-langworthy-443` — port 443 via ssh.github.com (reliable fallback)
- Both use `~/.ssh/id_ed25519_langworthywatch`

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

## Contact

- Site email: langworthywatch@gmail.com
- Repository: LangworthyWatch/ny23-accountability (private)
- Domain: langworthywatch.org

---

*Last updated: February 11, 2026*
