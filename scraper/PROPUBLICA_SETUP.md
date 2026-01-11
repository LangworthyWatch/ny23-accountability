# ProPublica Congress API Setup

ProPublica offers a free API for congressional voting records with no bot detection issues!

## Get Your Free API Key

1. **Go to**: https://www.propublica.org/datastore/api/propublica-congress-api

2. **Click "Request an API Key"**

3. **Fill out the form**:
   - Name: Your name
   - Email: Your email
   - Organization: Can say "Personal research project" or "Independent journalism"
   - Use: "Congressional accountability tracking"

4. **Check your email** - API key arrives instantly

5. **Save your API key** - you'll need it to run the scraper

## Using the ProPublica Scraper

### Method 1: Set Environment Variable (Recommended)

```bash
# Add to your ~/.zshrc or ~/.bash_profile
export PROPUBLICA_API_KEY="your-api-key-here"

# Reload shell
source ~/.zshrc

# Run scraper
cd /Users/zachbeaudoin/Langworthywatch/scraper
source venv/bin/activate
python3 scrapers/propublica_votes.py
```

### Method 2: Enter When Prompted

```bash
cd /Users/zachbeaudoin/Langworthywatch/scraper
source venv/bin/activate
python3 scrapers/propublica_votes.py

# It will prompt you for the API key
```

## What You'll Get

The ProPublica API provides:
- ✅ All of Langworthy's votes
- ✅ Bill numbers and titles
- ✅ How he voted (Yes/No/Present/Not Voting)
- ✅ Vote dates
- ✅ Vote results
- ✅ Links to bills

No 403 errors, no bot detection, completely free!

## Rate Limits

- **5,000 requests per day**
- More than enough for your needs
- Be respectful - don't hammer the API

## Example Data You'll Get

```json
{
  "bill": "H R 1234",
  "bill_title": "Rural Hospital Funding Act",
  "vote_cast": "No",
  "date": "2024-03-15",
  "result": "Passed",
  "question": "On Passage"
}
```

## Next Steps

1. Get your API key
2. Run `python3 scrapers/propublica_votes.py`
3. Review votes in `storage/raw_statements/`
4. Cross-reference with press release claims
5. Find contradictions!

---

**This is way better than scraping congress.gov!**
