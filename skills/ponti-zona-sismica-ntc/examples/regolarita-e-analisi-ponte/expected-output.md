# Esempio — Output atteso: regolarità KR e ammissibilità dell'analisi statica lineare

> Supporto documentale (NTC 2018, par. 7.9). Non è una verifica strutturale: le verifiche di duttilità/resistenza
> restano a carico del progettista.

## 1. Regolarità e fattore KR (§7.9.2.1)

Per ciascun elemento duttile: **ri = q0·MEd,i/MRd,i** (q0 = 3,5).

| Pila | MEd,i/MRd,i | ri = 3,5·(MEd,i/MRd,i) |
|---|---|---|
| P1 | 4000/5000 = 0,80 | 2,80 |
| P2 | 4500/5000 = 0,90 | 3,15 |
| P3 | 3000/6000 = 0,50 | 1,75 |

- **ri,max = 3,15** (P2), **ri,min = 1,75** (P3).
- **r̃ = ri,max/ri,min = 3,15/1,75 = 1,80**.
- **r̃ = 1,80 < 2** → geometria **regolare** → **KR = 1**. Quindi **q = q0·KR = 3,5·1 = 3,5**.
- (Se fosse stato r̃ ≥ 2, si sarebbe usato **KR = 2/r̃** [7.9.2], ripetendo l'analisi.)

## 2. Ammissibilità dell'analisi statica lineare (§7.9.4.1)

- Caso **b) direzione longitudinale**, ponte rettilineo a travata continua: ammessa se la **massa efficace
  complessiva delle pile** del sistema resistente **≤ 1/5** della massa dell'impalcato.
- Qui la massa efficace complessiva è **1/8** della massa dell'impalcato: **1/8 = 0,125 ≤ 1/5 = 0,20** → **requisito
  soddisfatto**.
- **Esito: l'analisi statica lineare è ammissibile** in direzione longitudinale. (Per la direzione trasversale
  andrebbe verificata la condizione c): b) soddisfatta e simmetria o eccentricità ≤ 5% della lunghezza.)

## Sintesi

- **r̃ = 1,80 < 2** → **KR = 1**, **q = 3,5**.
- Massa efficace pile **1/8 ≤ 1/5** → **analisi statica lineare ammissibile** (direzione longitudinale).

**Fuori scope**: le verifiche di duttilità/resistenza delle pile e i dettagli costruttivi (§7.9.6) restano a
carico del progettista. Non sostituisce il progettista.
