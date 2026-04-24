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
3. Registrare in `sources.yaml`: url, accessed, sha256
4. Archiviare il binario in `not_in_repo/` locale (mai committato)
5. Se pubblico dominio: preparare estratto testuale pertinente in `references/estratti/<id>.md` con citazione strutturata (articolo, comma, data di consultazione)

Per fonti a licenza proprietaria (UNI, etc.):
1. Registrare in `sources.yaml` con `license: proprietary-paid` e `binary_path: null`
2. Nessun embed testuale
3. La skill usa riferimenti strutturali ("vedi UNI 11414:2023 par. 5.2") ma non riproduce il testo

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

## Step 10 - Monitoring post-release

- Issue GitHub aperte per feedback utenti
- Iscrizione alle notifiche di modifica normativa (vedi [`update-cycle.md`](update-cycle.md))
- Review trimestrale minimo
