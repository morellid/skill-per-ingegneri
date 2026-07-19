# Output atteso - Applicabilità delle verifiche semplificate (§4.5.6.4)

## 1. Controllo dei requisiti di ammissibilità

Le **verifiche semplificate** per gli **edifici semplici** (§4.5.6.4) sono ammesse solo se sono
soddisfatte **tutte** le condizioni. Confronto con il caso in esame:

| Requisito (§4.5.6.4) | Limite | Caso in esame | Esito |
|---|---|---|---|
| Pareti continue dalle fondazioni alla sommità | richiesto | sì | ✓ |
| Numero di piani (muratura ordinaria) | ≤ **3** (≤ 4 se armata) | 3 | ✓ |
| Altezza di interpiano | ≤ **3,5 m** | 3,2 m | ✓ |
| Rapporto fra i lati in pianta | ≥ **1/3** (≈ 0,333) | 0,75 | ✓ |
| Snellezza convenzionale λ | ≤ **12** | ≈ 10 | ✓ |
| Carico variabile dei solai | ≤ **3,00 kN/m²** | 2,00 kN/m² | ✓ |
| Percentuali minime di parete resistente | Tab. 7.8.II | da verificare | (da controllare) |

Tutti i requisiti geometrici e di carico indicati sono rispettati; resta da controllare il requisito
sulle **percentuali di parete resistente** in ciascuna direzione (Tab. 7.8.II, richiamata dal §4.5.6.4).

→ Se anche quest'ultimo è soddisfatto, l'edificio è **"semplice"** e si possono applicare le **verifiche
semplificate**.

## 2. Coefficiente gamma_M per la via semplificata

Per le verifiche semplificate degli edifici semplici il §4.5.6.4 prescrive un coefficiente parziale
**maggiorato**: **γM = 4,2**, indipendentemente dalla categoria degli elementi e dalla classe di
esecuzione (è un valore cautelativo che sostituisce la Tab. 4.5.II ai soli fini di questa via
semplificata).

## 3. Verifica sulle tensioni (§4.5.6.4)

La verifica si riduce al controllo della **tensione media di compressione** al piano considerato:

**σ = N / (0,65 · A) ≤ fk / γM = fk / 4,2**

dove:

- **N** è il carico verticale totale alla base del muro nella **combinazione caratteristica** (rara),
  assumendo **γG = γQ = 1**;
- **A** è l'**area totale dei muri portanti** allo stesso piano;
- il fattore **0,65** tiene conto convenzionalmente dell'eccentricità e della snellezza.

## Avvertenza

La skill **inquadra** i requisiti di ammissibilità e la forma della verifica semplificata; **non calcola**
N, A, σ né fk, e **non decide** l'esito della verifica. La scelta della via semplificata e i calcoli
restano compito del progettista strutturale, che deve leggere il §4.5.6.4 (e la Tab. 7.8.II) delle
NTC 2018. La via semplificata **non** esime dai requisiti di progettazione **sismica** (§7.8), qui non
trattati.
