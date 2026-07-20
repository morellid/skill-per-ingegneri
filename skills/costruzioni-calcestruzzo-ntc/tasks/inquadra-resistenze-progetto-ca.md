# Task - Inquadra classi, coefficienti e resistenze di progetto del c.a. (§4.1, 4.1.2.1)

## Obiettivo

Inquadrare la **classe di resistenza** del calcestruzzo, i **coefficienti parziali** e le **resistenze di
progetto** dei materiali (calcestruzzo e acciaio), con i relativi **diagrammi di calcolo**, secondo le NTC
2018 §4.1.

## Input richiesti

- classe di resistenza del calcestruzzo (Cxx/yy) e tipo di acciaio (fyk);
- geometria degli elementi (per l'eventuale riduzione per elementi piani < 50 mm);
- livello di controllo di produzione (per l'eventuale γc = 1,4).

## Procedura (ancorata al testo)

1. **Classe di resistenza** (§4.1, Tab. 4.1.I). Individuare la classe (da C8/10 a C90/105); i valori
   caratteristici (fck, fctk, moduli) provengono dal §11.2.

2. **Coefficienti parziali** (§4.1.2.1.1). Assumere **γc = 1,5** per il calcestruzzo (riducibile a **1,4**
   solo per produzione continuativa con controllo e coefficiente di variazione della resistenza ≤ 10%,
   sistema di qualità §11.8.3) e **γs = 1,15** per l'acciaio (sempre, per tutti i tipi).

3. **Resistenze di progetto** (§4.1.2.1.1). Calcestruzzo a compressione **fcd = αcc·fck/γc** [4.1.3] con
   **αcc = 0,85**; per **elementi piani** (solette, pareti) gettati in opera con **spessore < 50 mm** la
   resistenza va ridotta a **0,80·fcd**. Calcestruzzo a trazione **fctd = fctk/γc** [4.1.4]. Acciaio
   **fyd = fyk/γs** [4.1.5].

4. **Diagrammi di calcolo** (§4.1.2.1.2). Per il calcestruzzo scegliere il modello σ-ε (parabola-rettangolo,
   triangolo-rettangolo o rettangolo/stress block); per le classi **≤ C50/60** usare **εc2 = 0,20%** ed
   **εcu = 0,35%** (per classi superiori i valori derivano da formula). Per l'acciaio, diagramma bilineare o
   elastico-perfettamente plastico.

## Output

Una nota che indichi: la **classe di resistenza**; i **coefficienti** γc (1,5 o 1,4) e γs (1,15); le
**formule delle resistenze di progetto** fcd = αcc·fck/γc, fctd = fctk/γc, fyd = fyk/γs (con l'eventuale
riduzione 0,80·fcd); i **diagrammi di calcolo** e le deformazioni (εc2, εcu). **La skill fornisce criteri e
coefficienti; non calcola le resistenze in valore né i valori caratteristici, che derivano dai §11.2/11.3.**
