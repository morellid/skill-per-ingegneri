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
    # 2a. Regola zero (vedi AGENTS.md): nessun placeholder SHA256.
    if grep -qE "sha256:.*(REPLACE_WHEN_DOWNLOADED|REPLACE_WITH_ACTUAL_HASH|PENDING_FETCH|TODO_HASH|XXX_HASH)" "$skill_path/references/sources.yaml"; then
      echo "  ERRORE: sources.yaml contiene placeholder SHA256 (Regola zero violata)"
      grep -nE "sha256:.*(REPLACE_WHEN_DOWNLOADED|REPLACE_WITH_ACTUAL_HASH|PENDING_FETCH|TODO_HASH|XXX_HASH)" "$skill_path/references/sources.yaml" | sed 's/^/    /'
      errors=$((errors + 1))
    fi
    # 2b. sha256 vuoto e' violazione (deve essere hash valido o null esplicito)
    if grep -qE '^[[:space:]]*sha256:[[:space:]]*(""|\x27\x27)?[[:space:]]*$' "$skill_path/references/sources.yaml"; then
      echo "  ERRORE: sources.yaml contiene sha256 vuoto (deve essere hash valido o null esplicito)"
      grep -nE '^[[:space:]]*sha256:[[:space:]]*(""|\x27\x27)?[[:space:]]*$' "$skill_path/references/sources.yaml" | sed 's/^/    /'
      errors=$((errors + 1))
    fi
    # 2c. Regola zero Step 3 (vedi AGENTS.md): per ogni fonte con md_path dichiarato
    # non null, il file referenziato deve esistere ed essere non vuoto.
    while IFS= read -r mdline; do
      mdpath=$(echo "$mdline" | sed -E 's/^[[:space:]]*md_path:[[:space:]]*//; s/[[:space:]]*$//; s/^"//; s/"$//')
      if [ -z "$mdpath" ] || [ "$mdpath" = "null" ]; then
        continue
      fi
      if [ ! -s "$skill_path/$mdpath" ]; then
        echo "  ERRORE: md_path '$mdpath' dichiarato in sources.yaml ma file mancante o vuoto (Regola zero Step 3)"
        errors=$((errors + 1))
      fi
    done < <(grep -E "^[[:space:]]*md_path:" "$skill_path/references/sources.yaml" 2>/dev/null || true)

    # 2d. Ogni excerpt_path/excerpt_paths dichiarato deve esistere.
    while IFS= read -r exline; do
      expath=$(echo "$exline" | sed -E 's/^[[:space:]-]*//; s/^excerpt_path:[[:space:]]*//; s/[[:space:]]*$//; s/^"//; s/"$//')
      if [ -z "$expath" ] || [ "$expath" = "[]" ] || [ "$expath" = "null" ]; then
        continue
      fi
      if [ ! -s "$skill_path/$expath" ]; then
        echo "  ERRORE: excerpt path '$expath' dichiarato in sources.yaml ma file mancante o vuoto"
        errors=$((errors + 1))
      fi
    done < <(grep -E "^[[:space:]]*(excerpt_path:|- references/estratti/)" "$skill_path/references/sources.yaml" 2>/dev/null || true)
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
