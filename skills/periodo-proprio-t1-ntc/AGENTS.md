# AGENTS.md - periodo-proprio-t1-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Stima preliminare code-driven del periodo del modo di vibrare principale T1 ai sensi di **NTC 2018 par. 7.3.3.2** (formula [7.3.6]) e **Circolare 7/2019 par. C7.3.3.2** (formula [C7.3.2]). Target: ingegneri strutturisti in fase di inquadramento/screening dell'analisi lineare statica.

## Fonti autoritative

Catalogate in `references/sources.yaml` (stessi PDF e stessi hash delle altre skill NTC del repo):

- **ntc2018-dm-17-01-2018**: DM 17/01/2018 (GU n. 42/2018 S.O. 8) - trascrizione par. 7.3.3.2 e [2.5.7] in `references/fonti/ntc2018-dm-17-01-2018.md`
- **circ-7-2019-mit**: Circ. 7/2019 (GU n. 35/2019 S.O. 5) - trascrizione par. C7.3.3.2 + nota 9 in `references/fonti/circ-7-2019-mit.md`. ATTENZIONE: le pagine del capitolo C7 nel PDF GU sono scansioni senza layer testo; la trascrizione viene dalla lettura visiva di pag. 204 GU.

Estratto operativo: `references/estratti/t1-formule-e-limiti.md`.

## Punti chiave (verificati sul testo)

- **[7.3.6] NTC**: T1 = 2*sqrt(d); d = spostamento laterale elastico del punto piu' alto [m] sotto la combinazione [2.5.7] in orizzontale; valida per costruzioni <= 40 m con massa approssimativamente uniforme, "in assenza di calcoli piu' dettagliati".
- **[C7.3.2] Circolare**: T1 = C1*H^(3/4); C1 = 0,085 (telaio acciaio o legno), 0,075 (telaio c.a.), 0,050 (muratura o qualsiasi altro tipo); H dal piano di fondazione; "in via di prima approssimazione". La Circolare dichiara la [7.3.6] "piu' affidabile".
- **La formula C1*H^(3/4) NON e' nelle NTC 2018**: e' solo nella Circolare (nella NTC 2008 era in norma). Citarla sempre come [C7.3.2] Circ. 7/2019.
- **Analisi lineare statica** (NTC 7.3.3.2): T1 <= 2,5*TC o TD + regolarita' in altezza; forze [7.3.7] con lambda = 0,85 se T1 < 2*TC e >= 3 orizzontamenti, altrimenti 1,0.

## Convenzioni specifiche

### Cosa NON fare
- Non attribuire la formula C1*H^(3/4) alle NTC 2018 (errore frequente da training data: e' della Circolare / vecchia NTC 2008)
- Non usare coefficienti C1 diversi da 0,085 / 0,075 / 0,050 o tipologie non tabellate
- Non presentare come valida una stima con H > 40 m o massa non uniforme: riportare il numero solo con le avvertenze del modulo
- Non calcolare a mano: usare sempre `tasks/lib/periodo_t1.py`
- Non calcolare TC/TD/Sd(T1) (rinvio a `spettro-risposta-ntc`) ne' valutare la regolarita' in altezza
- Non estendere a edifici esistenti (cap. 8), ponti, strutture isolate

### Cosa fare
- Citare formula + paragrafo per ogni valore ([7.3.6] NTC 7.3.3.2; [C7.3.2] Circ. C7.3.3.2)
- Con modello disponibile, preferire (o suggerire) la [7.3.6]
- Concludere sempre con il rinvio all'analisi modale e al progettista firmatario

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con strutturista)

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 1 (`stima-periodo-t1.md`) + modulo `tasks/lib/periodo_t1.py` con 22 test (`test_periodo_t1.py`)
- Esempi: 1 conforme (telaio c.a. 5 piani, H=16 m) + 1 caso limite fuori ambito (H=48 m, massa non uniforme)
