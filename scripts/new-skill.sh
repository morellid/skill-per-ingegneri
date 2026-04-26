#!/usr/bin/env bash
# Crea una nuova skill dal template.
# Uso: ./scripts/new-skill.sh <nome-skill>
#   dove <nome-skill> e' in kebab-case (es. "pos-allegato-xv-checker")
#
# La skill creata e' compatibile sia con Anthropic Claude Code che con OpenAI Codex
# (frontmatter SKILL.md con license: MIT + agents/openai.yaml).

set -euo pipefail

if [ $# -ne 1 ]; then
  echo "Uso: $0 <nome-skill>"
  echo "  Esempio: $0 pos-allegato-xv-checker"
  exit 1
fi

SKILL_NAME="$1"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEMPLATE_DIR="$REPO_ROOT/templates/skill-template"
TARGET_DIR="$REPO_ROOT/skills/$SKILL_NAME"

# Validazione nome (kebab-case)
if ! [[ "$SKILL_NAME" =~ ^[a-z][a-z0-9-]*[a-z0-9]$ ]]; then
  echo "Errore: nome skill deve essere kebab-case (lowercase, trattini, no underscore)"
  exit 1
fi

# Check che non esista gia'
if [ -d "$TARGET_DIR" ]; then
  echo "Errore: la skill '$SKILL_NAME' esiste gia' in $TARGET_DIR"
  exit 1
fi

# Copia template (include automaticamente agents/openai.yaml)
cp -r "$TEMPLATE_DIR" "$TARGET_DIR"

# Sostituzione placeholder
TODAY=$(date +%Y-%m-%d)
find "$TARGET_DIR" -type f \( -name "*.md" -o -name "*.yaml" \) -exec sed -i '' \
  -e "s/SKILL_NAME_PLACEHOLDER/$SKILL_NAME/g" \
  -e "s/YYYY-MM-DD/$TODAY/g" \
  {} \;

echo "Skill '$SKILL_NAME' creata in $TARGET_DIR"
echo ""
echo "Compatibilita': Claude Code + OpenAI Codex (dual-agent)"
echo ""
echo "Prossimi passi:"
echo "  1. Editare SKILL.md (nome leggibile, description, routing task, license: MIT gia' presente)"
echo "  2. Personalizzare agents/openai.yaml (display_name, short_description, default_prompt per il picker Codex)"
echo "  3. Popolare references/sources.yaml con fonti reali"
echo "  4. Creare task files in tasks/"
echo "  5. Vedi methodology/generazione-skill.md per il processo completo"
