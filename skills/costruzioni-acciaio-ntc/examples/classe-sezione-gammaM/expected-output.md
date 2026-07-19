# Output atteso - Materiale, classe e resistenza a flessione

## 1. Materiale: fyk e ftk (§4.2.1.1, Tab. 4.2.I)

Per l'acciaio **S275** (UNI EN 10025-2) con spessore delle ali **t = 12 mm ≤ 40 mm**, dalla Tab. 4.2.I:

- **fyk = 275 N/mm²** (tensione caratteristica di snervamento);
- **ftk = 430 N/mm²** (tensione caratteristica di rottura).

## 2. Classe della sezione e metodo di calcolo (§4.2.3.1-4.2.3.2)

La sezione è dichiarata di **classe 1 (duttile)**: è in grado di sviluppare una cerniera plastica con la
piena capacità rotazionale (generalmente Cθ ≥ 3). Per le sezioni di **classe 1 e 2** è ammesso il **metodo
plastico (P)** di calcolo della capacità resistente (oltre a quello elastico ed elasto-plastico) → **sì**,
il metodo plastico è ammesso.

## 3. Coefficiente gamma_M (§4.2.4.1.1, Tab. 4.2.VII)

Per la **resistenza della sezione** (verifica di resistenza, non di stabilità) si usa **γM0 = 1,05**.
(γM1 = 1,05 riguarda l'instabilità delle membrature; γM2 = 1,25 la frattura delle sezioni tese forate, qui
non presenti.)

## 4. Resistenza di progetto a flessione (§4.2.4.1.2.3)

Per una sezione di **classe 1** la resistenza di progetto a flessione retta è il **momento resistente
plastico** [4.2.12]:

**Mc,Rd = Mpl,Rd = Wpl · fyk / γM0 = Wpl · 275 / 1,05**

dove **Wpl** è il modulo di resistenza plastico della sezione (dal profilo). La verifica è **MEd/Mc,Rd ≤ 1**
[4.2.11]. Il valore numerico di Wpl e di Mc,Rd non è oggetto della skill.

## Avvertenza

La skill **inquadra** materiale (fyk 275 / ftk 430), classe (1 → metodo plastico ammesso), coefficiente
(γM0 = 1,05) e forma della resistenza (Mc,Rd = Wpl·fyk/γM0); **non fornisce** Wpl, **non calcola** Mc,Rd in
valore e **non esegue** la verifica. Restano compito del progettista strutturale, che deve leggere il §4.2
(e per la classificazione le Tab. 4.2.III-V / EC3) delle NTC 2018.
