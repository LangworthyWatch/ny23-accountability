#!/usr/bin/env python3
"""
Fetch and extract Langworthy's data from congress-legislators repo.

This script downloads the YAML files from unitedstates/congress-legislators
and extracts relevant information about Rep. Nicholas Langworthy.

Usage:
    python3 scripts/fetch_legislator_data.py

Outputs:
    data/langworthy_profile.json - Biographical and term data
    data/langworthy_committees.json - Committee assignments with dates
"""

import json
import yaml
import requests
from pathlib import Path
from datetime import datetime

# Langworthy's Bioguide ID (permanent identifier)
LANGWORTHY_BIOGUIDE = "L000600"

# GitHub raw content URLs for the congress-legislators repo
BASE_URL = "https://raw.githubusercontent.com/unitedstates/congress-legislators/main"

FILES = {
    "legislators": f"{BASE_URL}/legislators-current.yaml",
    "committees": f"{BASE_URL}/committee-membership-current.yaml",
    "committee_info": f"{BASE_URL}/committees-current.yaml",
    "social": f"{BASE_URL}/legislators-social-media.yaml"
}

def fetch_yaml(url):
    """Download and parse YAML file from URL"""
    print(f"Fetching {url}...")
    response = requests.get(url)
    response.raise_for_status()
    return yaml.safe_load(response.text)

def find_legislator(legislators_data, bioguide_id):
    """Find a specific legislator by Bioguide ID"""
    for legislator in legislators_data:
        if legislator.get("id", {}).get("bioguide") == bioguide_id:
            return legislator
    return None

def extract_committee_assignments(committees_data, bioguide_id):
    """Extract all committee assignments for a legislator"""
    assignments = []

    for committee_id, members in committees_data.items():
        for member in members:
            if member.get("bioguide") == bioguide_id:
                assignments.append({
                    "committee_id": committee_id,
                    "name": member.get("name"),
                    "party": member.get("party"),
                    "rank": member.get("rank"),
                    "title": member.get("title"),
                })

    return assignments

def enrich_with_committee_names(assignments, committee_info):
    """Add full committee names and metadata"""
    # Build lookup dict
    committee_lookup = {}

    for committee in committee_info:
        thomas_id = committee.get("thomas_id")
        if thomas_id:
            committee_lookup[thomas_id] = {
                "name": committee.get("name"),
                "type": committee.get("type"),
                "url": committee.get("url"),
                "jurisdiction": committee.get("jurisdiction")
            }

            # Add subcommittees
            for subcom in committee.get("subcommittees", []):
                subcom_id = thomas_id + subcom.get("thomas_id", "")
                committee_lookup[subcom_id] = {
                    "name": f"{committee.get('name')} - Subcommittee on {subcom.get('name')}",
                    "type": committee.get("type"),
                    "parent": thomas_id,
                    "parent_name": committee.get("name")
                }

    # Enrich assignments
    for assignment in assignments:
        committee_id = assignment["committee_id"]
        if committee_id in committee_lookup:
            assignment.update(committee_lookup[committee_id])

    return assignments

def extract_social_media(social_data, bioguide_id):
    """Extract social media accounts for a legislator"""
    for entry in social_data:
        if entry.get("id", {}).get("bioguide") == bioguide_id:
            return entry.get("social", {})
    return {}

def format_profile(legislator, committees, social):
    """Format complete profile for output"""
    return {
        "id": legislator.get("id"),
        "name": legislator.get("name"),
        "bio": legislator.get("bio"),
        "terms": legislator.get("terms"),
        "social_media": social,
        "committees": committees,
        "metadata": {
            "fetched_at": datetime.utcnow().isoformat(),
            "source": "github.com/unitedstates/congress-legislators",
            "license": "CC0 1.0 Universal (Public Domain)"
        }
    }

def get_current_term(legislator):
    """Extract current term information"""
    terms = legislator.get("terms", [])
    if not terms:
        return None

    # Last term is current
    current = terms[-1].copy()

    # Check if actually current
    end_date = current.get("end")
    if end_date:
        end = datetime.strptime(end_date, "%Y-%m-%d")
        if end < datetime.now():
            return None

    return current

def main():
    print("="*60)
    print("Fetching Langworthy's data from congress-legislators")
    print("="*60)

    # Create data directory if needed
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    try:
        # Fetch all data files
        legislators = fetch_yaml(FILES["legislators"])
        committees = fetch_yaml(FILES["committees"])
        committee_info = fetch_yaml(FILES["committee_info"])
        social = fetch_yaml(FILES["social"])

        # Find Langworthy
        print(f"\nLooking for Bioguide ID: {LANGWORTHY_BIOGUIDE}")
        langworthy = find_legislator(legislators, LANGWORTHY_BIOGUIDE)

        if not langworthy:
            print(f"ERROR: Could not find legislator with Bioguide ID {LANGWORTHY_BIOGUIDE}")
            return 1

        print(f"Found: {langworthy['name']['official_full']}")

        # Extract data
        committee_assignments = extract_committee_assignments(committees, LANGWORTHY_BIOGUIDE)
        committee_assignments = enrich_with_committee_names(committee_assignments, committee_info)
        social_media = extract_social_media(social, LANGWORTHY_BIOGUIDE)

        # Format output
        profile = format_profile(langworthy, committee_assignments, social_media)

        # Save profile
        profile_file = data_dir / "langworthy_profile.json"
        with open(profile_file, "w") as f:
            json.dump(profile, f, indent=2)
        print(f"\n✓ Saved profile to {profile_file}")

        # Save simplified committee data
        committees_file = data_dir / "langworthy_committees.json"
        with open(committees_file, "w") as f:
            json.dump({
                "member": {
                    "bioguide": LANGWORTHY_BIOGUIDE,
                    "name": langworthy["name"]["official_full"]
                },
                "committees": committee_assignments,
                "count": len(committee_assignments),
                "updated": datetime.utcnow().isoformat()
            }, f, indent=2)
        print(f"✓ Saved committees to {committees_file}")

        # Print summary
        print("\n" + "="*60)
        print("SUMMARY")
        print("="*60)

        current_term = get_current_term(langworthy)
        if current_term:
            print(f"\nCurrent Term:")
            print(f"  Position: {current_term['type'].upper()}")
            print(f"  State: {current_term['state']}")
            print(f"  District: {current_term.get('district', 'N/A')}")
            print(f"  Party: {current_term['party']}")
            print(f"  Term: {current_term['start']} to {current_term['end']}")

        print(f"\nCommittee Assignments ({len(committee_assignments)}):")
        for c in committee_assignments:
            title = f" ({c['title']})" if c.get('title') else ""
            print(f"  • {c.get('name', c['committee_id'])}{title}")

        if social_media:
            print(f"\nSocial Media:")
            for platform, handle in social_media.items():
                print(f"  • {platform.title()}: {handle}")

        print("\n" + "="*60)
        print("✓ Done!")
        print("="*60)

        return 0

    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
