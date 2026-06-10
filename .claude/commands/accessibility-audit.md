---
name: accessibility-audit
description: Run a WCAG 2.1 AA accessibility audit on the LangworthyWatch Hugo site (langworthywatch.org), mapping findings back to source files (templates, content, shortcodes, CSS) rather than compiled HTML. Also audits the social-media/*.png cards for palette-contrast compliance. Use when the user wants to audit the site for accessibility, mentions WCAG / a11y / contrast, or says `/accessibility-audit` with a site path / URL / card path. Designed for the LangworthyWatch Hugo project but most of the skill is generic.
---

# Accessibility Audit — LangworthyWatch site + social cards

Run a WCAG 2.1 AA accessibility audit on the LangworthyWatch Hugo site, mapping
findings back to source files (templates, content, shortcodes, CSS) rather than
compiled HTML. Also audits the `social-media/*.png` card library for
LW-palette-contrast compliance.

> **⚠️ Ported and adapted from public-ledger 2026-06-08.** The upstream version
> uses the Beaudoin / ECL D11 campaign palette (navy #1B2A4A / cream #F5F0E8 /
> red #C41E3A) and audits the campaign site. The LW port uses the
> LangworthyWatch social-card palette (see `/campaign-graphic-brief` for the
> full table) and audits the langworthywatch.org Hugo site + the
> `social-media/` PNG cards.

## When to use

- User wants to audit the LW site for accessibility
- User mentions WCAG, a11y audit, accessibility compliance
- User says `/accessibility-audit` with a site path, URL, or card path
- After Hugo template changes that could affect accessibility
- Before any major deployment (Stop hook auto-deploy makes this less of a
  manual gate; treat as periodic rather than per-deploy)
- After adding new social-media/*.png cards

## Arguments

`$ARGUMENTS` is a site directory, URL, or PNG path. Examples:
- "langworthy-tracker/" (default Hugo site root)
- "http://localhost:1313"
- "https://langworthywatch.org"
- "social-media/secure_data_act_contradiction.png" (audit one card)
- "social-media/" (audit all cards)
- "full audit before deploy"
- no argument: audit the Hugo site at langworthy-tracker/

---

## Context

The LangworthyWatch site is a fact-checking platform. Accessibility failures
undermine the journalistic credibility of the publisher. Per the project
CLAUDE.md, "Accessibility Requirements" mandates: all images have descriptive
alt text, semantic headings in order, forms have associated labels, links are
underlined with visible focus states, skip-to-content link exists in baseof.html.

axe-core covers ~57% of WCAG criteria automatically; the remaining 43% require
human review. Clearly distinguish machine-verified findings from items flagged
for human review.

## Step 1: Start Hugo dev server (Hugo audit only)

```bash
cd /Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker
hugo server --port 1313 --disableLiveReload &
HUGO_PID=$!
sleep 2

# Verify server is running
curl -s -o /dev/null -w "%{http_code}" http://localhost:1313/
```

If the site is already running, a URL is provided, or only PNG cards are being
audited, skip this step.

## Step 2: Run automated audits (Hugo site)

### pa11y-ci (sitemap-based, full site)

```bash
pa11y-ci \
  --sitemap http://localhost:1313/sitemap.xml \
  --standard WCAG2AA \
  --reporter json \
  > pa11y_results.json
```

### axe-core (page-by-page, detailed)

```bash
# Audit homepage
npx @axe-core/cli http://localhost:1313/ --stdout > axe_home.json

# Audit key pages
npx @axe-core/cli http://localhost:1313/fact-checks/ --stdout >> axe_results.json
npx @axe-core/cli http://localhost:1313/correspondence/ --stdout >> axe_results.json
npx @axe-core/cli http://localhost:1313/methodology/ --stdout >> axe_results.json

# Audit a recent fact-check (sample)
npx @axe-core/cli http://localhost:1313/fact-checks/2026-06-06-langworthy-secure-data-act-hr8413/ --stdout >> axe_results.json
```

For full-site audit, iterate over sitemap URLs:

```bash
curl -s http://localhost:1313/sitemap.xml | \
  grep -oP '<loc>\K[^<]+' | \
  while read url; do
    npx @axe-core/cli "$url" --stdout
  done > axe_full_results.json
```

## Step 3: Map findings to Hugo source files

Compiled HTML findings must be traced back to source files:

| Compiled location | Hugo source |
|-------------------|-------------|
| `<html lang="">` | `layouts/baseof.html` |
| Skip link | `layouts/baseof.html` |
| `<h1>` - `<h6>` hierarchy | Content file in `content/fact-checks/` + `layouts/_default/single.html` |
| `<img>` without alt | Content file Markdown or `layouts/_partials/` |
| Form labels | `layouts/shortcodes/` (correspondence-form, document-form) |
| Focus styles | `assets/css/_accessibility.css`, `_layout.css`, `_nav.css` |
| Sticky header | `layouts/baseof.html` + `assets/css/_nav.css` |
| Link text | Content file in `content/` |

### Mapping method

1. Inspect the compiled HTML element with the finding
2. Check if it comes from a template (`layouts/baseof.html`, `layouts/_partials/`)
3. Check if it comes from content Markdown (`content/fact-checks/`)
4. Check if it comes from a shortcode (`layouts/shortcodes/`)
5. Check CSS source for styling-related findings (`assets/css/_*.css`)

## Step 4: WCAG criteria checklist

| # | Criterion | Check | Method | WCAG |
|---|-----------|-------|--------|------|
| 1 | Language declared | `<html lang="en">` present | Automated | 3.1.1 |
| 2 | Page titles | Every page has unique, descriptive `<title>` | Automated | 2.4.2 |
| 3 | Heading hierarchy | No skipped levels per page | Automated | 1.3.1 |
| 4 | Skip navigation | Skip-to-content link in baseof.html | Automated | 2.4.1 |
| 5 | Image alt text | All `<img>` have non-empty `alt` (including Hugo figure shortcode) | Automated | 1.1.1 |
| 6 | Color contrast | 4.5:1 normal text, 3:1 large text | Automated | 1.4.3 |
| 7 | Keyboard navigation | All interactive elements keyboard-accessible | Semi-auto | 2.1.1 |
| 8 | Focus indicators | No `outline: none` without replacement style | Automated | 2.4.7 |
| 9 | Form labels | Visible `<label>` for correspondence-form / document-form inputs | Automated | 1.3.1, 4.1.2 |
| 10 | Link purpose | Flag "click here", "read more", "learn more" | Automated | 2.4.4 |
| 11 | Target size | Interactive targets ≥ 24×24 CSS px | Semi-auto | 2.5.8 |
| 12 | Focus not obscured | Sticky headers don't cover focused elements | Human review | 2.4.11 |
| 13 | Text resize | Content readable at 200% zoom, no horizontal scroll | Human review | 1.4.4 |

## Step 5: LW social-card palette contrast checks

The LW palette is used in both the Hugo site CSS AND the `social-media/*.png`
cards (which `/campaign-graphic-brief` specs). Run these greps:

```bash
# Check CSS for any combo of LW palette pairs (verify safe ones haven't been changed; flag risky ones)
cd langworthy-tracker
grep -rn "#E53E3E\|#1E3A5F\|#D69E2E\|#F5F7FA\|#FFFFFF\|#1A202C" assets/css/

# Also scan content/fact-checks/ for inline styles (rare)
grep -rn "style=\"color:" content/fact-checks/ | head
```

### LW palette pre-verified contrast table

(Same as in `/campaign-graphic-brief` Step 2; reproduced here for the audit
context. Approximate values — verify with WebAIM if scaling fonts smaller.)

| Pair | Approx ratio | AA Normal | AA Large | Status |
|------|--------------|-----------|----------|--------|
| DARK `#1A202C` on BG `#F5F7FA` | ~16:1 | ✅ | ✅ | Safe (body text) |
| NAVY `#1E3A5F` on BG | ~12:1 | ✅ | ✅ | Safe (headlines) |
| WHITE on NAVY | ~13:1 | ✅ | ✅ | Safe (header / footer) |
| WHITE on RED `#E53E3E` | ~4.4:1 | ⚠️ borderline | ✅ | OK only if text ≥18pt bold |
| GOLD `#D69E2E` on NAVY | ~3.6:1 | ❌ FAIL | ✅ Large | Only as bold 16pt+ |
| **RED on NAVY** | ~3.5:1 | ❌ | ⚠️ | **NEVER use as text pairing** |

```bash
# Specifically flag if RED + NAVY appear adjacent in any text color combo
grep -rn "color.*#E53E3E\|color.*#1E3A5F" assets/css/ static/css/
```

### Form-specific checks (correspondence submission, document submission)

The two forms LW has are in `layouts/shortcodes/correspondence-form.html` and
`document-form.html`. Audit those for:

- [ ] Every `<input>` has an associated `<label>` (not just placeholder text)
- [ ] Required fields indicated without color alone
- [ ] Error messages associated with inputs via `aria-describedby`
- [ ] Submit button has descriptive text (not just "Submit")

## Step 6: Audit `social-media/*.png` cards (PNG audit)

LW social cards are generated by `social-media/create_*_card.py` scripts. To
audit them:

### Option A: Spot-check via the generator script

```bash
cd langworthy-tracker
# List all card-generator scripts
ls social-media/create_*.py

# For each, the palette is defined at the top of the file as
# BG = "#F5F7FA", NAVY = "#1E3A5F", etc.
# Grep for any deviation from the standard palette:
grep -hn "^BG\|^NAVY\|^RED\|^GREEN\|^GOLD\|^WHITE" social-media/create_*.py | sort | uniq -c
```

Any palette value that differs from the standard table above warrants review.

### Option B: Render audit using a visual contrast tool

```bash
# Render a single card and pass to a contrast-checking tool
# (most rigorous: re-render the card and run a visual contrast scan)
python3 social-media/create_secure_data_act_card.py
# Then visual inspection or contrast-checker (e.g., Color Oracle for color
# blindness simulation, WebAIM Contrast Checker for measured ratios)
```

### Alt text audit for cards

Cards are typically posted with alt text via the platform's image upload flow
(Facebook, Instagram, etc.). If `/alt-text-writer` was run for the card, the
alt text should be in the corresponding fact-check entry's frontmatter or in
a `social-media/alt-text-[slug].md` companion file. Verify per-card alt text
exists before posting.

## Step 7: Generate report

### Severity levels

| Severity | Meaning | Action |
|----------|---------|--------|
| CRITICAL | Blocks access for entire user group | Fix before next deploy |
| HIGH | Significant barrier, workaround may exist | Fix before next deploy |
| MEDIUM | Partial barrier, most users can proceed | Fix within 1 week |
| LOW | Best practice improvement | Fix in next update |

### Report format

```markdown
# Accessibility Audit — LangworthyWatch
**Date:** [YYYY-MM-DD]
**Standard:** WCAG 2.1 Level AA
**Tools:** axe-core [version], pa11y-ci [version]
**Pages audited:** [N Hugo pages] + [N social-media PNGs]

## Summary

| Severity | Count | Auto-verified | Needs Human Review |
|----------|-------|---------------|-------------------|
| CRITICAL | [N] | [N] | [N] |
| HIGH | [N] | [N] | [N] |
| MEDIUM | [N] | [N] | [N] |
| LOW | [N] | [N] | [N] |

## Hugo site findings

### [Finding 1 Title]
**Severity:** CRITICAL
**WCAG:** [Criterion number and name]
**Verification:** [Automated / Human review required]
**Source file:** `layouts/baseof.html:15`
**Page(s):** [affected URLs]

**Issue:** [Description]

**Remediation:**
```html
<!-- Before -->
<nav>...</nav>

<!-- After -->
<nav aria-label="Main navigation">...</nav>
```

---

## Social-card findings

### [Card name] — [Finding]
**Severity:** MEDIUM
**Source:** `social-media/create_<slug>_card.py:<line>`
**Issue:** [e.g., "GOLD on NAVY used at 14pt regular weight — fails AA Large by 0.3"]
**Remediation:** Bump to 16pt Arial Bold, re-render via `python3 social-media/create_<slug>_card.py`

---

## Human Review Required

These items cannot be fully verified by automated tools:

- [ ] Alt text quality — are descriptions meaningful, not just present? (1.1.1)
- [ ] Keyboard trap — can users tab through all interactive elements? (2.1.2)
- [ ] Reading order — does content make sense when linearized? (1.3.2)
- [ ] Focus not obscured — does sticky header cover focused elements? (2.4.11)
- [ ] Text resize — readable at 200% zoom without horizontal scroll? (1.4.4)
- [ ] Target size — all touch/click targets at least 24×24 CSS pixels? (2.5.8)

## Passing Checks

| Check | Status | Method |
|-------|--------|--------|
| Language declaration | ✅ `lang="en"` present | Automated |
| Skip navigation | ✅ Present in baseof.html | Automated |
| ... | ... | ... |
```

## Step 8: Stop Hugo server

```bash
kill $HUGO_PID 2>/dev/null
```

## Re-audit triggers

Run after:
- Any file in `layouts/` changes (template accessibility)
- CSS/SCSS files change (contrast, focus styles)
- New content pages added (alt text, heading hierarchy)
- New `social-media/create_*.py` cards added
- Before any major Hugo theme update

## Coverage limitations

axe-core and pa11y-ci together cover approximately 57% of WCAG 2.1 AA criteria.
The remaining 43% require human review. This audit clearly marks which findings
are machine-verified and which are flagged for human review.

Key areas NOT covered by automation:
- Alt text quality (presence is checked, meaningfulness is not — use `/alt-text-writer`)
- Keyboard trap detection (basic tab order checked, complex traps are not)
- Reading order in complex layouts
- Cognitive load and plain language
- PNG-card text contrast (since the text is rasterized, automated checks don't
  reach into pixel-level OCR; rely on the palette table + spot-checks)

## Do NOT

- Report the site as "fully WCAG compliant" based on automated tools alone
- Skip human review items — they cover the most impactful barriers
- Ignore GOLD-on-NAVY or RED-on-NAVY contrast failures regardless of element size
- Audit compiled HTML without mapping back to Hugo source files
- Run audit against langworthywatch.org production URL without also checking
  local (template changes may not be deployed)
- Treat placeholder text as a substitute for visible form labels
- Mix the Beaudoin / ECL D11 campaign palette (#1B2A4A / #F5F0E8 / #C41E3A)
  into the LW audit — different visual brand
