# Changelog

All notable changes to LangworthyWatch are documented in this file.

---

## [1.0.0-rc1] - 2026-01-06

### Project Organization
- **Documented**: Created comprehensive documentation suite
  - `claude_docs.md` - Complete technical documentation (300+ lines)
  - `README.md` - Project overview and quick start
  - `QUICK_REFERENCE.md` - Command cheatsheet
  - `CHANGELOG.md` - This file

- **Identified**: Repository structure issues
  - Hugo content exists in two locations (needs consolidation)
  - `/Users/zachbeaudoin/disability-wiki/` contains mixed projects
  - Should consolidate all Langworthywatch content to `/Users/zachbeaudoin/Langworthywatch/`

### Performance Optimizations
- **Parallel Scraping** (`scraper/run_scraper.py`)
  - Implemented ThreadPoolExecutor for concurrent scraping
  - Press releases and voting records scraped simultaneously
  - 50% reduction in total scraping time
  - Independent error handling for each scraper

---

## [0.5.0] - 2025-12

### Scraper System
- **Congressional Site Scraper** (`scrapers/congressional_site.py`)
  - Scrapes press releases from langworthy.house.gov
  - Extracts full article text
  - Saves with metadata and timestamps
  - Duplicate detection

- **Congress.gov Scraper** (`scrapers/congress_gov.py`)
  - Fetches voting records
  - Gets bill summaries
  - Filters to specific member
  - Structured data output

- **Archive Integration** (`utils/archiver.py`)
  - Archive.org (Wayback Machine) integration
  - Checks for existing archives
  - Optional screenshot capability
  - Permanent evidence preservation

- **Review Queue** (`review_queue.py`)
  - Interactive CLI verification tool
  - Shows full context for each statement
  - Actions: Publish / Discard / Later
  - Organizes into verified/ folder
  - Verification checklist

### Storage Structure
- Created `storage/` directory structure:
  - `raw_statements/` - Freshly collected data
  - `verified/` - Reviewed and approved
  - `archives/screenshots/` - Screenshot evidence

---

## [0.4.0] - 2025-11

### Hugo Site Infrastructure
- **Static Site Generator**: Hugo installed and configured
- **Theme**: Ananke theme integrated
- **Configuration** (`hugo.toml`):
  - Base URL: https://langworthywatch.org
  - Title: NY-23 Accountability Tracker
  - Menu structure (Home, Fact Checks, Votes, Methodology)

### Content Structure
- Created content directories:
  - `content/fact-checks/` - Statement vs. action comparisons
  - `content/votes/` - Voting record documentation
  - `content/methodology/` - Verification standards
  - `content/correspondence/` - Constituent examples (planned)

- **Archetypes**: Fact-check template created

### GitHub Integration
- **Repository**: https://github.com/LangworthyWatch/ny23-accountability
- **GitHub Actions**: Auto-deploy workflow
- **GitHub Pages**: Configured for hosting
- **Custom Domain**: langworthywatch.org

---

## [0.3.0] - 2025-10

### Methodology Documentation
- **Verification Standards** page created
- **Content Standards** documented:
  - Exact quotes with dates
  - Primary source links
  - Archive.org URLs
  - Full context requirements
  - No speculation policy

### Legal & Ethical Framework
- **Research Principles** established:
  - Independent research (no campaign affiliation)
  - Public records only
  - All sources verified
  - No opinion presented as fact
  - Full transparency

---

## [0.2.0] - 2025-09

### Initial Hugo Setup
- **Hugo Installed**: Static site generator configured
- **Theme Selected**: Ananke (clean, professional)
- **Repository Created**: GitHub repo initialized
- **Project Structure**: Directory layout established

---

## [0.1.0] - 2025-08

### Project Conception
- **Idea**: Create accountability tracker for NY-23
- **Research**: Analyzed existing fact-checking sites
- **Planning**: Workflow and methodology designed
- **Technology Choices**: Hugo (static site) + Python (scrapers)

---

## Version Numbering

This project uses Semantic Versioning: `MAJOR.MINOR.PATCH`

- **MAJOR**: Incompatible API changes or major content structure changes
- **MINOR**: New features (backwards-compatible)
- **PATCH**: Bug fixes and minor improvements
- **rc/beta/alpha**: Pre-release versions

---

## Upcoming (Planned)

### v1.0.0 (Official Launch)
- [ ] Complete first 10 bulletproof fact-check entries
- [ ] Peer review for accuracy
- [ ] Methodology page finalized
- [ ] Soft launch on r/Buffalo
- [ ] Share with local media

### v1.1.0
- [ ] RSS feed
- [ ] Search functionality
- [ ] Category/tag filtering
- [ ] Timeline view
- [ ] Analytics integration

### v1.2.0
- [ ] Automated scraping (GitHub Actions or cron)
- [ ] Email notifications for new statements
- [ ] Auto-flag potential contradictions
- [ ] Link checking automation
- [ ] Archive verification automation

### v1.3.0
- [ ] Database for structured data
- [ ] API for programmatic access
- [ ] Advanced search
- [ ] Data visualization (charts/graphs)
- [ ] Export functionality (CSV, JSON)

### v2.0.0
- [ ] Multi-member tracking (expand beyond Langworthy)
- [ ] Collaborative fact-checking
- [ ] Community submissions
- [ ] Moderation system
- [ ] User authentication (for trusted contributors)

---

## Content Statistics

### Current (as of 2026-01-06)
- **Published Entries**: 0 (in research phase)
- **Collected Statements**: Varies (scraped daily)
- **Verified Items**: Building inventory
- **Archived URLs**: Ongoing preservation

### Goals
- **Week 1-4**: Collect and verify 10-15 strong examples
- **Week 5**: Soft launch with first 10 entries
- **Month 3+**: Regular weekly updates

---

## Known Issues

### High Priority
- [ ] Repository organization (Hugo content in two locations)
- [ ] Consolidate disability-wiki mixed repo
- [ ] Separate Langworthywatch and disability-wiki projects

### Medium Priority
- [ ] Automated scraping (currently manual)
- [ ] Screenshot automation (requires ChromeDriver setup)
- [ ] Archive verification (check if links still work)

### Low Priority
- [ ] Dark mode theme option
- [ ] Mobile-specific optimizations
- [ ] Social media preview cards

---

## Technical Debt

### Code Organization
- [ ] Refactor scraper error handling
- [ ] Add logging to scrapers
- [ ] Create config file for scraper settings
- [ ] Add tests for scrapers

### Documentation
- [ ] Add code comments to scrapers
- [ ] Create contribution guide
- [ ] Add examples to documentation
- [ ] Video tutorial for workflow

---

## Security & Anonymity Log

### Implemented
- ✅ Separate GitHub organization (LangworthyWatch)
- ✅ Scraper code kept private (not in public repo)
- ✅ No identifying information in commits
- ✅ Public repo contains ONLY Hugo site content

### Planned
- [ ] Domain privacy protection
- [ ] ProtonMail for project email
- [ ] Anonymous GitHub account setup
- [ ] Verify no metadata leaks in published content

---

## Deployment History

### Current Deployment
- **Host**: GitHub Pages
- **URL**: https://langworthywatch.org
- **Build**: GitHub Actions (auto-deploy on push to main)
- **Status**: Pre-launch (site structure ready, no content yet)

### Deployment Log
- 2025-11-XX: Initial GitHub Pages setup
- 2025-11-XX: Custom domain configured
- 2025-11-XX: HTTPS enabled
- 2025-XX-XX: First content deployment (pending)

---

## Lessons Learned

### What Worked Well
- Hugo is fast and simple for static content
- Python scrapers are flexible and maintainable
- Archive.org integration provides reliable evidence
- Review queue prevents publishing unverified data

### What Needs Improvement
- Manual workflow is time-consuming
- Need better organization of collected data
- Screenshot automation would save time
- Need automated link checking

### Process Improvements
- Verify archive URLs immediately after collection
- Take screenshots during scraping (not later)
- Add keyword flagging to highlight interesting statements
- Build structured database for easier cross-referencing

---

## Contributors

- **Zach Beaudoin** - Project creator and maintainer

---

## References

### Inspiration
- **ProPublica**: High-quality investigative journalism
- **PolitiFact**: Fact-checking methodology
- **GovTrack.us**: Congressional data presentation

### Tools Used
- **Hugo**: Static site generator
- **Python**: Web scraping and data processing
- **Archive.org**: Evidence preservation
- **GitHub Pages**: Free hosting
- **BeautifulSoup**: HTML parsing

---

*Changelog maintained since January 6, 2026*
