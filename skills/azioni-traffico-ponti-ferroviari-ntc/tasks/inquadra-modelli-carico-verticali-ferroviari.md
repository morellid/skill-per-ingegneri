# Task: inquadra-modelli-carico-verticali-ferroviari

Inquadra i **modelli di carico verticali** da traffico ferroviario e il **coefficiente di adattamento α**
secondo le **NTC 2018 par. 5.2.2.2.1-5.2.2.2.2**. Supporto documentale: **non** esegue combinazioni né verifiche.

## Quando usarla

Il progettista deve definire i carichi verticali da traffico di un ponte ferroviario. Per gli effetti
dinamici (Φ) e le azioni orizzontali usa `inquadra-effetti-dinamici-azioni-orizzontali`.

## Passi

1. **Coefficiente di adattamento α** (§5.2.2.2.1): i valori caratteristici dei modelli di carico vanno
   moltiplicati per **α**, variabile in ragione della tipologia dell'infrastruttura (ferrovie ordinarie,
   leggere, metropolitane…). Per le ferrovie ordinarie i valori di α sono indicati per ciascun modello.

2. **Modello di carico LM 71** (§5.2.2.2.1.1): schematizza il **traffico ferroviario normale**:
   - **4 assi da Q_vk = 250 kN** a interasse **1,60 m** (schema interassi 0,8-1,6-1,6-1,6-0,8 m);
   - **carico distribuito q_vk = 80 kN/m** in entrambe le direzioni, da **0,8 m** dagli assi d'estremità,
     lunghezza illimitata;
   - **eccentricità** del carico dal rapporto **Q_V2/Q_V1 = 1,25** [5.2.1], pari a **s/18** (s = 1435 mm),
     nella direzione più sfavorevole;
   - coefficiente di adattamento **α = 1,1** (ferrovie ordinarie).

3. **Modelli di carico SW** (§5.2.2.2.1.2, Tab. 5.2.I): **SW/0** (traffico normale, per travi continue se più
   sfavorevole dell'LM71) e **SW/2** (traffico **pesante**):

   | Tipo | q_vk [kN/m] | a [m] | c [m] | α |
   |---|---|---|---|---|
   | SW/0 | 133 | 15,0 | 5,3 | 1,1 |
   | SW/2 | 150 | 25,0 | 7,0 | 1,0 |

4. **Treno scarico** (§5.2.2.2.1.3): carico uniformemente distribuito **10,0 kN/m** (per verifiche particolari).

5. **Ripartizione locale** (§5.2.2.2.1.4-5): un carico assiale può ripartirsi su tre traverse (**25% / 50% /
   25%**); per le solette, ripartizione a **45°**; per i rilevati a tergo delle spalle, carico su **3,0 m**
   (senza incremento dinamico).

6. **Carichi sui marciapiedi** (§5.2.2.2.2): **10 kN/m²**, non contemporaneo al transito dei convogli (senza
   incremento dinamico).

Usa la checklist in `../references/estratti/azioni-ferroviari-checklist.md` (sezione 1).

## Output atteso

Un inquadramento dei modelli di carico verticali (LM71, SW/0, SW/2, treno scarico, marciapiedi) con i valori
caratteristici e il coefficiente di adattamento α, con **rinvio ai paragrafi/tabella** NTC. Nessuna
combinazione né verifica.

## Cosa NON fare

- Non **applicare** gli effetti dinamici (Φ) né le azioni orizzontali (usa l'altro task).
- Non **eseguire** le combinazioni delle azioni né le verifiche (SLU/SLE, fatica).
