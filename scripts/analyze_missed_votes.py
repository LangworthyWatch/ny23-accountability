#!/usr/bin/env python3
"""
Analyze missed votes from the votes.json data file.

Generates:
- Monthly breakdown of missed votes
- Comparison to House median
- Timeline data for visualization
- JSON output for Hugo data files

Usage:
    python3 scripts/analyze_missed_votes.py
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter

def load_votes():
    """Load votes from data file"""
    votes_file = Path("data/votes.json")
    with open(votes_file) as f:
        return json.load(f)

def analyze_attendance(votes):
    """Calculate attendance statistics"""
    total_votes = len(votes)

    # Count vote types
    vote_counts = Counter(v["vote"] for v in votes)

    # Missed votes are "Not Voting" or "Present" (sometimes)
    missed = vote_counts.get("Not Voting", 0)
    present = vote_counts.get("Present", 0)
    yea = vote_counts.get("Yea", 0)
    nay = vote_counts.get("Nay", 0)

    votes_cast = yea + nay

    # Calculate percentages
    attendance_rate = (votes_cast / total_votes) * 100 if total_votes > 0 else 0
    missed_rate = (missed / total_votes) * 100 if total_votes > 0 else 0

    return {
        "total_votes": total_votes,
        "votes_cast": votes_cast,
        "missed": missed,
        "present": present,
        "yea": yea,
        "nay": nay,
        "attendance_rate": round(attendance_rate, 1),
        "missed_rate": round(missed_rate, 1),
        "house_median": 2.0,  # From GovTrack data
        "worse_than_median": missed_rate > 2.0
    }

def analyze_by_month(votes):
    """Break down missed votes by month"""
    by_month = defaultdict(lambda: {"total": 0, "missed": 0, "yea": 0, "nay": 0})

    for vote in votes:
        date = datetime.strptime(vote["date"], "%Y-%m-%d")
        month_key = date.strftime("%Y-%m")

        by_month[month_key]["total"] += 1

        if vote["vote"] == "Not Voting":
            by_month[month_key]["missed"] += 1
        elif vote["vote"] == "Yea":
            by_month[month_key]["yea"] += 1
        elif vote["vote"] == "Nay":
            by_month[month_key]["nay"] += 1

    # Calculate rates
    for month_data in by_month.values():
        total = month_data["total"]
        month_data["missed_rate"] = round((month_data["missed"] / total) * 100, 1) if total > 0 else 0
        month_data["attendance_rate"] = round(((month_data["yea"] + month_data["nay"]) / total) * 100, 1) if total > 0 else 0

    return dict(sorted(by_month.items()))

def get_missed_vote_details(votes):
    """Get list of all missed votes with details"""
    missed = []

    for vote in votes:
        if vote["vote"] == "Not Voting":
            missed.append({
                "date": vote["date"],
                "roll_call": vote["roll_call"],
                "description": vote["description"],
                "bill": vote.get("bill", ""),
                "title": vote.get("title", ""),
                "url": vote["url"],
                "result": vote["result"]
            })

    # Sort by date (newest first)
    missed.sort(key=lambda x: x["date"], reverse=True)

    return missed

def generate_chart_data(by_month):
    """Generate data for timeline chart"""
    chart_data = {
        "labels": [],
        "missed": [],
        "total": []
    }

    for month, data in sorted(by_month.items()):
        # Convert YYYY-MM to readable format
        date = datetime.strptime(month, "%Y-%m")
        label = date.strftime("%b %Y")

        chart_data["labels"].append(label)
        chart_data["missed"].append(data["missed"])
        chart_data["total"].append(data["total"])

    return chart_data

def main():
    print("="*70)
    print("MISSED VOTES ANALYSIS")
    print("="*70)

    # Load data
    votes = load_votes()
    print(f"\nLoaded {len(votes)} votes")

    # Overall statistics
    stats = analyze_attendance(votes)

    print("\nOVERALL STATISTICS:")
    print("-" * 70)
    print(f"Total Roll Call Votes: {stats['total_votes']:,}")
    print(f"Votes Cast (Yea/Nay): {stats['votes_cast']:,}")
    print(f"Missed Votes: {stats['missed']}")
    print(f"Present: {stats['present']}")
    print(f"\nAttendance Rate: {stats['attendance_rate']}%")
    print(f"Missed Vote Rate: {stats['missed_rate']}%")
    print(f"House Median: {stats['house_median']}%")
    print(f"\n{'⚠ WORSE than median' if stats['worse_than_median'] else '✓ Better than median'}")

    # Monthly breakdown
    by_month = analyze_by_month(votes)

    print("\nMONTHLY BREAKDOWN:")
    print("-" * 70)
    print(f"{'Month':<12} {'Total':>7} {'Missed':>7} {'Rate':>7}")
    print("-" * 70)

    for month, data in sorted(by_month.items(), reverse=True)[:12]:  # Last 12 months
        date = datetime.strptime(month, "%Y-%m")
        month_label = date.strftime("%b %Y")
        print(f"{month_label:<12} {data['total']:>7} {data['missed']:>7} {data['missed_rate']:>6.1f}%")

    # Get missed vote details
    missed_votes = get_missed_vote_details(votes)

    print(f"\nMOST RECENT MISSED VOTES:")
    print("-" * 70)
    for vote in missed_votes[:10]:  # Show 10 most recent
        print(f"\n{vote['date']} - Roll Call #{vote['roll_call']}")
        print(f"  {vote['description'][:100]}...")
        if vote['bill']:
            print(f"  Bill: {vote['bill']}")

    # Save data files
    data_dir = Path("data")

    # Save overall stats
    stats_file = data_dir / "missed_votes_stats.json"
    with open(stats_file, "w") as f:
        json.dump({
            "statistics": stats,
            "by_month": by_month,
            "chart_data": generate_chart_data(by_month),
            "generated_at": datetime.utcnow().isoformat()
        }, f, indent=2)

    print(f"\n✓ Saved statistics to {stats_file}")

    # Save detailed missed votes
    details_file = data_dir / "missed_votes_details.json"
    with open(details_file, "w") as f:
        json.dump({
            "missed_votes": missed_votes,
            "count": len(missed_votes),
            "generated_at": datetime.utcnow().isoformat()
        }, f, indent=2)

    print(f"✓ Saved {len(missed_votes)} missed vote details to {details_file}")

    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"""
Langworthy missed {stats['missed']} of {stats['total_votes']:,} votes ({stats['missed_rate']}%)
This is {'WORSE' if stats['worse_than_median'] else 'better'} than the House median of {stats['house_median']}%

Constituents of NY-23 had no representation on these {stats['missed']} votes.
    """)

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
