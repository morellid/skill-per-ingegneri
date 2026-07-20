# Task - Inquadra la verifica SLU a sfilamento dei tiranti (§6.6.2)

## Obiettivo

Inquadrare la **verifica di sicurezza allo SLU a sfilamento** di un tirante di ancoraggio: condizione [6.2.1],
combinazione di verifica, **resistenza di progetto Rad** e determinazione della **resistenza caratteristica
Rak**, secondo le NTC 2018 §6.6.2.

## Input richiesti

- tipo di ancoraggio (**temporaneo / permanente**) e funzione (attivo / passivo);
- massima **azione di progetto Ed** sul tirante;
- modalità di determinazione della resistenza: **prove di progetto** (Ra,m medio/minimo, numero ancoraggi di
  prova) o **calcolo analitico** (Ra,c medio/minimo, numero profili di indagine).

## Procedura (ancorata al testo)

1. **Impostazione della verifica** (§6.6.2). Verificare la condizione **[6.2.1] Ed ≤ Rad** rispetto allo stato
   limite di **sfilamento** della fondazione dell'ancoraggio, con la combinazione **A1+M1+R3** (coefficienti
   Tab. 6.2.I, 6.2.II e 6.6.I).

2. **Resistenza di progetto** (Tab. 6.6.I). **Rad = Rak / γR** con **γR = 1,1** per ancoraggi **temporanei** e
   **γR = 1,2** per ancoraggi **permanenti**.

3. **Resistenza caratteristica Rak**. Scegliere il metodo:
   - **(a) da prove di progetto** [6.6.1]: **Rak = Min{ Ra,m,medio / ξa1 ; Ra,m,min / ξa2 }**, con ξa1/ξa2 da
     **Tab. 6.6.II** in funzione del numero di ancoraggi di prova (1 → 1,5/1,5; 2 → 1,4/1,3; >2 → 1,3/1,2);
   - **(b) da calcolo analitico** [6.6.2]: **Rak = Min{ Ra,c,medio / ξa3 ; Ra,c,min / ξa4 }**, con ξa3/ξa4 da
     **Tab. 6.6.III** in funzione del numero di profili di indagine (1 → 1,80/1,80 … ≥5 → 1,60/1,55). Nella
     valutazione analitica **non** si applicano γ ai parametri del terreno (M1).

4. **Esito**. Confrontare **Ed** con **Rad**: la verifica è soddisfatta se **Ed ≤ Rad**.

## Output

Una nota che indichi: la **combinazione** (A1+M1+R3), il **γR** applicabile (1,1 o 1,2), il metodo di
determinazione di **Rak** con i **fattori di correlazione ξ** (Tab. 6.6.II o 6.6.III) e l'esito del confronto
**Ed ≤ Rad**. **La skill inquadra la procedura e i coefficienti; non calcola Ra,m/Ra,c né dimensiona il
tirante.**
