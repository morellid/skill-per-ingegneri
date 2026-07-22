# categorie-sottosuolo-topografiche-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere/geologo da completare)

Skill di **supporto documentale** al **geologo, geotecnico o strutturista** per l'**inquadramento della
classificazione sismica del sito** — **categorie di sottosuolo** (A-E) e **condizioni topografiche** (T1-T4) —
secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 3.2.2**.

**Non calcola** lo spettro né i coefficienti di amplificazione (§3.2.3), **non** esegue analisi di risposta locale
(§7.11.3) e **non sostituisce** il geologo/geotecnico: fornisce i criteri (Vs,eq, substrato Vs≥800, regola dei 30
m, tabelle 3.2.II/3.2.III) per attribuire la categoria di sottosuolo e topografica.

## Target

Geologi, geotecnici e ingegneri strutturisti che, prima di definire l'azione sismica, devono classificare il
sottosuolo (A-E) e la topografia (T1-T4) del sito secondo le NTC 2018 par. 3.2.2.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `classifica-categoria-sottosuolo` | Categoria di sottosuolo A-E (Tab. 3.2.II) con l'approccio semplificato su Vs,eq = H/Σ(hi/Vs,i) [3.2.1], substrato Vs≥800, regola dei 30 m, piani di riferimento (§3.2.2) |
| `classifica-categoria-topografica` | Categoria topografica T1-T4 (Tab. 3.2.III) in funzione dell'inclinazione media e della forma del rilievo, per altezze > 30 m (§3.2.2) |

Nucleo: la **velocità equivalente Vs,eq = H/Σ(hi/Vs,i)** [3.2.1] (substrato Vs≥800, VS,30 per H>30 m) e le
categorie di sottosuolo **A-E** (Tab. 3.2.II) e topografiche **T1-T4** (Tab. 3.2.III).

## Relazione con altre skill

- **A monte** di `spettro-risposta-ntc` (§3.2.3): la categoria di sottosuolo e topografica determinano i
  coefficienti di amplificazione (SS/CC/ST) usati per lo spettro. Complementa `relazione-geologica-geotecnica-ntc`
  (§6.2, caratterizzazione). Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 3.2.2** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42 del
  20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto verbatim;
  la formula [3.2.1] e le Tab. 3.2.II/3.2.III verificate anche sull'immagine delle pagine.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** lo **spettro** né i **coefficienti di amplificazione** stratigrafica SS/CC e topografica ST
  (§3.2.3.2).
- **Non esegue** le **analisi di risposta sismica locale** (§7.11.3) né la **caratterizzazione geotecnica**
  (§6.2.2); non determina i valori di VS.
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il geologo/geotecnico né il progettista, né la lettura diretta del par. 3.2.2 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
