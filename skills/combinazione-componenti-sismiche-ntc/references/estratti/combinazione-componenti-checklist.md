# Estratto operativo - Combinazione delle componenti dell'azione sismica (NTC 2018 par. 7.3.5)

Checklist di inquadramento per il progettista strutturale. Ogni punto e' ancorato al testo trascritto in
`../fonti/ntc2018-par-7-3-5.md`. La skill **inquadra**, non esegue l'analisi ne' calcola gli effetti.

## 1. Combinazione delle tre componenti (par. 7.3.5)

- [ ] La risposta e' calcolata **unitariamente** per le tre componenti con l'espressione **1,00 x Ex + 0,30 x Ey
      + 0,30 x Ez** [7.3.10]?
- [ ] Gli **effetti piu' gravosi** derivano dal confronto tra le **tre combinazioni** ottenute **permutando
      circolarmente** i coefficienti (coefficiente **1,00** assegnato a turno a Ex, Ey, Ez; **0,30** alle altre
      due)?
      - Comb. 1: 1,00 x Ex + 0,30 x Ey + 0,30 x Ez
      - Comb. 2: 0,30 x Ex + 1,00 x Ey + 0,30 x Ez
      - Comb. 3: 0,30 x Ex + 0,30 x Ey + 1,00 x Ez

## 2. Componente verticale (par. 7.3.5)

- [ ] La **componente verticale (Ez)** e' tenuta in conto **solo nei casi previsti al par. 7.2.2**? (altrimenti
      la combinazione riguarda le due sole componenti orizzontali)

## 3. Variabilita' spaziale del moto (par. 7.3.5)

- [ ] La risposta e' combinata con gli **effetti pseudo-statici** indotti dagli **spostamenti relativi** della
      variabilita' spaziale del moto **solo nei casi del par. 3.2.4.1**?
- [ ] Tale combinazione usa la **radice quadrata della somma dei quadrati (SRSS)** (salvo par. 7.2.2 per gli
      appoggi mobili)?

## 4. Analisi dinamica con integrazione al passo (par. 7.3.5)

- [ ] Si applicano **simultaneamente** le **due componenti orizzontali** della storia temporale (piu' la
      verticale, ove necessario)?
- [ ] **Numero di storie temporali**:
      - **>= 3 storie temporali** -> si usano i **valori piu' sfavorevoli**;
      - **>= 7 diverse storie temporali** -> gli effetti sono la **media dei valori piu' sfavorevoli**.
- [ ] Per la **variabilita' spaziale**: storie temporali **differenziate** alla base, coerenti tra loro e
      generate in accordo con lo spettro appropriato **per ciascun vincolo**; oppure analisi con **moto sincrono**
      e effetti pseudo-statici (par. 3.2.4)?

## Fuori scope (rinvii)

- **Non** esegue l'analisi ne' calcola gli effetti; **non** genera/seleziona le storie temporali.
- Casi che richiedono la **componente verticale**: par. 7.2.2.
- **Variabilita' spaziale del moto**: par. 3.2.4 / 3.2.4.1.
- **Metodi di analisi** (statica/dinamica): par. 7.3.3 / 7.3.4; **spettro di progetto**: par. 3.2 (skill
  `spettro-risposta-ntc`).
