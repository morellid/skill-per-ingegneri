# Task - Inquadra l'analisi globale e le verifiche di stabilità dell'acciaio (§4.2.3, 4.2.4.1.3)

## Obiettivo

Inquadrare la scelta del **metodo di analisi globale** (effetti del secondo ordine e delle imperfezioni) e
le **verifiche di stabilità delle membrature** (aste compresse e travi inflesse), secondo le NTC 2018 §4.2.

## Input richiesti

- schema strutturale (telaio/controventato) e sensibilità agli effetti del secondo ordine;
- geometria delle membrature (lunghezza, vincoli, raggio d'inerzia, tipo di sezione) e sollecitazioni
  (compressione, flessione, presso-flessione);
- grado dell'acciaio e classe della sezione.

## Procedura (ancorata al testo)

1. **Metodo di analisi e secondo ordine** (§4.2.3.3-4.2.3.4). Verificare se l'analisi del **primo ordine**
   è ammessa: gli effetti del secondo ordine sono trascurabili se **α_cr = Fcr/FEd ≥ 10** (analisi
   elastica) o **≥ 15** (analisi plastica) [4.2.1]. Altrimenti condurre l'analisi del secondo ordine.
   Considerare le **imperfezioni** globali (telai/controventi) e locali; l'errore di verticalità è
   trascurabile se **HEd ≥ 0,15·VEd** [4.2.2].

2. **Stabilità delle aste compresse** (§4.2.4.1.3.1). Verificare **NEd/Nb,Rd ≤ 1** [4.2.41] con
   **Nb,Rd = χ·A·fyk/γM1** (classi 1-3) [4.2.42] o χ·Aeff·fyk/γM1 (classe 4). Calcolare la **snellezza
   normalizzata λ̄ = √(A·fyk/Ncr)** [4.2.45] (Ncr carico critico elastico con lunghezza d'inflessione
   l0 = β·l) e il **coefficiente χ = 1/(Φ + √(Φ² − λ̄²)) ≤ 1** [4.2.44], con **Φ = 0,5·[1 + α·(λ̄ − 0,2) +
   λ̄²]** e α (fattore di imperfezione) dalla curva di instabilità appropriata (Tab. 4.2.VIII, da norma/EC3).
   L'instabilità è **trascurabile se λ̄ < 0,2** o **NEd < 0,04·Ncr**. Rispettare i limiti di snellezza
   **λ = l0/i ≤ 200 (principali) / 250 (secondarie)** [4.2.47].

3. **Stabilità delle travi inflesse** (§4.2.4.1.3.2). Verificare lo **svergolamento** (instabilità
   flesso-torsionale) con χLT e λ̄LT = √(Wy·fyk/Mcr) [4.2.51], usando il fattore di imperfezione **αLT =
   0,21/0,34/0,49/0,76** per le curve **a/b/c/d** (Tab. 4.2.IX), con l'attribuzione della curva in funzione
   del tipo di profilo e del rapporto h/b.

4. **Membrature presso-inflesse** e **pannelli di classe 4** (§4.2.4.1.3.3-4): riferimento a normative di
   comprovata validità (UNI EN 1993).

## Output

Una nota che indichi: il **metodo di analisi** ammesso (con la verifica α_cr ≥ 10/15); le **verifiche di
stabilità** pertinenti (aste compresse con χ, λ̄, soglie λ̄ < 0,2 e limiti 200/250; travi inflesse con χLT
e le curve αLT). **La skill inquadra i criteri e le formule; non esegue le verifiche né calcola χ, Ncr o
Mcr in valore.**
