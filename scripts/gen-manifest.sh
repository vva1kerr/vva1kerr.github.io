#!/usr/bin/env bash
# Regenerates manifest.json from every .md file in docs/
# Usage: bash scripts/gen-manifest.sh  (run from repo root)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DOCS_DIR="$REPO_ROOT/docs"
MANIFEST="$REPO_ROOT/manifest.json"

python3 << PYEOF
import os, json

docs = sorted(f for f in os.listdir("$DOCS_DIR") if f.endswith(".md"))
pages = [
    {
        "id":    f[:-3],
        "label": f[:-3].replace("-", " ").replace("_", " ").title(),
        "file":  f"docs/{f[:-3]}.md"
    }
    for f in docs
]

with open("$MANIFEST", "w") as fh:
    json.dump(pages, fh, indent=2)
    fh.write("\n")

print(f"manifest.json updated — {len(pages)} page(s):")
for p in pages:
    print(f"  {p['id']} → {p['label']}")
PYEOF
