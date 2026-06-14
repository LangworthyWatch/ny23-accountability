#!/bin/bash
# Stop-hook auto-deploy for langworthy-tracker → Cloudflare Pages.
#
# Migrated from Netlify to Cloudflare Pages on 2026-06-14: Netlify hit a hard
# account credit/quota wall (deploys returned JSONHTTPError: Forbidden). Cloudflare
# Pages' free tier + `wrangler` direct upload sidesteps that AND the flagged-GitHub-
# account problem (no Git integration needed — build locally, upload public/).
# Site: langworthywatch.org → langworthywatch.pages.dev (project "langworthywatch").
#
# Runs at the end of every Claude Code session. Compares HEAD SHA to the last
# deployed SHA; if unchanged, skips (no wasted deploys). If changed, CLEAN-builds
# (rm -rf public — Hugo doesn't delete stale files, so a prior `hugo -D` can leak
# draft pages into public/) and deploys via wrangler.
#
# wrangler auth: OAuth via `wrangler login` (user-level creds). Re-run if it lapses.
# Output is JSON for the Stop hook contract so the user sees a one-line result.

set -euo pipefail
export CLOUDFLARE_ACCOUNT_ID=3b752cee282808bcfcebc84aaea9a1c3

REPO_DIR="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker"
cd "$REPO_DIR" || exit 0

MARKER_FILE="$REPO_DIR/.wrangler/last_deployed_sha"
current_sha=$(git rev-parse HEAD 2>/dev/null || echo "unknown")
deployed_sha=$(cat "$MARKER_FILE" 2>/dev/null || echo "")

if [ "$current_sha" = "$deployed_sha" ]; then
  jq -nc --arg sha "${current_sha:0:8}" \
    '{systemMessage: ("Auto-deploy skipped (HEAD " + $sha + " already deployed)."), suppressOutput: true}'
  exit 0
fi

build_output=$(rm -rf public && hugo --gc --minify 2>&1) || {
  err_summary=$(echo "$build_output" | head -3 | tr '\n' '|')
  jq -nc --arg err "$err_summary" \
    '{systemMessage: ("✗ Hugo build failed at session end: " + $err), suppressOutput: true}'
  exit 0
}

deploy_output=$(wrangler pages deploy public --project-name=langworthywatch --branch=main --commit-dirty=true 2>&1) || {
  err_summary=$(echo "$deploy_output" | tail -3 | tr '\n' '|')
  jq -nc --arg err "$err_summary" \
    '{systemMessage: ("✗ Cloudflare Pages deploy failed at session end. Run: cd langworthy-tracker; wrangler pages deploy public --project-name=langworthywatch. " + $err), suppressOutput: true}'
  exit 0
}

# Successful deploy — record the SHA so we do not redeploy the same commit.
mkdir -p "$REPO_DIR/.wrangler"
echo "$current_sha" > "$MARKER_FILE"

dep_url=$(echo "$deploy_output" | grep -oE 'https://[a-z0-9]+\.langworthywatch\.pages\.dev' | tail -1)
jq -nc --arg sha "${current_sha:0:8}" --arg url "$dep_url" \
  '{systemMessage: ("✓ Cloudflare Pages deploy live (" + $sha + "): https://langworthywatch.org" + (if $url != "" then " (preview: " + $url + ")" else "" end)), suppressOutput: true}'
