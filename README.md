# skill-per-ingegneri

Repository collettivo di skill AI per la pratica dell'ingegneria italiana.

**Catalogo completo e filtrabile: [www.ingegneri.ai](https://www.ingegneri.ai/)** - cerca per nome, filtra per area e apri la scheda di ogni skill con ambito e riferimenti normativi.

## Cosa contiene

Skill AI in formato dual-agent (compatibili sia con [Anthropic Claude Code](https://claude.com/claude-code) sia con [OpenAI Codex](https://developers.openai.com/codex)), scritte in italiano, basate esclusivamente su fonti normative ufficiali (D.Lgs., decreti attuativi, linee guida pubbliche). Ogni skill e' pensata per essere usata da ingegneri iscritti all'Albo come supporto - non sostituto - nella redazione e verifica di documenti tecnici e adempimenti.

Ogni skill e' anche utilizzabile da agent che leggono lo standard aperto [`AGENTS.md`](AGENTS.md) (Codex, Cursor, Windsurf, GitHub Copilot, Devin, Amp, Antigravity, ...).

Contiene anche:
- **Metodologia replicabile** per generare nuove skill (`methodology/`)
- **Template e script** per scaffolding e validazione (`templates/`, `scripts/`)
- **Riferimenti bibliografici** strutturati con hash delle fonti (`sources.yaml` per ogni skill)

## Skill disponibili

L'elenco completo e aggiornato delle skill e' pubblicato come **catalogo filtrabile** su **[www.ingegneri.ai](https://www.ingegneri.ai/)**: cerca per nome, filtra per area (sicurezza, strutture, edilizia, appalti, energia, ambiente, impianti, software e dati, CTU) e apri la scheda di ogni skill con ambito e riferimenti normativi.

Il catalogo e' generato automaticamente dai metadati di ogni skill (`skills/<nome>/SKILL.md`) e raccolto in [`catalog.yaml`](catalog.yaml) da `scripts/build_catalog.py`: e' sempre allineato al contenuto del repo. Ogni skill ha inoltre un proprio `README.md` in `skills/<nome>/` con dettaglio target, sotto-attivita' e limiti noti.

## Struttura

```
skill-per-ingegneri/
├── AGENTS.md                    # guida cross-agent (Codex, Cursor, Copilot, ...)
├── skills/                      # le skill pubblicate (catalogo: www.ingegneri.ai)
│   ├── pos-allegato-xv-checker/
│   │   ├── SKILL.md             # punto d'ingresso + routing (license: MIT in frontmatter)
│   │   ├── agents/
│   │   │   └── openai.yaml      # UI metadata per Codex
│   │   ├── tasks/               # istruzioni dettagliate per sotto-attivita'
│   │   ├── references/          # metadata fonti + estratti normativi
│   │   ├── examples/            # casi d'uso validi e problematici
│   │   └── CHANGELOG.md
│   └── <altre-skill>/           # stessa struttura per ciascuna skill
├── methodology/                 # come si genera e mantiene una skill
├── templates/                   # scaffold dual-agent per nuove skill
└── scripts/                     # utility CLI (new-skill, validate, fetch-sources)
```

## Come installare e usare le skill

Ogni skill in `skills/<nome>/` e' un pacchetto autonomo. Scegli le skill che ti servono dal [catalogo su www.ingegneri.ai](https://www.ingegneri.ai/), poi installane una o piu' nella directory skills del tuo agent con uno dei metodi seguenti.

| Agent | Path target |
|---|---|
| Anthropic Claude Code | `~/.claude/skills/<nome-skill>/` |
| OpenAI Codex | `~/.agents/skills/<nome-skill>/` |

### Installazione di una singola skill

```bash
# Claude Code
cp -r skills/pos-allegato-xv-checker ~/.claude/skills/

# Codex
cp -r skills/pos-allegato-xv-checker ~/.agents/skills/
```

### Installazione di tutto il catalogo via symlink

```bash
# Claude Code
mkdir -p ~/.claude/skills
for s in skills/*/; do
  ln -sfn "$(pwd)/$s" "$HOME/.claude/skills/$(basename "$s")"
done

# Codex
mkdir -p ~/.agents/skills
for s in skills/*/; do
  ln -sfn "$(pwd)/$s" "$HOME/.agents/skills/$(basename "$s")"
done
```

I symlink permettono di aggiornare tutte le skill installate con `git pull` nel repo.

### Installazione via Claude Code plugin marketplace

Le skill sono distribuite anche come marketplace nativo Claude Code: un plugin per ogni area del catalogo. Dentro Claude Code:

```
/plugin marketplace add morellid/skill-per-ingegneri
/plugin install <area-id>@skill-per-ingegneri
```

Dove `<area-id>` e' uno tra: `sicurezza-lavoro-cantieri`, `strutture-geotecnica`, `edilizia-urbanistica-catasto`, `appalti-opere-pubbliche`, `energia-incentivi`, `ambiente-territorio-mobilita`, `impianti-macchine-prodotti`, `software-dati-cybersecurity`. Le skill installate sono namespacciate (es. `/strutture-geotecnica:spettro-risposta-ntc`).

In alternativa, da terminale via il CLI [`vercel-labs/skills`](https://github.com/vercel-labs/skills):

```bash
npx skills@latest add morellid/skill-per-ingegneri
```

Il manifest e' in `.claude-plugin/marketplace.json`, **rigenerato automaticamente** da `scripts/build_catalog.py`.

### Installazione drag-and-drop su Claude.ai

Ogni skill e' distribuita anche come `.zip` autonomo nelle [GitHub Releases](https://github.com/morellid/skill-per-ingegneri/releases). Utile se usi Claude solo via web (claude.ai) e non hai installato Claude Code.

1. Apri l'ultima release: https://github.com/morellid/skill-per-ingegneri/releases/latest
2. Scarica il file `<skill-id>.zip` della skill che ti interessa (es. `pos-allegato-xv-checker.zip`).
3. Vai su https://claude.ai/customize/skills e fai upload (o drag-and-drop) del file `.zip`.

Lo zip contiene la skill completa (`SKILL.md`, `tasks/`, `examples/`, `references/`, `LICENSE`) in una singola directory top-level. Non serve estrarlo prima dell'upload.

### Codex `$skill-installer`

Da una sessione Codex (per skill singole):

```
$skill-installer https://github.com/<user>/skill-per-ingegneri/skills/pos-allegato-xv-checker
```

### Uso

Riavvia il tuo agent dopo l'installazione. Poi fai una domanda nel dominio della skill:

> "Verifica questo POS rispetto all'Allegato XV..."
>
> "Aiutami a redigere un DVR per un'azienda di 30 dipendenti"
>
> "Serve una DPIA per il nostro nuovo sistema di scoring clienti?"

L'agent caricara' la skill appropriata. In Codex puoi anche invocare esplicitamente: `/skills <nome-skill>`.

### Uso da altri agent (Cursor, Windsurf, GitHub Copilot, Devin, Amp, ...)

Per agent che leggono lo standard aperto [AGENTS.md](https://agents.md/), referenzia questo repo come submodule e aggiungi un puntatore al tuo progetto. Vedi [`AGENTS.md`](AGENTS.md) per i dettagli e le convenzioni.

Istruzioni dettagliate per ogni singola skill nel rispettivo `README.md` dentro `skills/<nome>/`.

## Come contribuire

Vedi [CONTRIBUTING.md](CONTRIBUTING.md). In sintesi:
- Solo fonti normative ufficiali (niente interpretazioni personali senza riferimento)
- Validazione da parte di un ingegnere di dominio prima del release
- Disclaimer di responsabilita' professionale obbligatorio in ogni skill
- Semver per skill, CHANGELOG aggiornato

## Principi

1. **Supporto, non sostituto**. Ogni skill emette output che richiede verifica e firma del professionista. Nessuna skill produce documenti auto-firmati o pronti al deposito senza revisione umana.
2. **Tracciabilita' delle fonti**. Ogni affermazione normativa e' riconducibile a un documento identificato da hash e data di consultazione (vedi `sources.yaml`).
3. **Lingua italiana**. Gli adempimenti sono italiani: istruzioni, output e riferimenti normativi sono in italiano. Struttura del codice e metadata in inglese per compatibilita' internazionale.
4. **Progressive disclosure**. Ogni skill e' monolitica ma carica solo i dettagli che servono per la specifica sotto-attivita' richiesta dall'utente.

## Autore

Davide Morelli <morelli.davide@gmail.com>

## Licenza

MIT. Vedi [LICENSE](LICENSE).

## Avvertenza

Le skill in questo repository sono strumenti di supporto e non sostituiscono il giudizio professionale. L'utilizzo improprio o non verificato degli output e' responsabilita' esclusiva dell'utente.
