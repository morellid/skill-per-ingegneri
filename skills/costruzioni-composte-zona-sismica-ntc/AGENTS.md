# AGENTS.md - costruzioni-composte-zona-sismica-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento delle regole generali** delle
costruzioni composte di acciaio-calcestruzzo in zona sismica secondo le **NTC 2018** (DM 17 gennaio 2018),
**paragrafo 7.6**: comportamenti strutturali (§7.6), caratteristiche dei materiali (§7.6.1), tipologie strutturali
e fattori di comportamento q0 (§7.6.2), rigidezza della sezione composta (§7.6.3), criteri e capisaldi del
capacity design per le strutture dissipative (§7.6.4). Target: ingegneri strutturisti che progettano edifici e
strutture composte acciaio-cls sismoresistenti.

**È una skill documentale per il tecnico**: fornisce comportamenti, materiali, tipologie, fattori q0, rigidezza e
capisaldi del capacity design; **non** esegue le verifiche (resistenza/duttilità di membrature e collegamenti) né
progetta i collegamenti.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Copre le **regole generali per le composte acciaio-cls in zona sismica** (§7.6). È
**distinta** da `costruzioni-composte-acciaio-cls-ntc` (§4.3, materiali/larghezze efficaci/connessioni/verifiche
**statiche**), da `costruzioni-acciaio-zona-sismica-ntc` (§7.5, cui il §7.6 rinvia per gli elementi in acciaio) e
da `fattore-comportamento-q-sismica-ntc` (§7.3.1, framework **generale** del fattore q). Condivide con le altre
skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018). Restano fuori scope: le verifiche di
dettaglio RES/DUT, le regole per tipologia/elemento e i dettagli costruttivi (§§ 7.6.4-7.6.8).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-7-6**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 7.6 (pagine PDF 251-253) estratto con `pdftotext -layout` e verificato sull'immagine (`pdftoppm -r 150`)
  per classi cls, B450C, n=7, q0, EU,Rd=1,1·γov·Epl,Rd e NEd/Npl,Rd≤0,3.

Trascrizione in `references/fonti/ntc2018-par-7-6.md`; estratto operativo in
`references/estratti/composte-sismica-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **§7.6**: comportamenti a) non dissipativo (→ §4.3); b) dissipativo (membrature composte); c) dissipativo
  (acciaio, integrità cls compresso).
- **§7.6.1**: cls **≥ C20/25 (LC20/22)** e **≤ C40/50 (LC40/44)**; acciaio c.a. **B450C** (B450A casi §7.4.2.2);
  acciaio strutturale §7.5 e §11.3.4.
- **§7.6.2**: tipologie a-e; pareti/nuclei c.a. → §7.4; **q0 Tab. 7.3.II** (prescrizioni §7.5.2).
- **§7.6.3**: cls compresso **n = Ea/Ecm = 7**; I1 non fessurato / I2 fessurato.
- **§7.6.4**: **EU,Rd = 1,1·γov·Epl,Rd**; **Rj,d ≥ RU,Rd** [7.6.1]; **Vwp,Rd = 0,8·(Vwp,s,Rd + Vwp,c,Rd)** [7.6.2]
  (≤ 40%); **μ = θu/θy** (θu al −15%); colonne dissipative telaio **NEd/Npl,Rd ≤ 0,3** [7.6.3].

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire** le verifiche di dettaglio RES/DUT di membrature e collegamenti né le regole per tipologia/
  elemento (§§ 7.6.4-7.6.8, Tab. 7.6.I-IV); non calcolare il q0 numerico (Tab. 7.3.II).
- Non **progettare** i collegamenti; non trattare i requisiti statici (§4.3, → skill dedicata), le regole sismiche
  dell'acciaio (§7.5, → skill dedicata) né il framework del fattore q (§7.3.1, → skill dedicata).

### Cosa fare
- Fornire comportamenti, materiali, tipologie, fattori q0, rigidezza (n=7) e capisaldi del capacity design, sempre
  con rinvio al paragrafo NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre il par. 7.6. Verificare sull'immagine i valori (cls C20/25-C40/50; B450C; n=7; EU,Rd=1,1·γov·Epl,Rd;
Vwp,Rd 0,8 e 40%; NEd/Npl,Rd ≤ 0,3; μ e -15%).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista esperto di strutture composte).

## Stato attuale

- Versione: 0.1.0-alpha (closes #462)
- Task files: 2 (`inquadra-materiali-tipologie-fattore-q.md`, `verifica-requisiti-capacity-design.md`)
- Esempi: 2 (materiali/tipologia e q0 di un telaio composto; capacity design e limite NEd/Npl,Rd di una colonna
  dissipativa)
