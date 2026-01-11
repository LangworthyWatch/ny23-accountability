"""
Vote Analysis Tool - Find contradictions between statements and votes
"""

import csv
import json
from pathlib import Path
from datetime import datetime
import re


class VoteAnalyzer:
    def __init__(self, votes_csv="data/langworthy_votes.csv"):
        self.votes_csv = Path(votes_csv)
        self.votes = []
        self.load_votes()

    def load_votes(self):
        """Load and parse votes from CSV"""
        print(f"Loading votes from {self.votes_csv}...")

        with open(self.votes_csv, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()

            # Find the header row (contains "Legislation Number")
            header_index = None
            for i, line in enumerate(lines):
                if 'Legislation Number' in line:
                    header_index = i
                    break

            if header_index is None:
                print("ERROR: Could not find header row")
                return

            # Parse CSV starting from header
            csv_data = ''.join(lines[header_index:])
            reader = csv.DictReader(csv_data.splitlines())

            for row in reader:
                # Only keep rows that have actual vote data
                if row.get('Roll Call Vote Number') and row.get('Member Vote'):
                    vote = {
                        'roll_call': row['Roll Call Vote Number'],
                        'date': row['Date Voted'],
                        'description': row['Description'],
                        'result': row['Roll Call Result'],
                        'vote': row['Member Vote'],
                        'url': row['URL'],
                        'bill': row.get('Legislation Number', ''),
                        'title': row.get('Title', '')
                    }
                    self.votes.append(vote)

        print(f"✓ Loaded {len(self.votes)} votes")

    def search_votes(self, keywords, vote_type=None):
        """
        Search for votes containing keywords

        Args:
            keywords: List of keywords to search for (case-insensitive)
            vote_type: Filter by vote ('Yea', 'Nay', 'Not Voting', 'Present')

        Returns:
            List of matching votes
        """
        matches = []
        keywords_lower = [k.lower() for k in keywords]

        for vote in self.votes:
            # Search in description, title, and bill number
            searchable = f"{vote['description']} {vote['title']} {vote['bill']}".lower()

            # Check if any keyword matches
            if any(keyword in searchable for keyword in keywords_lower):
                # Filter by vote type if specified
                if vote_type is None or vote['vote'] == vote_type:
                    matches.append(vote)

        return matches

    def votes_by_topic(self):
        """Categorize votes by topic"""
        topics = {
            'Healthcare': ['health', 'aca', 'affordable care', 'medicaid', 'medicare', 'hospital', 'medical'],
            'Immigration': ['immigration', 'border', 'asylum', 'deportation', 'sanctuary'],
            'Tax': ['tax', 'revenue', 'irs', 'salt', 'deduction'],
            'Veterans': ['veteran', 'va', 'military', 'defense', 'armed forces'],
            'Energy': ['energy', 'oil', 'gas', 'renewable', 'climate', 'epa'],
            'Budget': ['budget', 'appropriations', 'spending', 'shutdown', 'continuing resolution'],
            'Agriculture': ['farm', 'agriculture', 'rural', 'usda', 'crop'],
            'Education': ['education', 'school', 'student', 'college', 'university'],
        }

        categorized = {}

        for topic, keywords in topics.items():
            matches = self.search_votes(keywords)
            if matches:
                categorized[topic] = matches

        return categorized

    def export_for_site(self, output_dir="../langworthy-tracker/data"):
        """Export votes as JSON for the Hugo site"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Export all votes
        all_votes_file = output_path / "votes.json"
        with open(all_votes_file, 'w') as f:
            json.dump(self.votes, f, indent=2)

        print(f"✓ Exported all votes to {all_votes_file}")

        # Export by topic
        topics = self.votes_by_topic()
        topics_file = output_path / "votes_by_topic.json"

        # Convert to serializable format
        topics_serializable = {}
        for topic, votes in topics.items():
            topics_serializable[topic] = {
                'count': len(votes),
                'votes': votes
            }

        with open(topics_file, 'w') as f:
            json.dump(topics_serializable, f, indent=2)

        print(f"✓ Exported votes by topic to {topics_file}")
        print(f"\nVotes by topic:")
        for topic, data in topics_serializable.items():
            print(f"  {topic}: {data['count']} votes")

    def print_vote(self, vote):
        """Pretty print a vote"""
        print(f"\n{'='*80}")
        print(f"Roll Call: {vote['roll_call']} | Date: {vote['date']}")
        print(f"Bill: {vote['bill']}")
        print(f"Vote: {vote['vote']}")
        print(f"Result: {vote['result']}")
        print(f"Description: {vote['description']}")
        print(f"URL: {vote['url']}")


def main():
    analyzer = VoteAnalyzer()

    print("\n" + "="*80)
    print("VOTE ANALYSIS TOOL")
    print("="*80)

    # Example: Find healthcare votes
    print("\n\nSearching for HEALTHCARE votes...")
    healthcare_votes = analyzer.search_votes(['health', 'aca', 'medicaid'])
    print(f"Found {len(healthcare_votes)} healthcare-related votes")

    if healthcare_votes:
        print("\nFirst 3 healthcare votes:")
        for vote in healthcare_votes[:3]:
            analyzer.print_vote(vote)

    # Export data for website
    print("\n\n" + "="*80)
    print("EXPORTING DATA FOR WEBSITE")
    print("="*80)
    analyzer.export_for_site()

    print("\n✓ Analysis complete!")
    print("\nYou can now:")
    print("1. Search for specific topics: analyzer.search_votes(['keyword'])")
    print("2. Filter by vote type: analyzer.search_votes(['keyword'], vote_type='Nay')")
    print("3. See votes by topic: analyzer.votes_by_topic()")


if __name__ == "__main__":
    main()
