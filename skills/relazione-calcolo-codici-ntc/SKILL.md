---
name: relazione-calcolo-codici-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento della redazione dei progetti strutturali esecutivi e delle relazioni di calcolo, e in particolare delle analisi e verifiche svolte con l'ausilio di codici di calcolo automatico (software FEM), secondo le NTC 2018 (DM 17 gennaio 2018), Capitolo 10 (paragrafi 10.1 e 10.2). Aiuta a inquadrare gli elaborati del progetto strutturale esecutivo (relazione di calcolo strutturale, relazione sui materiali, elaborati grafici e particolari costruttivi, piano di manutenzione della parte strutturale, relazione sui risultati sperimentali), fermo restando che il progettista resta responsabile dell'intera progettazione; i doveri nell'uso dei codici di calcolo (controllo dell'affidabilita' dei codici e dell'attendibilita' dei risultati, esame preliminare della documentazione del software con basi teoriche, algoritmi, campi d'impiego e casi prova con file di input); i contenuti della relazione di calcolo (tipo di analisi statica o dinamica, lineare o non lineare e sue motivazioni, metodo di risoluzione e verifica, combinazioni e percorsi di carico; origine e caratteristiche dei codici con titolo, autore, produttore, versione e licenza; modalita' di presentazione dei risultati con i contenuti minimi, disegni e schemi grafici di deformate, sollecitazioni e inviluppi, tabulati in allegato); il giudizio motivato di accettabilita' dei risultati (controlli di attendibilita', confronto con calcoli semplici, equilibrio tra reazioni vincolari e carichi); e la valutazione indipendente del calcolo per opere di particolare importanza (ricalcolo da soggetto diverso con programmi diversi). Use when a structural designer must frame the structural project deliverables and the calculation report, or the requirements for analyses run with automatic calculation codes (FEM software) under the Italian NTC 2018 Chapter 10; it is a documentary aid and does NOT run the analysis, does NOT write the report, does NOT assess a specific software, and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Relazione di calcolo e codici di calcolo automatico (NTC 2018 cap. 10)"
summary: "Inquadra la redazione dei progetti strutturali esecutivi e delle relazioni di calcolo (NTC 2018 par. 10.1-10.2): elaborati del progetto, uso dei codici di calcolo, contenuti della relazione, giudizio motivato di accettabilita' e valutazione indipendente."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 10.1: elaborati del progetto esecutivo (relazione di calcolo, materiali, grafici, piano di manutenzione, risultati sperimentali); responsabilita' progettista"
  - "NTC 2018 - par. 10.2 e 10.2.1: analisi con codici di calcolo (affidabilita' dei codici, attendibilita' dei risultati, documentazione software); relazione di calcolo e giudizio di accettabilita'"
  - "NTC 2018 - par. 10.2.2: valutazione indipendente del calcolo per opere di particolare importanza (ricalcolo da soggetto diverso con programmi diversi)"
version: 0.1.0-alpha
status: alpha
tags:
  - relazione-di-calcolo
  - codici-di-calcolo
  - software-strutturale
  - progetto-esecutivo
  - ntc-2018
---

# Relazione di calcolo e codici di calcolo automatico (NTC 2018 cap. 10)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare** gli **elaborati del progetto strutturale
esecutivo** e i **contenuti della relazione di calcolo** — in particolare quando l'analisi è svolta con **codici di
calcolo automatico (software FEM)** — secondo le **NTC 2018** (DM 17 gennaio 2018), **Capitolo 10** (§10.1 e
§10.2):

- **elaborati del progetto** e responsabilità (§10.1);
- **uso dei codici di calcolo** e documentazione del software (§10.2);
- **contenuti della relazione di calcolo** e **giudizio di accettabilità** (§10.2.1);
- **valutazione indipendente** (§10.2.2).

**Non è** uno strumento che esegue l'analisi o redige la relazione: è un **supporto documentale** che inquadra
elaborati, contenuti e controlli. Complementa `combinazioni-carico-ntc`, `spettro-risposta-ntc` e le skill di
materiale/verifica per i contenuti tecnici da riportare in relazione.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-elaborati-uso-codici` | Elaborati del progetto esecutivo (§10.1) e doveri nell'uso dei codici di calcolo: affidabilità dei codici, attendibilità dei risultati, documentazione del software (§10.2) |
| `inquadra-relazione-giudizio-accettabilita` | Contenuti della relazione di calcolo (tipo di analisi, origine codici, presentazione risultati), giudizio motivato di accettabilità e valutazione indipendente (§10.2.1, 10.2.2) |

## Punti chiave (verificati sul testo)

- **Elaborati del progetto** (§10.1): relazione di calcolo strutturale, relazione sui materiali, elaborati grafici
  e particolari, piano di manutenzione, relazione sui risultati sperimentali. Le relazioni vanno sviluppate per
  consentire **elaborazioni indipendenti**; il **progettista resta responsabile** dell'intera progettazione.
- **Uso dei codici** (§10.2): il progettista **controlla l'affidabilità dei codici** e l'**attendibilità dei
  risultati**; esamina la **documentazione del software** (basi teoriche, algoritmi, campi d'impiego, **casi prova
  con file di input**) per valutarne l'idoneità al caso specifico.
- **Relazione di calcolo** (§10.2.1): **tipo di analisi** (statica/dinamica, lineare/non lineare) e motivazioni,
  metodo, combinazioni/percorsi di carico; **origine e caratteristiche dei codici** (titolo, autore, produttore,
  versione, licenza); **presentazione dei risultati** (contenuti minimi, disegni/schemi, inviluppi; **tabulati in
  allegato**). **Giudizio motivato di accettabilità**: controlli di attendibilità, **confronto con calcoli
  semplici**, **equilibrio tra reazioni e carichi**.
- **Valutazione indipendente** (§10.2.2): per **opere di particolare importanza**, ricalcolo dei calcoli più
  importanti da **soggetto diverso** con **programmi diversi** (controllo incrociato).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **Capitolo 10 (§10.1-10.2.2)** - testo del Supplemento Ordinario n. 8 alla
  G.U. n. 42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim; capitolo interamente descrittivo (nessuna formula/costante).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** l'analisi né le verifiche, **non redige** la relazione al posto del progettista.
- **Non valuta** né certifica uno specifico software.
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del Capitolo 10 delle NTC 2018 e della Circolare applicativa.**
