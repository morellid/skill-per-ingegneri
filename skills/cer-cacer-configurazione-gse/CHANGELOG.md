# CHANGELOG - cer-cacer-configurazione-gse

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-06

### Added
- Prima versione alpha della skill `cer-cacer-configurazione-gse`.
- Task files:
  - `valuta-perimetro-configurazione.md` - verifica cabina primaria + scelta AID/GAC/CER.
  - `redigi-statuto-cer.md` - bozza statuto/atto costitutivo CER (DM 7/12/2023 art. 4-5).
  - `simula-autoconsumo-condiviso.md` - calcolo semplificato energia condivisa, TIP, TR, contributo PNRR.
  - `predisponi-qualifica-gse.md` - checklist documentale per qualifica al servizio CACER.
- Fonti normative catalogate in `references/sources.yaml`:
  - D.Lgs. 199/2021 art. 30-32
  - DM MASE 7 dicembre 2023 n. 414
  - Delibera ARERA 727/2022/R/eel (TIAD)
  - Regole Operative CACER del GSE (Allegato 1)
- Esempi:
  - `cer-comune-piccolo-pnrr` - CER su Comune < 5.000 ab. con cumulo TIP + contributo PNRR.
  - `gac-condominio-fotovoltaico-tetto` - Gruppo Autoconsumatori condominiale con FV in copertura.

### Note di sviluppo
- Skill non ancora validata da dominio terzo (energy manager / EGE indipendente).
- Da considerare draft finche' non passa validazione Livello 2 (vedi `methodology/validazione.md`).
- Verificare aggiornamenti TIAD ARERA e Regole Operative GSE prima dell'uso operativo: il framework CACER e' stato oggetto di aggiornamenti frequenti dopo l'avvio del servizio (gennaio 2024).
