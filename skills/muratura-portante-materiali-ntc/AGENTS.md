# AGENTS.md - muratura-portante-materiali-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** e al **Direttore dei Lavori** per la **qualificazione dei
materiali** (elementi resistenti e malte) e la **determinazione dei parametri meccanici** (resistenza a
compressione fk e a taglio fvk0) della muratura portante secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo
11.10** (Cap. 11 «Materiali e prodotti per uso strutturale»): elementi e categorie I/II (§11.10.1), prove di
accettazione (§11.10.1.1), malte (§11.10.2), parametri meccanici fk e fvk0 (§11.10.3).

**È una skill documentale per il tecnico**: inquadra la qualificazione dei materiali e la stima dei parametri;
**non** esegue le verifiche di progetto (fd = fk/γM) né dimensiona la muratura.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Copre la **qualificazione dei materiali e i parametri meccanici** della muratura
portante (§11.10, Cap. 11). È **distinta** da `costruzioni-muratura-ntc` (§4.5, **progetto/verifiche**,
resistenze di progetto fd = fk/γM), da `costruzioni-muratura-zona-sismica-ntc` (§7.8.1, requisiti **sismici**) e
da `controlli-accettazione-cls-acciaio-ntc` (§§ 11.2/11.3, accettazione di **cls e acciaio**): il §11.10 è il
paragrafo del Cap. 11 specifico per la muratura. Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O.
n. 8 alla G.U. n. 42/2018). Restano fuori scope: la resistenza a taglio fvk con tensioni normali (§11.10.3.3) e i
moduli di elasticità (§11.10.3.5).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-11-10**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 11.10 (pagine PDF 365-368) estratto con `pdftotext -layout` e verificato sull'immagine (`pdftoppm -r 150`)
  per le Tab. 11.10.I/II/V/VI/VII/VIII e le formule di accettazione.

Trascrizione in `references/fonti/ntc2018-par-11-10.md`; estratto operativo in
`references/estratti/muratura-materiali-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **§11.10.1**: elementi UNI EN 771 + CE; Tab. 11.10.I **Cat. I → 2+**, **Cat. II → 4**; Cat. I **insuccesso ≤ 5%**;
  γM al §4.5.6.
- **§11.10.1.1**: laboratorio **art. 59 DPR 380/2001**; **350 m³ (Cat. II)** / **650 m³ (Cat. I)**; **n ≥ 6**;
  **media ≥ fbm** [11.10.1], **f1 ≥ 0,80·fbm** [11.10.2]; oppure **f1 ≥ fbk**.
- **§11.10.2**: classi **M2,5-M20/Md** (Tab. 11.10.II); **fm < 2,5 non ammesse**; Tab. 11.10.V composizioni;
  accettazione **3 provini 40×40×160** ogni **350 m³** (o 700 m³).
- **§11.10.3**: fk sperimentale (**n muretti ≥ 6**) o Tab. 11.10.VI/VII; **fbk = 0,8·fbm** (artificiali) / **0,75·fbm**
  (naturali); giunti **5-15 mm**; **fvk0** Tab. 11.10.VIII (laterizio 0,30/0,20/0,10; altri 0,20/0,15/0,10).

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire** le verifiche di progetto né calcolare le **resistenze di progetto** (fd = fk/γM); non
  dimensionare la muratura.
- Non trattare la resistenza a taglio **fvk con tensioni normali** (§11.10.3.3) né i **moduli di elasticità**
  (§11.10.3.5); non trattare il progetto (§4.5), la sismica (§7.8) né l'accettazione di cls/acciaio (§§11.2/11.3):
  rinvia alle skill dedicate.

### Cosa fare
- Fornire categorie/sistemi VVCP degli elementi, criteri di accettazione, classi/tipi di malta e la determinazione
  (sperimentale o stimata) di fk e fvk0, sempre con rinvio al paragrafo/tabella NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre il par. 11.10. Verificare sull'immagine i valori (Cat. I 2+/II 4; 350/650 m³; 0,80 fbm; malte 2,5-20;
fbk 0,8/0,75 fbm; giunti 5-15 mm; Tab. 11.10.VI/VII/VIII).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista esperto di muratura / Direttore dei Lavori).

## Stato attuale

- Versione: 0.1.0-alpha (closes #464)
- Task files: 2 (`inquadra-elementi-e-malte.md`, `determina-fk-e-fvk0.md`)
- Esempi: 2 (categoria elementi + classe malta + accettazione; stima di fk dalla Tab. 11.10.VI con fbk = 0,8·fbm)
