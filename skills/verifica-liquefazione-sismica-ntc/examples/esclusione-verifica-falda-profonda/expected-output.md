# Output atteso

## Criterio (NTC 2018 §7.11.3.4.2)

La verifica a liquefazione **può essere omessa** quando si manifesta **almeno una** delle quattro circostanze
di esclusione. Occorre quindi controllarle rispetto ai dati del sito.

## Confronto con i dati del sito

| Condizione di esclusione (§7.11.3.4.2) | Dato del sito | Soddisfatta? |
|---|---|---|
| (1) a_max in campo libero **< 0,1 g** | a_max ≈ **0,18 g** | **No** (0,18 ≥ 0,1) |
| (2) **falda > 15 m** (piano campagna sub-orizzontale, fondazioni superficiali) | falda ≈ **18 m**, fondazioni superficiali, piano campagna sub-orizzontale | **Sì** (18 > 15) |
| (3) sabbie pulite con (N₁)₆₀ > 30 o q_c1N > 180 | dato non fornito | non necessario valutarla |
| (4) granulometria fuori Fig. 7.11.1 (U_c < 3,5 / > 3,5) | dato non fornito | non necessario valutarla |

## Conclusione

È soddisfatta la **condizione (2)**: la **profondità media stagionale della falda (≈ 18 m) è superiore a
15 m**, con piano campagna sub-orizzontale e fondazioni superficiali. Poiché **basta una** circostanza,
la **verifica a liquefazione può essere omessa** ai sensi del **§7.11.3.4.2**.

## Note

- La condizione (1) **non** è soddisfatta (a_max ≥ 0,1 g); le NTC ricordano che, quando la condizione 1 non è
  soddisfatta, le indagini devono determinare i parametri per le condizioni 2, 3 e 4 — qui la (2) è
  verificata e sufficiente.
- L'esito va comunque **motivato dal progettista** nella relazione geotecnica, documentando il regime della
  falda (valore **medio stagionale**) e la natura del piano campagna e delle fondazioni.
- Se invece la falda fosse stata a profondità ≤ 15 m e nessun'altra condizione fosse ricorsa, sarebbe stato
  necessario impostare la verifica del coefficiente di sicurezza (§7.11.3.4.3, vedi task
  `inquadra-metodo-coefficiente-sicurezza`).
