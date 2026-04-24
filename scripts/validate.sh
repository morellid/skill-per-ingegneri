#!/usr/bin/env bash
# Valida una skill (struttura, frontmatter, sources.yaml, link).
# Uso: ./scripts/validate.sh <nome-skill>
#       ./scripts/validate.sh --all

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/skills"

validate_skill() {
  local skill_path="$1"
  local skill_name
  skill_name=$(basename "$skill_path")
  local errors=0

  echo "=== Validazione: $skill_name ==="

  # 1. SKILL.md presente
  if [ ! -f "$skill_path/SKILL.md" ]; then
    echo "  ERRORE: SKILL.md mancante"
    errors=$((errors + 1))
  else
    # 1a. Frontmatter YAML presente
    if ! head -1 "$skill_path/SKILL.md" | grep -q "^---$"; then
      echo "  ERRORE: SKILL.md senza frontmatter YAML"
      errors=$((errors + 1))
    fi
    # 1b. Ha name e description
    if ! grep -q "^name:" "$skill_path/SKILL.md"; then
      echo "  ERRORE: SKILL.md senza 'name' nel frontmatter"
      errors=$((errors + 1))
    fi
    if ! grep -q "^description:" "$skill_path/SKILL.md"; then
      echo "  ERRORE: SKILL.md senza 'description' nel frontmatter"
      errors=$((errors + 1))
    fi
    # 1c. Disclaimer presente
    if ! grep -qi "non sostituisce" "$skill_path/SKILL.md"; then
      echo "  WARN: SKILL.md potrebbe non contenere il disclaimer di responsabilita' professionale"
    fi
  fi

  # 2. sources.yaml presente e leggibile
  if [ ! -f "$skill_path/references/sources.yaml" ]; then
    echo "  ERRORE: references/sources.yaml mancante"
    errors=$((errors + 1))
  else
    if ! grep -q "^schema_version:" "$skill_path/references/sources.yaml"; then
      echo "  ERRORE: sources.yaml senza schema_version"
      errors=$((errors + 1))
    fi
  fi

  # 3. CHANGELOG.md
  if [ ! -f "$skill_path/CHANGELOG.md" ]; then
    echo "  ERRORE: CHANGELOG.md mancante"
    errors=$((errors + 1))
  fi

  # 4. README.md
  if [ ! -f "$skill_path/README.md" ]; then
    echo "  WARN: README.md mancante"
  fi

  # 5. Almeno un task file o una chiara indicazione che non servono
  if [ -d "$skill_path/tasks" ]; then
    local task_count
    task_count=$(find "$skill_path/tasks" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
    if [ "$task_count" -eq 0 ]; then
      echo "  WARN: nessun task file in tasks/"
    fi
  fi

  # 6. Esempi
  if [ -d "$skill_path/examples" ]; then
    local example_count
    example_count=$(find "$skill_path/examples" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
    if [ "$example_count" -eq 0 ]; then
      echo "  WARN: nessun esempio in examples/"
    fi
  fi

  if [ $errors -eq 0 ]; then
    echo "  OK: nessun errore bloccante"
  else
    echo "  $errors errori bloccanti"
    return 1
  fi
  return 0
}

if [ $# -eq 0 ] || [ "$1" = "--all" ]; then
  # Valida tutte le skill
  total_errors=0
  for skill_dir in "$SKILLS_DIR"/*/; do
    if [ -d "$skill_dir" ] && [ "$(basename "$skill_dir")" != "_archived" ]; then
      if ! validate_skill "$skill_dir"; then
        total_errors=$((total_errors + 1))
      fi
      echo ""
    fi
  done
  if [ $total_errors -gt 0 ]; then
    echo "$total_errors skill con errori bloccanti"
    exit 1
  fi
  echo "Tutte le skill valide."
else
  # Valida skill specifica
  skill_name="$1"
  skill_path="$SKILLS_DIR/$skill_name"
  if [ ! -d "$skill_path" ]; then
    echo "Errore: skill '$skill_name' non trovata in $SKILLS_DIR"
    exit 1
  fi
  validate_skill "$skill_path"
fi
