# Task - Inquadra la procedura di analisi e le verifiche di resistenza al fuoco (§3.6.1.5)

## Obiettivo

Inquadrare la **procedura di analisi della resistenza al fuoco** e le **verifiche di sicurezza** delle
strutture esposte all'incendio, secondo le NTC 2018 §3.6.1.5.

## Input richiesti

- **classe di resistenza al fuoco** richiesta (o livello di prestazione);
- tipo di incendio prevalente (materiali cellulosici, idrocarburi, strutture esterne);
- azioni permanenti e variabili concomitanti (per la combinazione eccezionale).

## Procedura (ancorata al testo)

1. **Articolazione dell'analisi** (§3.6.1.5): (a) individuare l'**incendio di progetto**; (b) analisi
   dell'**evoluzione della temperatura**; (c) analisi del **comportamento meccanico**; (d) **verifiche di
   sicurezza**.

2. **Incendio di progetto** (§3.6.1.5.1). Scegliere fra **curva nominale** (temperature per l'intervallo pari
   alla classe, senza raffreddamento) e **curva naturale** (intera durata, incl. raffreddamento). Curve
   nominali:
   - **standard** (cellulosici): **θg = 20 + 345·log10(8t + 1)** °C [3.6.2];
   - **idrocarburi**: **θg = 1080·(1 − 0,325·e^(−0,167t) − 0,675·e^(−2,5t)) + 20** °C [3.6.3];
   - **esterna**: **θg = 660·(1 − 0,687·e^(−0,32t) − 0,313·e^(−3,8t)) + 20** °C [3.6.4].

3. **Evoluzione della temperatura** (§3.6.1.5.2). Risolvere la propagazione del calore (irraggiamento e
   convezione dai gas), considerando eventuali **materiali protettivi**.

4. **Comportamento meccanico** (§3.6.1.5.3). Tenere conto della **riduzione della resistenza** dei materiali
   con la temperatura; applicare le azioni della **combinazione eccezionale** (permanenti + variabili
   concomitanti; **niente concomitanza** con altre eccezionali o sisma); considerare le sollecitazioni
   indirette da dilatazioni contrastate ove non trascurabili.

5. **Verifiche di sicurezza** (§3.6.1.5.4). Controllare che la **resistenza meccanica** sia mantenuta per il
   **tempo pari alla classe** (curva nominale) o per l'intera durata (curva naturale). Per periodi limitati
   (es. livello II) la verifica può riferirsi a un tempo di esposizione all'incendio naturale congruente col
   livello.

## Output

Una nota che indichi: la **curva d'incendio** applicabile (con la formula), lo schema dell'**analisi**
(temperatura → comportamento meccanico), la **combinazione eccezionale** e il **criterio di verifica** (tempo
della classe). **La skill inquadra la procedura e le formule delle curve; non esegue le analisi termiche o
meccaniche né fornisce le proprietà dei materiali ad alta temperatura (Eurocodici parte 1-2).**
