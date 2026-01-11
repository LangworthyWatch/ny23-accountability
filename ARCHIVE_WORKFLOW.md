# Archive.org Workflow for Fact-Checks

## Current Status

**27 pending archives** across 6 fact-check files need to be created.

## Quick Workflow (Per Source)

### 1. Find Original URL
Example: "CBO: Budgetary Effects of H.R. 1" (May 2025)

Google: `site:cbo.gov "Budgetary Effects of H.R. 1" 2025`

Find URL: `https://www.cbo.gov/publication/12345`

### 2. Create Archive
1. Go to: https://web.archive.org/save/
2. Paste URL: `https://www.cbo.gov/publication/12345`
3. Click **"Save Page"**
4. Wait for it to process (10-30 seconds)
5. Copy archive URL: `https://web.archive.org/web/20260107123456/https://www.cbo.gov/publication/12345`

### 3. Update Fact-Check

**Before:**
```markdown
- CBO: "Budgetary Effects of H.R. 1" (May 2025)
  - Archive: https://archive.is/[pending]
```

**After:**
```markdown
- CBO: "Budgetary Effects of H.R. 1" (May 2025)
  - URL: https://www.cbo.gov/publication/12345
  - Archive: https://web.archive.org/web/20260107123456/https://www.cbo.gov/publication/12345
```

## Priority Order (27 total)

### factcheck_infrastructure_credit.md (6 pending) - DO FIRST
High-profile claim, most citations needed

### factcheck_snap_cuts.md (5 pending)
Major policy claim

### factcheck_farm_bill_victory.md (5 pending)
Agricultural policy

### factcheck_medicaid_immigration.md (4 pending)
Healthcare policy

### factcheck_farm_workforce.md (4 pending)
Labor policy

### factcheck_social_security_tax.md (3 pending)
Social security

### factcheck_year_end_newsletter.md (0 archives)
Needs archives added from scratch

## Common Sources to Archive

### Government Sources
- **CBO (Congressional Budget Office)**: https://www.cbo.gov/
- **Congress.gov**: https://www.congress.gov/
- **Federal Register**: https://www.federalregister.gov/

### Policy Organizations
- **Center on Budget and Policy Priorities**: https://www.cbpp.org/
- **Urban Institute**: https://www.urban.org/
- **Tax Policy Center**: https://www.taxpolicycenter.org/

### News
- **WGRZ Buffalo**: https://www.wgrz.com/
- **Buffalo News**: https://buffalonews.com/

### Local
- **NY State OTDA**: https://otda.ny.gov/
- **FeedMore WNY**: https://www.feedmorewny.org/

## Tips

### If Archive.org is slow
Use **Archive.is** instead:
1. Go to: https://archive.is/
2. Paste URL
3. Get short link: `https://archive.is/AbC12`

### If source is paywalled
1. Archive it anyway (Archive.org can sometimes bypass)
2. Or find the press release version
3. Or use archive.is which handles paywalls better

### If source is PDF
Archive.org works fine with PDFs - just paste the direct PDF URL

### Batch Archiving
For efficiency:
1. Open all source URLs in tabs
2. Open archive.org/save in another window
3. Copy-paste-save each URL
4. Takes ~1 minute per source
5. Total time: ~30 minutes for all 27

## Verification

After creating archives, run validator again:
```bash
python3 fact_check_validator_agent.py
```

Should show:
- ✅ 0 pending archives
- ✅ Credibility score ≥ 95%

## Example: Complete One Fact-Check

Let's do `factcheck_social_security_tax.md` (3 pending):

1. Open file: `Fact Checks/factcheck_social_security_tax.md`
2. Find sources section
3. For each `[pending]`:
   - Google the citation
   - Find original URL
   - Archive on archive.org
   - Replace `[pending]` with archive URL
4. Save file
5. Run validator
6. Commit changes

**Time per fact-check**: 10-15 minutes
**Total time for all**: 1-2 hours

## Automation Note

The URLs aren't in the markdown files, so this requires manual research to find each source URL. This is by design - it ensures you verify each source exists and is credible.

---

**Next Steps**:
1. Pick one fact-check to start (recommend: factcheck_social_security_tax.md - only 3 archives)
2. Follow workflow above
3. Run validator to confirm
4. Move to next fact-check

Good luck! This is tedious but important for credibility.
