# DNSH PNRR - verifica schede e checklist

> Versione: 0.1.0-alpha
> Stato: in sviluppo (Livello 1 - autore-driven, fonti pubbliche)

Skill AI di supporto alla verifica documentale del principio **DNSH - Do No Significant Harm** per interventi PNRR/PNC, secondo Reg. UE 2020/852, Reg. UE 2021/241 e Guida operativa RGS aggiornata con circolare n. 22/2024.

## Target

- RUP e supporto al RUP
- Progettisti, direttori lavori, collaudatori
- Soggetti attuatori e amministrazioni locali
- Consulenti ambientali / CAM / PNRR
- Tecnici che predispongono relazioni DNSH, checklist ex ante/ex post e fascicoli evidenze

## Cosa fa

Tre sotto-attivita':

1. **`tasks/inquadra-misura-schede.md`** - Inquadra misura, intervento, fase e schede tecniche DNSH applicabili.
2. **`tasks/verifica-checklist.md`** - Verifica checklist ex ante/ex post con esito motivato e lacune documentali.
3. **`tasks/piano-evidenze-report.md`** - Genera piano evidenze e bozza di report DNSH per gara/SAL/collaudo/rendicontazione.

## Installazione

| Agent | Path target |
|---|---|
| Anthropic Claude Code | `~/.claude/skills/dnsh-pnrr-checker/` |
| OpenAI Codex | `~/.agents/skills/dnsh-pnrr-checker/` |

```bash
# Claude Code
cp -r skills/dnsh-pnrr-checker ~/.claude/skills/

# Codex
cp -r skills/dnsh-pnrr-checker ~/.agents/skills/
```

Riavviare l'agent.

## Fonti consultate

Dettaglio in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:

- Regolamento (UE) 2020/852, art. 17 - Tassonomia UE e DNSH.
- Regolamento (UE) 2021/241, art. 5 e 18 - Dispositivo per la ripresa e resilienza.
- Circolare RGS n. 22 del 14 maggio 2024 - aggiornamento Guida DNSH.
- Guida operativa DNSH RGS, terza edizione 2024.

## Limiti noti

- La skill non certifica la conformita' DNSH e non sostituisce firma o responsabilita' del tecnico/RUP/soggetto attuatore.
- La skill non sostituisce le istruzioni specifiche della misura PNRR/PNC, del bando, del decreto di finanziamento o del sistema ReGiS.
- Calcoli specialistici e verifiche di campo restano esterni e devono essere prodotti dai professionisti competenti.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
