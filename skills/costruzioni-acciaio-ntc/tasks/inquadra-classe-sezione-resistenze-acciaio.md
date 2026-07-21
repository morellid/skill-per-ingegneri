# Task - Inquadra materiali, classe di sezione e resistenze SLU dell'acciaio (§4.2.1, 4.2.3.1, 4.2.4.1)

## Obiettivo

Inquadrare la scelta del **materiale** (grado, fyk/ftk), la **classificazione della sezione** (classi 1-4)
e le **resistenze di progetto** agli stati limite ultimi con il coefficiente **γM** (Tab. 4.2.VII), secondo
le NTC 2018 §4.2.

## Input richiesti

- grado dell'acciaio (S235-S460) e spessore t degli elementi;
- geometria della sezione (tipo di profilo, rapporti b/t delle parti compresse) e tipo di sollecitazione;
- eventuale presenza di fori per collegamenti bullonati/chiodati nelle zone tese.

## Procedura (ancorata al testo)

1. **Materiale** (§4.2.1.1). Individuare il **grado** (da S235 a S460) e ricavare **fyk** e **ftk** dalle
   **Tab. 4.2.I** (profili a sezione aperta) o **4.2.II** (sezione cava), in funzione della qualità e dello
   spessore t (t ≤ 40 mm o 40 < t ≤ 80 mm).

2. **Classe della sezione** (§4.2.3.1). Classificare la sezione in **classe 1 (duttile, Cθ ≥ 3)**, **2
   (compatta, Cθ ≥ 1,5)**, **3 (semi-compatta)** o **4 (snella, sezione efficace)**, confrontando i
   rapporti larghezza/spessore delle parti compresse con le **Tab. 4.2.III-IV-V** (da leggere sulla
   norma/EC3, sono figure nel PDF). Per una **sezione composta** la classe è il **valore più alto** tra gli
   elementi. La classe determina il metodo di calcolo ammesso (E per tutte, P solo classe 1-2).

3. **Coefficiente γM** (§4.2.4.1.1, Tab. 4.2.VII). Adottare **γM0 = 1,05** per la resistenza delle sezioni,
   **γM1 = 1,05** (1,10 ponti) per l'instabilità, **γM2 = 1,25** per la frattura delle sezioni tese
   indebolite dai fori. La resistenza di progetto è **Rd = Rk/γM** [4.2.3].

4. **Resistenze di progetto SLU** (§4.2.4.1.2). Inquadrare le resistenze pertinenti: trazione (minore fra
   **A·fyk/γM0** e **0,9·Anet·ftk/γM2**), compressione (**A·fyk/γM0**, o Aeff per classe 4), flessione
   (**Wpl·fyk/γM0** classe 1-2, Wel,min classe 3, Weff,min classe 4), taglio (**Av·fyk/(√3·γM0)**),
   presso/tenso-flessione.

## Output

Una nota che indichi: il **grado** e i valori **fyk/ftk**; la **classe della sezione** (1-4) e il metodo di
calcolo ammesso; il **coefficiente γM** applicabile (γM0/γM1/γM2); le **formule delle resistenze di
progetto** SLU pertinenti. **La skill fornisce i criteri e i coefficienti; non calcola le resistenze in
valore né dimensiona la membratura.**
