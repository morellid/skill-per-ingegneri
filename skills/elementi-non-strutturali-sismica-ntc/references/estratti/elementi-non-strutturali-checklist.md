# Estratto operativo - Elementi non strutturali e impianti in zona sismica (NTC 2018 par. 7.2.3-7.2.4)

Checklist di inquadramento per il progettista strutturale. Ogni punto e' ancorato al testo trascritto in
`../fonti/ntc2018-par-7-2-3-7-2-4.md`. La skill **inquadra**, non calcola Fa ne' esegue le verifiche.

## 1. Elementi strutturali secondari (par. 7.2.3)

- [ ] Nell'analisi sismica la **rigidezza e la resistenza alle azioni orizzontali** dell'elemento sono
      **trascurate**?
- [ ] L'elemento e' progettato per i **soli carichi verticali** e per **seguire gli spostamenti** della struttura
      senza perdere capacita' portante (spostamenti allo **SLC**, par. 7.3.3.3 lineare / 7.3.4 non lineare)?
- [ ] La scelta **non** trasforma una struttura **irregolare** in **regolare** (par. 7.2.1)?
- [ ] Il **contributo totale** degli elementi secondari a **rigidezza e resistenza orizzontale** **non supera il
      15%** dell'analogo contributo degli elementi primari?

## 2. Elementi costruttivi non strutturali (par. 7.2.3)

- [ ] L'elemento rientra tra quelli che **influenzano significativamente la risposta strutturale** o che sono
      **significativi per la sicurezza/incolumita' delle persone**?
- [ ] La **capacita'** dell'elemento (e degli elementi che lo sostengono/collegano) e' **maggiore della domanda
      sismica** per ogni SL (par. 7.3.6)?
- [ ] Sono chiare le **responsabilita'** (elemento costruito in cantiere: progettista struttura individua la
      domanda e progetta la capacita', DL verifica l'esecuzione; elemento assemblato in cantiere: progettista
      struttura individua la domanda, fornitore/installatore forniscono elementi/collegamenti adeguati, DL
      verifica l'assemblaggio)?
- [ ] Se la distribuzione e' fortemente **irregolare in pianta**: incrementata **di un fattore 2 l'eccentricita'
      accidentale** (par. 7.2.6)?
- [ ] Se la distribuzione e' fortemente **irregolare in altezza**: incrementata **di un fattore 1,4 la domanda
      sismica sugli elementi verticali** (pilastri e pareti) dei livelli con significativa riduzione?
- [ ] La **forza sismica orizzontale** sull'elemento e' determinata con **Fa = (Sa x Wa) / qa** [7.2.1]?
      - **Fa** = forza orizzontale nel centro di massa (direzione piu' sfavorevole);
      - **Sa** = accelerazione massima adimensionalizzata (SL in esame, par. 3.2.1);
      - **Wa** = peso dell'elemento;
      - **qa** = fattore di comportamento dell'elemento.
      (Sa e qa da documenti di comprovata validita' in assenza di specifiche determinazioni.)

## 3. Impianti (par. 7.2.4)

- [ ] La **capacita'** dei componenti dell'impianto (e degli elementi che li sostengono/collegano) e' **maggiore
      della domanda sismica** per ogni SL (par. 7.3.6)?
- [ ] Sono chiare le **responsabilita'** (produttore per l'impianto, installatore per alimentazione e
      collegamenti, progettista strutturale per orizzontamenti/tamponature/tramezzi di ancoraggio)?
- [ ] L'impianto **eccede il 30%** del carico permanente del campo di solaio (o del pannello a cui e' appeso) o
      il **10%** del carico permanente totale della struttura? -> richiede uno **studio specifico** (fuori dalle
      prescrizioni del par. 7.2.4).

## Fuori scope (rinvii)

- **Non** calcola Fa ne' esegue le verifiche; **non** determina **Sa** e **qa** (documenti di comprovata
  validita').
- **Calcolo di spostamenti/domanda**: par. 7.3.3.3 / 7.3.4 / 7.3.6; **spettro**: par. 3.2 (skill
  `spettro-risposta-ntc`); **eccentricita' accidentale**: par. 7.2.6 (skill `criteri-modellazione-sismica-ntc`).
