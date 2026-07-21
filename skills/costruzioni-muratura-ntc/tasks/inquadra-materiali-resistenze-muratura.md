# Task - Inquadra materiali, categorie e resistenze di progetto della muratura (§4.5.2, 4.5.3, 4.5.6.1)

## Obiettivo

Inquadrare la **classificazione degli elementi** resistenti, le **caratteristiche meccaniche** della
muratura e le **resistenze di progetto** con il coefficiente parziale **γM** (Tab. 4.5.II), secondo le NTC
2018 §4.5.

## Input richiesti

- tipo di elemento (laterizio/calcestruzzo/pietra) e sua **percentuale di foratura Π**;
- **categoria degli elementi** (I o II, §11.10.1) e tipo di malta (a prestazione garantita / a
  composizione prescritta);
- **classe di esecuzione** prevista (1 o 2);
- resistenze caratteristiche **fk** e **fvk** (dal progetto/§11.10.3).

## Procedura (ancorata al testo)

1. **Classificazione elementi** (§4.5.2.2). Calcolare **Π = 100 F/A** e classificare (Tab. 4.5.Ia
   laterizio / 4.5.Ib calcestruzzo): **pieni** (Π ≤ 15%), **semipieni** (15% < Π ≤ 45%), **forati** (45% <
   Π ≤ 55%). Verificare gli spessori minimi dei setti. Individuare la **categoria I o II** dell'elemento.

2. **Caratteristiche meccaniche** (§4.5.3). Individuare **fk**, **fvk0**, **E**, **G**; se **fk ≥ 8 MPa**
   serve il **controllo sperimentale** (§11.10). I valori vanno indicati nel progetto.

3. **Resistenze di progetto** (§4.5.6.1). **fd = fk/γM** e **fvd = fvk/γM**, con **γM** dalla **Tab.
   4.5.II** in funzione della **classe di esecuzione** e della **categoria** degli elementi:
   - cat. I, malta a prestazione garantita → **2,0** (classe 1) / **2,5** (classe 2);
   - cat. I, malta a composizione prescritta → **2,2** / **2,7**;
   - cat. II, ogni tipo di malta → **2,5** / **3,0**.
   La **classe di esecuzione** (1 o 2) dipende dai controlli in cantiere previsti (supervisione, controllo
   ispettivo, controllo di malta/cls e dosaggio).

4. **Muratura armata** (§4.5.7, se pertinente). Barre ≥ 5 mm; percentuali minime di armatura; malta ≥ 10
   MPa, cls ≥ C12/15; **γs = 1,15**.

## Output

Una nota che indichi: la **classe dell'elemento** (pieno/semipieno/forato) e la **categoria** (I/II); le
caratteristiche meccaniche rilevanti; il **coefficiente γM** applicabile (Tab. 4.5.II) e le **resistenze
di progetto fd/fvd**. **La skill fornisce i criteri e i coefficienti; non calcola fk/fvk né le resistenze
di progetto in valore, che restano compito del progettista.**
