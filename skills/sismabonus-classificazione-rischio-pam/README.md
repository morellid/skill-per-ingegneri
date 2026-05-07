# Classificazione rischio sismico DM 58/2017 - PAM + IS-V (sismabonus)

> Versione: 0.1.0-alpha
> Stato: in sviluppo - validazione Livello 2 (confronto vs software certificati) NON ancora eseguita

Skill code-driven per il calcolo della classe di rischio sismico di un edificio esistente ai sensi del DM 58/2017 Allegato A (testo aggiornato DM 65/2017, DM 24/2020, DM 329/2020), metodo CONVENZIONALE: PAM + IS-V -> classe finale + salto classi tra stato di fatto e stato di progetto.

## Target

Ingegneri strutturisti italiani che eseguono valutazioni di vulnerabilita' sismica (NTC 2018 cap. 8) e asseverazioni sismabonus su edifici esistenti.

## Cosa fa

- Calcola il PAM (Perdita Annua Media) come area trapezoidale della Curva di Individuazione su 5 punti (SLID convenzionale + SLO + SLD + SLV + SLC) + termine di coda SLR=100% al λ di SLC.
- Calcola l'IS-V (Indice di Sicurezza per la Vita) = PGA_C(SLV) / PGA_D(SLV).
- Attribuisce la classe PAM (8 classi A+..G) e la classe IS-V (7 classi A+..F) usando le tabelle dell'Allegato A punto 2.3.
- Determina la classe finale come la peggiore tra le due (Allegato A punto 2.3).
- Confronta stato di fatto e stato di progetto e calcola il salto classi (Allegato A punto 3).
- Segnala warning sulle curve di individuazione non monotone (TR_C incongruenti).

Per il dettaglio tecnico vedi [`SKILL.md`](SKILL.md) e i task in [`tasks/`](tasks/).

## Cosa NON fa (in v0.1.0-alpha)

- Non esegue l'analisi di vulnerabilita' (NTC 2018 cap. 8): l'utente fornisce TR_C e PGA_C come output dell'analisi.
- Non incorpora il reticolo INGV per PGA_D al sito: l'utente fornisce PGA_D per i 4 SL NTC.
- Non implementa il METODO SEMPLIFICATO per edifici in muratura.
- Non genera l'Allegato B / B-bis (asseverazione tecnica): produce solo numeri e classi.
- Non determina le aliquote fiscali sismabonus.
- Non sostituisce la firma del progettista strutturale.

## Installazione

| Agent | Path target |
|---|---|
| Anthropic Claude Code | `~/.claude/skills/sismabonus-classificazione-rischio-pam/` |
| OpenAI Codex | `~/.agents/skills/sismabonus-classificazione-rischio-pam/` |

```bash
# Claude Code
cp -r skills/sismabonus-classificazione-rischio-pam ~/.claude/skills/

# Codex
cp -r skills/sismabonus-classificazione-rischio-pam ~/.agents/skills/
```

## Fonti consultate

Fonti primarie (tutte pubbliche):
- DM Min. Infrastrutture e Trasporti 28/2/2017 n. 58 - Linee guida per la classificazione del rischio sismico delle costruzioni
- DM MIT 7/3/2017 n. 65 - sostituzione dell'Allegato A
- DM MIT 9/1/2020 n. 24 - aggiornamento sezioni Allegato A
- DM MIT 6/8/2020 n. 329 - aggiornamento ulteriore (testo coordinato vigente)
- NTC 2018 (DM 17/1/2018) - cap. 3.2 (azione sismica), cap. 8 (costruzioni esistenti)
- Circ. MIT 21/1/2019 n. 7 - cap. C8

Dettaglio in [`references/sources.yaml`](references/sources.yaml).

## Limiti noti

Vedi sezione "Cosa NON fa" sopra e [`SKILL.md`](SKILL.md) per il dettaglio completo. **Ogni output va verificato dal progettista strutturale firmatario prima dell'uso per l'asseverazione tecnica (Allegato B / B-bis), il deposito al SUE o la richiesta di detrazione fiscale.**

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
