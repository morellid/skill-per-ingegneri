# CHANGELOG - carichi-atmosferici-ntc

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha+fix1] - 2026-05-10

### Fixed (source-grounding remediation - issue #94)
- `references/sources.yaml`: aggiunto SHA256 reale di ntc2018-gu42.pdf
  (dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46),
  letto direttamente il 2026-05-10. Circolare 7/2019 portata a binary_path: null
  (PDF non disponibile localmente; estratto verificato sui riferimenti NTC).
- `references/estratti/ntc2018-par-3-3.md`: riscritto interamente dopo lettura
  del PDF (GU pp. 52-56). Corretti errori sistematici di numerazione paragrafi
  ed equazioni presenti nella versione alpha:
  - par. 3.3.1 e' "Velocita' base di riferimento" (non "Pressione del vento")
  - pressione p = q_r*c_e*c_p*c_d e' eq. [3.3.4] par. 3.3.4 (non eq. 3.3.1)
  - q_r e' in par. 3.3.6 eq. [3.3.6] (non par. 3.3.4)
  - c_e e' in par. 3.3.7 eq. [3.3.7] (non eq. 3.3.5)
  - v_b base velocity e' par. 3.3.1 eq. [3.3.1]; v_r = v_b*c_r e' par. 3.3.2 eq. [3.3.2]
  - Aggiunte citazioni pagina GU per ogni paragrafo.
- `references/estratti/ntc2018-par-3-4.md`: riscritto interamente dopo lettura
  del PDF (GU pp. 57-59). Corretti errori sistematici:
  - mu_1 e' in par. 3.4.3.2 Tab. 3.4.II (non par. 3.4.5.2.1 - riferimento inesistente)
  - C_E e' in par. 3.4.4 Tab. 3.4.I (non par. 3.4.3)
  - C_t e' in par. 3.4.5 (non par. 3.4.4)
  - Province Padova, Venezia, Verona spostate da Zona I-Mediterranea a Zona II
    (errore nel dato: il PDF le assegna esplicitamente a Zona II, GU p. 58)
  - Aggiunte citazioni pagina GU per ogni paragrafo.
- `references/estratti/circ-7-2019-c-3-3-3-4.md`: corretto riferimento NTC
  par. 3.4.5.2.1 -> par. 3.4.3.2 (il paragrafo 3.4.5.2.1 non esiste in NTC 2018);
  aggiunta avvertenza che il PDF della Circolare non e' stato scaricato localmente.
- `tasks/lib/carichi_atmosferici.py`: corretti tutti i riferimenti a paragrafi
  ed equazioni NTC nei docstring e nella lista `riferimenti` di ogni funzione.

## [0.1.0-alpha] - 2026-05-08

### Added
- Prima versione alpha della skill (issue #27 SC.4 + SC.5).
- Modulo `tasks/lib/carichi_atmosferici.py` con formule chiuse NTC 2018 par. 3.3 (vento) e par. 3.4 (neve):
  - `velocita_riferimento_vb` (par. 3.3.1 eq. [3.3.1]), `coefficiente_ritorno_cr` (par. 3.3.3 eq. [3.3.3])
  - `pressione_cinetica_qr` (par. 3.3.6 eq. [3.3.6])
  - `coefficiente_esposizione_ce` (par. 3.3.7 eq. [3.3.7]) con tabelle k_r/z_0/z_min (Tab. 3.3.II)
  - `calcola_pressione_vento` (par. 3.3.4 eq. [3.3.4]) end-to-end
  - `carico_neve_al_suolo_qsk` per zone I-Alpina, I-Mediterranea, II, III (par. 3.4.2 eq. [3.4.2]-[3.4.5])
  - `coefficiente_forma_mu1` (par. 3.4.3.2 Tab. 3.4.II)
  - `coefficiente_esposizione_neve_ce` con classi battuta_dai_venti / normale / riparata (par. 3.4.4 Tab. 3.4.I)
  - `calcola_carico_neve` (par. 3.4.1 eq. [3.4.1]) end-to-end
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
