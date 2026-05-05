# Piano di Lavoro Amianto

> Versione: 0.1.0-alpha
> Stato: in sviluppo (Livello 1 - autore-driven, fonti pubbliche)

Skill AI di supporto per il **piano di lavoro amianto** ai sensi dell'**art. 256 del D.Lgs. 81/2008**, nel testo aggiornato dal **D.Lgs. 31 dicembre 2025 n. 213**, con integrazione operativa del **DM 6 settembre 1994**.

## Target

- Datori di lavoro e loro consulenti HSE
- RSPP e ASPP
- Coordinatori sicurezza CSP/CSE
- Imprese specializzate in bonifica/rimozione amianto
- Tecnici che devono fare un precheck prima dell'invio a ASL/ATS/SPSAL

## Cosa fa

Tre sotto-attivita':

1. **[`tasks/valuta-obbligo-e-precheck.md`](tasks/valuta-obbligo-e-precheck.md)** - chiarisce se il caso ricade nel piano di lavoro art. 256 e quali dati mancano.
2. **[`tasks/redigi-piano-lavoro.md`](tasks/redigi-piano-lavoro.md)** - produce una bozza guidata del piano, strutturata sui contenuti minimi obbligatori.
3. **[`tasks/verifica-piano-lavoro.md`](tasks/verifica-piano-lavoro.md)** - controlla completezza e coerenza di un piano gia' scritto.

La skill e' utile soprattutto per distinguere:
- casi di **vera demolizione/rimozione** da casi solo manutentivi o di gestione;
- obblighi del **piano di lavoro** rispetto alla **notifica**;
- carenze formali dell'art. 256 rispetto a carenze tecnico-operative ricavabili dal DM 6/9/1994.

## Installazione

| Agent | Path target |
|---|---|
| Anthropic Claude Code | `~/.claude/skills/piano-lavoro-amianto/` |
| OpenAI Codex | `~/.agents/skills/piano-lavoro-amianto/` |

```bash
# Claude Code
cp -r skills/piano-lavoro-amianto ~/.claude/skills/

# Codex
cp -r skills/piano-lavoro-amianto ~/.agents/skills/
```

Riavviare l'agent.

## Fonti consultate

Dettaglio in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:

- D.Lgs. 31 dicembre 2025 n. 213 (GU n. 6 del 09/01/2026), entrato in vigore il 24/01/2026.
- DM 6 settembre 1994 del Ministero della sanita', con allegato tecnico e allegato 4 sui DPI respiratori.

## Limiti noti

- La skill non sostituisce il professionista firmatario, il medico competente o il responsabile dell'impresa.
- La skill non esegue sopralluoghi, campionamenti, misure ambientali o verifiche di laboratorio.
- La skill non conclude automaticamente sui casi borderline: se il perimetro non e' chiaramente art. 256, restituisce un esito preliminare.
- La skill non sostituisce la modulistica o le procedure telematiche dell'organo di vigilanza territorialmente competente.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
