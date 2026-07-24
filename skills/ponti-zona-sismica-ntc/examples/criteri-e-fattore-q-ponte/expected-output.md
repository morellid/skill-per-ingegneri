# Esempio — Output atteso: criteri e riduzione di q0 per una pila in c.a. (νk)

> Supporto documentale (NTC 2018, par. 7.9). Non è una verifica strutturale: le verifiche di duttilità/resistenza
> delle pile restano a carico del progettista.

## 1. Criteri di progettazione (§7.9.2)

- Con comportamento **dissipativo**, la struttura deve dare luogo a un **meccanismo dissipativo stabile** con
  **dissipazione limitata alle pile**; il comportamento inelastico deve essere **flessionale**, con esclusione
  della rottura per taglio.
- Devono restare **elastici** (progettazione in capacità): **impalcato, apparecchi di appoggio, strutture di
  fondazione, spalle** e le pile che non scambiano azioni orizzontali con l'impalcato.

## 2. Compressione normalizzata νk (§7.9.2.1)

- Calcolo: **νk = NEd/(Ac·fck) = 6.000.000 N / (1.000.000 mm² × 30 MPa) = 6.000.000 / 30.000.000 = 0,20**.
- **νk = 0,20 ≤ 0,3** → **ammissibile** e i valori di q0 della Tab. 7.3.II **valgono senza riduzione**. (Il limite
  massimo invalicabile è νk = 0,6; per 0,3 < νk < 0,6 si applicherebbe la riduzione [7.9.1].)

## 3. Fattore di comportamento adottato

- Essendo **νk = 0,20 ≤ 0,3**, si mantiene **q0 = 3,5** (valore di Tab. 7.3.II), senza riduzione.
- Il fattore di comportamento finale è **q = q0·KR** (KR dalla verifica di regolarità, §7.9.2.1); da valutare a
  parte. Va inoltre applicato, dove pertinente, **λ(α)** con α = L/H.

*(Nota: se fosse stato, ad esempio, νk = 0,45, la riduzione [7.9.1] avrebbe dato*
*q0(νk) = q0 − [(νk/0,3) − 1]·(q0 − 1) = 3,5 − [(0,45/0,3) − 1]·(3,5 − 1) = 3,5 − 0,5·2,5 = 2,25.)*

## Sintesi

- Dissipazione **nelle pile**; impalcato/appoggi/fondazioni/spalle **elastici**.
- **νk = 0,20 ≤ 0,3** → q0 non ridotto.
- **q0 = 3,5** (da comporre con KR e λ(α)).

**Fuori scope**: verifiche di duttilità/resistenza delle pile, dettagli costruttivi (§7.9.6), carichi da traffico
(§§ 5.1.3/5.2.2) e fattore q per gli edifici (§7.3.1). Non sostituisce il progettista.
