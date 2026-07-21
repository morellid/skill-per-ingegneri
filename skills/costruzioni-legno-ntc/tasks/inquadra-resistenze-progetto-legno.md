# Task - Inquadra classi, kmod/gamma_M e resistenze di progetto del legno (§4.4.4, 4.4.5, 4.4.6)

## Obiettivo

Inquadrare l'assegnazione della **classe di durata del carico** e della **classe di servizio**, e il
calcolo delle **resistenze di progetto** del legno con **Xd = kmod·Xk/γM** (Tab. 4.4.III e 4.4.IV), secondo
le NTC 2018 §4.4.

## Input richiesti

- tipo di prodotto (legno massiccio, lamellare incollato, CLT, LVL, compensato, OSB, ecc.);
- condizioni ambientali di esercizio (umidità/UR) per la classe di servizio;
- combinazione di carico e classi di durata delle azioni presenti;
- livello di controllo di produzione (per l'eventuale colonna B di γM);
- valori caratteristici Xk (fk, fvk, ecc.) dal §11.7/progetto.

## Procedura (ancorata al testo)

1. **Classe di durata del carico** (§4.4.4, Tab. 4.4.I). Assegnare ciascuna azione a: permanente (>10
   anni), lunga (6 mesi-10 anni), media (1 settimana-6 mesi), breve (<1 settimana), istantaneo. Riferimenti
   tipici: peso proprio → permanente; variabili edifici → media; neve (as ≥ 1000 m) → almeno media; vento
   medio → breve; picco vento/eccezionali → istantaneo.

2. **Classe di servizio** (§4.4.5, Tab. 4.4.II). Individuare la classe **1** (UR ≤ 65%), **2** (UR > 85%
   solo poche settimane/anno) o **3** (umidità più elevata) in funzione dell'ambiente d'uso.

3. **Coefficiente kmod** (§4.4.6, Tab. 4.4.IV). Scegliere kmod in funzione di **materiale + classe di
   servizio + classe di durata**. Se la combinazione comprende azioni di classi diverse, usare il **kmod
   dell'azione di minor durata**.

4. **Coefficiente γM** (§4.4.6, Tab. 4.4.III). Usare la **colonna A** (es. legno massiccio 1,50, lamellare
   1,45, LVL/OSB 1,40, unioni 1,50); la **colonna B** (valori ridotti) solo per produzioni continuative con
   controllo e coefficiente di variazione della resistenza ≤ 15% (sistema di qualità §11.7). Per le
   **combinazioni eccezionali** γM = 1,00.

5. **Resistenza di progetto**. Applicare **Xd = kmod·Xk/γM** [4.4.1] per ciascuna proprietà (ft,0, fc,0,
   fm, fv, ...), con Xk dal §11.7. La skill fornisce i criteri e i coefficienti; i valori Xk e il calcolo
   numerico restano del progettista.

## Output

Una nota che indichi: la **classe di durata** delle azioni e la **classe di servizio**; il **kmod**
applicabile (con la regola dell'azione di minor durata); il **γM** applicabile (colonna A/B o eccezionale);
la formula **Xd = kmod·Xk/γM** con cui il progettista ricava le resistenze di progetto. **La skill non
calcola Xk né le resistenze in valore, che restano compito del progettista.**
