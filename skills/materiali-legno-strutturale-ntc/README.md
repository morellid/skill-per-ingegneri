# materiali-legno-strutturale-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista esperto di legno / Direttore dei Lavori da completare)

Skill di **supporto documentale** al **progettista strutturale** e al **Direttore dei Lavori** per la
**qualificazione** e le **proprietà** dei materiali e prodotti a base di legno per uso strutturale secondo le
**NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 11.7**: generalità e casi di qualificazione, profilo resistente e
coefficiente kh, tipi di prodotto e norme di riferimento, accettazione in cantiere.

**Non esegue** le verifiche di progetto (fd = kmod·fk/γM) e **non sostituisce** il progettista né il Direttore dei
Lavori: fornisce i casi di qualificazione, il profilo resistente (Tab. 11.7.I), il coefficiente kh e le norme CE
dei prodotti. È **distinta** da `costruzioni-legno-ntc` (§4.4, progetto), `costruzioni-legno-zona-sismica-ntc`
(§7.7) e dalle skill materiali `muratura-portante-materiali-ntc` (§11.10) e `controlli-accettazione-cls-acciaio-ntc`
(§11.2/§11.3).

## Target

Ingegneri strutturisti e Direttori dei Lavori che devono qualificare i prodotti in legno strutturale (massiccio,
lamellare, pannelli) e inquadrarne le proprietà secondo le NTC 2018 par. 11.7.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-proprieta-e-profilo-resistente` | Generalità/qualificazione (§11.7.1), valori caratteristici, profilo resistente Tab. 11.7.I e coefficiente kh (§11.7.1.1) |
| `qualifica-prodotti-e-accettazione` | Tipi di prodotto e norme di riferimento (§11.7.2-11.7.6) e accettazione in cantiere (§11.7.10) |

Nucleo: **casi A/B/C** di qualificazione (§11.7.1); **frattile 5%**, prove 300 s, **profilo resistente** (Tab.
11.7.I); **kh** (massiccio min[(150/h)^0,2;1,3]; lamellare min[(600/h)^0,1;1,1]); prodotti **UNI EN 14081-1 / 14080
/ 13986** e classi **UNI EN 338**.

## Relazione con altre skill

- Copre la **qualificazione dei materiali a base di legno** (§11.7, Cap. 11). **Distinta** da
  `costruzioni-legno-ntc` (§4.4), `costruzioni-legno-zona-sismica-ntc` (§7.7), `muratura-portante-materiali-ntc`
  (§11.10) e `controlli-accettazione-cls-acciaio-ntc` (§11.2/§11.3). Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 11.7** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 349-350.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** le **verifiche di progetto** né calcola le **resistenze di progetto** (fd = kmod·fk/γM).
- **Non tratta** in dettaglio gli **adesivi** (§11.7.7), i **collegamenti** (§11.7.8) né la **durabilità** (§11.7.9).
- **Non tratta** il **progetto/verifiche** (§4.4, → skill `costruzioni-legno-ntc`), i requisiti **sismici** (§7.7, →
  skill `costruzioni-legno-zona-sismica-ntc`) né l'accettazione di **muratura/cls/acciaio** (§§11.10/11.2/11.3, →
  skill dedicate); non sostituisce il progettista né il Direttore dei Lavori.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, il Direttore dei Lavori né la lettura del par. 11.7 delle NTC 2018 e della relativa Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
