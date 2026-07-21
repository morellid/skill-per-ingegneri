# consolidamento-geotecnico-opere-esistenti-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere geotecnico/strutturista da completare)

Skill di **supporto documentale** al **progettista geotecnico e strutturale** per l'**inquadramento della
progettazione degli interventi di consolidamento geotecnico di opere esistenti** (sottofondazioni, rinforzo
delle fondazioni, miglioramento del terreno di fondazione) secondo le **NTC 2018** (D.M. 17 gennaio 2018),
**paragrafo 6.10**: criteri generali, indagini, tipi di consolidamento, controlli e monitoraggio.

**Non calcola** né **dimensiona** gli interventi, **non definisce** il modello geotecnico, **non progetta** il
risanamento strutturale e **non sostituisce** il progettista: fornisce l'individuazione delle cause, il principio
del progetto unitario geotecnico-strutturale, i sei tipi di consolidamento e la regola del controllo
obbligatorio.

## Target

Ingegneri geotecnici e strutturisti che devono inquadrare la progettazione del consolidamento geotecnico di
un'opera esistente (sottofondazioni, rinforzo delle fondazioni) secondo le NTC 2018 par. 6.10.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-criteri-tipi-consolidamento` | Cause del comportamento anomalo, progetto unitario geotecnico-strutturale, i sei tipi di consolidamento e le cautele per gli interventi con variazioni di volume (§6.10.1, 6.10.3) |
| `inquadra-indagini-controlli-consolidamento` | Indagini su manufatto e terreno, grandezze cinematiche e pressioni interstiziali, controllo obbligatorio con ridistribuzione delle sollecitazioni, monitoraggio e collaudo (§6.10.2, 6.10.4) |

Nucleo: **progetto unitario** geotecnico-strutturale, i **sei tipi di consolidamento** (§6.10.3), le **cautele**
per interventi con variazioni di volume (iniezioni, congelamento, gettiniezione), e il **controllo obbligatorio**
quando l'intervento comporta una ridistribuzione delle sollecitazioni al contatto terreno-manufatto (§6.10).

## Relazione con altre skill

- **Complementa** `costruzioni-esistenti-ntc-cap8` (classificazione strutturale dell'esistente: LC/FC,
  adeguamento/miglioramento - Cap. 8) e `relazione-geologica-geotecnica-ntc` (che esclude i §6.3-6.12). Condivide
  la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 6.10** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** né **dimensiona** gli interventi di consolidamento; **non** definisce il modello geotecnico né
  **progetta** il risanamento strutturale.
- **Non tratta** il **miglioramento/rinforzo dei terreni** in generale (§6.9), la **classificazione sismica
  dell'esistente** (Cap. 8) né la **progettazione sismica** (Cap. 7).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista geotecnico/strutturale, né la lettura del par. 6.10 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
