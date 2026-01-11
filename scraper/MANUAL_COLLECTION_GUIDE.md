# Manual Collection Guide - The Better Approach

APIs are unreliable for this purpose. Manual collection gives you better quality, context, and understanding.

## Why Manual is Better

✅ **Better fact-checking** - You understand full context
✅ **No API restrictions** - No rate limits or blocks
✅ **Higher quality** - Hand-picked contradictions
✅ **Legal safety** - Just using public websites normally
✅ **Faster to start** - No debugging scrapers

## Your 30-Minute Weekly Workflow

### Monday Morning (15 min)

**1. Check Press Releases** (5 min)
- Visit: https://langworthy.house.gov/media/press-releases
- Scan recent releases
- Copy interesting claims to a doc

**2. Check Social Media** (5 min)
- Twitter/X: https://twitter.com/RepLangworthy
- Look for policy statements
- Screenshot + save URL

**3. Check Local News** (5 min)
- Google: "Nick Langworthy" site:buffalonews.com
- Google: "Nick Langworthy" site:spectrumlocalnews.com
- Note any claims made in interviews

### When You Find a Claim (15 min)

**1. Archive the Evidence**
- Visit: https://web.archive.org/save/
- Paste the URL
- Save the archive link

**2. Research Votes**
- Visit: https://www.congress.gov/member/nicholas-langworthy/L000266
- Look at voting record
- Find contradictions

**3. Cross-Reference**
- Did he vote against what he claims to support?
- Did he vote for what he claims to oppose?
- Is there a pattern of contradictions?

## Example: Finding a Contradiction

### Step 1: Find Claim
Visit https://langworthy.house.gov/media/press-releases

Found: "I've always supported rural hospitals" (Dec 5, 2024)

### Step 2: Archive
- Go to https://web.archive.org/save/
- Enter URL: https://langworthy.house.gov/media/press-releases/rural-hospitals
- Get archive link: https://web.archive.org/web/20241205.../

### Step 3: Research Votes
Visit https://www.congress.gov/member/nicholas-langworthy/L000266

Search for: "rural hospital" OR "healthcare" OR "medical"

Found votes:
- HR 1234: Rural Hospital Funding Act - Voted **NO**
- HR 5678: Healthcare Workforce Act - Voted **NO**

### Step 4: Create Entry
```bash
cd /Users/zachbeaudoin/Langworthywatch/langworthy-tracker
hugo new content/fact-checks/2024-12-05-rural-hospitals.md
```

Edit the file with:
- His claim
- Archive link
- His votes with congress.gov links
- Let facts speak for themselves

### Step 5: Publish
```bash
git add content/fact-checks/2024-12-05-rural-hospitals.md
git commit -m "Add fact-check: rural hospital funding contradiction"
git push
```

Site updates automatically!

## Quick Links

**Langworthy Sources:**
- Press releases: https://langworthy.house.gov/media/press-releases
- Twitter: https://twitter.com/RepLangworthy
- Congress profile: https://www.congress.gov/member/nicholas-langworthy/L000266

**Research Tools:**
- Archive.org: https://web.archive.org/save/
- Congress votes: https://www.congress.gov
- Bill search: https://www.congress.gov/search

**Your Site:**
- Live site: https://langworthywatch.org
- Local repo: /Users/zachbeaudoin/Langworthywatch/langworthy-tracker

## What You Already Have

✅ **Press release scraper** - Collected 10 releases
✅ **Archived automatically** - Permanent evidence
✅ **Review queue** - For verification

The scraper helps collect, but **you verify and create entries manually**.

## Monthly Goal

**1-2 solid fact-check entries per month**

That's enough to:
- Build credibility
- Demonstrate patterns
- Create accountability
- Avoid burnout

Quality > Quantity!

---

## You Have Everything You Need

1. ✅ Website live at langworthywatch.org
2. ✅ 10 press releases collected
3. ✅ Methodology page published
4. ✅ Professional foundation established

**Next: Create your first fact-check entry!**

Want me to help you find a contradiction and create your first entry?
