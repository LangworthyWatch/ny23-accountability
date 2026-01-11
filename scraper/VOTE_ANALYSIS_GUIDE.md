# Vote Analysis Tool - Quick Guide

## What It Does

Analyzes Rep. Langworthy's 1,603 congressional votes to find contradictions with public statements.

## Quick Start

```bash
cd /Users/zachbeaudoin/Langworthywatch/scraper
python3 analyze_votes.py
```

This exports vote data to `/langworthy-tracker/data/votes.json`

---

## Interactive Analysis

```bash
python3
```

Then in Python:

```python
from analyze_votes import VoteAnalyzer
a = VoteAnalyzer()  # Loads all 1,603 votes

# Search by keyword
immigration = a.search_votes(['immigration', 'border'])
print(f"Found {len(immigration)} immigration votes")

# Filter by vote type
no_votes = a.search_votes(['immigration'], vote_type='Nay')
yes_votes = a.search_votes(['immigration'], vote_type='Yea')

# See first result
if immigration:
    a.print_vote(immigration[0])

# Get all topics
topics = a.votes_by_topic()
for topic, votes in topics.items():
    print(f"{topic}: {len(votes)} votes")
```

---

## Finding Contradictions

### Example 1: Healthcare

**Step 1: Find claim in press release**
```bash
grep -i "healthcare" storage/raw_statements/*.json
```

**Step 2: Search votes**
```python
from analyze_votes import VoteAnalyzer
a = VoteAnalyzer()

# Find healthcare votes
healthcare = a.search_votes(['health', 'care', 'aca', 'medicaid'])

# Filter by NO votes (potential contradictions)
healthcare_no = a.search_votes(['health', 'care'], vote_type='Nay')

# Print details
for vote in healthcare_no[:5]:
    a.print_vote(vote)
```

**Step 3: Research specific vote**
- Use the congress.gov URL from the vote data
- Get bill details and full context
- Create fact-check entry if there's a contradiction

### Example 2: Veterans

```python
# Find veteran-related votes
veterans = a.search_votes(['veteran', 'va', 'military'])

# Look for NO votes or Not Voting
vet_no = a.search_votes(['veteran'], vote_type='Nay')
vet_absent = a.search_votes(['veteran'], vote_type='Not Voting')

print(f"Veteran votes (NO): {len(vet_no)}")
print(f"Veteran votes (Absent): {len(vet_absent)}")
```

### Example 3: Budget/Shutdown

```python
# Budget and shutdown votes
budget = a.search_votes(['budget', 'appropriation', 'spending', 'shutdown'])

# Filter by date range (e.g., during shutdown period)
shutdown_votes = [v for v in budget if '2025-10' in v['date'] or '2025-11' in v['date']]

print(f"Votes during Oct-Nov 2025: {len(shutdown_votes)}")
```

---

## Useful Search Keywords

### By Topic

**Healthcare:**
- `['health', 'care', 'aca', 'medicaid', 'medicare', 'hospital']`

**Immigration:**
- `['immigration', 'border', 'asylum', 'sanctuary']`

**Veterans:**
- `['veteran', 'va', 'military', 'defense']`

**Tax:**
- `['tax', 'revenue', 'salt', 'deduction']`

**Budget:**
- `['budget', 'appropriation', 'spending', 'shutdown']`

**Agriculture:**
- `['farm', 'agriculture', 'rural', 'crop']`

### By Vote Type

- `Yea` - Voted yes
- `Nay` - Voted no
- `Not Voting` - Absent/didn't vote
- `Present` - Voted present

---

## Exporting Data

```python
# Export all votes and topics to JSON
a.export_for_site()

# Creates:
# - ../langworthy-tracker/data/votes.json
# - ../langworthy-tracker/data/votes_by_topic.json
```

These JSON files can be used to add interactive features to the website.

---

## Advanced Analysis

### Find Votes by Date Range

```python
# Votes in December 2025
dec_votes = [v for v in a.votes if '2025-12' in v['date']]

# Votes on specific date
dec_18 = [v for v in a.votes if v['date'] == '2025-12-18']

print(f"Votes on Dec 18: {len(dec_18)}")
```

### Count Vote Types

```python
from collections import Counter

# Count how he voted
vote_counts = Counter(v['vote'] for v in a.votes)
print(vote_counts)

# Example output:
# Counter({'Yea': 1200, 'Nay': 350, 'Not Voting': 50, 'Present': 3})
```

### Find All NO Votes

```python
all_no_votes = [v for v in a.votes if v['vote'] == 'Nay']
print(f"Total NO votes: {len(all_no_votes)}")

# Group by month
from collections import defaultdict
by_month = defaultdict(list)
for v in all_no_votes:
    month = v['date'][:7]  # YYYY-MM
    by_month[month].append(v)

for month, votes in sorted(by_month.items()):
    print(f"{month}: {len(votes)} NO votes")
```

### Cross-Reference with Press Releases

```python
import json
from pathlib import Path

# Load press releases
press_releases = []
for file in Path('storage/raw_statements').glob('statement-*.json'):
    with open(file) as f:
        press_releases.append(json.load(f))

# Example: Find health-related claims
health_claims = [
    pr for pr in press_releases
    if any(word in pr.get('full_text', '').lower()
           for word in ['health', 'hospital', 'medicaid'])
]

# Then search votes
health_votes = a.search_votes(['health', 'hospital', 'medicaid'])

print(f"Health claims: {len(health_claims)}")
print(f"Health votes: {len(health_votes)}")
```

---

## Creating Fact-Check Entries

Once you find a contradiction:

1. **Note the details:**
   - Vote date and roll call number
   - How he voted (Yea/Nay)
   - Congress.gov URL

2. **Research the bill:**
   - Visit the URL from vote data
   - Get full bill title and impact
   - Find local impact data

3. **Create entry:**
```bash
cd ../langworthy-tracker
hugo new content/fact-checks/$(date +%Y-%m-%d)-topic-name.md
```

4. **Publish:**
```bash
git add content/fact-checks/*
git commit -m "Add fact-check: topic name"
git push
```

---

## Tips

1. **Use multiple keywords:** Better to search too broad and filter manually
2. **Check roll call numbers:** Sometimes same topic has multiple related votes
3. **Look for patterns:** Repeated NO votes on a topic = strong contradiction
4. **Cross-reference dates:** Match press release dates with vote dates
5. **Save your searches:** Create a notebook of useful search combinations

---

## Troubleshooting

**"Loaded 0 votes"**
- CSV file path is wrong
- Check: `data/langworthy_votes.csv` exists

**"No matches found"**
- Try broader keywords
- Try searching without vote_type filter
- Check if topic has different terminology

**"Module not found"**
- Activate virtual environment:
```bash
source venv/bin/activate
```

---

## Quick Examples

```bash
# One-liner to find specific votes
python3 -c "from analyze_votes import VoteAnalyzer; a=VoteAnalyzer(); print(len(a.search_votes(['border'])))"

# Export to JSON
python3 -c "from analyze_votes import VoteAnalyzer; a=VoteAnalyzer(); a.export_for_site()"

# Count by topic
python3 -c "from analyze_votes import VoteAnalyzer; a=VoteAnalyzer(); [print(f'{k}: {len(v)}') for k,v in a.votes_by_topic().items()]"
```

---

**Remember:** Quality over quantity. One well-documented contradiction is worth more than 10 rushed entries!
