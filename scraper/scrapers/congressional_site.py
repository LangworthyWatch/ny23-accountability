"""
Scraper for Rep. Langworthy's official congressional website
Collects press releases, statements, and newsletters
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import hashlib
import os
from pathlib import Path


class CongressionalSiteScraper:
    def __init__(self, storage_dir="../storage/raw_statements"):
        self.base_url = "https://langworthy.house.gov"
        self.press_url = f"{self.base_url}/media/press-releases"
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)

    def scrape_press_releases(self, limit=50):
        """Scrape press releases from official congressional site"""

        print(f"Fetching press releases from {self.press_url}...")

        try:
            response = requests.get(self.press_url, timeout=30)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching press releases: {e}")
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        releases = []

        # Find press release items (updated for langworthy.house.gov structure)
        # Site uses div.views-row for each press release
        articles = soup.find_all('div', class_='views-row', limit=limit)

        if not articles:
            # Fallback to older structure
            articles = soup.find_all('article', class_='news-item', limit=limit)

        print(f"Found {len(articles)} press release(s)")

        for article in articles:
            try:
                release = self._parse_press_release(article)
                if release:
                    releases.append(release)
            except Exception as e:
                print(f"Error parsing article: {e}")
                continue

        return releases

    def _parse_press_release(self, article):
        """Parse individual press release article"""

        # Find title and link - langworthy.house.gov uses div.h3 > a structure
        title_elem = article.find('div', class_='h3')
        if not title_elem:
            # Fallback to h2/h3
            title_elem = article.find('h2') or article.find('h3')

        if not title_elem:
            return None

        link_elem = title_elem.find('a')
        if not link_elem or not link_elem.get('href'):
            return None

        title = link_elem.get_text(strip=True)
        url = link_elem['href']

        # Make URL absolute if relative
        if url.startswith('/'):
            url = self.base_url + url

        # Find date - looks for div.col-auto containing date text
        date_elem = article.find('div', class_='col-auto')
        date_str = None
        if date_elem:
            date_text = date_elem.get_text(strip=True)
            # Extract just the date part (e.g., "December 5, 2025")
            if 'Press Release' not in date_text:
                date_str = date_text

        # Find snippet/teaser from blockquote or evo-press-release__body
        snippet_elem = article.find('div', class_='evo-press-release__body') or article.find('blockquote')
        snippet = snippet_elem.get_text(strip=True)[:200] if snippet_elem else ""

        # Get full text from article page
        full_text = self._get_full_text(url)

        # Generate unique ID
        content_hash = hashlib.md5(url.encode()).hexdigest()[:12]

        release = {
            'id': content_hash,
            'title': title,
            'date': date_str or datetime.now().isoformat(),
            'url': url,
            'snippet': snippet,
            'full_text': full_text,
            'source': 'congressional_website',
            'source_type': 'press_release',
            'collected_date': datetime.now().isoformat(),
            'verification_status': 'pending',
            'archived_url': None,
            'flags': []
        }

        return release

    def _get_full_text(self, url):
        """Fetch full text of press release from its page"""

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            # Try to find main content area (common patterns)
            content = (
                soup.find('div', class_='press-release-content') or
                soup.find('div', class_='body-content') or
                soup.find('article') or
                soup.find('div', class_='content')
            )

            if content:
                # Remove script and style elements
                for script in content(['script', 'style']):
                    script.decompose()

                return content.get_text(separator='\n', strip=True)

            return ""

        except Exception as e:
            print(f"Error fetching full text from {url}: {e}")
            return ""

    def save_releases(self, releases):
        """Save press releases to JSON files for review"""

        saved_count = 0
        skipped_count = 0

        for release in releases:
            filename = f"{release['collected_date'][:10]}-{release['id']}.json"
            filepath = self.storage_dir / filename

            # Check if already exists
            if filepath.exists():
                skipped_count += 1
                continue

            try:
                with open(filepath, 'w') as f:
                    json.dump(release, f, indent=2)

                print(f"✓ Saved: {release['title'][:60]}...")
                saved_count += 1

            except Exception as e:
                print(f"Error saving {filename}: {e}")

        print(f"\nSummary: {saved_count} saved, {skipped_count} skipped (already exists)")
        return saved_count


def main():
    """Run scraper as standalone script"""

    scraper = CongressionalSiteScraper()

    print("=" * 80)
    print("Langworthy Congressional Website Scraper")
    print("=" * 80)
    print()

    releases = scraper.scrape_press_releases()

    if releases:
        saved = scraper.save_releases(releases)
        print(f"\n✓ Scraped {len(releases)} press releases, saved {saved} new ones")
    else:
        print("\n⚠ No press releases found")


if __name__ == "__main__":
    main()
