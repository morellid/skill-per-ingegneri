# Bandi-tipo ANAC - Checker disciplinare di gara

> Versione: 0.1.0-alpha
> Stato: alpha - non validato da esperto di dominio esterno

Verifica la conformita' di un disciplinare di gara agli schemi ANAC obbligatori
(D.Lgs. 36/2023), identifica deroghe non giustificate, clausole mancanti e anomalie
che espongono la procedura al rischio di ricorso TAR.

## Target

RUP (Responsabili Unici del Procedimento), uffici gare, stazioni appaltanti (SA)
che devono pubblicare procedure di appalto pubblico e vogliono verificare la conformita'
del disciplinare prima della pubblicazione.

## Cosa fa

- **Verifica conformita' al bando-tipo ANAC**: controlla che il disciplinare segua la
  struttura e le clausole previste dallo schema ANAC applicabile (tipo contratto + criterio)
- **Identifica anomalie e rischi**: analizza il disciplinare per rilevare clausole non
  conformi al D.Lgs. 36/2023, riferimenti al vecchio codice (D.Lgs. 50/2016), deroghe
  non giustificate, requisiti sproporzionati

Per il dettaglio tecnico di ogni sotto-attivita' vedi `SKILL.md`.

## Installazione

```bash
# Claude Code
ln -sfn "$(pwd)/skills/bandi-tipo-anac-checker" "$HOME/.claude/skills/bandi-tipo-anac-checker"

# Codex
ln -sfn "$(pwd)/skills/bandi-tipo-anac-checker" "$HOME/.agents/skills/bandi-tipo-anac-checker"
```

## Fonti principali

- D.Lgs. 31 marzo 2023 n. 36 - Codice dei contratti pubblici
- ANAC - Schemi di disciplinare di gara per il D.Lgs. 36/2023 (bandi-tipo)
  https://www.anticorruzione.it/-/bandi-tipo

Dettaglio completo in `references/sources.yaml`.

## Limiti noti

- Non redige documenti di gara da zero: verifica e segnala anomalie, non produce il disciplinare
- Non confronta il testo verbatim degli schemi ANAC (documenti lunghi, aggiornati periodicamente):
  verifica la struttura e i requisiti normativi del D.Lgs. 36/2023; per il confronto puntuale
  e' necessario avere il documento ANAC aggiornato
- Non valuta la legittimita' della scelta della procedura ne' la coerenza con il capitolato tecnico
- Non sostituisce la revisione legale per procedure complesse o di importo rilevante
- Soglie europee aggiornate ogni 2 anni dalla Commissione UE: verificare i valori correnti

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
