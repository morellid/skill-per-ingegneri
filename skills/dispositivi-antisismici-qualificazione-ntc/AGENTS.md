# AGENTS.md - dispositivi-antisismici-qualificazione-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale**, al **Direttore dei Lavori** e al **collaudatore** per la
**qualificazione** e i **controlli di accettazione in cantiere** dei **dispositivi antisismici e di controllo delle
vibrazioni** (isolatori elastomerici e a scorrimento, dissipatori lineari/non lineari/viscosi, dispositivi di vincolo
a fusibile/provvisori) secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 11.9** (Cap. 11 «Materiali e prodotti
per uso strutturale»): requisiti generali (§11.9), tipologie (§11.9.1), qualificazione (§11.9.2), accettazione
(§11.9.3), prove e limiti per tipo (§11.9.4-11.9.10).

**È una skill documentale per il tecnico**: inquadra qualificazione e accettazione; **non** esegue il progetto delle
costruzioni isolate né dimensiona i dispositivi (§7.10).

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Copre la **qualificazione/accettazione dei dispositivi antisismici** (§11.9, Cap. 11).
È **distinta** da `isolamento-sismico-ntc` (§7.10, **progetto** delle costruzioni con isolamento/dissipazione), che
rinvia esplicitamente al §11.9 come fuori scope, e dalle skill materiali del Cap. 11
(`controlli-accettazione-cls-acciaio-ntc` §11.2/§11.3, ecc.): il §11.9 è il paragrafo specifico per i dispositivi
antisismici (UNI EN 15129, prove di accettazione demandate al Direttore dei Lavori). Condivide con le altre skill NTC
la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-11-9**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 11.9 (pagine PDF 358-364) estratto con `pdftotext -layout`; **tutti** i valori numerici (tabelle Tab.
  11.9.I-IV, formule, numerosità delle prove) verificati sull'immagine (`pdftoppm -r 150`) delle pagine PDF
  358/360/361/362/363/364, perché `pdftotext` corrompe pedici, simboli greci e disuguaglianze.

Trascrizione in `references/fonti/ntc2018-par-11-9.md`; estratto operativo in
`references/estratti/dispositivi-antisismici-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **§11.9**: vita di servizio **> 10 anni**; campo di temperatura in assenza di indicazioni **almeno −15 °C ÷ +45 °C**;
  UNI EN 15129: **dbd = SLV**, **γx·dbd = SLC**.
- **§11.9.2**: punto A del §11.1 → **UNI EN 15129 + Marcatura CE** (VVCP per applicazioni critiche); altrimenti **caso
  C del §11.1**; manuale di posa/manutenzione.
- **§11.9.3**: accettazione **obbligatoria per tutte le tipologie**, **demandata al Direttore dei Lavori**
  (campionamento sui lotti del cantiere, verifica geometrica/tolleranze, rifiuto non conformi); prove **laboratorio
  art. 59 DPR 380/2001** (FPC tests).
- **§11.9.4-11.9.10**: prove **≥ 20% e ≥ 4** per tipo; **Tab. 11.9.I-IV**; prova quasi statica **≥ 5 cicli ±d2**;
  lineari **ξe < 15%**, **|Ke−Kin|/Kin < 20%**; viscosi **γv = (1+td)·(1,5)^α**; elastomerici piastre **18%**,
  **2/20 mm**; scorrimento attrito **≤ 25%**, **1,25 d2**; fusibile **±10%/3 cicli/±15%**; provvisori corsa
  **≥ ±50/25 mm**, FS **1,5** (o **1,1**).

## Convenzioni specifiche

### Cosa NON fare
- Non **progettare** le costruzioni con isolamento/dissipazione né **dimensionare** i dispositivi (§7.10).
- Non trattare la qualificazione dei **materiali** del Cap. 11 (cls/acciaio §§11.2/11.3): rinvia alle skill dedicate.
- Non inventare valori: ogni tabella/formula/soglia deve essere rintracciabile in
  `references/fonti/ntc2018-par-11-9.md`.

### Cosa fare
- Fornire i requisiti generali, le tipologie, il percorso di qualificazione (UNI EN 15129/caso C) e la procedura di
  accettazione del Direttore dei Lavori, con le numerosità e i limiti prestazionali per tipo, sempre con rinvio al
  sotto-paragrafo/tabella NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e riestrarre
il par. 11.9. Verificare sull'immagine i valori (vita >10 anni; −15/+45 °C; Tab. 11.9.I-IV; ξe<15%; |Ke−Kin|/Kin<20%;
γv=(1+td)·(1,5)^α; 18%/2/20 mm; attrito 25%; 1,25 d2; fusibile ±10%/±15%; corsa ±50/25 mm; FS 1,5/1,1).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista esperto di isolamento sismico / collaudatore).

## Stato attuale

- Versione: 0.1.0-alpha (closes #470)
- Task files: 2 (`inquadra-tipologie-e-qualificazione.md`, `imposta-accettazione-e-prove-per-tipo.md`)
- Esempi: 2 (accettazione in cantiere di isolatori elastomerici con campionamento del DL; qualificazione di
  dissipatori viscosi)
