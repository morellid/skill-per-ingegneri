# metodi-analisi-sismica-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista esperto di analisi sismica da completare)

Skill di **supporto documentale** al **progettista strutturale** per la **scelta e l'impostazione del metodo di
analisi sismica** secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafi 7.3.2, 7.3.3 e 7.3.4**: scelta
dinamica/statica, analisi lineare dinamica (modale con spettro di risposta), analisi lineare statica (forze laterali),
valutazione degli spostamenti, analisi non lineare dinamica e statica (pushover).

**Non esegue** l'analisi né le verifiche e **non sostituisce** il progettista né la Circolare applicativa 2019:
inquadra la scelta del metodo e le sue condizioni di applicabilità. È **distinta** da
`fattore-comportamento-q-sismica-ntc` (§7.3.1, q), `periodo-proprio-t1-ntc` (§7.3.3.2, solo T1),
`criteri-modellazione-sismica-ntc` (§7.2.6) e `combinazione-componenti-sismiche-ntc` (§7.3.5).

## Target

Ingegneri strutturisti che devono scegliere il metodo di analisi sismica (statica lineare vs modale vs pushover),
verificarne l'applicabilità e impostare le distribuzioni di forze secondo le NTC 2018 par. 7.3.2-7.3.4.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `scegli-metodo-e-analisi-lineare` | Scelta dinamica/statica (§7.3.2); analisi modale (masse ≥85%, CQC) (§7.3.3.1); analisi lineare statica (T1≤2,5 TC, Fh/Fi/λ) (§7.3.3.2); spostamenti μd (§7.3.3.3) |
| `applica-analisi-non-lineare` | Analisi non lineare dinamica (§7.3.4.1) e statica/pushover (§7.3.4.2): curva di capacità, punto di controllo, distribuzioni Gruppo 1/2 |

Nucleo: metodo di riferimento **analisi modale con spettro** (§7.3.2); modale **masse >5% e ≥85%**, **CQC** (§7.3.3.1);
statica lineare **T1 ≤ 2,5·TC**, **Fh/Fi**, **λ = 0,85/1,0** (§7.3.3.2); spostamenti **dE = μd·dEe**, **SLC = 1,25·SLV**
(§7.3.3.3); **pushover** con **≥ 2 distribuzioni** e curva di capacità **Fb–dc** (§7.3.4.2).

## Relazione con altre skill

- Copre i **metodi di analisi sismica** (§7.3.2-7.3.4, Cap. 7). **Distinta** da `fattore-comportamento-q-sismica-ntc`
  (§7.3.1), `periodo-proprio-t1-ntc` (§7.3.3.2), `criteri-modellazione-sismica-ntc` (§7.2.6) e
  `combinazione-componenti-sismiche-ntc` (§7.3.5). Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **parr. 7.3.2-7.3.4** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e con tutti i valori
  numerici/formule verificati sull'immagine delle pagine PDF 222-224.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** l'**analisi** (modale, statica, pushover, time-history) né le **verifiche**; non dimensiona.
- **Non tratta** il **fattore q** (§7.3.1, → skill `fattore-comportamento-q-sismica-ntc`), la formula di **T1**
  (§7.3.3.2, → skill `periodo-proprio-t1-ntc`), i **criteri di modellazione** (§7.2.6) né la **combinazione delle
  componenti** (§7.3.5); non sostituisce il progettista né la Circolare 2019.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura dei par. 7.3.2-7.3.4 delle NTC 2018 e della relativa Circolare applicativa 2019.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
