# CHANGELOG - cedimenti-edometrici-ntc

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-09

### Added
- Prima versione alpha della skill (issue #32 SC.10).
- Modulo `tasks/lib/cedimenti.py` con formule chiuse di compressione monodimensionale per singolo strato omogeneo:
  - `cedimento_oc` - ramo OC: Delta h = h0/(1+e0) * Cr * log10(sigma_f/sigma_0)
  - `cedimento_nc` - ramo NC: Delta h = h0/(1+e0) * Cc * log10(sigma_f/sigma_0)
  - `calcola_cedimento` - end-to-end con dispatch automatico OC / NC / transizione, calcolo OCR, deformazione media, avvertenza per epsilon > 10%
- CLI con input JSON, output JSON.
- Test suite `tasks/lib/test_cedimenti.py`: 28 test, 5 classi, copertura raccordi/monotonia/validazione input/CLI.
- Task file: `tasks/calcola-cedimento.md`.
- Estratti normativi e didattici: `references/estratti/ntc2018-par-6-2.md`, `references/estratti/circ-7-2019-c-6-2.md`, `references/estratti/formulazione-edometrica-classica.md`.
- Esempi: `examples/caso-conforme-strato-argilla-OC-transizione/` (conforme), `examples/caso-problematico-ocr-minore-1/` (problematico).
- Catalogo fonti: `references/sources.yaml` (NTC 2018 + Circ. 7/2019 MIT, hash da calcolare al fetch; Lancellotta come riferimento didattico non incorporato).

### Note di sviluppo
- Skill non ancora validata da dominio terzo.
- Validazione Livello 2 (confronto numerico vs casi Lancellotta/Cestari/Holtz-Kovacs e/o software geotecnico certificato come Plaxis, GeoStudio, Settle3D su almeno 5 casi reali) da eseguire prima del release stabile.
- Da considerare draft finche' non passa Livello 2 (vedi `methodology/validazione.md`).
