# Estratto operativo - Spostamenti di interpiano allo SLD (NTC 2018 par. 7.3.6.1)

Checklist di inquadramento per il progettista strutturale. Ogni punto e' ancorato al testo trascritto in
`../fonti/ntc2018-par-7-3-6-1-sld.md`. La skill **inquadra**, non calcola gli spostamenti ne' esegue l'analisi.

## 1. Stato limite e classe d'uso (par. 7.3.6, Tab. 7.3.III)

- [ ] La costruzione e' in **CU I o II**? -> la verifica di rigidezza (RIG) degli elementi strutturali si
      riferisce allo **SLD**.
- [ ] La costruzione e' in **CU III o IV**? -> la verifica si riferisce allo **SLO** e i limiti sono i **2/3**
      di quelli sotto.

## 2. Grandezze (par. 7.3.6.1)

- [ ] **dr** = spostamento di interpiano = differenza tra gli spostamenti del **solaio superiore** e del **solaio
      inferiore**, calcolati con analisi lineare (par. 7.3.3.3) o non lineare (par. 7.3.4), sul **modello senza
      tamponature**.
- [ ] **h** = altezza del piano; **q** = fattore di comportamento.
- [ ] La verifica confronta **q*dr** con il limite (frazione di h) del tipo di tamponatura/struttura.

## 3. Limiti di spostamento di interpiano allo SLD (par. 7.3.6.1)

| Caso | Tipo | Limite | Formula |
|---|---|---|---|
| a | Tamponature **fragili** collegate rigidamente | q*dr **<=** 0,0050 h | [7.3.11a] |
| a | Tamponature **duttili** collegate rigidamente | q*dr **<=** 0,0075 h | [7.3.11b] |
| b | Tamponature **progettate per non subire danni** (deformabilita' intrinseca o collegamenti) | q*dr **<=** drp **<=** 0,0100 h | [7.3.12] |
| c | Struttura portante di **muratura ordinaria** | q*dr **<=** 0,0020 h | [7.3.13] |
| d | Struttura portante di **muratura armata** | q*dr **<=** 0,0030 h | [7.3.14] |
| e | Struttura portante di **muratura confinata** | q*dr **<** 0,0025 h | [7.3.15] |

> **Attenzione all'operatore**: i casi a-d usano **<=** (minore o uguale), il caso e (muratura confinata) usa
> **<** (strettamente minore).

## 4. Regole aggiuntive (par. 7.3.6.1)

- [ ] **CU III e IV** (SLO): limite = **2/3** del valore in tabella (es. tamponature fragili: 2/3 * 0,0050 h).
- [ ] **Coesistenza** di diversi tipi di tamponamento/struttura nello stesso piano -> si assume il **limite piu'
      restrittivo**.
- [ ] Se **dr > 0,005 h** (caso b) -> le **verifiche della capacita' di spostamento** degli elementi non
      strutturali vanno **estese** a tutte le tamponature, alle tramezzature interne e agli impianti.

## Fuori scope (rinvii)

- **Non** calcola gli spostamenti ne' esegue l'analisi (par. 7.3.3.3 lineare / 7.3.4 non lineare); **non**
  determina **q**.
- **Verifiche di resistenza (RES)** e **duttilita' (DUT)** degli elementi strutturali: par. 7.3.6.1 (altre
  sezioni), fuori ambito.
- **Elementi non strutturali** (par. 7.3.6.2) e **impianti** (par. 7.3.6.3): fuori ambito.
