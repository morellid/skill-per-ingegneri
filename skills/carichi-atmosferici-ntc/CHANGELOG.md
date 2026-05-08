# CHANGELOG - carichi-atmosferici-ntc

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-08

### Added
- Prima versione alpha della skill (issue #27 SC.4 + SC.5).
- Modulo `tasks/lib/carichi_atmosferici.py` con formule chiuse NTC 2018 par. 3.3 (vento) e par. 3.4 (neve):
  - `velocita_riferimento_vb` (eq. 3.3.2), `coefficiente_ritorno_cr` (eq. 3.3.3), `pressione_cinetica_qr` (eq. 3.3.4)
  - `coefficiente_esposizione_ce` (eq. 3.3.5) con tabelle k_r/z_0/z_min per categorie I/II/III/IV/V (Tab. 3.3.II)
  - `calcola_pressione_vento` (eq. 3.3.1) end-to-end
  - `carico_neve_al_suolo_qsk` per zone I-Alpina, I-Mediterranea, II, III (par. 3.4.2 eq. 3.4.1-3.4.4)
  - `coefficiente_forma_mu1` (par. 3.4.5.2.1)
  - `coefficiente_esposizione_neve_ce` con classi battuta_dai_venti / normale / riparata (Tab. 3.4.I)
  - `calcola_carico_neve` (eq. 3.4.1) end-to-end
- CLI con sottocomandi `vento` e `neve`, input JSON, output JSON.
- Test suite `tasks/lib/test_carichi_atmosferici.py`: 46 test, 12 classi, copertura raccordi/clamp/monotonia/validazione input/CLI.
- Task files: `tasks/calcola-vento.md`, `tasks/calcola-neve.md`.
- Estratti normativi: `references/estratti/ntc2018-par-3-3.md`, `references/estratti/ntc2018-par-3-4.md`, `references/estratti/circ-7-2019-c-3-3-3-4.md`.
- Esempi: `examples/caso-conforme-zona1-pianura-cat-II/` (conforme), `examples/caso-problematico-quota-oltre-1500/` (problematico).
- Catalogo fonti: `references/sources.yaml` (NTC 2018 + Circ. 7/2019 MIT, hash da calcolare al fetch).

### Note di sviluppo
- Skill non ancora validata da dominio terzo.
- Validazione Livello 2 (confronto numerico vs esempi Circolare C3.3/C3.4 o software di calcolo certificato su almeno 5 + 5 casi reali) da eseguire prima del release stabile.
- Da considerare draft finche' non passa Livello 2 (vedi `methodology/validazione.md`).
