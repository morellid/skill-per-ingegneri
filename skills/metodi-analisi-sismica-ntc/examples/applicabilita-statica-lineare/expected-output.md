# Output atteso — Applicabilità dell'analisi lineare statica (NTC 2018 §7.3.2-7.3.3.2)

> Supporto documentale: inquadra l'applicabilità del metodo delle forze laterali. **Non** esegue l'analisi.

## 1. Il metodo è ammissibile in linea di principio? (§7.3.2)

- Il metodo di riferimento resta l'**analisi modale con spettro**; l'**analisi lineare statica** è ammessa **solo** se
  la risposta, in ogni direzione principale, **non dipende significativamente dai modi superiori** (tipicamente
  costruzioni regolari e basse). L'edificio (4 piani, 13 m, regolare) è un candidato tipico.

## 2. Condizioni di applicabilità (§7.3.3.2)

Devono essere entrambe verificate:

- **T1 ≤ 2,5·TC** (o TD): 2,5·TC = 2,5 × 0,40 = **1,00 s**. Essendo **T1 = 0,45 s ≤ 1,00 s** → **verificata**.
- **Regolare in altezza**: dato del problema → **verificata**.

→ L'**analisi lineare statica è applicabile**.

## 3. Coefficiente λ e forze (§7.3.3.2)

- **Fh = Sd(T1)·W·λ/g** (taglio alla base); l'ordinata **Sd(T1)** viene dallo spettro di progetto (§3.2.3.5, fuori
  scope).
- **Coefficiente λ**: vale **0,85** se **T1 < 2·TC e la costruzione ha almeno tre orizzontamenti**, altrimenti **1,0**.
  - 2·TC = 2 × 0,40 = **0,80 s**; **T1 = 0,45 s < 0,80 s** → prima condizione **verificata**.
  - Orizzontamenti: 4 piani ≥ 3 → seconda condizione **verificata**.
  - → **λ = 0,85**.
- **Distribuzione ai piani**: **Fi = Fh·zi·Wi/(Σj zj·Wj)** [7.3.7] — forze proporzionali al prodotto **quota × peso**
  di ciascun impalcato (andamento triangolare inverso, coerente con il modo fondamentale).
- Tenere conto dell'**eccentricità accidentale** del centro di massa (§7.3.3).

## 4. Sintesi

| Verifica | Valore | Esito |
|---|---|---|
| T1 ≤ 2,5·TC | 0,45 ≤ 1,00 s | ✔ |
| Regolare in altezza | sì | ✔ |
| Analisi lineare statica | — | **Applicabile** |
| λ (T1 < 2·TC e ≥ 3 orizzontamenti) | 0,45 < 0,80; 4 piani | **0,85** |

**Fuori scope**: calcolo di Sd(T1) (spettro §3.2.3.5), di q (§7.3.1) e l'esecuzione dell'analisi.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura dei par. 7.3.2-7.3.4 delle NTC 2018 e della relativa Circolare applicativa 2019.**
