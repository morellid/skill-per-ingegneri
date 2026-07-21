# Task - Inquadra i carichi permanenti (G1/G2) e le riduzioni dei sovraccarichi (§3.1.2, 3.1.3, 3.1.4.1)

## Obiettivo

Inquadrare i **carichi permanenti** - pesi propri strutturali **G1** (Tab. 3.1.I) e non strutturali
**G2** (con il carico equivalente dei divisori) - e i **coefficienti riduttivi** dei sovraccarichi per
area di influenza (**α_A**) e numero di piani (**α_n**) (NTC 2018 §3.1.2, 3.1.3, 3.1.4.1).

## Input richiesti

- materiali strutturali e loro geometria (per G1);
- elementi non strutturali (tamponature, divisori, massetti, pavimenti, impianti) e, per i tramezzi, il
  **peso proprio per unità di lunghezza G2**;
- per le riduzioni: **area di influenza A** dell'elemento, **numero di piani n**, categoria d'uso e
  coefficiente **ψ0** (Tab. 2.5.I).

## Procedura (ancorata al testo)

1. **Pesi propri strutturali G1** (§3.1.2). Da geometria e **pesi dell'unità di volume** della **Tab.
   3.1.I** (c.a. **25,0 kN/m³**, acciaio **78,5**, ecc.); per materiali non in tabella, indagini/normative
   trattando i valori nominali come caratteristici.

2. **Carichi permanenti non strutturali G2** (§3.1.3). Da geometria e pesi dei materiali non strutturali.
   Per abitazioni/uffici, i **tramezzi** possono essere ragguagliati a un **carico equivalente distribuito
   g2** in funzione del peso lineare **G2**: **≤1,00 → 0,40**; **1-2 → 0,80**; **2-3 → 1,20**; **3-4 →
   1,60**; **4-5 → 2,00 kN/m²**. Con **G2 > 5,00 kN/m** → considerare l'**effettivo posizionamento** sul
   solaio (non il carico equivalente).

3. **Riduzione per area di influenza α_A** (§3.1.4.1). Per le categorie **A, B, C, D, H, I** e per un
   elemento orizzontale (trave), il sovraccarico può essere ridotto con **α_A = (5/7)·ψ0 + 10/A ≤ 1,0**
   (A in m²). Per **C e D**, **α_A ≥ 0,6**.

4. **Riduzione per numero di piani α_n** (§3.1.4.1). Per le **sole categorie A÷D** e per membrature
   verticali (pilastri/setti) di edifici con **più di 2 piani**, riduzione con **α_n = (2 + (n − 2)·ψ0) /
   n** (n = piani caricati).

5. **Non combinabili**. I coefficienti **α_A e α_n non si combinano** tra loro.

## Output

Una nota che indichi: i pesi dell'unità di volume rilevanti (Tab. 3.1.I) per G1; l'eventuale carico
equivalente **g2** dei tramezzi (o il posizionamento effettivo se G2 > 5 kN/m); e i coefficienti riduttivi
**α_A** e/o **α_n** applicabili (senza combinarli), con i limiti (≥0,6 per C/D). **La skill inquadra i
valori e le formule; non calcola i carichi di progetto né dimensiona.**
