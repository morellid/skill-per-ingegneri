# AGENTS.md - resistenza-fuoco-strutture-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento della resistenza al fuoco delle
strutture** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 3.6.1 (Incendio)**: definizioni,
richieste di prestazione, classi, procedura di analisi e verifiche. Target: ingegneri strutturisti e
professionisti antincendio.

**E' una skill documentale per il tecnico**: fornisce le definizioni (R/E/I), la struttura del carico
d'incendio [3.6.1], i livelli di prestazione (Tab. 3.5.IV), le classi e le curve nominali; **non calcola** il
carico d'incendio, **non esegue** le analisi termiche/meccaniche e **non** fornisce le proprietà dei materiali
ad alta temperatura.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Copre il compito di **progettazione strutturale in caso di incendio** che le
skill "costruzioni di X" (§4.x) rinviano al §3.6.1. È **distinta** da
`prevenzione-incendi-attivita-procedimenti-dpr151` (procedimenti amministrativi VVF ai sensi del DPR
151/2011): questa skill riguarda la resistenza al fuoco come requisito strutturale. Condivide con le altre
skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018). Restano fuori scope: il calcolo del
carico d'incendio (DM 9/3/2007), le classi/livelli delle regole tecniche VVF (D.Lgs 139/2006, DM 3/8/2015) e i
materiali ad alta temperatura (Eurocodici parte 1-2).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-3-6-1**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 3.6.1 estratto con `pdftotext -layout` (pp. 62-64) e trascritto verbatim.

Trascrizione in `references/fonti/ntc2018-par-3-6-1.md`; estratto operativo in
`references/estratti/resistenza-fuoco-checklist.md`.

## Punti chiave (verificati sul testo)

- **Definizioni** (§3.6.1.1): R (capacità portante), E (tenuta), I (isolamento); qf,d = qf·δq1·δq2·δn [3.6.1]
  (δq1 ≥ 1,00, δq2 ≥ 0,80, δn ≥ 0,20; dettaglio nel DM 9/3/2007).
- **Prestazioni** (Tab. 3.5.IV): Livelli I-V; per attività VVF classi da D.Lgs 139/2006.
- **Classi** (§3.6.1.3): 15, 20, 30, 45, 60, 90, 120, 180, 240, 360 minuti.
- **Curve nominali** (§3.6.1.5.1): standard θg = 20 + 345·log10(8t+1) [3.6.2]; idrocarburi [3.6.3]; esterna
  [3.6.4].
- **Verifica** (§3.6.1.5.4): resistenza meccanica per il tempo pari alla classe (combinazione eccezionale).

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** il carico d'incendio (fattori δni nel DM 9/3/2007) né **eseguire** le analisi
  termiche/meccaniche; non **fornire** le proprietà dei materiali ad alta temperatura (Eurocodici parte 1-2).
- Non **stabilire** le classi/livelli specifici delle regole tecniche VVF (D.Lgs 139/2006, DM 3/8/2015); non
  **trattare** i procedimenti amministrativi antincendio (→ skill DPR 151/2011).

### Cosa fare
- Fornire definizioni, prestazioni, classi, formule delle curve nominali e criteri di verifica, sempre con
  rinvio al paragrafo/tabella/formula NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 3.6.1. Verificare la formula [3.6.1] (fattori δ), le classi (15-360) e le
curve nominali [3.6.2]-[3.6.4].

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista/professionista antincendio).

## Stato attuale

- Versione: 0.1.0-alpha (closes #401)
- Task files: 2 (`inquadra-prestazioni-classi-fuoco.md`, `inquadra-analisi-verifica-fuoco.md`)
- Esempi: 2 (curva nominale standard a t=30/60 min per R60; livello di prestazione II e classe per attività
  soggetta a VVF)
