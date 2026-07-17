# CHANGELOG - vigilanza-sanzioni-abusi-edilizi-dpr380

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #294)
- Prima versione della skill di supporto al **regime repressivo degli abusi edilizi**, ai sensi del
  **D.P.R. 6 giugno 2001, n. 380** (T.U. Edilizia), Titolo IV, artt. **27, 31, 33, 34, 44**, nell'area
  `edilizia-urbanistica-catasto`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.P.R. 6 giugno 2001, n. 380** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: bac3f7b170cfd122936873c835b3f728e7880d058bd98ad45f55b94ba89a632f
    (codice 001G0429). Artt. 27 (grp8, v3), 31 (grp9, v8), 33 (grp9, v4), 34 (grp9, v8), 44 (grp9, v5)
    via `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dpr-380-2001-artt-27-31-33-34-44.md`.
- Estratto operativo `references/estratti/abusi-edilizi-checklist.md`.
- Due task: `inquadra-abuso-misura.md` e `ricostruisci-vigilanza-termini.md`.
- Due esempi: abuso in assenza di permesso (artt. 27/31); parziale difformità (art. 34).

### Contenuto ancorato al testo
- Art. 27 vigilanza (sospensione lavori, provvedimenti 45 gg, sequestro 15 gg, demolizione aree
  vincolate/Soprintendente 180 gg); art. 31 assenza/totale difformità (ingiunzione, 90 gg/proroga 240
  gg, acquisizione gratuita area ≤ 10 volte sup. utile abusiva, sanzione 2.000-20.000 euro, demolizione
  a spese, ordine del giudice); art. 33 ristrutturazione abusiva (doppio dell'aumento di valore,
  contributo dovuto); art. 34 parziale difformità (triplo del costo di produzione/valore venale); art.
  44 sanzioni penali (ammenda fino a 10.329; arresto fino a 2 anni + ammenda 5.164-51.645; lottizzazione
  e confisca).

### Scope e limiti
- Non adotta i provvedimenti né quantifica le sanzioni, non tratta la sanatoria (artt. 36/36-bis) né le
  tolleranze (art. 34-bis) - cfr. `modulistica-edilizia-unificata` (Salva Casa). Artt. 30, 32 citati e
  non trascritti. Non sostituisce Comune/SUE, tecnico o legale.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.P.R. 380/2001 pinnato (nuovo hash) e
  rileggere gli artt. 27, 31, 33, 34, 44 (testo tra `(( ))`).
- Validazione Livello 2 con tecnico/ufficio abusi o legale amministrativista.
