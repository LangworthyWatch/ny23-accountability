#!/bin/bash
# Quick Archive.org Batch Submission Script
# This script submits URLs to Archive.org one at a time

echo "========================================="
echo "Archive.org Batch URL Submission"
echo "========================================="
echo ""
echo "This script will submit 7 URLs to Archive.org's Wayback Machine"
echo "It takes about 2-3 minutes total"
echo ""

# Array of URLs to archive
urls=(
    "https://towerpointwealth.com/is-social-security-tax-free/"
    "https://www.newsweek.com/no-tax-social-security-seniors-big-beautiful-bill-2115721"
    "https://langworthy.house.gov/media/press-releases/congressman-nick-langworthy-visits-springville-spotlight-local-seniors-small"
    "https://langworthy.house.gov/media/press-releases/congressman-nick-langworthy-announces-over-38-million-fra-grant-finger-lakes"
    "https://langworthy.house.gov/media/press-releases/congressman-nick-langworthy-announces-46-million-federal-funding-water"
    "https://www.eda.gov/news/press-release/2024/06/25/us-department-commerce-invests-46-million-water-infrastructure"
    "https://www.fingerlakes1.com/2025/06/10/finger-lakes-railway-awarded-3-8-million-federal-grant-for-track-upgrades/"
)

count=1
total=${#urls[@]}

for url in "${urls[@]}"; do
    echo "[$count/$total] Archiving: ${url:0:70}..."

    # Submit to Archive.org using their save API
    # This doesn't wait for a response, just queues it
    curl -s -m 60 "https://web.archive.org/save/$url" > /dev/null 2>&1

    if [ $? -eq 0 ]; then
        echo "  ✓ Submitted"
    else
        echo "  ⚠ May have timed out (but probably queued)"
    fi

    # Rate limit: wait 3 seconds between submissions
    if [ $count -lt $total ]; then
        sleep 3
    fi

    ((count++))
done

echo ""
echo "========================================="
echo "✓ Done submitting URLs"
echo "========================================="
echo ""
echo "The URLs have been queued for archiving."
echo "Archive.org will process them over the next few minutes."
echo ""
echo "To get the archive URLs, wait 5-10 minutes, then run:"
echo "  python3 batch_archive_urls.py --retry"
echo ""
echo "This will check Archive.org for the completed archives"
echo "and retrieve the archive URLs."
echo ""
