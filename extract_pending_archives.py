#!/usr/bin/env python3
"""
Extract pending Archive.org URLs from fact-checks
Helps create archive backups efficiently
"""

import re
from pathlib import Path
import webbrowser
import time


class ArchiveHelper:
    def __init__(self, content_root="Fact Checks"):
        self.content_root = Path(content_root)
        self.pending_urls = []

    def extract_pending_archives(self):
        """Find all URLs marked as pending archives"""
        pattern = re.compile(r'-\s+(?:Archive|Original):\s+(https?://[^\s\)]+)\s+.*?\[pending\]', re.IGNORECASE)

        # Also find URLs that should have archives
        url_pattern = re.compile(r'(?:Original|Source|URL):\s+(https?://[^\s\)]+)')

        for fc_file in self.content_root.glob("factcheck_*.md"):
            content = fc_file.read_text(encoding='utf-8')

            # Find pending archives
            for match in pattern.finditer(content):
                url = match.group(1)
                self.pending_urls.append({
                    'file': fc_file.name,
                    'url': url,
                    'status': 'pending'
                })

        return self.pending_urls

    def print_urls(self):
        """Print all pending URLs"""
        print("\n" + "=" * 80)
        print("PENDING ARCHIVE.ORG BACKUPS")
        print("=" * 80)
        print(f"\nFound {len(self.pending_urls)} URLs needing archive backups:\n")

        # Group by file
        by_file = {}
        for item in self.pending_urls:
            file = item['file']
            if file not in by_file:
                by_file[file] = []
            by_file[file].append(item['url'])

        for file, urls in by_file.items():
            print(f"\n{file} ({len(urls)} URLs):")
            for url in urls:
                print(f"  {url}")

    def save_url_list(self, output_file="pending_archives.txt"):
        """Save URLs to text file for easy copying"""
        with open(output_file, 'w') as f:
            f.write("PENDING ARCHIVE.ORG BACKUPS\n")
            f.write("=" * 80 + "\n\n")
            f.write("Visit https://web.archive.org/save/ and archive each URL below:\n\n")

            by_file = {}
            for item in self.pending_urls:
                file = item['file']
                if file not in by_file:
                    by_file[file] = []
                by_file[file].append(item['url'])

            for file, urls in by_file.items():
                f.write(f"\n{file}:\n")
                for url in urls:
                    f.write(f"  {url}\n")

        print(f"\n✓ Saved to {output_file}")

    def open_archive_org(self, auto_open=False):
        """Open Archive.org save page"""
        if auto_open:
            print("\nOpening Archive.org in browser...")
            webbrowser.open("https://web.archive.org/save/")
            time.sleep(2)

            if self.pending_urls:
                print("\nWould you like to open each URL for archiving? (opens 27 tabs)")
                response = input("This will open all URLs. Continue? (yes/no): ")

                if response.lower() in ['yes', 'y']:
                    for i, item in enumerate(self.pending_urls, 1):
                        print(f"Opening {i}/{len(self.pending_urls)}: {item['url'][:60]}...")
                        webbrowser.open(f"https://web.archive.org/save/{item['url']}")
                        time.sleep(1)  # Rate limiting

    def create_batch_script(self):
        """Create a bash script to archive all URLs using curl"""
        script = """#!/bin/bash
# Batch archive URLs to Archive.org
# This script submits URLs to the Wayback Machine

echo "Archiving URLs to Archive.org..."
echo "This may take a few minutes..."
echo ""

"""
        for i, item in enumerate(self.pending_urls, 1):
            url = item['url']
            script += f"""
# {i}. {item['file']}
echo "Archiving {i}/{len(self.pending_urls)}: {url[:60]}..."
curl -s "https://web.archive.org/save/{url}" > /dev/null
sleep 2  # Rate limiting
"""

        script += """
echo ""
echo "Done! All URLs submitted to Archive.org."
echo "Note: It may take a few minutes for archives to process."
echo "Check back at https://web.archive.org/ to get archive URLs."
"""

        with open("archive_all_urls.sh", 'w') as f:
            f.write(script)

        import os
        os.chmod("archive_all_urls.sh", 0o755)

        print("\n✓ Created archive_all_urls.sh")
        print("  Run with: ./archive_all_urls.sh")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Extract and help archive pending URLs"
    )
    parser.add_argument(
        '--content-root',
        default='Fact Checks',
        help='Path to fact-check content directory'
    )
    parser.add_argument(
        '--save',
        action='store_true',
        help='Save URLs to pending_archives.txt'
    )
    parser.add_argument(
        '--create-script',
        action='store_true',
        help='Create bash script to archive all URLs'
    )
    parser.add_argument(
        '--open',
        action='store_true',
        help='Open Archive.org in browser (WARNING: opens many tabs)'
    )

    args = parser.parse_args()

    helper = ArchiveHelper(args.content_root)
    helper.extract_pending_archives()
    helper.print_urls()

    if args.save:
        helper.save_url_list()

    if args.create_script:
        helper.create_batch_script()

    if args.open:
        helper.open_archive_org(auto_open=True)

    if not (args.save or args.create_script or args.open):
        print("\n" + "=" * 80)
        print("Next Steps:")
        print("=" * 80)
        print("\nOption 1 - Manual (Recommended for verification):")
        print("  1. Visit https://web.archive.org/save/")
        print("  2. Paste each URL and click 'Save Page'")
        print("  3. Copy the archive URL (https://web.archive.org/web/TIMESTAMP/URL)")
        print("  4. Update fact-check files with actual archive URLs")
        print("\nOption 2 - Batch Script (Fast but less control):")
        print("  python3 extract_pending_archives.py --create-script")
        print("  ./archive_all_urls.sh")
        print("\nOption 3 - Save list for later:")
        print("  python3 extract_pending_archives.py --save")
        print("  # Then archive from pending_archives.txt")


if __name__ == "__main__":
    main()
