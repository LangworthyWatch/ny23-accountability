# LangworthyWatch

## Overview
Independent accountability project documenting statements and actions by Rep. Nick Langworthy (NY-23) using public records. The repository contains two subsystems: a Hugo static site (published at langworthywatch.org) tracked in a separate repo under `langworthy-tracker/`, and a Python scraper/analysis toolkit for collecting press releases, voting records, and archiving sources. The project also houses fact-check drafts and constituent letter archives in the root.

## Tech Stack
- **Static site**: Hugo (custom layouts, no external theme) -- lives in `langworthy-tracker/` (separate git repo)
- **Scrapers**: Python 3 with Requests, BeautifulSoup, lxml, Selenium, PyYAML
- **Archiving**: Archive.org Wayback Machine integration
- **Hosting**: GitHub Pages (langworthywatch.org)
- **Deployment**: GitHub Actions (auto-deploy on push to `langworthy-tracker` repo)
- **Analytics**: Google Analytics (in tracker site)
- **Donations**: Donorbox (in tracker site)

## Project Structure
```
Langworthywatch/
├── langworthy-tracker/              # Hugo site (SEPARATE GIT REPO, .gitignored here)
│   ├── content/fact-checks/         # Published fact-check entries
│   ├── content/votes/               # Voting record documentation
│   ├── content/correspondence/      # Constituent correspondence
│   ├── content/methodology/         # Verification standards
│   ├── layouts/                     # Custom Hugo templates
│   ├── static/                      # CSS, images, documents
│   ├── hugo.toml                    # Site config
│   └── CLAUDE.md                    # Detailed guide for the tracker site
├── scraper/                         # Python data collection tools
│   ├── scrapers/                    # Web scrapers (congress.gov, langworthy.house.gov)
│   ├── utils/archiver.py            # Archive.org integration
│   ├── run_scraper.py               # Parallel scraper runner
│   ├── review_queue.py              # Interactive verification tool
│   ├── monitor_agent.py             # Automated monitoring agent
│   ├── analyze_votes.py             # Vote analysis tools
│   ├── search_votes.py              # Vote search utility
│   ├── storage/                     # Collected raw data
│   └── requirements.txt            # Python dependencies
├── Fact Checks/                     # Draft fact-checks (Markdown files, not yet published)
├── Constituent Letters/             # PDF scans of constituent correspondence
├── storage/                         # Additional data storage
├── archive_helper.py                # URL archiving helper
├── batch_archive_urls.py            # Bulk URL archiving
├── extract_pending_archives.py      # Find URLs needing archiving
├── fact_check_validator_agent.py    # Automated fact-check validation
├── quick_archive.sh                 # Quick archive shell script
└── requirements.txt                 # Root-level dependencies (requests)
```

## Getting Started

### Hugo Site (in langworthy-tracker/)
```bash
cd langworthy-tracker
hugo server -D          # Dev server at localhost:1313
hugo                    # Production build
```

### Scraper System
```bash
cd scraper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run_scraper.py   # Run all scrapers
python review_queue.py  # Interactive review of collected data
```

## Key Commands
```bash
# Hugo site
cd langworthy-tracker && hugo server -D       # Dev server with drafts
cd langworthy-tracker && hugo                  # Production build

# Scrapers
cd scraper && python run_scraper.py           # Scrape press releases + votes
cd scraper && python review_queue.py          # Review queue ([p]ublish/[d]iscard/[l]ater)
cd scraper && python analyze_votes.py         # Analyze voting patterns
cd scraper && python monitor_agent.py         # Automated monitoring

# Archiving
python archive_helper.py                      # Archive individual URLs
python batch_archive_urls.py                  # Bulk archive
python extract_pending_archives.py            # Find unarchived URLs

# Fact-check validation
python fact_check_validator_agent.py          # Validate fact-check accuracy
```

## Coding Conventions
- **Fact-check files**: Named `factcheck_topic_description.md` in `Fact Checks/`
- **Published entries**: Named `YYYY-MM-DD-descriptive-slug.md` in `langworthy-tracker/content/fact-checks/`
- **Python scripts**: snake_case filenames, standard library preferred where possible
- **All sources must be archived** via Archive.org before publishing
- **No speculation or opinion** -- present documented facts only
- **Verdict labels**: TRUE, MOSTLY TRUE, MISLEADING, MOSTLY FALSE, FALSE, CONTRADICTION, DEFLECTION, MISSING CONTEXT, DOCUMENTED PATTERN, etc.

## Git & Save Practices
- **Commit message format**: Conventional Commits -- `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`
- **Commit subject**: Imperative mood, concise (<72 chars)
- **Commit body**: Explain *why*, not *what*
- **When to commit**: After each logical unit of work
- **What NOT to commit**: `.env`, `venv/`, `__pycache__/`, `.DS_Store`, `*.csv`, `*.log`, `storage/archives/screenshots/`, validation reports, `Constituent Letters/`
- **Branch strategy**: Work on `main`
- **Two repos**: This root repo and `langworthy-tracker/` are separate git repositories; commit to each independently
- **SSH note**: Port 22 to GitHub is frequently blocked; use the port 443 SSH fallback (`github-langworthy-443` host in `~/.ssh/config`)

## Testing
No formal test suite. Validation approach:
- Run `python fact_check_validator_agent.py` to validate fact-check accuracy
- Run `hugo server -D` in `langworthy-tracker/` to preview content
- Verify all source URLs are accessible and archived
- Cross-check claims against congress.gov and official sources

## Data & Security
- **Anonymity is critical**: Separate GitHub account, ProtonMail email, domain privacy protection
- **Never commit**: Personal identifying information, unredacted constituent letters, `.env` files, API keys
- **Redaction required**: Remove names, addresses, phone numbers, emails from constituent correspondence before any use
- **Legal basis**: Scraping public government websites is legal; archiving public statements is protected speech
- **Scraper etiquette**: Respect `robots.txt`, use reasonable delays between requests

## Known Issues / Limitations
- `langworthy-tracker/` is .gitignored from the parent repo -- it has its own git history
- Selenium-based scrapers require a browser driver (ChromeDriver) to be installed
- Some fact-check drafts in `Fact Checks/` have restricted permissions (600)

## Related Projects
- [langworthy-tracker](/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/) -- The published Hugo site (separate repo)
- [beaudoin-campaign](/Users/zachbeaudoin/projects/beaudoin-campaign/) -- Campaign website
- [new-york-ida](/Users/zachbeaudoin/projects/new-york-ida/) -- NY IDA accountability data analysis
- [ida-accountability](/Users/zachbeaudoin/projects/ida-accountability/) -- Multi-state IDA investigation
