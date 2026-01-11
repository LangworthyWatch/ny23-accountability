# Fact-Check Validator Agent Setup Guide

## Overview

The fact-check validator agent ensures political accountability content meets credibility standards:
- **Sources verification**: Checks every fact-check has a Sources section
- **Archive.org tracking**: Monitors pending archive backups
- **Claims identification**: Counts factual assertions requiring citations
- **Credibility scoring**: Calculates overall content reliability (0-100%)

## Quick Start

### 1. Run the Validator

```bash
cd /Users/zachbeaudoin/Langworthywatch
python3 fact_check_validator_agent.py
```

### 2. View Results

```bash
# View JSON report
cat fact_check_validation_report.json | python3 -m json.tool
```

## What Gets Validated

### 1. Sources Section ✅ **Critical**

**Requirement**: Every fact-check must have a `## Sources` or `### Sources` section

**Example**:
```markdown
### Sources

**Congressional Budget Office:**
- CBO: "Budgetary Effects of H.R. 1" (May 2025)
  - Archive: https://archive.is/ABC123

**Policy Analysis:**
- Center on Budget and Policy Priorities: "Analysis" (2025)
  - Archive: https://web.archive.org/web/20250101/example.com
```

**Validation**:
- Checks for heading containing "Sources" or "Source"
- Counts number of source entries
- Warns if < 3 sources for substantial claims

**Why it matters**: Without sources, claims are unverifiable and lack credibility.

### 2. Archive.org Backups ⚠️ **High Priority**

**Requirement**: All external sources should have Archive.org or Archive.is backups

**Pending Format** (needs action):
```markdown
- Archive: https://archive.is/[pending]
```

**Completed Format** (verified):
```markdown
- Archive: https://archive.is/ABC123
- Archive: https://web.archive.org/web/20250101120000/example.com
```

**Validation**:
- Counts total archive URLs
- Identifies pending archives: `[pending]`
- Flags fact-checks with no archives despite having sources

**Why it matters**: External links die. Archive.org preserves evidence permanently.

### 3. Claims Identification 📊 **Statistical**

**Automatically identifies sentences containing**:
- Statistical claims: "40 million people", "$295 billion", "30% reduction"
- Authority citations: "according to CBO", "reported by", "study shows"
- Data references: "data shows", "analysis found", "estimates"

**Purpose**: Ensures claims-to-sources ratio is reasonable

**Example matched patterns**:
- ✅ "The CBO estimates H.R. 1 would reduce SNAP by $295 billion"
- ✅ "According to CBPP, 5.4 million people would lose benefits"
- ✅ "Food insecurity increased 16% in 2024"

### 4. URL Accessibility (Optional)

**With `requests` module installed**:
- Checks HTTP status of source URLs
- Identifies broken links in Sources section
- Verifies archive.org backups are accessible

**Without `requests`**: Skips URL checking (still validates structure)

## Command Options

```bash
# Basic validation
python3 fact_check_validator_agent.py

# Custom content directory
python3 fact_check_validator_agent.py --content-root "/path/to/Fact Checks"

# Custom output file
python3 fact_check_validator_agent.py --output my_report.json
```

## Understanding the Report

### Credibility Score

**Formula**: Starts at 100, deductions for:
- Missing Sources section: -20 points each
- Pending archives: -5 points each
- Sources section but no archives: -10 points each

**Scoring**:
- **95-100**: Excellent - all sources properly archived
- **90-94**: Good - minor pending archives
- **80-89**: Fair - multiple pending archives or missing sources
- **< 80**: Poor - critical credibility issues

### Issue Severity Levels

**Critical** (🔴 Immediate action):
- Many claims but no Sources section
- Validation errors preventing scan

**High** (🔴 High priority):
- No Sources section found
- Sources section but zero archive backups

**Medium** (⚠️ Medium priority):
- Pending archive URLs
- Few source entries (< 3)

**Warning** (ℹ️ Low priority):
- No archive.org backups when sources exist
- Formatting inconsistencies

## Creating Archive.org Backups

### Manual Process

1. Visit the Wayback Machine:
   ```
   https://web.archive.org/save/
   ```

2. Enter URL to archive:
   ```
   https://www.cbo.gov/publication/12345
   ```

3. Click "Save Page" and wait for confirmation

4. Copy the archive URL:
   ```
   https://web.archive.org/web/20260106151530/https://www.cbo.gov/publication/12345
   ```

5. Update fact-check markdown:
   ```markdown
   - CBO: "Report Title" (2025)
     - Original: https://www.cbo.gov/publication/12345
     - Archive: https://web.archive.org/web/20260106151530/https://www.cbo.gov/publication/12345
   ```

### Bulk Archiving Script

Create `archive_pending.sh`:

```bash
#!/bin/bash
# Archive all pending URLs

URLS=(
  "https://www.cbo.gov/publication/12345"
  "https://www.cbpp.org/research/policy-basics"
  "https://www.urban.org/research/publication"
)

for url in "${URLS[@]}"; do
  echo "Archiving: $url"
  curl -s "https://web.archive.org/save/$url"
  sleep 5  # Rate limiting
done
```

### Archive.is (Alternative)

For sites that block Archive.org:

```bash
# Visit archive.is
https://archive.is/

# Enter URL and capture
# Copy short URL: https://archive.is/ABC123
```

## Scheduling

### Weekly Validation (Recommended)

```bash
crontab -e
```

Add:
```cron
# Run weekly on Sundays at 11 AM
0 11 * * 0 cd /Users/zachbeaudoin/Langworthywatch && python3 fact_check_validator_agent.py >> fact_check_validator.log 2>&1
```

### Pre-Publish Validation

Add to git pre-commit hook:

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Run validator on staged fact-checks
python3 fact_check_validator_agent.py

if [ $? -ne 0 ]; then
  echo "❌ Fact-check validation failed. Fix issues before committing."
  exit 1
fi
```

## Integration with Scraper

Validate after scraper runs new content:

```bash
# In scraper monitor or cron job
cd /Users/zachbeaudoin/Langworthywatch/scraper
python3 run_scraper.py

# Then validate fact-checks
cd /Users/zachbeaudoin/Langworthywatch
python3 fact_check_validator_agent.py
```

## Interpreting Results

### Current Status (Example)

```
Fact-checks scanned: 7
Total issues: 6
  Medium: 6

Claims identified: 59
Files with Sources section: 7/7 ✓
Archive.org URLs: 27
Pending archives: 27 ⚠️
```

**Translation**: All fact-checks have Sources sections (good!), but 27 archive backups are still pending creation.

### Action Priority

1. **First**: Create archive backups for pending URLs (27 total)
2. **Second**: Verify archives are accessible
3. **Third**: Ensure claims-to-sources ratio is reasonable

## Workflow Integration

### Content Creation Checklist

When creating new fact-checks:

- [ ] Write fact-check content
- [ ] Add Sources section with all citations
- [ ] Create Archive.org backup for each source URL
- [ ] Replace `[pending]` with actual archive URL
- [ ] Run `python3 fact_check_validator_agent.py`
- [ ] Fix any issues reported
- [ ] Commit to git

### Monthly Audit

- [ ] Run validator
- [ ] Check credibility score trend
- [ ] Update broken external links
- [ ] Re-archive updated sources
- [ ] Document common citation patterns

## Common Issues & Fixes

### "No Sources section found"

**Fix**:
```markdown
# Add at end of fact-check

---

### Sources

**Primary Sources:**
- [Organization]: "[Title]" ([Date])
  - Original: [URL]
  - Archive: [Archive URL]

**Supporting Evidence:**
- [Source 2]
  - Archive: [URL]
```

### "Archive URLs still pending"

**Fix**:
1. Visit https://web.archive.org/save/
2. Enter each URL marked `[pending]`
3. Wait for archive completion
4. Replace `[pending]` with actual archive URL

### "No Archive.org backups found for sources"

**Fix**: Add archive URLs to existing sources:

```markdown
**Before:**
- CBO: "Report Title" (2025)

**After:**
- CBO: "Report Title" (2025)
  - Original: https://www.cbo.gov/publication/12345
  - Archive: https://web.archive.org/web/[timestamp]/https://www.cbo.gov/publication/12345
```

### "Few source entries"

**Fix**: Add more supporting sources:
- Congressional records
- Independent fact-checkers (FactCheck.org, PolitiFact)
- Local news coverage
- Academic research
- Government data

## Best Practices

### 1. Archive Immediately

Create archive backups as soon as you cite a source. Don't wait.

### 2. Multiple Archives

For critical sources, create backups on both:
- Archive.org (wayback machine)
- Archive.is (archive.today)

### 3. Local Backups

Download PDFs of crucial documents:
```bash
mkdir -p "Fact Checks/evidence-backups"
wget -P "Fact Checks/evidence-backups" "https://www.cbo.gov/report.pdf"
```

### 4. Verify Archives Work

Test archive URLs after creation:
```bash
curl -I "https://web.archive.org/web/[timestamp]/[url]"
```

### 5. Document Archive Dates

Include archive date in citation:
```markdown
- CBO: "Report" (May 2025)
  - Archived: January 6, 2026
  - Archive: [URL]
```

## Automation Ideas

### Auto-Archive New Sources

```python
# archive_new_sources.py
import re
import requests

def archive_url(url):
    """Submit URL to Archive.org"""
    save_url = f"https://web.archive.org/save/{url}"
    response = requests.get(save_url)
    # Parse archive URL from response
    return archive_url

# Extract URLs from fact-check
# Archive each one
# Update markdown with archive URLs
```

### Archive Validation

```python
# validate_archives.py
import requests

def check_archive_exists(url):
    """Verify archive URL is accessible"""
    response = requests.head(url)
    return response.status_code == 200
```

## Maintenance

### Weekly Tasks

- [ ] Run fact-check validator
- [ ] Create pending archive backups
- [ ] Verify credibility score ≥ 95
- [ ] Update broken source URLs

### Monthly Tasks

- [ ] Re-archive updated sources
- [ ] Check archive.org for takedowns
- [ ] Add new sources for ongoing stories
- [ ] Review claims-to-sources ratio

### Quarterly Tasks

- [ ] Audit all archive URLs still accessible
- [ ] Download local PDF backups of critical sources
- [ ] Update documentation with new citation patterns

## Troubleshooting

### Validator not finding fact-checks

```bash
# Check file naming convention
ls -la "Fact Checks"/factcheck_*.md

# Files should start with "factcheck_"
# Example: factcheck_snap_cuts.md
```

### Archive.org not archiving

Some sites block archive.org crawlers:
1. Try archive.is instead
2. Download PDF and host on GitHub
3. Quote extensively in fact-check text

### False positives on claims

Adjust patterns in code if needed:
```python
# Edit fact_check_validator_agent.py
self.claim_indicators = [
    re.compile(r'your_custom_pattern'),
]
```

## Integration with GitHub Actions

Create `.github/workflows/fact-check-validator.yml`:

```yaml
name: Fact-Check Validation

on:
  pull_request:
    paths:
      - 'Fact Checks/*.md'
  workflow_dispatch:

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Run fact-check validator
        run: python3 fact_check_validator_agent.py

      - name: Comment on PR
        if: failure()
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '⚠️ Fact-check validation failed. Review sources and archives.'
            })
```

## Standards Checklist

High-quality fact-checks should have:

- [ ] Clear statement of claim with date/source
- [ ] Supporting data from authoritative sources
- [ ] Sources section with ≥ 3 citations
- [ ] Archive.org backup for every external URL
- [ ] Local context (NY-23 specific data)
- [ ] Questions section highlighting contradictions
- [ ] No pending archives (`[pending]` replaced)
- [ ] Credibility score ≥ 95%

## Next Steps

After setting up the fact-check validator:

1. Run initial validation
2. Create all pending archive backups (27 currently)
3. Schedule weekly automated runs
4. Add to pre-publish checklist
5. Monitor credibility score trend

---

**Estimated Time**: 8-10 hours for implementation + ongoing maintenance
**Value**: Ensures political accountability work is bulletproof and verifiable
**Target Score**: ≥ 95% credibility

*Last Updated: January 6, 2026*
