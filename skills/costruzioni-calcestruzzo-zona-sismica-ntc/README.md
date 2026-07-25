# costruzioni-calcestruzzo-zona-sismica-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista esperto di progettazione sismica del c.a. da completare)

Skill di **supporto documentale** al **progettista strutturale** per inquadrare la **progettazione sismica delle
costruzioni di calcestruzzo armato** secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 7.4**: caratteristiche
dei materiali, tipologie strutturali e fattori di comportamento (αu/α1, CD"A"/CD"B"), gerarchia delle resistenze
(capacity design) di travi, pilastri, nodi e pareti, dettagli costruttivi.

**Non esegue** il progetto né le verifiche di dettaglio e **non sostituisce** il progettista né la Circolare
applicativa 2019: inquadra il quadro progettuale sismico del c.a. È **distinta** da `costruzioni-calcestruzzo-ntc`
(§4.1, progetto **ordinario non sismico**) e da `fattore-comportamento-q-sismica-ntc` (§7.3.1, macchina generale del q).

## Target

Ingegneri strutturisti che devono impostare la progettazione sismica di edifici in calcestruzzo armato (scelta della
tipologia e del fattore di comportamento, gerarchia delle resistenze) secondo le NTC 2018 par. 7.4.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-tipologie-e-fattore-comportamento` | Materiali (§7.4.2), tipologie strutturali (§7.4.3.1) e fattori di comportamento αu/α1 e scelta CD"A"/CD"B" (§7.4.3.2) |
| `applica-gerarchia-delle-resistenze` | Gerarchia delle resistenze (§7.4.4): γRd (Tab. 7.2.I), taglio travi, pressoflessione pilastri (55%/65%), nodo pilastro forte-trave debole [7.4.4] |

Nucleo: acciaio **B450C** (§7.4.2); **tipologie** (telaio/pareti **taglio base ≥ 65%**, miste, pendolo inverso,
deformabili torsionalmente) (§7.4.3.1); **αu/α1** telai 1,1/1,2/1,3, pareti 1,0/1,1/1,2 e scelta **CD"A"/CD"B"**
(§7.4.3.2); **gerarchia delle resistenze** con **γRd** (Tab. 7.2.I), pilastri **≤ 55%/65%** e nodo **ΣMc,Rd ≥
γRd·ΣMb,Rd** (§7.4.4).

## Relazione con altre skill

- Copre la **progettazione sismica del c.a.** (§7.4, Cap. 7). **Distinta** da `costruzioni-calcestruzzo-ntc` (§4.1),
  `fattore-comportamento-q-sismica-ntc` (§7.3.1) e dalle altre skill sismiche per materiale (acciaio §7.5, composte
  §7.6, legno §7.7, muratura §7.8, ponti §7.9, isolamento §7.10). Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.4** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e con i valori
  numerici/formule verificati sull'immagine delle pagine PDF 228-230.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** il **progetto** né le **verifiche di dettaglio** (RES/DUT complete, dettagli costruttivi §7.4.6): il
  dettaglio numerico resta nella norma.
- **Non tratta** il **progetto ordinario non sismico** (§4.1, → skill `costruzioni-calcestruzzo-ntc`) né la macchina
  generale del **q** (§7.3.1, → skill `fattore-comportamento-q-sismica-ntc`); non sostituisce il progettista né la
  Circolare 2019.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura del par. 7.4 delle NTC 2018 e della relativa Circolare applicativa 2019.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
