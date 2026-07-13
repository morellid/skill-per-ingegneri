# Capacita' portante delle fondazioni superficiali: formulazione FHWA NHI-06-089 par. 8.4 + verifica NTC 2018 par. 6.4.2.1

> Estratto curato. Fonti (trascritte in `references/fonti/`):
> - `fhwa-nhi-06-089.md` (parr. 8.4.2, 8.4.3, 8.4.3.1-8.4.3.3, eq. 8-1..8-9, Tab. 8-4/8-5/8-6)
> - `ntc2018-dm-17-01-2018.md` (parr. 6.2.4.1.1-6.2.4.1.2, 6.4.2, 6.4.2.1; Tab. 6.2.I, 6.2.II, 6.4.I; cap. 12)
> - `circ-7-2019-mit.md` (par. C6.4.2.1)
>
> Ogni affermazione seguente e' parafrasi dei passaggi trascritti nei file sopra.

## 1. Inquadramento normativo

- NTC 6.4.2.1: verifica GEO di **collasso per carico limite** con la
  condizione Ed <= Rd [6.2.1], **Approccio 2 (A1+M1+R3)**: azioni
  amplificate con i coefficienti A1 (Tab. 6.2.I), parametri geotecnici con
  **M1 = 1,0** (Tab. 6.2.II: i valori di progetto coincidono con i
  caratteristici), resistenza divisa per **gamma_R = 2,3** (Tab. 6.4.I,
  carico limite).
- C6.4.2.1: effetto dell'azione e resistenza di progetto sono **forze
  normali al piano di posa**; la resistenza dipende da drenaggio, falda,
  geometria, eccentricita', meccanismo.
- Ne' NTC ne' Circolare danno la **formula del carico limite**: la
  formulazione viene dal **FHWA NHI-06-089 par. 8.4** (pubblico dominio),
  usato come "altro codice internazionale" ex **cap. 12 NTC** (livelli di
  sicurezza coerenti: responsabilita' del progettista).

## 2. Formulazione FHWA (forma generale implementata dalla skill)

qult = c*Nc*sc + (q_appl + gamma_a*Df*dq)*Nq*Cwq*sq + 0.5*gamma*B'*Ngamma*Cwgamma*sgamma

derivata dall'eq. [8-6] con base orizzontale e piano campagna orizzontale
(bc = bq = bgamma = 1) e carico verticale (niente fattori di inclinazione
del carico); il termine di sovraccarico segue la nota all'eq. [8-6]
(dq applicato alla sola quota di approfondimento gamma_a*Df, non al
sovraccarico applicato q_appl).

Fattori di capacita' portante (funzione di phi, eq. [8-2][8-3][8-4][8-5],
espressioni AASHTO 2004 with 2006 Interims):

- Nq = e^(pi*tan phi) * tan^2(45 + phi/2)
- Nc = (Nq - 1)*cot(phi) per phi > 0; Nc = 5,14 per phi = 0
- Ngamma = 2*(Nq + 1)*tan(phi)   (per phi = 0: Ngamma = 0; Nq = 1)

Cross-check: Table 8-2 della fonte, phi = 0 -> Nc = 5,14, Nq = 1,0,
Ngamma = 0,0 (trascritta).

Condizioni: **drenata** (c = c', phi = phi') o **non drenata** (c = cu,
phi = 0). Con M1 = 1,0 i parametri di progetto coincidono con i
caratteristici (Tab. 6.2.II).

## 3. Fattori correttivi implementati

- **Forma** (Table 8-4; da applicare se L/B < 10, il nastro e' L/B >= 10):
  - phi = 0: sc = 1 + B/(5L); sq = sgamma = 1
  - phi > 0: sc = 1 + (B/L)*(Nq/Nc); sq = 1 + (B/L)*tan(phi);
    sgamma = 1 - 0,4*(B/L)
- **Eccentricita'** (eq. 8-7/8-8/8-9): B' = B - 2eB; L' = L - 2eL;
  A' = B'*L' (pressione uniforme equivalente di Meyerhof). **Limiti**: su
  terreno e < 1/6 della dimensione; su roccia e < 1/4; oltre, "the footing
  should be resized" (la skill rifiuta il calcolo). I fattori di forma sono
  calcolati sulle dimensioni efficaci (raccomandazione AASHTO riportata
  dalla fonte).
- **Falda** (Table 8-5, con interpolazione lineare dichiarata dalla fonte):
  - Cwq: 0,5 a DW = 0 -> 1,0 a DW = Df -> 1,0 oltre
  - Cwgamma: 0,5 fino a DW = Df -> 1,0 a DW >= 1,5B + Df (interpolazione
    fra Df e 1,5B + Df)
- **Approfondimento dq** (Table 8-6): valori tabulati solo per phi = 32/37/42
  e Df/B = 1/2/4/8, condizionati a rinterro granulare compattato di qualita'
  e permanente; "otherwise, the depth correction factor can be conservatively
  omitted" -> il modulo usa **dq = 1,0 di default** e accetta un dq esplicito
  dell'utente (da Table 8-6, sotto sua responsabilita').

## 4. Passaggio alla verifica NTC

- q_Rd = qult / gamma_R con gamma_R = 2,3 (Tab. 6.4.I, R3)
- R_d = q_Rd * A' (forza normale al piano di posa, C6.4.2.1)
- Confronto Ed <= Rd [6.2.1]: **Ed** (componente normale della risultante di
  progetto, combinazione con coefficienti **A1**, Tab. 6.2.I) e' un input
  dell'utente; la skill confronta se fornito.
- STR senza gamma_R; scorrimento (gamma_R = 1,1) e stabilita' globale
  (Approccio 1, A2+M2+R2): verifiche distinte, fuori ambito della skill.

## 5. Casi dichiaratamente FUORI ambito (la skill li rifiuta o li segnala)

- **Carico inclinato** (par. 8.4.3.5; inoltre la Table 8-4 vieta l'uso
  simultaneo dei fattori di forma con quelli di inclinazione).
- **Base inclinata** (8.4.3.4) e **piano campagna in pendenza** (8.4.3.6,
  fattori Ncq/Ngamma_q); fondazioni su pendii: anche stabilita' globale NTC.
- **Terreni stratificati** (8.4.3.7): la [8-1] assume terreno omogeneo.
- **Rottura locale / punzonamento** (8.4.5): la formulazione assume rottura
  generale.
- **Azioni sismiche**: criteri aggiuntivi NTC par. 7.11.5.3.1, non coperti.
- Parametri geotecnici (c', phi', cu, gamma) e sovraccarichi: input dalla
  relazione geotecnica; la skill non li stima (la Table 8-1 della fonte,
  correlazioni SPT-phi, non e' implementata).
