# AGENTS.md - capacita-portante-fondazione-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Calcolo code-driven della **capacita' portante di fondazioni superficiali** per la verifica GEO a carico limite di NTC 2018 par. 6.4.2.1 (Approccio 2, A1+M1+R3, gamma_R = 2,3). Formulazione del carico limite dal **FHWA NHI-06-089 par. 8.4** (pubblico dominio), usata come "altro codice internazionale" ex **cap. 12 NTC 2018**. Target: ingegneri geotecnici e strutturisti in fase preliminare.

## Fonti autoritative

Catalogate in `references/sources.yaml`:

- **ntc2018-dm-17-01-2018**: NTC 2018 (hash reale, stesso PDF delle altre skill NTC) - trascrizioni 6.2.4.1.1/6.2.4.1.2 (Tab. 6.2.I/6.2.II), 6.4.2/6.4.2.1 (Tab. 6.4.I), cap. 12 in `references/fonti/ntc2018-dm-17-01-2018.md`
- **circ-7-2019-mit**: Circ. 7/2019 (hash reale) - C6.4.2.1 in `references/fonti/circ-7-2019-mit.md`
- **fhwa-nhi-06-089**: FHWA Vol. II (U.S. DOT 2006, pubblico dominio, hash riproducibile) - trascrizioni 8.4.2-8.4.3.3 in `references/fonti/fhwa-nhi-06-089.md`

Estratto operativo: `references/estratti/fhwa-capacita-portante-ntc.md`.

## Punti chiave (verificati sul testo)

- **Eq. [8-1]/[8-6]**: qult = c*Nc*sc + q*Nq*Cwq*sq*dq + 0.5*gamma*B'*Ngamma*Cwgamma*sgamma (base e piano campagna orizzontali, carico verticale); nota all'eq. 8-6: dq si applica alla sola quota gamma_a*Df, non al sovraccarico applicato
- **Fattori N** (espressioni AASHTO): Nq = e^(pi tan phi) tan^2(45+phi/2) [8-2]; Nc = (Nq-1)cot phi [8-3] / 5,14 per phi=0 [8-4]; Ngamma = 2(Nq+1)tan phi [8-5]. Cross-check Table 8-2 (phi=0: 5,14/1,0/0,0)
- **Forma** (Table 8-4, se L/B < 10): phi=0 -> sc = 1+B/(5L); phi>0 -> sc = 1+(B/L)(Nq/Nc), sq = 1+(B/L)tan phi, sgamma = 1-0,4(B/L). NON cumulabili con i fattori di inclinazione del carico
- **Eccentricita'** ([8-7..8-9]): B' = B-2eB, L' = L-2eL, A' = B'L'; limite e < 1/6 su terreno (1/4 su roccia), oltre: "the footing should be resized"
- **Falda** (Table 8-5, interpolazione): Cwq 0,5@DW=0 -> 1,0@DW=Df; Cwgamma 0,5 fino a Df -> 1,0 a 1,5B+Df
- **dq** (Table 8-6): solo phi 32/37/42 e Df/B 1/2/4/8, con rinterro granulare compattato permanente; "otherwise... conservatively omitted" -> default 1,0
- **NTC**: Ed <= Rd [6.2.1]; Approccio 2 (A1+M1+R3); gamma_R = 2,3 carico limite / 1,1 scorrimento (Tab. 6.4.I); M1 = 1,0 (Tab. 6.2.II); STR senza gamma_R; stabilita' globale in Approccio 1 (A2+M2+R2); sisma ex 7.11.5.3.1
- **C6.4.2.1**: Ed e Rd sono forze NORMALI al piano di posa

## Convenzioni specifiche

### Cosa NON fare
- Non calcolare a mano: usare sempre `tasks/lib/capacita_portante.py`
- Non attribuire la formulazione alle NTC: citarla sempre come FHWA NHI-06-089 par. 8.4 ex cap. 12 NTC
- Non calcolare casi fuori ambito: carico inclinato (8.4.3.5), base inclinata (8.4.3.4), pendio (8.4.3.6), terreni stratificati (8.4.3.7), rottura locale/punzonamento (8.4.5), sisma (NTC 7.11.5.3.1) -> rifiuto con citazione
- Non aggirare il rifiuto per eccentricita' >= 1/6 ("the footing should be resized")
- Non stimare c', phi', cu, gamma o DW (input dalla relazione geotecnica); non usare la Table 8-1 (correlazioni SPT) ne' le capacita' presuntive (8.4.8)
- Non usare dq diverso da 1,0 senza input esplicito dell'utente e senza richiamare le condizioni della Table 8-6
- Non calcolare Ed al posto dell'utente (combinazioni A1) e non spacciare il confronto [6.2.1] per verifica completa (mancano scorrimento, stabilita' globale, STR, SLE)

### Cosa fare
- Screening dei casi fuori ambito PRIMA del calcolo
- Citare per ogni valore l'equazione/tabella FHWA e la catena NTC (6.4.2.1, Tab. 6.4.I, Tab. 6.2.II, [6.2.1])
- Esporre i tre termini di qult separatamente e tutti i fattori
- Riportare integralmente le avvertenze del modulo
- Concludere con le verifiche non coperte e il rinvio al progettista firmatario

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con ingegnere geotecnico, confronto vs esempi pubblicati del manuale FHWA - Example 8-1 - e software geotecnico)

## Stato attuale

- Versione: 0.1.0-alpha (closes #31)
- Task files: 1 (`calcola-capacita-portante.md`) + modulo `tasks/lib/capacita_portante.py` con 21 test
- Esempi: 1 conforme (plinto 2x3 drenato con falda, Ed <= Rd) + 1 caso limite (eccentricita' oltre 1/6, rifiuto)
