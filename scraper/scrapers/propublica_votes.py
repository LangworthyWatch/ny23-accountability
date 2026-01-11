"""
ProPublica Congress API scraper for voting records
Free API with no bot detection issues!
Get your API key: https://www.propublica.org/datastore/api/propublica-congress-api
"""

import requests
from datetime import datetime
import json
from pathlib import Path


class ProPublicaVoteScraper:
    def __init__(self, api_key, storage_dir="../storage/raw_statements"):
        """
        Initialize ProPublica API scraper

        Args:
            api_key: Your ProPublica API key (get free at propublica.org/datastore/api)
        """
        self.api_key = api_key
        self.base_url = "https://api.propublica.org/congress/v1"
        self.member_id = "L000266"  # Langworthy's ProPublica ID
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)

        self.headers = {
            'X-API-Key': self.api_key
        }

    def get_member_votes(self, congress=118, chamber='house'):
        """
        Get voting record for Langworthy

        Args:
            congress: Congress number (118 = current, 2023-2024)
            chamber: 'house' or 'senate'
        """

        print(f"Fetching votes from ProPublica API for Congress {congress}...")

        # ProPublica endpoint for member votes
        url = f"{self.base_url}/members/{self.member_id}/votes.json"

        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            data = response.json()

            if data['status'] != 'OK':
                print(f"API returned status: {data['status']}")
                return []

            # Extract votes from response
            votes = []
            results = data.get('results', [])

            if not results:
                print("No vote data found")
                return []

            vote_data = results[0].get('votes', [])
            print(f"Found {len(vote_data)} votes")

            for vote in vote_data:
                parsed_vote = self._parse_vote(vote)
                if parsed_vote:
                    votes.append(parsed_vote)

            return votes

        except requests.RequestException as e:
            print(f"Error fetching votes from ProPublica: {e}")
            return []
        except (KeyError, IndexError) as e:
            print(f"Error parsing ProPublica response: {e}")
            return []

    def _parse_vote(self, vote):
        """Parse individual vote from ProPublica API"""

        try:
            vote_record = {
                'id': vote.get('roll_call', ''),
                'bill': vote.get('bill', {}).get('number', 'N/A'),
                'bill_title': vote.get('description', ''),
                'vote_cast': vote.get('position', ''),
                'date': vote.get('date', ''),
                'question': vote.get('question', ''),
                'result': vote.get('result', ''),
                'chamber': vote.get('chamber', 'House'),
                'source': 'propublica_api',
                'source_type': 'vote_record',
                'collected_date': datetime.now().isoformat(),
                'member_id': self.member_id,
                'vote_uri': vote.get('vote_uri', ''),
                'bill_uri': vote.get('bill', {}).get('bill_uri', '')
            }

            return vote_record

        except Exception as e:
            print(f"Error parsing vote: {e}")
            return None

    def save_votes(self, votes):
        """Save votes to JSON files"""

        saved_count = 0
        skipped_count = 0

        for vote in votes:
            # Create filename from vote ID and date
            filename = f"vote-propublica-{vote['date']}-{vote['id']}.json"
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

    def get_specific_vote(self, congress, chamber, session, roll_call):
        """
        Get details of a specific vote

        Args:
            congress: Congress number (e.g., 118)
            chamber: 'house' or 'senate'
            session: Session number (1 or 2)
            roll_call: Roll call number
        """

        url = f"{self.base_url}/{congress}/{chamber}/sessions/{session}/votes/{roll_call}.json"

        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            data = response.json()

            return data.get('results', {})

        except Exception as e:
            print(f"Error fetching specific vote: {e}")
            return None


def main():
    """Run scraper - requires API key"""

    import os

    # Get API key from environment variable or prompt
    api_key = os.environ.get('PROPUBLICA_API_KEY')

    if not api_key:
        print("=" * 80)
        print("PROPUBLICA CONGRESS API SCRAPER")
        print("=" * 80)
        print()
        print("You need a free API key from ProPublica.")
        print()
        print("Get one here:")
        print("https://www.propublica.org/datastore/api/propublica-congress-api")
        print()
        api_key = input("Enter your ProPublica API key: ").strip()

    if not api_key:
        print("No API key provided. Exiting.")
        return

    scraper = ProPublicaVoteScraper(api_key)

    print("\n" + "=" * 80)
    print("Fetching Langworthy's voting record...")
    print("=" * 80)
    print()

    votes = scraper.get_member_votes(congress=118)

    if votes:
        saved = scraper.save_votes(votes)
        print(f"\n✓ Scraped {len(votes)} votes, saved {saved} new ones")
    else:
        print("\n⚠ No votes found")


if __name__ == "__main__":
    main()
