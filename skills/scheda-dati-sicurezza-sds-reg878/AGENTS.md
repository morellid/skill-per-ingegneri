# AGENTS.md - scheda-dati-sicurezza-sds-reg878

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **compilazione** e alla **verifica di completezza**
della **Scheda di Dati di Sicurezza (SDS)** secondo l'**allegato II del REACH**
quale sostituito dal **Reg. (UE) 2020/878** (formato a 16 sezioni). Target:
ingegneri chimici/di processo, RSPP, uffici regolatori dei fornitori di
sostanze/miscele.

**E' una skill documentale/di struttura**: non classifica la sostanza/miscela
(CLP), non compie la valutazione della sicurezza chimica, non ricava i valori.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **reg-ue-2020-878-sds**: Reg. (UE) 2020/878 (sostituisce l'allegato II REACH).
  Fonte eur-lex trattata come **online-only** (`binary_path: null`, `sha256:
  null`): eur-lex non e' riproducibile con hash stabile e blocca gli IP datacenter
  di GitHub Actions (stesso approccio della skill ai-act-compliance). La Parte A
  (0.2-0.3) e la struttura delle 16 sezioni sono trascritte verbatim in
  `references/fonti/reg-ue-2020-878-sds.md`.

Estratto operativo: `references/estratti/sds-16-sezioni-checklist.md`.

## Punti chiave (verificati sul testo)

- **16 sezioni obbligatorie** in ordine fisso (Parte B), ciascuna con sotto-sezioni
  numerate (es. 1.1-1.4, 2.1-2.3, 3.1-3.2, ... 15.1-15.2, 16).
- **Parte A**: SDS compilata da **persona competente** (0.2.3); **divieto di
  indicazioni minimizzanti** non coerenti con la classificazione (0.2.4);
  **datazione** in prima pagina e gestione **revisioni** con segnalazione in
  sezione 16 (0.2.5); formato non a lunghezza prestabilita (0.3.1).
- Per le **miscele** si usa la sotto-sezione **3.2**; per le **sostanze** la 3.1.
- La sezione **11** rinvia alle classi di pericolo del **Reg. (CE) 1272/2008
  (CLP)**; la sezione **16** (miscele) indica il **metodo di valutazione** della
  classificazione.

## Convenzioni specifiche

### Cosa NON fare
- Non **classificare** ai sensi del **CLP** ne' compiere la valutazione della
  sicurezza chimica / scenari d'esposizione.
- Non stabilire **quando** la SDS e' obbligatoria: e' l'**art. 31 REACH** (rinvio,
  non riprodotto).
- Non ricavare **valori** (limiti di esposizione, dati tossicologici/ecologici,
  classi ADR/RID/IMDG/IATA).

### Cosa fare
- Strutturare le 16 sezioni/sotto-sezioni e verificarne completezza e ordine.
- Applicare le prescrizioni generali della Parte A (persona competente,
  datazione/revisione, no indicazioni minimizzanti).
- Chiudere con il rinvio alla persona competente / classificatore CLP.

## Aggiornamento della fonte

eur-lex online-only: a ogni aggiornamento rileggere il testo del Reg. (UE)
2020/878 (ed eventuali modifiche successive dell'allegato II REACH) e aggiornare la
trascrizione in `references/fonti/`.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con esperto REACH/CLP).

## Stato attuale

- Versione: 0.1.0-alpha (closes #35)
- Task files: 2 (`compila-sds.md`, `verifica-completezza-sds.md`)
- Esempi: 2 (sezione 3 per una miscela; revisione e datazione)
