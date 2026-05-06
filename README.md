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
| [`pos-allegato-xv-checker`](skills/pos-allegato-xv-checker/) | Guida la compilazione assistita e verifica completezza e coerenza di un Piano Operativo di Sicurezza (POS) di cantiere | D.Lgs. 81/2008 art. 96-97, Allegato XV + DI 9/9/2014 modelli semplificati |
| [`dvr-generico`](skills/dvr-generico/) | Stesura, verifica e aggiornamento del Documento di Valutazione dei Rischi (DVR) cross-settoriale | D.Lgs. 81/2008 art. 17, 28, 29 |
| [`gdpr-registro-dpia`](skills/gdpr-registro-dpia/) | Registro delle attivita' di trattamento e Valutazione d'Impatto (DPIA) | GDPR art. 30, 35, 36 + provv. Garante |
| [`nis2-self-assessment`](skills/nis2-self-assessment/) | Self-assessment NIS2 (perimetro, gap analysis misure ACN, notifica incidenti, governance) | D.Lgs. 138/2024 + Det. ACN 379907/2025 |
| [`ai-act-compliance`](skills/ai-act-compliance/) | Classificazione sistemi AI + obblighi provider/deployer/GPAI/trasparenza | Reg. UE 2024/1689 (AI Act) |
| [`spettro-risposta-ntc`](skills/spettro-risposta-ntc/) | Calcolo code-driven dello spettro di risposta elastico orizzontale (TR, ag/F0/Tc*, S, eta, TB/TC/TD, Se(T)) per SLO/SLD/SLV/SLC | NTC 2018 par. 3.2 + Circ. 7/2019 |
| [`combinazioni-carico-ntc`](skills/combinazioni-carico-ntc/) | Generazione/verifica code-driven delle combinazioni delle azioni SLU/SLE/sismiche/eccezionali per edifici civili e industriali correnti | NTC 2018 par. 2.5.3 + Tab. 2.5.I + Tab. 2.6.I |
| [`pfte-allegato-i7-checker`](skills/pfte-allegato-i7-checker/) | Checklist e verifica completezza degli elaborati di un PFTE / progetto esecutivo di lavori pubblici, integrato dal correttivo 2024 | D.Lgs. 36/2023 art. 41 + Allegato I.7 + D.Lgs. 209/2024 |
| [`modulistica-edilizia-unificata`](skills/modulistica-edilizia-unificata/) | Determina il modulo edilizio unificato (Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / PdC / Sanatoria art. 36 / 36-bis) per un intervento e l'elenco degli allegati richiesti, integrato con le modifiche del Salva Casa | DPR 380/2001 + D.Lgs. 222/2016 Tabella A + DL 69/2024 conv. L. 105/2024 + Modulistica unificata 27/3/2025 |
| [`transizione-5-0-asseverazione`](skills/transizione-5-0-asseverazione/) | Asseverazione tecnica ex ante / ex post per il credito d'imposta Piano Transizione 5.0 (calcolo riduzione consumi >=3% struttura o >=5% processo, conversione tep, modelli MIMIT) | DL 19/2024 art. 38 + DM MIMIT-MEF 24/7/2024 + Circolare MIMIT 25877/2024 |
| [`dnsh-pnrr-checker`](skills/dnsh-pnrr-checker/) | Verifica documentale DNSH per interventi PNRR e, solo se la misura lo richiama espressamente, per interventi PNC: mappatura misura, schede tecniche RGS, checklist ex ante/ex post, piano evidenze e report per gara/SAL/collaudo/ReGiS | Reg. UE 2020/852 art. 17 + Reg. UE 2021/241 art. 5 e 18 + Circolare RGS 22/2024 + Guida operativa DNSH RGS 2024 + DL 77/2021 art. 14 |
| [`piano-lavoro-amianto`](skills/piano-lavoro-amianto/) | Precheck, redazione guidata e verifica del piano di lavoro per demolizione o rimozione di amianto, nel testo vigente dell'art. 256 D.Lgs. 81/2008 aggiornato dal D.Lgs. 213/2025 | D.Lgs. 81/2008 art. 251, 256, 258, 259 + D.Lgs. 213/2025 + DM 6/9/1994 |
| [`catasto-pregeo-docfa-atti-telematici`](skills/catasto-pregeo-docfa-atti-telematici/) | Assistente alla redazione e al check pre-trasmissione degli atti telematici di aggiornamento del Catasto Terreni (Pregeo 10) e del Catasto Fabbricati (Docfa 4): scelta tipologia atto Pregeo (TM/FR/FM/SC/TP), causale e categoria Docfa, EP/ES/ET/Quadro D, deposito telematico frazionamenti dal 1/7/2025, diagnosi rifiuti telematici via Sister | DPR 380/2001 art. 30 + DM 28/1998 + Circ. AdE 3/2009 + Vademecum Docfa v1.0 (7/2022) + Risoluzione AdE 40/E del 9/6/2025 |
| [`pratiche-edilizie-lr65-2014-toscana`](skills/pratiche-edilizie-lr65-2014-toscana/) | Determina il titolo abilitativo edilizio (Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / PdC) per interventi in Toscana e genera la checklist documenti richiesti, con specificita' regionali (sismica DGRT 421/2014, DPGR 1/R/2022 Genio Civile, vincolo paesaggistico, Piano Operativo) | LR Toscana 65/2014 + DPR 380/2001 + DPGR 1/R/2022 + DPR 31/2017 (paesaggio) |
| [`cer-cacer-configurazione-gse`](skills/cer-cacer-configurazione-gse/) | Configurazione di CER (art. 31), GAC (art. 30 c. 2) o AID (art. 30 c. 1 lett. a) n. 2) con verifica perimetro cabina primaria, redazione guidata dello statuto, simulazione semplificata di energia condivisa, TIP, tariffa di restituzione e contributo PNRR per Comuni < 50.000 ab. (regime vigente post DM 127/2025 + DL 19/2026 art. 27), e checklist documentale per la qualifica al portale GSE | D.Lgs. 199/2021 artt. 30-31-32 + DM MASE 7/12/2023 n. 414 + DM MASE 16/5/2025 n. 127 + DL 19/2/2026 n. 19 art. 27 + Delibera ARERA 727/2022/R/eel (TIAD) + Regole Operative CACER del GSE |

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
│   ├── combinazioni-carico-ntc/
│   ├── pfte-allegato-i7-checker/
│   ├── modulistica-edilizia-unificata/
│   ├── transizione-5-0-asseverazione/
│   ├── dnsh-pnrr-checker/
│   ├── catasto-pregeo-docfa-atti-telematici/
│   ├── pratiche-edilizie-lr65-2014-toscana/
│   └── cer-cacer-configurazione-gse/
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
