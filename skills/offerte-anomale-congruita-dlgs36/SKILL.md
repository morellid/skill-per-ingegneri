---
name: offerte-anomale-congruita-dlgs36
description: "Supporto documentale al RUP e alla commissione giudicatrice/seggio di gara per l'inquadramento della verifica delle offerte anormalmente basse (giudizio di congruita') e dell'esclusione automatica delle offerte anomale nei contratti pubblici, ai sensi del D.Lgs. 31 marzo 2023, n. 36 (Codice dei contratti pubblici), artt. 110 e 54, con l'art. 108, comma 9. Aiuta a inquadrare il presupposto della verifica di congruita' - valutazione di congruita', serieta', sostenibilita' e realizzabilita' della migliore offerta che appaia anormalmente bassa in base a elementi specifici indicati nel bando, inclusi i costi dichiarati - la richiesta scritta di spiegazioni con termine non superiore a quindici giorni, l'oggetto ammissibile delle spiegazioni, le giustificazioni non ammesse su minimi salariali e costi di sicurezza, e i casi di esclusione per violazione degli obblighi ambientali, sociali e del lavoro, dell'articolo 119, per oneri di sicurezza incongrui o per costo del personale inferiore alle tabelle, oltre agli aiuti di Stato; l'esclusione automatica delle offerte anomale nei contratti sotto la soglia europea con il criterio del prezzo piu' basso, senza interesse transfrontaliero, se le offerte ammesse sono almeno cinque, in deroga all'articolo 110 e con il metodo dell'Allegato II.2 scelto o sorteggiato; e l'indicazione a pena di esclusione dei costi della manodopera e degli oneri di sicurezza nell'offerta economica. Use when a RUP or a tender board must frame the verification of abnormally low tenders and the automatic exclusion of anomalous offers under the Italian D.Lgs. 36/2023; it is a documentary aid and does NOT compute the anomaly threshold or apply the Annex II.2 methods, does NOT draft the request for explanations or the congruity report, does NOT assess the justifications on the merits, and does NOT replace the RUP or the contracting authority."
license: MIT
area: appalti-opere-pubbliche
title: "Offerte anomale e verifica di congruita' (D.Lgs 36/2023 artt. 110, 54)"
summary: "Inquadra la verifica delle offerte anormalmente basse (D.Lgs 36/2023 art. 110): presupposto, spiegazioni (termine 15 gg), giustificazioni non ammesse ed esclusione; l'esclusione automatica sotto soglia (art. 54, Allegato II.2) e i costi di manodopera/sicurezza (art. 108 c. 9)."
normative_refs:
  - "D.Lgs. 31 marzo 2023, n. 36 (Codice dei contratti pubblici) - art. 110 (offerte anormalmente basse), art. 54 (esclusione automatica sotto soglia, All. II.2), art. 108 c. 9 (costi manodopera/sicurezza)"
  - "Richiamati (non riprodotti): Allegato II.2 e Allegato X dir. 2014/24/UE; artt. 41 c. 13, 50 c. 1, 108, 119 D.Lgs 36/2023; art. 107 TFUE; correttivo D.Lgs. 209/2024"
version: 0.1.0-alpha
status: alpha
tags:
  - offerte-anomale
  - verifica-congruita
  - contratti-pubblici
  - dlgs-36-2023
  - rup-commissione
---

# Offerte anomale e verifica di congruita' (D.Lgs 36/2023 artt. 110, 54)

## Quando usare questa skill

Usala quando un **RUP** o una **commissione giudicatrice/seggio di gara** deve **inquadrare** la
**verifica delle offerte anormalmente basse** (giudizio di congruità) o l'**esclusione automatica** delle
offerte anomale nei contratti pubblici, ai sensi del **D.Lgs. 36/2023**:

- **presupposto** e **procedimento** della verifica di congruità (art. 110);
- **giustificazioni** ammesse e non ammesse e **casi di esclusione** (art. 110);
- **esclusione automatica** sotto soglia e **metodo** dell'Allegato II.2 (art. 54);
- **costi della manodopera** e **oneri di sicurezza** nell'offerta economica (art. 108, c. 9).

**Non è** uno strumento che calcola la soglia di anomalia o redige gli atti: è un **supporto documentale**
che inquadra il procedimento, i termini e i casi di esclusione.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-verifica-congruita` | Presupposto, richiesta di spiegazioni, giustificazioni e casi di esclusione delle offerte anormalmente basse (art. 110) |
| `inquadra-esclusione-automatica-sottosoglia` | Presupposti e metodo (Allegato II.2) dell'esclusione automatica sotto soglia e distinzione dall'art. 110 (art. 54) |

## Punti chiave (verificati sul testo)

- **Verifica di congruità** (art. 110, c. 1): la migliore offerta **anormalmente bassa** (per **elementi
  specifici** indicati nel bando, inclusi i costi ex art. 108 c. 9) è valutata per **congruità, serietà,
  sostenibilità, realizzabilità**.
- **Spiegazioni** (art. 110, cc. 2-3): richiesta **scritta**, **termine ≤ 15 giorni**; oggetto: economia
  del processo, soluzioni tecniche/condizioni favorevoli, originalità.
- **Non ammesse** (art. 110, c. 4): giustificazioni su **minimi salariali** e **costi di sicurezza**.
- **Esclusione** (art. 110, c. 5): spiegazioni inadeguate, oppure violazione obblighi ambientali/sociali/
  lavoro, art. 119, **oneri di sicurezza incongrui** (art. 108 c. 9), **costo del personale** sotto le
  tabelle (art. 41 c. 13). **Aiuti di Stato** (c. 6): consultazione e informazione alla Commissione UE.
- **Esclusione automatica** (art. 54): **sotto soglia**, **prezzo più basso**, senza interesse
  transfrontaliero, **lavori/servizi**, **offerte ammesse ≥ 5**, **in deroga** all'art. 110; **metodo**
  dell'**Allegato II.2** scelto o sorteggiato; esclusi gli affidamenti diretti (art. 50 c. 1 a-b).
- **Costi** (art. 108, c. 9): **manodopera** e **oneri di sicurezza** indicati **a pena di esclusione**
  (salvo forniture senza posa e servizi intellettuali).

## Fonti

- **D.Lgs. 31 marzo 2023, n. 36** - **artt. 110, 54 e 108 c. 9** - testo vigente su Normattiva (indice
  pinnato a `!vig=2026-07-17`, SHA256 `0e9a1938...`, codice 23G00044), articoli letti via `caricaArticolo`
  (formato AKN) e trascritti verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** la **soglia di anomalia** né applica i **metodi dell'Allegato II.2**.
- **Non redige** la richiesta di spiegazioni né il **verbale di congruità**; **non valuta** nel merito le
  giustificazioni.
- **Non tratta** la valutazione dell'**offerta tecnica** (skill `oepv-valutatore-offerte-tecniche`) né il
  soccorso istruttorio.

**La skill è un supporto documentale: non sostituisce il RUP o la stazione appaltante, né la lettura degli
artt. 110, 54 e 108 del D.Lgs. 36/2023 e dell'Allegato II.2.**
