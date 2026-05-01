# relazione-cam-dm256-2022

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1)

Skill per la redazione e la verifica della **Relazione Tecnica dei Requisiti Ambientali CAM** ai sensi del **DM 23 giugno 2022 n. 256** (Criteri Ambientali Minimi per l'edilizia pubblica).

## Target

Architetti, ingegneri civili, progettisti e consulenti tecnici che lavorano su commesse pubbliche soggette all'obbligo CAM (art. 57 D.Lgs. 36/2023).

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `identifica-criteri-applicabili` | Data la tipologia (NC/R1/R2/MS), produce la tabella dei criteri CAM obbligatori e facoltativi |
| `draft-relazione-cam` | Guida dialogica per redigere la bozza della Relazione CAM criterio per criterio |
| `check-relazione-cam` | Verifica una relazione esistente e produce la lista delle azioni correttive |

Per il dettaglio tecnico vedi `SKILL.md`.

## Installazione

```bash
# Claude Code
ln -sfn "$(pwd)/skills/relazione-cam-dm256-2022" "$HOME/.claude/skills/relazione-cam-dm256-2022"

# OpenAI Codex
ln -sfn "$(pwd)/skills/relazione-cam-dm256-2022" "$HOME/.agents/skills/relazione-cam-dm256-2022"
```

## Fonti consultate

- **DM 23 giugno 2022 n. 256** (GU n. 183 del 06/08/2022) - CAM edilizia pubblica
- **Allegato DM 256/2022** - testo integrale criteri base e premianti
- **D.Lgs. 36/2023 art. 57** - obbligo CAM negli appalti PA

Dettaglio completo (URL, SHA256) in `references/sources.yaml`. Estratti testuali in `references/estratti/`.

## Limiti noti

Non produce calcoli energetici, capitolati, APE, piani di gestione rifiuti ne' documenti di progetto. E' uno strumento di supporto alla redazione della Relazione CAM. Gli output devono essere rivisti e firmati dal progettista responsabile.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
