# Nota

Esempio ancorato al **§4.2.4.1.2.1** (trazione) e al **§4.2.4.1.3.1** (aste compresse) delle NTC 2018, con
la **Tab. 4.2.VII** (coefficienti γM), trascritti in `references/fonti/ntc2018-par-4-2.md`.

Punti verificati sul testo:

- **Trazione con fori**: Nt,Rd = minore fra **Npl,Rd = A·fyk/γM0** [4.2.6] e **Nu,Rd = 0,9·Anet·ftk/γM2**
  [4.2.7]; **γM0 = 1,05**, **γM2 = 1,25** (Tab. 4.2.VII).
- **Stabilità asta compressa**: **Nb,Rd = χ·A·fyk/γM1** [4.2.42], **γM1 = 1,05**; χ da [4.2.44]; λ̄ da
  [4.2.45].
- **Instabilità trascurabile** se **λ̄ < 0,2** o **NEd < 0,04·Ncr**.
- **Limiti di snellezza** λ = l0/i: **200 (principali) / 250 (secondarie)** [4.2.47].
- fyk/ftk per S355 (t ≤ 40 mm): 355 / 510 N/mm² (Tab. 4.2.I).

La skill **non** calcola A, Anet, Ncr, χ né le resistenze: fornisce solo l'inquadramento di formule e
coefficienti. Le curve di instabilità (α) sono nella Tab. 4.2.VIII (figura, non riprodotta → norma/EC3).
