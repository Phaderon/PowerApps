#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCES="$ROOT/.sources"
mkdir -p "$SOURCES"

clone_or_pull() {
  local name="$1"
  local url="$2"
  local dest="$SOURCES/$name"

  if [[ -d "$dest/.git" ]]; then
    echo "Updating $name"
    git -C "$dest" pull --ff-only
  else
    echo "Cloning $name"
    git clone --depth 1 "$url" "$dest"
  fi
}

clone_or_pull "powerapps-docs" "https://github.com/MicrosoftDocs/powerapps-docs.git"
clone_or_pull "power-platform" "https://github.com/MicrosoftDocs/power-platform.git"

echo "Done. Build/search the local index with:"
echo "  python3 tools/index-msdocs.py --rebuild"

