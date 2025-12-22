# Scripts Directory

This directory contains Python scripts for maintaining and enriching the LangworthyWatch accountability database.

## Setup

### 1. Install Dependencies

```bash
cd scripts
pip install -r requirements.txt
```

### 2. Get API Keys (Optional but Recommended)

**Congress.gov API:**
- Sign up: https://api.congress.gov/sign-up/
- Set environment variable: `export CONGRESS_GOV_API_KEY=your_key`

**ProPublica Congress API:**
- Get key: https://www.propublica.org/datastore/api/propublica-congress-api
- Set environment variable: `export PROPUBLICA_API_KEY=your_key`

## Scripts Overview

### Data Collection

#### `fetch_legislator_data.py`
Fetches Langworthy's biographical data and committee assignments from the `unitedstates/congress-legislators` repository.

**Usage:**
```bash
python3 fetch_legislator_data.py
```

**Outputs:**
- `data/langworthy_profile.json` - Full biographical and term data
- `data/langworthy_committees.json` - Current committee assignments

**No API key required** - uses public GitHub data.

**Run this:** Weekly or when committee assignments change

---

#### `find_procedural_inaction.py`
Identifies bills stuck in Langworthy's committees with no action.

**Usage:**
```bash
export CONGRESS_GOV_API_KEY=your_key
python3 find_procedural_inaction.py
```

**Requires:**
- `data/langworthy_committees.json` (run `fetch_legislator_data.py` first)
- Congress.gov API key

**Outputs:**
- `data/procedural_inaction_candidates.json` - Bills stuck >90 days with no committee action

**Run this:** Monthly or when researching new fact-checks

---

### Data Enrichment

#### `enrich_votes.py` (TO BE CREATED)
Adds bill numbers, titles, and topics to the raw vote data.

**Planned features:**
- Match roll call numbers to bill numbers
- Add policy topic tags (Healthcare, Veterans, etc.)
- Cross-reference with committee assignments
- Identify votes on bills from Langworthy's committees

**Will require:** ProPublica API key

---

### Analysis Tools

#### `match_statements_to_votes.py` (TO BE CREATED)
Semi-automated tool to find contradictions between statements and actions.

**Planned features:**
- Text search through press releases
- Match topics to votes
- Flag potential contradictions for manual review

---

## Workflow Examples

### Adding a New Procedural Inaction Fact-Check

1. **Fetch latest committee data:**
   ```bash
   python3 fetch_legislator_data.py
   ```

2. **Find stuck bills:**
   ```bash
   python3 find_procedural_inaction.py
   ```

3. **Review candidates:**
   ```bash
   cat data/procedural_inaction_candidates.json | jq '.stuck_bills[] | select(.topics[] | contains("Healthcare"))'
   ```

4. **Search for statements:**
   - Check Langworthy's press releases: https://langworthy.house.gov/media/press-releases
   - Search Congressional Record
   - Review local news coverage

5. **Document the gap:**
   - Copy `content/fact-checks/_template-procedural-inaction.md`
   - Fill in bill details, public statements, and timeline
   - Cite all sources

6. **Build and preview:**
   ```bash
   hugo server
   ```

---

### Enriching Vote Data

1. **Get current votes:**
   ```bash
   # Your existing scraper should have created data/votes.json
   ```

2. **Enrich with topics and bills:**
   ```bash
   python3 enrich_votes.py
   # Creates data/votes_enriched.json
   ```

3. **Copy enriched data:**
   ```bash
   cp data/votes_enriched.json data/votes.json
   ```

4. **Rebuild site:**
   ```bash
   hugo
   ```

---

## Data Sources

### Primary Sources (Free, Public Domain)

1. **unitedstates/congress-legislators**
   - URL: https://github.com/unitedstates/congress-legislators
   - License: CC0 (Public Domain)
   - Contains: Committee assignments, biographical data, social media
   - Update frequency: Weekly or when changes occur

2. **Congress.gov API**
   - URL: https://api.congress.gov/
   - License: Public domain (government data)
   - Contains: Bill text, status, committee referrals, votes
   - Rate limit: Generous (5000 requests/hour)

3. **ProPublica Congress API**
   - URL: https://projects.propublica.org/api-docs/congress-api/
   - License: You may republish the data
   - Contains: Bills, votes, members, statements
   - Rate limit: 5000 requests/day

4. **VoteView / ICPSR**
   - URL: https://voteview.com/data
   - License: Free for research
   - Contains: Historical votes with policy area codes
   - Format: CSV downloads

### Secondary Sources

- House.gov press releases
- Senate.gov committee pages
- GovTrack.us (for cross-referencing)
- Congressional Record (official floor statements)

---

## File Formats

### Input Data

**`data/votes.json`** (from your scraper):
```json
[
  {
    "roll_call": "362",
    "date": "2025-12-18",
    "description": "On passage...",
    "vote": "Yea",
    "url": "https://www.congress.gov/votes/...",
    "bill": "",
    "title": ""
  }
]
```

**`data/langworthy_committees.json`** (from `fetch_legislator_data.py`):
```json
{
  "member": {
    "bioguide": "L000600",
    "name": "Nicholas A. Langworthy"
  },
  "committees": [
    {
      "committee_id": "HSAG",
      "name": "House Committee on Agriculture",
      "type": "house",
      "party": "majority",
      "rank": 15
    }
  ]
}
```

### Output Data

**`data/procedural_inaction_candidates.json`**:
```json
{
  "generated_at": "2025-12-22T10:30:00Z",
  "congress": 119,
  "stuck_bills": [
    {
      "bill_number": "H.R. 2880",
      "title": "PBM Reform Act",
      "topics": ["Healthcare"],
      "days_stuck": 291,
      "committee": "House Oversight and Accountability",
      "latest_action": "Referred to committee"
    }
  ],
  "by_topic": {
    "Healthcare": 15,
    "Veterans": 8
  }
}
```

---

## Best Practices

### API Usage
- Cache API responses to avoid hitting rate limits
- Use conditional requests (ETags) when possible
- Respect rate limits - add delays between bulk requests

### Data Updates
- Committee assignments: Check monthly
- Vote data: Update weekly during session
- Bill status: Update when researching specific cases

### Version Control
- Commit enriched data files
- Don't commit API keys
- Use `.gitignore` for cache files

### Documentation
- Cite sources in fact-check entries
- Archive URLs (use Archive.org)
- Screenshot social media posts
- Keep raw data alongside processed data

---

## Troubleshooting

**"No module named 'yaml'"**
```bash
pip install pyyaml
```

**"No CONGRESS_GOV_API_KEY set"**
```bash
export CONGRESS_GOV_API_KEY=your_key
# Or add to ~/.bashrc or ~/.zshrc
```

**"Permission denied"**
```bash
chmod +x scripts/*.py
```

**"Rate limit exceeded"**
- Wait before making more requests
- Add delays: `time.sleep(1)` between requests
- Cache responses locally

---

## Contributing

When adding new scripts:

1. Add docstring at top explaining purpose
2. Include usage example
3. Handle errors gracefully
4. Output progress messages
5. Save intermediate results
6. Update this README

---

## License Note

All data from congress-legislators, Congress.gov, and ProPublica is in the public domain or explicitly republishable. Always cite sources in your published fact-checks.

See: [DATA_ENRICHMENT_GUIDE.md](../DATA_ENRICHMENT_GUIDE.md) for detailed methodology.
