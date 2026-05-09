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

## Regola zero: source-grounding obbligatorio (STOP rule)

**Le skill di questo repo sono ESCLUSIVAMENTE basate su fonti ufficiali, scaricate, verificate via SHA256 e referenziate in `references/sources.yaml`. Senza fonti scaricate non si crea, non si modifica, non si estende una skill. Non c'e' margine di deroga.**

Operativamente:

- **Prima** di scrivere `SKILL.md`, `references/estratti/`, esempi o codice di calcolo, scarica le fonti dichiarate con `./scripts/fetch-sources.sh <nome-skill>` e calcola gli SHA256 reali. Sostituisci ogni placeholder `REPLACE_WHEN_DOWNLOADED` con l'hash effettivo.
- **Mai** scrivere `references/estratti/<file>.md` "a memoria" sulla base dei training data dell'agent. Ogni estratto deve riportare contenuti **letti dal file scaricato**. Se non hai letto il file, non scrivi l'estratto.
- **Mai** aprire una PR con `sha256: REPLACE_WHEN_DOWNLOADED` o equivalenti placeholder nei `sources.yaml`. La PR e' incompleta per definizione.
- **Mai** marcare il vincolo come "gap pre-v1.0 tollerabile in alpha": e' la regola che la nozione stessa di "alpha tollerabile" cerca di violare. Lo stato `0.1.0-alpha` riguarda assenza di Livello 2 / casi reali / validazione di campo, NON assenza di fonti scaricate. Le fonti scaricate sono prerequisito di qualsiasi versione, alpha inclusa.

### Protocollo di rifiuto (refusal protocol)

Se l'agent (umano o AI) **non puo' accedere** alle fonti ufficiali necessarie - per restrizioni di rete, paywall, allowlist sandbox, host irraggiungibili, paesi senza accesso al portale, ecc. - **deve rifiutare** di creare la skill e segnalarlo esplicitamente all'utente. Le vie alternative consentite sono:

1. l'utente fornisce un mirror accessibile (es. `raw.githubusercontent.com/<repo-privato>/...`) dei PDF/HTML ufficiali, e l'agent ne calcola SHA256;
2. l'utente carica i file in `not_in_repo/` e fornisce gli SHA256 calcolati localmente, e l'agent rinforza la conformita' in commit message + sources.yaml;
3. l'utente paste-incolla il testo dei paragrafi rilevanti dalla copia ufficiale, e l'agent scrive estratti citando esplicitamente il testo originale (commit message dichiara la provenance);
4. l'utente sposta il fetch a CI (es. GitHub Actions con rete libera) e l'agent appronta il workflow.

**Non sono consentite** le seguenti scorciatoie: scrivere estratti da memoria, citare URL senza scaricare, usare placeholder come stato finale, ipotizzare valori di tabelle non lette, parafrasare formule da training data senza verifica sul testo originale.

### Anti-pattern: la CI verde non e' source-grounding (lezione PR #115-#120)

Maggio 2026, caso reale chiuso senza merge. Un agente Sonnet a cui era stato chiesto "fai passare la CI" ha:

- calcolato gli SHA256 reali dei PDF tramite GitHub Actions (rete libera, a differenza del sandbox di sviluppo)
- committato i risultati nei `sources.yaml`, sostituendo i placeholder
- aperto 6 PR di "remediation" che facevano passare i check sintattici della CI

**Tutte e 6 le PR sono state chiuse senza merge** perche' il lavoro era una **violazione semantica**: gli `references/estratti/*.md` e le costanti numeriche dei moduli Python erano rimasti scritti dai training data dell'agent originario, **senza nessuna lettura del PDF**.

Lezione operativa per ogni agent:

- **Calcolare lo SHA256 di un PDF non rende source-grounded la skill che cita quel PDF.** L'hash conferma che il file esiste e non e' stato manomesso, non che il suo contenuto sia stato letto.
- **Far passare la CI non e' obiettivo, e' effetto collaterale.** L'obiettivo e' che ogni affermazione normativa nella skill sia tracciabile al testo del PDF realmente letto. Se un agent prende come prompt "fai passare la CI" e ottiene CI verde senza aver letto i PDF, sta producendo lavoro corrotto.
- **GitHub Actions puo' scaricare PDF, non puo' leggerli e parafrasarli.** Il fetch automatico e' uno strumento per la fase finale (calcolo hash dopo che la remediation semantica e' fatta), non un sostituto della remediation.
- **Refusal protocol applicato anche alla remediation**: se un agent e' richiesto di "sistemare le P1 source-grounding remediation issues" ma non ha modo di leggere i PDF (sandbox blocca host normativi, paywall, ecc.), **deve rifiutare** e segnalarlo, non delegare a CI il calcolo degli hash. Vedi `methodology/source-grounding-remediation.md` per il workflow corretto.

### Differenza fra "validazione sintattica" e "remediation semantica"

| Operazione | Tipo | Sufficiente per Regola zero? |
|---|---|---|
| `grep REPLACE_WHEN_DOWNLOADED sources.yaml` ritorna 0 righe | sintattica | NO |
| `validate.sh` passa | sintattica | NO |
| Workflow `source-grounding.yml` verde | sintattica | NO |
| Hash SHA256 dichiarato coincide con il binario scaricato | sintattica | NO |
| Estratti riscritti dopo lettura del PDF, con citazioni paragrafo+pagina | semantica | si' (necessario) |
| Costanti del codice di calcolo verificate contro il testo del PDF | semantica | si' (necessario) |
| Affermazioni nei tasks/examples cite paragrafi specifici del PDF | semantica | si' (necessario) |

Sintattica + semantica = Regola zero rispettata. Solo sintattica = violazione mascherata.

## Regole non negoziabili (applicano sempre)

1. **Source-grounded** (vedi Regola zero sopra). Ogni affermazione normativa DEVE essere riconducibile a una voce in `references/sources.yaml` (URL, `accessed`, `sha256` reale calcolato sul file scaricato, licenza). Senza fonte scaricata, niente affermazione, niente skill. Non si commettono PR con `sha256: REPLACE_WHEN_DOWNLOADED`.
2. **Niente fabbricazioni**. Se un fatto non e' in `references/estratti/` (a sua volta tratto dal file scaricato), non inventarlo: o scarichi la fonte e aggiorni `sources.yaml` con SHA256 reale (vedi `scripts/fetch-sources.sh`), o ti fermi e segnali la lacuna all'utente seguendo il protocollo di rifiuto. Mai usare i training data dell'agent come surrogato della fonte.
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
2. **Mapping fonti FIRST**. Identifica la lista esatta delle fonti ufficiali (decreti, regolamenti, circolari, linee guida pubbliche) necessarie alla skill. Verifica che siano scaricabili dal tuo ambiente.
3. **Scarica le fonti PRIMA di scrivere qualsiasi contenuto**. Predisponi `sources.yaml` con URL, `accessed`, `binary_path` (in `not_in_repo/`), licenza, e ESEGUI `./scripts/fetch-sources.sh <nome-skill>`. Calcola SHA256 reali e committali nel `sources.yaml`. Se anche **una sola** fonte non e' scaricabile, **fermati**: applica il protocollo di rifiuto della Regola zero. Non procedere con il resto della skill.
4. Solo dopo che tutte le fonti sono scaricate e hashate, segui il workflow completo in `methodology/generazione-skill.md` (scaffold -> SKILL.md -> estratti tratti dal file scaricato -> tasks -> esempi -> disclaimer -> validazione).
5. Scaffold: `./scripts/new-skill.sh <nome-skill>` (kebab-case).
6. Versione iniziale: `0.1.0-alpha`. Lo stato alpha riguarda solo l'assenza di validazione Livello 2 (vs casi reali / esperti di dominio): le fonti **devono comunque** essere scaricate e hashate.
7. Validazione obbligatoria prima del rilascio: `methodology/validazione.md` (almeno Livello 1, Livello 2 da ingegnere di dominio diverso dall'autore prima di v1.0).

## Quando modifichi una skill esistente

- Bug fix -> patch (`0.1.0 -> 0.1.1`).
- Miglioramento compatibile -> minor (`0.1.0 -> 0.2.0`).
- Breaking change o major update normativo -> major (`0.x.y -> 1.0.0`).
- Aggiorna sempre `skills/<skill>/CHANGELOG.md` (Keep a Changelog).
- Se cambia una norma: aggiorna `sources.yaml` (URL, `accessed`, `sha256`), gli `estratti/` se servono, e cita il trigger normativo nel changelog. Vedi `methodology/update-cycle.md`.
- Tocca solo cio' che serve: non ristrutturare skill adiacenti, non riformattare codice non tuo.

## Prima di committare

```bash
./scripts/fetch-sources.sh <nome-skill>     # PRIMA: scarica fonti, calcola SHA256, sostituisci ogni REPLACE_WHEN_DOWNLOADED
./scripts/validate.sh --all                 # check strutturale di tutto il catalogo
./scripts/validate.sh <nome-skill>          # check di una skill sola
grep -r "REPLACE_WHEN_DOWNLOADED" skills/<nome-skill>/   # DEVE non trovare nulla
```

**Nessuna PR puo' essere aperta** finche' `grep REPLACE_WHEN_DOWNLOADED` (o equivalenti `REPLACE_WITH_ACTUAL_HASH`, `PENDING_FETCH`, `sha256:` vuoti) su `references/sources.yaml` ritorna anche solo una riga. I binari scaricati finiscono in `not_in_repo/` (mai committati); sono referenziati via hash in `sources.yaml`. Gli estratti in `references/estratti/` devono riportare contenuti tratti dal file scaricato, mai da training data dell'agent.

### CI gate (GitHub Actions)

Il workflow `.github/workflows/source-grounding.yml` implementa il gate lato server:

- `check-no-placeholders`: rifiuta qualunque PR che contenga placeholder SHA256 nei `sources.yaml`. Bloccante.
- `validate-sources`: per ogni voce con `binary_path` non null e licenza libera, scarica il file dall'URL pubblico (la CI ha rete libera) e verifica che lo SHA256 dichiarato coincida con quello calcolato. Bloccante: hash mismatch o fonte non raggiungibile fa fallire la PR.
- `validate-script-runs`: esegue `scripts/validate.sh --all`.

Lo stesso check anti-placeholder e' baked in `scripts/validate.sh`, quindi `./scripts/validate.sh <skill>` localmente fallisce se ci sono placeholder.

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

- **Mai e poi mai** creare una skill senza fonti ufficiali scaricate, hashate e referenziate. La skill che non rispetta la Regola zero non esiste come skill di questo repo.
- **Mai e poi mai** committare PR con `sha256: REPLACE_WHEN_DOWNLOADED` o placeholder equivalenti. Il `sources.yaml` con placeholder e' uno stato intermedio durante lo scaffolding, non uno stato di rilascio.
- **Mai e poi mai** scrivere estratti normativi attingendo dai training data dell'agent. Solo dal file scaricato e verificato via SHA256.
- **Mai e poi mai** marcare l'assenza di fonti scaricate come "gap pre-v1.0 tollerabile in alpha": e' la regola che la nozione "alpha tollerabile" cerca di violare.
- Non aggirare il vincolo con compromessi creativi tipo "metto il PDF su un server temporaneo e citato senza commit del hash", "uso un riassunto di Wikipedia", "cito la legge da sentenza", "cito da slide del professore": tutte queste soluzioni violano la Regola zero.
- Non aggiungere skill che richiedono giudizio professionale non delegabile (es. calcoli strutturali a firma, certificazioni firmate).
- Non committare binari (PDF, DOCX) - vanno in `not_in_repo/`, referenziati via hash in `sources.yaml`.
- Non rimuovere il disclaimer di responsabilita' professionale.
- Non rompere il formato dual-agent: senza `license: MIT` nel frontmatter o senza `agents/openai.yaml` la skill e' incompleta.
- Non duplicare l'`AGENTS.md` di skill rispetto al `SKILL.md`: deve essere lean (~30-80 righe) e aggiungere convenzioni di dominio, non reinstaurare la skill.
- Non duplicare contenuto tra root `AGENTS.md`, `CLAUDE.md` e `README.md`. Una sola sorgente per ogni informazione.

## Disclaimer

Le skill in questo repository sono strumenti di supporto e non sostituiscono il giudizio professionale di ingegneri, RSPP, DPO, CSE/CSP, o altri professionisti firmatari. L'utilizzo improprio o non verificato degli output e' responsabilita' esclusiva dell'utente.
