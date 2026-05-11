# CHANGELOG - predimensionamento-flessione-ca-ntc

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1-alpha] - 2026-05-11

### fix(source-grounding)
- Scaricati e letti i PDF NTC 2018 (not_in_repo/ntc2018-gu42.pdf, SHA256
  dda1e397...) e Circolare MIT 7/2019 (not_in_repo/circ-7-2019.pdf, SHA256
  f7c3b8d1...). Chiude issue #108.
- Aggiunto `references/fonti/ntc2018-dm-17-01-2018.md`: trascrizione fedele dei
  paragrafi 4.1.1.1, 4.1.2.1.1.1, 4.1.2.1.1.3, 4.1.2.1.2.1, 4.1.2.3.4.1,
  4.1.2.3.4.2 del PDF NTC 2018 letto.
- Aggiunto `references/fonti/circ-7-2019-mit.md`: trascrizione fedele dei
  paragrafi C4.1.2.1.2.1 e C4.1.2.3.4.2 del PDF Circolare 7/2019 letto.
- Riscritti `references/estratti/ntc2018-par-4-1-2.md` e
  `references/estratti/circ-7-2019-c-4-1-2.md` da testo del PDF letto
  (non piu' da training data).
- Corretto errore nel numero equazione: `fcd = alpha_cc * fck / gamma_c` e'
  l'eq. **[4.1.3]** del NTC 2018 (non 4.1.4 come indicato nella v0.1.0).
  L'eq. [4.1.4] e' `fctd = fctk / gamma_c` (resistenza a trazione cls).
- Corretto riferimento limite x/d <= 0,45: deriva da **NTC 2018 par. 4.1.1.1**
  (ridistribuzione momenti nelle travi continue), NON dalla Circolare 7/2019
  C4.1.2 (che non contiene tale valore numerico - verificato con grep sul PDF).
  Il messaggio di avvertenza nel codice e nei riferimenti ora cita la fonte
  corretta con il contesto preciso.
- Aggiornati commenti in `flessione_ca.py` con riferimenti ai paragrafi NTC
  verificati sul testo PDF (Es = 200000 MPa da EN 1992-1-1 / NTC par. 11.3.2.1;
  lambda=0,8 eta=1 da EN 1992-1-1 par. 3.1.7 per Classe 1).
- Aggiunto `md_path` per entrambe le fonti in `sources.yaml`.
- SHA256 reali calcolati (`sha256sum`) sostituiscono i placeholder.
- 34/34 test passano.

## [0.1.0-alpha] - 2026-05-09

### Added
- Prima versione alpha della skill (issue #28 SC.6).
- Modulo `tasks/lib/flessione_ca.py` con formule chiuse NTC 2018 par. 4.1.2.1 e 4.1.2.3.4.2:
  - `resistenza_calcestruzzo_fcd` (eq. [4.1.3]): f_cd = alpha_cc * fck / gamma_c, con rifiuto fck > 50 MPa
  - `resistenza_acciaio_fyd` (par. 4.1.2.1.1.3): f_yd = fyk / gamma_s
  - `deformazione_snervamento_eyd`: eps_yd = f_yd / Es (Es = 200000 MPa default)
  - `asse_neutro_x`: equilibrio Cc = T con stress-block (lambda = 0.8) -> x = (A_s f_yd) / (lambda b f_cd)
  - `deformazione_acciaio_eps_s`: eps_s = eps_cu (d - x) / x
  - `calcola_m_rd` (par. 4.1.2.3.4.2): M_Rd = A_s * f_yd * z, con z = d - 0.4 x; verifica duttilita' (snervamento acciaio + x/d <= 0.45)
- CLI con input JSON, output JSON.
- Test suite `tasks/lib/test_flessione_ca.py`: 34 test, 8 classi, copertura formule materiali/equilibrio/deformazione/end-to-end/monotonia/avvertenza zeta/CLI.
- Task file: `tasks/calcola-m-rd.md`.
- Estratti normativi: `references/estratti/ntc2018-par-4-1-2.md`, `references/estratti/circ-7-2019-c-4-1-2.md`.
- Esempi: `examples/caso-conforme-300x500-3phi16-C25-30/` (conforme), `examples/caso-problematico-sovra-armata/` (problematico).
- Catalogo fonti: `references/sources.yaml` (NTC 2018 + Circ. 7/2019 MIT, hash da calcolare al fetch).

### Note di sviluppo
- Skill non ancora validata da dominio terzo.
- Validazione Livello 2 (confronto numerico vs manuali standard di tecnica delle costruzioni e/o software certificato su almeno 5 casi reali) da eseguire prima del release stabile.
- Da considerare draft finche' non passa Livello 2 (vedi `methodology/validazione.md`).
