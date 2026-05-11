#!/usr/bin/env bash
# Scarica le fonti ufficiali dichiarate nei sources.yaml e verifica gli hash.
# I binari vengono depositati in not_in_repo/ (fuori dal controllo git).
# Uso: ./scripts/fetch-sources.sh [<nome-skill>]
#      Se nome-skill omesso: scarica per tutte le skill

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/skills"
BINARIES_ROOT="$REPO_ROOT/not_in_repo"

mkdir -p "$BINARIES_ROOT"

# Nota: questa e' una versione minimale che richiede python per parsare YAML.
# Se python non disponibile, usare yq (https://github.com/mikefarah/yq) o equivalente.

fetch_for_skill() {
  local skill_path="$1"
  local skill_name
  skill_name=$(basename "$skill_path")
  local sources_file="$skill_path/references/sources.yaml"

  if [ ! -f "$sources_file" ]; then
    echo "  Skip: $skill_name (no sources.yaml)"
    return 0
  fi

  echo "=== Fetch per skill: $skill_name ==="

  python3 <<EOF
import yaml
import hashlib
import os
import urllib.request
import sys
from urllib.parse import urlparse

sources_file = "$sources_file"
binaries_root = "$BINARIES_ROOT"
skill_name = "$skill_name"

OFFICIAL_HOST_SUFFIXES = (
    "acn.gov.it",
    "agenziaentrate.gov.it",
    "anticorruzione.it",
    "arera.it",
    "cnr.it",
    "consiglio.regione.toscana.it",
    "cslp.mit.gov.it",
    "eur-lex.europa.eu",
    "europa.eu",
    "funzionepubblica.gov.it",
    "garanteprivacy.it",
    "gazzettaufficiale.it",
    "gse.it",
    "ingv.it",
    "ispettorato.gov.it",
    "italiadomani.gov.it",
    "lavoro.gov.it",
    "mase.gov.it",
    "mimit.gov.it",
    "mit.gov.it",
    "normattiva.it",
    "regione.toscana.it",
    "rgs.mef.gov.it",
    "salute.gov.it",
    "statoregioni.it",
)
SKIP_FETCH_LICENSES = {"proprietary-paid", "other"}


def is_official_url(url):
    if not url:
        return False
    host = (urlparse(url).netloc or "").lower()
    return any(host == suffix or host.endswith("." + suffix) for suffix in OFFICIAL_HOST_SUFFIXES)

with open(sources_file) as f:
    data = yaml.safe_load(f)

for src in data.get("sources", []):
    sid = src.get("id", "unknown")
    url = src.get("url")
    download_url = src.get("download_url")
    artifact_url = download_url or url
    license_type = src.get("license", "unknown")
    binary_path = src.get("binary_path")
    expected_hash = src.get("sha256")

    if not binary_path or binary_path == "null":
        print(f"  [{sid}] nessun binary_path - skip")
        continue

    if not artifact_url:
        print(f"  [{sid}] ERRORE: binary_path dichiarato ma URL/download_url mancante")
        sys.exit(1)

    if not is_official_url(artifact_url):
        if license_type in SKIP_FETCH_LICENSES:
            print(f"  [{sid}] host non ufficiale e licenza {license_type} - skip fetch automatico")
            continue
        print(f"  [{sid}] ERRORE: URL non ufficiale per fonte con binary_path: {artifact_url}")
        sys.exit(1)

    if license_type in SKIP_FETCH_LICENSES:
        print(f"  [{sid}] licenza {license_type} - skip fetch automatico")
        continue

    # Normalizza path
    if binary_path.startswith("not_in_repo/"):
        local_file = os.path.join(binaries_root, binary_path[len("not_in_repo/"):])
    else:
        local_file = os.path.join(binaries_root, os.path.basename(binary_path))

    os.makedirs(os.path.dirname(local_file), exist_ok=True)

    if os.path.exists(local_file):
        # Verifica hash
        with open(local_file, "rb") as f:
            actual_hash = hashlib.sha256(f.read()).hexdigest()
        if expected_hash and actual_hash != expected_hash:
            print(f"  [{sid}] HASH MISMATCH! atteso={expected_hash[:16]}... attuale={actual_hash[:16]}...")
        else:
            print(f"  [{sid}] gia' presente, hash ok")
        continue

    # Download
    try:
        print(f"  [{sid}] download da {artifact_url} ...", end=" ")
        req = urllib.request.Request(artifact_url, headers={"User-Agent": "Mozilla/5.0 (compatible; skill-per-ingegneri-fetch/1.0)"})
        with urllib.request.urlopen(req, timeout=60) as resp, open(local_file, "wb") as out:
            out.write(resp.read())
        with open(local_file, "rb") as f:
            actual_hash = hashlib.sha256(f.read()).hexdigest()
        if expected_hash and actual_hash != expected_hash:
            print(f"HASH MISMATCH! atteso={expected_hash[:16]}... attuale={actual_hash[:16]}...")
            sys.exit(1)
        else:
            print("OK")
    except Exception as e:
        print(f"ERRORE: {e}")
EOF
}

if [ $# -eq 0 ]; then
  for skill_dir in "$SKILLS_DIR"/*/; do
    if [ -d "$skill_dir" ]; then
      fetch_for_skill "$skill_dir"
      echo ""
    fi
  done
else
  fetch_for_skill "$SKILLS_DIR/$1"
fi
