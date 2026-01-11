# LangworthyWatch - Quick Reference Guide

Fast reference for common operations.

---

## 🚀 Quick Start

### Hugo Site
```bash
cd /Users/zachbeaudoin/Langworthywatch/langworthy-tracker
hugo server -D
# Access at http://localhost:1313
```

### Scraper
```bash
cd /Users/zachbeaudoin/Langworthywatch/scraper
source venv/bin/activate
python run_scraper.py
```

---

## 📁 File Locations

| Item | Location |
|------|----------|
| **Hugo Site** | `/Users/zachbeaudoin/Langworthywatch/langworthy-tracker/` |
| **Scrapers** | `/Users/zachbeaudoin/Langworthywatch/scraper/` |
| **Content** | `langworthy-tracker/content/fact-checks/` |
| **Config** | `langworthy-tracker/hugo.toml` |
| **Raw Data** | `scraper/storage/raw_statements/` |
| **Verified Data** | `scraper/storage/verified/` |

---

## 🕷️ Scraper Commands

### Run All Scrapers (Parallel)
```bash
cd scraper
source venv/bin/activate
python run_scraper.py
```

### Run Individual Scrapers
```bash
# Press releases only
python scrapers/congressional_site.py

# Votes only
python scrapers/congress_gov.py
```

### Review Collected Data
```bash
python review_queue.py
```

Actions:
- `[p]` - Publish (move to verified)
- `[d]` - Discard
- `[l]` - Later
- `[v]` - View again
- `[q]` - Quit

### Archive URLs
```python
from utils.archiver import Archiver

archiver = Archiver()
archive_url = archiver.archive_url("https://langworthy.house.gov/...")
```

---

## 🌐 Hugo Commands

### Development Server
```bash
cd langworthy-tracker
hugo server -D
# Access: http://localhost:1313
```

### Create New Entry
```bash
# New fact-check
hugo new content/fact-checks/2024-12-21-topic.md

# New vote entry
hugo new content/votes/2024-12-21-bill.md
```

### Build for Production
```bash
hugo

# Output in public/ directory
```

### Clean Build
```bash
hugo --gc  # Garbage collection
hugo       # Rebuild
```

---

## 📝 Git Workflow

### Check Status
```bash
git status
git log --oneline -5
```

### Commit New Entry
```bash
git add content/fact-checks/2024-12-21-topic.md
git commit -m "Add fact-check: topic description"
git push origin main
```

### View Remote
```bash
git remote -v
# Should show: github.com/LangworthyWatch/ny23-accountability
```

---

## 🔍 Content Creation Workflow

### 1. Collect Data (Morning)
```bash
cd scraper
source venv/bin/activate
python run_scraper.py
```

### 2. Review Data (Afternoon)
```bash
python review_queue.py
# Mark items for publishing
```

### 3. Research (Manual)
- Read verified statements
- Find contradictions with votes
- Collect all sources
- Archive everything

### 4. Create Entry
```bash
cd ../langworthy-tracker
hugo new content/fact-checks/YYYY-MM-DD-topic.md
```

Template:
```markdown
---
title: "Title Here"
date: 2024-12-21
draft: false
---

## The Statement
**Date**: Dec 15, 2024
**Source**: [Press Release](URL)
**Archive**: [Archive.org](URL)

> Exact quote here

## The Record
**Vote**: H.R. 1234 - Bill Title
**Date**: Dec 10, 2024
**Source**: [Congress.gov](URL)
**Archive**: [Archive.org](URL)

Rep. Langworthy voted: NO

## Context
Full context here...

## Sources
1. [Link 1]
2. [Link 2]
```

### 5. Preview & Publish
```bash
# Preview locally
hugo server -D

# Build
hugo

# Commit and push
git add content/fact-checks/YYYY-MM-DD-topic.md
git commit -m "Add fact-check: topic"
git push origin main
```

---

## 🌍 URLs & Access

| Resource | URL |
|----------|-----|
| **Live Site** | https://langworthywatch.org |
| **Local Hugo** | http://localhost:1313 |
| **GitHub Repo** | https://github.com/LangworthyWatch/ny23-accountability |
| **Congress.gov** | https://www.congress.gov |
| **Langworthy Site** | https://langworthy.house.gov |
| **Archive.org** | https://web.archive.org |

---

## 🔧 Setup Commands

### Hugo Setup (First Time)
```bash
# Install Hugo
brew install hugo

# Clone repo
cd /Users/zachbeaudoin/Langworthywatch
git clone https://github.com/LangworthyWatch/ny23-accountability.git langworthy-tracker

# Install theme (if needed)
cd langworthy-tracker
git submodule update --init --recursive
```

### Scraper Setup (First Time)
```bash
cd /Users/zachbeaudoin/Langworthywatch/scraper

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Install ChromeDriver for screenshots
brew install --cask chromedriver
```

---

## 🐛 Troubleshooting

### Hugo Issues

**"command not found: hugo"**
```bash
brew install hugo
```

**Theme not loading**
```bash
git submodule update --init --recursive
```

**Changes not showing**
```bash
hugo --gc
hugo server -D
```

### Scraper Issues

**No statements found**
- Website structure changed
- Check URLs in scrapers
- Inspect HTML selectors

**Archive.org failing**
- Rate limiting (wait a few minutes)
- Check https://status.archive.org

**Screenshots not working**
```bash
brew install --cask chromedriver
```

### Git Issues

**Wrong remote**
```bash
git remote -v
git remote set-url origin https://github.com/LangworthyWatch/ny23-accountability.git
```

---

## 📊 Data Organization

### Scraper Storage Structure
```
scraper/storage/
├── raw_statements/          # Freshly collected (pending review)
│   ├── 2024-12-21_press_release_123.json
│   └── 2024-12-20_vote_456.json
├── verified/                # Reviewed and approved
│   └── 2024-12-15_healthcare_statement.json
└── archives/
    └── screenshots/         # Screenshot evidence
```

### Hugo Content Structure
```
content/
├── _index.md                # Homepage
├── fact-checks/             # Statement vs. action entries
│   └── 2024-12-21-topic.md
├── votes/                   # Voting record docs
│   └── 2024-12-20-bill.md
└── methodology/             # Verification standards
    └── _index.md
```

---

## 🎯 Verification Checklist

Before publishing:
- [ ] Source URL verified and accessible
- [ ] Archived to Archive.org
- [ ] Full context preserved (not cherry-picked)
- [ ] Relevant for accountability
- [ ] Can be cross-referenced with votes/actions
- [ ] All sources linked
- [ ] Exact quotes (not paraphrased)
- [ ] No speculation or opinion

---

## 📈 Common Patterns

### Finding Contradictions
1. Statement says: "I always support X"
2. Vote record shows: Voted against X funding
3. Create entry with both sources
4. Let readers judge

### Archive Everything
```bash
# Before creating entry:
1. Archive press release
2. Archive vote page
3. Take screenshots
4. Save locally
5. Note archive URLs in entry
```

### Quality Over Quantity
- 1 bulletproof fact-check > 10 rushed entries
- Every entry must be indisputable
- Zero tolerance for errors
- Full context always

---

## ⚡ Performance Tips

### Parallel Scraping
```bash
# Use run_scraper.py for 50% faster collection
python run_scraper.py

# vs. running individually (slower):
python scrapers/congressional_site.py
python scrapers/congress_gov.py
```

### Hugo Build Speed
```bash
# Faster builds
hugo --gc --minify

# Development (no minify)
hugo server -D --disableFastRender=false
```

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| **claude_docs.md** | Complete technical documentation |
| **README.md** | Project overview |
| **QUICK_REFERENCE.md** | This file - command cheatsheet |
| **CHANGELOG.md** | Version history |
| **scraper/README.md** | Scraper system documentation |

---

*Quick Reference v1.0 - January 6, 2026*
