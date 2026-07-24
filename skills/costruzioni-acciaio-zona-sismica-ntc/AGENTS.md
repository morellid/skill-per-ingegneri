# AGENTS.md - costruzioni-acciaio-zona-sismica-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento delle regole generali** delle
costruzioni di acciaio in zona sismica secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.5**:
caratteristiche dei materiali e fattore di sovraresistenza γov (§7.5.1), tipologie strutturali (§7.5.2.1),
fattori di comportamento q0 e αu/α1 (§7.5.2.2), regole generali per gli elementi dissipativi e classe della
sezione trasversale (§7.5.3, Tab. 7.5.I). Target: ingegneri strutturisti che progettano telai e controventi
sismoresistenti in acciaio.

**È una skill documentale per il tecnico**: fornisce materiali, tipologie, fattori di comportamento e classe
delle sezioni; **non** esegue le verifiche (resistenza/duttilità di membrature e collegamenti) né progetta i
collegamenti.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Copre le **regole generali per l'acciaio in zona sismica** (§7.5). È **distinta**
da `costruzioni-acciaio-ntc` (§4.2, materiali/resistenze/instabilità/verifiche **statiche**) e da
`fattore-comportamento-q-sismica-ntc` (§7.3.1, framework **generale** del fattore q): il §7.5 aggiunge i requisiti
sismici specifici dell'acciaio (γov, tipologie e controventi dissipativi, Tab. 7.5.I classe sezione). Condivide
con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018). Restano fuori scope: le
verifiche RES/DUT di membrature e collegamenti (§§ 7.5.3.1-7.5.3.2, 7.5.4-7.5.6) e il q0 numerico (Tab. 7.3.II).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-7-5**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 7.5 (pagine PDF 243-246) estratto con `pdftotext -layout` e verificato sull'immagine (`pdftoppm -r 150`)
  per γov, αu/α1, Tab. 7.5.I e il limite NEd/Npl,Rd.

Trascrizione in `references/fonti/ntc2018-par-7-5.md`; estratto operativo in
`references/estratti/acciaio-sismica-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **§7.5.1**: acciaio conforme §11.3.4.9; **γov = 1,25** (S235/S275/S355) / **1,15** (S420/S460).
- **§7.5.2.1**: tipologie a-f; controventi concentrici b1 diagonale tesa attiva / b2 a V / **b3 a K non
  dissipativa**; a mensola/pendolo inverso (carico assiale normalizzato ≤ 0,3 → telaio); dispositivi antisismici
  esclusi, nuclei/pareti c.a. → §7.4.
- **§7.5.2.2**: q0 max Tab. 7.3.II; **αu/α1 = 1,1 / 1,2 / 1,3 / 1,2 / 1,0**.
- **§7.5.3 / Tab. 7.5.I**: zone dissipative nelle membrature; capacity design **1,1·γov·Rpl,Rd**; μ = θu/θy
  (θu al −15%); CD"B" (2<q0≤4) → Classe 1 o 2, CD"A" (q0>4) → Classe 1; colonne dissipative telaio **NEd/Npl,Rd ≤ 0,3**.

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire** le verifiche RES/DUT di membrature e collegamenti né le regole specifiche per tipologia
  (§§ 7.5.3.1-7.5.3.2, 7.5.4-7.5.6); non calcolare il q0 numerico (Tab. 7.3.II).
- Non **progettare** i collegamenti; non trattare i requisiti statici (§4.2, → skill dedicata) né il framework
  del fattore q (§7.3.1, → skill dedicata).

### Cosa fare
- Fornire materiali/γov, tipologie strutturali, fattori q0/αu/α1 e classe della sezione (Tab. 7.5.I), sempre con
  rinvio al paragrafo/tabella NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre il par. 7.5. Verificare sull'immagine i valori (γov 1,25/1,15; αu/α1 1,1/1,2/1,3/1,0; Tab. 7.5.I
Classe 1-2 vs Classe 1; NEd/Npl,Rd ≤ 0,3).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista esperto di strutture in acciaio).

## Stato attuale

- Versione: 0.1.0-alpha (closes #458)
- Task files: 2 (`inquadra-tipologie-materiali-fattore-q.md`, `verifica-requisiti-classe-sezione-dissipativi.md`)
- Esempi: 2 (materiali/γov, tipologia e αu/α1 di un telaio in acciaio; classe della sezione per un elemento
  dissipativo con la Tab. 7.5.I)
