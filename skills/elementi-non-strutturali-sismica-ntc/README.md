# elementi-non-strutturali-sismica-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento della progettazione
sismica degli elementi strutturali secondari, degli elementi costruttivi non strutturali** (tamponature,
controsoffitti, parapetti, rivestimenti) **e degli impianti** secondo le **NTC 2018** (D.M. 17 gennaio 2018),
**paragrafi 7.2.3 e 7.2.4**.

**Non calcola** Fa né **esegue** le verifiche, **non determina** Sa e qa e **non sostituisce** il progettista:
fornisce i criteri (limite 15% per gli elementi secondari, incrementi 2/1,4 per irregolarità, soglie 30%/10% per
gli impianti) e la forza Fa = Sa·Wa/qa.

## Target

Ingegneri strutturisti che devono inquadrare la verifica sismica di elementi non strutturali (tamponature,
controsoffitti, parapetti), classificare elementi secondari o progettare l'ancoraggio antisismico degli impianti
secondo le NTC 2018 par. 7.2.3-7.2.4.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-forza-elementi-non-strutturali` | Elementi costruttivi non strutturali: definizione, capacità > domanda, responsabilità, incrementi per irregolarità (2 in pianta, 1,4 in altezza) e forza Fa = Sa·Wa/qa [7.2.1] (§7.2.3) |
| `inquadra-elementi-secondari-impianti` | Elementi strutturali secondari (limite 15%, SLC) e impianti (capacità > domanda, responsabilità, soglie 30%/10% per lo studio specifico) (§7.2.3, 7.2.4) |

Nucleo: la forza **Fa = (Sa·Wa)/qa** [7.2.1] sugli elementi non strutturali, il limite del **15%** per gli
elementi secondari, gli incrementi **×2** (pianta) e **×1,4** (altezza) per la distribuzione irregolare, e le
soglie impianti **30%/10%** per lo studio specifico (§7.2.3-7.2.4).

## Relazione con altre skill

- **Complementa** `criteri-modellazione-sismica-ntc` (§7.2.6, eccentricità accidentale),
  `regolarita-strutturale-sismica-ntc` (§7.2.1), `spostamenti-interpiano-sld-ntc` (§7.3.6.1) e `spettro-risposta-ntc`
  (§3.2). Nessuna tratta gli elementi secondari/non strutturali/impianti. Condivide la fonte GU con le altre skill
  NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.2.3-7.2.4** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim; la formula [7.2.1] e le costanti verificate anche sull'immagine della pagina.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** Fa né **esegue** le verifiche; **non** determina **Sa** e **qa** (documenti di comprovata
  validità).
- **Non calcola** la domanda/gli spostamenti (§7.3.3.3/§7.3.4/§7.3.6) né lo spettro (§3.2).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura dei par. 7.2.3-7.2.4 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
