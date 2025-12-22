# Vote Data Enrichment & Accountability Tracking Guide

## Problem Statement

Your current `data/votes.json` contains:
- Roll call numbers
- Dates
- Vote positions (Yea/Nay)
- Procedural descriptions ("On passage...", "On motion to recommit...")

**Missing critical information:**
- Bill numbers (H.R. 1234, S. 567)
- Bill titles ("Affordable Care Act Extension")
- Policy topics (Healthcare, Immigration, Veterans)
- Committee context

## Solution: Multi-Source Data Pipeline

### Layer 1: Identity & Committee Data (Foundation)

**Source:** `unitedstates/congress-legislators` (GitHub)
- **URL:** https://github.com/unitedstates/congress-legislators
- **License:** Public domain (CC0)
- **What it gives you:**
  - Bioguide ID: `L000600` (Langworthy's permanent ID)
  - Committee assignments (current + historical)
  - Term dates
  - Leadership roles

**How to use:**
```bash
# Clone or download
git clone https://github.com/unitedstates/congress-legislators.git

# Or fetch specific files
curl -o legislators-current.yaml \
  https://raw.githubusercontent.com/unitedstates/congress-legislators/main/legislators-current.yaml
```

**Example data structure:**
```yaml
- id:
    bioguide: L000600
    govtrack: 456789
  name:
    official_full: Nicholas A. Langworthy
  terms:
  - type: rep
    start: '2023-01-03'
    state: NY
    district: 23
    party: Republican
```

**Committees file:**
```yaml
- thomas_id: HSIF  # Energy & Commerce
  members:
  - bioguide: L000600
    party: Republican
    rank: 15
```

### Layer 2: Vote Content & Topics

**Option A: ProPublica Congress API** (Recommended for journalists)

- **URL:** https://projects.propublica.org/api-docs/congress-api/
- **Cost:** Free (requires API key)
- **License:** You can republish the data
- **Rate limits:** Generous for your use case

**What it gives you:**
```json
{
  "roll_call": "362",
  "date": "2025-12-18",
  "bill": {
    "number": "H.R. 5376",
    "title": "Build Back Better Act",
    "latest_action": "Passed House"
  },
  "question": "On Passage",
  "result": "Passed",
  "subject": "Health",
  "positions": [
    {
      "member_id": "L000600",
      "name": "Langworthy",
      "vote_position": "Yes"
    }
  ]
}
```

**Setup:**
1. Get API key: https://www.propublica.org/datastore/api/propublica-congress-api
2. Store in environment variable: `export PROPUBLICA_API_KEY=your_key`

**Sample request:**
```bash
curl "https://api.propublica.org/congress/v1/119/house/sessions/1/votes.json" \
  -H "X-API-Key: YOUR_KEY_HERE"
```

**Option B: VoteView / ICPSR** (Academic standard)

- **URL:** https://voteview.com/data
- **Cost:** Free
- **What it gives you:** Policy area codes (standardized topics)

**Download:**
```bash
# Get all House votes with policy codes
curl -o voteview_119.csv \
  "https://voteview.com/static/data/out/votes/H119_votes.csv"
```

**Policy codes include:**
- Code 3: Health
- Code 19: Immigration
- Code 16: Defense
- Code 21: Government Operations

### Layer 3: Bill Details

**Source:** Congress.gov API (official)

- **URL:** https://api.congress.gov/
- **Documentation:** https://github.com/LibraryOfCongress/api.congress.gov/
- **Cost:** Free (requires API key)

**What it gives you:**
```json
{
  "bill": {
    "number": "H.R. 5376",
    "title": "Build Back Better Act",
    "summary": "This bill provides funding for...",
    "sponsors": [...],
    "committees": [
      {"name": "Energy and Commerce", "activities": ["Referred"]}
    ],
    "actions": [
      {"date": "2025-03-15", "text": "Referred to Committee"}
    ]
  }
}
```

## Data Enrichment Pipeline

### Step 1: Match Votes to Bills

Create a Python script to enrich your `votes.json`:

```python
import json
import requests
from datetime import datetime

PROPUBLICA_KEY = "your_key"

def enrich_votes(votes_file):
    """Add bill numbers and titles to vote records"""
    with open(votes_file) as f:
        votes = json.load(f)

    # Get ProPublica vote data
    url = "https://api.propublica.org/congress/v1/119/house/sessions/1/votes.json"
    headers = {"X-API-Key": PROPUBLICA_KEY}
    response = requests.get(url, headers=headers)
    pp_votes = response.json()["results"]["votes"]

    # Match by roll call number
    for vote in votes:
        roll_num = vote["roll_call"]
        matching = next((v for v in pp_votes if v["roll_call"] == roll_num), None)

        if matching:
            vote["bill"] = matching["bill"].get("number", "")
            vote["title"] = matching["bill"].get("title", "")
            vote["subject"] = matching.get("subject", "")
            vote["topic"] = categorize_subject(matching.get("subject", ""))

    return votes

def categorize_subject(subject):
    """Map ProPublica subjects to your topic categories"""
    mapping = {
        "Health": "Healthcare",
        "Immigration": "Immigration",
        "Armed Forces and National Security": "Defense",
        "Veterans' Affairs": "Veterans",
        "Agriculture": "Agriculture",
        # ... add more mappings
    }
    return mapping.get(subject, "Other")
```

### Step 2: Add Committee Context

```python
import yaml

def add_committee_context(votes, legislators_file, committees_file):
    """Add which committee had jurisdiction"""

    # Load Langworthy's committee assignments
    with open(legislators_file) as f:
        legislators = yaml.safe_load(f)

    langworthy = next(l for l in legislators
                      if l["id"]["bioguide"] == "L000600")

    committees = langworthy.get("committees", [])

    # For each vote, check if it went through Langworthy's committees
    for vote in votes:
        bill = vote.get("bill", "")
        if bill:
            # Query Congress.gov for committee referrals
            vote["committees"] = get_bill_committees(bill)
            vote["langworthy_committee_member"] = any(
                c in committees for c in vote["committees"]
            )

    return votes
```

## Documenting Procedural vs. Direct Inaction

### Direct Inaction (Floor Votes)

**Template for fact-check entries:**

```markdown
---
title: "ACA Subsidy Extension: Voted Against Bipartisan Fix"
date: 2025-12-17
topic: "Healthcare"
action_type: "direct_vote"
vote_position: "No"
---

## The Vote

- **Date:** December 17, 2025
- **Bill:** H.R. 1234 - ACA Premium Subsidy Extension Act
- **Langworthy vote:** NO
- **Result:** Failed 216-217
- **Impact:** 24 million Americans face 113% premium increases

## Public Statement

> "I support making healthcare more affordable for working families"
— Press release, October 2025

## The Contradiction

Langworthy voted against extending subsidies that prevent premium spikes,
directly contradicting his stated support for affordability.
```

### Procedural Inaction (Committee Obstruction)

**Template for fact-check entries:**

```markdown
---
title: "PBM Reform: 291 Days of Committee Inaction"
date: 2025-12-17
topic: "Healthcare"
action_type: "procedural_inaction"
committee: "House Oversight and Accountability"
---

## Committee Role

**Member:** Rep. Nicholas Langworthy (R-NY-23)
**Committee:** House Oversight and Accountability Committee
**Jurisdiction:** Pharmacy Benefit Manager oversight
**Member since:** January 3, 2023
**Source:** [congress-legislators/committee-membership-current.yaml](https://github.com/unitedstates/congress-legislators)

## Bill Status

- **Bill:** H.R. 2880 - Pharmacy Benefit Manager Reform Act
- **Introduced:** March 15, 2025
- **Referred to:** House Oversight (Langworthy's committee)
- **Committee action:** None
- **Days in committee:** 291 (as of Dec 31, 2025)
- **Status:** No markup scheduled, no hearing held

**Source:** Congress.gov bill tracker

## Public Statement

**Date:** December 17, 2025
**Context:** Press release on drug pricing

> "We have to act—and we have to act now on comprehensive PBM reform to protect seniors"

**Source:** House Oversight Committee press release

## The Gap

**What Langworthy said:** Immediate action needed
**What his committee did:** No action in 9+ months
**His role:** Voting member with ability to push for committee action

## Committee Context

As a member of the committee with jurisdiction, Langworthy could have:
1. Requested a committee hearing
2. Pushed for markup session
3. Signed onto discharge petition (if leadership blocked it)
4. Publicly pressured committee chairman

**None of these happened.**

## Timeline

| Date | Event |
|------|-------|
| March 15, 2025 | Bill referred to House Oversight |
| Dec 17, 2025 | Langworthy calls for "immediate action" |
| Dec 31, 2025 | Still no committee vote (291 days) |

## Why This Matters

Committee inaction is where most bills die. Unlike floor votes, committee
proceedings get less media attention, making it easier for members to claim
support while enabling legislative failure behind closed doors.

**Langworthy's public urgency + committee inaction = rhetoric without action**
```

## Front Matter Fields for Hugo

Add these fields to your fact-check entries to enable filtering:

```yaml
---
action_type: "direct_vote" | "procedural_inaction" | "statement_contradiction"
vote_position: "Yes" | "No" | "Present" | "Not Voting" | "N/A"
committee: "House Oversight and Accountability"  # if procedural
bill_number: "H.R. 2880"
topic: "Healthcare"
impact_score: 1-5  # How many people affected
veracity: "false" | "misleading" | "true" | "needs_context"
---
```

## Automation Script

Create `scripts/enrich_votes.py`:

```python
#!/usr/bin/env python3
"""
Enrich votes.json with bill titles, topics, and committee context
"""

import json
import os
import requests
import yaml
from pathlib import Path

PROPUBLICA_KEY = os.getenv("PROPUBLICA_API_KEY")
CONGRESS_GOV_KEY = os.getenv("CONGRESS_GOV_API_KEY")

def main():
    # Load current votes
    votes_file = Path("data/votes.json")
    with open(votes_file) as f:
        votes = json.load(f)

    print(f"Loaded {len(votes)} votes")

    # Enrich with ProPublica data
    votes = enrich_with_propublica(votes)

    # Add committee context
    votes = add_committee_info(votes)

    # Save enriched data
    output_file = Path("data/votes_enriched.json")
    with open(output_file, "w") as f:
        json.dump(votes, f, indent=2)

    print(f"Saved enriched data to {output_file}")

    # Generate procedural inaction candidates
    generate_inaction_reports(votes)

if __name__ == "__main__":
    main()
```

Run it:
```bash
export PROPUBLICA_API_KEY=your_key
python3 scripts/enrich_votes.py
```

## Publishing Strategy

### For the Vote Database

1. **Full searchable table** at `/votes/` (using the Hugo template I created)
2. **Topic-specific pages** at `/votes/healthcare/`, `/votes/immigration/`
3. **Downloadable CSV** for researchers

### For Accountability Analysis

1. **Fact-checks section** (what you have now) - individual contradictions
2. **Committee inaction tracker** - dedicated page listing all bills stuck in his committees
3. **Pattern analysis** - aggregate view showing rhetoric vs. action gaps

## Next Steps

1. **Get API keys:**
   - ProPublica: https://www.propublica.org/datastore/api/propublica-congress-api
   - Congress.gov: https://api.congress.gov/sign-up/

2. **Clone congress-legislators repo:**
   ```bash
   cd ../
   git clone https://github.com/unitedstates/congress-legislators.git
   ```

3. **Run enrichment script** (I can help you build this)

4. **Update votes.json** with enriched data

5. **Deploy** - your Hugo template will automatically display the enhanced data

## Legal & Ethical Notes

**Can you republish this data?**
- ✅ Congressional records: Public domain
- ✅ ProPublica API: Explicitly allows republication
- ✅ Congress.gov: Government data, public domain
- ✅ VoteView: Academic use, cite source
- ✅ congress-legislators: CC0 license

**Attribution:**
Always cite sources in your methodology page.

**Updates:**
- Votes: Update after each session (usually weekly)
- Committee data: Monthly or when membership changes
- Bill status: Weekly for active bills

---

**Questions or need help implementing?** Let me know which part to tackle first.
