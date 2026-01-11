# Langworthy Accountability Tracker - Scraper System

Automated collection and verification system for tracking Rep. Langworthy's statements and votes.

## Setup

### Install Dependencies

```bash
cd /Users/zachbeaudoin/Langworthywatch/scraper

# Install Python packages
pip install -r requirements.txt

# Optional: For screenshots (requires ChromeDriver)
brew install chromedriver
```

## Usage

### 1. Scrape Press Releases

Collect statements from Langworthy's official congressional website:

```bash
python scrapers/congressional_site.py
```

This will:
- Fetch recent press releases
- Extract full text
- Save to `storage/raw_statements/`

### 2. Scrape Voting Records

Collect votes from Congress.gov:

```bash
python scrapers/congress_gov.py
```

This will:
- Fetch recent votes
- Get bill summaries
- Save to `storage/raw_statements/`

### 3. Review Collected Statements

Interactive review to verify what you've collected:

```bash
python review_queue.py
```

This lets you:
- Review each statement
- Mark for publishing or discard
- Keep in queue for later

Actions:
- **[p]** - Publish (move to verified folder)
- **[d]** - Discard (not useful)
- **[l]** - Later (keep in queue)
- **[v]** - View again
- **[q]** - Quit

### 4. Archive Evidence

Archive URLs to Wayback Machine:

```python
from utils.archiver import Archiver

archiver = Archiver()

# Archive a URL
archive_url = archiver.archive_url("https://langworthy.house.gov/...")

# Archive with screenshot
result = archiver.archive_with_screenshot(url, take_screenshot=True)
```

## Workflow

### Daily Collection (Manual)

1. **Morning**: Run scrapers
   ```bash
   python scrapers/congressional_site.py
   python scrapers/congress_gov.py
   ```

2. **Afternoon**: Review queue
   ```bash
   python review_queue.py
   ```

3. **Research**: Cross-reference statements with votes
   - Look for contradictions
   - Verify context
   - Collect supporting sources

4. **Create Entry**: Write Hugo markdown file
   ```bash
   cd ../langworthy-tracker
   hugo new content/fact-checks/2024-12-21-topic.md
   ```

5. **Publish**: Push to GitHub
   ```bash
   git add content/fact-checks/2024-12-21-topic.md
   git commit -m "Add fact-check: topic"
   git push
   ```

## Directory Structure

```
scraper/
├── scrapers/
│   ├── congressional_site.py    # Press releases scraper
│   └── congress_gov.py           # Voting record scraper
├── utils/
│   └── archiver.py               # Archive.org integration
├── storage/
│   ├── raw_statements/           # Collected statements (pending review)
│   ├── verified/                 # Verified, ready to publish
│   └── archives/
│       └── screenshots/          # Screenshot evidence
├── review_queue.py               # Interactive verification tool
└── requirements.txt              # Python dependencies
```

## Features

### Congressional Site Scraper
- ✅ Scrapes press releases automatically
- ✅ Extracts full text from article pages
- ✅ Saves with metadata and timestamps
- ✅ Avoids duplicates

### Congress.gov Scraper
- ✅ Fetches voting records
- ✅ Gets bill summaries
- ✅ Links to official sources
- ✅ Tracks member-specific votes

### Archiver
- ✅ Saves URLs to Archive.org (Wayback Machine)
- ✅ Checks if already archived
- ✅ Optional screenshot capability
- ✅ Permanent evidence preservation

### Review Queue
- ✅ Interactive CLI interface
- ✅ Shows full context for verification
- ✅ Verification checklist
- ✅ Organize: publish, discard, or defer

## Verification Standards

Before marking a statement for publishing:

1. **Source Verified** - Original URL accessible and accurate
2. **Archived** - Saved to Archive.org
3. **Context Confirmed** - Full context preserved, not cherry-picked
4. **Relevant** - Actually useful for accountability tracking
5. **Cross-referenceable** - Can be compared with votes/actions

## Tips

### Finding Contradictions

1. Scrape recent statements about a topic (e.g., "healthcare")
2. Scrape voting records on related bills
3. Look for mismatches:
   - Says "I support X" but voted against X funding
   - Claims "always" supported Y but voted against Y multiple times
   - States position that contradicts actual votes

### Keyword Flagging (Future Enhancement)

You can add keyword detection to auto-flag interesting statements:

```python
keywords = ["rural hospital", "veteran", "healthcare", "social security"]

for keyword in keywords:
    if keyword.lower() in statement['full_text'].lower():
        statement['flags'].append(keyword)
```

## Automation (Future)

Currently manual. Future enhancements:

- Schedule scrapers to run daily (cron job or GitHub Actions)
- Auto-flag potential contradictions
- Email notifications for interesting content
- Automated cross-referencing

## Security & Anonymity

**IMPORTANT**: Keep this scraper separate from your public GitHub

- ✅ Run on your personal machine
- ✅ It only collects public information
- ✅ Don't commit scraper to public repo (keep private)
- ✅ Only push verified Hugo content to public site

## Troubleshooting

### No statements found

- Congressional website structure may have changed
- Check if URLs are correct
- Inspect actual HTML and update selectors in scrapers

### Archive.org not working

- Rate limiting (wait a few minutes)
- Network issues
- Archive.org may be down (check status.archive.org)

### Screenshots failing

- Need Selenium + ChromeDriver installed
- Check ChromeDriver version matches Chrome version
- Run: `brew install --cask chromedriver`

## Legal & Ethical Notes

✅ **This is legal**:
- Scraping public government websites
- Collecting publicly available congressional records
- Archiving public statements for research

✅ **Best practices**:
- Respect robots.txt
- Don't hammer servers (reasonable delays)
- Only collect public information
- Document everything with sources

---

## Next Steps

1. Run your first scrape
2. Review the collected statements
3. Find your first contradiction
4. Create your first fact-check entry
5. Publish to langworthywatch.org!

**Remember**: Quality over quantity. One bulletproof fact-check is better than ten rushed entries.
