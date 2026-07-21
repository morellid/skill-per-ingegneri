# Output atteso - Inquadramento della categoria e del coefficiente gamma_M

## 1. Classificazione dell'elemento (§4.5.2.2, Tab. 4.5.Ia)

Con **percentuale di foratura Π = 38%**, l'elemento in laterizio ricade nell'intervallo **15% < Π ≤ 45%**:
è un **elemento semipieno** (Tab. 4.5.Ia). Vanno inoltre verificati i requisiti sui setti minimi (7 mm
interni, 10 mm esterni per il laterizio) e sull'area di ciascun foro, secondo la stessa tabella.

## 2. Categoria dell'elemento (§4.5.2.2 / §11.10.1)

Gli elementi sono dichiarati **di categoria I**: la categoria dipende dal livello di controllo di
produzione e dalla probabilità che la resistenza a compressione sia inferiore a quella caratteristica
dichiarata (definizione al §11.10.1, richiamato dal §4.5). La categoria (I o II) è uno dei due parametri
che entrano nella Tab. 4.5.II.

## 3. Classe di esecuzione (§4.5.6.1, Tab. 4.5.II nota)

La **classe di esecuzione** distingue due livelli di controllo in cantiere:

- **Classe 2**: sono garantiti (a) la **supervisione delle operazioni** da parte di un **capocantiere**
  qualificato e (b) il **controllo ispettivo** di operazioni e materiali da parte del **direttore dei
  lavori**.
- **Classe 1**: oltre ai requisiti della classe 2, occorre anche il **controllo in loco** della **malta**
  a resistenza garantita (o preparata a piè d'opera con dosaggio "a volume" nei modi previsti) e il
  controllo del **dosaggio dei componenti**.

Nel caso descritto sono presenti solo supervisione e controllo ispettivo, **senza** il controllo del
dosaggio/malta in loco: siamo quindi in **classe di esecuzione 2**.

## 4. Coefficiente parziale gamma_M (Tab. 4.5.II)

Incrociando **categoria I**, **malta a prestazione garantita** e **classe di esecuzione 2** nella
**Tab. 4.5.II**:

| Materiale | Classe 1 | Classe 2 |
|---|---|---|
| Elementi cat. I, malta a prestazione garantita | 2,0 | **2,5** |
| Elementi cat. I, malta a composizione prescritta | 2,2 | 2,7 |
| Elementi cat. II, ogni tipo di malta | 2,5 | 3,0 |

→ **γM = 2,5**.

## 5. Resistenze di progetto (§4.5.6.1)

Note le resistenze caratteristiche (fk a compressione e fvk a taglio, da §11.10.3 o prove), le resistenze
di progetto si ottengono come:

- **fd = fk / γM = fk / 2,5**;
- **fvd = fvk / γM = fvk / 2,5**.

I valori numerici di fk e fvk non sono forniti in questo esempio: vanno assunti dal progetto/§11.10 e non
sono oggetto della skill.

## Avvertenza

La skill **inquadra** i criteri di classificazione e il coefficiente γM applicabile; **non calcola** fk,
fvk né le resistenze di progetto in valore, e **non esegue** le verifiche. Restano compito del progettista
strutturale, che deve leggere il testo del §4.5 e del cap. 11.10 delle NTC 2018.
