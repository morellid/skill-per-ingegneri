# Output atteso - Resistenza di progetto di un piolo con testa (§4.3.4.3.1.2)

## 1. Formule e coefficiente

La resistenza di progetto a taglio di un piolo con testa in **soletta piena** è il **minore** fra due
valori:

- **rottura del piolo**: **PRd,a = 0,8·ftk·(π·d²/4)/γV** [4.3.9];
- **rifollamento del calcestruzzo**: **PRd,c = 0,29·α·d²·√(fck·Ecm)/γV** [4.3.10];

con il fattore parziale delle connessioni **γV = 1,25** (§4.3.3).

## 2. Parametri del caso

- **d = 19 mm** (rientra nell'intervallo ammesso **16-25 mm**);
- **ftk = 450 MPa** (≤ 500 MPa, come richiesto);
- **hsc/d = 100/19 ≈ 5,26 > 4** → il coefficiente **α = 1,0** [4.3.11b] (per 3 ≤ hsc/d ≤ 4 sarebbe α =
  0,2·(hsc/d + 1));
- **fck = 25 MPa** (C25/30); **Ecm** è il modulo secante medio del calcestruzzo (§11.2.10.3, non oggetto
  della skill).

Il progettista calcola PRd,a e PRd,c con questi dati (più Ecm) e assume come **resistenza di progetto la
minore** delle due.

## 3. Soletta con lamiera grecata (§4.3.4.3.1.2)

Se la soletta è realizzata con **lamiera grecata**, la resistenza (calcolata per la soletta piena) va
**ridotta**:

- greche **parallele** all'asse del profilo: **kl = 0,6·b0·(hsc − hp)/hp² ≤ 1,0** [4.3.13];
- greche **trasversali**: **kt = 0,7·b0·(hsc − hp)/hp²/nr** [4.3.14] (nr pioli per greca), utilizzabile solo
  se **ftk < 450 MPa** e con kt non superiore ai limiti della **Tab. 4.3.II** (da leggere sulla norma).

(hp altezza della greca, b0 larghezza; per il caso in esame con ftk = 450 MPa la formula di kt non è
applicabile, essendo richiesto ftk < 450 MPa.)

## Avvertenza

La skill **inquadra** le formule (PRd,a, PRd,c), i coefficienti (γV = 1,25, α = 1,0) e i limiti (ftk ≤ 500
MPa, d 16-25 mm) e le riduzioni per lamiera grecata; **non calcola** PRd in valore (serve anche Ecm dal
§11.2) e **non dimensiona** la connessione. Restano compito del progettista, che deve leggere il §4.3 (e la
Tab. 4.3.II / EC4) delle NTC 2018.
