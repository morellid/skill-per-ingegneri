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
    │   ├── sources.yaml       # catalogo fonti (URL, accessed, sha256, md_path, licenza)
    │   ├── fonti/             # MD delle fonti ufficiali (transcrizione/conversione del PDF), committato
    │   └── estratti/          # estratti curati (parafrasi mirate dei fonti/, citate nei tasks)
    ├── examples/              # >=1 caso conforme + >=1 caso problematico
    ├── AGENTS.md              # convenzioni di dominio della skill
    ├── README.md              # doc utente della skill
    └── CHANGELOG.md           # semver per skill
```

## Regola zero: source-grounding obbligatorio (STOP rule)

**Le skill di questo repo sono ESCLUSIVAMENTE basate su fonti ufficiali, scaricate, verificate via SHA256, convertite in markdown committato nella skill (`references/fonti/<id>.md`), e referenziate in `references/sources.yaml`. Senza fonti scaricate E convertite a MD non si crea, non si modifica, non si estende una skill. Non c'e' margine di deroga.**

### Workflow obbligato (4 step in ordine, sequenziali, non saltabili)

```
1. SCARICARE le fonti ufficiali (PDF/HTML)        -> not_in_repo/<id>.pdf
2. SALVARE l'hash SHA256                          -> references/sources.yaml (campo sha256)
3. CONVERTIRE il PDF in markdown                  -> references/fonti/<id>.md (COMMITTATO)
4. USARE il markdown della fonte per la skill     -> SKILL.md, tasks/, examples/, codice
```

**Step 3 e' lo step gating della Regola zero.** Il file `references/fonti/<id>.md` e' la transcrizione (o conversione fedele) del PDF nei suoi paragrafi rilevanti. Va committato nel repo. E' la prova non falsificabile che qualcuno ha letto la fonte: qualunque agent che genera skill content senza un MD di fonte alle spalle sta inevitabilmente attingendo dai training data, non dalla fonte.

**Non si scrive neanche un token di SKILL.md, AGENTS.md (di skill), tasks/, examples/, o codice di calcolo prima che `references/fonti/<id>.md` esista, generato dalla lettura del PDF scaricato.** Questo include i placeholder, i TODO, le bozze: niente di niente.

### Vincoli operativi

- **Prima** di scrivere qualunque contenuto della skill, esegui i 4 step sopra in ordine. Per lo step 1: `./scripts/fetch-sources.sh <nome-skill>`. Per lo step 3: leggi il PDF e produci `references/fonti/<id>.md` con la transcrizione dei paragrafi rilevanti (vedi `methodology/generazione-skill.md` Step 2.5).
- **Mai** scrivere `references/estratti/<file>.md` "a memoria" sulla base dei training data. Gli estratti sono parafrasi mirate di contenuto presente in `references/fonti/<id>.md`. Se il MD della fonte non c'e', l'estratto non si scrive.
- **Mai** aprire una PR con `sha256: REPLACE_WHEN_DOWNLOADED` o equivalenti placeholder, ne' con `references/fonti/<id>.md` mancante per fonti dichiarate non-paywall.
- **Mai** committare un `references/fonti/<id>.md` vuoto, segnaposto, o con testo "TBD/TODO". Se la fonte non e' stata letta, il file non esiste e la skill non si scrive.
- **Mai** marcare il vincolo come "gap pre-v1.0 tollerabile in alpha": lo stato `0.1.0-alpha` riguarda assenza di Livello 2 / casi reali / validazione di campo, NON assenza di fonti scaricate, hashate, e convertite a MD. Sono prerequisito di qualsiasi versione, alpha inclusa.

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
3. **Step 1 - SCARICA le fonti**. Predisponi `sources.yaml` con URL, `accessed`, `binary_path` (in `not_in_repo/`), licenza. Esegui `./scripts/fetch-sources.sh <nome-skill>`. Se anche **una sola** fonte non e' scaricabile, **fermati**: applica il protocollo di rifiuto della Regola zero.
4. **Step 2 - SALVA l'hash SHA256**. Per ogni fonte scaricata calcola e committa lo `sha256:` reale nel `sources.yaml`. Sostituisci ogni placeholder `REPLACE_WHEN_DOWNLOADED`.
5. **Step 3 - CONVERTI il PDF in markdown** in `references/fonti/<id>.md`, committato. Il MD deve essere una transcrizione fedele dei paragrafi rilevanti del PDF (non tutto il PDF se troppo lungo; ma tutto cio' che la skill cita). Vedi `methodology/generazione-skill.md` Step 2.5 per le convenzioni.
6. **Step 4 - USA il markdown per la skill**. Solo ora apri `SKILL.md` e cominci a scrivere. Ogni affermazione normativa deve poter citare un punto specifico in `references/fonti/<id>.md`. Gli `references/estratti/*.md` sono parafrasi mirate di parti di `fonti/`. Vedi `methodology/generazione-skill.md` per il resto del workflow (scaffold, tasks, esempi, disclaimer, validazione).
7. Scaffold tecnico: `./scripts/new-skill.sh <nome-skill>` (kebab-case). Da eseguire dopo lo Step 4 inizia.
8. Versione iniziale: `0.1.0-alpha`. Lo stato alpha riguarda solo l'assenza di validazione Livello 2 (vs casi reali / esperti di dominio): le fonti **devono comunque** essere scaricate, hashate e convertite a MD prima di scrivere la skill.
9. Validazione obbligatoria prima del rilascio: `methodology/validazione.md` (almeno Livello 1, Livello 2 da ingegnere di dominio diverso dall'autore prima di v1.0).
10. **Aggiorna `README.md` di root**: aggiungi una riga alla tabella "Skill disponibili" con `[`<nome-skill>`](skills/<nome-skill>/) | descrizione 1-2 frasi | riferimenti normativi`. La tabella di root e' la fonte di verita' dell'elenco pubblicato: una PR di nuova skill che non la aggiorna e' incompleta.

## Quando modifichi una skill esistente

- Bug fix -> patch (`0.1.0 -> 0.1.1`).
- Miglioramento compatibile -> minor (`0.1.0 -> 0.2.0`).
- Breaking change o major update normativo -> major (`0.x.y -> 1.0.0`).
- Aggiorna sempre `skills/<skill>/CHANGELOG.md` (Keep a Changelog).
- Se cambia una norma: aggiorna `sources.yaml` (URL, `accessed`, `sha256`), gli `estratti/` se servono, e cita il trigger normativo nel changelog. Vedi `methodology/update-cycle.md`.
- Se la modifica cambia descrizione, scope o riferimenti normativi della skill in modo visibile all'utente finale: aggiorna anche la riga della skill nella tabella "Skill disponibili" di `README.md` di root.
- Tocca solo cio' che serve: non ristrutturare skill adiacenti, non riformattare codice non tuo.

## Quando rimuovi o deprechi una skill

- Segui il flusso di deprecation di `methodology/update-cycle.md`.
- Rimuovi la riga corrispondente dalla tabella "Skill disponibili" del `README.md` di root (oppure marca la skill come deprecata con link alla sostitutiva, se esiste). README di root e elenco effettivo di `skills/` non devono mai divergere.

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
- Non aprire/mergere una PR che aggiunge, rinomina, rimuove o deprecca una skill senza aggiornare la tabella "Skill disponibili" del `README.md` di root: e' la fonte di verita' del catalogo pubblicato.

## Disclaimer

Le skill in questo repository sono strumenti di supporto e non sostituiscono il giudizio professionale di ingegneri, RSPP, DPO, CSE/CSP, o altri professionisti firmatari. L'utilizzo improprio o non verificato degli output e' responsabilita' esclusiva dell'utente.
