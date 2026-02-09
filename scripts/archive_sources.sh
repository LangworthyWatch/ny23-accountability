#!/bin/bash
# Archive Sources Script for LangworthyWatch
# Submits URLs from fact-check sources to Archive.org Wayback Machine
#
# Usage: ./scripts/archive_sources.sh [--dry-run]
#
# This script extracts URLs from fact-check markdown files and submits them
# to the Wayback Machine for archival. Run with --dry-run first to see URLs.

set -e

CONTENT_DIR="content/fact-checks"
LOG_FILE="archive_log_$(date +%Y%m%d_%H%M%S).txt"
DRY_RUN=false

if [[ "$1" == "--dry-run" ]]; then
    DRY_RUN=true
    echo "=== DRY RUN MODE - No URLs will be submitted ==="
fi

echo "LangworthyWatch Source Archival Script"
echo "========================================"
echo "Log file: $LOG_FILE"
echo ""

# Extract URLs from markdown files
extract_urls() {
    # Find URLs in Sources sections and throughout files
    grep -oh 'https://[^)"<>[:space:]]*' "$CONTENT_DIR"/*.md 2>/dev/null | \
    grep -v 'archive.org' | \
    grep -v 'localhost' | \
    grep -v 'example.com' | \
    grep -v 'langworthywatch.org' | \
    sort -u
}

# Submit URL to Wayback Machine
archive_url() {
    local url="$1"
    echo "Archiving: $url"

    if [[ "$DRY_RUN" == "true" ]]; then
        echo "  [DRY RUN] Would submit to archive.org"
        return 0
    fi

    # Submit to Wayback Machine
    response=$(curl -s -w "%{http_code}" -o /dev/null "https://web.archive.org/save/$url" 2>/dev/null || echo "000")

    if [[ "$response" == "200" ]] || [[ "$response" == "302" ]]; then
        echo "  [OK] Submitted successfully"
        echo "$(date): OK - $url" >> "$LOG_FILE"
    else
        echo "  [WARN] Response code: $response"
        echo "$(date): WARN ($response) - $url" >> "$LOG_FILE"
    fi

    # Rate limit to avoid overwhelming archive.org
    sleep 2
}

# Main execution
echo "Extracting URLs from $CONTENT_DIR..."
urls=$(extract_urls)
url_count=$(echo "$urls" | wc -l | tr -d ' ')

echo "Found $url_count unique URLs to archive"
echo ""

if [[ "$DRY_RUN" == "true" ]]; then
    echo "URLs that would be archived:"
    echo "----------------------------"
    echo "$urls"
    echo ""
    echo "Run without --dry-run to submit these URLs to archive.org"
else
    echo "Starting archival process..."
    echo "This will take approximately $((url_count * 2 / 60)) minutes"
    echo ""

    while IFS= read -r url; do
        if [[ -n "$url" ]]; then
            archive_url "$url"
        fi
    done <<< "$urls"

    echo ""
    echo "Archival complete. Check $LOG_FILE for results."
fi

echo ""
echo "=== Summary ==="
echo "Total URLs processed: $url_count"
if [[ -f "$LOG_FILE" ]]; then
    ok_count=$(grep -c "^.*: OK" "$LOG_FILE" 2>/dev/null || echo "0")
    warn_count=$(grep -c "^.*: WARN" "$LOG_FILE" 2>/dev/null || echo "0")
    echo "Successful: $ok_count"
    echo "Warnings: $warn_count"
fi
