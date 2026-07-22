# Checklist - Verifiche geotecniche SLU: approcci progettuali e coefficienti parziali (NTC 2018 par. 6.2.4)

> Parafrasi operativa dei par. 6.2.2 e 6.2.4 delle NTC 2018, ancorata alla trascrizione verbatim in
> `../fonti/ntc2018-par-6-2-4.md` (PDF GU S.O. n. 8 alla G.U. n. 42 del 20/02/2018, SHA256 `dda1e397...`).
> Ogni voce rinvia al paragrafo/tabella/formula della fonte. La skill e' un **supporto documentale**: non esegue
> le verifiche, non riproduce i coefficienti R specifici di ciascuna opera (par. 6.3-6.11).

## Sezione 1 - Stati limite ultimi e approcci progettuali (par. 6.2.4.1)

- [ ] **EQU** (§6.2.4.1): perdita di equilibrio -> **Einst,d ≤ Estb,d** (azione instabilizzante ≤ stabilizzante);
      fattori parziali dalla **colonna EQU** della Tab. 6.2.I.
- [ ] **STR / GEO** (§6.2.4.1): resistenza di un **elemento strutturale (STR)** o **del terreno (GEO)** ->
      **Ed ≤ Rd** [6.2.1], con Ed effetto delle azioni (γF·Fk), Rd resistenza (parametri Xk/γM, γR sul sistema).
- [ ] **Combinazioni di gruppi** (§6.2.4): azioni **A1/A2**, parametri geotecnici **M1/M2**, resistenze
      **R1/R2/R3**.
- [ ] **Approccio 1** (§6.2.4): **due combinazioni** di gruppi (ognuna critica per aspetti diversi).
- [ ] **Approccio 2** (§6.2.4): **un'unica combinazione** di gruppi.
- [ ] **Default** (§6.2.4): per SLU **non trattati** nei §6.3-6.11 si usa l'**Approccio 1** con **(A1+M1+R1)** e
      **(A2+M2+R2)**; **R1 sempre unitari**; **R2 ≥ 1** (scelti dal progettista in assenza di indicazioni
      specifiche).

## Sezione 2 - Coefficienti parziali (Tab. 6.2.I e 6.2.II)

- [ ] **Azioni - Tab. 6.2.I** (EQU / A1 / A2): **G1** favorevole 0,9/1,0/1,0, sfavorevole **1,1/1,3/1,0**; **G2**
      favorevole 0,8/0,8/0,8, sfavorevole **1,5/1,5/1,3**; **Q** favorevole 0,0, sfavorevole **1,5/1,5/1,3**.
      Terreno e acqua sono **carichi permanenti (strutturali)** quando contribuiscono con peso/resistenza/rigidezza;
      per la spinta delle terre si usano i γG1.
- [ ] **Parametri geotecnici - Tab. 6.2.II** (M1 / M2): **tan φ'k** 1,0 / **1,25**; **c'k** (coesione efficace)
      1,0 / **1,25**; **cuk** (resistenza non drenata) 1,0 / **1,4**; **γ** (peso unita' di volume) 1,0 / 1,0.
- [ ] **Resistenza di progetto Rd** (§6.2.4.1.2): analitica dai **valori caratteristici / γM** (Tab. 6.2.II),
      tenendo conto dei **γR** (gruppi R) **specificati nei paragrafi di ciascuna opera** (§6.3-6.11).

## Sezione 3 - Valori caratteristici (par. 6.2.2)

- [ ] **Definizione** (§6.2.2): il **valore caratteristico** di un parametro geotecnico e' una **stima ragionata e
      cautelativa** del valore del parametro **per ogni stato limite considerato**, dedotta da prove di laboratorio
      e in sito; la caratterizzazione/modellazione e' responsabilita' del **progettista**.

## Cosa la skill NON fa

- [ ] Non **esegue** le verifiche ne' calcola **Ed / Rd**, la spinta o le resistenze.
- [ ] Non riproduce i **coefficienti γR** (gruppi R1/R2/R3) specifici di ciascuna opera (§6.3-6.11): quelli stanno
      nelle skill d'opera (muri/paratie, fondazioni, pali, pendii, scavi, ecc.).
- [ ] Non tratta in dettaglio le **verifiche SLE** geotecniche (§6.2.4.2) ne' sostituisce il progettista o la
      lettura diretta dei par. 6.2.2-6.2.4 delle NTC 2018.
