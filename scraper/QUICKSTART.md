# Quick Start Guide

Get scraping in 5 minutes!

## 1. Setup (One Time)

```bash
cd /Users/zachbeaudoin/Langworthywatch/scraper

# Activate virtual environment
source venv/bin/activate

# You're ready!
```

## 2. Run Your First Scrape

```bash
# Collect statements and votes
python3 run_scraper.py
```

This will:
- Scrape recent press releases from langworthy.house.gov
- Collect recent votes from congress.gov
- Save everything to `storage/raw_statements/`

## 3. Review What You Collected

```bash
# Interactive review tool
python3 review_queue.py
```

This lets you:
- See each statement
- Mark for publishing or discard
- Keep in queue for later

## 4. Find Contradictions

Look for patterns like:
- **Statement**: "I support rural hospitals"
- **Vote**: NO on Rural Hospital Funding Act

## 5. Create Fact-Check Entry

```bash
cd ../langworthy-tracker

# Create new entry
hugo new content/fact-checks/2024-12-21-healthcare-contradiction.md

# Edit the file with your findings
```

## 6. Publish

```bash
# In langworthy-tracker directory
git add content/fact-checks/2024-12-21-healthcare-contradiction.md
git commit -m "Add fact-check: healthcare funding contradiction"
git push
```

Your site updates automatically at **https://langworthywatch.org** 🎉

## Daily Workflow

**Every morning** (5-10 minutes):
```bash
cd /Users/zachbeaudoin/Langworthywatch/scraper
source venv/bin/activate
python3 run_scraper.py
```

**When you have time** (30-60 minutes):
```bash
python3 review_queue.py
# Research contradictions
# Create fact-check entries
# Publish to site
```

## Tips

### Activate Virtual Environment

Always run:
```bash
source venv/bin/activate
```

You'll see `(venv)` in your prompt when active.

### Deactivate When Done

```bash
deactivate
```

### See What's Collected

```bash
ls storage/raw_statements/
```

### Clear Old Data

```bash
# Remove all pending items
rm storage/raw_statements/*.json

# Start fresh
```

## Troubleshooting

**"ModuleNotFoundError: No module named 'requests'"**
→ Activate virtual environment: `source venv/bin/activate`

**"No statements found"**
→ Website structure may have changed. Check scrapers.

**"Permission denied"**
→ Run: `chmod +x run_scraper.py`

## Next Steps

1. Run your first scrape: `python3 run_scraper.py`
2. Review collected items: `python3 review_queue.py`
3. Find a contradiction
4. Create your first fact-check entry
5. Publish!

---

**Remember**: Quality over quantity. One solid, verified contradiction is worth more than dozens of weak claims.
