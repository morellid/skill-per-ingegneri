# criteri-modellazione-sismica-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento dei criteri di
modellazione della struttura e dell'azione sismica** ai fini della progettazione sismica secondo le **NTC 2018**
(D.M. 17 gennaio 2018), **paragrafo 7.2.6**.

**Non costruisce** il modello né **esegue** l'analisi, **non determina** q e **non sostituisce** il progettista:
fornisce i criteri di modellazione (modello 3D, rigidezza fessurata, orizzontamenti rigidi, elementi non
strutturali, eccentricità accidentale, limiti per la risposta sismica locale).

## Target

Ingegneri strutturisti che devono impostare il modello di calcolo sismico di una costruzione secondo le NTC 2018
par. 7.2.6.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-modellazione-struttura` | Modello 3D, leggi costitutive, rigidezza fessurata (sino al 50%), orizzontamenti rigidi (soletta c.a. 40/50 mm), elementi non strutturali come massa (§7.2.6) |
| `inquadra-modellazione-azione-sismica` | Rappresentazione dell'azione (forze/spettri/storie), limiti 70% per RSL/ITS (5% smorzamento), eccentricità accidentale ≥ 0,05 della dimensione media (§7.2.6) |

Nucleo: **modello 3D**, **rigidezza fessurata sino al 50%**, **orizzontamenti infinitamente rigidi** (soletta c.a.
≥ 40/50 mm), **elementi non strutturali come massa**, limiti **70%** per RSL/interazione terreno-struttura, ed
**eccentricità accidentale ≥ 0,05** × dimensione media perpendicolare, costante su tutti i piani (§7.2.6).

## Relazione con altre skill

- **Complementa** `regolarita-strutturale-sismica-ntc` (§7.2.1), `spostamenti-interpiano-sld-ntc` (§7.3.6.1),
  `periodo-proprio-t1-ntc` (§7.3.3.2) e `spettro-risposta-ntc` (§3.2). Nessuna tratta i criteri di modellazione.
  Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.2.6** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non costruisce** il modello né **esegue** l'analisi (metodi al §7.3); **non** determina **q**.
- **Non tratta** la **risposta sismica locale** (§3.2.3.6) né le **fondazioni miste** (§6.4.3).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 7.2.6 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
