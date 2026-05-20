#!/usr/bin/env bash
# Crea un .zip per ogni skill in skills/<id>/ -> dist/<id>.zip
# Ogni zip contiene una singola directory top-level <id>/ con SKILL.md + asset
# + una copia della LICENSE del repo. Pronto per drag-and-drop su claude.ai/customize/skills.
#
# Esclusioni: not_in_repo/, .DS_Store, __pycache__, *.pyc
#
# Uso: ./scripts/build_releases.sh
# Funziona in locale (macOS/Linux) e in GitHub Actions (ubuntu-latest).
# Output: dist/<skill-id>.zip (uno per skill), dist/ e' gitignorato.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/skills"
DIST_DIR="$REPO_ROOT/dist"
LICENSE_FILE="$REPO_ROOT/LICENSE"

if [ ! -f "$LICENSE_FILE" ]; then
  echo "ERROR: LICENSE non trovato a $LICENSE_FILE" >&2
  exit 1
fi

if ! command -v zip >/dev/null 2>&1; then
  echo "ERROR: comando 'zip' non disponibile. Installalo (brew install zip / apt-get install zip)." >&2
  exit 1
fi

rm -rf "$DIST_DIR"
mkdir -p "$DIST_DIR"

STAGING="$(mktemp -d)"
trap 'rm -rf "$STAGING"' EXIT

count=0
for skill_dir in "$SKILLS_DIR"/*/; do
  skill_id="$(basename "$skill_dir")"

  if [ ! -f "$skill_dir/SKILL.md" ]; then
    echo "SKIP $skill_id: SKILL.md mancante"
    continue
  fi

  pkg_dir="$STAGING/$skill_id"
  rm -rf "$pkg_dir"

  # Copia contenuto della skill nello staging escludendo binari e artefatti locali.
  # rsync e' disponibile sia su macOS sia su ubuntu-latest in Actions.
  rsync -a \
    --exclude 'not_in_repo/' \
    --exclude '.DS_Store' \
    --exclude '__pycache__/' \
    --exclude '*.pyc' \
    "$skill_dir" "$pkg_dir/"

  cp "$LICENSE_FILE" "$pkg_dir/LICENSE"

  zip_path="$DIST_DIR/$skill_id.zip"
  (cd "$STAGING" && zip -rq "$zip_path" "$skill_id")

  size="$(du -h "$zip_path" | cut -f1)"
  echo "OK   $skill_id.zip  ($size)"
  count=$((count + 1))
done

echo ""
echo "Costruiti $count zip in $DIST_DIR"
