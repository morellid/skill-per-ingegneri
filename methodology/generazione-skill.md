# Processo di generazione di una skill

Workflow standard per portare una skill da proposta a release v0.1.

## Step 0 - Pre-requisiti

- Task approvato secondo [`criteri-selezione.md`](criteri-selezione.md)
- Disponibili fonti normative ufficiali consultabili
- Autore e' competente nel dominio o lavora con un validatore di dominio

## Step 1 - Mapping delle fonti

Prima di scrivere riga di skill, elencare **tutte** le fonti normative pertinenti:

- Leggi, decreti, decreti legislativi applicabili
- Allegati tecnici
- Linee guida ministeriali o di enti (INAIL, CNI, ANAC)
- Circolari esplicative
- Norme UNI/CEI di riferimento (anche se non embedabili)
- Giurisprudenza rilevante se applicabile

Output: prima bozza di `references/sources.yaml` con tutti gli ID, URL, date, hash (anche se estratti non ancora preparati).

## Step 2 - Download e archiviazione fonti

Per ogni fonte pubblica:
1. Scaricare il PDF/documento
2. Calcolare SHA256: `sha256sum documento.pdf`
3. Registrare in `sources.yaml`: url, accessed, sha256, `binary_path: not_in_repo/<id>.pdf`, licenza
4. Archiviare il binario in `not_in_repo/` locale (mai committato)

Per fonti a licenza proprietaria (UNI, etc.):
1. Registrare in `sources.yaml` con `license: proprietary-paid` e `binary_path: null`, `md_path: null`
2. Nessun embed testuale
3. La skill usa riferimenti strutturali ("vedi UNI 11414:2023 par. 5.2") ma non riproduce il testo
4. **In ogni caso almeno una fonte pubblica e scaricabile deve esistere**: una skill basata solo su norme a pagamento non e' source-grounded ai sensi della Regola zero (vedi `AGENTS.md`)

## Step 2.5 - Conversione in markdown delle fonti (gating step)

**Questo e' lo step gating della Regola zero.** Senza questo passo NON si scrive **nessun token** di SKILL.md, AGENTS.md, tasks, examples, o codice di calcolo.

Per ogni fonte pubblica scaricata:

1. Apri il PDF e leggi i paragrafi/articoli rilevanti per la skill.
2. Crea `skills/<nome-skill>/references/fonti/<id>.md` (committato nel repo) con la transcrizione fedele:
   - se il PDF e' breve (es. una circolare di 10 pagine): transcrivi il testo integrale dei paragrafi citati
   - se il PDF e' lungo (es. NTC 2018, 200+ pagine): transcrivi solo i capitoli/articoli direttamente referenziati dalla skill, etichettando chiaramente quali sezioni sono incluse e quali omesse
3. Il MD include un header con:
   - id della fonte (matching `sources.yaml`)
   - sha256 del binario sorgente
   - versione/edizione del PDF
   - data di transcrizione
   - lista esplicita dei paragrafi/articoli inclusi (e quelli volutamente esclusi)
4. La transcrizione deve essere **fedele**: stessi numeri, stesse formule, stesse citazioni. Eventuali OCR errors vanno corretti contro il PDF originale, non lasciati. Non parafrasare in questo step (per le parafrasi c'e' `references/estratti/`).
5. Per testi a pagamento (proprietary-paid): il MD non si scrive. La skill usa solo rinvii strutturali.
6. Aggiorna `sources.yaml` aggiungendo per ogni fonte pubblica `md_path: references/fonti/<id>.md`.

**Perche' questo step esiste**: e' la prova non falsificabile che qualcuno ha letto la fonte. Un agent che attinge dai training data senza leggere il PDF non puo' produrre un MD plausibile (non sa quali paragrafi sono incrociati, quali numeri di pagina sono effettivi, quali errata corrige sono stati pubblicati). Lo step rende impossibile lo shortcut "scrivo la skill da memoria e committo placeholder".

**Cosa NON e' Step 2.5**:
- Non e' "incolla un riassunto autogenerato dell'agent"
- Non e' "trovo un documento simile su un altro sito e lo copio"
- Non e' "uso una versione del PDF diversa da quella hashed in `sources.yaml`"
- Non e' opzionale, non e' rinviabile, non e' "lo facciamo in v0.2"

## Step 2.6 - Estratti curati (parafrasi mirate)

Solo dopo lo Step 2.5, prepara gli `references/estratti/<id>.md`:

1. Sono parafrasi mirate dei paragrafi specifici di `references/fonti/<id>.md` che la skill cita.
2. Citano esplicitamente la sezione del MD di fonte (es. "vedi `references/fonti/ntc-2018.md` par. 3.2.3.2.1").
3. Sono tipicamente piu' brevi e contestualizzati per il task della skill, ma ogni numero/coefficiente deve essere rintracciabile in `fonti/`.
4. Se non c'e' un MD di fonte alle spalle, **l'estratto non si scrive**.

## Step 3 - Scaffold skill

```bash
./scripts/new-skill.sh nome-skill
```

Questo copia `templates/skill-template/` in `skills/nome-skill/` con placeholder sostituiti.

## Step 4 - SKILL.md (punto d'ingresso)

Scrivere il frontmatter YAML con `name` e `description`. La `description` deve essere precisa su:
- Cosa fa la skill
- Quando usarla
- Target utente
- Sotto-attivita' disponibili

Corpo del SKILL.md: leggero. Deve fare **progressive disclosure** - contenere il routing verso i task specifici, non le istruzioni dettagliate.

## Step 5 - Task files

Per ogni sotto-attivita', un file in `tasks/`:
- `check-*.md` per verifiche
- `draft-*.md` per generazione contenuto
- `valida-*.md` per validazioni strutturate

Ogni task file contiene:
- **Obiettivo**: cosa produce il task
- **Input richiesti**: cosa deve fornire l'utente
- **Fonti**: rinvii a `references/estratti/`
- **Procedura**: step-by-step
- **Output**: formato atteso
- **Limiti**: cosa il task NON fa, rinvio al professionista firmatario

## Step 6 - Esempi

In `examples/`:
- Almeno un caso conforme (output "tutto ok")
- Almeno un caso problematico (output evidenzia problemi)
- Opzionalmente: caso borderline / ambiguo

Ogni esempio ha struttura:
```
examples/caso-nome/
├── input.md         # dati di input
├── expected-output.md   # output atteso
└── note.md          # commenti di dominio
```

## Step 7 - Disclaimer

Ogni skill include obbligatoriamente:

> **Avvertenza**: questa skill e' uno strumento di supporto alla redazione/verifica di documenti tecnici. Non sostituisce il giudizio del professionista firmatario. L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill non produce documenti pronti al deposito o alla firma.

## Step 8 - Validazione

Segue [`validazione.md`](validazione.md). Non si pubblica v0.1 senza passarla.

## Step 9 - Release v0.1

- Tag git: `<skill-name>/v0.1.0`
- CHANGELOG.md aggiornato
- PR chiusa, main aggiornato
- README di skill completo

### Verifica compatibilita' dual-agent (obbligatoria)

Prima del tag finale, verificare che la skill sia installabile e funzionante su entrambi gli agent:

```bash
# Test Claude Code
ln -sfn "$(pwd)/skills/<nome-skill>" "$HOME/.claude/skills/<nome-skill>"
# Avviare Claude Code, verificare che la skill sia rilevata e i task funzionino

# Test Codex
ln -sfn "$(pwd)/skills/<nome-skill>" "$HOME/.agents/skills/<nome-skill>"
# Avviare Codex, verificare che la skill appaia nel picker (display_name da agents/openai.yaml)
# Eseguire /skills <nome-skill> e provare il default_prompt
```

Se la skill funziona su uno ma non sull'altro, identificare la differenza (frontmatter incompleto, cartella agents/ mancante, link interni rotti) e correggere prima del release.

## Step 10 - Monitoring post-release

- Issue GitHub aperte per feedback utenti
- Iscrizione alle notifiche di modifica normativa (vedi [`update-cycle.md`](update-cycle.md))
- Review trimestrale minimo
