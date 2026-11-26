#!/usr/bin/env bash
# Regenerate index.html from index.md. Usage: ./build/build.sh
set -euo pipefail
cd "$(dirname "$0")/.."
# 1. Redraw the masked sheets in the live repo from build/sheets.md (wording + which figures show).
cfg() { python3 -c "import os, tomllib; print(os.path.expanduser(tomllib.load(open('build/sleeves.toml', 'rb'))['$1']))"; }
LIVE="$(cfg live_root)"; PY="$(cfg live_python)"; SITE="$(pwd)"
(cd "$LIVE" && PYTHONPATH=.:scratch:scratch/tmp "$PY" scratch/public_sheets.py --text "$SITE/build/sheets.md")
# 2. Table + page. Capture first so a failed table build stops here and leaves index.html untouched.
expanded="$(python3 build/prepare_index.py)"
printf '%s\n' "$expanded" | pandoc \
  -f markdown-tex_math_dollars-smart \
  -t html5 --standalone --columns=1000 \
  --template build/template.html \
  --lua-filter build/figure_link.lua \
  -o index.html
echo "wrote index.html"
