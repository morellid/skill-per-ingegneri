# Task - Inquadra corsie convenzionali, Schemi di Carico e intensità (§5.1.3.3)

## Obiettivo

Inquadrare la **definizione dei carichi verticali da traffico** su un ponte stradale: suddivisione della
superficie carrabile in **corsie convenzionali**, **Schemi di Carico** applicabili e **intensità Qik/qik**,
secondo le NTC 2018 §5.1.3.3.

## Input richiesti

- larghezza della **superficie carrabile** `w` (ed eventuale spartitraffico e tipo di barriere);
- tipo di verifica (**globale** o **locale**) e categoria del ponte (carichi interi / **pedonale**);
- presenza di marciapiedi (protetti / non protetti da sicurvia) e, per luci > 300 m, la luce.

## Procedura (ancorata al testo)

1. **Corsie convenzionali** (§5.1.3.3.2, Tab. 5.1.I). Determinare numero e larghezza:
   **w < 5,40 m → nl = 1**, corsia 3,00 m; **5,4 ≤ w < 6,0 m → nl = 2**, corsia w/2; **6,0 m ≤ w →
   nl = Int(w/3)**, corsia 3,00 m (zona rimanente w − 3,00·nl). Numerare come corsia 1 quella che, caricata,
   dà l'effetto più sfavorevole, poi 2, ecc. In presenza di spartitraffico applicare i casi a) barriera
   fissa / b) barriera mobile.

2. **Schemi di Carico** (§5.1.3.3.3). Individuare gli Schemi pertinenti: **Schema 1** (tandem 2 assi +
   distribuito) per verifiche globali e locali; **Schema 2** (asse singolo) per verifiche locali; **Schema
   3** (150 kN) e **Schema 4** (10 kN) per i marciapiedi (non protetti / protetti); **Schema 5** (folla
   5,0 kN/m², combinazione 2,5 kN/m²). Per **luce > 300 m** valutare gli **Schemi 6.a/b/c** [5.1.1]-[5.1.3].

3. **Categorie stradali** (§5.1.3.3.4). Stabilire se il ponte è a **carichi interi** o **pedonale** (solo
   Schema 5); considerare eventuali **veicoli speciali**.

4. **Intensità dei carichi** (Tab. 5.1.II). Assegnare per corsia: **corsia 1 Qik = 300 kN, qik = 9,00
   kN/m²**; **corsia 2 = 200 / 2,50**; **corsia 3 = 100 / 2,50**; **altre = 0 / 2,50**. La larghezza di
   ingombro convenzionale è **3,00 m** e il numero di corsie non è inferiore a **2** (salvo w < 5,40 m).

5. **Gruppi di azioni** (§5.1.3.14, Tab. 5.1.IV). Ricordare che i carichi verticali entrano nei gruppi di
   azioni con i valori caratteristici/frequenti; il carico più gravoso è indicato come **q1**.

## Output

Una nota che indichi: **numero e larghezza** delle corsie convenzionali per la `w` data; gli **Schemi di
Carico** applicabili al tipo di verifica e alla categoria; le **intensità Qik/qik** per corsia; il rinvio
alle **Fig. 5.1.1/5.1.2** (geometrie non riprodotte). **La skill inquadra la definizione dei carichi; non
individua la disposizione più gravosa né calcola le sollecitazioni.**
