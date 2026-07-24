# Checklist — Costruzioni di acciaio in zona sismica (NTC 2018 §7.5, regole generali)

Estratto operativo ancorato a `../fonti/ntc2018-par-7-5.md` (NTC 2018, DM 17/1/2018, GU n. 42 del 20/2/2018 —
S.O. n. 8). Ogni valore è tratto dal testo del par. 7.5 letto anche sull'immagine delle pagine PDF 243/245/246.

## 1. Comportamento e materiali (§7.5, §7.5.1)

- [ ] Scelta del **comportamento**: **non dissipativo** (capacità secondo il **§ 4.2**, senza requisiti
      aggiuntivi) oppure **dissipativo** (§§ 7.1-7.3 + regole §§ 7.5.3-7.5.6).
- [ ] Acciaio strutturale conforme al **§ 11.3.4.9**.
- [ ] Fattore di sovraresistenza del materiale **γov = 1,25** per **S235, S275, S355**; **γov = 1,15** per
      **S420, S460**.

## 2. Tipologie strutturali (§7.5.2.1, Fig. 7.5.1)

- [ ] Individuare la tipologia: **a) intelaiate** (zone dissipative alle estremità delle travi); **b) controventi
      concentrici** — b1) diagonale tesa attiva, b2) a V, **b3) a K NON dissipativa**; **c) controventi
      eccentrici** (dissipazione nei traversi per flessione/taglio); **d) a mensola/pendolo inverso**; **e)
      intelaiate con controventi concentrici**; **f) intelaiate con tamponature**.
- [ ] Struttura a un piano con più colonne collegate in sommità e **carico assiale normalizzato ≤ 0,3**: può
      essere considerata **a telaio**.
- [ ] Escluse: strutture con **dispositivi antisismici**; se le forze orizzontali sono assorbite da nuclei/pareti
      in c.a. → **§ 7.4**.

## 3. Fattori di comportamento (§7.5.2.2)

- [ ] **q0** (valore massimo) dalla **Tab. 7.3.II** per tipologia; nel framework generale **q = q0·KR** (§ 7.3.1).
- [ ] **αu/α1** (strutture regolari in pianta): **1,1** (un piano); **1,2** (telaio più piani, 1 campata); **1,3**
      (telaio più piani, più campate); **1,2** (controventi eccentrici più piani); **1,0** (mensola/pendolo inverso).
- [ ] I valori di q0 sono validi solo se rispettate le regole di progetto/dettaglio §§ 7.5.3-7.5.6.

## 4. Regole generali per elementi dissipativi + Tab. 7.5.I (§7.5.3)

- [ ] Zone dissipative **nelle membrature**; collegamenti e componenti non dissipative con **adeguata capacità**.
- [ ] Capacity design del collegamento in zona dissipativa: **Rj,d ≥ 1,1·γov·Rpl,Rd** [7.5.1].
- [ ] Duttilità locale **μ = θu/θy**; capacità al collasso θu alla **riduzione del 15%** della resistenza massima.
- [ ] **Classe della sezione trasversale** (Tab. 7.5.I):

  | Classe di duttilità | Valore di base q0 | Classe di sezione |
  |---|---|---|
  | CD "B" | 2 < q0 ≤ 4 | Classe 1 o 2 |
  | CD "A" | q0 > 4 | Classe 1 |

- [ ] Colonne primarie dissipative dei **telai**: **NEd/Npl,Rd ≤ 0,3** [7.5.3].

## 5. Fuori scope

- [ ] Verifiche di **resistenza (RES)** e di **duttilità (DUT)** di membrature e collegamenti e le regole
      specifiche per tipologia (§§ 7.5.3.1-7.5.3.2, 7.5.4-7.5.6); calcolo del **q0 numerico** (Tab. 7.3.II);
      requisiti **statici** (§ 4.2, skill dedicata) e framework del **fattore q** (§ 7.3.1, skill dedicata).
