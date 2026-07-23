# Esempio — Output atteso: requisiti dei materiali e scelta di αu/α1 (muratura ordinaria)

> Supporto documentale (NTC 2018, par. 7.8.1). Non è una verifica strutturale: le verifiche dei pannelli
> (§§ 7.8.2-7.8.4) restano a carico del progettista.

## 1. Classe di duttilità e coefficienti parziali (§7.8.1.1)

- Nel rispetto dei §§ 4.5 e 11.10, la costruzione in muratura è **moderatamente dissipativa** → classe di
  duttilità **CD"B"**.
- I **coefficienti parziali di sicurezza** per la resistenza del materiale (Cap. 4) possono essere **ridotti del
  20%** e comunque **non sotto 2**.

## 2. Requisiti dei materiali (§7.8.1.2, agS > 0,075g)

| Requisito (§7.8.1.2) | Limite | Valore proposto | Esito |
|---|---|---|---|
| Percentuale volumetrica dei vuoti | ≤ 45% | 42% | ✅ |
| f_bk direzione portante (area lorda) | ≥ 5 MPa (o f_b ≥ 6 MPa) | 5,5 MPa | ✅ |
| f_bk direzione perpendicolare (nel piano) | ≥ 1,5 MPa | 1,8 MPa | ✅ |
| Malta di allettamento (muratura ordinaria) | ≥ 5 MPa (M5) | M5 (5 MPa) | ✅ |
| Setti paralleli al piano del muro | continui e rettilinei | sì | ✅ |

Nessun giunto sottile né giunto verticale a secco: i relativi limiti (altezza/piani, setti ≥ 7/10 mm,
foratura ≤ 55%) **non si applicano**. **Tutti i requisiti del §7.8.1.2 risultano soddisfatti** (restano da
rispettare anche quelli del §4.5.2, categoria degli elementi).

## 3. Fattore di comportamento αu/α1 (§7.8.1.3)

- q0 dalla **Tab. 7.3.II**; si assume **q = q0·KR** (KR al §7.3.1).
- In **assenza di analisi statica non lineare**, per la **muratura ordinaria** si adotta **αu/α1 = 1,7**
  (valore forfettario di norma). Con pushover si potrebbe calcolare αu/α1, comunque **≤ 2,5**.

## Sintesi

- **CD"B"**; coefficienti parziali riducibili del 20% (≥ 2).
- Materiali proposti **conformi** al §7.8.1.2 (per agS > 0,075g).
- **αu/α1 = 1,7** (muratura ordinaria, senza analisi non lineare).

**Fuori scope**: verifiche di pressoflessione/taglio dei pannelli (§§ 7.8.2), metodi di analisi (§7.8.1.5),
requisiti statici §4.5 e framework del fattore q §7.3.1 (skill dedicate). Non sostituisce il progettista.
