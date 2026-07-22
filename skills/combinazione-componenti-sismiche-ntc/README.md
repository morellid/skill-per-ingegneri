# combinazione-componenti-sismiche-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento della combinazione delle
componenti dell'azione sismica** e della risposta alla variabilità spaziale del moto secondo le **NTC 2018**
(D.M. 17 gennaio 2018), **paragrafo 7.3.5**.

**Non esegue** l'analisi né **calcola** gli effetti, **non genera** le storie temporali e **non sostituisce** il
progettista: fornisce la regola di combinazione (1,00 Ex + 0,30 Ey + 0,30 Ez, con permutazione circolare), la
condizione sulla componente verticale, i criteri per la variabilità spaziale (SRSS) e la regola 3/7 delle storie
temporali.

## Target

Ingegneri strutturisti che devono combinare le componenti dell'azione sismica (regola 1,00 + 0,30 + 0,30) secondo
le NTC 2018 par. 7.3.5.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-combinazione-componenti` | Regola 1,00 Ex + 0,30 Ey + 0,30 Ez [7.3.10], le tre combinazioni per permutazione circolare, componente verticale solo nei casi §7.2.2 |
| `inquadra-analisi-integrazione-passo-variabilita` | Storie temporali (≥ 3 → valori più sfavorevoli, ≥ 7 → media) e variabilità spaziale del moto (SRSS nei casi §3.2.4.1, storie differenziate o moto sincrono) |

Nucleo: la combinazione **1,00·Ex + 0,30·Ey + 0,30·Ez** [7.3.10] con **permutazione circolare** (effetti più
gravosi), la **componente verticale** solo nei casi §7.2.2, la **SRSS** per la variabilità spaziale (§3.2.4.1), e
la regola delle **storie temporali** (≥ 3 → valori più sfavorevoli, ≥ 7 → media) (§7.3.5).

## Relazione con altre skill

- **Complementa** `combinazioni-carico-ntc` (§2.5.3, combinazioni di carico e ψ), `criteri-modellazione-sismica-ntc`
  (§7.2.6), `regolarita-strutturale-sismica-ntc` (§7.2.1), `spostamenti-interpiano-sld-ntc` (§7.3.6.1) e
  `spettro-risposta-ntc` (§3.2). Nessuna tratta la combinazione delle componenti. Condivide la fonte GU con le
  altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.3.5** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim; la formula [7.3.10] verificata anche sull'immagine della pagina.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** l'analisi né **calcola** gli effetti; **non** genera/seleziona le storie temporali.
- **Non tratta** i casi che richiedono la **componente verticale** (§7.2.2) né la **variabilità spaziale del
  moto** (§3.2.4/§3.2.4.1).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 7.3.5 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
