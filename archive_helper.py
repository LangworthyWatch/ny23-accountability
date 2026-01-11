#!/usr/bin/env python3
"""
Interactive Archive.org Helper for Fact-Checks
Helps systematically create archives and update markdown files
"""

import re
import json
from pathlib import Path
from typing import List, Dict

class ArchiveWorkflow:
    def __init__(self, content_root="Fact Checks"):
        self.content_root = Path(content_root)
        self.pending_citations = []

    def extract_pending_citations(self):
        """Extract all citations marked as [pending]"""
        for fc_file in self.content_root.glob("factcheck_*.md"):
            content = fc_file.read_text(encoding='utf-8')
            lines = content.split('\n')

            for i, line in enumerate(lines):
                if '[pending]' in line and 'Archive:' in line:
                    # Get context: citation text (line before)
                    citation_line = lines[i-1] if i > 0 else ""

                    # Extract citation details
                    citation = {
                        'file': fc_file.name,
                        'line_num': i + 1,
                        'citation': citation_line.strip(),
                        'archive_line': line.strip(),
                        'search_query': self.create_search_query(citation_line)
                    }
                    self.pending_citations.append(citation)

        return self.pending_citations

    def create_search_query(self, citation):
        """Generate a Google search query from the citation"""
        # Remove leading dashes and whitespace
        text = citation.strip('- ').strip()

        # Extract organization/source and title
        if ':' in text:
            source, title = text.split(':', 1)
            source = source.strip()
            title = title.strip()

            # Remove date info in parentheses for search
            title_clean = re.sub(r'\([^)]+\)', '', title).strip()

            # Create search query
            return f'site:{self.guess_domain(source)} {title_clean}'

        return text

    def guess_domain(self, source):
        """Guess the domain from the source name"""
        domain_map = {
            'Langworthy.house.gov': 'langworthy.house.gov',
            'CBO': 'cbo.gov',
            'Center on Budget': 'cbpp.org',
            'Urban Institute': 'urban.org',
            'FactCheck.org': 'factcheck.org',
            'National Immigration Law Center': 'nilc.org',
            'American Farm Bureau': 'fb.org',
            'National Milk Producers': 'nmpf.org',
            'NY Farm Bureau': 'nyfb.org',
            'American Immigration Council': 'americanimmigrationcouncil.org',
            'WGRZ': 'wgrz.com',
            'FeedMore WNY': 'feedmorewny.org',
            'FingerLakes1': 'fingerlakes1.com',
            'Civil Eats': 'civileats.com',
            'Observer Today': 'observertoday.com',
            'Post-Journal': 'post-journal.com',
            'Towerpoint Wealth': 'towerpointwealth.com',
            'Newsweek': 'newsweek.com',
            'U.S. Economic Development Administration': 'eda.gov',
            'Wellsville Sun': 'wellsvillesun.com'
        }

        for key, domain in domain_map.items():
            if key.lower() in source.lower():
                return domain

        return 'google.com'  # Fallback

    def print_summary(self):
        """Print organized summary by file"""
        print("\n" + "=" * 80)
        print("PENDING ARCHIVE.ORG BACKUPS - ORGANIZED BY FILE")
        print("=" * 80)
        print(f"\nTotal: {len(self.pending_citations)} citations\n")

        # Group by file
        by_file = {}
        for citation in self.pending_citations:
            file = citation['file']
            if file not in by_file:
                by_file[file] = []
            by_file[file].append(citation)

        # Sort by number of pending (most first)
        sorted_files = sorted(by_file.items(), key=lambda x: -len(x[1]))

        for file, citations in sorted_files:
            print(f"\n{'─' * 80}")
            print(f"📄 {file} ({len(citations)} pending)")
            print(f"{'─' * 80}")

            for i, cit in enumerate(citations, 1):
                print(f"\n{i}. {cit['citation']}")
                print(f"   Search: {cit['search_query']}")
                print(f"   File: {file}:{cit['line_num']}")

    def create_interactive_workflow(self):
        """Create an interactive workflow file"""
        workflow = []

        for citation in self.pending_citations:
            workflow.append({
                'citation': citation['citation'],
                'file': citation['file'],
                'line': citation['line_num'],
                'search_query': citation['search_query'],
                'archive_url': '',  # To be filled in
                'status': 'pending'
            })

        # Save as JSON for easy updating
        workflow_file = Path('archive_workflow.json')
        with open(workflow_file, 'w') as f:
            json.dump(workflow, f, indent=2)

        print(f"\n✓ Created {workflow_file}")
        print(f"  This file tracks your progress as you create archives")

        return workflow_file

    def update_markdown_files(self, workflow_file='archive_workflow.json'):
        """Update markdown files with completed archives from workflow"""
        # Load workflow
        with open(workflow_file) as f:
            workflow = json.load(f)

        # Group by file
        updates_by_file = {}
        for item in workflow:
            if item['status'] == 'completed' and item['archive_url']:
                file = item['file']
                if file not in updates_by_file:
                    updates_by_file[file] = []
                updates_by_file[file].append(item)

        # Update each file
        updated_count = 0
        for file, updates in updates_by_file.items():
            file_path = self.content_root / file
            content = file_path.read_text(encoding='utf-8')

            for update in updates:
                # Find and replace [pending] with actual URL
                old_pattern = f"- Archive: https://archive.is/[pending]"
                new_text = f"- Archive: {update['archive_url']}"

                if old_pattern in content:
                    content = content.replace(old_pattern, new_text, 1)
                    updated_count += 1
                    print(f"✓ Updated {file}: {update['citation'][:60]}...")

            # Write back
            file_path.write_text(content, encoding='utf-8')

        print(f"\n✓ Updated {updated_count} archives across {len(updates_by_file)} files")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Interactive Archive.org workflow helper"
    )
    parser.add_argument(
        '--extract',
        action='store_true',
        help='Extract all pending citations'
    )
    parser.add_argument(
        '--create-workflow',
        action='store_true',
        help='Create interactive workflow JSON file'
    )
    parser.add_argument(
        '--update',
        action='store_true',
        help='Update markdown files from completed workflow'
    )
    parser.add_argument(
        '--workflow-file',
        default='archive_workflow.json',
        help='Path to workflow JSON file'
    )

    args = parser.parse_args()

    workflow = ArchiveWorkflow()
    workflow.extract_pending_citations()

    if args.extract or not any([args.create_workflow, args.update]):
        workflow.print_summary()

    if args.create_workflow:
        workflow.create_interactive_workflow()
        print("\n" + "=" * 80)
        print("NEXT STEPS:")
        print("=" * 80)
        print("\n1. For each citation in archive_workflow.json:")
        print("   - Google the search query")
        print("   - Find the original URL")
        print("   - Archive at https://web.archive.org/save/")
        print("   - Copy archive URL")
        print("   - Add to 'archive_url' field in JSON")
        print("   - Change 'status' to 'completed'")
        print("\n2. When done, run:")
        print("   python3 archive_helper.py --update")
        print("\n3. This will update all markdown files automatically")

    if args.update:
        workflow.update_markdown_files(args.workflow_file)


if __name__ == "__main__":
    main()
