# Output atteso - Azione di frenamento q3 (§5.1.3.5)

## 1. Formula e limiti

L'azione longitudinale di frenamento o di accelerazione **q3** è funzione del carico verticale totale agente
sulla **corsia convenzionale n. 1** ed è data da [5.1.4]:

    180 kN ≤ q3 = 0,6·(2·Q1k) + 0,10·q1k·w1·L ≤ 900 kN

con w1 larghezza della corsia e L lunghezza della zona caricata. La forza è applicata a livello della
pavimentazione, lungo l'asse della corsia, uniformemente distribuita sulla lunghezza caricata.

## 2. Applicazione ai dati del caso

- **2·Q1k = 600 kN** (tandem dello Schema 1 sulla corsia 1: due assi da 300 kN);
- **q1k = 9,00 kN/m²**, **w1 = 3,00 m**, **L = 20 m**.

Sostituendo:

    q3 = 0,6·600 + 0,10·9,00·3,00·20 = 360 + 54 = 414 kN

Il valore **414 kN** rientra nell'intervallo ammesso **180 kN ≤ q3 ≤ 900 kN**, quindi si assume **q3 = 414
kN**. (Se il calcolo desse un valore < 180 kN si assumerebbe 180 kN; se > 900 kN si assumerebbe 900 kN.)

## 3. Azioni correlate

- La **forza centrifuga q4** (§5.1.3.6) va valutata separatamente in funzione del raggio R (Tab. 5.1.III),
  con Qv = Σ 2·Qik; frenamento e centrifuga entrano in **gruppi di azioni distinti** (Tab. 5.1.IV, gruppi 2a
  e 2b), non sommati come caratteristici nello stesso gruppo.
- Nelle combinazioni SLU si applicano i coefficienti parziali della **Tab. 5.1.V** (traffico γQ sfavorevole
  1,35 in A1) e i coefficienti ψ della **Tab. 5.1.VI**.

## Avvertenza

La skill **inquadra** la formula [5.1.4] e i suoi **limiti** (180-900 kN) e chiarisce quali grandezze vi
entrano (2·Q1k, q1k, w1, L). Il calcolo mostrato è un'**illustrazione** dell'applicazione della formula
normativa: la determinazione della lunghezza caricata L più gravosa, la combinazione con le altre azioni e
le verifiche restano compito del progettista, che deve leggere il §5.1.3 delle NTC 2018.
