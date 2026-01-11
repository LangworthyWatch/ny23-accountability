#!/usr/bin/env python3
"""
Batch Archive.org URL Submission and Retrieval
Automatically archives URLs and retrieves archive links
"""

import json
import time
import subprocess
import re
from pathlib import Path
from urllib.parse import quote

class BatchArchiver:
    def __init__(self, workflow_file='archive_workflow.json'):
        self.workflow_file = Path(workflow_file)
        self.workflow = []
        self.found_urls = {
            # factcheck_social_security_tax.md
            "Towerpoint Wealth: \"Is Social Security Tax-Free Under the New Big Beautiful Bill?\" (2025)":
                "https://towerpointwealth.com/is-social-security-tax-free/",
            "Newsweek: Analysis of Social Security tax provisions (2025)":
                "https://www.newsweek.com/no-tax-social-security-seniors-big-beautiful-bill-2115721",
            "Langworthy.house.gov: \"Congressman Nick Langworthy Visits Springville to Spotlight Local Seniors, Small Businesses\" (July 11, 2025)":
                "https://langworthy.house.gov/media/press-releases/congressman-nick-langworthy-visits-springville-spotlight-local-seniors-small",

            # factcheck_infrastructure_credit.md
            "Langworthy.house.gov: Finger Lakes Railway grant announcement (June 2025)":
                "https://langworthy.house.gov/media/press-releases/congressman-nick-langworthy-announces-over-38-million-fra-grant-finger-lakes",
            "Langworthy.house.gov: Watkins Glen water infrastructure announcement (June 2024)":
                "https://langworthy.house.gov/media/press-releases/congressman-nick-langworthy-announces-46-million-federal-funding-water",
            "U.S. Economic Development Administration: Watkins Glen grant press release (June 25, 2024)":
                "https://www.eda.gov/news/press-release/2024/06/25/us-department-commerce-invests-46-million-water-infrastructure",
            "FingerLakes1.com: \"Finger Lakes Railway awarded $3.8 million federal grant for track upgrades\" (June 11, 2025)":
                "https://www.fingerlakes1.com/2025/06/10/finger-lakes-railway-awarded-3-8-million-federal-grant-for-track-upgrades/",
        }

    def load_workflow(self):
        """Load the workflow JSON file"""
        if self.workflow_file.exists():
            with open(self.workflow_file) as f:
                self.workflow = json.load(f)
        return self.workflow

    def add_found_urls_to_workflow(self):
        """Match found URLs to workflow items"""
        self.load_workflow()

        matched = 0
        for item in self.workflow:
            citation = item['citation'].strip('- ')

            # Try exact match first
            if citation in self.found_urls:
                item['original_url'] = self.found_urls[citation]
                matched += 1
            else:
                # Try fuzzy match on key phrases
                for found_citation, url in self.found_urls.items():
                    if self._citations_match(citation, found_citation):
                        item['original_url'] = url
                        matched += 1
                        break

        # Save updated workflow
        with open(self.workflow_file, 'w') as f:
            json.dump(self.workflow, f, indent=2)

        print(f"\n✓ Matched {matched} URLs to workflow items")
        return matched

    def _citations_match(self, cit1, cit2):
        """Check if two citations are similar enough to match"""
        # Remove common words and compare
        def clean(s):
            s = s.lower()
            s = re.sub(r'[:\(\)\[\]\"\'"]', '', s)
            return set(s.split())

        words1 = clean(cit1)
        words2 = clean(cit2)

        # If 70% of words overlap, consider it a match
        overlap = len(words1 & words2)
        total = max(len(words1), len(words2))

        return overlap / total > 0.7 if total > 0 else False

    def submit_to_archive_org(self, url):
        """Submit URL to Archive.org using curl"""
        archive_save_url = f"https://web.archive.org/save/{url}"

        try:
            # Submit to Archive.org
            result = subprocess.run(
                ['curl', '-s', '-I', archive_save_url],
                capture_output=True,
                text=True,
                timeout=30
            )

            # Archive.org returns a job ID in the headers
            # We'll check for success by looking for a 200/302 response
            if '200 OK' in result.stdout or '302' in result.stdout:
                print(f"  ✓ Submitted to Archive.org")
                return True
            else:
                print(f"  ✗ Failed to submit (HTTP error)")
                return False

        except subprocess.TimeoutExpired:
            print(f"  ⏱  Timeout submitting to Archive.org")
            return False
        except Exception as e:
            print(f"  ✗ Error: {e}")
            return False

    def get_archive_url(self, url, max_retries=3, wait_seconds=5):
        """Get the Archive.org URL for a given original URL"""
        # Check if URL has been archived recently
        availability_url = f"http://archive.org/wayback/available?url={quote(url)}"

        for attempt in range(max_retries):
            try:
                result = subprocess.run(
                    ['curl', '-s', availability_url],
                    capture_output=True,
                    text=True,
                    timeout=15
                )

                data = json.loads(result.stdout)

                # Check if archived snapshot exists
                if 'archived_snapshots' in data and 'closest' in data['archived_snapshots']:
                    closest = data['archived_snapshots']['closest']
                    if closest.get('available'):
                        archive_url = closest.get('url', '')
                        if archive_url:
                            return archive_url

                # Wait and retry
                if attempt < max_retries - 1:
                    time.sleep(wait_seconds)

            except Exception as e:
                print(f"  ⚠  Error checking archive: {e}")
                if attempt < max_retries - 1:
                    time.sleep(wait_seconds)

        return None

    def archive_all_urls(self, submit_only=False):
        """Archive all URLs with original_url in workflow"""
        self.load_workflow()

        submitted = 0
        retrieved = 0
        failed = 0

        print("\n" + "=" * 80)
        print("BATCH ARCHIVING URLS")
        print("=" * 80 + "\n")

        for i, item in enumerate(self.workflow, 1):
            if 'original_url' not in item or not item['original_url']:
                continue

            url = item['original_url']
            citation = item['citation'][:70]

            print(f"\n[{i}/{len(self.workflow)}] {citation}...")
            print(f"  URL: {url}")

            # Submit to Archive.org
            if self.submit_to_archive_org(url):
                submitted += 1

                if not submit_only:
                    # Wait for Archive.org to process (they need ~10 seconds)
                    print(f"  ⏳ Waiting for Archive.org to process...")
                    time.sleep(12)

                    # Try to get archive URL
                    archive_url = self.get_archive_url(url)

                    if archive_url:
                        print(f"  ✓ Archive URL: {archive_url}")
                        item['archive_url'] = archive_url
                        item['status'] = 'completed'
                        retrieved += 1
                    else:
                        print(f"  ⏱  Archive URL not ready yet (try again later)")
                        item['status'] = 'submitted'
            else:
                failed += 1
                item['status'] = 'failed'

            # Save progress after each URL
            with open(self.workflow_file, 'w') as f:
                json.dump(self.workflow, f, indent=2)

        print("\n" + "=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print(f"\n✓ Submitted: {submitted}")
        if not submit_only:
            print(f"✓ Retrieved archive URLs: {retrieved}")
            print(f"⏱ Pending (submitted but URL not ready): {submitted - retrieved}")
        print(f"✗ Failed: {failed}")
        print(f"\n✓ Progress saved to {self.workflow_file}")

    def retry_pending(self):
        """Retry getting archive URLs for items marked as 'submitted'"""
        self.load_workflow()

        pending = [item for item in self.workflow if item.get('status') == 'submitted']

        if not pending:
            print("\n✓ No pending items to retry")
            return

        print(f"\n⟳ Retrying {len(pending)} pending URLs...\n")

        retrieved = 0
        for item in pending:
            url = item.get('original_url', '')
            if not url:
                continue

            print(f"Checking: {item['citation'][:70]}...")

            archive_url = self.get_archive_url(url, max_retries=1, wait_seconds=0)

            if archive_url:
                print(f"  ✓ Archive URL: {archive_url}")
                item['archive_url'] = archive_url
                item['status'] = 'completed'
                retrieved += 1
            else:
                print(f"  ⏱ Still pending...")

        # Save updates
        with open(self.workflow_file, 'w') as f:
            json.dump(self.workflow, f, indent=2)

        print(f"\n✓ Retrieved {retrieved} new archive URLs")

    def update_markdown_files(self):
        """Update markdown files with completed archive URLs"""
        from pathlib import Path

        self.load_workflow()

        completed = [item for item in self.workflow
                    if item.get('status') == 'completed' and item.get('archive_url')]

        if not completed:
            print("\n⚠ No completed items with archive URLs to update")
            return

        print(f"\n📝 Updating markdown files for {len(completed)} completed archives...\n")

        # Group by file
        by_file = {}
        for item in completed:
            file = item['file']
            if file not in by_file:
                by_file[file] = []
            by_file[file].append(item)

        content_root = Path('Fact Checks')
        updated_count = 0

        for file, items in by_file.items():
            file_path = content_root / file

            if not file_path.exists():
                print(f"⚠ File not found: {file}")
                continue

            content = file_path.read_text(encoding='utf-8')
            original_content = content

            for item in items:
                # Replace [pending] with actual archive URL
                # Find the line with [pending] near this citation
                old_pattern = "- Archive: https://archive.is/[pending]"
                new_text = f"- Archive: {item['archive_url']}"

                # Try replacing once
                if old_pattern in content:
                    content = content.replace(old_pattern, new_text, 1)
                    print(f"  ✓ {file}: {item['citation'][:60]}...")
                    updated_count += 1
                else:
                    # Try alternative pattern
                    old_pattern2 = "Archive: https://archive.is/[pending]"
                    if old_pattern2 in content:
                        content = content.replace(old_pattern2, f"Archive: {item['archive_url']}", 1)
                        print(f"  ✓ {file}: {item['citation'][:60]}...")
                        updated_count += 1
                    else:
                        print(f"  ⚠ Could not find [pending] for: {item['citation'][:60]}...")

            # Write back if changes were made
            if content != original_content:
                file_path.write_text(content, encoding='utf-8')

        print(f"\n✓ Updated {updated_count} archive URLs in markdown files")

    def print_status(self):
        """Print current workflow status"""
        self.load_workflow()

        total = len(self.workflow)
        with_urls = len([item for item in self.workflow if item.get('original_url')])
        completed = len([item for item in self.workflow if item.get('status') == 'completed'])
        submitted = len([item for item in self.workflow if item.get('status') == 'submitted'])
        pending = total - with_urls

        print("\n" + "=" * 80)
        print("WORKFLOW STATUS")
        print("=" * 80)
        print(f"\nTotal citations: {total}")
        print(f"URLs found: {with_urls} ({with_urls/total*100:.0f}%)")
        print(f"Completed (archived): {completed}")
        print(f"Submitted (pending): {submitted}")
        print(f"URLs still needed: {pending}")
        print(f"\n{'─' * 80}")

        if pending > 0:
            print("\nCitations still needing URLs:")
            for item in self.workflow:
                if not item.get('original_url'):
                    print(f"  • {item['citation']}")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Batch archive URLs to Archive.org"
    )
    parser.add_argument(
        '--add-urls',
        action='store_true',
        help='Add found URLs to workflow'
    )
    parser.add_argument(
        '--archive',
        action='store_true',
        help='Submit all URLs with original_url to Archive.org'
    )
    parser.add_argument(
        '--submit-only',
        action='store_true',
        help='Only submit URLs, don\'t wait for archive URLs'
    )
    parser.add_argument(
        '--retry',
        action='store_true',
        help='Retry getting archive URLs for submitted items'
    )
    parser.add_argument(
        '--update',
        action='store_true',
        help='Update markdown files with completed archives'
    )
    parser.add_argument(
        '--status',
        action='store_true',
        help='Show workflow status'
    )

    args = parser.parse_args()

    archiver = BatchArchiver()

    if args.add_urls:
        archiver.add_found_urls_to_workflow()

    if args.archive:
        archiver.archive_all_urls(submit_only=args.submit_only)

    if args.retry:
        archiver.retry_pending()

    if args.update:
        archiver.update_markdown_files()

    if args.status or not any([args.add_urls, args.archive, args.retry, args.update]):
        archiver.print_status()


if __name__ == "__main__":
    main()
