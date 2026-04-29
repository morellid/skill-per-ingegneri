# Modulistica edilizia unificata + Salva Casa

> Versione: 0.1.0-alpha
> Stato: in sviluppo (Livello 1 di validazione)

Skill di supporto per la **scelta del modulo edilizio nazionale unificato** (Edilizia libera, CILA, SCIA, SCIA alternativa al PdC, Permesso di Costruire, Sanatoria art. 36 / art. 36-bis) e l'**identificazione degli allegati** richiesti, ai sensi del **DPR 380/2001** e della **Tabella A del D.Lgs. 222/2016**, integrata con le modifiche del **Salva Casa** (DL 69/2024 conv. L. 105/2024) e con la **modulistica nazionale unificata** aggiornata in **Conferenza Unificata il 27/3/2025**.

## Target

- **Ingegneri edili** e progettisti
- **Architetti** e **geometri**
- **Tecnici degli sportelli SUE/SUAP** comunali
- **Studi professionali** che assistono privati e imprese nella presentazione di pratiche edilizie

## Cosa fa

Tre sotto-attivita' (vedi [SKILL.md](SKILL.md) per il dettaglio tecnico):

1. **Determina regime edilizio e modulo**: dato l'intervento (tipologia, immobile, parti strutturali, vincoli, zona urbanistica) propone il modulo corretto citando articolo DPR 380 e voce Tabella A D.Lgs. 222/2016.
2. **Genera elenco allegati per modulo**: per il modulo individuato, restituisce l'elenco strutturato degli allegati (sempre obbligatori, condizionali, facoltativi) come da modulistica nazionale 2025.
3. **Verifica applicabilita' Salva Casa**: applica le modifiche introdotte dal DL 69/2024 (tolleranze art. 34-bis, sanatoria semplificata art. 36-bis, cambio destinazione d'uso art. 23-ter, stato legittimo art. 9-bis, edilizia libera ampliata).

## Cosa NON fa

- **Non legge il regolamento edilizio comunale** o gli strumenti urbanistici locali (PRG/PUC): puo' integrare/ridurre il regime nazionale (es. soglia pertinenze, dotazione standard).
- **Non integra automaticamente le leggi regionali** (recupero sottotetti, paesaggio, distanze).
- **Non valuta la conformita' urbanistica** specifica al PRG/PUC del Comune.
- **Non sostituisce l'istruttoria SUE/SUAP** ne' la valutazione di Conferenza dei Servizi.
- **Non emette pareri** di Soprintendenza, ASL, VVF, Ufficio Sismica.
- **Non calcola** contributi di costruzione, oneri di urbanizzazione, sanzioni.
- **Non sostituisce la firma del tecnico abilitato** sulle asseverazioni.

Vedi [SKILL.md](SKILL.md) e [AGENTS.md](AGENTS.md) per la lista completa.

## Installazione

Skill compatibile con Anthropic Claude Code e OpenAI Codex.

```bash
# Claude Code
cp -r skills/modulistica-edilizia-unificata ~/.claude/skills/

# OpenAI Codex
cp -r skills/modulistica-edilizia-unificata ~/.agents/skills/
```

In alternativa, via symlink dal repo (vedi root [README.md](../../README.md)).

Esempi di prompt che attivano la skill:
- "Devo fare manutenzione straordinaria con sostituzione del solaio: CILA o SCIA?"
- "Quali allegati servono per il PdC di una nuova villetta in zona B?"
- "Il mio intervento rientra nelle nuove tolleranze art. 34-bis Salva Casa?"
- "Posso fare la sanatoria semplificata art. 36-bis per un cambio uso senza titolo?"
- "Cambio di destinazione d'uso da residenziale a B&B post Salva Casa: che modulo serve?"

## Fonti consultate

- **DPR 6/6/2001 n. 380** - Testo Unico Edilizia, versione consolidata vigente
- **D.Lgs. 25/11/2016 n. 222** - SCIA 2, Tabella A sezione II Edilizia
- **DL 29/5/2024 n. 69 conv. L. 24/7/2024 n. 105** - Salva Casa
- **Conferenza Unificata - Modulistica edilizia unificata** aggiornata Salva Casa, 27/3/2025 (Funzione Pubblica)

Dettagli completi (URL canonici, hash, licenza) in [`references/sources.yaml`](references/sources.yaml).
Estratti testuali strutturati in [`references/estratti/`](references/estratti/).

## Avvertenza

Questa skill e' uno strumento di **supporto alla scelta del modulo edilizio** e all'identificazione degli allegati. **Non sostituisce il giudizio del tecnico abilitato firmatario, ne' del responsabile del procedimento dello sportello SUE/SUAP.** Ogni output richiede revisione e firma del professionista. Per casi al limite, interpellare sempre lo sportello SUE comunale prima del deposito.

## Limiti noti

Vedi sezione "Limiti" in [SKILL.md](SKILL.md). In sintesi:
- Skill di **classificazione del regime + lista allegati**, non di redazione del progetto.
- **Non sostituisce** l'istruttoria comunale ne' i pareri di enti terzi (Soprintendenza, ASL, VVF).
- **Non integra** automaticamente regolamenti edilizi comunali, leggi regionali, varianti locali del Salva Casa.
- Per casi borderline (CILA vs SCIA, SCIA vs PdC, art. 36 vs 36-bis), rinvio al **SUE comunale** + tecnico abilitato.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
