# Output atteso — Impostazione delle distribuzioni di forze per la pushover (NTC 2018 §7.3.4.2)

> Supporto documentale: inquadra l'impostazione della pushover. **Non** esegue l'analisi.

## 1. Punto di controllo e curva di capacità (§7.3.4.2)

- Si applicano i carichi gravitazionali e, per la direzione considerata, **forze orizzontali** con risultante (taglio
  alla base) **Fb**, scalate per far crescere **monotonamente** (nei due versi, fino al collasso locale o globale) lo
  spostamento **dc** del **punto di controllo coincidente con il centro di massa dell'ultimo livello** (esclusi
  eventuali torrini). Si considerano anche punti di controllo alternativi (estremità della pianta) quando è
  significativo l'accoppiamento traslazioni-rotazioni.
- Il diagramma **Fb – dc** è la **curva di capacità** della struttura.

## 2. Quante distribuzioni (§7.3.4.2)

- Si devono considerare **almeno due distribuzioni di forze d'inerzia**: una del **Gruppo 1 (principali)** e una del
  **Gruppo 2 (secondarie)**.

## 3. Gruppo 1 — distribuzioni principali

- Il modo fondamentale ha **partecipazione di massa 82% ≥ 75%** → è ammessa una tra:
  - distribuzione **proporzionale alle forze statiche** (§7.3.3.2) — usando come seconda distribuzione la a) del
    Gruppo 2;
  - distribuzione **proporzionale alla forma del modo fondamentale**.
- **Distribuzione modale obbligatoria?** In tutti i casi si può usare la distribuzione delle forze di piano di
  un'analisi dinamica lineare con modi la cui massa complessiva sia **≥ 85%**; questa è **obbligatoria se T1 > 1,3·TC**.
  - 1,3·TC = 1,3 × 0,35 = **0,455 s**; **T1 = 0,55 s > 0,455 s** → **la distribuzione modale (multimodale) è
    obbligatoria** in questo caso.

## 4. Gruppo 2 — distribuzioni secondarie

- Scegliere una tra: a) **uniforme** (accelerazioni costanti lungo l'altezza); b) **adattiva**; c) **multimodale** con
  **≥ 6 modi**.

## 5. Sintesi

| Aspetto | Esito |
|---|---|
| Punto di controllo | Centro di massa dell'**ultimo livello** (esclusi torrini) |
| Curva di capacità | **Fb – dc** |
| N. distribuzioni | **≥ 2** (una Gruppo 1 + una Gruppo 2) |
| Modo fondamentale ≥ 75% | 82% → sì (ammesse forze statiche / forma modale) |
| Distribuzione modale obbligatoria | **Sì** (T1 = 0,55 s > 1,3·TC = 0,455 s) |
| Gruppo 2 | uniforme / adattiva / multimodale (≥ 6 modi) |

**Fuori scope**: esecuzione della pushover, tracciamento numerico della curva di capacità, definizione dello spettro.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura dei par. 7.3.2-7.3.4 delle NTC 2018 e della relativa Circolare applicativa 2019.**
