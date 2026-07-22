# relazione-calcolo-codici-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento della redazione dei
progetti strutturali esecutivi e delle relazioni di calcolo** — in particolare delle **analisi svolte con codici
di calcolo automatico (software FEM)** — secondo le **NTC 2018** (D.M. 17 gennaio 2018), **Capitolo 10** (§10.1 e
§10.2).

**Non esegue** l'analisi né le verifiche, **non** redige la relazione al posto del progettista e **non valuta** uno
specifico software: fornisce l'elenco degli elaborati, i contenuti minimi della relazione di calcolo, i requisiti
d'uso dei codici e i controlli del giudizio di accettabilità.

## Target

Ingegneri strutturisti che devono strutturare gli elaborati del progetto esecutivo e la relazione di calcolo, e
documentare correttamente l'uso di software FEM secondo le NTC 2018 Cap. 10.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-elaborati-uso-codici` | Elaborati del progetto esecutivo (§10.1) e doveri nell'uso dei codici di calcolo: affidabilità dei codici, attendibilità dei risultati, documentazione del software (§10.2) |
| `inquadra-relazione-giudizio-accettabilita` | Contenuti della relazione di calcolo (tipo di analisi, origine codici, presentazione risultati), giudizio motivato di accettabilità e valutazione indipendente (§10.2.1, 10.2.2) |

Nucleo: gli **elaborati** del progetto (§10.1), i **doveri sull'uso dei codici** (affidabilità/attendibilità,
§10.2), i **contenuti della relazione di calcolo** e il **giudizio motivato di accettabilità** (confronto con
calcoli semplici, equilibrio reazioni/carichi, §10.2.1) e la **valutazione indipendente** (§10.2.2).

## Relazione con altre skill

- **Trasversale**: si applica a qualunque progetto strutturale; per i contenuti tecnici da riportare in relazione
  complementa `combinazioni-carico-ntc` (§2.5.3), `spettro-risposta-ntc` (§3.2), le skill di materiale (§4) e di
  verifica geotecnica (`verifiche-geotecniche-slu-ntc`, §6.2.4). Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **Capitolo 10 (§10.1-10.2.2)** - testo del Supplemento Ordinario n. 8 alla
  G.U. n. 42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim; capitolo interamente descrittivo (nessuna formula/costante).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** l'analisi né le verifiche, **non redige** la relazione al posto del progettista.
- **Non valuta** né certifica uno specifico software.
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del Capitolo 10 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
