# skill-per-ingegneri

Repository collettivo di skill AI per la pratica dell'ingegneria italiana.

## Cosa contiene

Skill AI in formato dual-agent (compatibili sia con [Anthropic Claude Code](https://claude.com/claude-code) sia con [OpenAI Codex](https://developers.openai.com/codex)), scritte in italiano, basate esclusivamente su fonti normative ufficiali (D.Lgs., decreti attuativi, linee guida pubbliche). Ogni skill e' pensata per essere usata da ingegneri iscritti all'Albo come supporto - non sostituto - nella redazione e verifica di documenti tecnici e adempimenti.

Ogni skill e' anche utilizzabile da agent che leggono lo standard aperto [`AGENTS.md`](AGENTS.md) (Codex, Cursor, Windsurf, GitHub Copilot, Devin, Amp, Antigravity, ...).

Contiene anche:
- **Metodologia replicabile** per generare nuove skill (`methodology/`)
- **Template e script** per scaffolding e validazione (`templates/`, `scripts/`)
- **Riferimenti bibliografici** strutturati con hash delle fonti (`sources.yaml` per ogni skill)

## Skill disponibili

| Skill | Ambito | Riferimenti normativi |
|---|---|---|
| [`pos-allegato-xv-checker`](skills/pos-allegato-xv-checker/) | Verifica completezza e coerenza di un Piano Operativo di Sicurezza (POS) di cantiere | D.Lgs. 81/2008 art. 96-97, Allegato XV |
| [`dvr-generico`](skills/dvr-generico/) | Stesura, verifica e aggiornamento del Documento di Valutazione dei Rischi (DVR) cross-settoriale | D.Lgs. 81/2008 art. 17, 28, 29 |
| [`gdpr-registro-dpia`](skills/gdpr-registro-dpia/) | Registro delle attivita' di trattamento e Valutazione d'Impatto (DPIA) | GDPR art. 30, 35, 36 + provv. Garante |
| [`nis2-self-assessment`](skills/nis2-self-assessment/) | Self-assessment NIS2 (perimetro, gap analysis misure ACN, notifica incidenti, governance) | D.Lgs. 138/2024 + Det. ACN 379907/2025 |
| [`ai-act-compliance`](skills/ai-act-compliance/) | Classificazione sistemi AI + obblighi provider/deployer/GPAI/trasparenza | Reg. UE 2024/1689 (AI Act) |
| [`spettro-risposta-ntc`](skills/spettro-risposta-ntc/) | Calcolo code-driven dello spettro di risposta elastico orizzontale (TR, ag/F0/Tc*, S, eta, TB/TC/TD, Se(T)) per SLO/SLD/SLV/SLC | NTC 2018 par. 3.2 + Circ. 7/2019 |
| [`pfte-allegato-i7-checker`](skills/pfte-allegato-i7-checker/) | Checklist e verifica completezza degli elaborati di un PFTE / progetto esecutivo di lavori pubblici, integrato dal correttivo 2024 | D.Lgs. 36/2023 art. 41 + Allegato I.7 + D.Lgs. 209/2024 |
| [`modulistica-edilizia-unificata`](skills/modulistica-edilizia-unificata/) | Determina il modulo edilizio unificato (Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / PdC / Sanatoria art. 36 / 36-bis) per un intervento e l'elenco degli allegati richiesti, integrato con le modifiche del Salva Casa | DPR 380/2001 + D.Lgs. 222/2016 Tabella A + DL 69/2024 conv. L. 105/2024 + Modulistica unificata 27/3/2025 |

Ogni skill ha un proprio `README.md` con dettaglio target, sotto-attivita' e limiti noti.

## Struttura

```
skill-per-ingegneri/
├── AGENTS.md                    # guida cross-agent (Codex, Cursor, Copilot, ...)
├── skills/                      # le skill pubblicate
│   ├── pos-allegato-xv-checker/
│   │   ├── SKILL.md             # punto d'ingresso + routing (license: MIT in frontmatter)
│   │   ├── agents/
│   │   │   └── openai.yaml      # UI metadata per Codex
│   │   ├── tasks/               # istruzioni dettagliate per sotto-attivita'
│   │   ├── references/          # metadata fonti + estratti normativi
│   │   ├── examples/            # casi d'uso validi e problematici
│   │   └── CHANGELOG.md
│   ├── dvr-generico/
│   ├── gdpr-registro-dpia/
│   ├── nis2-self-assessment/
│   ├── ai-act-compliance/
│   ├── spettro-risposta-ntc/
│   ├── pfte-allegato-i7-checker/
│   └── modulistica-edilizia-unificata/
├── methodology/                 # come si genera e mantiene una skill
├── templates/                   # scaffold dual-agent per nuove skill
└── scripts/                     # utility CLI (new-skill, validate, fetch-sources)
```

## Come installare e usare le skill

Ogni skill in `skills/<nome>/` e' un pacchetto autonomo. Si installa nella directory skills del tuo agent.

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
