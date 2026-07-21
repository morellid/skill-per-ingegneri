# regolarita-strutturale-sismica-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento della valutazione della
regolarità di una costruzione in pianta e in altezza** ai fini della progettazione sismica secondo le **NTC
2018** (D.M. 17 gennaio 2018), **paragrafo 7.2.1**, e delle sue conseguenze sul metodo di analisi e sul fattore
di comportamento (§7.3.1, §7.3.3.1).

**Non calcola** la struttura né **esegue** l'analisi, **non determina** q0 (Tab. 7.3.II) né T1, e **non
sostituisce** il progettista: fornisce i criteri di regolarità (in pianta a-c, in altezza d-g) con le soglie e le
conseguenze (fattore KR = 1 o 0,8, applicabilità dell'analisi lineare statica).

## Target

Ingegneri strutturisti che devono stabilire se una costruzione è regolare in pianta e/o in altezza e trarne le
conseguenze normative secondo le NTC 2018 par. 7.2.1 e 7.3.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-regolarita-pianta-altezza` | Criteri di regolarità in pianta (a-c) e in altezza (d-g) con le relative soglie, struttura scatolare, rinvio ponti (§7.2.1) |
| `inquadra-conseguenze-regolarita` | Conseguenze della regolarità in altezza: fattore KR = 1 o 0,8 sul fattore di comportamento (§7.3.1) e ammissibilità dell'analisi lineare statica (§7.3.3.1) |

Nucleo: i **criteri a-c (pianta)** e **d-g (altezza)** con le soglie (rientranze ≤ 5%, rapporto lati < 4,
variazioni di massa ≤ 25%, rigidezza −30%/+10%, capacità/domanda entro 30%, rientri 10%/30%), e le **conseguenze**
(**KR = 1/0,8** sul fattore di comportamento; **analisi lineare statica** solo se regolare in altezza e T1 ≤ 2,5
TC o TD) (§7.2.1, §7.3).

## Relazione con altre skill

- **Complementa** `spettro-risposta-ntc` (§3.2), `periodo-proprio-t1-ntc` (§7.3.3.2, stima di T1) e
  `combinazioni-carico-ntc` (§2.5.3). Nessuna di queste tratta i criteri di regolarità. Condivide la fonte GU con
  le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.2.1** (regolarità) e **par. 7.3.1/7.3.3.1** (conseguenze) -
  testo del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256
  `dda1e397...`), estratto con `pdftotext` e trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** la struttura né **esegue** l'analisi; **non** determina **q0** (Tab. 7.3.II) né le classi di
  duttilità (§7.2.2); **non** calcola **T1** (§7.3.3.2, skill `periodo-proprio-t1-ntc`).
- **Non tratta** la **regolarità dei ponti** (§7.9.2.1).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 7.2.1 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
