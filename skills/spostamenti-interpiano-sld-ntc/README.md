# spostamenti-interpiano-sld-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento della verifica di
deformabilità allo stato limite di danno (SLD)** - i **limiti di spostamento di interpiano** degli elementi
strutturali - secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafi 7.3.6 e 7.3.6.1** (verifiche di
rigidezza RIG).

**Non calcola** gli spostamenti né **esegue** l'analisi, **non determina** q e **non sostituisce** il
progettista: fornisce il quadro delle verifiche, i sei limiti di drift e le regole di applicazione.

## Target

Ingegneri strutturisti che devono impostare la verifica di deformabilità allo SLD (limiti di spostamento di
interpiano) di un edificio secondo le NTC 2018 par. 7.3.6.1.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-limiti-spostamento-interpiano` | I sei limiti [7.3.11a]-[7.3.15] per tipo di tamponatura/struttura, con q, dr (modello senza tamponature) e h (§7.3.6.1) |
| `inquadra-classe-uso-stato-limite` | Stato limite per classe d'uso (SLD per CU I-II, SLO per CU III-IV con limiti ai 2/3), coesistenza ed estensione delle verifiche (§7.3.6, 7.3.6.1) |

Nucleo: i **limiti di spostamento di interpiano** q·dr/h — **0,0050 h** (tamponature fragili), **0,0075 h**
(duttili), **0,0100 h** (progettate per non danneggiarsi), **0,0020/0,0030/0,0025 h** (muratura
ordinaria/armata/confinata) — con **SLD per CU I-II** e **SLO (2/3) per CU III-IV**, e dr calcolato sul modello
**senza tamponature** (§7.3.6.1).

## Relazione con altre skill

- **Complementa** `regolarita-strutturale-sismica-ntc` (§7.2.1/7.3.1, KR e metodo di analisi),
  `periodo-proprio-t1-ntc` (§7.3.3.2, stima di T1) e `spettro-risposta-ntc` (§3.2). Nessuna tratta i limiti di
  drift allo SLD. Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.3.6 e 7.3.6.1** - testo del Supplemento Ordinario n. 8 alla
  G.U. n. 42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim; i sei limiti e gli operatori (≤ per a-d, < per e) verificati anche sull'immagine della
  pagina.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** gli spostamenti né **esegue** l'analisi (§7.3.3.3 / §7.3.4); **non** determina **q**.
- **Non tratta** le verifiche di **resistenza (RES)** o **duttilità (DUT)** degli elementi strutturali, né quelle
  degli **elementi non strutturali** (§7.3.6.2) e degli **impianti** (§7.3.6.3).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 7.3.6.1 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
