---
name: periodo-proprio-t1-ntc
description: Stima code-driven del periodo del modo di vibrare principale T1 di una costruzione ai sensi delle NTC 2018 par. 7.3.3.2 e della Circolare 7/2019 par. C7.3.3.2. Implementa la formula [7.3.6] T1 = 2*sqrt(d) (d = spostamento laterale elastico del punto piu' alto sotto la combinazione [2.5.7] in orizzontale) e la formula semplificata [C7.3.2] T1 = C1*H^(3/4) con C1 = 0,085 (telaio acciaio o legno), 0,075 (telaio c.a.), 0,050 (muratura o altro). Verifica i limiti della stima (H <= 40 m, massa approssimativamente uniforme) e, se TC e' fornito, la condizione T1 <= 2,5*TC per l'analisi lineare statica e il coefficiente lambda (0,85/1,0) della [7.3.7]. Use when an Italian structural engineer needs a preliminary estimate of the fundamental period T1 under NTC 2018 for linear static analysis screening; the skill does not replace modal analysis.
license: MIT
area: strutture-geotecnica
title: "Periodo proprio T1 approssimato (NTC 2018 par. 7.3.3.2)"
summary: "Stima code-driven di T1: formula [7.3.6] T1 = 2*sqrt(d) delle NTC 2018 e formula [C7.3.2] T1 = C1*H^(3/4) della Circ. 7/2019 (C1 = 0,085/0,075/0,050), con check dei limiti (H <= 40 m, massa uniforme), condizione T1 <= 2,5*TC e lambda per le forze [7.3.7]"
normative_refs:
  - "NTC 2018 par. 7.3.3.2"
  - "Circolare 7/2019 par. C7.3.3.2"
version: 0.1.0-alpha
status: alpha
tags:
  - ntc-2018
  - sismica
  - periodo-proprio
  - code-driven
---

# Periodo proprio T1 approssimato (NTC 2018 par. 7.3.3.2 + Circ. 7/2019 par. C7.3.3.2)

## Quando usare questa skill

Usare quando un ingegnere strutturista italiano deve:

- **Stimare in via preliminare il periodo T1** del modo di vibrare principale di una costruzione, per inquadrare la risposta spettrale o verificare l'applicabilita' dell'analisi lineare statica.
- **Applicare la formula [7.3.6]** delle NTC 2018 (T1 = 2*sqrt(d)) a partire dallo spostamento laterale elastico d del punto piu' alto dell'edificio, ottenuto dal proprio modello di calcolo sotto la combinazione [2.5.7] applicata in orizzontale.
- **Applicare la formula semplificata [C7.3.2]** della Circolare 7/2019 (T1 = C1*H^(3/4)) quando non dispone ancora di un modello, con i coefficienti C1 tabellati per tipologia (telaio acciaio/legno 0,085; telaio c.a. 0,075; muratura o altro 0,050).
- **Verificare la condizione T1 <= 2,5*TC** dell'analisi lineare statica e determinare il coefficiente **lambda** (0,85/1,0) della distribuzione di forze [7.3.7], se TC e' noto.
- **Verificare valori** prodotti da altri fogli di calcolo o software.

**Non usare** quando l'utente chiede:

- L'**analisi modale** o il calcolo dello spostamento d: la skill non ha un solutore; d viene dal modello dell'utente.
- Il calcolo di **TC, TD o dell'ordinata spettrale Sd(T1)**: usare la skill [`spettro-risposta-ntc`](../spettro-risposta-ntc/).
- La stima di T1 per **edifici esistenti** con i metodi del cap. 8, per **ponti** o per costruzioni fuori dai limiti della stima semplificata (H > 40 m, massa non uniforme): serve l'analisi modale.
- Formule di letteratura non presenti nelle fonti (la Circolare cita l'esistenza di formulazioni "basate unicamente sul numero di piani" solo per dire che la [7.3.6] e' piu' affidabile: la skill non le implementa).

## Avvertenza

Questa skill fornisce una **stima preliminare** di T1 a supporto del progettista strutturista. **Non sostituisce l'analisi modale ne' il giudizio del professionista firmatario.** La regolarita' in altezza (par. 7.2.1), la condizione alternativa su TD e ogni impiego del valore di T1 nelle verifiche restano responsabilita' del progettista. L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente.

## Sotto-attivita' disponibili

- **Stima del periodo T1**: l'utente chiede "quanto vale il periodo proprio del mio edificio?", "posso usare l'analisi statica lineare?", "T1 con la formula dell'altezza", "ho lo spostamento in sommita', calcolami T1" -> leggi [`tasks/stima-periodo-t1.md`](tasks/stima-periodo-t1.md)

Il task usa il modulo deterministico [`tasks/lib/periodo_t1.py`](tasks/lib/periodo_t1.py) (test in [`tasks/lib/test_periodo_t1.py`](tasks/lib/test_periodo_t1.py)): **mai calcolare a mano** i valori.

## Processo generale

1. **Chiedi il metodo** (o deducilo dagli input): con modello disponibile -> [7.3.6] da d; senza modello -> [C7.3.2] da H e tipologia. La Circolare dichiara la [7.3.6] "piu' affidabile" (C7.3.3.2).
2. **Raccogli gli input** e i dati per i check: H, massa approssimativamente uniforme (si/no), eventuali TC e numero di orizzontamenti.
3. **Esegui il modulo Python** e riporta il JSON.
4. **Cita sempre** formula e paragrafo ([7.3.6] NTC 2018 par. 7.3.3.2; [C7.3.2] Circ. 7/2019 par. C7.3.3.2) per ogni valore.
5. **Concludi** con i limiti della stima, il rinvio all'analisi modale nei casi fuori ambito e il rinvio al progettista.

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie (scaricate, hashate e trascritte in [`references/fonti/`](references/fonti/)):

- **DM 17 gennaio 2018 (NTC 2018)** - GU n. 42 del 20/02/2018 S.O. n. 8 - par. 7.3.3.2 ([7.3.6], [7.3.7]) e par. 2.5.3 ([2.5.7]) - [`ntc2018-dm-17-01-2018.md`](references/fonti/ntc2018-dm-17-01-2018.md)
- **Circolare 21 gennaio 2019 n. 7 C.S.LL.PP.** - GU n. 35 dell'11/02/2019 S.O. n. 5 - par. C7.3.3.2 ([C7.3.2] + nota 9) - [`circ-7-2019-mit.md`](references/fonti/circ-7-2019-mit.md)

Estratto operativo: [`references/estratti/t1-formule-e-limiti.md`](references/estratti/t1-formule-e-limiti.md).

## Limiti

Cosa questa skill NON fa:

- Non esegue **analisi modale** e non calcola lo spostamento d (viene dal modello dell'utente, sotto la combinazione [2.5.7]).
- Non calcola **TC, TD, Sd(T1)** ne' lo spettro: rinvio a [`spettro-risposta-ntc`](../spettro-risposta-ntc/).
- Non valuta la **regolarita' in altezza** ne' la condizione alternativa su TD (NTC 7.3.3.2): restano al progettista.
- Non distribuisce le **forze [7.3.7]** sui piani: fornisce solo lambda.
- Non copre **edifici esistenti** (cap. 8 NTC), **ponti**, strutture con isolamento o dissipazione.
- Non implementa formule di **letteratura** esterne alle fonti trascritte.

**Ogni output e' supporto al progettista, non sostituzione.**
