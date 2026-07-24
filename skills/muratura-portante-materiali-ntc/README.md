# muratura-portante-materiali-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista esperto di muratura / Direttore dei Lavori da completare)

Skill di **supporto documentale** al **progettista strutturale** e al **Direttore dei Lavori** per la
**qualificazione dei materiali** e la **determinazione dei parametri meccanici** della muratura portante secondo
le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 11.10**: elementi e categorie, malte, resistenza a compressione
fk e a taglio fvk0.

**Non esegue** le verifiche di progetto (fd = fk/γM) né **dimensiona** la muratura e **non sostituisce** il
progettista né il Direttore dei Lavori: fornisce le categorie/sistemi VVCP degli elementi, i criteri di
accettazione, le classi di malta e la determinazione di fk e fvk0. È **distinta** da `costruzioni-muratura-ntc`
(§4.5, progetto), `costruzioni-muratura-zona-sismica-ntc` (§7.8.1) e `controlli-accettazione-cls-acciaio-ntc`
(§11.2/§11.3).

## Target

Ingegneri strutturisti e Direttori dei Lavori che devono qualificare gli elementi e le malte per muratura portante
e ricavarne i parametri meccanici secondo le NTC 2018 par. 11.10.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-elementi-e-malte` | Elementi Cat. I/II e prove di accettazione (§11.10.1) e malte, classi e prove (§11.10.2) |
| `determina-fk-e-fvk0` | Determinazione di fk (sperimentale/stima, Tab. 11.10.VI-VII) e fvk0 (Tab. 11.10.VIII) (§11.10.3) |

Nucleo: **elementi Cat. I (2+) / II (4)** e accettazione (350/650 m³; media ≥ fbm; f1 ≥ 0,80·fbm); **malte**
(M2,5-M20; fm ≥ 2,5); **fk** (Tab. 11.10.VI-VII, fbk = 0,8/0,75·fbm); **fvk0** (Tab. 11.10.VIII).

## Relazione con altre skill

- Copre la **qualificazione dei materiali e i parametri meccanici** (§11.10, Cap. 11). **Distinta** da
  `costruzioni-muratura-ntc` (§4.5), `costruzioni-muratura-zona-sismica-ntc` (§7.8.1) e
  `controlli-accettazione-cls-acciaio-ntc` (§11.2/§11.3). Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 11.10** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 365-368.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** le **verifiche di progetto** né calcola le **resistenze di progetto** (fd = fk/γM); non
  dimensiona la muratura.
- **Non tratta** la resistenza a taglio **fvk con tensioni normali** (§11.10.3.3) né i **moduli di elasticità**
  (§11.10.3.5).
- **Non tratta** il **progetto/verifiche** (§4.5, → skill `costruzioni-muratura-ntc`), i requisiti **sismici**
  (§7.8, → skill `costruzioni-muratura-zona-sismica-ntc`) né l'accettazione di **cls/acciaio** (§11.2/§11.3, →
  skill dedicata); non sostituisce il progettista né il Direttore dei Lavori.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, il Direttore dei Lavori né la lettura del par. 11.10 delle NTC 2018 e della relativa Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
