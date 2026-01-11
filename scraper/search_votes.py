#!/usr/bin/env python3
"""
Interactive vote search tool
Usage: python3 search_votes.py [keywords]
"""

import sys
from analyze_votes import VoteAnalyzer


def main():
    a = VoteAnalyzer()

    if len(sys.argv) < 2:
        print("Usage: python3 search_votes.py <keywords>")
        print("\nExamples:")
        print("  python3 search_votes.py health aca")
        print("  python3 search_votes.py border immigration")
        print("  python3 search_votes.py veteran military")
        return

    keywords = sys.argv[1:]
    print(f"\nSearching for: {', '.join(keywords)}")
    print("="*80)

    # Search all votes
    all_matches = a.search_votes(keywords)
    print(f"\n✓ Found {len(all_matches)} total votes")

    # Break down by vote type
    yea = a.search_votes(keywords, vote_type='Yea')
    nay = a.search_votes(keywords, vote_type='Nay')
    not_voting = a.search_votes(keywords, vote_type='Not Voting')

    print(f"\nBreakdown:")
    print(f"  YES votes: {len(yea)}")
    print(f"  NO votes: {len(nay)}")
    print(f"  Not Voting: {len(not_voting)}")

    # Show first few NO votes (most interesting for contradictions)
    if nay:
        print(f"\n{'='*80}")
        print(f"First {min(3, len(nay))} NO votes:")
        for vote in nay[:3]:
            a.print_vote(vote)

    # Show first few YES votes
    if yea:
        print(f"\n{'='*80}")
        print(f"First {min(3, len(yea))} YES votes:")
        for vote in yea[:3]:
            a.print_vote(vote)


if __name__ == "__main__":
    main()
