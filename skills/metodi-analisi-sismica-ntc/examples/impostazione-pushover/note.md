# Note — Impostazione delle distribuzioni di forze per la pushover

## Perché questo esempio

Mostra le decisioni chiave nell'impostazione di una pushover: punto di controllo, numero e tipo di distribuzioni
(Gruppo 1 + Gruppo 2) e la condizione che rende **obbligatoria** la distribuzione modale (T1 > 1,3·TC).

## Ancoraggio alla fonte

Ogni valore è tratto da `../../references/fonti/ntc2018-par-7-3-2-7-3-4.md` (NTC 2018, §7.3.4.2), verificato
sull'immagine della pagina PDF 224:

- Punto di controllo al **centro di massa dell'ultimo livello** (esclusi torrini); curva di capacità **Fb–dc**.
- **Almeno due distribuzioni** (Gruppo 1 + Gruppo 2).
- Gruppo 1: modo fondamentale **≥ 75%** → forze statiche (§7.3.3.2) o forma modale; distribuzione da analisi dinamica
  (modi **≥ 85%**) **obbligatoria se T1 > 1,3·TC**.
- Gruppo 2: a) uniforme, b) adattiva, c) multimodale con **≥ 6 modi**.

Il confronto numerico (1,3·TC = 0,455 s) è una semplice applicazione aritmetica della soglia sui dati di input.

## Limiti

Non si esegue la pushover né si traccia numericamente la curva di capacità: l'esempio riguarda solo l'impostazione
delle distribuzioni e del punto di controllo.
