# Task: inquadra-conseguenze-regolarita

Inquadra le **conseguenze della regolarità (in altezza)** sul **metodo di analisi** e sul **fattore di
comportamento** secondo le **NTC 2018 par. 7.3.1 e 7.3.3.1**. Supporto documentale: **non** calcola la struttura
ne' esegue l'analisi.

## Quando usarla

Il progettista ha stabilito se la costruzione e' regolare in altezza (con `inquadra-regolarita-pianta-altezza`) e
vuole conoscerne le conseguenze normative. Per i criteri di regolarita' usa l'altro task.

## Passi

1. **Fattore di comportamento** (§7.3.1): il limite superiore del fattore di comportamento allo SLV e'
   **q_lim = q0 * KR**, dove **KR** dipende dalla regolarita' **in altezza**:
   - **KR = 1** per costruzioni **regolari in altezza**;
   - **KR = 0,8** per costruzioni **non regolari in altezza** (il fattore di comportamento e' quindi **ridotto**,
     con conseguente aumento della domanda sismica di progetto).
   Il valore di base q0 (Tab. 7.3.II) e le classi di duttilita' (§7.2.2) restano di competenza del progettista e
   **fuori** dall'ambito di questa skill.
2. **Metodo di analisi** (§7.3.3.1): l'**analisi lineare statica** puo' essere effettuata **a condizione che**:
   - il periodo del modo di vibrare principale nella direzione in esame **T1 non superi 2,5 TC o TD**; **e**
   - la costruzione sia **regolare in altezza**.
   Se anche una sola condizione non e' soddisfatta (T1 troppo grande o costruzione non regolare in altezza),
   l'analisi lineare statica **non e' ammessa** e si adotta l'**analisi lineare dinamica** (modale) o l'analisi
   non lineare.
3. **Nota sulla regolarita' in pianta**: la regolarita' in pianta incide su modellazione e distribuzione delle
   azioni, ma il fattore KR e la condizione per l'analisi statica dipendono dalla regolarita' **in altezza**. La
   stima e i limiti di **T1** sono trattati dalla skill `periodo-proprio-t1-ntc` (§7.3.3.2).

Usa la checklist in `../references/estratti/regolarita-checklist.md` (sezione 4).

## Output atteso

Un inquadramento che indichi, a partire dall'esito di regolarita' in altezza: il valore di **KR** (1 o 0,8) da
applicare a q0 e l'**ammissibilita'** dell'analisi lineare statica (con le due condizioni T1 <= 2,5 TC o TD e
regolarita' in altezza), con **rinvio ai paragrafi** NTC. Nessun calcolo strutturale.

## Cosa NON fare

- Non determinare q0 (Tab. 7.3.II) ne' calcolare T1 (rinvio a `periodo-proprio-t1-ntc`); non eseguire l'analisi.
- Non trattare le classi di duttilita' (§7.2.2) ne' la regolarita' dei ponti (§7.9.2.1).
