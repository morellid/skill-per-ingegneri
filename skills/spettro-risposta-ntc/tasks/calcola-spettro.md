# Task: calcola lo spettro di risposta elastico NTC 2018

## Obiettivo

Calcolare e tabulare lo spettro di risposta elastico in accelerazione (componente orizzontale) ai sensi di NTC 2018 par. 3.2.3, per uno o piu' degli stati limite SLO, SLD, SLV, SLC, dato il sito.

## Quando usare questo task

- "Calcolami lo spettro NTC per il sito X"
- "Dammi i parametri S, eta, TB, TC, TD allo SLV"
- "Tabulami Se(T) da T=0 a T=4 s con passo 0.05 s per tutti gli stati limite"
- "Mi servono ag/F0/Tc* interpolati al TR di progetto"
- "Verifico il valore di SS che mi da' un altro software"

## Input richiesti

Acquisire dall'utente, in quest'ordine, e validare prima di proseguire:

1. **Vita nominale V_N [anni]** (NTC par. 2.4.1)
   - Valori tipici: 10 (provvisori), 50 (ordinarie), 100 (rilevanti)
2. **Classe d'uso** (NTC par. 2.4.2): I, II, III, IV. Coefficiente C_U corrispondente (Tab. 2.4.II): 0.7, 1.0, 1.5, 2.0
3. **Categoria di sottosuolo** (NTC par. 3.2.2): A, B, C, D, E (Vs,30 da indagini geofisiche, vedi relazione geologica/geotecnica)
   - **Se l'utente indica S1 o S2 -> NON eseguire il calcolo**: rinviare ad analisi specifiche di risposta sismica locale (par. 3.2.2)
4. **Categoria topografica** (NTC Tab. 3.2.IV): T1 (pianeggiante o pendio fino 15 grad), T2 (pendio > 15 grad), T3 (rilievo h > 30 m, larghezza in cresta >> base, fianchi 15-30 grad), T4 (idem ma fianchi > 30 grad)
5. **Parametri di pericolosita' al sito**: 9 valori per ciascuno di ag [g], F0 [adim.], Tc* [s], in corrispondenza dei TR di riferimento {30, 50, 72, 101, 140, 201, 475, 975, 2475} anni. L'utente li ricava da:
   - Servizio interattivo INGV: http://zonesismiche.mi.ingv.it/
   - Foglio Excel CSLP del Servizio Tecnico Centrale del Consiglio Superiore dei Lavori Pubblici
   - Output del software di calcolo strutturale del progettista (purche' allineato con il reticolo INGV)
6. **Smorzamento viscoso xi [%]** - default 5% (eta = 1.0). Valori diversi solo con motivazione strutturale documentata.
7. **Stato limite o stati limite richiesti**: SLO / SLD / SLV / SLC / TUTTI (default: TUTTI)
8. **Periodi di tabulazione [s]**: range start:stop:step (default suggerito: 0:4:0.05)

## Fonti normative

Vedi `references/sources.yaml`. Estratti rilevanti:
- [`references/estratti/ntc2018-par-3-2.md`](../references/estratti/ntc2018-par-3-2.md) - definizioni stati limite, formule spettro
- [`references/estratti/ntc2018-allegato-a-tab.md`](../references/estratti/ntc2018-allegato-a-tab.md) - reticolo TR di riferimento
- [`references/estratti/ntc2018-classi-uso-vita.md`](../references/estratti/ntc2018-classi-uso-vita.md) - VN, CU, VR
- [`references/estratti/circ-7-2019-c-3-2.md`](../references/estratti/circ-7-2019-c-3-2.md) - commento applicativo

## Procedura

1. **Sanity check input**: verifica che VN sia >= 10 (segnala se < 35 -> VR sara' clampata a 35 per par. 2.4.3), che la classe d'uso sia coerente con la destinazione d'uso dichiarata, che la categoria di sottosuolo non sia S1/S2.

2. **Prepara file parametri di riferimento** in formato JSON:

   ```json
   {
     "tr_anni": [30, 50, 72, 101, 140, 201, 475, 975, 2475],
     "ag_g":    [0.030, 0.045, ..., 0.420],
     "F0":      [2.50, 2.55, ..., 2.76],
     "Tc_star": [0.20, 0.22, ..., 0.36]
   }
   ```

   (tutte le liste hanno 9 elementi, allineati con `tr_anni`).

3. **Esegui il modulo Python** `tasks/lib/spettro.py` via Bash (regola inviolabile da SKILL.md: NON ricalcolare a mano dalle formule). Usa `${CLAUDE_SKILL_DIR}` in Claude Code, oppure il path assoluto della skill installata su Codex / altri agent:

   ```bash
   python3 ${CLAUDE_SKILL_DIR}/tasks/lib/spettro.py \
       --tr-riferimento /tmp/params-sito.json \
       --vn 50 --classe-uso II \
       --cat-sottosuolo C --cat-topografica T1 \
       --stato-limite TUTTI \
       --tabula 0:4:0.05 \
       --out-csv /tmp/spettro-sito.csv
   ```

   Per output JSON machine-readable usa `--json`. Tutti i numeri presentati all'utente devono provenire dallo stdout del modulo, non da rielaborazioni successive.

4. **Citazione delle formule applicate** (sempre nell'output a video, prima della tabella):
   - Vita di riferimento: V_R = V_N * C_U  (NTC eq. 2.4.1) - valore minimo 35 anni (par. 2.4.3)
   - Tempi di ritorno: T_R = - V_R / ln(1 - P_VR) con P_VR da Tab. 3.2.I
   - Interpolazione log su TR di riferimento: NTC Allegato A
   - Periodi spettro: T_C = C_C * T_c*; T_B = T_C / 3; T_D = 4 * (a_g / g) + 1.6 (eq. 3.2.7-3.2.8)
   - Spettro Se(T): NTC eq. 3.2.4 a tratti su [0, T_B], [T_B, T_C], [T_C, T_D], [T_D, +inf)

5. **Output strutturato per ciascuno stato limite**:
   - Riga riepilogo: SL, P_VR, TR (anni), ag (g), F0, Tc* (s)
   - Coefficienti: SS, ST, S = SS*ST, CC, eta, TB, TC, TD
   - Tabella Se(T) con etichetta del ramo per ciascun T
   - Eventuale CSV se l'utente lo chiede

## Output atteso

Esempio (parziale, in formato umano-leggibile):

```
=== SLV ===
  TR        =     474.56 anni    (P_VR = 10%, V_R = 50 anni)
  ag        =     0.2179 g
  F0        =     2.7200
  Tc*       =     0.3200 s
  cat. sottosuolo = C    cat. topografica = T1
  SS        =     1.3444    ST = 1.00    S = 1.3444
  CC        =     1.5293    eta = 1.0000
  TB,TC,TD  =     0.1631, 0.4894, 2.4716 s

  Tabella Se(T) [81 punti]:
    T = 0.000 s   Se = 0.29297 g   [0-TB]
    T = 0.050 s   Se = 0.45125 g   [0-TB]
    T = 0.100 s   Se = 0.60953 g   [0-TB]
    T = 0.163 s   Se = 0.79636 g   [TB-TC]
    ...
```

## Nota sulle convenzioni

- ag e' espresso in **frazione di g** (adimensionale). Per ottenere [m/s^2] moltiplicare per 9.81.
- I periodi sono in secondi.
- F0 e' adimensionale.

## Limiti

Questo task NON fa:
- Non calcola lo spettro **verticale** (NTC par. 3.2.3.2.2): da estendere in versione successiva
- Non riduce con fattore q per ottenere lo spettro di **progetto** Sd(T): la riduzione dipende da scelte progettuali del professionista (vedi NTC par. 3.2.3.5 e par. 7)
- Non sostituisce la determinazione del **Vs,30** e della categoria di sottosuolo, che richiede indagini geofisiche e relazione geologica
- Non esegue interpolazione **bi-lineare in lat/lon** sul reticolo INGV: l'utente fornisce gia' i 9 valori al sito (i servizi INGV o il foglio CSLP fanno l'interpolazione spaziale)
- Non gestisce siti **fuori reticolo** (le isole minori, ecc.): il modulo solleva errore esplicito se TR < 30 o TR > 2475 anni

**L'output va sempre verificato dal progettista strutturale prima di essere usato in analisi di calcolo o in relazione di calcolo.**
