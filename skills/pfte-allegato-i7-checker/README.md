# PFTE Allegato I.7 Checker

> Versione: 0.1.0-alpha
> Stato: in sviluppo (Livello 1 di validazione)

Skill di supporto per la generazione della checklist degli elaborati e per la verifica di completezza di un Progetto di Fattibilita' Tecnico-Economica (PFTE) e del progetto esecutivo, ai sensi del **D.Lgs. 31 marzo 2023 n. 36** (Codice dei contratti pubblici) art. 41 + Allegato I.7, integrato dal correttivo **D.Lgs. 31 dicembre 2024 n. 209**.

## Target

- **Ingegneri civili** e progettisti di opere pubbliche
- **RUP** (Responsabili Unici del Procedimento) di stazioni appaltanti
- **Stazioni appaltanti** e PA che bandiscono lavori pubblici
- **Studi professionali** che assistono PA o operatori economici

## Cosa fa

Tre sotto-attivita' (vedi [SKILL.md](SKILL.md) per il dettaglio tecnico):

1. **Genera checklist PFTE**: dato l'inquadramento dell'opera (tipologia, importo, espropri, VIA, BIM, modalita' di affidamento), produce l'elenco strutturato degli elaborati obbligatori con citazione articolo + lettera dell'Allegato I.7.
2. **Verifica completezza PFTE**: dato un PFTE gia' redatto (elenco elaborati, indice, struttura cartelle), segnala mancanze, lacune o elaborati che non rispettano i contenuti minimi.
3. **Verifica coerenza PFTE / esecutivo**: confronta i due livelli sullo stesso intervento per coerenza degli elaborati, dei dati di base e del quadro economico (art. 41 co. 8).

## Cosa NON fa

- **Non e' la verifica della progettazione ex art. 42** del Codice (quella richiede soggetto qualificato e indipendente).
- **Non valuta l'adeguatezza tecnica** dei contenuti dei singoli elaborati.
- **Non sostituisce il giudizio del RUP** sulla congruita' del PFTE rispetto al DIP.
- **Non aggiorna automaticamente** prezzari regionali o tabelle Ministero del Lavoro.
- **Non gestisce regimi pre-1 luglio 2023** (transitorio D.Lgs. 50/2016 - rinvio al RUP).

Vedi [SKILL.md](SKILL.md) e [AGENTS.md](AGENTS.md) per la lista completa.

## Installazione

Skill compatibile con Anthropic Claude Code e OpenAI Codex.

```bash
# Claude Code
cp -r skills/pfte-allegato-i7-checker ~/.claude/skills/

# OpenAI Codex
cp -r skills/pfte-allegato-i7-checker ~/.agents/skills/
```

In alternativa, via symlink dal repo (vedi root [README.md](../../README.md)).

Esempi di prompt che attivano la skill:
- "Quali elaborati servono per il PFTE di una scuola da 4 mln EUR con espropri?"
- "Verifica questo PFTE rispetto all'Allegato I.7"
- "L'esecutivo e' coerente con il PFTE? Confronta i due elenchi"
- "Sto bandendo una manutenzione straordinaria su edificio comunale: cosa devo includere nel PFTE?"

## Fonti consultate

- **D.Lgs. 31/03/2023 n. 36** - Codice dei contratti pubblici, art. 41 + Allegato I.7 (GU n. 87 del 13/04/2023 SO n. 14)
- **D.Lgs. 31/12/2024 n. 209** - Decreto correttivo (GU n. 17 del 22/01/2025 SO)

Dettagli completi (URL canonici, hash, licenza) in [`references/sources.yaml`](references/sources.yaml).
Estratti testuali strutturati in [`references/estratti/`](references/estratti/).

## Avvertenza

Questa skill e' uno strumento di **supporto alla verifica di completezza documentale** di un PFTE/esecutivo. **Non sostituisce il giudizio del progettista firmatario, del RUP, ne' del verificatore della progettazione (art. 42 D.Lgs. 36/2023).** Ogni output richiede revisione e firma del professionista.

## Limiti noti

Vedi sezione "Limiti" in [SKILL.md](SKILL.md). In sintesi:
- Skill di completezza, **non di adeguatezza tecnica**.
- **Non sostituisce la verifica ex art. 42**.
- **Non integra automaticamente** norme regionali o di settore (es. paesaggio, beni culturali, prevenzione incendi).

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
