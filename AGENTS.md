# AGENTS.md - skill-per-ingegneri

> File di guida cross-agent secondo lo standard aperto [AGENTS.md](https://agents.md/), governato dalla Linux Foundation Agentic AI Foundation. Letto nativamente da Codex, Cursor, Windsurf, GitHub Copilot, Devin, Amp, Antigravity e altri tool. Claude Code usa il suo formato (`CLAUDE.md` + `SKILL.md`); le skill in questo repo sono compatibili con entrambi.

## Cos'e' questo repository

`skill-per-ingegneri` e' un **catalogo di skill AI** per la pratica dell'ingegneria italiana. Ogni skill in `skills/<nome>/` e' un pacchetto autonomo con `SKILL.md` (entry point) + `tasks/` (sotto-attivita') + `references/` (estratti normativi + sources.yaml) + `examples/`.

Le skill sono pensate per girare come pacchetti installabili dentro un agent (Claude Code, OpenAI Codex), oppure essere referenziate come contesto da agent che leggono AGENTS.md.

## Skill disponibili

Vedi [`README.md`](README.md) per l'elenco aggiornato. Al momento:

- `skills/pos-allegato-xv-checker/` - verifica POS rispetto Allegato XV D.Lgs. 81/2008
- `skills/dvr-generico/` - DVR per imprese italiane di qualunque settore (D.Lgs. 81/2008 art. 17, 28, 29)
- `skills/gdpr-registro-dpia/` - Registro art. 30 GDPR + DPIA art. 35
- `skills/ai-act-compliance/` - AI Act italiano (versione preliminare; la versione inglese full-feature e' nel repo separato `ai-act-skill`)
- `skills/nis2-self-assessment/` - self-assessment NIS2 italiana (D.Lgs. 138/2024 + Det. ACN 164179/2025 -> 379907/2025): perimetro essenziale/importante, gap analysis misure di base, verifica incidente significativo, obblighi organi di amministrazione
- `skills/spettro-risposta-ntc/` - calcolo code-driven dello spettro di risposta elastico orizzontale ai sensi NTC 2018 par. 3.2 + Circ. 7/2019; modulo Python con test suite, output verificabile vs foglio Excel CSLP
- `skills/pfte-allegato-i7-checker/` - checklist e verifica completezza elaborati PFTE / progetto esecutivo di lavori pubblici ai sensi D.Lgs. 36/2023 art. 41 + Allegato I.7 (Codice contratti pubblici), integrato dal correttivo D.Lgs. 209/2024
- `skills/modulistica-edilizia-unificata/` - determinazione del modulo edilizio nazionale unificato (Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / PdC / Sanatoria art. 36 / 36-bis) per un intervento e relativo elenco di allegati, ai sensi DPR 380/2001 + Tabella A D.Lgs. 222/2016, integrato con il Salva Casa (DL 69/2024 conv. L. 105/2024) e con la modulistica unificata aggiornata in Conferenza Unificata il 27/3/2025
- `skills/transizione-5-0-asseverazione/` - asseverazione tecnica ex ante/ex post del Piano Transizione 5.0 (calcolo riduzione consumi 3% struttura / 5% processo, conversione tep, modelli MIMIT) per EGE / ESCo / ingegneri / periti industriali ai sensi DL 19/2024 art. 38 + DM MIMIT-MEF 24/7/2024 + Circolare MIMIT 25877/2024

## Come installarle

Ogni skill si installa singolarmente nella directory skills del tuo agent.

| Agent | Path target |
|---|---|
| Anthropic Claude Code | `~/.claude/skills/<nome-skill>/` |
| OpenAI Codex | `~/.agents/skills/<nome-skill>/` |

Esempi:

```bash
# Claude Code - una sola skill
cp -r skills/pos-allegato-xv-checker ~/.claude/skills/

# Codex - una sola skill
cp -r skills/pos-allegato-xv-checker ~/.agents/skills/

# Claude Code - tutte le skill via symlink
for s in skills/*/; do
  ln -sfn "$(pwd)/$s" "$HOME/.claude/skills/$(basename "$s")"
done

# Codex - tutte le skill via symlink
for s in skills/*/; do
  ln -sfn "$(pwd)/$s" "$HOME/.agents/skills/$(basename "$s")"
done
```

Riavvia il tuo agent (Claude Code o Codex) per la discovery.

## Come usarle (post-installazione)

In Claude Code o Codex, fai una domanda nel dominio della skill. L'agent la carica automaticamente.

```
"Verifica questo POS rispetto all'Allegato XV..."
"Aiutami a redigere un DVR per un'azienda di 30 dipendenti"
"Serve una DPIA per il nostro nuovo sistema di scoring clienti?"
```

In Codex puoi anche invocare esplicitamente:

```
/skills pos-allegato-xv-checker
```

## Convenzioni quando lavori SU questo repo (modifichi le skill)

### Source-grounded
Ogni affermazione normativa in una skill DEVE essere riconducibile a un documento ufficiale catalogato in `skills/<skill>/references/sources.yaml` (con URL, data accessed, SHA256 hash, licenza). Senza fonte, niente affermazione.

### Niente fabricazioni
Se un fatto non e' negli estratti `references/estratti/<skill>/...`, non inventarlo. O scarichi la fonte e aggiorni `sources.yaml`, o segnali la lacuna all'utente.

### Disclaimer obbligatorio
Ogni skill include in `SKILL.md` una sezione "Avvertenza" che dichiara che la skill e' supporto, non sostituto del giudizio del professionista. Mai derogare.

### Plain markdown
Skill, task, esempi sono markdown puro. Niente HTML embed, niente immagini, niente codice eseguibile inline (eccezione: code block illustrativi di output template).

### Lingua italiana per il contenuto
Gli adempimenti sono italiani. Istruzioni, output, esempi sono in italiano. Solo struttura, codice, metadata sono in inglese (convenzione internazionale).

### Progressive disclosure
Ogni skill e' monolitica ma carica i dettagli specifici on-demand. SKILL.md fa da router verso `tasks/<task-scelto>.md` solo quando il task corrispondente e' richiesto.

### Doppio formato (Claude Code + Codex)
Da quando il repo supporta entrambi gli agent (vedi convenzioni in `methodology/generazione-skill.md`):
- Frontmatter SKILL.md con campi: `name`, `description`, **`license: MIT`** (il campo `license` viene utilizzato da Codex; e' ignorato da Claude Code senza problemi)
- Cartella `agents/openai.yaml` per ciascuna skill, con `display_name`, `short_description`, `default_prompt` (Codex UI metadata)
- Tutto il resto del contenuto e' identico per i due agent

### Versioning per skill
Ogni skill ha la sua `CHANGELOG.md` e segue Semantic Versioning. Il repo collettivo non ha una versione unica.

### Quando esegui uno script

- `scripts/new-skill.sh <nome>` - scaffold di una nuova skill dal template
- `scripts/validate.sh <nome>` (o `--all`) - check strutturale di una skill o di tutto il catalogo
- `scripts/fetch-sources.sh <nome>` (o tutto) - scarica le fonti pubbliche in `not_in_repo/`, verifica hash

Esegui `./scripts/validate.sh --all` prima di committare modifiche.

### Commit style
Conventional Commits in inglese (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`). Quando il commit tocca una skill specifica, usa lo scope: `feat(pos-allegato-xv-checker): ...`. Co-authored-by trailer per AI agent che hanno contribuito.

## Cosa NON fare

- Non aggiungere skill che richiedono giudizio professionale non delegabile (calcoli strutturali a firma, certificazioni)
- Non versionare binari (PDF, DOCX, ecc.) - vanno in `not_in_repo/` e sono referenziati via hash in `sources.yaml`
- Non rimuovere il disclaimer di responsabilita' professionale
- Non rompere il formato dual-agent: ogni skill nuova deve avere sia `license: MIT` nel frontmatter che `agents/openai.yaml`

## Disclaimer

Le skill in questo repository sono strumenti di supporto e non sostituiscono il giudizio professionale di ingegneri, RSPP, DPO, CSE/CSP, o altri professionisti firmatari. L'utilizzo improprio o non verificato degli output e' responsabilita' esclusiva dell'utente.
