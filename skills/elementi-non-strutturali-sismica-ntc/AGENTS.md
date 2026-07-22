# AGENTS.md - elementi-non-strutturali-sismica-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento della progettazione sismica degli
elementi strutturali secondari, degli elementi costruttivi non strutturali** (tamponature, controsoffitti,
parapetti, rivestimenti) **e degli impianti** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafi 7.2.3 e
7.2.4**. Target: ingegneri strutturisti.

**E' una skill documentale per il tecnico**: fornisce i criteri (limite 15% per gli elementi secondari,
incrementi 2/1,4 per irregolarita', soglie 30%/10% per gli impianti) e la forza Fa = Sa*Wa/qa; **non calcola** Fa,
**non esegue** le verifiche e **non determina** Sa e qa.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. **Complementa** `criteri-modellazione-sismica-ntc` (§7.2.6, eccentricita'
accidentale), `regolarita-strutturale-sismica-ntc` (§7.2.1), `spostamenti-interpiano-sld-ntc` (§7.3.6.1) e
`spettro-risposta-ntc` (§3.2). E' **distinta**: nessuna di queste tratta gli elementi secondari/non strutturali/
impianti del §7.2.3-7.2.4. Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n.
42/2018). Restano fuori scope il calcolo di Fa/domanda (§7.3) e la determinazione di Sa e qa.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-7-2-3-7-2-4**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17
  gennaio 2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill
  NTC). Par. 7.2.3-7.2.4 estratti con `pdftotext -layout` (p. GU 212) e trascritti verbatim; la formula [7.2.1] e
  le costanti (15%, 2, 1,4, 30%, 10%) verificate anche sull'immagine renderizzata della pagina PDF 216 (pdftoppm).

Trascrizione in `references/fonti/ntc2018-par-7-2-3-7-2-4.md`; estratto operativo in
`references/estratti/elementi-non-strutturali-checklist.md`.

## Punti chiave (verificati sul testo)

- **Elementi secondari** (§7.2.3): rigidezza/resistenza orizzontale trascurate; progettati per carichi verticali +
  seguire gli spostamenti allo SLC (§7.3.3.3/§7.3.4); non trasformano irregolare in regolare (§7.2.1); contributo
  totale a rigidezza/resistenza orizzontale **<= 15%** degli elementi primari.
- **Elementi non strutturali** (§7.2.3): capacita' > domanda per ogni SL (§7.3.6); responsabilita' progettista/DL/
  fornitore-installatore; irregolarita' in pianta -> eccentricita' accidentale **x2** (§7.2.6); in altezza ->
  domanda sugli elementi verticali **x1,4**; forza **Fa = (Sa*Wa)/qa** [7.2.1] (Sa adimensionalizzata §3.2.1, Wa
  peso, qa fattore di comportamento; Sa e qa da documenti di comprovata validita').
- **Impianti** (§7.2.4): capacita' > domanda (§7.3.6); responsabilita' produttore/installatore/progettista
  strutturale; **studio specifico** se l'impianto eccede il **30%** del carico permanente del campo di solaio (o
  del pannello) o il **10%** del carico permanente totale della struttura.

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** Fa ne' **eseguire** le verifiche; non **determinare** Sa e qa (documenti di comprovata
  validita').
- Non **confondere** la formula (Fa = Sa*Wa/qa: Sa per Wa, il tutto diviso qa) ne' i coefficienti (15%, 2, 1,4,
  30%, 10%).
- Non **calcolare** la domanda/gli spostamenti (§7.3) ne' lo spettro (§3.2).

### Cosa fare
- Fornire criteri e formula (Fa = Sa*Wa/qa) con i limiti e le soglie, sempre con rinvio al paragrafo/formula NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere i par. 7.2.3-7.2.4. Verificare la formula [7.2.1] (Fa = Sa*Wa/qa, operatori
sull'immagine) e le costanti (15%, 2, 1,4, 30%, 10%).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #427)
- Task files: 2 (`inquadra-forza-elementi-non-strutturali.md`, `inquadra-elementi-secondari-impianti.md`)
- Esempi: 2 (forza Fa su una tamponatura con irregolarita' in pianta; elementi secondari con limite 15% e
  impianto pesante oltre la soglia del 30%)
