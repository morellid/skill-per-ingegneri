# CHANGELOG - cbam-declarant-trimestrale

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-18

### Added

- Prima versione alpha della skill di supporto al dichiarante CBAM autorizzato per la **fase definitiva** del CBAM (dal 1° gennaio 2026), ai sensi del Reg. (UE) 2023/956 come modificato dal Reg. (UE) 2025/2083 (Omnibus CBAM).
- Fonti normative consultate e committate:
  - `references/fonti/reg-ue-2023-956-cbam-consolidato.md` - testo consolidato 20/10/2025 del Reg. CBAM (artt. fase definitiva, Allegati I, III, IV, V, VII), SHA256 verificato.
  - `references/fonti/reg-ue-2025-2083-cbam-omnibus.md` - testo integrale del Reg. Omnibus dell'8/10/2025 (considerando + dispositivo + allegati), SHA256 verificato.
  - `references/fonti/circ-adm-36-2025-cbam.md` - Circolare ADM 36/2025 del 24/12/2025 (avvio fase definitiva, codici TARIC).
  - `references/fonti/avviso-adm-cbam-211025.md` - Avviso ADM del 21/10/2025 (conseguenze mancata qualifica).
- Estratti curati in `references/estratti/` per orientamento operativo:
  - articoli della fase definitiva Reg. 2023/956 organizzati per fase del ciclo del dichiarante (ambito, qualifica, dichiarazione, certificati, sanzioni, tempistiche);
  - considerando chiave Reg. 2025/2083;
  - codici TARIC e formalismo Y128 dalla Circolare ADM 36/2025;
  - conseguenze mancata conformita' dall'Avviso ADM.
- Quattro task files in `tasks/`:
  - `check-qualifica-e-deroghe.md` - verifica della necessita' di qualifica + applicabilita' delle deroghe (Y128 vs Y134-Y137-Y237-Y238).
  - `plan-equilibrio-trimestrale.md` - pianificazione dell'obbligo trimestrale 50 % di certificati CBAM (Art. 22 §2, dal 2027).
  - `draft-dichiarazione-cbam-annuale.md` - check-list per la dichiarazione annuale Art. 6 (prima volta 2027 per anno 2026).
  - `assess-rischio-sanzionatorio.md` - mappa sanzioni Art. 26 §§1, 1bis, 2, 2bis, 4bis.
- Due esempi in `examples/`:
  - 1 caso conforme (importatore stabilito UE, settore alluminio, sotto soglia con superamento previsto).
  - 1 caso problematico (rappresentante doganale indiretto privo di qualifica, importatore terzo > soglia).
- Aggiunto host `adm.gov.it` alla lista `OFFICIAL_HOST_SUFFIXES` in `scripts/fetch-sources.sh` e `.github/workflows/scripts/verify-sources.py` per supportare le fonti ADM.

### Note di sviluppo

- Skill non ancora validata da dominio terzo. Per promozione a 0.2 e' necessaria validazione di Livello 2 da responsabile compliance dogane / consulente CBAM di importatore diverso dall'autore.
- Da considerare draft finche' non passa validazione Livello 2 (vedi `methodology/validazione.md`).
- Gli atti delegati e di esecuzione richiamati dal Reg. CBAM consolidato (artt. 2 §§10-11, 2bis §3, 7 §7, 9 §5, 14 §6, 18 §3, 20 §§5bis-6, 21 §3, 27 §6) sono in continua evoluzione: la skill rinvia al testo dell'atto pubblicato in GU UE e non sostituisce la consultazione del Registro CBAM e della pagina MASE "EU ETS - Italia :: CBAM".
