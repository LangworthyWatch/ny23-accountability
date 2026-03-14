"""
Review Queue - Interface for verifying collected statements

This tool helps you review scraped statements and decide what to publish
"""

import json
import os
from pathlib import Path
from datetime import datetime


class ReviewQueue:
    def __init__(self, pending_dir="storage/raw_statements", verified_dir="storage/verified"):
        self.pending_dir = Path(pending_dir)
        self.verified_dir = Path(verified_dir)
        self.verified_dir.mkdir(parents=True, exist_ok=True)

    def list_pending(self, source_filter=None):
        """
        List all statements awaiting review

        Args:
            source_filter: Optional filter by source (e.g., 'congressional_website', 'congress_gov')

        Returns:
            list: Pending statements
        """

        pending = []

        if not self.pending_dir.exists():
            print(f"No pending directory found at {self.pending_dir}")
            return pending

        for filename in sorted(self.pending_dir.glob('*.json')):
            try:
                with open(filename) as f:
                    data = json.load(f)

                    # Apply source filter if specified
                    if source_filter and data.get('source') != source_filter:
                        continue

                    data['_filename'] = filename.name
                    pending.append(data)

            except json.JSONDecodeError:
                print(f"⚠ Could not parse {filename}")
            except Exception as e:
                print(f"⚠ Error reading {filename}: {e}")

        return pending

    def display_for_review(self, statement):
        """Pretty print statement for review"""

        print("\n" + "=" * 80)
        print("STATEMENT FOR REVIEW")
        print("=" * 80)

        print(f"\nID: {statement.get('id', 'N/A')}")
        print(f"Source: {statement.get('source', 'N/A')}")
        print(f"Type: {statement.get('source_type', 'N/A')}")
        print(f"Date: {statement.get('date', 'N/A')}")
        print(f"Collected: {statement.get('collected_date', 'N/A')[:10]}")

        if statement.get('url'):
            print(f"URL: {statement['url']}")

        if statement.get('archived_url'):
            print(f"Archived: {statement['archived_url']}")

        print("\n" + "-" * 80)

        if statement.get('title'):
            print(f"\nTitle: {statement['title']}")

        if statement.get('bill'):
            print(f"\nBill: {statement['bill']}")
            print(f"Vote: {statement.get('vote_cast', 'N/A')}")
            if statement.get('bill_title'):
                print(f"Bill Title: {statement['bill_title']}")

        print("\nContent:")
        content = statement.get('full_text') or statement.get('snippet') or statement.get('text', 'N/A')

        # Truncate if very long
        if len(content) > 1000:
            print(content[:1000] + "...\n[truncated]")
        else:
            print(content)

        if statement.get('flags'):
            print(f"\n🚩 Flags: {', '.join(statement['flags'])}")

        print("=" * 80)

    def review_statement(self, statement):
        """Interactive review of a statement"""

        self.display_for_review(statement)

        print("\nVerification Checklist:")
        print("  [ ] Original source verified")
        print("  [ ] Archived at Archive.org")
        print("  [ ] Context confirmed")
        print("  [ ] Relevant to accountability tracking")
        print("  [ ] Ready to cross-reference with votes/actions")

        print("\nActions:")
        print("  [p] - Mark for publishing (move to verified)")
        print("  [d] - Discard (not useful)")
        print("  [l] - Review later (keep in queue)")
        print("  [v] - View full content again")
        print("  [q] - Quit review session")

        while True:
            action = input("\nAction: ").strip().lower()

            if action == 'p':
                return self._mark_for_publishing(statement)
            elif action == 'd':
                return self._discard(statement)
            elif action == 'l':
                print("✓ Keeping in queue for later")
                return 'later'
            elif action == 'v':
                self.display_for_review(statement)
            elif action == 'q':
                return 'quit'
            else:
                print("Invalid action. Use: p (publish), d (discard), l (later), v (view), q (quit)")

    def _mark_for_publishing(self, statement):
        """Move statement to verified folder"""

        filename = statement.get('_filename', f"{statement['id']}.json")
        source_path = self.pending_dir / filename
        dest_path = self.verified_dir / filename

        try:
            # Update verification status
            statement['verification_status'] = 'verified'
            statement['verified_date'] = datetime.now().isoformat()

            # Remove internal fields
            statement.pop('_filename', None)

            # Save to verified folder
            with open(dest_path, 'w') as f:
                json.dump(statement, f, indent=2)

            # Remove from pending
            if source_path.exists():
                source_path.unlink()

            print(f"✓ Moved to verified: {dest_path}")
            return 'published'

        except Exception as e:
            print(f"✗ Error moving to verified: {e}")
            return 'error'

    def _discard(self, statement):
        """Remove statement from queue"""

        filename = statement.get('_filename', f"{statement['id']}.json")
        source_path = self.pending_dir / filename

        confirm = input("Are you sure you want to discard this? (yes/no): ").strip().lower()

        if confirm == 'yes':
            try:
                if source_path.exists():
                    source_path.unlink()
                print("✓ Discarded")
                return 'discarded'
            except Exception as e:
                print(f"✗ Error discarding: {e}")
                return 'error'
        else:
            print("Cancelled")
            return 'later'

    def start_review_session(self, source_filter=None):
        """Start interactive review session"""

        pending = self.list_pending(source_filter=source_filter)

        if not pending:
            print("\n✓ No pending statements to review!")
            return

        print(f"\n{len(pending)} statement(s) pending review")
        print()

        reviewed = 0
        published = 0
        discarded = 0

        for statement in pending:
            result = self.review_statement(statement)

            reviewed += 1

            if result == 'published':
                published += 1
            elif result == 'discarded':
                discarded += 1
            elif result == 'quit':
                print(f"\nReview session ended. Reviewed: {reviewed}, Published: {published}, Discarded: {discarded}")
                return

        print(f"\n✓ All statements reviewed!")
        print(f"  Published: {published}")
        print(f"  Discarded: {discarded}")
        print(f"  Remaining: {len(pending) - published - discarded}")


def main():
    """Run review queue interface"""

    queue = ReviewQueue()

    print("=" * 80)
    print("Langworthy Tracker - Review Queue")
    print("=" * 80)
    print()

    # Check for pending items
    pending = queue.list_pending()

    if not pending:
        print("No statements in review queue.")
        print("\nRun a scraper first:")
        print("  python scrapers/congressional_site.py")
        print("  python scrapers/congress_gov.py")
        return

    print(f"Found {len(pending)} statement(s) to review\n")

    # Start review session
    queue.start_review_session()


if __name__ == "__main__":
    main()
