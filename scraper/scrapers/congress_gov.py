"""
Scraper for Congress.gov voting records
Collects votes, bill sponsorships, and floor statements
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import hashlib
from pathlib import Path


class CongressGovScraper:
    def __init__(self, storage_dir="../storage/raw_statements"):
        # Langworthy's member ID (NY-23, elected 2022)
        self.member_id = "L000266"
        self.base_url = "https://www.congress.gov"
        self.member_url = f"{self.base_url}/member/nicholas-langworthy/{self.member_id}"
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)

    def get_recent_votes(self, congress=118, limit=100):
        """Get voting record from congress.gov"""

        print(f"Fetching votes for Congress {congress}...")

        # Congress.gov has an API-like structure for votes
        votes_url = f"{self.member_url}?congress={congress}"

        # Add headers to appear as a normal browser (avoid 403 errors)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

        try:
            response = requests.get(votes_url, headers=headers, timeout=30)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching votes: {e}")
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        votes = []

        # Find votes section
        # Note: Congress.gov structure may vary, this is a starting point
        vote_items = soup.find_all('li', class_='expanded')[:limit]

        if not vote_items:
            # Try alternative structure
            vote_table = soup.find('table', class_='item_table')
            if vote_table:
                vote_items = vote_table.find_all('tr')[1:limit+1]  # Skip header

        print(f"Found {len(vote_items)} vote(s)")

        for item in vote_items:
            try:
                vote = self._parse_vote(item, congress)
                if vote:
                    votes.append(vote)
            except Exception as e:
                print(f"Error parsing vote: {e}")
                continue

        return votes

    def _parse_vote(self, item, congress):
        """Parse individual vote record"""

        # Find bill number and link
        bill_link = item.find('a', href=lambda h: h and '/bill/' in h)
        if not bill_link:
            return None

        bill_number = bill_link.get_text(strip=True)
        bill_url = bill_link['href']
        if bill_url.startswith('/'):
            bill_url = self.base_url + bill_url

        # Find bill title
        title_elem = item.find('span', class_='result-title')
        if not title_elem:
            # Try to get from parent text
            title = item.get_text(strip=True)
        else:
            title = title_elem.get_text(strip=True)

        # Find vote information (Yes/No/Present/Not Voting)
        vote_elem = item.find('span', class_='vote')
        vote_cast = vote_elem.get_text(strip=True) if vote_elem else "Unknown"

        # Find date
        date_elem = item.find('span', class_='date') or item.find('time')
        vote_date = None
        if date_elem:
            vote_date = date_elem.get('datetime') or date_elem.get_text(strip=True)

        # Get bill details
        bill_summary = self._get_bill_summary(bill_url)

        # Generate unique ID
        vote_id = hashlib.md5(f"{bill_number}{vote_date}".encode()).hexdigest()[:12]

        vote_record = {
            'id': vote_id,
            'bill': bill_number,
            'bill_title': title,
            'bill_url': bill_url,
            'bill_summary': bill_summary,
            'vote_cast': vote_cast,
            'date': vote_date or datetime.now().isoformat(),
            'congress': congress,
            'source': 'congress_gov',
            'source_type': 'vote_record',
            'collected_date': datetime.now().isoformat(),
            'member_id': self.member_id
        }

        return vote_record

    def _get_bill_summary(self, bill_url):
        """Fetch bill summary from bill page"""

        try:
            response = requests.get(bill_url, timeout=30)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find bill summary
            summary = soup.find('div', class_='overview') or soup.find('div', id='bill-summary')

            if summary:
                # Clean up
                for script in summary(['script', 'style']):
                    script.decompose()

                return summary.get_text(separator=' ', strip=True)[:500]  # Limit length

            return ""

        except Exception as e:
            print(f"Could not fetch bill summary: {e}")
            return ""

    def save_votes(self, votes):
        """Save votes to JSON files"""

        saved_count = 0
        skipped_count = 0

        for vote in votes:
            filename = f"vote-{vote['id']}.json"
            filepath = self.storage_dir / filename

            if filepath.exists():
                skipped_count += 1
                continue

            try:
                with open(filepath, 'w') as f:
                    json.dump(vote, f, indent=2)

                print(f"✓ Saved: {vote['bill']} - {vote['vote_cast']}")
                saved_count += 1

            except Exception as e:
                print(f"Error saving {filename}: {e}")

        print(f"\nSummary: {saved_count} saved, {skipped_count} skipped")
        return saved_count


def main():
    """Run scraper as standalone script"""

    scraper = CongressGovScraper()

    print("=" * 80)
    print("Congress.gov Vote Scraper - Rep. Langworthy")
    print("=" * 80)
    print()

    votes = scraper.get_recent_votes(congress=118)

    if votes:
        saved = scraper.save_votes(votes)
        print(f"\n✓ Scraped {len(votes)} votes, saved {saved} new ones")
    else:
        print("\n⚠ No votes found")


if __name__ == "__main__":
    main()
