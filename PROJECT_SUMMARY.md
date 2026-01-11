# Langworthy Accountability Tracker - Project Summary

## What You Built

A professional, cost-effective accountability tracker for Rep. Nicholas Langworthy (NY-23) that documents contradictions between public statements and congressional voting record.

**Live Site:** https://langworthywatch.org
**Cost:** $7.50/year (domain only)

---

## Features

### ✅ Live Website
- Custom domain with HTTPS
- Professional design (Hugo + Ananke theme)
- Automatic deployment via GitHub Actions
- Mobile-responsive

### ✅ Content Management
- **5 Published Fact-Checks:**
  1. Epstein files transparency contradiction
  2. Rural hospitals Medicaid cuts
  3. Government shutdown/ACA subsidies
  4. SALT tax relief
  5. Veterans support

- **Methodology Page:** Establishes credibility with clear standards
- **Voting Record Page:** Ready for integration

### ✅ Data Collection & Analysis
- **Press Release Scraper:** Collects claims from langworthy.house.gov
- **Archive Integration:** Permanent evidence via Archive.org
- **Vote Database:** 1,603 congressional votes imported and analyzed
- **Vote Analysis Tool:** Search and categorize votes by topic

###  Tools & Scripts

#### Press Release Scraper
```bash
cd /Users/zachbeaudoin/Langworthywatch/scraper
source venv/bin/activate
python3 scrapers/congressional_site.py
```

#### Vote Analysis Tool
```bash
cd /Users/zachbeaudoin/Langworthywatch/scraper
python3 analyze_votes.py
```

Exports votes as JSON to `/langworthy-tracker/data/votes.json`

---

## Project Structure

```
Langworthywatch/
├── langworthy-tracker/          # Hugo website
│   ├── content/
│   │   ├── fact-checks/         # Individual fact-check entries
│   │   ├── methodology/         # Standards & corrections policy
│   │   └── votes/               # Voting record page
│   ├── data/                    # Vote data exports (JSON)
│   ├── static/                  # Images, CNAME file
│   └── themes/ananke/           # Site theme
│
└── scraper/                     # Data collection tools
    ├── scrapers/                # Press release & vote scrapers
    ├── data/                    # Raw data (votes CSV)
    ├── storage/                 # Collected statements
    ├── analyze_votes.py         # Vote analysis tool
    └── requirements.txt         # Python dependencies
```

---

## Workflow: Adding New Fact-Checks

### 1. Collect Claims (15 min/week)
```bash
cd /Users/zachbeaudoin/Langworthywatch/scraper
source venv/bin/activate
python3 scrapers/congressional_site.py
```

Review collected statements in `storage/raw_statements/`

### 2. Research Votes (15 min)
- Visit: https://www.congress.gov/member/nicholas-langworthy/L000600
- Search for relevant votes
- Or use: `python3 analyze_votes.py` to search vote database

### 3. Create Fact-Check Entry (30 min)
```bash
cd /Users/zachbeaudoin/Langworthywatch/langworthy-tracker
hugo new content/fact-checks/YYYY-MM-DD-topic-name.md
```

Follow this template:
```markdown
---
title: "Descriptive Title"
date: YYYY-MM-DD
draft: false
topic: "Healthcare" # or Immigration, Tax, etc.
claim_date: "Month YYYY"
source: "Press Release / Statement"
---

## Statement
[Quote and source]

## Congressional Record
[Votes and actions]

## Context
[Local impact, what happened]

## Sources
[All citations]
```

### 4. Publish (1 min)
```bash
git add content/fact-checks/your-new-entry.md
git commit -m "Add fact-check: descriptive title"
git push
```

Site updates automatically within 1-2 minutes!

---

## Vote Database Features

The vote analysis tool (`analyze_votes.py`) can:

1. **Search by keyword:**
```python
from analyze_votes import VoteAnalyzer
a = VoteAnalyzer()
immigration_votes = a.search_votes(['immigration', 'border'])
```

2. **Filter by vote type:**
```python
# Find all NO votes on healthcare
health_no = a.search_votes(['health'], vote_type='Nay')
```

3. **Categorize by topic:**
```python
topics = a.votes_by_topic()
# Returns: Healthcare, Immigration, Tax, Veterans, Energy, Budget, etc.
```

4. **Export for website:**
```python
a.export_for_site()  # Creates data/votes.json
```

---

## Monthly Maintenance

**Time:** ~1 hour/month
**Goal:** 1-2 new fact-check entries

1. **Week 1:** Run press release scraper, review claims
2. **Week 2:** Research voting record for contradictions
3. **Week 3:** Write and publish fact-check entry
4. **Week 4:** Monitor and respond to any feedback

---

## Technical Details

### Hosting & Deployment
- **Hosting:** GitHub Pages (free)
- **Domain:** Cloudflare ($7.50/year)
- **SSL:** Automatic via GitHub Pages
- **CI/CD:** GitHub Actions (Hugo workflow)

### Dependencies
- **Hugo:** v0.140+ (static site generator)
- **Python 3:** For scrapers and analysis
- **Git:** Version control

### API Status
- ❌ ProPublica Congress API - Deactivated
- ❌ GovTrack API - Returns 403
- ❌ Congress.gov scraping - Anti-bot measures
- ✅ Manual research - Most reliable and credible

---

## Security & Privacy

- **Anonymous publication:** LangworthyWatch GitHub account
- **Privacy-protected domain:** Through Cloudflare
- **Evidence preservation:** All sources archived
- **Version control:** Full history in Git

---

## Future Enhancements (Optional)

### Easy Additions:
1. **Add search functionality** to website
2. **Create topic tags** for fact-checks
3. **Email notifications** when new press releases published
4. **Social media cards** for sharing

### Advanced (if needed):
1. **Interactive vote explorer** on website
2. **Automated claim detection** using NLP
3. **Analytics dashboard** (visitor stats)
4. **RSS feed** for fact-checks

---

## Key Files

### Website Content
- `/langworthy-tracker/content/fact-checks/*.md` - Published fact-checks
- `/langworthy-tracker/content/methodology/_index.md` - Standards page
- `/langworthy-tracker/hugo.toml` - Site configuration

### Data & Tools
- `/scraper/data/langworthy_votes.csv` - Complete voting record (1,603 votes)
- `/scraper/analyze_votes.py` - Vote analysis tool
- `/scraper/scrapers/congressional_site.py` - Press release scraper

### Deployment
- `/.github/workflows/hugo.yml` - Automatic deployment
- `/static/CNAME` - Custom domain configuration

---

## Support Resources

### Guides Created
- `/scraper/MANUAL_COLLECTION_GUIDE.md` - Manual research workflow
- `/scraper/PROPUBLICA_SETUP.md` - API setup (deprecated)
- `/ENABLE_GITHUB_PAGES.md` - Deployment setup

### Quick Commands
```bash
# Preview site locally
cd /Users/zachbeaudoin/Langworthywatch/langworthy-tracker
hugo server -D

# Create new fact-check
hugo new content/fact-checks/$(date +%Y-%m-%d)-topic-name.md

# Deploy to production
git push origin main
```

---

## Achievements 🎉

✅ Professional accountability website live
✅ Cost under $10/year
✅ Automated deployment pipeline
✅ 5 documented contradictions published
✅ 1,603 votes imported and searchable
✅ Evidence permanently archived
✅ Anonymous publication maintained
✅ Credible methodology established

**You've built a fully functional, sustainable accountability tracker!**

---

*Last updated: January 11, 2026*
