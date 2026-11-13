#!/usr/bin/env bash
# Render the share cards for the home page, /projects and /resume into static/og/.
# Uses headless Chrome; set CHROME to override its path.
set -euo pipefail

cd "$(dirname "$0")/../.."
chrome="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
template="file://$PWD/scripts/og/card.html"

render() {
  local name=$1 query=$2 profile
  profile=$(mktemp -d)
  "$chrome" --headless=new --disable-gpu --hide-scrollbars --user-data-dir="$profile" \
    --allow-file-access-from-files --virtual-time-budget=2000 --window-size=1200,630 \
    --screenshot="$PWD/static/og/$name.png" "$template?$query" 2>/dev/null
  rm -rf "$profile"
  echo "static/og/$name.png"
}

render home "$(python3 -c 'import urllib.parse as u; print(u.urlencode({
  "title": "Josh McKinney",
  "lead": "Software engineer: backend, platform, security, and developer tools.",
  "points": "Ratatui co-maintainer|OpenAI (Codex)|Amazon / AWS security",
}))')"

render projects "$(python3 -c 'import urllib.parse as u; print(u.urlencode({
  "title": "Projects",
  "lead": "Rust and terminal tools I build and maintain, led by Ratatui: 70M+ downloads.",
  "points": "Ratatui|tui-widgets|betamax|jk|ratatui-diff",
}))')"

render resume "$(python3 -c 'import urllib.parse as u; print(u.urlencode({
  "title": "Josh McKinney",
  "lead": "Software engineer: backend, platform, security, and developer tooling. 20+ years.",
  "points": "OpenAI (Codex)|Amazon / AWS security|Ratatui co-maintainer",
}))')"
