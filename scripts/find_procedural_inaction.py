#!/usr/bin/env python3
"""
Identify potential procedural inaction cases.

This script cross-references:
1. Langworthy's committee assignments
2. Bills referred to those committees
3. His public statements on topics
4. Committee inaction (no markup, no vote)

Usage:
    python3 scripts/find_procedural_inaction.py

Requires:
    - data/langworthy_committees.json (from fetch_legislator_data.py)
    - Congress.gov API key in CONGRESS_GOV_API_KEY env var
"""

import json
import os
import requests
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

CONGRESS_GOV_API_KEY = os.getenv("CONGRESS_GOV_API_KEY")
CONGRESS_NUMBER = 119  # Current Congress

def load_committees():
    """Load Langworthy's committee data"""
    committees_file = Path("data/langworthy_committees.json")
    if not committees_file.exists():
        print("ERROR: Run fetch_legislator_data.py first to get committee data")
        return None

    with open(committees_file) as f:
        return json.load(f)

def get_committee_bills(committee_code, congress=CONGRESS_NUMBER):
    """
    Fetch bills referred to a committee using Congress.gov API

    Args:
        committee_code: Thomas ID like "HSAG" or "SSEG"
        congress: Congress number (default 119)

    Returns:
        List of bills with metadata
    """
    if not CONGRESS_GOV_API_KEY:
        print("WARNING: No CONGRESS_GOV_API_KEY set. Using dummy data.")
        return []

    url = f"https://api.congress.gov/v3/committee/{congress}/{committee_code}/bills"
    params = {
        "api_key": CONGRESS_GOV_API_KEY,
        "format": "json",
        "limit": 250  # Max per request
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("bills", [])
    except Exception as e:
        print(f"Error fetching bills for {committee_code}: {e}")
        return []

def analyze_bill_status(bill):
    """
    Determine if a bill shows signs of inaction

    Returns:
        dict with inaction indicators
    """
    actions = bill.get("actions", {})
    latest_action = actions.get("latestAction", {})
    latest_date = latest_action.get("actionDate")

    if latest_date:
        latest = datetime.strptime(latest_date, "%Y-%m-%d")
        days_since_action = (datetime.now() - latest).days
    else:
        days_since_action = None

    # Check for committee activity
    committee_actions = [
        a for a in actions.get("actions", [])
        if "committee" in a.get("text", "").lower()
    ]

    has_markup = any(
        "markup" in a.get("text", "").lower()
        for a in committee_actions
    )

    has_hearing = any(
        "hearing" in a.get("text", "").lower()
        for a in committee_actions
    )

    has_vote = any(
        "vote" in a.get("text", "").lower() or
        "passed" in a.get("text", "").lower()
        for a in committee_actions
    )

    return {
        "days_since_action": days_since_action,
        "has_markup": has_markup,
        "has_hearing": has_hearing,
        "has_committee_vote": has_vote,
        "stuck": days_since_action and days_since_action > 90 and not has_vote,
        "latest_action": latest_action.get("text", ""),
        "latest_date": latest_date
    }

def categorize_by_topic(bill):
    """
    Attempt to categorize bill by topic

    This is a simple heuristic - ideally use ProPublica or VoteView for better classification
    """
    title = bill.get("title", "").lower()
    policy_area = bill.get("policyArea", {}).get("name", "").lower()

    # Simple keyword matching
    topics = []

    if any(kw in title or kw in policy_area for kw in ["health", "medicare", "medicaid", "aca", "care"]):
        topics.append("Healthcare")

    if any(kw in title or kw in policy_area for kw in ["veteran", "va ", "armed forces"]):
        topics.append("Veterans")

    if any(kw in title or kw in policy_area for kw in ["immigration", "border", "refugee"]):
        topics.append("Immigration")

    if any(kw in title or kw in policy_area for kw in ["farm", "agriculture", "rural"]):
        topics.append("Agriculture")

    if any(kw in title or kw in policy_area for kw in ["energy", "climate", "environment"]):
        topics.append("Energy & Environment")

    if any(kw in title or kw in policy_area for kw in ["budget", "appropriation", "spending"]):
        topics.append("Budget")

    if not topics:
        topics.append(policy_area.title() if policy_area else "Other")

    return topics

def generate_report(committees_data):
    """Generate procedural inaction report"""
    print("="*70)
    print("PROCEDURAL INACTION ANALYSIS")
    print("="*70)

    committees = committees_data.get("committees", [])

    # Focus on full committees (not subcommittees)
    main_committees = [
        c for c in committees
        if len(c["committee_id"]) == 4  # Main committees have 4-char IDs
    ]

    print(f"\nAnalyzing {len(main_committees)} main committees...\n")

    all_stuck_bills = []

    for committee in main_committees:
        committee_id = committee["committee_id"]
        committee_name = committee.get("name", committee_id)

        print(f"\n{committee_name}")
        print("-" * 70)

        bills = get_committee_bills(committee_id)

        if not bills:
            print("  (No API data available)")
            continue

        print(f"  Total bills referred: {len(bills)}")

        # Analyze each bill
        stuck_bills = []
        for bill in bills:
            status = analyze_bill_status(bill)

            if status["stuck"]:
                topics = categorize_by_topic(bill)
                stuck_bills.append({
                    "bill_number": bill.get("number"),
                    "title": bill.get("title"),
                    "topics": topics,
                    "days_stuck": status["days_since_action"],
                    "latest_action": status["latest_action"],
                    "latest_date": status["latest_date"],
                    "committee": committee_name,
                    "committee_id": committee_id
                })

        if stuck_bills:
            print(f"  ⚠ Bills stuck >90 days: {len(stuck_bills)}")
            for bill in stuck_bills[:5]:  # Show top 5
                print(f"     • {bill['bill_number']}: {bill['title'][:60]}...")
                print(f"       Stuck for {bill['days_stuck']} days | Topics: {', '.join(bill['topics'])}")

            all_stuck_bills.extend(stuck_bills)
        else:
            print("  ✓ No bills stuck >90 days")

    # Save full report
    report_file = Path("data/procedural_inaction_candidates.json")
    with open(report_file, "w") as f:
        json.dump({
            "generated_at": datetime.utcnow().isoformat(),
            "congress": CONGRESS_NUMBER,
            "member": committees_data.get("member"),
            "stuck_bills": all_stuck_bills,
            "count": len(all_stuck_bills),
            "by_topic": group_by_topic(all_stuck_bills),
            "by_committee": group_by_committee(all_stuck_bills)
        }, f, indent=2)

    print("\n" + "="*70)
    print(f"✓ Saved {len(all_stuck_bills)} candidates to {report_file}")
    print("="*70)

    # Print summary by topic
    if all_stuck_bills:
        print("\nSUMMARY BY TOPIC:")
        print("-" * 70)
        by_topic = group_by_topic(all_stuck_bills)
        for topic, count in sorted(by_topic.items(), key=lambda x: x[1], reverse=True):
            print(f"  {topic}: {count} bills")

def group_by_topic(bills):
    """Count bills by topic"""
    topic_counts = defaultdict(int)
    for bill in bills:
        for topic in bill["topics"]:
            topic_counts[topic] += 1
    return dict(topic_counts)

def group_by_committee(bills):
    """Group bills by committee"""
    by_committee = defaultdict(list)
    for bill in bills:
        by_committee[bill["committee"]].append(bill)
    return {k: len(v) for k, v in by_committee.items()}

def main():
    # Load committee data
    committees_data = load_committees()
    if not committees_data:
        return 1

    # Generate report
    generate_report(committees_data)

    print("\n" + "="*70)
    print("NEXT STEPS:")
    print("="*70)
    print("""
1. Review data/procedural_inaction_candidates.json
2. For each stuck bill, search for Langworthy statements on that topic
3. If he made public statements supporting action, document the gap
4. Use the procedural inaction template to create a fact-check entry

Example search:
  - Press releases on his official site
  - Local news interviews
  - Congressional Record speeches
  - Social media posts
  - Town halls or public events

Match the topic and timeframe to find contradictions.
    """)

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
