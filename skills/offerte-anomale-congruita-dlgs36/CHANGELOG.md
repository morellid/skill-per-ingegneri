# CHANGELOG - offerte-anomale-congruita-dlgs36

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-18

### Added (closes #374)
- Prima versione della skill di supporto al **RUP** e alla **commissione giudicatrice/seggio di gara** per
  l'inquadramento della **verifica delle offerte anormalmente basse** (giudizio di congruità) e
  dell'**esclusione automatica** delle offerte anomale nei contratti pubblici, ai sensi del **D.Lgs.
  36/2023, artt. 110 e 54** (con l'art. 108, comma 9), nell'area `appalti-opere-pubbliche`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 36/2023** - indice Normattiva pinnato `!vig=2026-07-17` SHA256:
    0e9a193836e379cb33cb6daf1a5a988c608eb9559d84b91a841d9ed9791a62af (codice 23G00044, idGruppo 6 e 17).
    Artt. 54 (v2), 108 (v6, comma 9) e 110 (v2) via `caricaArticolo` (header X-Requested-With, formato
    AKN).
  - Trascrizione verbatim in `references/fonti/dlgs-36-2023-110-54-108.md` (testo vigente).
- Estratto operativo `references/estratti/offerte-anomale-checklist.md`.
- Due task: `inquadra-verifica-congruita.md` e `inquadra-esclusione-automatica-sottosoglia.md`.
- Due esempi: verifica di congruità in gara OEPV sopra soglia (art. 110); esclusione automatica sotto
  soglia a prezzo più basso con 8 offerte (art. 54).

### Contenuto ancorato al testo
- Offerte anormalmente basse (art. 110): valutazione di congruità/serietà/sostenibilità/realizzabilità
  della migliore offerta e indicazione degli elementi specifici nel bando (c. 1); richiesta scritta di
  spiegazioni con termine non superiore a 15 giorni (c. 2); oggetto ammissibile delle spiegazioni (c. 3);
  giustificazioni non ammesse su minimi salariali e costi di sicurezza (c. 4); casi di esclusione -
  obblighi ambientali/sociali/lavoro (allegato X dir. 2014/24/UE), art. 119, oneri di sicurezza incongrui,
  costo del personale sotto le tabelle dell'art. 41 c. 13 (c. 5); aiuti di Stato con informazione alla
  Commissione UE (c. 6). Esclusione automatica (art. 54): sotto soglia UE, prezzo più basso, senza
  interesse transfrontaliero, lavori/servizi, offerte ammesse ≥ 5, in deroga all'art. 110, metodo
  dell'Allegato II.2 scelto o sorteggiato, esclusi gli affidamenti diretti dell'art. 50 c. 1 lett. a-b
  (cc. 1-2; comma 3 abrogato dal D.Lgs. 209/2024). Costi della manodopera e oneri di sicurezza indicati a
  pena di esclusione (art. 108 c. 9).

### Scope e limiti
- Non calcola la soglia di anomalia né applica i metodi dell'Allegato II.2, non redige la richiesta di
  spiegazioni né il verbale di congruità, non valuta nel merito le giustificazioni. Non sostituisce il RUP
  né la stazione appaltante.

### Note di sviluppo
- Complementare a `oepv-valutatore-offerte-tecniche` (che precede la verifica di congruità) e alle altre
  skill D.Lgs 36/2023. Validazione Livello 2 con RUP/esperto di contratti pubblici.
