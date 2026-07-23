# Nota

Esempio ancorato al **§7.10.5** delle NTC 2018, trascritto in `references/fonti/ntc2018-par-7-10.md`.

Punti verificati sul testo e sull'immagine (pagina PDF 279):

- **no push-over** (§7.10.5.3);
- analisi statica lineare: **Tis ∈ [3·Tbf, 3,0 s]**, **KV ≥ 800·Kesi**, **TV = 2π√(M/KV) < 0,1 s**, no trazione,
  regolare in pianta; edifici **≤ 20 m e ≤ 5 piani**, sottostruttura **T ≤ 0,05 s**, pianta **< 50 m**,
  eccentricità **≤ 3%**;
- condizioni del modello lineare equivalente (§7.10.5.2): rigidezza ≥ 50% secante al 20%, smorzamento < 30%,
  variazione < 10%, incremento forza ≥ 2,5% del peso (operatori e radice verificati sull'immagine, perché
  `pdftotext` li altera).

La skill inquadra i requisiti; **non** calcola Tis/Kesi/TV né esegue l'analisi.
