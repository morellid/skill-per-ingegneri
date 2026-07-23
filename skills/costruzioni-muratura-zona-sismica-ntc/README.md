# costruzioni-muratura-zona-sismica-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista esperto di muratura da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento delle regole generali**
delle **costruzioni di muratura in zona sismica** secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo
7.8.1**: premessa/CD"B", requisiti dei materiali, fattori di comportamento e requisiti geometrici delle pareti.

**Non esegue** le verifiche dei pannelli (pressoflessione/taglio) né **progetta** l'armatura e **non
sostituisce** il progettista: fornisce i requisiti dei materiali, i valori di αu/α1 e la Tab. 7.8.I. È
**distinta** da `costruzioni-muratura-ntc` (§4.5, statica) e da `fattore-comportamento-q-sismica-ntc` (§7.3.1,
fattore q generale).

## Target

Ingegneri strutturisti e progettisti di edifici in muratura che devono impostare un edificio in muratura in
zona sismica secondo le NTC 2018 par. 7.8.1.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-materiali-fattori-comportamento` | Premessa/CD"B" (§7.8.1.1), requisiti dei materiali (§7.8.1.2) e fattori di comportamento αu/α1 (§7.8.1.3) |
| `verifica-requisiti-geometrici-pareti` | Criteri di progetto e requisiti geometrici delle pareti resistenti al sisma (§7.8.1.4, Tab. 7.8.I) |

Nucleo: **CD"B"** e coeff. parziali ridotti (§7.8.1.1); **materiali** (f_bk ≥ 5 MPa, malta ≥ 5 MPa, vuoti ≤ 45%);
**αu/α1** (1,7 ordinaria / 1,5 armata / 1,6 confinata); **Tab. 7.8.I** (t_min, snellezza h0/t, l/h'; solai ≤ 5 m).

## Relazione con altre skill

- Copre le **regole generali** per la muratura in zona sismica (§7.8.1). **Distinta** da
  `costruzioni-muratura-ntc` (§4.5, statica) e `fattore-comportamento-q-sismica-ntc` (§7.3.1). Condivide la
  fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.8.1** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 261-262.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** le **verifiche** dei pannelli murari (pressoflessione nel piano e fuori piano, taglio: §§ 7.8.2
  ordinaria, 7.8.3 armata, 7.8.4 confinata) né i **metodi di analisi** (§7.8.1.5).
- **Non progetta** l'**armatura** né i **dettagli/cordoli** (§§ 7.8.1.7-7.8.5).
- **Non tratta** i requisiti **statici** (§4.5, → skill `costruzioni-muratura-ntc`) né il **fattore q** generale
  (§7.3.1, → skill `fattore-comportamento-q-sismica-ntc`); non sostituisce il progettista.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura del par. 7.8 delle NTC 2018 e della relativa Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
