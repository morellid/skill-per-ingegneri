# AGENTS.md - garanzie-appalti-pubblici-dlgs36

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'inquadramento delle **garanzie** negli appalti pubblici:
**garanzia provvisoria** (art. 106) e **garanzia definitiva** con le coperture
assicurative (art. 117) del **D.Lgs. 36/2023** (Codice dei contratti pubblici).
Target: ingegneri/architetti e tecnici (RUP, progettisti, DL, operatori economici).

**È una skill documentale**: inquadra tipi, importi, riduzioni, svincoli e coperture;
**non calcola** gli importi del caso concreto, **non redige** le fideiussioni/polizze
ne' gli schemi tipo (DM), non sostituisce la stazione appaltante, il RUP, il garante
o l'operatore economico.

## Nota sull'area

Area **appalti-opere-pubbliche**. Complementare alle altre skill sul Codice dei
contratti pubblici (`specifiche-tecniche-ict-appalti-dlgs36`, `bandi-tipo-anac-checker`,
`oepv-valutatore-offerte-tecniche` e, nelle PR aperte, subappalto/modifiche-varianti):
questa copre le **garanzie** (provvisoria e definitiva) e le coperture assicurative.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-36-2023-artt-106-117**: D.Lgs. 36/2023, pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `0e9a1938...`; codice 23G00044). Artt. 106 (versione 2,
  idGruppo 16) e 117 (versione 1, idGruppo 18), flagTipoArticolo 2, caricati via
  `caricaArticolo` e trascritti verbatim.

Trascrizione in `references/fonti/dlgs-36-2023-artt-106-117.md`; estratto operativo in
`references/estratti/garanzie-appalti-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 106** (garanzia provvisoria): 2% del valore (riducibile all'1%,
  incrementabile al 4%; c. 1); cauzione/fideiussione (cc. 1-3); requisiti rinuncia
  preventiva escussione + art. 1957 c.c. + operativita' 15 gg + efficacia >= 180 gg
  (cc. 4-5); copre mancata aggiudicazione/sottoscrizione (c. 6); riduzioni 30%/50%/
  10%/fino 20% con cumulabilita' (c. 8); svincolo automatico alla firma, 30 gg per i
  non aggiudicatari (cc. 7, 10); non si applica a progettazione/PSC/supporto RUP (c. 11).
- **Art. 117** (garanzia definitiva): 10% dell'importo (c. 1); maggiorazione per
  ribasso > 10% (1 punto/punto) e > 20% (2 punti/punto) (c. 2); oggetto adempimento +
  risarcimento, cessa al collaudo/CRE, riduzioni art. 106 c. 8 (c. 3); sostituzione
  con ritenuta 10% nei lavori (c. 4); escussione (c. 5); mancata costituzione =
  decadenza + incameramento provvisoria (c. 6); svincolo progressivo fino all'80%
  (c. 8); polizze CAR + RCT (massimale 5%, min 500k/max 5M; c. 10), decennale postuma
  20-40% (c. 11), schemi tipo (c. 12), RTI (c. 13), esonero (c. 14).

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** gli importi/massimali del caso concreto: fornire solo percentuali
  e regole (2%, 1%-4%, 10%, maggiorazione, 80%, 5%, 20-40%, 500k-5M).
- Non **redigere** fideiussioni/cauzioni/polizze ne' gli **schemi tipo** (DM c. 12).
- Non **inventare** riduzioni o massimali fuori dal testo degli artt. 106/117.

### Cosa fare
- **Individuare** quale garanzia si applica, l'importo/regola, le riduzioni cumulabili
  e lo svincolo, con rinvio alla stazione appaltante/RUP/garante per il calcolo e la
  stipula.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 36/2023 pinnato a nuovo `!vig=` (nuovo
hash) e rileggere gli artt. 106 e 117 (testo tra `(( ))` = modifiche successive, es.
correttivo D.Lgs. 209/2024).

## Validatori

- Non ancora assegnato (Livello 2 con esperto di contratti pubblici / RUP).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`inquadra-garanzia-provvisoria.md`, `inquadra-garanzia-definitiva.md`)
- Esempi: 2 (garanzia provvisoria con riduzioni - art. 106; garanzia definitiva maggiorazione/svincolo - art. 117)
