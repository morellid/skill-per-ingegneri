# AGENTS.md - relazione-tecnica-requisiti-minimi-dlgs192

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **tecnico** (progettista, direttore dei lavori) per la **relazione tecnica
di progetto attestante la rispondenza ai requisiti minimi di contenimento dei consumi energetici**
(la "relazione ex legge 10"): contenuto, deposito, sistemi alternativi, asseverazione a fine lavori,
controlli e sanzioni, ai sensi del **D.Lgs. 19 agosto 2005, n. 192, art. 8** (con l'art. 15 cc. 1,
3, 4). Target: ingegneri e architetti come progettisti o direttori dei lavori.

**E' una skill documentale per il tecnico**: inquadra l'adempimento e la sua collocazione; **non
redige** la relazione, **non esegue** i calcoli/verifiche, non sostituisce il progettista/DL.

## Nota sull'area e sulla complementarita'

Area **energia-incentivi**. Distinta da `attestato-prestazione-energetica-dlgs192` (APE, art. 6) e
complementare a `trasmittanza-termica-opache-dm2015` (verifiche numeriche del DM 26/6/2015). Questa
copre l'**adempimento della relazione tecnica** (art. 8).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-192-2005-art8-15**: D.Lgs. 192/2005, pagina indice Normattiva pinnata a `!vig=2026-07-17`
  (hash `bfaa5336...`; codice 005G0219 - stesso indice della skill APE, ripinnato a oggi). Art. 8
  (versione 5, idGruppo 1) e art. 15 (versione 4, idGruppo 3) caricati via `caricaArticolo` (formato
  AKN) e trascritti verbatim (dell'art. 15: cc. 1, 3, 4).

Trascrizione in `references/fonti/dlgs-192-2005-art8-15.md`; estratto operativo in
`references/estratti/relazione-tecnica-checklist.md`.

## Punti chiave (verificati sul testo)

- **Relazione** redatta dai **progettisti** (calcoli e verifiche), depositata dal **proprietario in
  doppia copia** con la DIA/titolo abilitativo (art. 8 c. 1); **esclusioni**: pompa di calore <= 15
  kW, sostituzione generatore sotto soglia DM 37/2008.
- **Sistemi alternativi** ad alta efficienza: valutazione di fattibilita' documentata per nuove
  costruzioni e ristrutturazioni importanti (c. 1-bis).
- **Asseverazione + AQE** del **direttore dei lavori** a fine lavori, pena l'inefficacia della fine
  lavori (c. 2); **controlli** del Comune in corso d'opera o entro 5 anni (cc. 3-5).
- **Sanzioni**: dichiarazione sostitutiva di atto notorio (art. 15 c. 1); professionista 700-4200
  euro per relazione non conforme (c. 3); direttore dei lavori 1000-6000 euro per omessa
  asseverazione (c. 4).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** la relazione tecnica ne' l'asseverazione/AQE.
- Non **eseguire** i calcoli/verifiche energetiche (DM 26/6/2015) ne' riprodurre gli **schemi** di
  relazione del decreto MiSE.
- Non trattare l'**APE** (art. 6), l'**esercizio impianti** (art. 7) ne' i commi 2 e 5-10 dell'art.
  15: rinvio.

### Cosa fare
- Stabilire se la relazione e' dovuta (esclusioni), chi la redige, cosa contiene (incl. sistemi
  alternativi), come/quando si deposita; inquadrare asseverazione a fine lavori, controlli e
  sanzioni, sui commi degli artt. 8 e 15.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 192/2005 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere gli artt. 8 e 15, verificando le modifiche segnalate dai doppi tondi `(( ))` (es. D.Lgs.
48/2020) e l'evoluzione del decreto attuativo MiSE sugli schemi di relazione.

## Validatori

- Non ancora assegnato (Livello 2 con termotecnico / certificatore energetico).

## Stato attuale

- Versione: 0.1.0-alpha (closes #346)
- Task files: 2 (`inquadra-relazione-deposito.md`, `inquadra-asseverazione-sanzioni.md`)
- Esempi: 2 (relazione per nuova costruzione con sistemi alternativi ed esclusione PdC 12 kW; fine
  lavori senza asseverazione: inefficacia, sanzione al DL, controlli del Comune)
