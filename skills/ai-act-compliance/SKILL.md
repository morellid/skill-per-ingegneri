---
name: ai-act-compliance
description: Descrizione breve della skill in italiano. Specifica cosa fa, quando usarla, per chi. Esempio "Verifica la completezza e coerenza di un POS rispetto all'Allegato XV D.Lgs. 81/2008. Use when user asks to validate a POS document for Italian construction safety plans."
---

# NOME_LEGGIBILE_SKILL

## Quando usare questa skill

Descrivere in 2-3 frasi quando questa skill e' appropriata e quando non lo e'. Includere il target utente (es. "ingegnere civile / coordinatore sicurezza in fase di esecuzione").

## Avvertenza

Questa skill e' uno strumento di supporto alla redazione/verifica di documenti tecnici. **Non sostituisce il giudizio del professionista firmatario.** L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill non produce documenti pronti al deposito o alla firma.

## Sotto-attivita' disponibili

Questa skill supporta diverse sotto-attivita'. In base alla richiesta dell'utente, carica il file appropriato da `tasks/`:

- **Nome sotto-attivita' 1**: quando l'utente chiede X, leggere `tasks/task-1.md`
- **Nome sotto-attivita' 2**: quando l'utente chiede Y, leggere `tasks/task-2.md`

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera.

## Processo generale

1. Identifica la sotto-attivita' desiderata dall'utente
2. Carica il file `tasks/<task-scelto>.md`
3. Richiedi input necessari come specificato nel task
4. Applica la procedura descritta
5. Produci l'output nel formato atteso
6. Includi sempre nel report finale un rinvio alla verifica del professionista

## Fonti normative

Riferimenti completi in `references/sources.yaml`. Estratti testuali delle fonti pubbliche in `references/estratti/`.

## Limiti

Cosa questa skill NON fa:
- Non produce documenti auto-firmati
- Non sostituisce verifiche di campo
- Non interpreta normativa ambigua senza rinvio al professionista
- [aggiungere limiti specifici della skill]
