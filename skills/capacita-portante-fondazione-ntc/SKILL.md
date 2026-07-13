---
name: capacita-portante-fondazione-ntc
description: "Calcolo code-driven della capacita' portante di fondazioni superficiali per la verifica GEO a carico limite delle NTC 2018 par. 6.4.2.1 (Approccio 2, A1+M1+R3, gamma_R = 2,3 da Tab. 6.4.I). La formulazione del carico limite viene dal manuale FHWA NHI-06-089 par. 8.4 (eq. 8-1..8-6, fattori Nc/Nq/Ngamma espressioni AASHTO, fattori di forma Table 8-4, falda Table 8-5, dimensioni efficaci per eccentricita' eq. 8-7..8-9 con limite e < B/6), fonte in pubblico dominio usata come altro codice internazionale ai sensi del cap. 12 NTC 2018. Condizioni drenate (c', phi') e non drenate (cu, phi = 0). Output: qult, q_Rd = qult/2,3, R_d = q_Rd*A' e confronto Ed <= Rd. Casi fuori ambito rifiutati (carico inclinato, base inclinata, pendio, terreni stratificati, rottura locale, sisma). Use when an Italian geotechnical or structural engineer needs a preliminary bearing capacity check of a shallow foundation under NTC 2018; the skill does not replace the signed geotechnical design."
license: MIT
area: strutture-geotecnica
title: "Capacita' portante fondazioni superficiali (NTC 6.4.2)"
summary: "Calcolo code-driven del carico limite di fondazioni superficiali (FHWA NHI-06-089 par. 8.4, eq. 8-1..8-6, codice internazionale ex cap. 12 NTC 2018) e verifica GEO NTC 6.4.2.1 (Approccio 2, gamma_R = 2,3): qult, q_Rd, R_d, Ed <= Rd; casi fuori ambito rifiutati"
normative_refs:
  - "NTC 2018 par. 6.4.2.1 + Tab. 6.4.I + cap. 12"
  - "Circolare 7/2019 par. C6.4.2.1"
  - "FHWA NHI-06-089 (2006) par. 8.4"
version: 0.1.0-alpha
status: alpha
tags:
  - ntc-2018
  - geotecnica
  - fondazioni
  - carico-limite
  - code-driven
---

# Capacita' portante fondazioni superficiali (NTC 2018 par. 6.4.2 + FHWA NHI-06-089)

## Quando usare questa skill

Usare quando un ingegnere geotecnico o strutturista italiano deve:

- **Calcolare in via preliminare il carico limite** qult di una fondazione superficiale (nastro o rettangolare) su terreno omogeneo, in condizioni drenate (c', phi') o non drenate (cu), con correzioni per forma (Table 8-4), falda (Table 8-5) ed eccentricita' (dimensioni efficaci, eq. 8-7..8-9).
- **Ottenere la resistenza di progetto NTC**: q_Rd = qult/gamma_R con gamma_R = 2,3 (Tab. 6.4.I, R3) e R_d = q_Rd*A' (forza normale al piano di posa, C6.4.2.1), con confronto **Ed <= Rd** [6.2.1] se l'utente fornisce Ed.
- **Verificare valori** prodotti da fogli di calcolo o software geotecnici.

**Non usare** quando il caso presenta (la skill rifiuta o segnala):

- **Carico inclinato**, **base inclinata**, **piano campagna in pendenza / fondazione su pendio**, **terreni stratificati**, **rottura locale o punzonamento** attesa: paragrafi FHWA 8.4.3.4-8.4.3.7 e 8.4.5 non implementati; per i pendii serve anche la stabilita' globale (NTC 6.4.2.1, Approccio 1).
- **Azioni sismiche** (criteri NTC par. 7.11.5.3.1), verifica a **scorrimento** (gamma_R = 1,1), verifiche **STR** e **SLE** (per i cedimenti vedere [`cedimenti-edometrici-ntc`](../cedimenti-edometrici-ntc/)).
- Stima dei **parametri geotecnici**: vengono dalla relazione geotecnica; le correlazioni SPT (Table 8-1 FHWA) non sono implementate.

## Avvertenza

Questa skill e' uno strumento di supporto e **non sostituisce il progetto geotecnico firmato**. La formulazione del carico limite proviene da un codice internazionale (FHWA NHI-06-089) utilizzato ai sensi del **cap. 12 NTC 2018**, che pone in capo al progettista la responsabilita' di "garantire espressamente livelli di sicurezza coerenti" con le NTC. Il quadro della verifica (Ed <= Rd, Approccio 2, gamma_R) e' quello delle NTC; Ed va calcolato dall'utente con i coefficienti A1 (Tab. 6.2.I).

## Sotto-attivita' disponibili

- **Calcolo capacita' portante**: l'utente chiede "qual e' il carico limite della mia fondazione?", "verifica a carico limite NTC", "q_lim con falda a -1,5 m", fornisce B/L/Df/parametri -> leggi [`tasks/calcola-capacita-portante.md`](tasks/calcola-capacita-portante.md). Usa SEMPRE il modulo [`tasks/lib/capacita_portante.py`](tasks/lib/capacita_portante.py) (test in [`tasks/lib/test_capacita_portante.py`](tasks/lib/test_capacita_portante.py)): mai calcoli a mano.

## Processo generale

1. **Screening fuori ambito** (carico inclinato, pendio, stratificazione, sisma...): se presente, rifiuta con citazione e rinvia al progettista.
2. **Raccogli gli input** (geometria, condizione drenata/non drenata, parametri caratteristici, falda, eventuale Ed) ed esegui il modulo.
3. **Cita sempre** le equazioni FHWA usate ([8-2]..[8-6], Table 8-4/8-5) e la catena NTC (6.4.2.1 Approccio 2, Tab. 6.4.I gamma_R = 2,3, Tab. 6.2.II M1 = 1,0, condizione [6.2.1]).
4. Riporta **integralmente le avvertenze** del modulo e i casi rifiutati senza aggirarli (es. eccentricita' >= 1/6: "the footing should be resized").
5. Concludi con le verifiche non coperte e il **rinvio al progettista firmatario**.

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti (scaricate, hashate e trascritte in [`references/fonti/`](references/fonti/)):

- **DM 17 gennaio 2018 (NTC 2018)** - parr. 6.2.4.1.1-6.2.4.1.2 (Tab. 6.2.I/6.2.II), 6.4.2-6.4.2.1 (Tab. 6.4.I), cap. 12 - [`ntc2018-dm-17-01-2018.md`](references/fonti/ntc2018-dm-17-01-2018.md)
- **Circolare 7/2019 C.S.LL.PP.** - par. C6.4.2.1 - [`circ-7-2019-mit.md`](references/fonti/circ-7-2019-mit.md)
- **FHWA NHI-06-089 "Soils and Foundations - Reference Manual Volume II"** (U.S. DOT, 2006, pubblico dominio) - parr. 8.4.2-8.4.3.3 - [`fhwa-nhi-06-089.md`](references/fonti/fhwa-nhi-06-089.md)

Estratto operativo: [`references/estratti/fhwa-capacita-portante-ntc.md`](references/estratti/fhwa-capacita-portante-ntc.md).

## Limiti

Cosa questa skill NON fa:

- Non calcola **Ed** (combinazioni e coefficienti A1: a carico dell'utente) e non esegue **scorrimento**, **stabilita' globale**, **STR**, **SLE**, **verifiche sismiche**.
- Non copre carico inclinato, base inclinata, pendii, terreni stratificati, rottura locale/punzonamento (FHWA 8.4.3.4-8.4.3.7, 8.4.5): **rifiuto esplicito**.
- Non accetta eccentricita' **e >= 1/6** della dimensione su terreno (FHWA 8.4.3.1: ridimensionare).
- Non stima c', phi', cu, gamma, posizione della falda: input dalla relazione geotecnica.
- **dq** solo come input esplicito (Table 8-6, condizioni della fonte); default conservativo 1,0.
- Non usa capacita' **presuntive** (FHWA 8.4.8) ne' correlazioni SPT (Table 8-1).

**Ogni output e' supporto al progettista, non sostituzione.**
