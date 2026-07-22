# fattore-comportamento-q-sismica-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento del comportamento
strutturale** (dissipativo / non dissipativo) **e del fattore di comportamento q** secondo le **NTC 2018** (D.M.
17 gennaio 2018), **paragrafi 7.2.2 e 7.3.1**.

**Non calcola** q né la domanda sismica, **non** definisce lo spettro di progetto (§3.2.3) e **non sostituisce**
il progettista: fornisce i criteri (comportamento dissipativo/non dissipativo, classi di duttilità CD"A"/CD"B",
progettazione in capacità) e la formula qlim = q0·KR con i suoi termini.

## Target

Ingegneri strutturisti che, in un progetto sismico, devono scegliere il comportamento strutturale e la classe di
duttilità e determinare il fattore di comportamento q con cui ridurre lo spettro elastico allo spettro di
progetto, secondo le NTC 2018 par. 7.2.2-7.3.1.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-comportamento-strutturale` | Comportamento non dissipativo vs dissipativo, classi di duttilità CD"A"/CD"B" e progettazione in capacità (γRd globale ≥ 1,25) (§7.2.2) |
| `inquadra-fattore-comportamento-q` | Fattore q allo SLV: qlim = q0·KR [7.3.1] (KR 1/0,8), q0 Tab. 7.3.II, kw pareti c.a., verticale q=1,5 (ponti 1), non dissipativo [7.3.2] (§7.3.1) |

Nucleo: la scelta del **comportamento strutturale** (§7.2.2) e il limite superiore del fattore di comportamento
**qlim = q0 · KR** [7.3.1], con **KR = 1/0,8**, la riduzione **kw** per pareti in c.a. e i casi particolari
(verticale q=1,5 / ponti 1; non dissipativo **1 ≤ qND = (2/3)·qCD"B" ≤ 1,5** [7.3.2]).

## Relazione con altre skill

- **A valle**: `spettro-risposta-ntc` (§3.2) usa q per lo spettro di progetto; **a monte** `regolarita-strutturale-sismica-ntc`
  (§7.2.1) fissa la regolarità in altezza da cui dipende KR. I valori q0 material-specifici sono nelle skill di
  materiale (`costruzioni-calcestruzzo-ntc`, `costruzioni-acciaio-ntc`, ecc., §7.4-7.9). Condivide la fonte GU con
  le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.2.2 e 7.3.1** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim; le formule [7.3.1], [7.3.2] e la Tab. 7.3.II verificate anche sull'immagine delle pagine.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** q, qlim, qND, kw o αu/α1 né **la domanda sismica** / lo **spettro di progetto** (§3.2.3).
- **Non riproduce** il **set completo** delle Tab. 7.3.II per ogni tipologia/materiale (§7.4-7.9).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura dei par. 7.2.2-7.3.1 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
