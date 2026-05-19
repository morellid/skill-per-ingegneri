#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml>=6.0",
#   "semver>=3.0",
# ]
# ///
"""Aggrega il frontmatter di ogni skills/<id>/SKILL.md in catalog.yaml.

Single source of truth della categorizzazione user-facing del catalogo skill.
Letto al build time dalla landing (ai-ingegneri.davidemorelli.it).

Usage:
    uv run scripts/build_catalog.py [--check]

Senza flag: scrive catalog.yaml.
--check:    valida senza scrivere, exit 1 su errore.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

import semver
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
AREAS_PATH = REPO_ROOT / "areas.yaml"
SKILLS_DIR = REPO_ROOT / "skills"
CATALOG_PATH = REPO_ROOT / "catalog.yaml"

REQUIRED_FIELDS = ("name", "description", "license", "area", "title", "summary", "version", "status")
OPTIONAL_FIELDS = ("normative_refs", "tags")
VALID_STATUS = {"alpha", "stable"}

LIMITS = {
    "title": 80,
    "summary": 280,
    "normative_ref": 200,
    "tag": 40,
}

TAG_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]*$")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


@dataclass
class ValidationError:
    skill_id: str
    field: str
    message: str

    def __str__(self) -> str:
        return f"  {self.skill_id} :: {self.field}: {self.message}"


def load_areas() -> tuple[list[dict], set[str]]:
    if not AREAS_PATH.exists():
        sys.exit(f"areas.yaml mancante: {AREAS_PATH}")
    data = yaml.safe_load(AREAS_PATH.read_text(encoding="utf-8"))
    areas = data.get("areas", [])
    ids = {a["id"] for a in areas}
    return areas, ids


def parse_frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("frontmatter YAML assente: prime righe non sono '---\\n...\\n---'")
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        raise ValueError(f"YAML non parsabile: {e}") from e
    return data or {}


def validate_skill(skill_id: str, fm: dict, area_ids: set[str]) -> list[ValidationError]:
    errors: list[ValidationError] = []

    for field in REQUIRED_FIELDS:
        if field not in fm or fm[field] in (None, "", []):
            errors.append(ValidationError(skill_id, field, "obbligatorio"))

    if fm.get("name") and fm["name"] != skill_id:
        errors.append(ValidationError(skill_id, "name", f"deve essere '{skill_id}', non '{fm['name']}'"))

    if fm.get("area") and fm["area"] not in area_ids:
        errors.append(ValidationError(skill_id, "area", f"'{fm['area']}' non in areas.yaml"))

    if fm.get("status") and fm["status"] not in VALID_STATUS:
        errors.append(ValidationError(skill_id, "status", f"'{fm['status']}' non in {sorted(VALID_STATUS)}"))

    version = fm.get("version")
    if version:
        try:
            semver.Version.parse(str(version))
        except ValueError as e:
            errors.append(ValidationError(skill_id, "version", f"non semver valido: {e}"))

    title = fm.get("title")
    if isinstance(title, str) and len(title) > LIMITS["title"]:
        errors.append(ValidationError(skill_id, "title", f"max {LIMITS['title']} char, e' {len(title)}"))

    summary = fm.get("summary")
    if isinstance(summary, str) and len(summary) > LIMITS["summary"]:
        errors.append(ValidationError(skill_id, "summary", f"max {LIMITS['summary']} char, e' {len(summary)}"))

    refs = fm.get("normative_refs") or []
    if not isinstance(refs, list):
        errors.append(ValidationError(skill_id, "normative_refs", "deve essere una lista"))
    else:
        for i, ref in enumerate(refs):
            if not isinstance(ref, str):
                errors.append(ValidationError(skill_id, f"normative_refs[{i}]", "deve essere stringa"))
            elif len(ref) > LIMITS["normative_ref"]:
                errors.append(ValidationError(skill_id, f"normative_refs[{i}]", f"max {LIMITS['normative_ref']} char"))

    tags = fm.get("tags") or []
    if not isinstance(tags, list):
        errors.append(ValidationError(skill_id, "tags", "deve essere una lista"))
    else:
        for i, tag in enumerate(tags):
            if not isinstance(tag, str):
                errors.append(ValidationError(skill_id, f"tags[{i}]", "deve essere stringa"))
                continue
            if len(tag) > LIMITS["tag"]:
                errors.append(ValidationError(skill_id, f"tags[{i}]", f"max {LIMITS['tag']} char"))
            if not TAG_PATTERN.match(tag):
                errors.append(ValidationError(skill_id, f"tags[{i}]", f"'{tag}' non e' kebab-case [a-z0-9-]"))

    return errors


def build_catalog(areas: list[dict]) -> tuple[dict, list[ValidationError]]:
    skill_dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())
    area_ids = {a["id"] for a in areas}
    errors: list[ValidationError] = []
    skills_out: list[dict] = []

    for sd in skill_dirs:
        skill_md = sd / "SKILL.md"
        if not skill_md.exists():
            errors.append(ValidationError(sd.name, "SKILL.md", "file mancante"))
            continue
        try:
            fm = parse_frontmatter(skill_md)
        except ValueError as e:
            errors.append(ValidationError(sd.name, "frontmatter", str(e)))
            continue

        errors.extend(validate_skill(sd.name, fm, area_ids))

        skills_out.append({
            "id": sd.name,
            "area": fm.get("area"),
            "title": fm.get("title"),
            "summary": fm.get("summary"),
            "normative_refs": fm.get("normative_refs") or [],
            "version": fm.get("version"),
            "status": fm.get("status"),
            "tags": fm.get("tags") or [],
        })

    by_area = Counter(s["area"] for s in skills_out if s["area"])
    areas_out = [
        {"id": a["id"], "name": a["name"], "order": a["order"], "count": by_area.get(a["id"], 0)}
        for a in sorted(areas, key=lambda x: x["order"])
    ]

    catalog = {
        "schema_version": 1,
        "generated_at": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "areas": areas_out,
        "skills": sorted(skills_out, key=lambda s: s["id"]),
    }
    return catalog, errors


def dump_yaml(data: dict) -> str:
    return yaml.safe_dump(
        data,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
        width=120,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="valida senza scrivere")
    args = parser.parse_args()

    areas, _ = load_areas()
    catalog, errors = build_catalog(areas)

    if errors:
        print(f"Validazione fallita ({len(errors)} errori):", file=sys.stderr)
        for err in errors:
            print(err, file=sys.stderr)
        return 1

    if args.check:
        print(f"OK: {len(catalog['skills'])} skill, {len(catalog['areas'])} aree.")
        return 0

    CATALOG_PATH.write_text(
        "# AUTO-GENERATED da scripts/build_catalog.py. NON modificare a mano.\n"
        "# Single source of truth della categorizzazione user-facing del catalogo skill.\n\n"
        + dump_yaml(catalog),
        encoding="utf-8",
    )
    print(f"Scritto {CATALOG_PATH.relative_to(REPO_ROOT)}: {len(catalog['skills'])} skill, {len(catalog['areas'])} aree.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
