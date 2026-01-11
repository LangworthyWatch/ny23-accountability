"""
GovTrack API scraper for voting records
Completely free, no API key needed!
https://www.govtrack.us/api/v2/
"""

import requests
from datetime import datetime
import json
from pathlib import Path


class GovTrackVoteScraper:
    def __init__(self, storage_dir="../storage/raw_statements"):
        self.base_url = "https://www.govtrack.us/api/v2"
        # Langworthy's GovTrack ID (found via govtrack.us website)
        self.person_id = 412879
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)

        # Headers to avoid blocking
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json'
        }

    def find_member(self, last_name="Langworthy", state="NY"):
        """Find member ID by name"""

        url = f"{self.base_url}/person"
        params = {
            'lastname': last_name,
            'current': 'true'  # Only current members
        }

        try:
            response = requests.get(url, params=params, headers=self.headers, timeout=30)
            response.raise_for_status()
            data = response.json()

            members = data.get('objects', [])

            for member in members:
                # Check if from NY and in House
                if member.get('state') == state and 'Representative' in member.get('name', ''):
                    print(f"Found: {member['name']} (ID: {member['id']})")
                    self.person_id = member['id']
                    return member['id']

            print(f"Could not find {last_name} from {state}")
            return None

        except Exception as e:
            print(f"Error finding member: {e}")
            return None

    def get_votes(self, limit=100):
        """Get voting record from GovTrack"""

        print(f"Fetching votes from GovTrack for person ID {self.person_id}...")

        # GovTrack votes endpoint
        url = f"{self.base_url}/vote_voter"

        params = {
            'person': self.person_id,
            'order_by': '-created',  # Most recent first
            'limit': limit
        }

        try:
            response = requests.get(url, params=params, headers=self.headers, timeout=30)
            response.raise_for_status()
            data = response.json()

            vote_voters = data.get('objects', [])
            print(f"Found {len(vote_voters)} votes")

            votes = []
            for vote_voter in vote_voters:
                parsed_vote = self._parse_vote(vote_voter)
                if parsed_vote:
                    votes.append(parsed_vote)

            return votes

        except requests.RequestException as e:
            print(f"Error fetching votes: {e}")
            return []

    def _parse_vote(self, vote_voter):
        """Parse individual vote"""

        try:
            # Get vote details
            vote_url = vote_voter.get('vote')
            if not vote_url:
                return None

            # Fetch full vote details
            vote_details = self._get_vote_details(vote_url)
            if not vote_details:
                return None

            # Extract vote information
            vote_record = {
                'id': vote_details.get('id', ''),
                'bill': self._get_bill_number(vote_details),
                'bill_title': vote_details.get('question', ''),
                'vote_cast': vote_voter.get('option', {}).get('value', ''),
                'date': vote_details.get('created', '').split('T')[0],  # Extract date only
                'result': vote_details.get('result', ''),
                'chamber': vote_details.get('chamber', ''),
                'question': vote_details.get('question', ''),
                'vote_type': vote_details.get('vote_type', ''),
                'source': 'govtrack_api',
                'source_type': 'vote_record',
                'collected_date': datetime.now().isoformat(),
                'govtrack_url': f"https://www.govtrack.us{vote_details.get('link', '')}",
                'bill_url': self._get_bill_url(vote_details)
            }

            return vote_record

        except Exception as e:
            print(f"Error parsing vote: {e}")
            return None

    def _get_vote_details(self, vote_url):
        """Get full details of a vote"""

        try:
            response = requests.get(vote_url, headers=self.headers, timeout=30)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching vote details: {e}")
            return None

    def _get_bill_number(self, vote_details):
        """Extract bill number from vote details"""

        related_bill = vote_details.get('related_bill')
        if related_bill:
            # Extract bill number from URL like /api/v2/bill/118/hr1234
            parts = related_bill.split('/')
            if len(parts) >= 6:
                congress = parts[-2]
                bill_type = parts[-1][:2].upper()
                bill_num = parts[-1][2:]
                return f"{bill_type} {bill_num}"

        return "N/A"

    def _get_bill_url(self, vote_details):
        """Get bill URL"""

        related_bill = vote_details.get('related_bill')
        if related_bill:
            parts = related_bill.split('/')
            if len(parts) >= 6:
                congress = parts[-2]
                bill_slug = parts[-1]
                return f"https://www.govtrack.us/congress/bills/{congress}/{bill_slug}"

        return ""

    def save_votes(self, votes):
        """Save votes to JSON files"""

        saved_count = 0
        skipped_count = 0

        for vote in votes:
            filename = f"vote-govtrack-{vote['date']}-{vote['id']}.json"
            filepath = self.storage_dir / filename

            if filepath.exists():
                skipped_count += 1
                continue

            try:
                with open(filepath, 'w') as f:
                    json.dump(vote, f, indent=2)

                print(f"✓ Saved: {vote['bill']} - {vote['vote_cast']} ({vote['date']})")
                saved_count += 1

            except Exception as e:
                print(f"Error saving {filename}: {e}")

        print(f"\nSummary: {saved_count} saved, {skipped_count} skipped")
        return saved_count


def main():
    """Run GovTrack scraper"""

    scraper = GovTrackVoteScraper()

    print("=" * 80)
    print("GOVTRACK VOTE SCRAPER - Rep. Langworthy")
    print("=" * 80)
    print()

    # Find Langworthy's ID
    member_id = scraper.find_member("Langworthy", "NY")

    if not member_id:
        print("Could not find member. Exiting.")
        return

    print()

    # Get votes
    votes = scraper.get_votes(limit=50)

    if votes:
        saved = scraper.save_votes(votes)
        print(f"\n✓ Scraped {len(votes)} votes, saved {saved} new ones")
    else:
        print("\n⚠ No votes found")


if __name__ == "__main__":
    main()
