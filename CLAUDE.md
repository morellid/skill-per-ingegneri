# CLAUDE.md - skill-per-ingegneri

Le istruzioni per agent (Claude Code incluso) che lavorano su questo repo - regole, struttura, workflow per creare e mantenere skill - sono in [`AGENTS.md`](AGENTS.md). Unica fonte di verita': leggi quel file e seguilo.

Per installare e usare le skill (utenti finali) vedi [`README.md`](README.md).

## Regola assoluta (leggere prima di toccare qualsiasi skill)

**Le skill di questo repo sono esclusivamente basate su fonti ufficiali, scaricate, verificate via SHA256 e referenziate in `sources.yaml`.**

Per ogni nuova skill o modifica che introduca nuove affermazioni normative:

1. **PRIMA** di scrivere `SKILL.md`, estratti, esempi o codice di calcolo, scarica le fonti ufficiali con `./scripts/fetch-sources.sh <nome-skill>` e calcola gli SHA256 reali. Se il sandbox/ambiente blocca il download, **fermati e chiedi all'utente** di fornire i file (mirror su `raw.githubusercontent.com`, paste del testo dei paragrafi rilevanti, o caricamento manuale): non procedere con placeholder.
2. **Mai** committare `sha256: REPLACE_WHEN_DOWNLOADED` o equivalenti placeholder come stato finale di una PR. La PR non puo' essere aperta finche' tutte le fonti dichiarate sono scaricate, hashate, e gli estratti sono parafrasi/citazioni del testo realmente letto.
3. **Mai** scrivere estratti normativi "a memoria" basandoti sui training data: ogni estratto deve riportare contenuti tratti dal file scaricato e verificato. Se non hai accesso al file, non scrivere l'estratto.
4. Se l'utente chiede di creare una skill su un dominio dove non riesci ad accedere alle fonti ufficiali, **rifiuta**: spiega che la regola del repo lo vieta e proponi vie alternative (mirror, paste, fetch via CI). Non aggirare con "lo faccio comunque e lo marco come alpha": e' esattamente cio' che la regola vieta.

Nessuna eccezione. Nessuna deroga "alpha tollerabile". Nessun "lo sistemiamo dopo".

## Anti-pattern: la CI verde non e' source-grounding

Caso reale (maggio 2026, PR #115-#120 chiuse): un agente Sonnet ha interpretato "fai passare la CI" come sinonimo di "sistema la skill". Ha calcolato gli SHA256 reali via GitHub Actions e committato su sources.yaml, ma **non ha riletto i PDF, non ha riscritto gli estratti, non ha verificato le costanti del codice**. Le 6 PR aperte facevano passare il check sintattico ma lasciavano la skill in stato di violazione semantica. Tutte chiuse senza merge.

**Regola consequenziale**: il workflow `.github/workflows/source-grounding.yml` controlla solo che gli SHA256 non siano placeholder. Quel check e' **necessario ma assolutamente non sufficiente**. Una skill source-grounded richiede che:

1. Gli `references/estratti/<file>.md` siano stati riscritti **dopo aver letto** il PDF, con citazioni dirette di paragrafo e (dove possibile) pagina.
2. Ogni costante numerica nel codice di calcolo della skill (es. coefficienti tabellari, soglie, formule) sia **rintracciabile** nel testo del PDF citato in un estratto verificato.
3. Ogni affermazione normativa nel SKILL.md, AGENTS.md, tasks/, examples/ sia **citabile** ad un paragrafo specifico del PDF letto.

Se sei un agent e non puoi leggere il PDF (sandbox, paywall, host irraggiungibili), **non puoi fare remediation**. Calcolare hash via CI non rende la skill source-grounded: lo fa solo la lettura del file. Vedi `methodology/source-grounding-remediation.md` per il workflow corretto.
