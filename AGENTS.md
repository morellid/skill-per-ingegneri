# AGENTS.md - skill-per-ingegneri

> Guida cross-agent ([standard aperto](https://agents.md/), Linux Foundation Agentic AI Foundation) per chi **crea o modifica skill in questo repo**. Letta nativamente da Codex, Cursor, Windsurf, GitHub Copilot, Devin, Amp, Antigravity. Claude Code la legge tramite [`CLAUDE.md`](CLAUDE.md), che rinvia qui.
>
> **Per installare e usare le skill** (utenti finali): vedi [`README.md`](README.md). Questo file e' solo per agent che modificano il repo.

## Cos'e' questo repo

Catalogo di skill AI per la pratica dell'ingegneria italiana, in formato dual-agent (Claude Code + OpenAI Codex). Ogni skill in `skills/<nome>/` e' un pacchetto autonomo, source-grounded su norme italiane/UE, scritto in italiano, distribuito come supporto al professionista firmatario (mai sostituto).

Per l'elenco aggiornato delle skill pubblicate: [`README.md`](README.md).

## Struttura minima che un agent deve conoscere

```
skill-per-ingegneri/
├── AGENTS.md                  # questo file
├── CLAUDE.md                  # rinvia ad AGENTS.md
├── README.md                  # doc utenti finali (install/uso)
├── CONTRIBUTING.md            # processo per contributori umani
├── methodology/               # SOP dettagliate (leggi prima di operare)
│   ├── criteri-selezione.md   # quando una skill ha senso
│   ├── generazione-skill.md   # workflow nuova skill
│   ├── validazione.md         # 3 livelli di validazione
│   └── update-cycle.md        # mantenimento post-release
├── templates/skill-template/  # scaffold per scripts/new-skill.sh
├── scripts/                   # new-skill.sh, validate.sh, fetch-sources.sh
└── skills/<nome>/             # le skill
    ├── SKILL.md               # entry point + frontmatter (name, description, license: MIT)
    ├── agents/openai.yaml     # UI metadata Codex
    ├── tasks/                 # sotto-attivita' (progressive disclosure)
    ├── references/
    │   ├── sources.yaml       # catalogo fonti (URL, accessed, sha256, licenza)
    │   └── estratti/          # estratti testuali delle fonti pubbliche
    ├── examples/              # >=1 caso conforme + >=1 caso problematico
    ├── AGENTS.md              # convenzioni di dominio della skill
    ├── README.md              # doc utente della skill
    └── CHANGELOG.md           # semver per skill
```

## Regole non negoziabili (applicano sempre)

1. **Source-grounded**. Ogni affermazione normativa DEVE essere riconducibile a una voce in `skills/<skill>/references/sources.yaml` (URL, `accessed`, `sha256`, licenza). Senza fonte, niente affermazione.
2. **Niente fabbricazioni**. Se un fatto non e' in `references/estratti/`, non inventarlo: o scarichi la fonte e aggiorni `sources.yaml` (vedi `scripts/fetch-sources.sh`), o segnali la lacuna all'utente.
3. **Disclaimer obbligatorio** in ogni `SKILL.md`: la skill e' supporto, non sostituto del professionista firmatario. Mai derogare.
4. **Plain markdown**. Niente HTML, niente immagini, niente codice eseguibile inline (eccetto code block illustrativi).
5. **Italiano per il contenuto utente**, inglese per struttura/codice/metadata.
6. **Dual-agent obbligatorio**:
   - Frontmatter `SKILL.md` con `name`, `description`, `license: MIT` (Codex usa `license`; Claude Code lo ignora senza problemi).
   - File `agents/openai.yaml` con `display_name`, `short_description`, `default_prompt`.
   - Resto del contenuto identico per i due agent.
7. **Progressive disclosure**. `SKILL.md` e' un router leggero: rinvia a `tasks/<task>.md` solo quando il task e' richiesto.
8. **Caratteri ASCII standard**. Niente trattini lunghi, virgolette tipografiche, apostrofi tipografici.

## Quando crei una nuova skill

1. Verifica idoneita' del task secondo `methodology/criteri-selezione.md`.
2. Segui il workflow completo in `methodology/generazione-skill.md` (mapping fonti -> download/hash -> scaffold -> SKILL.md -> tasks -> esempi -> disclaimer -> validazione).
3. Scaffold: `./scripts/new-skill.sh <nome-skill>` (kebab-case).
4. Versione iniziale: `0.1.0-alpha`.
5. Validazione obbligatoria prima del rilascio: `methodology/validazione.md` (almeno Livello 1, Livello 2 da ingegnere di dominio diverso dall'autore prima di v1.0).

## Quando modifichi una skill esistente

- Bug fix -> patch (`0.1.0 -> 0.1.1`).
- Miglioramento compatibile -> minor (`0.1.0 -> 0.2.0`).
- Breaking change o major update normativo -> major (`0.x.y -> 1.0.0`).
- Aggiorna sempre `skills/<skill>/CHANGELOG.md` (Keep a Changelog).
- Se cambia una norma: aggiorna `sources.yaml` (URL, `accessed`, `sha256`), gli `estratti/` se servono, e cita il trigger normativo nel changelog. Vedi `methodology/update-cycle.md`.
- Tocca solo cio' che serve: non ristrutturare skill adiacenti, non riformattare codice non tuo.

## Prima di committare

```bash
./scripts/validate.sh --all          # check strutturale di tutto il catalogo
./scripts/validate.sh <nome-skill>   # check di una skill sola
```

Se hai aggiunto/aggiornato fonti: `./scripts/fetch-sources.sh <nome-skill>` (i binari finiscono in `not_in_repo/`, mai committati; sono referenziati via hash in `sources.yaml`).

## Commit style

Conventional Commits in inglese, con scope quando tocchi una skill specifica:

```
feat(pos-allegato-xv-checker): add modello semplificato DI 9/9/2014
fix(dvr-generico): correct art. 28 citation
docs: clarify dual-agent requirements in AGENTS.md
chore(scripts): bump validate.sh schema check
```

Trailer `Co-authored-by:` per gli AI agent che hanno contribuito.

## Cosa NON fare

- Non aggiungere skill che richiedono giudizio professionale non delegabile (es. calcoli strutturali a firma, certificazioni firmate).
- Non committare binari (PDF, DOCX) - vanno in `not_in_repo/`, referenziati via hash in `sources.yaml`.
- Non rimuovere il disclaimer di responsabilita' professionale.
- Non rompere il formato dual-agent: senza `license: MIT` nel frontmatter o senza `agents/openai.yaml` la skill e' incompleta.
- Non duplicare l'`AGENTS.md` di skill rispetto al `SKILL.md`: deve essere lean (~30-80 righe) e aggiungere convenzioni di dominio, non reinstaurare la skill.
- Non duplicare contenuto tra root `AGENTS.md`, `CLAUDE.md` e `README.md`. Una sola sorgente per ogni informazione.

## Disclaimer

Le skill in questo repository sono strumenti di supporto e non sostituiscono il giudizio professionale di ingegneri, RSPP, DPO, CSE/CSP, o altri professionisti firmatari. L'utilizzo improprio o non verificato degli output e' responsabilita' esclusiva dell'utente.
