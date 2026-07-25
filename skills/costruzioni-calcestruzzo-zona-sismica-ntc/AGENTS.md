# AGENTS.md - costruzioni-calcestruzzo-zona-sismica-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per la **progettazione sismica delle costruzioni di calcestruzzo
armato** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.4** (Cap. 7 «Progettazione per azioni sismiche»):
caratteristiche dei materiali (§7.4.2), tipologie strutturali e fattori di comportamento (§7.4.3), dimensionamento e
verifica con la gerarchia delle resistenze (§7.4.4), dettagli costruttivi CD"A"/CD"B" (§7.4.6, come contesto).

**È una skill documentale per il tecnico**: inquadra il quadro progettuale sismico del c.a.; **non** esegue il progetto
né le verifiche di dettaglio.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Copre la **progettazione sismica del c.a.** (§7.4, Cap. 7). È **distinta** da:
- `costruzioni-calcestruzzo-ntc` (§4.1, **progetto ordinario non sismico** del c.a.);
- `fattore-comportamento-q-sismica-ntc` (§7.3.1, **macchina generale del q** e Tab. 7.3.II): il §7.4.3.2 fornisce gli
  **αu/α1** e le regole di scelta CD specifiche del c.a.;
- le altre skill sismiche per materiale: `costruzioni-acciaio-zona-sismica-ntc` (§7.5),
  `costruzioni-composte-zona-sismica-ntc` (§7.6), `costruzioni-legno-zona-sismica-ntc` (§7.7),
  `costruzioni-muratura-zona-sismica-ntc` (§7.8), `ponti-zona-sismica-ntc` (§7.9), `isolamento-sismico-ntc` (§7.10).
Il §7.4 è il tassello **c.a.** della serie sismica per materiale. Condivide la fonte GU con le altre skill NTC.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-7-4**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 7.4 (pagine PDF 227-236) estratto con `pdftotext -layout`; i valori numerici e le formule (tipologie, αu/α1,
  55%/65%, [7.4.1]-[7.4.4]) verificati sull'immagine (`pdftoppm -r 150`) delle pagine PDF 228/229/230.

Trascrizione in `references/fonti/ntc2018-par-7-4.md`; estratto operativo in
`references/estratti/ca-sismica-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **§7.4.2**: acciaio **B450C**; **B450A** solo **Ø 5-10 mm** (reti/tralicci) o trasversale se plasticizzazione
  impedita/secondari/non dissipativo.
- **§7.4.3.1**: telaio/pareti **taglio base ≥ 65%**; miste **> 50%** ai telai → equiv. telai; pendolo inverso **≥ 50%
  massa**; monopiano **N ≤ 30%** cls; deformabili torsionalmente **r²/ls² ≥ 1**; pareti estese debolmente armate
  **T ≤ TC** (CD"B").
- **§7.4.3.2**: q via §7.3.1/Tab. 7.3.II; pareti accoppiate se momento base **≥ 20%**; **αu/α1** telai **1,1/1,2/1,3**,
  pareti **1,0/1,1/1,2**; travi a spessore → **CD"B"**.
- **§7.4.4**: **γRd** da **Tab. 7.2.I**; travi taglio da **capacità flessionale amplificata**; pilastri compressione
  **≤ 55% (CD"A") / 65% (CD"B")** solo cls; nodo **ΣMc,Rd ≥ γRd·ΣMb,Rd** [7.4.4]; duttilità travi **μφ** [7.4.3],
  **μφ = 2μd − 1**; CD"A" armature **±45°** [7.4.1]/[7.4.2].

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire** il progetto né le **verifiche di dettaglio** (RES/DUT complete) né riprodurre i **dettagli
  costruttivi** (§7.4.6): il dettaglio numerico resta nella norma.
- Non trattare il **progetto ordinario non sismico** (§4.1) né la macchina generale del **q** (§7.3.1): rinvia alle
  skill dedicate.
- Non inventare valori: ogni numero/formula deve essere rintracciabile in `references/fonti/ntc2018-par-7-4.md`.

### Cosa fare
- Fornire il quadro progettuale sismico del c.a.: scelta della tipologia, del fattore di comportamento (αu/α1) e della
  CD; applicazione della gerarchia delle resistenze a travi/pilastri/nodi, sempre con rinvio al sotto-paragrafo/formula
  NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e riestrarre
il par. 7.4. Verificare sull'immagine i valori (B450C/B450A 5-10 mm; 65%/50%/30%; r²/ls²≥1; αu/α1 1,1-1,3 e 1,0-1,2;
55%/65%; [7.4.1]-[7.4.4]).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista esperto di progettazione sismica del c.a.).

## Stato attuale

- Versione: 0.1.0-alpha (closes #474)
- Task files: 2 (`inquadra-tipologie-e-fattore-comportamento.md`, `applica-gerarchia-delle-resistenze.md`)
- Esempi: 2 (scelta di tipologia e fattore di comportamento per un edificio a telaio; gerarchia delle resistenze al
  nodo trave-pilastro)
