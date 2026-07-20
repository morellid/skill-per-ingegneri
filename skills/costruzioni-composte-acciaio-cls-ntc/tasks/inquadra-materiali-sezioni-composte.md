# Task - Inquadra materiali, coefficienti e resistenza delle sezioni composte (§4.3.2, 4.3.3, 4.3.4.2)

## Obiettivo

Inquadrare i **materiali** e i **coefficienti parziali**, la **classificazione delle sezioni** composte e i
metodi di calcolo della **resistenza a flessione** delle travi con soletta collaborante, secondo le NTC
2018 §4.3.

## Input richiesti

- classe del calcestruzzo e tipo di acciaio (carpenteria, armatura);
- geometria della sezione composta (profilo, soletta, larghezza) e classe della sezione in acciaio;
- fase di verifica (SLU / SLE / eccezionale).

## Procedura (ancorata al testo)

1. **Materiali e coefficienti** (§4.3.3). Assumere le resistenze di progetto **fd = fk/γM** [4.3.6] con,
   allo **SLU**: **γC = 1,5** (calcestruzzo), **γA = 1,05** (acciaio da carpenteria), **γS = 1,15** (acciaio
   da armatura), **γV = 1,25** (connessioni); allo **SLE** e nelle situazioni **eccezionali** γM = 1. La
   classe del calcestruzzo deve essere tra **C20/25 e C60/75** (leggeri LC20/22-LC55/60).

2. **Classificazione della sezione** (§4.3.2.1). Classificare la sezione composta secondo lo schema
   dell'acciaio (§4.2.3): per le **classi 1 e 2** sono ammesse distribuzioni **plastiche o elastiche**, per
   le **classi 3 e 4** solo **elastiche**. Per le classi 1-2, l'armatura As in soletta usata per il momento
   plastico deve essere in **B450C** e rispettare la condizione [4.3.1].

3. **Larghezza collaborante** (§4.3.2.3). Determinare **bei = min(Le/8, bi)** (Le distanza tra i punti di
   momento nullo).

4. **Resistenza a flessione** (§4.3.4.2.1). Individuare il metodo: **elastico** (limiti fcd/fyd/fsd, cls
   teso trascurato), **plastico** (compressione cls **0,85·fcd**, ammesso per classi 1-2), **elasto-plastico**
   (analisi non lineare, ogni classe). La **resistenza a taglio verticale** è affidata **interamente alla
   trave metallica** (§4.2.4.1.2).

## Output

Una nota che indichi: i **coefficienti** γC/γA/γS/γV; la **classe** della sezione e il metodo di calcolo del
momento resistente (elastico/plastico/elasto-plastico) ammesso; la **larghezza collaborante**. **La skill
fornisce criteri e coefficienti; non calcola il momento resistente né dimensiona la sezione.**
