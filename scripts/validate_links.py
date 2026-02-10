#!/usr/bin/env python3
"""
Internal Link Validator for Langworthywatch Hugo Site
Checks all markdown files for broken internal links and suggests improvements
"""

import re
from pathlib import Path
from collections import defaultdict

# Base directory
BASE_DIR = Path(__file__).parent
CONTENT_DIR = BASE_DIR / 'content'

def extract_links(content):
    """Extract all markdown links from content"""
    # Pattern for [text](url)
    pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    return re.findall(pattern, content)

def is_internal_link(url):
    """Check if a link is internal (relative path)"""
    return not url.startswith(('http://', 'https://', 'mailto:', '#'))

def normalize_path(link_url, current_file):
    """Normalize a link URL to absolute path"""
    if link_url.startswith('/'):
        # Absolute from content root
        return CONTENT_DIR / link_url.lstrip('/')
    else:
        # Relative to current file
        return (current_file.parent / link_url).resolve()

def check_link_exists(link_path):
    """Check if a link target exists"""
    # Check as-is
    if link_path.exists():
        return True

    # Check with .md extension
    if link_path.with_suffix('.md').exists():
        return True

    # Check as directory with _index.md
    if link_path.is_dir() and (link_path / '_index.md').exists():
        return True

    # Check parent directory with _index.md
    if (link_path.parent / '_index.md').exists():
        return True

    return False

def find_potential_links(content, all_files):
    """Find potential internal links based on keywords"""
    suggestions = []
    content_lower = content.lower()

    # Keywords to look for
    keywords = {
        'fact-check': '/fact-checks/',
        'voting record': '/votes/',
        'methodology': '/methodology/',
        'campaign finance': '/campaign-finance/',
        'missed vote': '/missed-votes/',
    }

    for keyword, link in keywords.items():
        if keyword in content_lower and link not in content:
            suggestions.append(f"Consider linking '{keyword}' to {link}")

    return suggestions

def main():
    print("=" * 80)
    print("LANGWORTHYWATCH INTERNAL LINK VALIDATOR")
    print("=" * 80)
    print()

    # Find all markdown files
    md_files = list(CONTENT_DIR.glob('**/*.md'))
    print(f"Found {len(md_files)} markdown files\n")

    broken_links = []
    all_links = []
    suggestions_by_file = defaultdict(list)

    # Check each file
    for md_file in md_files:
        rel_path = md_file.relative_to(CONTENT_DIR)
        content = md_file.read_text()

        # Extract links
        links = extract_links(content)

        for text, url in links:
            if is_internal_link(url):
                all_links.append((rel_path, text, url))

                # Normalize and check
                target = normalize_path(url, md_file)

                if not check_link_exists(target):
                    broken_links.append({
                        'file': str(rel_path),
                        'text': text,
                        'url': url,
                        'target': str(target)
                    })

        # Find suggestions
        suggestions = find_potential_links(content, md_files)
        if suggestions:
            suggestions_by_file[str(rel_path)] = suggestions

    # Report broken links
    if broken_links:
        print("❌ BROKEN INTERNAL LINKS FOUND:")
        print("-" * 80)
        for link in broken_links:
            print(f"\nFile: {link['file']}")
            print(f"  Text: '{link['text']}'")
            print(f"  URL: {link['url']}")
            print(f"  Target: {link['target']}")
    else:
        print("✓ No broken internal links found!")

    print("\n" + "=" * 80)
    print(f"SUMMARY")
    print("=" * 80)
    print(f"Total markdown files: {len(md_files)}")
    print(f"Total internal links: {len(all_links)}")
    print(f"Broken links: {len(broken_links)}")

    # Suggestions
    if suggestions_by_file:
        print("\n" + "=" * 80)
        print("SUGGESTED INTERNAL LINKS")
        print("=" * 80)
        for file_path, suggestions in suggestions_by_file.items():
            print(f"\n{file_path}:")
            for suggestion in suggestions:
                print(f"  • {suggestion}")

    # Save report
    report_file = BASE_DIR / 'link_validation_report.txt'
    with open(report_file, 'w') as f:
        f.write("LANGWORTHYWATCH INTERNAL LINK VALIDATION REPORT\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Generated: {Path(__file__).stat().st_mtime}\n\n")

        if broken_links:
            f.write("BROKEN LINKS:\n")
            f.write("-" * 80 + "\n")
            for link in broken_links:
                f.write(f"\nFile: {link['file']}\n")
                f.write(f"  Text: '{link['text']}'\n")
                f.write(f"  URL: {link['url']}\n")
                f.write(f"  Target: {link['target']}\n")

        f.write("\n" + "=" * 80 + "\n")
        f.write("SUMMARY\n")
        f.write("=" * 80 + "\n")
        f.write(f"Total files: {len(md_files)}\n")
        f.write(f"Total internal links: {len(all_links)}\n")
        f.write(f"Broken links: {len(broken_links)}\n")

        if suggestions_by_file:
            f.write("\n" + "=" * 80 + "\n")
            f.write("SUGGESTED INTERNAL LINKS\n")
            f.write("=" * 80 + "\n")
            for file_path, suggestions in suggestions_by_file.items():
                f.write(f"\n{file_path}:\n")
                for suggestion in suggestions:
                    f.write(f"  • {suggestion}\n")

    print(f"\n✓ Report saved to: {report_file}")
    print()

if __name__ == '__main__':
    main()
