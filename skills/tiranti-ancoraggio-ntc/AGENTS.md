# AGENTS.md - tiranti-ancoraggio-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista geotecnico e strutturale** per l'**inquadramento del progetto e della
verifica dei tiranti di ancoraggio** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 6.6**: criteri
di progetto, verifica SLU a sfilamento, aspetti costruttivi e prove di carico. Target: ingegneri geotecnici e
strutturisti.

**E' una skill documentale per il tecnico**: fornisce i criteri, la procedura di verifica (Ed ≤ Rad,
Rad = Rak/γR), i fattori di correlazione (Tab. 6.6.II/III) e le regole delle prove di carico; **non calcola**
la resistenza allo sfilamento, **non dimensiona** il tirante e **non esegue** le prove.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. **Complementa** `opere-sostegno-ntc` (§6.5, muri e paratie): le paratie
tirantate richiedono la verifica degli ancoraggi (§6.5.3.1.1 rinvia al calcolo degli ancoraggi), e il §6.6
fornisce la verifica a sfilamento e le prove. Condivide con le altre skill NTC la stessa fonte (PDF GU del
S.O. n. 8 alla G.U. n. 42/2018). Restano fuori scope i sistemi di ancoraggio come prodotti (§11.5.2), la
progettazione strutturale dell'armatura e la progettazione sismica (Cap. 7).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-6-6**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 6.6 estratto con `pdftotext -layout` (pp. 197-199) e trascritto verbatim.

Trascrizione in `references/fonti/ntc2018-par-6-6.md`; estratto operativo in
`references/estratti/tiranti-ancoraggio-checklist.md`.

## Punti chiave (verificati sul testo)

- **Criteri** (§6.6.1): provvisori/permanenti, attivi/passivi; conferma sperimentale con prove sempre
  necessaria.
- **Verifica SLU** (§6.6.2): Ed ≤ Rad, combinazione A1+M1+R3; Rad = Rak/γR (Tab. 6.6.I: 1,1 temporanei / 1,2
  permanenti).
- **Rak**: (a) prove [6.6.1] con ξa1/ξa2 (Tab. 6.6.II: 1,5/1,4/1,3 e 1,5/1,3/1,2); (b) calcolo [6.6.2] con
  ξa3/ξa4 (Tab. 6.6.III: 1,80..1,60 e 1,80..1,55). Analitico → M1.
- **Aspetti costruttivi** (§6.6.3): sistemi qualificati (§11.5.2), fori ≥ nominale, tesatura dopo presa.
- **Prove** (§6.6.4): di progetto 1/2/3/7/8/10 per <30/31-50/51-100/101-200/201-500/>500; in corso d'opera su
  tutti a 1,2·Pd (SLE).

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** la resistenza allo sfilamento né **dimensionare** il tirante o l'armatura; non **valutare**
  Ra,m/Ra,c al posto del progettista.
- Non **eseguire** né **interpretare** le prove di carico; non **riprodurre** i sistemi di ancoraggio come
  prodotti (§11.5.2), le paratie/muri (§6.5) né la progettazione sismica (Cap. 7).

### Cosa fare
- Fornire criteri, procedura di verifica (Ed ≤ Rad, Rad = Rak/γR), fattori di correlazione (Tab. 6.6.II/III) e
  regole delle prove, sempre con rinvio al paragrafo/tabella NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 6.6. Verificare γR (Tab. 6.6.I: 1,1/1,2), i fattori ξ (Tab. 6.6.II/III) e i
numeri delle prove (§6.6.4.1: 1/2/3/7/8/10).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere geotecnico/strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #399)
- Task files: 2 (`inquadra-verifica-sfilamento-tiranti.md`, `inquadra-criteri-prove-tiranti.md`)
- Esempi: 2 (verifica a sfilamento di un tirante permanente con Rak da prove; numero di prove per 120
  ancoraggi e prova in corso d'opera a 1,2·Pd)
