# Contribuire a skill-per-ingegneri

## Prima di contribuire

- Essere ingegnere iscritto all'Albo (o professionista equivalente) nel dominio della skill cui si contribuisce.
- Avere familiarita' con il formato skill condiviso da [Anthropic Claude Code](https://claude.com/claude-code) e [OpenAI Codex](https://developers.openai.com/codex), e con lo standard aperto [`AGENTS.md`](https://agents.md/) (governato dalla Linux Foundation Agentic AI Foundation).
- Aver letto [`AGENTS.md`](AGENTS.md) (root del repo), [`methodology/generazione-skill.md`](methodology/generazione-skill.md), e [`methodology/validazione.md`](methodology/validazione.md).
- Per modifiche a una skill specifica: aver letto anche `skills/<skill>/AGENTS.md` (convenzioni di dominio).

## Principi non negoziabili

1. **Solo fonti ufficiali**. Ogni affermazione normativa nelle skill e' riconducibile a un documento identificato in `sources.yaml` con URL, data di consultazione, hash SHA256.
2. **Responsabilita' professionale**. Ogni skill include un disclaimer che l'output non sostituisce il giudizio del professionista firmatario.
3. **Validazione pre-release**. Nessuna skill raggiunge v1.0 senza almeno una validazione da parte di un ingegnere di dominio diverso dall'autore.
4. **Changelog sempre aggiornato**. Ogni modifica incrementa semver e appare in CHANGELOG.md della skill.
5. **Dual-agent obbligatorio**. Ogni skill deve essere installabile e funzionante sia su Claude Code (`~/.claude/skills/<nome>/`) sia su OpenAI Codex (`~/.agents/skills/<nome>/`). Vedi sezione "Requisiti dual-agent" sotto.

## Requisiti dual-agent (obbligatori per ogni skill)

Da quando il repo supporta entrambi gli agent (vedi commit `feat: dual-agent support`), ogni skill nuova o modificata deve includere:

### File obbligatori in `skills/<nome>/`

- **`SKILL.md`** con frontmatter YAML che include i campi:
  - `name` - nome skill in kebab-case (es. `pos-allegato-xv-checker`)
  - `description` - 1-3 frasi che descrivono cosa fa la skill, quando usarla, per chi
  - `license: MIT` - obbligatorio (Codex lo legge; Claude Code ignora i campi extra)

- **`agents/openai.yaml`** - UI metadata per il picker Codex:
  - `display_name` - nome leggibile dall'utente (es. "POS Allegato XV Checker")
  - `short_description` - sintesi 1-2 righe per il picker
  - `default_prompt` - prompt di esempio che attiva la skill in modo naturale

- **`AGENTS.md`** - convenzioni di dominio specifiche per la skill (sources autoritative, articoli normativi rilevanti, validatori se identificati, don't specifici al dominio). Vedi `templates/skill-template/AGENTS.md` come scaffold.

### File standard (gia' obbligatori prima)

- `tasks/` - sotto-attivita' della skill, una per file (progressive disclosure)
- `references/sources.yaml` - catalogo delle fonti normative
- `references/estratti/` - estratti testuali delle fonti pubbliche
- `examples/` - almeno 1 caso conforme + 1 caso problematico
- `CHANGELOG.md` - history della skill in formato Keep a Changelog
- `README.md` - doc utente (dominio, target, limiti)

### Test di compatibilita' (obbligatorio prima del tag release)

```bash
# Claude Code
ln -sfn "$(pwd)/skills/<nome>" "$HOME/.claude/skills/<nome>"
# Avviare Claude Code, verificare discovery + esecuzione di un task

# Codex
ln -sfn "$(pwd)/skills/<nome>" "$HOME/.agents/skills/<nome>"
# Avviare Codex, verificare che la skill appaia nel picker con il display_name
# Eseguire /skills <nome> e provare il default_prompt
```

Se la skill funziona su uno solo dei due, identificare la differenza (frontmatter incompleto, `agents/openai.yaml` mancante, link interni rotti) e correggere prima del release.

## Processo

### Nuova skill

1. Leggi [`methodology/criteri-selezione.md`](methodology/criteri-selezione.md) per valutare se il task proposto e' adatto.
2. Apri una issue con la proposta (cosa fa, su quali fonti si basa, dominio applicativo).
3. Una volta approvata, usa lo scaffold: `scripts/new-skill.sh nome-skill`.
4. Segui [`methodology/generazione-skill.md`](methodology/generazione-skill.md).
5. PR con la skill a versione `0.1.0-alpha`, marcata come draft finche' non passa validazione.

### Modifica a skill esistente

1. Apri una issue che identifica il problema o il miglioramento.
2. PR con modifiche mirate:
   - Bug fix: patch version (`0.1.0 → 0.1.1`)
   - Miglioramento compatibile: minor version (`0.1.0 → 0.2.0`)
   - Breaking change o major update normativo: major version (`0.x.y → 1.0.0`)
3. CHANGELOG.md aggiornato con descrizione e riferimento al trigger normativo se applicabile.

### Aggiornamento fonti normative

Quando una norma cambia (modifica legislativa, decreto attuativo, nuova linea guida):

1. Verifica l'impatto sulle skill che la citano.
2. Aggiorna `sources.yaml`: nuovo URL se cambia, nuova `accessed`, nuovo `sha256`, nuovo `excerpt_path`.
3. Aggiorna gli estratti in `references/estratti/` se necessari.
4. Incrementa la versione della skill.
5. CHANGELOG.md: sezione "Aggiornamento normativo" con riferimento esatto.

## Stile

- **Lingua**: contenuti utente in italiano, struttura/metadata in inglese.
- **Punteggiatura**: caratteri standard ASCII. Evitare trattini lunghi, virgolette tipografiche, apostrofi tipografici.
- **Commit message**: in inglese, formato [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, `refactor:`). Quando il commit tocca una skill specifica, usa lo scope: `feat(pos-allegato-xv-checker): ...`.
- **File YAML**: indentazione 2 spazi.
- **Markdown**: una frase per riga per diff puliti (opzionale).
- **AGENTS.md per skill**: lean, ~30-80 righe. Non duplicare il SKILL.md - aggiunge convenzioni di dominio e pointer alle fonti, non reinstaura la skill.

## Codice di condotta

Il repo ha obiettivi professionali e istituzionali. Discussioni tecniche e critiche costruttive sono benvenute. Polemiche personali, spam e self-promotion non pertinente vengono rimossi.
