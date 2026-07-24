# costruzioni-acciaio-zona-sismica-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista esperto di strutture in acciaio da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento delle regole generali**
delle **costruzioni di acciaio in zona sismica** secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo
7.5**: materiali e sovraresistenza γov, tipologie strutturali, fattori di comportamento e classe delle sezioni.

**Non esegue** le verifiche (resistenza/duttilità di membrature e collegamenti) né **progetta** i collegamenti e
**non sostituisce** il progettista: fornisce γov, le tipologie, i valori di αu/α1 e la Tab. 7.5.I. È **distinta**
da `costruzioni-acciaio-ntc` (§4.2, statica) e da `fattore-comportamento-q-sismica-ntc` (§7.3.1, fattore q
generale).

## Target

Ingegneri strutturisti e progettisti di edifici in acciaio (telai, controventi concentrici/eccentrici) che devono
impostare una struttura in acciaio in zona sismica secondo le NTC 2018 par. 7.5.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-tipologie-materiali-fattore-q` | Materiali/γov (§7.5.1), tipologie strutturali (§7.5.2.1) e fattori di comportamento q0/αu/α1 (§7.5.2.2) |
| `verifica-requisiti-classe-sezione-dissipativi` | Regole generali per elementi dissipativi e classe della sezione (§7.5.3, Tab. 7.5.I; NEd/Npl,Rd ≤ 0,3) |

Nucleo: **γov** (1,25 S235/S275/S355; 1,15 S420/S460); **tipologie** (intelaiate, controventi concentrici/
eccentrici, mensola/pendolo inverso); **αu/α1** (1,1-1,3); **Tab. 7.5.I** (CD"B" Classe 1 o 2 / CD"A" Classe 1);
colonne dissipative telaio **NEd/Npl,Rd ≤ 0,3**.

## Relazione con altre skill

- Copre le **regole generali** per l'acciaio in zona sismica (§7.5). **Distinta** da `costruzioni-acciaio-ntc`
  (§4.2, statica) e `fattore-comportamento-q-sismica-ntc` (§7.3.1). Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.5** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 243-246.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** le **verifiche** di resistenza (RES) e di duttilità (DUT) di membrature e collegamenti né le
  regole specifiche per tipologia (§§ 7.5.3.1-7.5.3.2, 7.5.4-7.5.6).
- **Non progetta** i **collegamenti** né calcola il **q0** numerico (Tab. 7.3.II).
- **Non tratta** i requisiti **statici** (§4.2, → skill `costruzioni-acciaio-ntc`) né il **fattore q** generale
  (§7.3.1, → skill `fattore-comportamento-q-sismica-ntc`); non sostituisce il progettista.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura del par. 7.5 delle NTC 2018 e della relativa Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
