# Repository Cleanup Guide

## Status: COMPLETED (January 11, 2026)

The cleanup described in this guide has been completed. The Langworthywatch and Disability-Wiki projects are now properly separated.

---

## Original Problem (RESOLVED)

---

## Current Structure (BROKEN)

### Issue #1: disability-wiki Contains TWO Projects

**Location**: `/Users/zachbeaudoin/disability-wiki/`

**Contains BOTH**:
1. ✅ **Wiki.js setup** for disabilitywiki.org
   - `docker-compose.yml`
   - `install_wikijs.sh`
   - `disability-wiki/` (254 markdown files)

2. ❌ **Hugo site** for langworthywatch.org (WRONG!)
   - `hugo.toml`
   - `content/` (Hugo content)
   - `themes/` (Ananke theme)
   - `CNAME` (langworthywatch.org)

**Git Remote**: https://github.com/Beaudoin0zach/disability-wiki

### Issue #2: Langworthywatch Split Across Locations

**Location 1**: `/Users/zachbeaudoin/Langworthywatch/langworthy-tracker/`
- ✅ Correct Hugo site with git
- Git Remote: https://github.com/LangworthyWatch/ny23-accountability

**Location 2**: `/Users/zachbeaudoin/disability-wiki/` (WRONG!)
- ❌ Duplicate Hugo content
- Wrong git repository

### Issue #3: Scraper is Separate (OK)

**Location**: `/Users/zachbeaudoin/Langworthywatch/scraper/`
- ✅ Python scrapers (private, not in git)
- ✅ This is correct - keep separate

---

## Target Structure (CORRECT)

### Project 1: Disability Wiki
```
/Users/zachbeaudoin/disability-wiki/
├── .git/                     # Git: github.com/Beaudoin0zach/disability-wiki
├── docker-compose.yml        # Wiki.js configuration
├── install_wikijs.sh         # Wiki.js installer
├── disability-wiki/          # 254 markdown content files
├── scripts/                  # Python utilities
│   ├── generate_descriptions.py
│   └── validate_wiki_links.py
├── docs/                     # Documentation
├── backups/                  # Backup storage
├── claude.md                 # Technical documentation
├── README.md                 # Project README
├── QUICK_REFERENCE.md        # Command cheatsheet
└── CHANGELOG.md              # Version history
```

**Remove from disability-wiki**:
- ❌ hugo.toml
- ❌ content/ (Hugo)
- ❌ themes/
- ❌ archetypes/
- ❌ static/
- ❌ CNAME (langworthywatch.org)

### Project 2: LangworthyWatch
```
/Users/zachbeaudoin/Langworthywatch/
├── langworthy-tracker/       # Hugo site (PUBLIC)
│   ├── .git/                 # Git: github.com/LangworthyWatch/ny23-accountability
│   ├── content/              # Hugo content
│   ├── themes/               # Ananke theme
│   ├── hugo.toml             # Hugo config
│   ├── static/CNAME          # langworthywatch.org
│   └── README.md
│
├── scraper/                  # Data collection (PRIVATE)
│   ├── scrapers/
│   ├── utils/
│   ├── storage/
│   ├── run_scraper.py
│   └── README.md
│
├── claude_docs.md            # Technical documentation
├── README.md                 # Project overview
├── QUICK_REFERENCE.md        # Command cheatsheet
├── CHANGELOG.md              # Version history
└── REPOSITORY_CLEANUP.md     # This file
```

---

## Cleanup Steps

### Step 1: Backup Everything (CRITICAL!)

```bash
# Backup disability-wiki
cd ~
tar -czf disability-wiki-backup-$(date +%Y%m%d).tar.gz disability-wiki/

# Backup Langworthywatch
tar -czf langworthywatch-backup-$(date +%Y%m%d).tar.gz Langworthywatch/

# Verify backups
ls -lh *-backup-*.tar.gz
```

### Step 2: Clean disability-wiki (Remove Hugo Files)

```bash
cd /Users/zachbeaudoin/disability-wiki

# Remove Hugo-specific files
rm hugo.toml
rm CNAME
rm -rf content/
rm -rf themes/
rm -rf archetypes/
rm -rf static/
rm -rf public/  # If it exists

# Keep only Wiki.js files
# - docker-compose.yml
# - install_wikijs.sh
# - disability-wiki/
# - scripts/
# - docs/
# - backups/
# - claude.md
# - README.md
# - QUICK_REFERENCE.md
# - CHANGELOG.md
```

### Step 3: Verify Langworthywatch Hugo Site

```bash
cd /Users/zachbeaudoin/Langworthywatch/langworthy-tracker

# Check git remote
git remote -v
# Should show: github.com/LangworthyWatch/ny23-accountability

# Verify Hugo works
hugo server -D
# Visit http://localhost:1313
```

### Step 4: Update Git Repositories

#### disability-wiki Repository
```bash
cd /Users/zachbeaudoin/disability-wiki

# Check status
git status

# Add removed files to commit
git add -A
git commit -m "Remove Langworthywatch content - separate projects"

# Push changes
git push origin main
```

#### Langworthywatch Repository
```bash
cd /Users/zachbeaudoin/Langworthywatch/langworthy-tracker

# Verify content is here
ls content/

# Check git status
git status

# If needed, commit and push
git add .
git commit -m "Consolidated Langworthywatch Hugo site"
git push origin main
```

### Step 5: Verify Separation

```bash
# Check disability-wiki has no Hugo files
cd /Users/zachbeaudoin/disability-wiki
ls | grep -E "(hugo|content|themes)"
# Should return nothing

# Check Langworthywatch has Hugo site
cd /Users/zachbeaudoin/Langworthywatch/langworthy-tracker
ls | grep -E "(hugo|content|themes)"
# Should show: hugo.toml, content/, themes/

# Check git remotes are correct
cd /Users/zachbeaudoin/disability-wiki
git remote -v
# Should show: github.com/Beaudoin0zach/disability-wiki

cd /Users/zachbeaudoin/Langworthywatch/langworthy-tracker
git remote -v
# Should show: github.com/LangworthyWatch/ny23-accountability
```

---

## Post-Cleanup Verification

### Test disability-wiki
```bash
cd /Users/zachbeaudoin/disability-wiki

# Start Wiki.js locally
export PATH="/Applications/Docker.app/Contents/Resources/bin:$PATH"
docker compose up -d

# Access: http://localhost:8080
open http://localhost:8080

# Run scripts
python3 scripts/validate_wiki_links.py
python3 scripts/generate_descriptions.py
```

### Test Langworthywatch
```bash
cd /Users/zachbeaudoin/Langworthywatch

# Test Hugo site
cd langworthy-tracker
hugo server -D
# Access: http://localhost:1313

# Test scrapers
cd ../scraper
source venv/bin/activate
python run_scraper.py
```

---

## Future Workflow

### Working on disability-wiki
```bash
cd /Users/zachbeaudoin/disability-wiki

# Always verify git remote first
git remote -v
# Should be: github.com/Beaudoin0zach/disability-wiki

# Make changes to Wiki.js, documentation, scripts
# Commit and push
git add .
git commit -m "Update disability wiki"
git push origin main
```

### Working on Langworthywatch
```bash
cd /Users/zachbeaudoin/Langworthywatch/langworthy-tracker

# Always verify git remote first
git remote -v
# Should be: github.com/LangworthyWatch/ny23-accountability

# Make changes to Hugo content
# Commit and push
git add content/fact-checks/new-entry.md
git commit -m "Add fact-check: topic"
git push origin main
```

---

## Common Mistakes to Avoid

### ❌ DON'T
- Edit Hugo files in disability-wiki directory
- Commit Langworthywatch content to disability-wiki repo
- Mix the two projects in one directory
- Push to wrong git remote

### ✅ DO
- Keep projects completely separate
- Always check `git remote -v` before committing
- Use separate terminal windows/tabs for each project
- Verify you're in correct directory before git operations

---

## Git Remote Quick Reference

```bash
# Check current remote
git remote -v

# Change remote (if wrong)
git remote set-url origin <correct-url>

# Verify remote changed
git remote -v
```

### Correct Remotes
- **disability-wiki**: `https://github.com/Beaudoin0zach/disability-wiki.git`
- **Langworthywatch**: `https://github.com/LangworthyWatch/ny23-accountability.git`

---

## If Things Go Wrong

### Restore from Backup
```bash
# If cleanup went wrong, restore from backup
cd ~
tar -xzf disability-wiki-backup-YYYYMMDD.tar.gz
tar -xzf langworthywatch-backup-YYYYMMDD.tar.gz
```

### Reset Git Repository
```bash
# If git got messed up
cd <project-directory>

# See what changed
git status

# Discard all local changes
git reset --hard origin/main

# Pull fresh copy
git pull origin main
```

---

## Summary

### Cleanup Completed (January 11, 2026)

The following issues have been resolved:
- ✅ Hugo content removed from disability-wiki repository
- ✅ Langworthywatch content lives only in `/projects/Langworthywatch/langworthy-tracker/`
- ✅ .DS_Store and binary files removed from git tracking
- ✅ Proper .gitignore added to prevent future issues
- ✅ Scraper archiver improved with rate limiting and exponential backoff
- ✅ Validator now fails hard on missing dependencies

### Current State
- ✅ disability-wiki = Wiki.js only (github.com/Beaudoin0zach/disability-wiki)
- ✅ Langworthywatch = Hugo site + scrapers (github.com/LangworthyWatch/ny23-accountability)
- ✅ Clear separation, no confusion
- ✅ Correct git remotes for each project

---

*Repository Cleanup Guide - Updated January 11, 2026*
