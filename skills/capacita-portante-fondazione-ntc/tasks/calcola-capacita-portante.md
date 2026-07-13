# Task: Calcolo della capacita' portante di una fondazione superficiale (FHWA NHI-06-089 par. 8.4 + NTC 6.4.2.1)

Calcola il carico limite qult con la formulazione del FHWA NHI-06-089 (codice internazionale ex cap. 12 NTC 2018) e la resistenza di progetto NTC (Approccio 2, gamma_R = 2,3), con confronto Ed <= Rd se Ed e' fornito.

## Obiettivo

Restituire all'utente:

- **qult** [kPa] con i tre termini separati (coesione, sovraccarico, peso), i fattori Nc/Nq/Ngamma, i fattori di forma, falda e dq usati;
- **q_Rd = qult/2,3** [kPa] e **R_d = q_Rd * A'** [kN] (forza normale al piano di posa, C6.4.2.1); per il nastro, per metro di sviluppo;
- esito **Ed <= Rd** [6.2.1] se Ed e' fornito;
- **avvertenze** (ipotesi della formulazione, casi fuori ambito, responsabilita' ex cap. 12).

## Input richiesti

1. **Geometria**: B [m] (lato minore); L [m] (assente -> nastro, L/B >= 10); Df [m]; eventuali eccentricita' eB/eL [m] (e < dim/6 su terreno, altrimenti la fonte impone il ridimensionamento).
2. **Condizione di calcolo**: `drenata` (c' [kPa], phi' [gradi]) oppure `non-drenata` (cu [kPa], phi = 0). Parametri caratteristici dalla relazione geotecnica (con M1 = 1,0 coincidono con i valori di progetto - Tab. 6.2.II).
3. **Pesi**: gamma sotto il piano di posa [kN/m3]; gamma sopra (default = sotto); eventuale sovraccarico applicato q_appl [kPa].
4. **Falda**: DW [m dal piano campagna] (assente -> assunta oltre 1,5B+Df, dichiarato in avvertenza).
5. Facoltativi: **dq** (Table 8-6, solo con rinterro granulare compattato permanente; default 1,0 = omissione conservativa); **Ed** [kN] (componente normale della risultante di progetto in combinazione A1, calcolata dall'utente).

## Fonti normative

Leggere prima di procedere:

- `references/estratti/fhwa-capacita-portante-ntc.md` - formulazione, fattori, limiti, verifica NTC
- `references/fonti/fhwa-nhi-06-089.md` - trascrizione parr. 8.4.2-8.4.3.3
- `references/fonti/ntc2018-dm-17-01-2018.md` - 6.4.2.1, Tab. 6.2.I/6.2.II/6.4.I, cap. 12
- `references/fonti/circ-7-2019-mit.md` - C6.4.2.1

## Procedura

### Passo 1 - Screening dei casi fuori ambito

Se il caso presenta anche uno solo di: **carico inclinato**, **base inclinata**, **piano campagna in pendenza / fondazione su pendio**, **terreni stratificati** nel volume significativo, **rottura locale/punzonamento attesa** (terreni molto sciolti/molli), **verifica sismica**: la skill NON calcola. Spiega il limite citando il paragrafo FHWA (8.4.3.4/8.4.3.5/8.4.3.6/8.4.3.7/8.4.5) o NTC 7.11.5.3.1 e rinvia al progettista. Per fondazioni su pendio ricorda anche la verifica di stabilita' globale (NTC 6.4.2.1, Approccio 1 A2+M2+R2).

### Passo 2 - Esegui il calcolo con il modulo Python

Usa SEMPRE il modulo `tasks/lib/capacita_portante.py` (mai calcoli a mano):

```bash
# nastro, condizione drenata, falda profonda
python3 tasks/lib/capacita_portante.py --b 2 --df 1 --gamma 18 \
  --condizione drenata --phi 30

# rettangolare con eccentricita', falda, confronto con Ed
python3 tasks/lib/capacita_portante.py --b 2 --l 3 --df 1 --gamma 18 \
  --condizione drenata --phi 30 --c 5 --eb 0.2 --dw 1.5 --ed 900
```

Comportamenti da conoscere:

- **eccentricita' >= 1/6 della dimensione** (su terreno): il modulo rifiuta ("the footing should be resized", FHWA 8.4.3.1) - non aggirare;
- **dq**: default 1,0 (omissione conservativa, Table 8-6); un dq esplicito produce un'avvertenza con le condizioni della fonte;
- **DW assente**: falda assunta profonda, dichiarato in avvertenza.

### Passo 3 - Presenta il risultato

1. qult con i tre termini e tutti i fattori, citando le equazioni ([8-2]..[8-6], Table 8-4/8-5) e - se usati - i valori di cross-check (Table 8-2: phi=0 -> Nc=5,14).
2. q_Rd e R_d con la catena NTC: Approccio 2 (A1+M1+R3), gamma_R = 2,3 (Tab. 6.4.I), M1 = 1,0 (Tab. 6.2.II), condizione [6.2.1]; Ed a carico dell'utente con i coefficienti A1 (Tab. 6.2.I).
3. Riporta **integralmente le avvertenze** del modulo.
4. Ricorda le verifiche NON coperte: scorrimento (gamma_R = 1,1), stabilita' globale, STR (senza gamma_R), SLE/cedimenti (vedere la skill `cedimenti-edometrici-ntc`), sisma.

### Passo 4 - Concludi sempre con

- La formulazione e' un codice internazionale usato ex cap. 12 NTC: "e' responsabilita' del progettista garantire espressamente livelli di sicurezza coerenti".
- I parametri geotecnici vengono dalla relazione geotecnica: la skill non li stima (le correlazioni SPT della Table 8-1 non sono implementate).
- **Il risultato e' un supporto al progettista firmatario, non una verifica firmabile.**

## Output

Blocco JSON del modulo + sintesi testuale con citazioni (equazioni FHWA, tabelle NTC) e avvertenze.

## Limiti

- Solo carico verticale (anche eccentrico), base e piano campagna orizzontali, terreno omogeneo, rottura generale.
- Non calcola Ed (combinazioni A1), ne' scorrimento, stabilita' globale, verifiche STR, SLE, sisma.
- Non stima i parametri geotecnici ne' determina la posizione della falda.
- dq solo come input esplicito dell'utente (Table 8-6), default conservativo 1,0.
