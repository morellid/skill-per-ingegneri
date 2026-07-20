# Output atteso - Coefficienti, metodo di calcolo e taglio (trave composta)

## 1. Coefficienti parziali (§4.3.3)

Le resistenze di progetto si ottengono con **fd = fk/γM** [4.3.6]. Allo **stato limite ultimo**:

- **calcestruzzo** della soletta: **γC = 1,5** → fcd = fck/1,5;
- **acciaio da carpenteria** (profilo S355): **γA = 1,05** → fyd = fyk/1,05;
- **acciaio da armatura** (B450C): **γS = 1,15** → fsd = fsk/1,15;
- **connessioni** (connettori a taglio): **γV = 1,25**.

Allo **stato limite di esercizio** e nelle situazioni **eccezionali** si assume γM = 1. La classe C25/30
rientra nell'intervallo ammesso **C20/25 - C60/75** (§4.3.3.1.2).

## 2. Metodo di calcolo del momento resistente (§4.3.4.2.1)

La sezione in acciaio è di **classe 2**: per le classi **1 e 2** è ammesso il **metodo plastico** (oltre a
quello elastico ed elasto-plastico). Nel metodo plastico:

- i materiali sono considerati completamente plasticizzati;
- la **tensione di compressione nel calcestruzzo** è assunta pari a **0,85·fcd**;
- la resistenza a **trazione** del calcestruzzo è **trascurata**.

(Il metodo elastico limiterebbe le deformazioni ai limiti elastici fcd/fyd/fsd; l'elasto-plastico usa
un'analisi non lineare ed è applicabile a qualunque classe.)

Per una sezione di classe 1 o 2, l'**armatura di trazione As** in soletta usata per il momento plastico deve
essere in **B450C** e rispettare la condizione [4.3.1].

## 3. Resistenza a taglio verticale (§4.3.4.2.2)

La resistenza a **taglio verticale** della membratura è affidata **interamente alla trave metallica**, la
cui resistenza si calcola con le formule del §4.2.4.1.2 (costruzioni di acciaio).

## Avvertenza

La skill **inquadra** i coefficienti (γC = 1,5, γA = 1,05, γS = 1,15, γV = 1,25), il metodo di calcolo
ammesso (plastico per la classe 2, con cls a 0,85·fcd) e l'attribuzione del taglio; **non calcola** il
momento resistente né dimensiona la sezione. Restano compito del progettista, che deve leggere il §4.3 (e i
§4.1/4.2, §11.2/11.3) delle NTC 2018.
