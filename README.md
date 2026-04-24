# skill-per-ingegneri

Repository collettivo di skill AI per la pratica dell'ingegneria italiana.

## Cosa contiene

Skill AI in formato [Anthropic skill-creator](https://docs.anthropic.com/), scritte in italiano, basate esclusivamente su fonti normative ufficiali (D.Lgs., decreti attuativi, linee guida pubbliche). Ogni skill e' pensata per essere usata da ingegneri iscritti all'Albo come supporto - non sostituto - nella redazione e verifica di documenti tecnici e adempimenti.

Contiene anche:
- **Metodologia replicabile** per generare nuove skill (`methodology/`)
- **Template e script** per scaffolding e validazione (`templates/`, `scripts/`)
- **Riferimenti bibliografici** strutturati con hash delle fonti (`sources.yaml` per ogni skill)

## Struttura

```
skill-per-ingegneri/
├── skills/                      # le skill pubblicate
│   └── pos-allegato-xv-checker/
│       ├── SKILL.md             # punto d'ingresso + routing (progressive disclosure)
│       ├── tasks/               # istruzioni dettagliate per sotto-attivita'
│       ├── references/          # metadata fonti + estratti normativi
│       ├── examples/            # casi d'uso validi e problematici
│       └── CHANGELOG.md
├── methodology/                 # come si genera e mantiene una skill
├── templates/                   # scaffold per nuove skill
└── scripts/                     # utility CLI
```

## Come usare le skill

Le skill sono pensate per girare in [Claude Code](https://claude.com/claude-code) o via Claude Agent SDK. Per installarle localmente in Claude Code:

```bash
# da definire una volta stabilizzato lo schema di installazione
```

Istruzioni dettagliate per ogni skill nel rispettivo `README.md`.

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

## Licenza

MIT. Vedi [LICENSE](LICENSE).

## Avvertenza

Le skill in questo repository sono strumenti di supporto e non sostituiscono il giudizio professionale. L'utilizzo improprio o non verificato degli output e' responsabilita' esclusiva dell'utente.
