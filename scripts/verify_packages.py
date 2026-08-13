#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml>=6.0",
# ]
# ///
"""Verifica che gli zip prodotti da build_releases.sh siano pacchetti validi.

Non si limita a "il file esiste e non e' vuoto": apre ogni archivio e controlla
che sia davvero installabile su claude.ai/customize/skills.

Controlli, per ogni skill dichiarata in catalog.yaml:
  1. dist/<id>.zip esiste
  2. l'archivio ha una sola directory root, ed e' <id>/
  3. contiene <id>/SKILL.md e <id>/LICENSE
  4. non contiene nessuno dei path esclusi (not_in_repo/, __pycache__/, ...)
  5. l'elenco delle entry coincide con l'albero sorgente skills/<id>

Il punto 5 e' quello che intercetta un pacchetto formalmente valido ma che ha
perso per strada una directory (tasks/, references/): senza di esso lo zip
passerebbe il check pur essendo inutilizzabile.

Lo stesso contratto e' implementato in JS nel repo del sito
(skill-per-ingegneri-landing, scripts/lib/skill-package.mjs), che genera gli zip
scaricabili dal catalogo. Se i due divergono, entrambi i lati falliscono.

Uso: uv run scripts/verify_packages.py
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
DIST_DIR = REPO_ROOT / "dist"
CATALOG = REPO_ROOT / "catalog.yaml"

# Stesse esclusioni delle --exclude di build_releases.sh.
EXCLUDED_DIRS = frozenset({"not_in_repo", "__pycache__"})
EXCLUDED_FILES = frozenset({".DS_Store"})
EXCLUDED_SUFFIXES = (".pyc",)

REQUIRED_ENTRIES = ("SKILL.md", "LICENSE")


def is_excluded(rel_path: str) -> bool:
    segments = rel_path.split("/")
    return (
        any(s in EXCLUDED_DIRS for s in segments)
        or segments[-1] in EXCLUDED_FILES
        or rel_path.endswith(EXCLUDED_SUFFIXES)
    )


def expected_entries(skill_dir: Path) -> set[str]:
    """Entry attese: i file della skill, piu' la LICENSE del repo che
    build_releases.sh copia dentro ogni pacchetto."""
    entries = {
        p.relative_to(skill_dir).as_posix()
        for p in skill_dir.rglob("*")
        if p.is_file() and not is_excluded(p.relative_to(skill_dir).as_posix())
    }
    entries.add("LICENSE")
    return entries


def verify_package(zip_path: Path, skill_id: str, expected: set[str]) -> list[str]:
    problems: list[str] = []

    try:
        with zipfile.ZipFile(zip_path) as archive:
            if archive.testzip() is not None:
                return [f"archivio corrotto: {archive.testzip()}"]
            names = [n for n in archive.namelist() if not n.endswith("/")]
    except zipfile.BadZipFile as err:
        return [f"archivio illeggibile: {err}"]

    if not names:
        return ["archivio vuoto"]

    roots = {n.split("/")[0] for n in names}
    if roots != {skill_id}:
        problems.append(f'root attesa "{skill_id}/", trovate: {", ".join(sorted(roots))}')

    prefix = f"{skill_id}/"
    inner = {n[len(prefix):] for n in names if n.startswith(prefix)}

    for required in REQUIRED_ENTRIES:
        if required not in inner:
            problems.append(f"manca {skill_id}/{required}")

    for rel in sorted(inner):
        if is_excluded(rel):
            problems.append(f"entry esclusa presente: {skill_id}/{rel}")

    missing = sorted(expected - inner)
    extra = sorted(inner - expected)
    if missing:
        problems.append(f"entry mancanti ({len(missing)}): {', '.join(missing[:5])}")
    if extra:
        problems.append(f"entry inattese ({len(extra)}): {', '.join(extra[:5])}")

    return problems


def main() -> int:
    catalog = yaml.safe_load(CATALOG.read_text(encoding="utf8"))
    skill_ids: list[str] = [s["id"] for s in catalog["skills"]]

    if not DIST_DIR.is_dir():
        print(f"ERRORE: {DIST_DIR} non esiste. Esegui prima ./scripts/build_releases.sh", file=sys.stderr)
        return 1

    errors: list[str] = []
    for skill_id in skill_ids:
        zip_path = DIST_DIR / f"{skill_id}.zip"
        if not zip_path.is_file():
            errors.append(f"{skill_id}: zip non prodotto ({zip_path.name})")
            continue

        skill_dir = SKILLS_DIR / skill_id
        if not skill_dir.is_dir():
            errors.append(f"{skill_id}: dichiarata in catalog.yaml ma skills/{skill_id}/ non esiste")
            continue

        for problem in verify_package(zip_path, skill_id, expected_entries(skill_dir)):
            errors.append(f"{skill_id}: {problem}")

    # Zip prodotti per skill che non sono a catalogo: segnalati, non bloccanti.
    orphans = sorted({p.stem for p in DIST_DIR.glob("*.zip")} - set(skill_ids))
    for orphan in orphans:
        print(f"NOTA: {orphan}.zip prodotto ma non presente in catalog.yaml")

    if errors:
        print(f"\n{len(errors)} problemi di impacchettamento:\n", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(f"OK: {len(skill_ids)} pacchetti verificati")
    return 0


if __name__ == "__main__":
    sys.exit(main())
