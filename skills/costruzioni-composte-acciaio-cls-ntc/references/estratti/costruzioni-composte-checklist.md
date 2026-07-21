# Estratto operativo - Costruzioni composte acciaio-calcestruzzo (NTC 2018 §4.3)

> Parafrasi ancorata a `references/fonti/ntc2018-par-4-3.md`. Ogni voce cita il paragrafo/formula NTC.
> La skill inquadra materiali, coefficienti, sezioni, connessione e colonne; **non** calcola le resistenze,
> **non** esegue le verifiche, **non** dimensiona.

## 1. Ambito e stati limite (§4.3, 4.3.1)

- Strutture in **acciaio per carpenteria** + **calcestruzzo armato** rese **collaboranti** da un **sistema
  di connessione**. Per il resto: rinvio a **§4.1** (c.a.) e **§4.2** (acciaio).
- Oltre agli SLU/SLE dei §4.1/4.2: **SLU di resistenza della connessione** e **SLE della connessione**
  (scorrimenti); considerare le **fasi costruttive**.

## 2. Analisi e classificazione (§4.3.2)

- **Classificazione delle sezioni** come per l'acciaio (§4.2.3): classi **1-2** → distribuzioni **plastiche
  o elastiche**; classi **3-4** → solo **elastiche**. Armatura As in classe 1-2 in **B450C**, condizione
  [4.3.1].
- **Analisi elastica** con **omogeneizzazione n** (viscosità; se le tensioni di lunga durata non
  preponderanti, modulo del cls dimezzato) e **fessurazione** (EJ1 sezione reagente / EJ2 fessurata nelle
  zone a momento negativo).
- **Larghezza collaborante**: **bei = min(Le/8, bi)** (§4.3.2.3).

## 3. Resistenze di progetto e coefficienti (§4.3.3)

**fd = fk/γM** [4.3.6]. Allo **SLU**:

| Componente | γM |
|---|---|
| Calcestruzzo (γC) | **1,5** |
| Acciaio da carpenteria (γA) | **1,05** |
| Acciaio da armatura (γS) | **1,15** |
| Connessioni (γV) | **1,25** |

Allo **SLE** e nelle situazioni **eccezionali**: γM = 1. Classe del calcestruzzo tra **C20/25 e C60/75**
(leggeri LC20/22-LC55/60, densità ≥ 1800 kg/m³).

## 4. Travi con soletta collaborante (§4.3.4)

- **Momento resistente**: **elastico** (limiti fcd/fyd/fsd, cls teso trascurato), **plastico** (compressione
  cls **0,85·fcd**, materiali plasticizzati), **elasto-plastico** (analisi non lineare, ogni classe).
- **Taglio verticale**: affidato **interamente alla trave metallica** (§4.2.4.1.2).
- Lamiera grecata **parallela** all'asse del profilo: **non** conta nel momento resistente.

## 5. Sistema di connessione a taglio (§4.3.4.3)

- **Grado di connessione K = N/Nf** (N connettori presenti, Nf per il pieno momento plastico); connettori
  **duttili** (pioli h ≥ 4·d, d 16-25 mm) → connessione parziale entro i limiti [4.3.7]-[4.3.8].
- **Resistenza dei pioli con testa** (soletta piena): minore fra
  - **PRd,a = 0,8·ftk·(π·d²/4)/γV** [4.3.9] (rottura del piolo);
  - **PRd,c = 0,29·α·d²·√(fck·Ecm)/γV** [4.3.10] (rifollamento del cls);
  con **γV = 1,25**, **ftk ≤ 500 MPa**, **d = 16-25 mm**, **α = 0,2·(hsc/d + 1)** per 3 ≤ hsc/d ≤ 4 e
  **α = 1,0** per hsc/d > 4.
- **Lamiera grecata**: riduzione con **kl = 0,6·b0·(hsc − hp)/hp² ≤ 1,0** [4.3.13] (greche parallele) o
  **kt = 0,7·b0·(hsc − hp)/hp²/nr** [4.3.14] (greche trasversali; solo se ftk < 450 MPa; kt ≤ limiti Tab.
  4.3.II).

## 6. Colonne composte (§4.3.5)

Colonne **parzialmente rivestite**, **completamente rivestite** e **riempite** di calcestruzzo; resistenza,
instabilità locale/globale, pressoinflessione (rinvio al testo).

## Cosa la skill NON fa

- **Non calcola** le resistenze né esegue le verifiche; **non dimensiona** la sezione né la connessione.
- **Non riproduce** le **Fig. 4.3.3/4.3.4** né la **Tab. 4.3.II** (figure/tabella figurata → norma/EC4) né i
  materiali dei **§11.2/11.3**; **non tratta** la **progettazione sismica** (§7.6).
- **Non sostituisce** il progettista strutturale né la **Circolare 7/2019**. Completa la famiglia
  "costruzioni di X" con `costruzioni-calcestruzzo-ntc` (§4.1), `costruzioni-acciaio-ntc` (§4.2),
  `costruzioni-legno-ntc` (§4.4) e `costruzioni-muratura-ntc` (§4.5).
