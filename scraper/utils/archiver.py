"""
Archiver utility for saving evidence
- Archives URLs to Archive.org (Wayback Machine)
- Takes screenshots of web pages
- Ensures evidence is preserved permanently
"""

import requests
import time
import random
from pathlib import Path
from datetime import datetime


class Archiver:
    # Rate limiting constants
    DEFAULT_DELAY = 10  # seconds between archive requests
    MAX_RETRIES = 3
    INITIAL_BACKOFF = 30  # seconds
    MAX_BACKOFF = 300  # 5 minutes max

    def __init__(self, screenshot_dir="../storage/archives/screenshots", delay_between_requests=None):
        self.wayback_save_url = "https://web.archive.org/save/"
        self.wayback_check_url = "https://archive.org/wayback/available"
        self.screenshot_dir = Path(screenshot_dir)
        self.screenshot_dir.mkdir(parents=True, exist_ok=True)
        self.delay = delay_between_requests if delay_between_requests is not None else self.DEFAULT_DELAY
        self._last_request_time = 0

    def _wait_for_rate_limit(self):
        """Enforce delay between archive requests."""
        elapsed = time.time() - self._last_request_time
        if elapsed < self.delay:
            wait_time = self.delay - elapsed
            print(f"  Rate limiting: waiting {wait_time:.1f}s...")
            time.sleep(wait_time)
        self._last_request_time = time.time()

    def archive_url(self, url, force_new=False):
        """
        Save URL to Internet Archive (Wayback Machine)

        Uses rate limiting and exponential backoff to handle Archive.org limits.

        Args:
            url: URL to archive
            force_new: Force a new snapshot even if one exists

        Returns:
            str: Archive.org URL of saved page, or None if failed
        """

        if not force_new:
            # Check if already archived recently
            existing = self.check_if_archived(url)
            if existing:
                print(f"Already archived: {existing}")
                return existing

        print(f"Archiving {url}...")

        backoff = self.INITIAL_BACKOFF
        for attempt in range(1, self.MAX_RETRIES + 1):
            try:
                # Respect rate limiting
                self._wait_for_rate_limit()

                # Request archive
                save_url = self.wayback_save_url + url
                response = requests.get(save_url, timeout=120)

                if response.status_code == 200:
                    # Get archive URL from response
                    archive_url = response.url

                    # Clean up the URL
                    if 'web.archive.org/web/' in archive_url:
                        print(f"✓ Archived: {archive_url}")
                        return archive_url
                    else:
                        print(f"⚠ Archive request succeeded but URL format unexpected")
                        return None

                elif response.status_code == 429:
                    # Rate limited - back off exponentially
                    jitter = random.uniform(0, backoff * 0.1)
                    wait_time = backoff + jitter
                    print(f"⚠ Rate limited (429). Attempt {attempt}/{self.MAX_RETRIES}. Waiting {wait_time:.1f}s...")
                    time.sleep(wait_time)
                    backoff = min(backoff * 2, self.MAX_BACKOFF)
                    continue

                elif response.status_code == 523:
                    # Origin unreachable - Archive.org can't reach the site
                    print(f"✗ Archive.org cannot reach origin (523): {url}")
                    return None

                elif response.status_code >= 500:
                    # Server error - retry with backoff
                    jitter = random.uniform(0, backoff * 0.1)
                    wait_time = backoff + jitter
                    print(f"⚠ Server error ({response.status_code}). Attempt {attempt}/{self.MAX_RETRIES}. Waiting {wait_time:.1f}s...")
                    time.sleep(wait_time)
                    backoff = min(backoff * 2, self.MAX_BACKOFF)
                    continue

                else:
                    print(f"✗ Archive failed with status {response.status_code}")
                    return None

            except requests.Timeout:
                print(f"⚠ Request timed out. Attempt {attempt}/{self.MAX_RETRIES}.")
                if attempt < self.MAX_RETRIES:
                    time.sleep(backoff)
                    backoff = min(backoff * 2, self.MAX_BACKOFF)
                continue

            except requests.RequestException as e:
                print(f"✗ Archive error for {url}: {e}")
                return None

        print(f"✗ Failed to archive after {self.MAX_RETRIES} attempts: {url}")
        return None

    def check_if_archived(self, url, days_old=7):
        """
        Check if URL has been archived recently

        Args:
            url: URL to check
            days_old: Consider archives newer than this many days

        Returns:
            str: Archive URL if found, None otherwise
        """

        try:
            response = requests.get(
                self.wayback_check_url,
                params={'url': url},
                timeout=30
            )

            if response.status_code == 200:
                data = response.json()

                if data.get('archived_snapshots', {}).get('closest'):
                    snapshot = data['archived_snapshots']['closest']
                    if snapshot.get('available'):
                        return snapshot['url']

            return None

        except Exception as e:
            print(f"Error checking archive status: {e}")
            return None

    def take_screenshot(self, url, output_filename=None):
        """
        Take screenshot of webpage

        Note: Requires selenium and a webdriver (Chrome/Firefox)
        This is a basic implementation - may need webdriver setup

        Args:
            url: URL to screenshot
            output_filename: Optional filename for screenshot

        Returns:
            str: Path to screenshot file, or None if failed
        """

        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
        except ImportError:
            print("⚠ Selenium not installed. Run: pip install selenium")
            print("  Also install ChromeDriver: brew install chromedriver")
            return None

        if not output_filename:
            # Generate filename from URL and timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            safe_url = url.replace('https://', '').replace('http://', '')
            safe_url = ''.join(c if c.isalnum() or c in '-_' else '_' for c in safe_url)[:50]
            output_filename = f"{safe_url}_{timestamp}.png"

        output_path = self.screenshot_dir / output_filename

        print(f"Taking screenshot of {url}...")

        options = Options()
        options.headless = True
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = None
        try:
            driver = webdriver.Chrome(options=options)
            driver.get(url)

            # Wait for page to load
            time.sleep(2)

            # Take screenshot
            driver.save_screenshot(str(output_path))

            print(f"✓ Screenshot saved: {output_path}")
            return str(output_path)

        except Exception as e:
            print(f"✗ Screenshot error: {e}")
            return None

        finally:
            if driver:
                driver.quit()

    def archive_with_screenshot(self, url, take_screenshot=False):
        """
        Archive URL and optionally take screenshot

        Args:
            url: URL to archive
            take_screenshot: Whether to also take a screenshot

        Returns:
            dict: {'archive_url': str, 'screenshot_path': str}
        """

        result = {
            'archive_url': None,
            'screenshot_path': None
        }

        # Archive to Wayback Machine
        result['archive_url'] = self.archive_url(url)

        # Optionally take screenshot
        if take_screenshot:
            result['screenshot_path'] = self.take_screenshot(url)

        return result


def main():
    """Test archiver"""

    archiver = Archiver()

    # Test URL
    test_url = "https://langworthy.house.gov"

    print("=" * 80)
    print("Testing Archiver")
    print("=" * 80)
    print()

    # Archive URL
    archive_url = archiver.archive_url(test_url)

    if archive_url:
        print(f"\n✓ Success! Archived at: {archive_url}")
    else:
        print("\n✗ Archiving failed")

    # Screenshot would require Selenium setup
    print("\nNote: Screenshot feature requires Selenium + ChromeDriver")
    print("Install with: pip install selenium && brew install chromedriver")


if __name__ == "__main__":
    main()
