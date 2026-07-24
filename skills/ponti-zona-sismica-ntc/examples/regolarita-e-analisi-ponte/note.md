# Nota — regolarità KR e analisi statica lineare

- **Ancoraggio**: ri = q0·MEd,i/MRd,i, il criterio r̃ = rmax/rmin < 2 (KR = 1) / ≥ 2 (KR = 2/r̃, [7.9.2]) e i
  requisiti dell'analisi statica lineare provengono da `../../references/fonti/ntc2018-par-7-9.md` (§7.9.2.1 e
  §7.9.4.1), verificati sull'immagine della pagina PDF 270 (GU 266).
- **Punto didattico**: mostra i due controlli di inquadramento — la regolarità (che fissa KR e quindi q = q0·KR)
  e l'ammissibilità dell'analisi statica lineare (massa efficace pile ≤ 1/5 massa impalcato).
- **Esclusione di pile**: nel calcolo di rmax/rmin si possono escludere le pile la cui resistenza a taglio non
  ecceda il 20% della resistenza sismica totale diviso il numero di elementi; nell'esempio tutte le pile sono
  incluse.
- **Direzione trasversale**: richiede la condizione c) (b) soddisfatta + simmetria o eccentricità ≤ 5%): non
  valutata qui perché l'input riguarda la direzione longitudinale.
- **Limite della skill**: nessuna verifica di resistenza; KR e q si compongono poi con λ(α) e con le verifiche a
  carico del progettista.
