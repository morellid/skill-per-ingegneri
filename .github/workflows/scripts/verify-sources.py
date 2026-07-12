#!/usr/bin/env python3
"""Verifica che le fonti dichiarate in skills/<skill>/references/sources.yaml
siano effettivamente raggiungibili e che gli SHA256 dichiarati coincidano
con quelli del binario scaricato.

Uso:
  python3 verify-sources.py                    # verifica tutte le skill
  python3 verify-sources.py skill-a            # verifica solo skill-a
  python3 verify-sources.py skill-a skill-b   # verifica skill-a e skill-b

Eseguito dal workflow .github/workflows/source-grounding.yml. La CI di
GitHub Actions ha rete libera (no allowlist), quindi puo' fare il fetch
reale delle fonti normative italiane (Gazzetta Ufficiale, Normattiva,
eur-lex, MIT, ecc.) e validare la conformita' alla Regola zero
(vedi AGENTS.md).

Comportamento:
  - per ogni voce di sources.yaml con `binary_path` non null, host
    ufficiale e non paywalled, scarica il file dall'URL e calcola lo SHA256;
  - confronta con `sha256:` dichiarato; se mismatch, fail della CI;
  - se `sha256: null` ed e' presente `binary_path`, fail della CI
    (Regola zero: l'hash deve essere reale);
  - se HTTP non risponde, fail della CI con messaggio diagnostico (la
    fonte ufficiale potrebbe essere stata spostata: aggiornare URL).

Eccezioni accettate:
  - `binary_path: null` -> fonte solo URL/online (es. servizio interattivo
    INGV, foglio Excel CSLP). In questo caso `sha256: null` e' coerente
    e il fetch e' saltato.
  - testi a pagamento o fonti dichiaratamente non normative/non ufficiali
    (es. `license: proprietary-paid` o `license: other`) -> skip manuale.
"""

from __future__ import annotations

import hashlib
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

import yaml


REPO_ROOT = Path(__file__).resolve().parents[3]
SKILLS_DIR = REPO_ROOT / "skills"
BINARIES_ROOT = REPO_ROOT / "not_in_repo"

USER_AGENT = (
    "Mozilla/5.0 (compatible; skill-per-ingegneri-CI/1.0; "
    "+https://github.com/morellid/skill-per-ingegneri)"
)
# Alcuni CDN (es. Akamai davanti a gse.it) bloccano UA che dichiarano "bot"
# anche per documenti pubblici scaricabili da browser. Su 401/403/429 cadiamo
# su un UA browser realistico: il documento e' comunque pubblico e l'hash
# dichiarato non cambia in funzione dello UA.
BROWSER_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
)
TIMEOUT_SECONDS = 60
OFFICIAL_HOST_SUFFIXES = (
    "acn.gov.it",
    "adm.gov.it",
    "agenziaentrate.gov.it",
    "anticorruzione.it",
    "arera.it",
    "cnr.it",
    "consiglio.regione.toscana.it",
    "cslp.mit.gov.it",
    "eur-lex.europa.eu",
    "europa.eu",
    "fhwa.dot.gov",
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


def is_official_url(url: str | None) -> bool:
    if not url:
        return False
    host = (urlparse(url).netloc or "").lower()
    if not host:
        return False
    return any(host == suffix or host.endswith(f".{suffix}") for suffix in OFFICIAL_HOST_SUFFIXES)


def load_sources(skill_dir: Path) -> dict | None:
    sources_yaml = skill_dir / "references" / "sources.yaml"
    if not sources_yaml.is_file():
        return None
    with sources_yaml.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _do_fetch(url: str, dest: Path, user_agent: str) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": user_agent})
    with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp, dest.open("wb") as out:
        while True:
            chunk = resp.read(65536)
            if not chunk:
                break
            out.write(chunk)


def fetch(url: str, dest: Path) -> None:
    try:
        _do_fetch(url, dest, USER_AGENT)
    except urllib.error.HTTPError as exc:
        if exc.code in (401, 403, 429):
            print(
                f"  [retry UA] {url} -> HTTP {exc.code} con UA bot, "
                "riprovo con UA browser",
                flush=True,
            )
            _do_fetch(url, dest, BROWSER_USER_AGENT)
        else:
            raise


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
        download_url = src.get("download_url")
        artifact_url = download_url or url
        binary_path = src.get("binary_path")
        declared_hash = src.get("sha256")
        license_type = src.get("license", "unknown")
        md_path = src.get("md_path")

        # Regola zero Step 3: per ogni fonte ufficiale con binary_path non null,
        # md_path deve essere dichiarato e il file deve esistere e non essere vuoto.
        has_binary = binary_path and binary_path not in (None, "null")
        official_url = is_official_url(artifact_url)
        if has_binary and official_url and license_type not in SKIP_FETCH_LICENSES:
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

        if not artifact_url:
            errors.append(f"[{skill_name}/{sid}] binary_path dichiarato ma URL/download_url mancante")
            continue

        # Caso 2: fonti non ufficiali o a pagamento -> niente fetch automatico.
        # La licenza NON e' usata come proxy di autorevolezza: per i binari scaricati
        # si pretende un host ufficiale, salvo fonti dichiaratamente non normative
        # (es. esempi) o testi a pagamento.
        if not official_url:
            if license_type in SKIP_FETCH_LICENSES:
                print(f"[{skill_name}/{sid}] host non ufficiale e licenza {license_type} - skip fetch (verifica manuale)")
                continue
            errors.append(
                f"[{skill_name}/{sid}] URL non ufficiale per fonte con binary_path: {artifact_url} "
                "(usare il sito ufficiale dell'ente, non mirror o portali terzi)"
            )
            continue

        if license_type in SKIP_FETCH_LICENSES:
            print(f"[{skill_name}/{sid}] licenza {license_type} - skip fetch (verifica manuale)")
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

        # Caso 3.5: fonte deliberatamente non fetchabile dal CI.
        # Valido SOLO per host che bloccano gli IP datacenter di GitHub Actions
        # (es. gse.it dietro Akamai blocca i runner Azure). Il campo richiede
        # una motivazione esplicita (stringa non vuota). Tutti gli altri check
        # restano attivi: hash reale, md_path presente, binary_path dichiarato.
        # Limite accettato: niente check di drift automatico per questa entry,
        # l'aggiornamento e' a cura dell'agent (verifica manuale + nuovo SHA256).
        ci_fetch_blocked = src.get("ci_fetch_blocked")
        if ci_fetch_blocked:
            reason = str(ci_fetch_blocked).strip()
            if not reason or reason.lower() in ("true", "yes", "1"):
                errors.append(
                    f"[{skill_name}/{sid}] ci_fetch_blocked richiede motivazione esplicita "
                    "(stringa con la ragione del blocco, non un boolean)"
                )
                continue
            print(
                f"[{skill_name}/{sid}] CI fetch SKIPPED (ci_fetch_blocked): {reason}",
                flush=True,
            )
            continue

        # Caso 4: fetch e verifica hash
        local_path = BINARIES_ROOT / Path(binary_path).relative_to(
            "not_in_repo"
        ) if binary_path.startswith("not_in_repo/") else BINARIES_ROOT / Path(binary_path).name
        local_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            print(f"[{skill_name}/{sid}] fetch {artifact_url}", flush=True)
            fetch(artifact_url, local_path)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
            errors.append(f"[{skill_name}/{sid}] fonte non raggiungibile: {artifact_url} ({exc})")
            continue

        actual = sha256_of(local_path)
        if actual != declared_hash:
            errors.append(
                f"[{skill_name}/{sid}] HASH MISMATCH: dichiarato={declared_hash[:16]}... "
                f"calcolato={actual[:16]}... per {artifact_url}"
            )
        else:
            print(f"[{skill_name}/{sid}] OK ({actual[:16]}...)")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"ERRORE: {SKILLS_DIR} non esiste", file=sys.stderr)
        return 1

    skill_names = sys.argv[1:]
    if skill_names:
        skill_dirs: list[Path] = []
        for name in skill_names:
            d = SKILLS_DIR / name
            if not d.is_dir():
                print(f"ERRORE: skill '{name}' non trovata in {SKILLS_DIR}", file=sys.stderr)
                return 1
            skill_dirs.append(d)
    else:
        skill_dirs = sorted(
            d for d in SKILLS_DIR.iterdir()
            if d.is_dir() and not d.name.startswith("_")
        )

    all_errors: list[str] = []
    for skill_dir in skill_dirs:
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
    scope = ", ".join(skill_names) if skill_names else "tutte le skill"
    print(f"OK: tutte le fonti raggiungibili e gli hash combaciano ({scope}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
