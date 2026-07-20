# Task - Inquadra azioni da traffico derivate, altre azioni e combinazioni (§5.1.3.4-5.1.3.14)

## Obiettivo

Inquadrare le **azioni derivate dal traffico** (frenamento, forza centrifuga), le **altre azioni** (neve,
vento, temperatura, parapetti/urto) e i **coefficienti** per le combinazioni sui ponti stradali, secondo le
NTC 2018 §5.1.3.4-5.1.3.14.

## Input richiesti

- carico verticale sulla corsia 1 (2·Q1k, q1k) e larghezza w1, lunghezza caricata L;
- geometria del ponte (raggio di curvatura R, presenza di giunti, parapetti/barriere);
- lo **stato limite** e la **colonna** dei coefficienti parziali (EQU / A1 / A2).

## Procedura (ancorata al testo)

1. **Incremento dinamico addizionale q2** (§5.1.3.4). Gli effetti dinamici sono già inclusi nei carichi
   mobili; **q2** va considerato solo in casi particolari (es. giunti di dilatazione).

2. **Frenamento/accelerazione q3** (§5.1.3.5, [5.1.4]). Applicare
   **180 kN ≤ q3 = 0,6·(2·Q1k) + 0,10·q1k·w1·L ≤ 900 kN**, funzione del carico verticale totale sulla corsia
   convenzionale n. 1; forza applicata a livello della pavimentazione, lungo l'asse della corsia.

3. **Forza centrifuga q4** (§5.1.3.6, Tab. 5.1.III). Con Qv = Σ 2·Qik (assi tandem dello Schema 1):
   **R < 200 m → q4 = 0,2·Qv**; **200 ≤ R ≤ 1500 → q4 = 40·Qv/R**; **R ≥ 1500 → q4 = 0**. Direzione normale
   all'asse del ponte.

4. **Altre azioni** (§5.1.3.7-5.1.3.11): **neve/vento q5** (vento su parete di 3 m dal piano stradale; neve
   non concomitante col traffico salvo ponti coperti - rinvio Cap. 3); **temperatura q7** (Cap. 3);
   **parapetti/urto q8** (parapetti h ≥ 1,10 m, azione orizzontale 1,5 kN/m; forze da urto amplificate ×1,50
   per l'impalcato; γ unitario per l'urto); **resistenze passive q9**.

5. **Combinazioni** (§5.1.3.14). Comporre i **gruppi di azioni** (Tab. 5.1.IV) e applicare i **coefficienti
   parziali SLU** (Tab. 5.1.V, colonne EQU/A1/A2: traffico γQ sfavorevole **1,35 / 1,35 / 1,15**; g2 sfav.
   1,50/1,50/1,30) e i **coefficienti di combinazione ψ** (Tab. 5.1.VI). Per le azioni sismiche assumere di
   regola **ψ2j = 0,0** (0,2 in zona urbana di intenso traffico).

## Output

Una nota che indichi: la **formula/limiti** di q3 [5.1.4]; il **valore normativo** di q4 in funzione di R;
le regole per le **altre azioni** (neve/vento/temperatura/parapetti); i **coefficienti** (γ della Tab.
5.1.V, ψ della Tab. 5.1.VI) da usare nelle combinazioni. **La skill inquadra le formule e i coefficienti;
non calcola i valori numerici delle azioni né esegue le verifiche.**
