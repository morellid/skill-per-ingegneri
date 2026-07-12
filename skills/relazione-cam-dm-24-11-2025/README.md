# relazione-cam-dm-24-11-2025

> Versione: 1.0.0-alpha | Stato: in sviluppo (validazione Livello 1)

Skill per la redazione e la verifica della **Relazione CAM di progetto** ai sensi del criterio 2.1.1 dell'Allegato 1 al **DM MASE 24 novembre 2025** (Criteri Ambientali Minimi per l'edilizia, GU n. 281 del 3/12/2025, in vigore dal 2/2/2026), secondo il **modello ufficiale MASE** (versione 02/02/2026).

Il DM 24/11/2025 **abroga e sostituisce il DM 23/6/2022 n. 256** (e il correttivo DM 5/8/2024): questa skill sostituisce la precedente `relazione-cam-dm256-2022`. I criteri del vecchio DM restano disponibili negli estratti [STORICO] per il solo regime transitorio (art. 2 DM 24/11/2025 + circolare MASE 10/4/2026).

## Target

Architetti, ingegneri civili, progettisti e consulenti tecnici che lavorano su commesse pubbliche soggette all'obbligo CAM (art. 57 co. 2 D.Lgs. 36/2023).

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `identifica-criteri-applicabili` | Determina il regime (DM 24/11/2025 vs transitorio DM 256/2022) e produce la bozza della Tabella 1 di applicabilita' dei criteri (modello MASE) |
| `draft-relazione-cam` | Guida dialogica per redigere la bozza della Relazione CAM di progetto: sezioni normativa/progetto/allegati, Schede Tipo per criterio |
| `check-relazione-cam` | Verifica una relazione esistente (regime, struttura del modello, criteri, mezzi di prova) e produce la lista delle azioni correttive |

Per il dettaglio tecnico vedi `SKILL.md`.

## Installazione

```bash
# Claude Code
ln -sfn "$(pwd)/skills/relazione-cam-dm-24-11-2025" "$HOME/.claude/skills/relazione-cam-dm-24-11-2025"

# OpenAI Codex
ln -sfn "$(pwd)/skills/relazione-cam-dm-24-11-2025" "$HOME/.agents/skills/relazione-cam-dm-24-11-2025"
```

## Fonti consultate

- **DM MASE 24 novembre 2025** - articolato (GU n. 281 del 3/12/2025)
- **Allegato 1 al DM 24/11/2025** - testo dei criteri (PDF ufficiale MASE, pagina "CAM vigenti")
- **Circolare MASE 10 aprile 2026** - chiarimenti su ambito di applicazione e regime transitorio
- **Modello MASE di Relazione CAM di progetto** (versione 02/02/2026)
- **D.Lgs. 36/2023 art. 57** - obbligo CAM negli appalti PA
- [STORICO] DM 23/6/2022 n. 256 + Allegato - solo regime transitorio

Dettaglio completo (URL, SHA256, trascrizioni) in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

La skill non riproduce i requisiti prestazionali puntuali dei singoli criteri (per ogni criterio applicato va letto il testo integrale nel PDF ufficiale dell'Allegato 1); non produce studi LCA, capitolati, APE, piani di cantiere ne' la Relazione CAM dell'impresa appaltatrice (criterio 3.1.1). Gli output devono essere rivisti e firmati dal progettista responsabile.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
