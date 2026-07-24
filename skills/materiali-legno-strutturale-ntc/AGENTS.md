# AGENTS.md - materiali-legno-strutturale-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** e al **Direttore dei Lavori** per la **qualificazione** e le
**proprietà** dei materiali e prodotti a base di legno per uso strutturale secondo le **NTC 2018** (DM 17 gennaio
2018), **paragrafo 11.7** (Cap. 11 «Materiali e prodotti per uso strutturale»): generalità/casi di qualificazione
(§11.7.1), proprietà dei materiali, profilo resistente e coefficiente kh (§11.7.1.1), tipi di prodotto e norme di
riferimento (§11.7.2-11.7.6), accettazione in cantiere (§11.7.10).

**È una skill documentale per il tecnico**: inquadra la qualificazione e le proprietà; **non** esegue le verifiche
di progetto (fd = kmod·fk/γM).

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Copre la **qualificazione dei materiali a base di legno** (§11.7, Cap. 11). È
**distinta** da `costruzioni-legno-ntc` (§4.4, **progetto/verifiche**, fd = kmod·fk/γM), da
`costruzioni-legno-zona-sismica-ntc` (§7.7, requisiti **sismici**) e dalle altre skill materiali del Cap. 11
(`muratura-portante-materiali-ntc` §11.10, `controlli-accettazione-cls-acciaio-ntc` §11.2/§11.3): il §11.7 è il
paragrafo specifico per il legno. Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U.
n. 42/2018). Restano fuori scope: adesivi (§11.7.7), collegamenti (§11.7.8) e durabilità (§11.7.9).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-11-7**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 11.7 (pagine PDF 349-350 e seguenti) estratto con `pdftotext -layout` e verificato sull'immagine
  (`pdftoppm -r 150`) per la Tab. 11.7.I, le formule di kh e le condizioni di prova.

Trascrizione in `references/fonti/ntc2018-par-11-7.md`; estratto operativo in
`references/estratti/legno-materiali-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **§11.7.1**: qualificazione §11.1 (caso A CE / B qualificazione / C Linee Guida CSLP); Direttore dei Lavori
  rifiuta le forniture non conformi; laboratori **art. 59 DPR 380/2001** o notificati.
- **§11.7.1.1**: valori caratteristici = **frattile 5%**; prove **300 s** a **20±2 °C** / **UR 65±5%**; profilo
  resistente **Tab. 11.7.I**; **kh** massiccio **min[(150/h)^0,2;1,3]** [11.7.1], lamellare **min[(600/h)^0,1;1,1]**
  [11.7.2].
- **§11.7.2-11.7.6**: massiccio **UNI EN 14081-1** + CE, classi **UNI EN 338**; giunti a dita (caso C); lamellare
  **UNI EN 14080** (classi tavole **> C30** solo a macchina); pannelli **UNI EN 13986** (valori UNI EN 12369).
- **§11.7.10**: identificazione/rintracciabilità e **accettazione in cantiere** a cura del Direttore dei Lavori.

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire** le verifiche di progetto né calcolare le **resistenze di progetto** (fd = kmod·fk/γM).
- Non trattare in dettaglio adesivi (§11.7.7), collegamenti (§11.7.8), durabilità (§11.7.9); non trattare il
  progetto (§4.4), la sismica (§7.7) né l'accettazione di muratura/cls/acciaio (§§11.10/11.2/11.3): rinvia alle
  skill dedicate.

### Cosa fare
- Fornire i casi di qualificazione, le proprietà/profilo resistente e kh, i tipi di prodotto con le norme di
  riferimento e i criteri di accettazione, sempre con rinvio al paragrafo/tabella NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre il par. 11.7. Verificare sull'immagine i valori (frattile 5%; 300 s; 20±2 °C; 65±5%; kh 150/1,3 e
600/1,1; C30; UNI EN 14081/14080/13986/338).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista esperto di legno / Direttore dei Lavori).

## Stato attuale

- Versione: 0.1.0-alpha (closes #466)
- Task files: 2 (`inquadra-proprieta-e-profilo-resistente.md`, `qualifica-prodotti-e-accettazione.md`)
- Esempi: 2 (profilo resistente + coefficiente kh per una trave in legno massiccio; qualificazione di un prodotto
  in legno lamellare)
