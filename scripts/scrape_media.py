#!/usr/bin/env python3
"""
Scrape and track media coverage of Rep. Langworthy.

This script helps maintain a database of news articles, op-eds, and media
coverage. It can be used manually or automated to track new coverage.

Usage:
    # Add a single article
    python3 scripts/scrape_media.py add --url "https://..." --title "Article Title"

    # List all media items
    python3 scripts/scrape_media.py list

    # Export to Hugo data format
    python3 scripts/scrape_media.py export

Manual workflow:
    1. Find article/op-ed
    2. Archive it on Archive.org
    3. Add to database with this script
    4. Rebuild Hugo site
"""

import json
import argparse
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse

# Media categories
CATEGORIES = {
    "op-ed": "Op-Ed & Commentary",
    "investigative": "Investigative Reporting",
    "local": "Local News Coverage",
    "national": "National News",
    "letter": "Letter to the Editor",
    "analysis": "Analysis & Fact-Check",
    "other": "Other Coverage"
}

def load_media_database():
    """Load existing media database"""
    db_file = Path("data/media_coverage.json")

    if db_file.exists():
        with open(db_file) as f:
            return json.load(f)

    return {
        "items": [],
        "last_updated": None
    }

def save_media_database(db):
    """Save media database"""
    db_file = Path("data/media_coverage.json")
    db["last_updated"] = datetime.now().isoformat()

    # Sort by date (newest first)
    db["items"].sort(key=lambda x: x["date"], reverse=True)

    with open(db_file, "w") as f:
        json.dump(db, f, indent=2)

    print(f"✓ Saved {len(db['items'])} media items to {db_file}")

def get_source_name(url):
    """Extract publication name from URL"""
    domain = urlparse(url).netloc

    # Common sources in NY-23
    sources = {
        "olean.com": "Olean Times Herald",
        "oleantimesherald.com": "Olean Times Herald",
        "observertoday.com": "Observer Today (Dunkirk)",
        "post-journal.com": "Post-Journal (Jamestown)",
        "eveningtribune.com": "Evening Tribune (Hornell)",
        "stargazette.com": "Star-Gazette (Elmira)",
        "pressconnects.com": "Press & Sun-Bulletin",
        "democratandchronicle.com": "Democrat & Chronicle (Rochester)",
        "buffalonews.com": "Buffalo News",
        "nytimes.com": "New York Times",
        "washingtonpost.com": "Washington Post",
        "politico.com": "Politico",
        "thehill.com": "The Hill",
        "huffpost.com": "HuffPost",
        "cnn.com": "CNN",
        "axios.com": "Axios",
        "propublica.org": "ProPublica"
    }

    for key, name in sources.items():
        if key in domain:
            return name

    # Default: clean up domain name
    return domain.replace("www.", "").replace(".com", "").title()

def add_media_item(args):
    """Add a new media item to the database"""
    db = load_media_database()

    # Create new item
    item = {
        "id": len(db["items"]) + 1,
        "title": args.title,
        "url": args.url,
        "archive_url": args.archive_url or "",
        "source": args.source or get_source_name(args.url),
        "author": args.author or "",
        "date": args.date or datetime.now().strftime("%Y-%m-%d"),
        "category": args.category,
        "excerpt": args.excerpt or "",
        "topics": args.topics.split(",") if args.topics else [],
        "added_at": datetime.now().isoformat()
    }

    db["items"].append(item)
    save_media_database(db)

    print("\n✓ Added media item:")
    print(f"  Title: {item['title']}")
    print(f"  Source: {item['source']}")
    print(f"  Category: {CATEGORIES[item['category']]}")

    if not item["archive_url"]:
        print(f"\n⚠ Remember to archive this URL:")
        print(f"  https://web.archive.org/save/{item['url']}")

def list_media_items(args):
    """List all media items"""
    db = load_media_database()

    print("\n" + "="*70)
    print(f"MEDIA COVERAGE DATABASE ({len(db['items'])} items)")
    print("="*70)

    # Group by category
    by_category = {}
    for item in db["items"]:
        category = item["category"]
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(item)

    for category, items in sorted(by_category.items()):
        print(f"\n{CATEGORIES[category]} ({len(items)} items):")
        print("-" * 70)

        for item in items[:5]:  # Show 5 most recent per category
            print(f"\n  [{item['date']}] {item['title']}")
            print(f"  Source: {item['source']}")
            if item['author']:
                print(f"  Author: {item['author']}")
            if item['topics']:
                print(f"  Topics: {', '.join(item['topics'])}")

def export_for_hugo(args):
    """Export media database for Hugo"""
    db = load_media_database()

    # Create Hugo-friendly export
    export = {
        "media_items": db["items"],
        "count": len(db["items"]),
        "by_category": {},
        "by_topic": {},
        "last_updated": db.get("last_updated")
    }

    # Group by category
    for item in db["items"]:
        category = item["category"]
        if category not in export["by_category"]:
            export["by_category"][category] = []
        export["by_category"][category].append(item)

    # Group by topic
    for item in db["items"]:
        for topic in item["topics"]:
            if topic not in export["by_topic"]:
                export["by_topic"][topic] = []
            export["by_topic"][topic].append(item)

    # Save
    export_file = Path("data/media_coverage_export.json")
    with open(export_file, "w") as f:
        json.dump(export, f, indent=2)

    print(f"✓ Exported {len(db['items'])} items to {export_file}")
    print(f"\nBreakdown by category:")
    for cat, items in export["by_category"].items():
        print(f"  {CATEGORIES[cat]}: {len(items)}")

def main():
    parser = argparse.ArgumentParser(description="Manage media coverage database")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a media item")
    add_parser.add_argument("--url", required=True, help="Article URL")
    add_parser.add_argument("--title", required=True, help="Article title")
    add_parser.add_argument("--source", help="Publication name (auto-detected if omitted)")
    add_parser.add_argument("--author", help="Author name")
    add_parser.add_argument("--date", help="Publication date (YYYY-MM-DD)")
    add_parser.add_argument("--category", choices=CATEGORIES.keys(), required=True,
                          help="Article category")
    add_parser.add_argument("--excerpt", help="Brief excerpt or summary")
    add_parser.add_argument("--topics", help="Comma-separated topics (e.g., 'healthcare,veterans')")
    add_parser.add_argument("--archive-url", help="Archive.org URL")

    # List command
    list_parser = subparsers.add_parser("list", help="List all media items")

    # Export command
    export_parser = subparsers.add_parser("export", help="Export for Hugo")

    args = parser.parse_args()

    if args.command == "add":
        add_media_item(args)
    elif args.command == "list":
        list_media_items(args)
    elif args.command == "export":
        export_for_hugo(args)
    else:
        parser.print_help()
        return 1

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
