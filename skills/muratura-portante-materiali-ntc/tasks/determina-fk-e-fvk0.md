# Task — Determina i parametri meccanici fk e fvk0 (NTC 2018 §11.10.3)

Supporto documentale per determinare i **parametri meccanici** di una muratura portante secondo il par. 11.10.3
delle NTC 2018 (DM 17/1/2018): la **resistenza a compressione fk** (sperimentale o stimata) e la **resistenza
caratteristica a taglio in assenza di tensioni normali fvk0**. **Non** esegue le verifiche di progetto.

Fonte: `../references/fonti/ntc2018-par-11-10.md`; checklist: `../references/estratti/muratura-materiali-checklist.md`.

## Input tipico

- Tipo di elementi: **artificiali pieni/semipieni** o **naturali di pietra squadrata**.
- Resistenza a compressione dell'elemento: caratteristica **fbk** o media **fbm**.
- Classe della **malta** (M2,5/M5/M10/M15…); spessore dei giunti; disponibilità di prove sperimentali.

## Passi

1. **Resistenza a compressione fk (§11.10.3.1)**
   - **Via sperimentale**: fk si determina su **n muretti (n ≥ 6)** (UNI EN 1052-1), con verifica dei materiali
     (malta: 3 provini 40×40×160; elementi: 10 elementi, UNI EN 772-1).
   - **Via stima (elementi artificiali pieni/semipieni)**: ricava fk dalla **Tab. 11.10.VI** in funzione di **fbk**
     e della classe di malta. Se è dichiarata solo la media fbm: **fbk = 0,8·fbm**. Validità: **giunti 5-15 mm**
     riempiti; **interpolazione lineare** ammessa, **mai estrapolazione**.
   - **Via stima (elementi naturali di pietra squadrata)**: **fbk = 0,75·fbm** [11.10.3]; ricava fk dalla **Tab.
     11.10.VII**.

2. **Resistenza caratteristica a taglio fvk0 (§11.10.3.2)**
   - **Via sperimentale**: su **n campioni (n ≥ 6)** (UNI EN 1052-3) o compressione diagonale.
   - **Via stima**: ricava fvk0 dalla **Tab. 11.10.VIII** in funzione dell'elemento e della classe di malta
     (laterizio 0,30/0,20/0,10; silicato di calcio e cls 0,20/0,15/0,10; malta strati sottili/alleggerita);
     interpolazione lineare ammessa, no estrapolazione.

3. **Output**: valore stimato/sperimentale di fk (con indicazione della tabella e degli input fbk/classe malta) e
   di fvk0, con nota sui limiti di validità (giunti 5-15 mm, no estrapolazione). Segnala che fk e fvk0 sono
   **valori caratteristici**: le resistenze di progetto (fd = fk/γM) e le verifiche restano fuori scope.

## Cosa NON fare

- Non calcolare le **resistenze di progetto** (fd = fk/γM) né eseguire le verifiche (§4.5): fuori scope.
- Non **estrapolare** oltre i valori delle Tab. 11.10.VI/VII/VIII; non usare la Tab. 11.10.VI (artificiali) per
  elementi naturali (usa la VII) e viceversa.
- Non trattare la resistenza a taglio **fvk con tensioni normali** (§11.10.3.3) né i **moduli di elasticità**
  (§11.10.3.5).
- Non inventare valori: ogni numero deve essere rintracciabile in `../references/fonti/ntc2018-par-11-10.md`.
