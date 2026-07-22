# Task: inquadra-coefficienti-parametri-geotecnici

Inquadra i **coefficienti parziali sui parametri geotecnici** (M1/M2, Tab. 6.2.II), la **resistenza di progetto
Rd** e il **valore caratteristico** secondo le **NTC 2018 par. 6.2.4.1.2 e 6.2.2**. Supporto documentale: **non**
calcola Rd.

## Quando usarla

Il progettista deve applicare i coefficienti parziali M1/M2 ai parametri del terreno e impostare la resistenza di
progetto. Per gli approcci progettuali e i coefficienti sulle azioni usa `inquadra-approcci-progettuali-slu`.

## Passi

1. **Valore caratteristico** (§6.2.2): il valore caratteristico di un parametro geotecnico è una **stima ragionata
   e cautelativa** del valore del parametro **per ogni stato limite considerato**, dedotta dall'interpretazione di
   prove di laboratorio e in sito. La caratterizzazione e la modellazione geotecnica sono responsabilità del
   **progettista**.
2. **Coefficienti parziali M1/M2** (§6.2.4.1.2, Tab. 6.2.II), applicati **dividendo** il valore caratteristico:
   - **tan φ'k** (tangente dell'angolo di resistenza al taglio) → γφ': **M1 = 1,0**, **M2 = 1,25**;
   - **c'k** (coesione efficace) → γc': **M1 = 1,0**, **M2 = 1,25**;
   - **cuk** (resistenza non drenata) → γcu: **M1 = 1,0**, **M2 = 1,4**;
   - **γ** (peso dell'unità di volume) → γγ: **M1 = 1,0**, **M2 = 1,0**.
   In sostanza **M1 lascia inalterati** i parametri, **M2 riduce** resistenza al taglio (tan φ', c') e resistenza
   non drenata (cu).
3. **Resistenza di progetto Rd** (§6.2.4.1.2): può essere determinata (a) **analiticamente** dai valori
   caratteristici dei parametri **divisi per γM** (Tab. 6.2.II), tenendo conto ove necessario dei coefficienti
   **γR** specificati **nei paragrafi di ciascun tipo di opera**; (b) da correlazioni con prove in sito; (c) da
   misure dirette su prototipi (in b e c i γR sono nelle tabelle di ciascuna opera).
4. **Combinazione con l'approccio** (§6.2.4): M1 si accoppia ad A1/R1, M2 ad A2/R2 nell'Approccio 1 di default
   ((A1+M1+R1) e (A2+M2+R2)). Il set completo dei **γR** è nelle skill d'opera (§6.3-6.11).

Usa la checklist in `../references/estratti/verifiche-geotecniche-slu-checklist.md` (sezioni 2 e 3).

## Output atteso

Un inquadramento che indichi i coefficienti M1/M2 della Tab. 6.2.II (tan φ' e c' 1,0/1,25, cu 1,0/1,4, γ 1,0/1,0),
il concetto di valore caratteristico (stima ragionata e cautelativa) e come si imposta Rd (Xk/γM con i γR di
opera), con **rinvio ai paragrafi/tabella** NTC. Nessun calcolo di Rd.

## Cosa NON fare

- Non **calcolare** Rd né i parametri di progetto: la skill inquadra i coefficienti, non esegue i conti.
- Non attribuire i **coefficienti γR** specifici dell'opera (§6.3-6.11): rinvia alle skill d'opera.
