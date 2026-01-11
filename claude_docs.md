# LangworthyWatch - Complete Technical Documentation

## Project Overview

**LangworthyWatch** (NY-23 Accountability Tracker) is an independent research project that documents statements and actions by New York's 23rd Congressional District representative using publicly available government records. The site presents facts side-by-side to enable constituent accountability.

**Live Site**: https://langworthywatch.org
**Repository**: https://github.com/LangworthyWatch/ny23-accountability
**Framework**: Hugo (Static Site Generator)
**Status**: Active / Manually Updated

---

## Project Philosophy

### Core Principles
1. **Independent Research** - No campaign affiliation
2. **Public Records Only** - All sources are government websites
3. **All Sources Verified** - Primary sources linked and archived
4. **No Opinion** - Present facts, let constituents judge
5. **Full Context** - Never cherry-pick quotes
6. **Transparency** - Methodology documented publicly

### Anti-Disinformation Standards
- Every entry must have primary source links
- All URLs archived to Archive.org
- Screenshots saved locally as backup
- Full quotes with complete context
- Verification checklist before publishing
- No speculation or opinion presented as fact

---

## Project Structure

### Directory Organization

```
/Users/zachbeaudoin/Langworthywatch/
├── 📁 langworthy-tracker/        # Hugo static site (PUBLIC)
│   ├── .git/                     # Git repo: github.com/LangworthyWatch/ny23-accountability
│   ├── content/                  # Hugo content
│   │   ├── _index.md             # Homepage
│   │   ├── fact-checks/          # Statement vs. action comparisons
│   │   ├── votes/                # Voting record documentation
│   │   ├── methodology/          # Verification standards
│   │   └── correspondence/       # Constituent letter examples
│   ├── themes/ananke/            # Hugo theme
│   ├── static/                   # Static assets
│   ├── archetypes/               # Content templates
│   ├── hugo.toml                 # Hugo configuration
│   ├── .gitignore
│   └── README.md
│
└── 📁 scraper/                   # Data collection tools (PRIVATE)
    ├── scrapers/
    │   ├── congressional_site.py # Press release scraper
    │   └── congress_gov.py       # Voting record scraper
    ├── utils/
    │   └── archiver.py           # Archive.org integration
    ├── storage/
    │   ├── raw_statements/       # Collected data (pending review)
    │   ├── verified/             # Verified, ready to publish
    │   └── archives/
    │       └── screenshots/      # Screenshot evidence
    ├── review_queue.py           # Interactive verification tool
    ├── run_scraper.py            # Master script (parallel execution)
    ├── requirements.txt          # Python dependencies
    ├── venv/                     # Virtual environment
    └── README.md                 # Scraper documentation
```

### Repository Organization (Resolved January 2026)

The projects are now properly separated:
- **Langworthywatch Hugo site**: `/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/`
- **Disability Wiki (Wiki.js)**: `/Users/zachbeaudoin/projects/disability-wiki/`

Each project has its own git repository with no content overlap.

---

## Hugo Static Site

### Configuration (hugo.toml)

```toml
baseURL = 'https://langworthywatch.org/'
languageCode = 'en-us'
title = 'NY-23 Accountability Tracker'
theme = 'ananke'

[params]
  description = 'Documenting NY-23 representation through public records'

[menu]
  [[menu.main]]
    name = 'Home'
    url = '/'
    weight = 1
  [[menu.main]]
    name = 'Fact Checks'
    url = '/fact-checks/'
    weight = 2
  [[menu.main]]
    name = 'Voting Record'
    url = '/votes/'
    weight = 3
  [[menu.main]]
    name = 'Methodology'
    url = '/methodology/'
    weight = 4
```

### Content Structure

#### Homepage (`content/_index.md`)
```markdown
---
title: "NY-23 Accountability Tracker"
description: "Documenting NY-23 representation through public records"
---

## About This Site

Documents statements and actions using publicly available government records.

Facts side-by-side: what was said vs. what was done.
All sources linked and archived for verification.
```

#### Fact-Check Template (`archetypes/fact-checks.md`)
```markdown
---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: false
categories: ["fact-check"]
tags: []
---

## The Statement

**Date**: [Date of statement]
**Source**: [Link to press release/tweet/etc]
**Archive**: [Archive.org URL]

> [Exact quote]

## The Record

**Vote**: [Bill number and title]
**Date**: [Vote date]
**Source**: [Congress.gov link]
**Archive**: [Archive.org URL]

Rep. Langworthy voted: [YES/NO]

## Context

[Full context of both statement and vote]

## Sources

1. [Primary source 1]
2. [Congress.gov link]
3. [Archive links]
```

---

## Scraper System

### Python Scrapers (PRIVATE - Not in Public Git)

#### 1. Congressional Site Scraper
**File**: `scraper/scrapers/congressional_site.py`

**Scrapes from**: https://langworthy.house.gov/media/press-releases

**What it collects**:
- Press release titles
- Publication dates
- Full text content
- Source URLs
- Metadata

**Output**: JSON files in `storage/raw_statements/`

**Features**:
- ✅ Avoids duplicates
- ✅ Extracts full article text
- ✅ Saves with timestamps
- ✅ Handles pagination
- ✅ Respects robots.txt

#### 2. Congress.gov Scraper
**File**: `scraper/scrapers/congress_gov.py`

**Scrapes from**: https://www.congress.gov

**What it collects**:
- Voting records
- Bill summaries
- Sponsor information
- Vote date and result
- Member-specific votes

**Output**: JSON files in `storage/raw_statements/`

**Features**:
- ✅ Filters to specific member
- ✅ Gets recent votes
- ✅ Links to official sources
- ✅ Structured data output

#### 3. Parallel Scraper (Optimized)
**File**: `scraper/run_scraper.py`

Runs both scrapers concurrently using `ThreadPoolExecutor`:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_press = executor.submit(scrape_press_releases, 20)
        future_votes = executor.submit(scrape_votes, 20)

        releases, press_saved = future_press.result()
        votes, vote_saved = future_votes.result()
```

**Performance**: 50% faster than sequential scraping

---

## Archive & Verification System

### Archive.org Integration
**File**: `scraper/utils/archiver.py`

**Features**:
- ✅ Saves URLs to Wayback Machine
- ✅ Checks if already archived
- ✅ Optional screenshot capability
- ✅ Permanent evidence preservation
- ✅ Returns archive URLs

**Usage**:
```python
from utils.archiver import Archiver

archiver = Archiver()

# Archive a URL
archive_url = archiver.archive_url("https://langworthy.house.gov/...")

# Archive with screenshot
result = archiver.archive_with_screenshot(url, take_screenshot=True)
```

### Review Queue
**File**: `scraper/review_queue.py`

Interactive CLI tool for verifying collected statements.

**Features**:
- Shows full statement context
- Verification checklist
- Actions: Publish / Discard / Later
- Organizes into verified/ folder

**Commands**:
- `[p]` - Publish (move to verified)
- `[d]` - Discard (not useful)
- `[l]` - Later (keep in queue)
- `[v]` - View again
- `[q]` - Quit

**Verification Checklist**:
1. ✓ Source URL verified and accessible
2. ✓ Archived to Archive.org
3. ✓ Full context preserved (not cherry-picked)
4. ✓ Relevant for accountability tracking
5. ✓ Can be cross-referenced with votes/actions

---

## Workflow

### Daily Collection (Manual Process)

#### 1. Morning: Run Scrapers
```bash
cd /Users/zachbeaudoin/Langworthywatch/scraper

# Activate virtual environment
source venv/bin/activate

# Run scrapers in parallel
python run_scraper.py

# Or run individually:
python scrapers/congressional_site.py
python scrapers/congress_gov.py
```

#### 2. Afternoon: Review Collected Data
```bash
# Interactive review
python review_queue.py
```

Actions:
- Review each collected statement
- Mark for publishing (moves to `verified/`)
- Discard irrelevant items
- Keep interesting items for later research

#### 3. Research: Find Contradictions
Manual process:
1. Read verified statements
2. Look for strong claims (e.g., "I always support X")
3. Search voting records for contradictions
4. Verify full context
5. Collect all sources
6. Archive everything to Archive.org

#### 4. Create Fact-Check Entry
```bash
cd /Users/zachbeaudoin/Langworthywatch/langworthy-tracker

# Create new entry
hugo new content/fact-checks/2024-12-21-topic.md

# Edit the file
# Fill in: statement, vote record, context, sources
```

#### 5. Publish to GitHub
```bash
# Preview locally
hugo server -D

# Build for production
hugo

# Commit and push
git add content/fact-checks/2024-12-21-topic.md
git commit -m "Add fact-check: topic description"
git push origin main
```

**GitHub Actions will automatically deploy to langworthywatch.org**

---

## Setup & Installation

### Hugo Site Setup

#### 1. Install Hugo
```bash
# macOS
brew install hugo

# Verify installation
hugo version
```

#### 2. Clone Repository
```bash
cd /Users/zachbeaudoin/Langworthywatch

# If not already cloned:
git clone https://github.com/LangworthyWatch/ny23-accountability.git langworthy-tracker
cd langworthy-tracker
```

#### 3. Install Theme
```bash
# Ananke theme should already be in themes/
# If missing:
git submodule update --init --recursive
```

#### 4. Run Development Server
```bash
hugo server -D

# Access at http://localhost:1313
```

#### 5. Build for Production
```bash
hugo

# Output in public/ directory
```

### Scraper Setup

#### 1. Navigate to Scraper Directory
```bash
cd /Users/zachbeaudoin/Langworthywatch/scraper
```

#### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

**Requirements**:
- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `selenium` - (Optional) Screenshot capability

#### 4. (Optional) Install ChromeDriver for Screenshots
```bash
brew install --cask chromedriver
```

#### 5. Run Your First Scrape
```bash
python run_scraper.py
```

---

## Content Standards

### Every Entry Must Include

1. **Exact Quote with Date**
   - Verbatim text
   - Publication date
   - Primary source link
   - Archive.org archived URL
   - Screenshot (saved locally)

2. **Voting Record or Action**
   - Bill number and title
   - Vote date
   - How member voted
   - Congress.gov link
   - Archive.org archived URL

3. **Full Context**
   - Complete statements (not excerpts)
   - Bill summary (what it actually does)
   - Any clarifications needed
   - Related context

4. **No Speculation**
   - Only documented facts
   - No assumptions about intent
   - No opinion presented as fact
   - Let readers draw conclusions

---

## Deployment

### GitHub Pages Deployment

**Repository**: https://github.com/LangworthyWatch/ny23-accountability

**Configuration**:
1. GitHub Actions workflow (`.github/workflows/hugo.yml`)
2. Builds on push to `main` branch
3. Deploys to GitHub Pages
4. Custom domain: langworthywatch.org

### DNS Configuration

**CNAME Record**:
```
langworthywatch.org → langworthywatch.github.io
```

**File**: `static/CNAME`
```
langworthywatch.org
```

### GitHub Pages Settings
- **Source**: GitHub Actions
- **Custom domain**: langworthywatch.org
- **Enforce HTTPS**: ✓ Enabled

---

## Git Workflow

### Commit Message Format
```bash
# New fact-check entry
git commit -m "Add fact-check: [topic description]"

# Update entry
git commit -m "Update fact-check: [what changed]"

# Site improvements
git commit -m "Improve methodology page clarity"

# Fix errors
git commit -m "Fix: correct date on healthcare vote entry"
```

### Branch Strategy
- **main** - Production (auto-deploys)
- **draft** - Work in progress (optional)

### Before Each Push
```bash
# Check for errors
hugo

# Preview changes
hugo server -D

# Verify all links work
# Verify all archives exist
# Read through entry for accuracy
```

---

## Security & Anonymity

### Maintaining Anonymity (If Desired)

#### 1. Separate GitHub Account
- Use ProtonMail for email
- Don't link to personal GitHub
- No identifying information in commits

#### 2. Scraper is PRIVATE
- **Never commit scraper to public repo**
- Keep in `/Users/zachbeaudoin/Langworthywatch/scraper/`
- Add to `.gitignore` if needed

#### 3. Only Publish Verified Hugo Content
- Public repo contains ONLY Hugo site
- No scraper code
- No raw collected data
- No personal information

#### 4. Domain Privacy
- Use domain privacy protection
- Register with separate email
- No WHOIS personal info

### Legal & Ethical Notes

✅ **This is legal**:
- Scraping public government websites
- Archiving public statements
- Research using public records
- Publishing factual information

✅ **Best practices**:
- Respect robots.txt
- Reasonable scraping delays
- Only collect public information
- Document everything with sources
- Full context always
- No speculation

---

## Troubleshooting

### Hugo Issues

#### "command not found: hugo"
```bash
brew install hugo
```

#### Theme not loading
```bash
git submodule update --init --recursive
```

#### Changes not showing
```bash
# Clear Hugo cache
hugo --gc

# Rebuild
hugo server -D
```

### Scraper Issues

#### No statements found
- Congressional website structure changed
- Check URLs are current
- Inspect HTML and update selectors

#### Archive.org not working
- Rate limiting (wait a few minutes)
- Archive.org may be down
- Check https://status.archive.org

#### Screenshots failing
- ChromeDriver not installed
- Chrome version mismatch
- Install: `brew install --cask chromedriver`

### Git Issues

#### Wrong remote repository
```bash
# Check current remote
git remote -v

# Should show:
# origin  https://github.com/LangworthyWatch/ny23-accountability.git

# If wrong, update:
git remote set-url origin https://github.com/LangworthyWatch/ny23-accountability.git
```

---

## Maintenance Tasks

### Weekly
- [ ] Run scrapers to collect new statements
- [ ] Review queue for interesting content
- [ ] Check Archive.org links still work
- [ ] Monitor site analytics (if configured)

### Monthly
- [ ] Review all archive links
- [ ] Update Hugo and theme if needed
- [ ] Check for broken links
- [ ] Review methodology for improvements

### Quarterly
- [ ] Full site audit
- [ ] Update any outdated information
- [ ] Consider new features/improvements
- [ ] Backup all collected data

---

## Future Enhancements

### Planned Features
- [ ] Automated scraping (GitHub Actions/cron)
- [ ] Email notifications for new statements
- [ ] Auto-flag potential contradictions
- [ ] Search functionality
- [ ] Category filtering
- [ ] Timeline view
- [ ] RSS feed

### Technical Improvements
- [ ] CI/CD for automated testing
- [ ] Link checking automation
- [ ] Archive verification automation
- [ ] Screenshot comparison tool
- [ ] Database for structured data
- [ ] API for programmatic access

---

## Content Strategy

### Phase 1: Foundation (Weeks 1-4)
- Collect 10-15 strongest examples
- Perfect verification process
- Document methodology thoroughly
- Get trusted reviewers
- Zero factual errors

### Phase 2: Soft Launch (Week 5)
- Publish first 10 entries
- Share on r/Buffalo
- Post in WNY political groups
- Send to local journalists
- Monitor response

### Phase 3: Growth (Month 3+)
- Regular weekly updates
- Growing readership
- Media citations
- Accountability conversations in district

---

## Success Metrics

### Credibility Metrics
- ✓ Zero successful challenges to accuracy
- ✓ Trusted reviewers approve all entries
- ✓ All sources remain accessible
- ✓ Methodology is transparent

### Impact Metrics
- Site traffic (GitHub Pages insights)
- Social media shares
- Media mentions
- Constituent engagement
- Local political discourse

---

## Resources

### Hugo Documentation
- **Official Docs**: https://gohugo.io/documentation/
- **Ananke Theme**: https://github.com/theNewDynamic/gohugo-theme-ananke
- **Hugo Forums**: https://discourse.gohugo.io/

### Government Resources
- **Congress.gov**: https://www.congress.gov
- **Langworthy's Site**: https://langworthy.house.gov
- **Archive.org**: https://web.archive.org

### Tools
- **Archive.org Save Page**: https://web.archive.org/save
- **BeautifulSoup Docs**: https://www.crummy.com/software/BeautifulSoup/
- **Python Requests**: https://requests.readthedocs.io/

---

## Contact

**Organization**: LangworthyWatch
**GitHub**: https://github.com/LangworthyWatch
**Repository**: https://github.com/LangworthyWatch/ny23-accountability
**Site**: https://langworthywatch.org

---

## Project Status

**Current Status**: Active, manually updated
**Launch Date**: TBD (building foundation first)
**Content Published**: 0 fact-checks (in research phase)
**Data Collected**: Ongoing scraping

**Next Milestones**:
1. Complete first 10 bulletproof fact-checks
2. Get peer review
3. Soft launch on r/Buffalo
4. Build consistent update schedule

---

*Last Updated: January 6, 2026*
*Hugo Version: Latest*
*Documentation Version: 1.0*
