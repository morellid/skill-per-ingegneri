# Note - Carico dei tramezzi e riduzione del sovraccarico

- Fonte: `references/fonti/ntc2018-par-3-1.md` (§3.1.3 correlazione g2/G2; §3.1.4.1 riduzioni α_A/α_n).
- Punti verificati sul testo:
  - **g2** dei tramezzi in funzione di **G2**: ≤1,00→0,40; **1-2→0,80**; 2-3→1,20; 3-4→1,60; 4-5→2,00
    kN/m². G2 = 1,5 kN/m ⇒ **g2 = 0,80 kN/m²**. G2 > 5,00 kN/m → posizionamento effettivo.
  - **α_A = (5/7)·ψ0 + 10/A ≤ 1,0** (cat. A,B,C,D,H,I); per C/D **≥ 0,6** (per A nessun limite inferiore
    di 0,6). ψ0 dalla Tab. 2.5.I (non riprodotta; cat. A ψ0=0,7).
  - **α_n = (2 + (n−2)·ψ0)/n** (cat. A÷D, edifici > 2 piani).
  - **α_A e α_n NON combinabili**.
- La skill fornisce formule e vincoli: **non** calcola i valori numerici (dipendono da ψ0), **non**
  dimensiona.
