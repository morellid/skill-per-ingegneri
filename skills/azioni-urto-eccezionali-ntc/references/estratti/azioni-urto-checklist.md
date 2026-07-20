# Estratto operativo - Azioni eccezionali da urto (NTC 2018 §3.6.3)

> Parafrasi ancorata a `references/fonti/ntc2018-par-3-6-3.md`. Ogni voce cita il paragrafo/tabella/formula
> NTC. La skill **inquadra** classificazione, forze statiche equivalenti e punti di applicazione; **non**
> calcola le sollecitazioni né dimensiona/verifica gli elementi.

## 1. Classificazione (§3.6.3.2, Tab. 3.6.II)

| Categoria | Effetti |
|---|---|
| **1** | Trascurabili sulle strutture |
| **2** | Localizzati su parte delle strutture |
| **3** | Generalizzati sulle strutture |

- Le azioni da urto si applicano agli elementi (o ai loro sistemi di protezione) le cui conseguenze sono di
  **categoria 2 e 3**.

## 2. Urti da traffico veicolare sotto ponti/strutture (§3.6.3.3.1)

- Direzioni **non simultanee**: parallela **Fd,x** e ortogonale **Fd,y**, con **Fd,y = 0,50·Fd,x** [3.6.7].
- **Forze statiche equivalenti** (Tab. 3.6.III):

| Tipo di strada / area | Veicolo | Fd,x [kN] |
|---|---|---|
| Autostrade, strade extraurbane | - | **1000** |
| Strade locali | - | **750** |
| Strade urbane | - | **500** |
| Parcheggi e autorimesse | Automobili | **50** |
| Parcheggi e autorimesse | Veicoli merci > 3,5 t | **150** |

- **Membrature verticali - punti di applicazione**: automobili → **0,5 m** sopra la superficie di marcia (area
  0,25 m × min(1,50 m; larghezza)); in generale → **1,25 m** sopra la superficie (area 0,5 m × min(1,50 m;
  larghezza)).
- **Elementi orizzontali sopra la strada**: **F = r·Fd,x** [3.6.8], con **r = 1,0** fino a **5 m** di altezza
  del sottovia, **decrescente linearmente 1,0→0** tra **5 e 6 m**, **0** oltre **6 m**; intradosso a **10°
  verso l'alto**; area **0,25 × 0,25 m**.
- **Carrelli elevatori**: **F = 5·W** [3.6.9] (W = peso carrello + massimo carico), applicata a **0,75 m** dal
  piano di calpestio.

## 3. Urti da traffico veicolare sopra i ponti (§3.6.3.3.2)

- Sugli **elementi di sicurezza**: forza orizzontale equivalente **100 kN**, agente trasversalmente e
  orizzontalmente **100 mm sotto la sommità** dell'elemento o **1,0 m sopra il piano di marcia** (il minore).
- Verifiche locali dell'impalcato → **§5.1.3.10**.

## 4. Urti da traffico ferroviario (§3.6.3.4)

- Determinare le azioni con **analisi di rischio**; in mancanza, **azioni statiche equivalenti** per distanza
  **d** dall'asse del binario:

| Distanza d | Parallela [kN] | Perpendicolare [kN] |
|---|---|---|
| **d ≤ 5 m** | **4000** | **1500** |
| **5 < d ≤ 15 m** | **2000** | **750** |
| **d > 15 m** | 0 | 0 |

- Applicate a **1,80 m dal piano del ferro**, **non simultanee**; non si applicano ai sostegni di
  tettoie/pensiline.

## 5. Urti di imbarcazioni ed aeromobili (§3.6.3.5)

- Azioni da valutare sulla base di **documenti di comprovata validità** (Cap. 12) - fuori scope.

## Cosa la skill NON fa

- **Non calcola** le sollecitazioni né **dimensiona/verifica** gli elementi o i sistemi di protezione; **non**
  sceglie la categoria di azione al posto del progettista.
- **Non riproduce** le **analisi di rischio** (ferrovia) né le procedure per **imbarcazioni/aeromobili**;
  **non** tratta le **esplosioni** (§3.6.2) né l'**incendio** (§3.6.1, skill `resistenza-fuoco-strutture-ntc`).
- **Non sostituisce** il progettista strutturale né la lettura del §3.6.3 delle NTC 2018 e della Circolare
  applicativa.
