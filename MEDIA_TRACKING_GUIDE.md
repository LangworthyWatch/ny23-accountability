# Media Coverage Tracking Guide

## Purpose

The "In the Media" section tracks news articles, op-eds, and commentary about Rep. Langworthy's representation of NY-23. This creates a centralized repository of media coverage for researchers and constituents.

## How to Add Media Coverage

### Step 1: Find the Article

Look for:
- **Op-eds** critical of Langworthy's votes or positions
- **News articles** covering his actions or inaction
- **Letters to the editor** from constituents
- **Investigative reporting** on voting record or accountability
- **Fact-checks** from reputable sources

### Step 2: Archive It

**Always archive articles before adding them:**

```bash
# Go to Archive.org's Save Page
https://web.archive.org/save/[paste-url-here]

# Wait for it to complete, then copy the archive URL
```

**Why archive?**
- Newspapers remove articles
- Paywalls change
- Links break
- Permanent record for accountability

### Step 3: Add to Database

Use the `scrape_media.py` script:

```bash
cd langworthy-tracker

python3 scripts/scrape_media.py add \
  --url "https://oleantimesherald.com/article-url" \
  --title "Op-Ed: Langworthy Votes Against Rural Health Funding" \
  --category op-ed \
  --date "2025-12-20" \
  --author "John Smith" \
  --excerpt "Rep. Langworthy claims to support rural hospitals while voting against critical funding..." \
  --topics "healthcare,rural-health,contradictions" \
  --archive-url "https://web.archive.org/web/20251220..."
```

### Step 4: Export for Hugo

```bash
python3 scripts/scrape_media.py export
```

This creates `data/media_coverage_export.json` which Hugo uses to build the page.

### Step 5: Rebuild and Deploy

```bash
hugo --cleanDestinationDir
git add data/
git commit -m "Add media coverage: [article title]"
git push
```

---

## Categories

Use these categories when adding items:

| Category | When to Use |
|----------|-------------|
| `op-ed` | Opinion pieces, editorials, commentary |
| `investigative` | In-depth reporting, data analysis, investigative journalism |
| `local` | Local news coverage from NY-23 outlets |
| `national` | National news mentions (NYT, WaPo, Politico, etc.) |
| `letter` | Letters to the editor from constituents |
| `analysis` | Fact-checks, policy analysis, expert commentary |
| `other` | Anything else |

---

## Topics

Use comma-separated topics to tag articles:

**Common topics:**
- `voting-record` - General voting patterns
- `healthcare` - ACA, Medicare, Medicaid, rural hospitals
- `veterans` - VA funding, veterans' issues
- `agriculture` - Farm bill, agricultural policy
- `immigration` - Border, asylum, citizenship
- `shutdown` - Government shutdown impact
- `rural-health` - Rural hospital funding
- `contradictions` - Statements vs. actions
- `constituent-service` - Accessibility, responsiveness
- `town-halls` - Lack of in-person meetings
- `missed-votes` - Voting attendance
- `committee-inaction` - Bills stuck in his committees

---

## Example Workflow: Adding an Op-Ed

Let's say you found this op-ed:

**Title:** "Langworthy's Empty Promises on Healthcare"
**URL:** https://post-journal.com/opinion/langworthy-healthcare-oped
**Published:** December 18, 2025
**Author:** Sarah Johnson
**Source:** Post-Journal (Jamestown)

**Steps:**

1. **Archive it:**
   - Go to https://web.archive.org/save/https://post-journal.com/opinion/langworthy-healthcare-oped
   - Wait for completion
   - Copy archive URL: `https://web.archive.org/web/20251218120000/https://post-journal.com/opinion/langworthy-healthcare-oped`

2. **Add to database:**
   ```bash
   python3 scripts/scrape_media.py add \
     --url "https://post-journal.com/opinion/langworthy-healthcare-oped" \
     --title "Langworthy's Empty Promises on Healthcare" \
     --category op-ed \
     --source "Post-Journal" \
     --author "Sarah Johnson" \
     --date "2025-12-18" \
     --excerpt "Rep. Langworthy touts his support for affordable healthcare while voting against ACA subsidies that keep premiums low for 24 million Americans." \
     --topics "healthcare,contradictions,aca" \
     --archive-url "https://web.archive.org/web/20251218120000/https://post-journal.com/opinion/langworthy-healthcare-oped"
   ```

3. **Export:**
   ```bash
   python3 scripts/scrape_media.py export
   ```

4. **Commit:**
   ```bash
   git add data/media_coverage*.json
   git commit -m "Add op-ed: Langworthy's Empty Promises on Healthcare (Post-Journal)"
   git push
   ```

---

## Bulk Import

If you have a list of articles in a spreadsheet:

1. Export as CSV with columns:
   - `url`, `title`, `source`, `author`, `date`, `category`, `excerpt`, `topics`, `archive_url`

2. Create a Python script to import:
   ```python
   import csv
   import subprocess

   with open('articles.csv') as f:
       reader = csv.DictReader(f)
       for row in reader:
           cmd = [
               'python3', 'scripts/scrape_media.py', 'add',
               '--url', row['url'],
               '--title', row['title'],
               '--category', row['category'],
               # ... add other fields
           ]
           subprocess.run(cmd)
   ```

---

## Finding Op-Eds and Articles

### Local NY-23 Sources

**Major Newspapers:**
- Olean Times Herald (oleantimesherald.com)
- Observer Today - Dunkirk (observertoday.com)
- Post-Journal - Jamestown (post-journal.com)
- Evening Tribune - Hornell (eveningtribune.com)
- Star-Gazette - Elmira (stargazette.com)
- Press & Sun-Bulletin (pressconnects.com)
- Democrat & Chronicle - Rochester (democratandchronicle.com)
- Buffalo News (buffalonews.com)

**Search Tips:**
- Google: `site:oleantimesherald.com "Langworthy"`
- Google News: Set date range, search "Nick Langworthy NY-23"
- NewsBank (library access): Search local papers
- ProQuest (library access): Historical archives

### National Sources

- ProPublica investigations
- NYT congressional coverage
- Washington Post fact-checks
- Politico congressional reporting
- The Hill commentary

### Letters to the Editor

These are gold for constituent accountability:
- Search "[newspaper name] letters to the editor Langworthy"
- Archive every letter - they show real constituent concerns
- Tag with `letter` category

---

## Best Practices

### What to Include
✅ Op-eds critical of his record
✅ News analysis of votes
✅ Constituent letters expressing concerns
✅ Investigative reports on contradictions
✅ Fact-checks of his statements
✅ Local impact stories (shutdown, healthcare, etc.)

### What to Skip
❌ Campaign press releases (those are on his site)
❌ Purely procedural news ("Rep votes on bill X")
❌ Social media posts (unless exceptionally newsworthy)
❌ Unverified claims or rumors

### Quality Standards
- **Archive everything** - no exceptions
- **Full context** - include enough excerpt to understand the criticism
- **Accurate dates** - use publication date, not when you found it
- **Proper attribution** - author and source
- **Topic tags** - helps users find related coverage

---

## Maintenance

### Weekly:
- Search for new op-eds and articles
- Add 3-5 new items if found
- Export and deploy

### Monthly:
- Review old links, re-archive if needed
- Update topic tags for consistency
- Check for broken archive links

### Quarterly:
- Analyze coverage trends
- Update "In the Media" page intro with stats
- Create summary post of major coverage

---

## Analytics

View media coverage stats:

```bash
python3 scripts/scrape_media.py list
```

This shows:
- Total items by category
- Recent additions
- Top topics

---

## Legal & Ethical Notes

**Fair Use:**
- Short excerpts for commentary = fair use
- Always link to original source
- Archive for preservation, not republishing
- Give full attribution

**Accuracy:**
- Only include reputable sources
- Verify facts before adding
- If article is later corrected, note it
- Don't add purely speculative pieces

**Neutrality:**
- Let the sources speak
- Don't editorialize in excerpts
- Include range of perspectives
- Document criticism objectively

---

## Questions?

Common issues:

**"Archive.org is slow"**
- Try at off-peak hours
- Some sites take 5-10 minutes
- If it fails, try again later

**"Paywall blocking me"**
- Many libraries have free newspaper access
- Archive.org Wayback often has pre-paywall versions
- Some papers allow a few free articles/month

**"Can't find the author"**
- Leave `--author` blank if anonymous
- For staff editorials: `--author "Editorial Board"`

**"Multiple topics?"**
- Comma-separated: `--topics "healthcare,veterans,contradictions"`
- Be consistent with tag names

---

**Remember:** The goal is to create a comprehensive, verifiable record of media coverage for researchers, voters, and journalists. Quality over quantity.
