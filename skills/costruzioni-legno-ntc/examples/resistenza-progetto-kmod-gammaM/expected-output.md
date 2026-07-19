# Output atteso - Inquadramento di classe di servizio, kmod e gamma_M

## 1. Classe di servizio (§4.4.5, Tab. 4.4.II)

L'ambiente è un edificio riscaldato e ventilato in cui l'umidità relativa dell'aria supera l'85% **solo per
poche settimane all'anno**: questa è la definizione della **classe di servizio 2** (Tab. 4.4.II). (La
classe 1 richiede UR ≤ 65%; la classe 3 riguarda umidità più elevata.)

## 2. Classe di durata del carico dominante (§4.4.4, Tab. 4.4.I)

La combinazione comprende:

- **peso proprio** → classe **permanente**;
- **neve** a quota < 1000 m → classe da valutarsi in funzione del sito; per il caso in esame si assume la
  classe **media durata** (per as ≥ 1000 m sarebbe almeno media).

Per la scelta di kmod la regola del §4.4.6 impone di usare il valore corrispondente **all'azione di minor
durata** presente nella combinazione: fra "permanente" e "media durata", l'azione di **minor durata** è la
**neve (media durata)**. Quindi si adotta **kmod della classe di durata "media"**.

## 3. Coefficiente kmod (§4.4.6, Tab. 4.4.IV)

Per il **legno lamellare incollato** in **classe di servizio 2** e **classe di durata media**, la
Tab. 4.4.IV fornisce **kmod = 0,80**.

## 4. Coefficiente gamma_M (§4.4.6, Tab. 4.4.III)

La trave **non** è prodotta in serie con controllo continuativo del materiale (coefficiente di variazione
≤ 15% e sistema di qualità), quindi si usa la **colonna A**. Per il **legno lamellare incollato**:

| Materiale | Colonna A | Colonna B |
|---|---|---|
| Legno massiccio | 1,50 | 1,45 |
| **Legno lamellare incollato** | **1,45** | 1,35 |
| LVL, compensato, OSB | 1,40 | 1,30 |
| Unioni | 1,50 | 1,40 |

→ **γM = 1,45**.

## 5. Resistenza di progetto (§4.4.6)

La resistenza di progetto a flessione si ottiene con [4.4.1]:

**fm,d = kmod · fm,k / γM = 0,80 · fm,k / 1,45**

dove **fm,k** è la resistenza caratteristica a flessione del lamellare, presa dal §11.7/progetto (non
oggetto della skill). Il valore numerico di fm,d lo calcola il progettista.

## Avvertenza

La skill **inquadra** le classi e i coefficienti (classe di servizio 2, kmod = 0,80 per durata media,
γM = 1,45); **non fornisce** fm,k, **non calcola** fm,d in valore e **non esegue** la verifica di
resistenza. Restano compito del progettista strutturale, che deve leggere il §4.4 e il §11.7 delle NTC
2018.
