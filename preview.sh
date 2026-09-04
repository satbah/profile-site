#!/bin/bash
# Local preview of this repo's content, exactly as nginx would serve it on
# the VPS (same static-file + `index index.html` behavior — no server-side
# logic on either side, so this is a faithful preview).
#
# Rebuilds en/index.html first so you're always previewing current content,
# not a stale build. Ctrl-C to stop.
set -euo pipefail
cd "$(dirname "$0")"

PORT="${1:-8420}"

echo "Rebuilding en/index.html from index.html..."
python3 build_en.py

echo ""
echo "Preview server running:"
echo "  日本語: http://localhost:${PORT}/"
echo "  English: http://localhost:${PORT}/en/"
echo ""
echo "(This is the same push -> commit -> deploy content, not yet pushed."
echo " Nothing here touches git or the live site.)"
echo ""

python3 -m http.server "$PORT"
