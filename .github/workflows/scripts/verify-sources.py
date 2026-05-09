#!/usr/bin/env python3
"""Verifica che le fonti dichiarate in skills/<skill>/references/sources.yaml
siano effettivamente raggiungibili e che gli SHA256 dichiarati coincidano
con quelli del binario scaricato.

Eseguito dal workflow .github/workflows/source-grounding.yml. La CI di
GitHub Actions ha rete libera (no allowlist), quindi puo' fare il fetch
reale delle fonti normative italiane (Gazzetta Ufficiale, Normattiva,
eur-lex, MIT, ecc.) e validare la conformita' alla Regola zero
(vedi AGENTS.md).

Comportamento:
  - per ogni voce di sources.yaml con `binary_path` non null e licenza
    libera, scarica il file dall'URL e calcola lo SHA256;
  - confronta con `sha256:` dichiarato; se mismatch, fail della CI;
  - se `sha256: null` ed e' presente `binary_path`, fail della CI
    (Regola zero: l'hash deve essere reale);
  - se HTTP non risponde, fail della CI con messaggio diagnostico (la
    fonte ufficiale potrebbe essere stata spostata: aggiornare URL).

Eccezioni accettate:
  - `binary_path: null` -> fonte solo URL/online (es. servizio interattivo
    INGV, foglio Excel CSLP). In questo caso `sha256: null` e' coerente
    e il fetch e' saltato.
  - licenza non libera (es. proprietary-paid per testi a pagamento) ->
    skip (rinvio a verifica manuale).
"""

from __future__ import annotations

import hashlib
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[3]
SKILLS_DIR = REPO_ROOT / "skills"
BINARIES_ROOT = REPO_ROOT / "not_in_repo"

USER_AGENT = (
    "Mozilla/5.0 (compatible; skill-per-ingegneri-CI/1.0; "
    "+https://github.com/morellid/skill-per-ingegneri)"
)
TIMEOUT_SECONDS = 60


def load_sources(skill_dir: Path) -> dict | None:
    sources_yaml = skill_dir / "references" / "sources.yaml"
    if not sources_yaml.is_file():
        return None
    with sources_yaml.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def fetch(url: str, dest: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp, dest.open("wb") as out:
        while True:
            chunk = resp.read(65536)
            if not chunk:
                break
            out.write(chunk)


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        while True:
            chunk = fh.read(65536)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def verify_skill(skill_dir: Path) -> list[str]:
    """Returns a list of error messages (empty if all OK)."""
    errors: list[str] = []
    skill_name = skill_dir.name
    data = load_sources(skill_dir)
    if data is None:
        return errors

    sources = data.get("sources", []) or []
    for src in sources:
        sid = src.get("id", "<unknown>")
        url = src.get("url")
        binary_path = src.get("binary_path")
        declared_hash = src.get("sha256")
        license_type = src.get("license", "unknown")
        md_path = src.get("md_path")

        # Regola zero Step 3: per ogni fonte pubblica con binary_path non null,
        # md_path deve essere dichiarato e il file deve esistere e non essere vuoto.
        is_free_license = license_type in ("public-domain", "cc-by", "cc-by-nc")
        has_binary = binary_path and binary_path not in (None, "null")
        if has_binary and is_free_license:
            if not md_path or md_path in (None, "null"):
                errors.append(
                    f"[{skill_name}/{sid}] md_path mancante: per fonti pubbliche con binary_path "
                    "occorre committare references/fonti/<id>.md (Regola zero Step 3)"
                )
            else:
                target = skill_dir / md_path
                if not target.is_file() or target.stat().st_size == 0:
                    errors.append(
                        f"[{skill_name}/{sid}] md_path '{md_path}' dichiarato ma file mancante o vuoto "
                        "(Regola zero Step 3)"
                    )

        # Caso 1: niente binario dichiarato -> solo URL online, skip fetch
        if not binary_path or binary_path in (None, "null"):
            # se c'e' anche un sha256 dichiarato non null, e' incoerente
            if declared_hash and declared_hash not in (None, "null"):
                errors.append(
                    f"[{skill_name}/{sid}] binary_path null ma sha256 non null: "
                    "incoerenza in sources.yaml"
                )
            continue

        # Caso 2: licenze non libere -> skip fetch automatico
        if license_type not in ("public-domain", "cc-by", "cc-by-nc"):
            print(f"[{skill_name}/{sid}] licenza {license_type} non-libera - skip fetch (verifica manuale)")
            continue

        # Caso 3: hash placeholder -> already caught dal job check-no-placeholders,
        # ma ricontroliamo per robustezza
        placeholders = (
            "REPLACE_WHEN_DOWNLOADED",
            "REPLACE_WITH_ACTUAL_HASH",
            "PENDING_FETCH",
            "TODO_HASH",
        )
        if declared_hash in placeholders or declared_hash in (None, "null", ""):
            errors.append(
                f"[{skill_name}/{sid}] sha256 mancante o placeholder ('{declared_hash}'): "
                "Regola zero richiede hash reale"
            )
            continue

        if not url:
            errors.append(f"[{skill_name}/{sid}] binary_path dichiarato ma URL mancante")
            continue

        # Caso 4: fetch e verifica hash
        local_path = BINARIES_ROOT / Path(binary_path).relative_to(
            "not_in_repo"
        ) if binary_path.startswith("not_in_repo/") else BINARIES_ROOT / Path(binary_path).name
        local_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            print(f"[{skill_name}/{sid}] fetch {url}", flush=True)
            fetch(url, local_path)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
            errors.append(f"[{skill_name}/{sid}] fonte non raggiungibile: {url} ({exc})")
            continue

        actual = sha256_of(local_path)
        if actual != declared_hash:
            errors.append(
                f"[{skill_name}/{sid}] HASH MISMATCH: dichiarato={declared_hash[:16]}... "
                f"calcolato={actual[:16]}... per {url}"
            )
        else:
            print(f"[{skill_name}/{sid}] OK ({actual[:16]}...)")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"ERRORE: {SKILLS_DIR} non esiste", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        if skill_dir.name.startswith("_"):
            continue  # es. _archived
        errors = verify_skill(skill_dir)
        if errors:
            print(f"=== {skill_dir.name}: {len(errors)} errori ===")
            for e in errors:
                print(f"  {e}")
        all_errors.extend(errors)

    print()
    if all_errors:
        print(f"FAIL: {len(all_errors)} violazioni source-grounding (Regola zero)")
        for e in all_errors:
            print(f"::error::{e}")
        return 1
    print("OK: tutte le fonti raggiungibili e gli hash combaciano.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
