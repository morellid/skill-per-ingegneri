# Estratto operativo - Costruzioni in muratura (NTC 2018 §4.5)

> Parafrasi ancorata a `references/fonti/ntc2018-par-4-5.md`. Ogni voce cita il paragrafo/tabella NTC.
> La skill inquadra materiali, verifiche e coefficienti; **non** calcola le resistenze, **non** esegue le
> verifiche, **non** dimensiona.

## 1. Materiali e categorie degli elementi (§4.5.2)

- **Elementi artificiali** classificati per **percentuale di foratura Π = 100 F/A** (Tab. 4.5.Ia laterizio
  / 4.5.Ib calcestruzzo): **pieni** (Π ≤ 15%), **semipieni** (15% < Π ≤ 45%), **forati** (45% < Π ≤ 55%).
- Setti minimi: laterizio/silicato **7 mm** interni, **10 mm** esterni; calcestruzzo **18 mm**.
- **Categoria I o II** degli elementi (§11.10.1) → incide su γM.
- **Tipi di muratura**: singolo/doppio paramento; pietra **squadrata**, **non squadrata**, **listata**.

## 2. Caratteristiche meccaniche (§4.5.3)

- **fk** (compressione), **fvk0** (taglio senza azione assiale), **E**, **G**. Se **fk ≥ 8 MPa** →
  controllo sperimentale (§11.10). I valori usati vanno indicati nel progetto.

## 3. Organizzazione strutturale (§4.5.4)

- Struttura **tridimensionale** con comportamento **scatolare**; pannelli resistenti alle azioni
  orizzontali se lunghezza ≥ **0,3·h interpiano**; **cordoli** di piano in c.a. e **incatenamenti**.
- **Spessori minimi muri portanti**: artificiali **pieni 150**, **semipieni 200**, **forati 240**; pietra
  **squadrata 240**, **listata 400**, **non squadrata 500** (mm).
- **Snellezza convenzionale** [4.5.1]: **λ = h0/t ≤ 20**.

## 4. Resistenze di progetto e coefficiente γM (§4.5.6.1)

**fd = fk/γM** ; **fvd = fvk/γM** [4.5.2-4.5.3], con γM dalla **Tab. 4.5.II**:

| Materiale | Classe esecuzione 1 | Classe esecuzione 2 |
|---|---|---|
| Elementi cat. I, malta a prestazione garantita | 2,0 | 2,5 |
| Elementi cat. I, malta a composizione prescritta | 2,2 | 2,7 |
| Elementi cat. II, ogni tipo di malta | 2,5 | 3,0 |

- **Classe 2**: supervisione (capocantiere) + controllo ispettivo (direttore dei lavori). **Classe 1**: in
  più, controllo in loco di malta/cls e dosaggio "a volume" (o malta premiscelata certificata).

## 5. Verifiche SLU (§4.5.6.2)

Stati limite: **pressoflessione fuori piano** (resistenza e stabilità), **pressoflessione nel piano**,
**taglio nel piano**, **carichi concentrati**, travi di accoppiamento. Trascurata la resistenza a
**trazione per flessione**.

- Metodo **semplificato** per carichi laterali: **fd,rid = Φ·fd** [4.5.4]; **Φ** dalla **Tab. 4.5.III** in
  funzione di **λ** e del coefficiente di eccentricità **m = 6 e/t** [4.5.6] (interpolazione sì,
  estrapolazione no).
- **h0 = ρ·h** [4.5.5]; **ρ = 1** per muro isolato, altrimenti Tab. 4.5.IV (in funzione di h/a).
- **Eccentricità**: es (carichi verticali) [4.5.7]; **ea = h/200** (tolleranze) [4.5.8]; **ev = Mv/N**
  (azioni orizzontali) [4.5.9]; combinate **e1 = es + ea**, **e2 = e1/2 + ev** [4.5.10]; **e1 ≤ 0,33 t**,
  **e2 ≤ 0,33 t** [4.5.11].

## 6. Verifiche semplificate per edifici semplici (§4.5.6.4)

Ammesse con **γM = 4,2** se: a) pareti continue dalle fondazioni alla sommità; b) interpiano ≤ **3,5 m**;
c) **≤ 3 piani** (ordinaria) o **4** (armata); d) rapporto fra i lati in pianta **≥ 1/3**; e) **snellezza ≤
12**; f) carico variabile solai **≤ 3,00 kN/m²**; g) percentuali minime di parete (Tab. 7.8.II). Verifica
[4.5.12]: **σ = N/(0,65 A) ≤ fk/γM** (N con γG = γQ = 1, combinazione caratteristica; A area dei muri
portanti al piano).

## 7. Muratura armata (§4.5.7)

Elementi pieni/semipieni con armature (§11.3). **Barre ≥ 5 mm**. Fuori piano: armatura totale **≥ 0,03%**
(0,015% per faccia). Nel piano/taglio: orizzontale **0,04-0,5%** (interasse ≤ 60 cm), verticale
**0,05-1,0%** (≥ 2 cm² alle estremità/intersezioni/aperture, interasse ≤ 4 m). Malta **≥ 10 MPa**, cls **≥
C12/15**, **γs = 1,15**.

## Cosa la skill NON fa

- **Non calcola** le resistenze né esegue le verifiche; **non dimensiona** la muratura.
- **Non tratta** la **progettazione sismica** (§7.8), la **resistenza al fuoco** (§4.5.11), il **cap.
  11.10** (materiali) né gli **Eurocodici** (§4.6).
- **Non sostituisce** il progettista strutturale né la **Circolare 7/2019**.
