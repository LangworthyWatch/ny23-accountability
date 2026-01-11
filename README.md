# LangworthyWatch - NY-23 Accountability Tracker

Independent research documenting NY-23 Congressional representation through public records.

**Live Site**: https://langworthywatch.org
**Repository**: https://github.com/LangworthyWatch/ny23-accountability

---

## About

LangworthyWatch documents statements and actions by New York's 23rd Congressional District representative using publicly available government records. We present facts side-by-side to enable constituent accountability.

### Core Principles
- **Independent Research** - No campaign affiliation
- **Public Records Only** - All sources are government websites
- **All Sources Verified** - Primary sources linked and archived
- **No Opinion** - Present facts, let constituents judge
- **Full Context** - Never cherry-pick quotes

---

## Project Structure

```
Langworthywatch/
├── 📁 langworthy-tracker/        # Hugo static site (PUBLIC)
│   ├── content/fact-checks/      # Statement vs. action entries
│   ├── content/votes/            # Voting record documentation
│   ├── content/methodology/      # Verification standards
│   ├── themes/ananke/            # Hugo theme
│   └── hugo.toml                 # Configuration
│
└── 📁 scraper/                   # Data collection tools (PRIVATE)
    ├── scrapers/                 # Python web scrapers
    │   ├── congressional_site.py # Press release scraper
    │   └── congress_gov.py       # Voting record scraper
    ├── utils/archiver.py         # Archive.org integration
    ├── review_queue.py           # Verification tool
    ├── run_scraper.py            # Parallel scraper (optimized)
    └── storage/                  # Collected data
```

---

## Quick Start

### Hugo Site (Public)

```bash
cd /Users/zachbeaudoin/Langworthywatch/langworthy-tracker

# Install Hugo (if needed)
brew install hugo

# Run development server
hugo server -D

# Access at http://localhost:1313

# Build for production
hugo
```

### Scraper System (Private)

```bash
cd /Users/zachbeaudoin/Langworthywatch/scraper

# Setup virtual environment (first time)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run scrapers
python run_scraper.py

# Review collected data
python review_queue.py
```

---

## Workflow

### 1. Collect Data
```bash
cd scraper
source venv/bin/activate
python run_scraper.py
```

Scrapes:
- Press releases from langworthy.house.gov
- Voting records from congress.gov

### 2. Review & Verify
```bash
python review_queue.py
```

Interactive review:
- [p] Publish - Move to verified folder
- [d] Discard - Not useful
- [l] Later - Keep for future research

### 3. Create Entry
```bash
cd ../langworthy-tracker
hugo new content/fact-checks/2024-12-21-topic.md
```

Fill in template:
- Statement (exact quote + source)
- Voting record (vote + source)
- Full context
- All sources archived

### 4. Publish
```bash
# Preview locally
hugo server -D

# Commit and push
git add content/fact-checks/2024-12-21-topic.md
git commit -m "Add fact-check: topic description"
git push origin main
```

GitHub Actions automatically deploys to langworthywatch.org.

---

## Content Standards

Every entry must include:

1. **Exact Quote**
   - Verbatim text
   - Publication date
   - Primary source link
   - Archive.org URL

2. **Voting Record/Action**
   - Bill number and title
   - Vote date and result
   - Congress.gov link
   - Archive.org URL

3. **Full Context**
   - Complete statements
   - Bill summary
   - Related context

4. **No Speculation**
   - Only documented facts
   - No assumptions
   - Let readers judge

---

## Features

### Hugo Static Site
- ✅ Fast, secure static site
- ✅ GitHub Pages hosting
- ✅ Automatic deployment
- ✅ Clean, professional design
- ✅ Responsive layout

### Scraper System
- ✅ Automated data collection
- ✅ Parallel execution (50% faster)
- ✅ Duplicate avoidance
- ✅ Archive.org integration
- ✅ Interactive review queue

---

## Documentation

📖 **[Read claude_docs.md for complete technical documentation](./claude_docs.md)**

Includes:
- Full project architecture
- Scraper documentation
- Hugo configuration
- Workflow details
- Deployment procedures
- Troubleshooting guide

📋 **[Read QUICK_REFERENCE.md for command cheatsheet](./QUICK_REFERENCE.md)**

---

## Security & Anonymity

### Maintaining Anonymity
- ✅ Separate GitHub account
- ✅ ProtonMail email
- ✅ Domain privacy protection
- ✅ No identifying information

### Legal & Ethical
- ✅ Scraping public government websites is legal
- ✅ Archiving public statements is legal
- ✅ Publishing factual information is protected speech
- ✅ Respect robots.txt
- ✅ Reasonable scraping delays

---

## Technology Stack

- **Static Site**: Hugo
- **Theme**: Ananke
- **Hosting**: GitHub Pages
- **Deployment**: GitHub Actions
- **Scrapers**: Python (Requests, BeautifulSoup)
- **Archiving**: Archive.org (Wayback Machine)

---

## Project Status

**Status**: Active, in research phase
**Published Entries**: 0 (building foundation first)
**Data Collection**: Ongoing

**Next Steps**:
1. Complete first 10 bulletproof fact-checks
2. Get peer review for accuracy
3. Soft launch on r/Buffalo
4. Build consistent update schedule

---

## Contributing

This is an independent research project. If you find errors:

1. Check the methodology page
2. Verify the primary sources
3. Open an issue on GitHub with corrections

We welcome:
- Corrections to factual errors
- Additional context
- Better sources
- Methodology improvements

---

## License

Content is for educational and research purposes. All government records cited are public domain.

---

## Resources

- **Congress.gov**: https://www.congress.gov
- **Langworthy's Site**: https://langworthy.house.gov
- **Archive.org**: https://web.archive.org
- **Hugo Docs**: https://gohugo.io/documentation/

---

## Contact

**GitHub**: https://github.com/LangworthyWatch
**Repository**: https://github.com/LangworthyWatch/ny23-accountability
**Site**: https://langworthywatch.org

---

*Independent Research | Public Records Only | All Sources Verified*

*Last Updated: January 6, 2026*
