# Task - Inquadra le verifiche SLU (resistenza e stabilità) e SLE del legno (§4.4.7, 4.4.8)

## Obiettivo

Inquadrare le **verifiche agli stati limite ultimi** (resistenza e stabilità) e le **verifiche agli stati
limite di esercizio** (deformabilità e frecce) degli elementi in legno, secondo le NTC 2018 §4.4.

## Input richiesti

- tipo di sollecitazione dell'elemento (trazione, compressione, flessione, taglio, torsione, combinate);
- geometria (sezione, luce L, snellezza, presenza di ritegni torsionali/controventi);
- classe di servizio e tipo di prodotto (per kdef e per βc);
- resistenze e moduli elastici caratteristici (dal §11.7/progetto).

## Procedura (ancorata al testo)

1. **Verifiche di resistenza SLU** (§4.4.8.1). Individuare gli stati limite pertinenti: **trazione**
   [4.4.2] e **compressione** [4.4.3] parallele alla fibratura, **compressione perpendicolare** [4.4.4],
   **flessione** [4.4.5] con **km = 0,7 (sezioni rettangolari) / 1,0 (altre)**, **tensoflessione** [4.4.6],
   **pressoflessione** [4.4.7], **taglio** [4.4.8], **torsione** [4.4.9] con ksh e la combinazione
   **taglio+torsione** [4.4.10]. Le resistenze di progetto sono Xd = kmod·Xk/γM (§4.4.6).

2. **Verifiche di stabilità SLU** (§4.4.8.2). Usare i moduli **caratteristici (frattile 5%)**. Per gli
   **elementi inflessi** (svergolamento) [4.4.11]: σm,d/(kcrit,m·fm,d) ≤ 1 con kcrit,m = 1 se
   **λrel,m ≤ 0,75** [4.4.12]. Per gli **elementi compressi** (instabilità di colonna) [4.4.13]:
   σc,0,d/(kcrit,c·fc,0,d) ≤ 1 con kcrit,c = 1 se **λrel,c ≤ 0,3**, altrimenti [4.4.15-16] con
   **βc = 0,2 (massiccio) / 0,1 (lamellare)**.

3. **Verifiche SLE** (§4.4.7). Valutare la **deformazione istantanea** (moduli medi) e quella a **lungo
   termine** (moduli ridotti col fattore **1/(1 + kdef)**, kdef da Tab. 4.4.V). Controllare le **frecce**:
   istantanea da soli variabili (comb. rara) **< L/300** e finale **< L/200** (L = luce; per mensole,
   doppio dello sbalzo). Considerare la deformabilità dei collegamenti.

4. **Esecuzione e stabilità geometrica** (§4.4.15). Verificare che lo scostamento dalla geometria teorica
   rientri in **1/500 (lamellare) / 1/300 (massiccio)** della distanza tra vincoli, per le membrature
   sensibili all'instabilità.

## Output

Una nota che elenchi: le **verifiche SLU di resistenza** pertinenti (con km per la flessione) e le
**verifiche di stabilità** (kcrit,m / kcrit,c con le soglie di λrel); le **verifiche SLE** con le frecce
limite (L/300 istantanea, L/200 finale) e il fattore 1/(1+kdef). **La skill inquadra i criteri e le
formule; non esegue le verifiche né dimensiona la struttura.**
