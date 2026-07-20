# Estratto operativo - Costruzioni di calcestruzzo (NTC 2018 §4.1)

> Parafrasi ancorata a `references/fonti/ntc2018-par-4-1.md`. Ogni voce cita il paragrafo/formula NTC.
> La skill inquadra classi, coefficienti, resistenze di progetto e verifiche; **non** calcola le
> resistenze, **non** esegue le verifiche, **non** arma.

## 1. Classi di resistenza e analisi (§4.1, 4.1.1)

- **Classe di resistenza** (Tab. 4.1.I): da **C8/10** a **C90/105** (calcestruzzo normale); i valori
  caratteristici fck/Rck e le proprietà del materiale sono al **§11.2**.
- **Analisi**: elastica lineare (anche con ridistribuzione), plastica, non lineare. Limite dell'asse neutro
  nelle sezioni critiche: **x/d ≤ 0,45 per fck ≤ 50 MPa** e **≤ 0,35 per fck > 50 MPa**.

## 2. Resistenze di progetto (§4.1.2.1.1)

- **Calcestruzzo a compressione**: **fcd = αcc·fck/γc** [4.1.3], con **αcc = 0,85** e **γc = 1,5**. γc
  riducibile a **1,4** per produzione continuativa controllata (CoV ≤ 10%, sistema qualità §11.8.3). Per
  elementi piani gettati in opera con **spessore < 50 mm** → resistenza ridotta a **0,80·fcd**.
- **Calcestruzzo a trazione**: **fctd = fctk/γc** [4.1.4] (γc = 1,5).
- **Acciaio**: **fyd = fyk/γs** [4.1.5], con **γs = 1,15** (sempre, tutti i tipi di acciaio, anche
  precompressione: fpyk/fp(0,1)k/fp(1)k).
- **Aderenza**: fbd con η1 = 1,0 (buona) / 0,7 (non buona) e η2 = 1,0 per Φ ≤ 32 mm, (132−Φ)/100 per Φ > 32
  mm [4.1.7].

## 3. Diagrammi di calcolo (§4.1.2.1.2)

- **Calcestruzzo**: parabola-rettangolo, triangolo-rettangolo, rettangolo (stress block); per classi **≤
  C50/60**: **εc2 = 0,20%**, **εcu = 0,35%** (εc3 = 0,175%, εc4 = 0,07%); per classi > C50/60 valori da
  formula. Modello per il **calcestruzzo confinato** disponibile.
- **Acciaio**: bilineare finito o elastico-perfettamente plastico.

## 4. Stati limite ultimi (§4.1.2.3)

- **Pressoflessione**: conservazione delle sezioni piane, calcestruzzo non reagente a trazione, diagrammi di
  calcolo.
- **Taglio**: modello a **traliccio** con inclinazione dei puntoni **1 ≤ ctgθ ≤ 2,5** [4.1.25]; resistenza
  con/senza armature trasversali (VRsd, VRcd).
- **Torsione**: traliccio periferico, **1 ≤ ctgθ ≤ 2,5** [4.1.38]. **Punzonamento** e carichi concentrati.

## 5. Stati limite di esercizio (§4.1.2.2)

- **Fessurazione**: stati limite di **decompressione**, **formazione delle fessure**, **apertura delle
  fessure** con **w1 = 0,2 mm**, **w2 = 0,3 mm**, **w3 = 0,4 mm**. La scelta dipende da **condizioni
  ambientali** (ordinarie/aggressive/molto aggressive), **sensibilità delle armature** (poco/molto sensibili)
  e **combinazione** (frequente, quasi permanente).
- **Limitazione delle tensioni**: **σc ≤ 0,60·fck** (combinazione caratteristica) [4.1.15]; **σc ≤ 0,45·fck**
  (combinazione quasi permanente) [4.1.16]; **σs ≤ 0,8·fyk** [4.1.17].
- **Deformazione** e **vibrazioni**: spostamenti entro limiti compatibili con l'uso e gli elementi non
  strutturali.

## Cosa la skill NON fa

- **Non calcola** le resistenze né esegue le verifiche; **non dimensiona** né **arma** gli elementi.
- **Non riproduce** le proprietà dei materiali (fck, fctk, fyk, moduli) dei **§11.2/11.3** né gli
  **Eurocodici** (UNI EN 1992); **non tratta** la **progettazione sismica** (§7.4) né i calcestruzzi
  speciali (leggeri §4.1.12, fibrorinforzati §11.2.12).
- **Non sostituisce** il progettista strutturale né la **Circolare 7/2019**. È complementare (documentale) a
  `predimensionamento-flessione-ca-ntc` (predimensionamento a flessione, code-driven).
