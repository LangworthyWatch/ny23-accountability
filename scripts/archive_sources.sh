#!/bin/bash
# Archive Sources Script for LangworthyWatch
# Submits URLs from fact-check sources to Archive.org Wayback Machine
#
# Usage:
#   ./scripts/archive_sources.sh [--dry-run] [PATH ...]
#
#   PATH  One or more markdown files, or directories to scan for *.md.
#         Omit to scan every entry in content/fact-checks (the old behavior).
#
# Examples:
#   ./scripts/archive_sources.sh --dry-run
#       Preview every URL across all fact-checks.
#
#   ./scripts/archive_sources.sh content/fact-checks/2026-07-16-rules-committee-gatekeeper-pattern.md
#       Archive only the URLs cited by that one entry. Use this after editing a
#       single entry — archiving the whole corpus every time exhausts the
#       Wayback rate limit and gets the run 429'd partway through.
#
#   ./scripts/archive_sources.sh --dry-run content/correspondence/letters
#       Preview URLs under a directory.

set -e

DEFAULT_DIR="content/fact-checks"
LOG_FILE="archive_log_$(date +%Y%m%d_%H%M%S).txt"
DRY_RUN=false
TARGETS=()

usage() { sed -n '2,22p' "$0" | sed 's/^# \{0,1\}//'; }

# ---- argument parsing ----------------------------------------------------
# --dry-run may appear anywhere; everything else is treated as a path.
for arg in "$@"; do
    case "$arg" in
        --dry-run) DRY_RUN=true ;;
        -h|--help) usage; exit 0 ;;
        -*)        echo "ERROR: unknown option: $arg" >&2
                   echo "Run with --help for usage." >&2
                   exit 2 ;;
        *)         TARGETS[${#TARGETS[@]}]="$arg" ;;
    esac
done

# ---- resolve targets to a concrete file list -----------------------------
FILES=()
add_md_under() {   # $1 = directory
    local f
    while IFS= read -r f; do
        [[ -n "$f" ]] && FILES[${#FILES[@]}]="$f"
    done < <(find "$1" -type f -name '*.md' | sort)
}

if [[ ${#TARGETS[@]} -eq 0 ]]; then
    if [[ ! -d "$DEFAULT_DIR" ]]; then
        echo "ERROR: default directory '$DEFAULT_DIR' not found." >&2
        echo "Run this from the repo root, or pass explicit paths." >&2
        exit 2
    fi
    add_md_under "$DEFAULT_DIR"
    SCOPE="all entries in $DEFAULT_DIR"
else
    for t in "${TARGETS[@]}"; do
        if [[ -d "$t" ]]; then
            add_md_under "$t"
        elif [[ -f "$t" ]]; then
            FILES[${#FILES[@]}]="$t"
        else
            echo "ERROR: no such file or directory: $t" >&2
            exit 2
        fi
    done
    SCOPE="${#FILES[@]} file(s) you named"
fi

if [[ ${#FILES[@]} -eq 0 ]]; then
    echo "ERROR: no markdown files matched." >&2
    exit 2
fi

echo "LangworthyWatch Source Archival Script"
echo "========================================"
echo "Scope:    $SCOPE"
echo "Log file: $LOG_FILE"
echo ""
if [[ ${#FILES[@]} -le 10 ]]; then
    echo "Scanning:"
    for f in "${FILES[@]}"; do echo "  - $f"; done
    echo ""
fi

# Extract URLs from the resolved file list
extract_urls() {
    grep -oh 'https://[^)"<>[:space:]]*' "${FILES[@]}" 2>/dev/null | \
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

    # Gov sources that block both curl AND the Wayback "save" endpoint (Cloudflare 520 /
    # Akamai 403). These must be captured from a real browser via Save Page Now — flag,
    # don't waste retries. (Documented in the /wrap skill.)
    case "$url" in
        *congress.gov*|*fema.gov*|*clerk.house.gov*|*rules.house.gov*|*energycommerce.house.gov*|*oversight.house.gov*)
            echo "  [MANUAL] gov source blocks the save endpoint — capture from a browser (Save Page Now)"
            echo "$(date): MANUAL - $url" >> "$LOG_FILE"
            return 0
            ;;
    esac

    # Submit to Wayback with retry/backoff on transient failures (000 / 429 / 5xx).
    local attempt response
    for attempt in 1 2 3; do
        response=$(curl -s -m 40 -w "%{http_code}" -o /dev/null "https://web.archive.org/save/$url" 2>/dev/null || echo "000")
        if [[ "$response" == "200" ]] || [[ "$response" == "302" ]]; then
            echo "  [OK] Submitted (attempt $attempt)"
            echo "$(date): OK - $url" >> "$LOG_FILE"
            sleep 2
            return 0
        fi
        echo "  [retry $attempt/3] response $response"
        sleep $((attempt * 5))
    done
    echo "  [WARN] gave up after 3 attempts (last: $response) — retry later or capture from a browser"
    echo "$(date): WARN ($response after 3 tries) - $url" >> "$LOG_FILE"
    sleep 2
}

# Main execution
echo "Extracting URLs..."
urls=$(extract_urls)

if [[ -z "$urls" ]]; then
    url_count=0
else
    url_count=$(printf '%s\n' "$urls" | wc -l | tr -d ' ')
fi

echo "Found $url_count unique URLs to archive"
echo ""

if [[ "$url_count" -eq 0 ]]; then
    echo "Nothing to do."
    exit 0
fi

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
    ok_count=$(grep -c ": OK" "$LOG_FILE" 2>/dev/null || echo "0")
    warn_count=$(grep -c ": WARN" "$LOG_FILE" 2>/dev/null || echo "0")
    manual_count=$(grep -c ": MANUAL" "$LOG_FILE" 2>/dev/null || echo "0")
    echo "Successful: $ok_count"
    echo "Warnings: $warn_count"
    echo "Manual (gov, browser capture needed): $manual_count"
fi
