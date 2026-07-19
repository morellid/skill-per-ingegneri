# Estratto operativo - Carichi permanenti e sovraccarichi variabili (NTC 2018 §3.1)

> Parafrasi ancorata a `references/fonti/ntc2018-par-3-1.md`. Ogni voce cita il paragrafo/tabella NTC.
> La skill inquadra i valori dei carichi e le riduzioni; **non** calcola i carichi di progetto, **non**
> combina le azioni, **non** dimensiona.

## 1. Pesi propri dei materiali strutturali - G1 (§3.1.2)

Dai valori dei pesi dell'unità di volume della **Tab. 3.1.I** (valori nominali trattati come
caratteristici), tra cui:
- **calcestruzzo armato/precompresso 25,0 kN/m³**; calcestruzzo ordinario 24,0; leggeri 14,0÷20,0;
- **acciaio 78,5 kN/m³**; ghisa 72,5; alluminio 27,0;
- laterizio pieno 18,0; granito 27,0; calcare compatto 26,0; legno 4,0÷8,0; vetro 25,0; acqua 9,81.

Per materiali non in tabella → indagini/normative di comprovata validità.

## 2. Carichi permanenti non strutturali - G2 (§3.1.3)

Tamponature, divisori, massetti, pavimenti, intonaci, controsoffitti, impianti, ecc. Per abitazioni e
uffici, i **tramezzi** possono essere ragguagliati a un **carico equivalente distribuito g2** in funzione
del peso proprio per unità di lunghezza **G2** della partizione:

| G2 [kN/m] | g2 [kN/m²] |
|---|---|
| ≤ 1,00 | 0,40 |
| 1,00 < G2 ≤ 2,00 | 0,80 |
| 2,00 < G2 ≤ 3,00 | 1,20 |
| 3,00 < G2 ≤ 4,00 | 1,60 |
| 4,00 < G2 ≤ 5,00 | 2,00 |

Elementi divisori con **G2 > 5,00 kN/m** → considerati con l'**effettivo posizionamento** sul solaio (non
come carico distribuito equivalente).

## 3. Sovraccarichi variabili qk/Qk/Hk per categoria d'uso (§3.1.4, Tab. 3.1.II)

Valori (qk [kN/m²] uniforme, Qk [kN] concentrato, Hk [kN/m] orizzontale) - estratto:

| Cat. | Ambiente | qk | Qk | Hk |
|---|---|---|---|---|
| A | Residenziale | 2,00 | 2,00 | 1,00 |
| B1 / B2 | Uffici non aperti / aperti al pubblico | 2,00 / 3,00 | 2,00 | 1,00 |
| C1 | Tavoli (scuole, ristoranti…) | 3,00 | 3,00 | 1,00 |
| C2 | Posti a sedere fissi (chiese, teatri…) | 4,00 | 4,00 | 2,00 |
| C3/C4/C5 | Musei/attività fisiche/grandi affollamenti | 5,00 | 5,00 | 3,00 |
| D1 / D2 | Negozi / centri commerciali | 4,00 / 5,00 | 4,00 / 5,00 | 2,00 |
| E1 | Magazzini, archivi, depositi | ≥6,00 | 7,00 | 1,00 |
| F | Rimesse veicoli leggeri (≤30 kN) | 2,50 | 2×10,00 | 1,00 |
| G | Veicoli medi (30-160 kN) | ≥5,00 | 2×50,00 | 1,00 |
| H | Coperture solo manutenzione | 0,50 | 1,20 | 1,00 |

- **Scale comuni, balconi, ballatoi**: qk 4,00 (cat. A/B), o ≥4,00 secondo la categoria servita (C, D).
- **E2** (industriale), **I** (coperture praticabili → categoria di appartenenza), **K** (usi speciali) e i
  **carichi atipici** (macchinari, serbatoi, ecc.): **caso per caso**, indicati in progetto.

## 4. Riduzioni dei sovraccarichi (§3.1.4.1)

- **Area di influenza** (cat. A, B, C, D, H, I), per elemento orizzontale (trave): coefficiente
  **α_A = (5/7)·ψ0 + 10/A ≤ 1,0** (A = area di influenza in m², ψ0 dalla Tab. 2.5.I). Per **C e D**, α_A
  **≥ 0,6**.
- **Numero di piani** (sole cat. A÷D), per membrature verticali (pilastri/setti) di edifici con **> 2
  piani**: **α_n = (2 + (n − 2)·ψ0) / n** (n = numero di piani caricati).
- I due coefficienti **α_A e α_n NON si combinano**.

## 5. Carichi concentrati Qk e orizzontali Hk (§3.1.4.2-3.1.4.3)

- **Qk** (concentrati): **verifiche locali distinte**, **non** contemporanei ai qk d'insieme; impronta
  **50×50 mm** (F: due impronte 100×100 mm a interasse 1,80 m; G: 200×200 mm a 1,80 m).
- **Hk** (orizzontali lineari): **verifiche locali**, **non** combinati con le verifiche d'insieme;
  applicati a **1,20 m** dal piano di calpestio, ai **parapetti/mancorrenti** al **bordo superiore**;
  riguardano tramezzi, pareti, tamponamenti (esclusi i divisori mobili).

## Cosa la skill NON fa

- **Non calcola** i carichi di progetto né **combina** le azioni (skill `combinazioni-carico-ntc`);
  **non dimensiona** gli elementi.
- **Non tratta** i **carichi da ponte** (cap. 5), l'**azione sismica** (§3.2) né il **vento/neve**
  (§3.3/3.4, skill `carichi-atmosferici-ntc`).
- **Non sostituisce** il progettista strutturale né la **Circolare 7/2019**.
