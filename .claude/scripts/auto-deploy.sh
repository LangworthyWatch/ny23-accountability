#!/bin/bash
# Stop-hook auto-deploy for langworthy-tracker.
#
# Why: Netlify's GitHub-app webhook integration is broken AND GitHub Actions
# is permanently disabled at the LangworthyWatch user account level (account
# was flagged). So `git push` to main does NOT deploy on its own — the only
# working deploy path is `netlify deploy --prod --dir=public` from this machine.
#
# This script runs at the end of every Claude Code session in this project.
# It compares the current HEAD SHA to the SHA last deployed (tracked in
# .netlify/last_deployed_sha). If they differ, build + deploy. If they match,
# skip — no Netlify build minutes wasted on read-only sessions.
#
# Output is JSON for the Stop hook contract so the user sees a one-line result.

set -euo pipefail

REPO_DIR="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker"
cd "$REPO_DIR" || exit 0

MARKER_FILE="$REPO_DIR/.netlify/last_deployed_sha"
current_sha=$(git rev-parse HEAD 2>/dev/null || echo "unknown")
deployed_sha=$(cat "$MARKER_FILE" 2>/dev/null || echo "")

if [ "$current_sha" = "$deployed_sha" ]; then
  jq -nc --arg sha "${current_sha:0:8}" \
    '{systemMessage: ("Auto-deploy skipped (HEAD " + $sha + " already deployed)."), suppressOutput: true}'
  exit 0
fi

# Build + deploy. Capture output for status reporting.
build_output=$(hugo --gc --minify 2>&1) || {
  err_summary=$(echo "$build_output" | head -3 | tr '\n' '|')
  jq -nc --arg err "$err_summary" \
    '{systemMessage: ("✗ Hugo build failed at session end: " + $err), suppressOutput: true}'
  exit 0
}

deploy_output=$(netlify deploy --prod --dir=public 2>&1) || {
  err_summary=$(echo "$deploy_output" | head -3 | tr '\n' '|')
  jq -nc --arg err "$err_summary" \
    '{systemMessage: ("✗ Netlify deploy failed at session end. Run manually: cd langworthy-tracker; netlify deploy --prod --dir=public. " + $err), suppressOutput: true}'
  exit 0
}

# Successful deploy — record the SHA so we don't redeploy the same commit.
mkdir -p "$REPO_DIR/.netlify"
echo "$current_sha" > "$MARKER_FILE"

# Extract the production URL for a clean one-line confirmation.
prod_url=$(echo "$deploy_output" | grep -oE 'https://langworthywatch\.org' | head -1)
unique_url=$(echo "$deploy_output" | grep -oE 'https://[a-z0-9-]+--langworthywatch\.netlify\.app' | head -1)

if [ -n "$prod_url" ]; then
  jq -nc --arg url "$prod_url" --arg uniq "$unique_url" --arg sha "${current_sha:0:8}" \
    '{systemMessage: ("✓ Netlify deploy live (" + $sha + "): " + $url + (if $uniq != "" then " (unique: " + $uniq + ")" else "" end)), suppressOutput: true}'
else
  jq -nc --arg sha "${current_sha:0:8}" \
    '{systemMessage: ("✓ Netlify deploy completed (commit " + $sha + ")."), suppressOutput: true}'
fi
