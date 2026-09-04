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

# Warn (don't block) if origin/main has commits this checkout doesn't —
# e.g. pushed from another machine, or edited on GitHub directly. `git
# push` itself will refuse a non-fast-forward push either way, but it's
# better to notice before you start editing than from a push error after.
git fetch origin main -q 2>/dev/null || true
if git rev-parse origin/main >/dev/null 2>&1; then
    behind=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo 0)
    if [ "$behind" -gt 0 ]; then
        echo "⚠  origin/main has ${behind} commit(s) not in this checkout."
        echo "   Run 'git pull' before editing, or you'll be editing a stale copy"
        echo "   and 'git push' will be rejected later."
        echo ""
    fi
fi

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
