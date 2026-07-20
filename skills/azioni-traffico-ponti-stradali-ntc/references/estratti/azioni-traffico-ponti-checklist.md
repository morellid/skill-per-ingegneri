# Estratto operativo - Azioni da traffico sui ponti stradali (NTC 2018 §5.1.3)

> Parafrasi ancorata a `references/fonti/ntc2018-par-5-1.md`. Ogni voce cita il paragrafo/tabella/formula
> NTC. La skill **inquadra** la definizione delle azioni; **non** calcola le sollecitazioni, **non** esegue
> le verifiche, **non** dimensiona.

## 1. Inquadramento (§5.1.1, 5.1.2)

- "**Ponti**" comprende viadotti, cavalcavia, sottopassi, strade sopraelevate, ecc. (§5.1.1).
- **Superficie carrabile** = piattaforma + marciapiedi sormontabili (h < 20 cm, non protetti) (§5.1.2.1).
- **Altezza libera** ≥ **5 m** (4 m / 3,20 m in deroga; **2,50 m** sottopassi pedonali) (§5.1.2.2).
- **Compatibilità idraulica**: piena di progetto **Tr = 200 anni**; luce netta tra pile ≥ **40 m**; **franco
  idraulico ≥ 1,50 m** (§5.1.2.3).

## 2. Elenco delle azioni (§5.1.3)

Permanenti (g1/g2/g3) - distorsioni e deformazioni impresse (ε1-ε4) - variabili da traffico - altre variabili
(termiche, idrodinamiche, vento, neve, parapetti) - resistenze passive dei vincoli - urti da veicolo in svio -
sismiche - eccezionali.

- **Permanenti** (§5.1.3.1): **g1** peso proprio strutturale; **g2** permanenti portati (pavimentazione,
  marciapiedi, barriere, parapetti, finiture…); **g3** altre (spinta terre, idrauliche).
- **Distorsioni** (§5.1.3.2): **ε1** presollecitazioni; **ε2** ritiro; **ε3** viscosità; **ε4** cedimenti
  vincolari.

## 3. Corsie convenzionali (§5.1.3.3.2, Tab. 5.1.I)

| Larghezza superficie carrabile "w" | Numero corsie nl | Larghezza corsia [m] | Zona rimanente [m] |
|---|---|---|---|
| w < 5,40 m | **1** | 3,00 | w − 3,00 |
| 5,4 ≤ w < 6,0 m | **2** | w/2 | 0 |
| 6,0 m ≤ w | **Int(w/3)** | 3,00 | w − 3,00·nl |

- La corsia più gravosa è la **Numero 1**, poi la 2, ecc. Larghezza di ingombro convenzionale **3,00 m**;
  numero di corsie **≥ 2** salvo w < 5,40 m (§5.1.3.3.5).

## 4. Schemi di Carico (§5.1.3.3.3) e intensità (Tab. 5.1.II)

- **Schema 1**: 2 assi in **tandem** (impronte quadrate 0,40 m) + carico distribuito → **verifiche globali e
  locali** (un tandem per corsia, in asse).
- **Schema 2**: **asse singolo** (impronte 0,60 × 0,35 m) → verifiche locali; in alternativa ruota da 200 kN.
- **Schema 3**: carico isolato **150 kN** (impronta 0,40 m) → marciapiedi non protetti da sicurvia.
- **Schema 4**: carico isolato **10 kN** (impronta 0,10 m) → marciapiedi protetti e passerelle pedonali.
- **Schema 5**: **folla compatta 5,0 kN/m²** (valore di combinazione **2,5 kN/m²**).
- **Schemi 6.a/b/c** (luce > 300 m, alternativa al modello principale): qL,a = 128,95·(1/L)^0,25 [5.1.1];
  qL,b = 88,71·(1/L)^0,38 [5.1.2]; qL,c = 77,12·(1/L)^0,38 [5.1.3].

**Tab. 5.1.II - Intensità Qik / qik:**

| Corsia | Carico asse Qik [kN] | qik [kN/m²] |
|---|---|---|
| 1 | 300 | 9,00 |
| 2 | 200 | 2,50 |
| 3 | 100 | 2,50 |
| altre | 0 | 2,50 |

- **Categorie stradali** (§5.1.3.3.4): ponti a carichi **interi** vs **ponti pedonali** (solo Schema 5);
  eventuali **veicoli speciali**.
- Le **geometrie/interassi** degli Schemi (Fig. 5.1.2) e la numerazione corsie (Fig. 5.1.1) sono **figure**:
  non riprodotte → testo NTC / EC1.

## 5. Azioni da traffico derivate

- **q2** incremento dinamico addizionale (giunti) (§5.1.3.4).
- **q3** frenamento/accelerazione (§5.1.3.5): **180 kN ≤ q3 = 0,6·(2·Q1k) + 0,10·q1k·w1·L ≤ 900 kN** [5.1.4]
  (funzione del carico sulla corsia 1; 2·Q1k = carico totale del tandem sulla corsia 1).
- **q4** forza centrifuga (§5.1.3.6, Tab. 5.1.III), Qv = Σ 2·Qik:

| Raggio R [m] | q4 [kN] |
|---|---|
| R < 200 | 0,2·Qv |
| 200 ≤ R ≤ 1500 | 40·Qv/R |
| R ≥ 1500 | 0 |

## 6. Altre azioni

- **q5** neve/vento (§5.1.3.7): vento su parete di **3 m** dal piano stradale; neve **non concomitante** col
  traffico (salvo ponti coperti). Rinvio al **Cap. 3**.
- **q6** idrodinamiche (§5.1.3.8); **q7** temperatura (§5.1.3.9, rinvio Cap. 3).
- **q8** parapetti/urto (§5.1.3.10): parapetti **h ≥ 1,10 m**, azione orizzontale **1,5 kN/m**; barriere per
  classe di contenimento; forze da urto amplificate ×**1,50** per l'impalcato; γ **unitario** per l'urto.
- **q9** resistenze passive dei vincoli (§5.1.3.11).
- **E** sismiche (§5.1.3.12): **ψ2j = 0,0** di regola, **0,2** in zona urbana di intenso traffico.
- **A** eccezionali (§5.1.3.13): protezione dei **piedritti** a distanza ≤ 5,0 m dalla sede stradale.

## 7. Combinazioni (§5.1.3.14)

- **Gruppi di azioni** Tab. 5.1.IV (1, 2a, 2b, 3, 4, 5): combinano modello principale, veicoli speciali,
  folla, frenatura e centrifuga con valori caratteristici/frequenti/di combinazione.
- **Coefficienti parziali SLU** Tab. 5.1.V (colonne **EQU / A1 / A2**): g1/g3 sfav. 1,10/1,35/1,00; g2 sfav.
  1,50/1,50/1,30; traffico γQ sfav. **1,35/1,35/1,15**; altre variabili sfav. 1,50/1,50/1,30.
- **Coefficienti ψ** Tab. 5.1.VI (es.: Schema 1 tandem ψ0 = 0,75; distribuiti/concentrati ψ0 = 0,40;
  temperatura ψ0 = 0,6, ψ2 = 0,5).

## Cosa la skill NON fa

- **Non calcola** le sollecitazioni né esegue le verifiche; **non dimensiona** l'impalcato, le pile o gli
  appoggi; non individua la disposizione più gravosa dei carichi mobili al posto del progettista.
- **Non riproduce** le **Fig. 5.1.1/5.1.2/5.1.3** (numerazione corsie, geometrie degli Schemi di Carico e
  delle impronte, diffusione dei carichi): rinvio al testo NTC e all'**EC1 (UNI EN 1991-2)**.
- **Non tratta** i **ponti ferroviari** (§5.2), la **fatica** e le verifiche di dettaglio (§5.1.4), né la
  **progettazione sismica dei ponti** (§7.9). **Non riproduce** la **Circolare 21/1/2019 n. 7**.
