# Nota — criteri e riduzione di q0 per una pila in c.a.

- **Ancoraggio**: la definizione di νk = NEd/(Ac·fck), i limiti 0,3/0,6 e la formula [7.9.1] provengono da
  `../../references/fonti/ntc2018-par-7-9.md` (§7.9.2.1), verificati sull'immagine della pagina PDF 270 (GU 266).
- **Unità coerenti**: NEd in N, Ac in mm², fck in MPa (N/mm²) → νk adimensionale. Nell'esempio 6·10⁶ N /
  (10⁶ mm² · 30 N/mm²) = 0,20.
- **Perché conta**: se νk supera 0,3 i q0 di Tab. 7.3.II non valgono «pieni» e vanno ridotti con [7.9.1] fino al
  limite νk = 0,6 (oltre il quale la sezione non è ammessa come dissipativa). L'esempio mostra il caso favorevole
  e, in nota, il calcolo per un νk intermedio.
- **q0 non numerico dalla skill**: il valore di q0 (Tab. 7.3.II) è un input di progetto — la skill non lo calcola,
  ma applica la riduzione per νk e rinvia a KR/λ(α).
- **Limite della skill**: nessuna verifica di duttilità/resistenza; capacità delle pile a carico del progettista.
