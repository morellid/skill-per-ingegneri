# Estratto operativo - Costruzioni di acciaio (NTC 2018 §4.2)

> Parafrasi ancorata a `references/fonti/ntc2018-par-4-2.md`. Ogni voce cita il paragrafo/tabella NTC.
> La skill inquadra materiali, classi di sezione, coefficienti e verifiche; **non** calcola le resistenze,
> **non** esegue le verifiche, **non** dimensiona.

## 1. Materiali (§4.2.1)

- Gradi da **S235 a S460** (§4.2.1.1); tensioni caratteristiche **fyk** (snervamento) e **ftk** (rottura)
  dalle **Tab. 4.2.I** (sezione aperta) e **4.2.II** (sezione cava), in funzione della qualità e dello
  spessore t (t ≤ 40 mm / 40 < t ≤ 80 mm). Es. S235: fyk 235 / ftk 360; S275: 275/430; S355: 355/510
  (t ≤ 40 mm).
- Bulloni e chiodi (§4.2.1.4): fyb/ftb dal §11.3.4.6. Esecuzione secondo **UNI EN 1090-2**.

## 2. Classificazione delle sezioni (§4.2.3.1)

- Classe **1 - duttili** (Cθ ≥ 3): cerniera plastica con piena capacità rotazionale;
- Classe **2 - compatte** (Cθ ≥ 1,5): momento resistente plastico, rotazione limitata;
- Classe **3 - semi-compatte**: snervamento delle fibre estreme, no momento plastico;
- Classe **4 - snelle**: instabilità locale in campo elastico → **sezione efficace**.
- La classe di una **sezione composta** = valore di classe **più alto** tra gli elementi. I rapporti b/t
  limite sono nelle **Tab. 4.2.III-IV-V** (nel PDF figure, non riprodotte → leggere sulla norma/EC3).

## 3. Metodi di calcolo e analisi (§4.2.3.2-4.2.3.3)

- Capacità della sezione: **E** (tutte le classi), **P** (solo classe 1-2), **EP** (tutte). Analisi
  globale: **E** (tutte), **P** (solo strutture di classe 1), **EP** (tutte) - Tab. 4.2.VI.
- **Secondo ordine trascurabile** se **α_cr = Fcr/FEd ≥ 10** (analisi elastica) o **≥ 15** (plastica)
  [4.2.1]; errore di verticalità trascurabile se **HEd ≥ 0,15·VEd** [4.2.2].

## 4. Coefficienti parziali gamma_M (§4.2.4.1.1, Tab. 4.2.VII)

**Rd = Rk/γM** [4.2.3], con:

| Verifica | Coefficiente |
|---|---|
| Resistenza delle sezioni (classe 1-2-3-4) | **γM0 = 1,05** |
| Instabilità delle membrature | **γM1 = 1,05** (1,10 per ponti stradali/ferroviari) |
| Frattura delle sezioni tese indebolite dai fori | **γM2 = 1,25** |

## 5. Resistenze di progetto SLU (§4.2.4.1.2)

- **Trazione** [4.2.5]: minore fra **Npl,Rd = A·fyk/γM0** [4.2.6] e **Nu,Rd = 0,9·Anet·ftk/γM2** [4.2.7].
- **Compressione** [4.2.9]: **Nc,Rd = A·fyk/γM0** (classi 1-3), **Aeff·fyk/γM0** (classe 4) [4.2.10].
- **Flessione** [4.2.11]: **Mc,Rd = Wpl·fyk/γM0** (classe 1-2), **Wel,min·fyk/γM0** (classe 3),
  **Weff,min·fyk/γM0** (classe 4) [4.2.12-14].
- **Taglio** [4.2.16]: **Vc,Rd = Av·fyk/(√3·γM0)** [4.2.17]. Se **VEd > 0,5·Vc,Rd** [4.2.30] si riduce la
  resistenza a flessione (tensione ridotta (1−ρ)·fyk).
- Presso/tenso-flessione (retta/biassiale) con MN,Rd per sezioni I/H di classe 1-2 [4.2.33-39]; classi 3-4
  verifica elastica/tensionale.

## 6. Stabilità delle membrature (§4.2.4.1.3)

- **Aste compresse** [4.2.41]: **Nb,Rd = χ·A·fyk/γM1** (classi 1-3) [4.2.42]; **χ = 1/(Φ + √(Φ² − λ̄²)) ≤ 1**
  [4.2.44], **Φ = 0,5·[1 + α·(λ̄ − 0,2) + λ̄²]**, α dalla Tab. 4.2.VIII; **λ̄ = √(A·fyk/Ncr)** [4.2.45].
  Instabilità **trascurabile se λ̄ < 0,2** o **NEd < 0,04·Ncr**. Snellezza λ = l0/i limitata a **200
  (principali) / 250 (secondarie)** [4.2.47].
- **Travi inflesse** (svergolamento): χLT con **αLT = 0,21/0,34/0,49/0,76** per le curve **a/b/c/d**
  (Tab. 4.2.IX); λ̄LT = √(Wy·fyk/Mcr) [4.2.51].

## 7. Fatica e SLE (§4.2.4.1.4, 4.2.4.2)

- **Fatica** [4.2.54]: **Δσd ≤ ΔσR/γMf**; per gli **edifici** generalmente **non necessaria** salvo
  dispositivi di sollevamento o macchine vibranti.
- **SLE** (§4.2.4.2): spostamenti verticali e laterali, vibrazioni, plasticizzazioni locali (limiti dalla
  combinazione caratteristica secondo NTC/Circolare).

## Cosa la skill NON fa

- **Non calcola** le resistenze né esegue le verifiche; **non dimensiona** membrature e collegamenti.
- **Non riproduce** le **Tab. 4.2.III-V** (b/t) né la **Tab. 4.2.VIII** (curve), che sono figure → norma/EC3;
  **non riproduce** i materiali del **§11.3.4** né gli **Eurocodici** (UNI EN 1993).
- **Non tratta** la **progettazione sismica** (§7.5); **non sostituisce** il progettista né la **Circolare
  7/2019**.
