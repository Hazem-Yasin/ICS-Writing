#!/usr/bin/env bash
# Clone the eight content repositories into place next to this hub repo.
# Run from the hub root:  bash tools/setup_repos.sh [owner]
# Needs access to the (private) repositories, e.g. `gh auth login` first.
set -euo pipefail
cd "$(dirname "$0")/.."
OWNER="${1:-Hazem-Yasin}"
declare -A REPOS=(
  [canon/documents]=ics-writing-canon-documents
  [canon/characters]=ics-writing-canon-characters
  [canon/enemies]=ics-writing-canon-enemies
  [canon/facility]=ics-writing-canon-facility
  [canon/weapons]=ics-writing-canon-weapons
  [canon/internal-communications]=ics-writing-canon-internal-communications
  [design]=ics-writing-design
  [story]=ics-writing-story
)
for dir in "${!REPOS[@]}"; do
  if [ -e "$dir/.git" ]; then echo "ok      $dir"; continue; fi
  mkdir -p "$(dirname "$dir")"
  git clone "https://github.com/$OWNER/${REPOS[$dir]}.git" "$dir"
done
git config core.hooksPath tools/hooks
echo "done. Check with: python3 tools/ics.py check"
