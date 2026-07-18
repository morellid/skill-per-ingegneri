# CHANGELOG - autorizzazione-scarico-acque-reflue-dlgs152

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #366)
- Prima versione della skill di supporto al **tecnico ambientale/impianti** e al **titolare dello
  scarico** per l'**autorizzazione allo scarico di acque reflue** e la **domanda** per gli scarichi
  industriali, ai sensi del **D.Lgs. 3 aprile 2006, n. 152, Parte III, artt. 124 e 125**, nell'area
  `ambiente-territorio-mobilita`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 152/2006** - indice Normattiva pinnato `!vig=2026-07-17` SHA256:
    c2175fe5c9313db1087d444b07e71d727154140d579ffcf6357ababa5d57b45c (codice 006G0171, idGruppo 25).
    Artt. 124 (v3) e 125 (v1) via `caricaArticolo` (formato AKN).
  - Trascrizione verbatim in `references/fonti/dlgs-152-2006-124-125.md` (art. 124 cc. 1-12; art. 125
    cc. 1-2).
- Estratto operativo `references/estratti/autorizzazione-scarico-checklist.md`.
- Due task: `inquadra-autorizzazione-scarico.md` e `inquadra-domanda-scarico-industriale.md`.
- Due esempi: nuovo scarico industriale in pubblica fognatura (competenza, termini, contenuti, rinnovo);
  ampliamento con/senza modifica dello scarico (nuova autorizzazione vs comunicazione).

### Contenuto ancorato al testo
- Criteri generali (124): obbligo di autorizzazione preventiva, titolare/scarico finale/consorzio,
  regimi delle domestiche/fognarie e termali definiti dalle regioni, autorizzazione provvisoria dei
  depuratori, competenza (provincia o ente di governo dell'ambito) e termine di 90 giorni, validita' 4
  anni e rinnovo con regola speciale per le sostanze pericolose dell'art. 108, prescrizioni tecniche,
  spese a carico del richiedente, nuova autorizzazione per trasferimento/cambio d'uso/ampliamento con
  scarico diverso. Domanda scarichi industriali (125): caratteristiche quali/quantitative, volume annuo,
  ricettore, punto di prelievo, sistema di scarico e depurazione, misurazione del flusso, apparecchiature;
  Tab. 3/A: capacita' di produzione e fabbisogno orario d'acqua.

### Scope e limiti
- Non redige la domanda ne' progetta l'impianto di depurazione, non applica i valori limite di emissione
  dell'Allegato 5 (Tab. 1/2/3/3-A/4), non tratta l'AUA/AIA come procedure. Non sostituisce il tecnico, il
  gestore del servizio idrico integrato ne' l'autorita' competente.

### Note di sviluppo
- Distinta da `autorizzazione-integrata-ambientale-dlgs152` (AIA). L'autorizzazione allo scarico puo'
  confluire nell'AUA (DPR 59/2013) per talune imprese. Validazione Livello 2 con tecnico ambientale/
  idraulico.
