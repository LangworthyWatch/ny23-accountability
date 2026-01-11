#!/usr/bin/env python3
"""
Master script to run all scrapers
Run this daily to collect new statements and votes
"""

import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Add scrapers directory to path
sys.path.insert(0, str(Path(__file__).parent))

from scrapers.congressional_site import CongressionalSiteScraper
from scrapers.congress_gov import CongressGovScraper
from utils.archiver import Archiver


def scrape_press_releases(limit=20):
    """Scrape press releases in parallel-safe function"""
    print("\n📰 SCRAPING PRESS RELEASES")
    print("-" * 80)
    scraper = CongressionalSiteScraper()
    releases = scraper.scrape_press_releases(limit=limit)
    saved = 0
    if releases:
        saved = scraper.save_releases(releases)
        print(f"✓ Saved {saved} new press releases")
    return releases, saved


def scrape_votes(limit=20):
    """Scrape voting records in parallel-safe function"""
    print("\n🗳️  SCRAPING VOTING RECORDS")
    print("-" * 80)
    scraper = CongressGovScraper()
    votes = scraper.get_recent_votes(limit=limit)
    saved = 0
    if votes:
        saved = scraper.save_votes(votes)
        print(f"✓ Saved {saved} new votes")
    return votes, saved


def main():
    print("=" * 80)
    print("LANGWORTHY ACCOUNTABILITY TRACKER - SCRAPER")
    print("=" * 80)
    print("Running scrapers in parallel for faster collection...\n")

    # Run scrapers in parallel using ThreadPoolExecutor
    releases, votes = None, None
    press_saved, vote_saved = 0, 0

    with ThreadPoolExecutor(max_workers=2) as executor:
        # Submit both scraping tasks to run concurrently
        future_press = executor.submit(scrape_press_releases, 20)
        future_votes = executor.submit(scrape_votes, 20)

        # Wait for both to complete and get results
        try:
            releases, press_saved = future_press.result()
        except Exception as e:
            print(f"❌ Error scraping press releases: {e}")

        try:
            votes, vote_saved = future_votes.result()
        except Exception as e:
            print(f"❌ Error scraping votes: {e}")

    total_collected = press_saved + vote_saved

    # Archive press releases (sequential to respect rate limits)
    if releases:
        print("\n💾 Archiving press releases...")
        archiver = Archiver()
        for release in releases[:5]:  # Archive first 5 to avoid rate limits
            if not release.get('archived_url'):
                try:
                    archive_url = archiver.archive_url(release['url'])
                    if archive_url:
                        release['archived_url'] = archive_url
                        print(f"  ✓ Archived: {release['title'][:50]}...")
                except Exception as e:
                    print(f"  ✗ Failed to archive: {e}")

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"✓ Total new items collected: {total_collected}")
    print(f"  - Press releases: {press_saved}")
    print(f"  - Votes: {vote_saved}")
    print()
    print("Next steps:")
    print("  1. Review collected items: python review_queue.py")
    print("  2. Cross-reference statements with votes")
    print("  3. Create fact-check entries for contradictions")
    print("  4. Publish to langworthywatch.org")
    print()


if __name__ == "__main__":
    main()
