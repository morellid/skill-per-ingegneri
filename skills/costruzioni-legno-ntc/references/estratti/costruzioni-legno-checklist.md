# Estratto operativo - Costruzioni di legno (NTC 2018 §4.4)

> Parafrasi ancorata a `references/fonti/ntc2018-par-4-4.md`. Ogni voce cita il paragrafo/tabella NTC.
> La skill inquadra classi, coefficienti, resistenze di progetto e verifiche; **non** calcola le
> resistenze, **non** esegue le verifiche, **non** dimensiona.

## 1. Classi di durata del carico (§4.4.4, Tab. 4.4.I)

- Ogni azione di progetto va assegnata a una classe: **permanente** (>10 anni), **lunga durata** (6 mesi-10
  anni), **media durata** (1 settimana-6 mesi), **breve durata** (<1 settimana), **istantaneo**.
- Attribuzione tipica: peso proprio → permanente; variabili magazzini/depositi → lunga; variabili edifici
  (esclusi magazzini) → media; neve qsk → in funzione del sito per as < 1000 m, almeno **media** per
  as ≥ 1000 m; vento medio → breve; picco del vento ed eccezionali → istantaneo.

## 2. Classi di servizio (§4.4.5, Tab. 4.4.II)

- **Classe 1**: umidità in equilibrio a 20 °C, UR aria ≤ 65% (salvo poche settimane/anno).
- **Classe 2**: 20 °C, UR aria > 85% solo per poche settimane/anno.
- **Classe 3**: umidità più elevata della classe 2.
- La classe di servizio definisce la dipendenza di resistenze e moduli elastici dalle condizioni ambientali
  (→ scelta di kmod e kdef).

## 3. Resistenza di progetto e coefficienti (§4.4.6)

**Xd = kmod · Xk / γM** [4.4.1] (Xk dal §11.7; γM da Tab. 4.4.III; kmod da Tab. 4.4.IV).

- **kmod di combinazione** = valore dell'**azione di minor durata** presente nella combinazione.
- **γM** dalla **colonna A** in generale; **colonna B** solo per produzioni continuative con controllo e
  coefficiente di variazione della resistenza ≤ 15% (sistema di qualità §11.7).

**Tab. 4.4.III - γM (SLU, combinazioni fondamentali)**

| Materiale | Colonna A | Colonna B |
|---|---|---|
| Legno massiccio | 1,50 | 1,45 |
| Legno lamellare incollato | 1,45 | 1,35 |
| Pannelli di tavole incollate a strati incrociati (CLT) | 1,45 | 1,35 |
| Pannelli di particelle o di fibre | 1,50 | 1,40 |
| LVL, compensato, pannelli di scaglie orientate (OSB) | 1,40 | 1,30 |
| Unioni | 1,50 | 1,40 |
| **Combinazioni eccezionali** | **1,00** | **1,00** |

- **kmod** (Tab. 4.4.IV): dipende da materiale, classe di servizio e classe di durata. Esempio legno
  massiccio/lamellare in classe di servizio 1: permanente 0,60; lunga 0,70; media 0,80; breve 0,90;
  istantanea 1,10 (in classe 3 i valori scendono: 0,50/0,55/0,65/0,70/0,90).

## 4. Stati limite di esercizio (§4.4.7)

- Valutare **deformazione istantanea** (moduli **medi**) e **a lungo termine** (moduli ridotti col fattore
  **1/(1 + kdef)**), tenendo conto della deformabilità dei collegamenti.
- **kdef** (Tab. 4.4.V): legno massiccio/lamellare/LVL 0,60 (cl. 1), 0,80 (cl. 2), 2,00 (cl. 3). Umidità
  prossima al punto di saturazione con essiccazione sotto carico → sommare a kdef un valore ≥ 2,0.
- **Frecce limite** (requisiti minimi indicativi): freccia **istantanea** da soli variabili (comb. rara)
  **< L/300**; freccia **finale** **< L/200** (L = luce; per mensole, doppio dello sbalzo).

## 5. Stati limite ultimi - resistenza (§4.4.8.1)

- Trazione/compressione **parallela** [4.4.2]/[4.4.3] e **perpendicolare** [4.4.4] alla fibratura (tener
  conto dell'angolo fibratura-tensione).
- **Flessione** [4.4.5a-b]: coefficiente **km = 0,7 (sezioni rettangolari)** / **1,0 (altre sezioni)**.
- **Tensoflessione** [4.4.6] e **pressoflessione** [4.4.7] (stesso km).
- **Taglio** [4.4.8]: τd ≤ fv,d (Jourawski, larghezza ridotta per fessurazioni). **Torsione** [4.4.9]:
  τtor,d ≤ ksh·fv,d (ksh = 1,2 circolari; 1 + 0,15 h/b ≤ 2 rettangolari; 1 altre). Taglio+torsione:
  interazione [4.4.10].

## 6. Stati limite ultimi - stabilità (§4.4.8.2)

- Usare i moduli elastici **caratteristici (frattile 5%)**.
- **Elementi inflessi** (svergolamento) [4.4.11]: σm,d/(kcrit,m·fm,d) ≤ 1; **kcrit,m = 1 per λrel,m ≤ 0,75**;
  = 1,56 − 0,75·λrel,m per 0,75 < λrel,m ≤ 1,4; = 1/λrel,m² per λrel,m > 1,4 [4.4.12].
- **Elementi compressi** (instabilità di colonna) [4.4.13]: σc,0,d/(kcrit,c·fc,0,d) ≤ 1; **kcrit,c = 1 per
  λrel,c ≤ 0,3**, altrimenti [4.4.15-16] con **βc = 0,2 (massiccio)** / **0,1 (lamellare)**.

## 7. Collegamenti, robustezza, fuoco, esecuzione (§4.4.9-4.4.15)

- Collegamenti dimensionati su prove/normative di comprovata validità; **giunti a dita a tutta sezione
  vietati in classe di servizio 3** (§4.4.9).
- Robustezza (§4.4.12): protezione dall'umidità, mezzi/sistemi duttili, limitazione della trazione
  perpendicolare alla fibratura.
- **Resistenza al fuoco** (§4.4.14): rinvio a **UNI EN 1995-1-2** con γM delle combinazioni eccezionali
  (1,00).
- Esecuzione (§4.4.15): scostamento dalla geometria teorica ≤ **1/500 (lamellare)** / **1/300 (massiccio)**
  della distanza tra vincoli; portare il legno all'umidità di equilibrio prima della messa in carico.

## Cosa la skill NON fa

- **Non calcola** le resistenze né esegue le verifiche; **non dimensiona** elementi e collegamenti.
- **Non riproduce** le proprietà dei materiali (fk, moduli) del **§11.7** né gli **Eurocodici** (UNI EN
  1995); **non tratta** la **progettazione sismica** (§7.7).
- **Non sostituisce** il progettista strutturale né la **Circolare 7/2019**.
