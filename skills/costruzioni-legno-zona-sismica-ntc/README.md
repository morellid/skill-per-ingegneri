# costruzioni-legno-zona-sismica-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista esperto di strutture di legno da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento delle regole generali**
delle **costruzioni di legno in zona sismica** secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 7.7**:
aspetti concettuali/CD, materiali e pannelli, fattori di comportamento q0 e requisiti di duttilità.

**Non esegue** le verifiche (resistenza/duttilità di elementi e collegamenti) né **progetta** i collegamenti e
**non sostituisce** il progettista: fornisce comportamento, materiali, i valori q0 (Tab. 7.3.II) e i requisiti di
duttilità dei mezzi di unione. È **distinta** da `costruzioni-legno-ntc` (§4.4, statica) e da
`fattore-comportamento-q-sismica-ntc` (§7.3.1, fattore q generale).

## Target

Ingegneri strutturisti e progettisti di edifici in legno (telaio leggero/platform frame, XLAM/CLT) che devono
impostare un edificio in legno in zona sismica secondo le NTC 2018 par. 7.7.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-comportamento-materiali-fattore-q` | Aspetti concettuali/CD (§7.7.1), materiali e pannelli (§7.7.2) e fattori di comportamento q0 (§7.7.3) |
| `verifica-requisiti-duttilita-dettagli` | Precisazioni sulla duttilità (§7.7.3.1), disposizioni costruttive, verifiche e dettagli (§§7.7.5-7.7.7) |

Nucleo: **CD"A"/CD"B"** e zone dissipative nei collegamenti (§7.7.1); **materiali** (pannelli 13/9/12/15 mm,
unioni incollate non dissipative); **q0** (Tab. 7.3.II); **duttilità** (statica 4/6; d≤12 mm & 10d; d≤3,1 mm & 4d;
coeff. giunti di carpenteria 1,3; resistenza −20%).

## Relazione con altre skill

- Copre le **regole generali** per il legno in zona sismica (§7.7). **Distinta** da `costruzioni-legno-ntc`
  (§4.4, statica) e `fattore-comportamento-q-sismica-ntc` (§7.3.1). Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.7** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 258-260.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** le **verifiche** di resistenza e di duttilità dei singoli elementi e collegamenti né calcola il
  valore numerico di **q0** per tipologia (Tab. 7.3.II).
- **Non progetta** i **collegamenti** né i dettagli (§7.7.7).
- **Non tratta** i requisiti **statici** (§4.4, → skill `costruzioni-legno-ntc`) né il **fattore q** generale
  (§7.3.1, → skill `fattore-comportamento-q-sismica-ntc`); non sostituisce il progettista.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura del par. 7.7 delle NTC 2018 e della relativa Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
