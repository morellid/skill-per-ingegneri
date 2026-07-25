# Note — Gerarchia delle resistenze al nodo trave-pilastro

## Perché questo esempio

Mostra la **catena della gerarchia delle resistenze** (capacity design) del c.a. sismico: flessione trave → taglio
trave (amplificato di γRd) → nodo pilastro forte-trave debole → limite di compressione e taglio del pilastro. È il
cuore del §7.4.4.

## Ancoraggio alla fonte

Ogni formula/valore è tratto da `../../references/fonti/ntc2018-par-7-4.md` (NTC 2018, §7.4.4), verificato
sull'immagine delle pagine PDF 229/230:

- γRd da **Tab. 7.2.I** (§7.4.4).
- Taglio travi: domanda da equilibrio della trave incernierata con **capacità flessionale amplificata di γRd**; CD"A"
  ctgθ=1, VR1 [7.4.1], armature ±45° VEd,max ≤ As·fyd/√2 [7.4.2].
- Nodo: **ΣMc,Rd ≥ γRd·ΣMb,Rd** [7.4.4], escluso sommità ultimo orizzontamento.
- Pilastri pressoflessione: compressione **≤ 55% (CD"A") / 65% (CD"B")** della capacità del solo cls.

## Limiti

Non si eseguono le verifiche numeriche complete né si dimensionano le armature (§7.4.6): l'esempio inquadra la logica
della progettazione in capacità e i relativi riferimenti normativi.
