# AGENTS.md - offerte-anomale-congruita-dlgs36

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **RUP** e alla **commissione giudicatrice/seggio di gara** per l'inquadramento
della **verifica delle offerte anormalmente basse** (giudizio di congruità) e dell'**esclusione
automatica** delle offerte anomale nei contratti pubblici, ai sensi del **D.Lgs. 36/2023, artt. 110 e 54**
(con l'art. 108, comma 9). Target: RUP, commissioni giudicatrici, uffici gare, tecnici delle stazioni
appaltanti.

**E' una skill documentale per il tecnico**: inquadra il procedimento, i termini, le giustificazioni
ammesse/non ammesse e i casi di esclusione; **non calcola** la soglia di anomalia, **non applica** i
metodi dell'Allegato II.2 e **non redige** gli atti.

## Nota sull'area e sulla complementarita'

Area **appalti-opere-pubbliche**. Complementare, non sovrapposta, a `oepv-valutatore-offerte-tecniche`
(valutazione dell'offerta tecnica, che precede la verifica di congruità), `rup-responsabile-unico-progetto-dlgs36`,
`garanzie-appalti-pubblici-dlgs36`, `subappalto-contratti-pubblici-dlgs36` e alle altre skill D.Lgs
36/2023, con cui condivide la fonte (indice Normattiva del D.Lgs 36/2023, codice 23G00044).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-36-2023-110-54-108**: D.Lgs. 36/2023, indice Normattiva pinnato a `!vig=2026-07-17` (hash
  `0e9a1938...`; codice 23G00044, idGruppo 6 art. 54 e 17 artt. 108/110). Artt. 54 (v2), 108 (v6, comma 9)
  e 110 (v2) letti via `caricaArticolo` (header X-Requested-With, formato AKN) e trascritti verbatim
  (testo vigente).

Trascrizione in `references/fonti/dlgs-36-2023-110-54-108.md`; estratto in
`references/estratti/offerte-anomale-checklist.md`.

## Punti chiave (verificati sul testo)

- **Verifica di congruità** (art. 110): presupposto (c. 1), spiegazioni con termine ≤ 15 gg (cc. 2-3),
  giustificazioni non ammesse (c. 4), casi di esclusione (c. 5), aiuti di Stato (c. 6).
- **Esclusione automatica** (art. 54): sotto soglia, prezzo più basso, senza interesse transfrontaliero,
  lavori/servizi, offerte ammesse ≥ 5, in deroga all'art. 110; metodo dell'Allegato II.2 scelto o
  sorteggiato; esclusi gli affidamenti diretti (art. 50 c. 1 a-b); comma 3 abrogato (D.Lgs. 209/2024).
- **Costi** (art. 108, c. 9): manodopera e oneri di sicurezza indicati a pena di esclusione (salvo
  forniture senza posa e servizi intellettuali).

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** la **soglia di anomalia** né applicare i **metodi dell'Allegato II.2**.
- Non **redigere** la richiesta di spiegazioni né il **verbale di congruità**; non **valutare** nel merito
  le giustificazioni.
- Non trattare la valutazione dell'**offerta tecnica** (skill `oepv-valutatore-offerte-tecniche`) né il
  soccorso istruttorio.

### Cosa fare
- Inquadrare quando scatta la verifica di congruità (art. 110) o l'esclusione automatica (art. 54); il
  procedimento, i termini, le giustificazioni e i casi di esclusione; il ruolo dei costi ex art. 108 c. 9.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 36/2023 pinnato a nuovo `!vig=` (nuovo hash) e rileggere gli
artt. 54, 108 e 110 (via `caricaArticolo` con header `X-Requested-With: XMLHttpRequest` sulla sessione
aperta da `caricaDettaglioAtto`), verificando le modifiche dei doppi tondi `(( ))` (ulteriori correttivi
dopo il D.Lgs. 209/2024) e l'eventuale aggiornamento dell'Allegato II.2.

## Validatori

- Non ancora assegnato (Livello 2 con RUP/esperto di contratti pubblici).

## Stato attuale

- Versione: 0.1.0-alpha (closes #374)
- Task files: 2 (`inquadra-verifica-congruita.md`, `inquadra-esclusione-automatica-sottosoglia.md`)
- Esempi: 2 (offerta sospetta anomala in gara OEPV sopra soglia - verifica di congruità art. 110; lavori
  sotto soglia a prezzo più basso con 8 offerte - esclusione automatica art. 54)
