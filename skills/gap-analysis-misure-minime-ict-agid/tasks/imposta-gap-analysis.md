# Task: imposta-gap-analysis

Imposta la **gap analysis** dell'ente rispetto agli **8 gruppi di controlli ABSC**
(Circ. AgID 2/2017), controllo per controllo.

## Input richiesti

- **Ente** e conferma di rientrare tra i destinatari (art. 2 c.2 C.A.D.).
- **Perimetro**: sistemi/servizi ICT e eventuali sottoinsiemi omogenei per requisiti di
  sicurezza.
- **Livello obiettivo** (Minimo obbligatorio; Standard; Alto) per ciascun sottoinsieme.

## Procedura

1. **Per ciascun gruppo ABSC** (1, 2, 3, 4, 5, 8, 10, 13) elenca i controlli da valutare
   e, per ognuno, registra:
   - **ABSC_ID** (`x.y.z`) e descrizione;
   - **livello** (Minimo/Standard/Alto) - da **leggere sulla tabella del PDF**, non
     desumere;
   - **Subcategory FNSC** associata (raccordo al Framework Nazionale Cyber Security);
   - **stato di attuazione** (attuato / parziale / non attuato);
   - **evidenze** e **azioni** per colmare il gap.
2. **Priorita'**: i controlli marcati **Minimo** sono **obbligatori** (soglia minima):
   trattali come prioritari.
3. **Sottoinsiemi**: se la struttura e' complessa/eterogenea, applica i livelli in modo
   omogeneo per sottoinsiemi (evitando misure sproporzionate alle piccole realta').
4. **Sintesi**: produci l'elenco dei gap (per gruppo/livello) e il piano di rientro.

## Output atteso

- Tabella di gap analysis per ABSC_ID con livello, stato, evidenze, azioni.
- Elenco dei controlli **Minimo** non ancora attuati (priorita' massima).
- Base per la compilazione del modulo (`compila-modulo-implementazione`).

## Avvertenze

- Il **livello esatto** dei controlli e' nelle tabelle **grafiche del PDF** (pagg.
  ~68-73): leggilo, non inventarlo.
- La skill imposta la valutazione; lo **stato reale** si accerta con analisi tecnica.
