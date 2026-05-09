# CLAUDE.md - skill-per-ingegneri

Le istruzioni per agent (Claude Code incluso) che lavorano su questo repo - regole, struttura, workflow per creare e mantenere skill - sono in [`AGENTS.md`](AGENTS.md). Unica fonte di verita': leggi quel file e seguilo.

Per installare e usare le skill (utenti finali) vedi [`README.md`](README.md).

## Regola assoluta (leggere prima di toccare qualsiasi skill)

**Le skill di questo repo sono esclusivamente basate su fonti ufficiali, scaricate, verificate via SHA256, convertite in markdown committato nella skill, e referenziate in `sources.yaml`.**

### Workflow obbligato (4 step in ordine)

```
1. SCARICARE le fonti (PDF/HTML ufficiale) -> not_in_repo/<id>.pdf
2. SALVARE l'hash SHA256 in references/sources.yaml
3. CONVERTIRE il PDF in markdown -> references/fonti/<id>.md (committato)
4. USARE il markdown della fonte per scrivere la skill
```

**Non si scrive neanche un token di SKILL.md, AGENTS.md, tasks/, examples/, o codice di calcolo prima che il file `references/fonti/<id>.md` esista nella skill, generato dalla lettura del PDF scaricato.** Il MD committato e' la prova non falsificabile che qualcuno ha letto la fonte: qualunque skill content scritto senza un MD di fonte alle spalle e' inevitabilmente fabbricazione di training data.

### Vincoli operativi

1. **PRIMA** di scrivere `SKILL.md`, estratti, esempi o codice di calcolo, esegui i 4 step sopra in ordine. Se il sandbox/ambiente blocca il download, **fermati e chiedi all'utente** di fornire i file (mirror su `raw.githubusercontent.com`, paste del testo, o caricamento manuale): non procedere con placeholder.
2. **Mai** committare `sha256: REPLACE_WHEN_DOWNLOADED` o equivalenti placeholder come stato finale di una PR.
3. **Mai** committare un `references/fonti/<id>.md` vuoto o con testo "TBD". Se la fonte non e' stata letta, il file non esiste.
4. **Mai** scrivere estratti normativi "a memoria" basandoti sui training data: ogni estratto deve essere parafrasi di contenuto presente in `references/fonti/<id>.md`. Se il MD della fonte non c'e', l'estratto non si scrive.
5. Se l'utente chiede di creare una skill su un dominio dove non riesci ad accedere alle fonti ufficiali, **rifiuta**: spiega che la regola del repo lo vieta. Non aggirare con "lo faccio comunque e lo marco come alpha", ne' con "lo facciamo dopo": e' esattamente cio' che la regola vieta.

Nessuna eccezione. Nessuna deroga "alpha tollerabile". Nessun "lo sistemiamo dopo".

## Anti-pattern: la CI verde non e' source-grounding

Caso reale (maggio 2026, PR #115-#120 chiuse): un agente Sonnet ha interpretato "fai passare la CI" come sinonimo di "sistema la skill". Ha calcolato gli SHA256 reali via GitHub Actions e committato su sources.yaml, ma **non ha riletto i PDF, non ha riscritto gli estratti, non ha verificato le costanti del codice**. Le 6 PR aperte facevano passare il check sintattico ma lasciavano la skill in stato di violazione semantica. Tutte chiuse senza merge.

**Regola consequenziale**: il workflow `.github/workflows/source-grounding.yml` controlla solo che gli SHA256 non siano placeholder. Quel check e' **necessario ma assolutamente non sufficiente**. Una skill source-grounded richiede che:

1. Gli `references/estratti/<file>.md` siano stati riscritti **dopo aver letto** il PDF, con citazioni dirette di paragrafo e (dove possibile) pagina.
2. Ogni costante numerica nel codice di calcolo della skill (es. coefficienti tabellari, soglie, formule) sia **rintracciabile** nel testo del PDF citato in un estratto verificato.
3. Ogni affermazione normativa nel SKILL.md, AGENTS.md, tasks/, examples/ sia **citabile** ad un paragrafo specifico del PDF letto.

Se sei un agent e non puoi leggere il PDF (sandbox, paywall, host irraggiungibili), **non puoi fare remediation**. Calcolare hash via CI non rende la skill source-grounded: lo fa solo la lettura del file. Vedi `methodology/source-grounding-remediation.md` per il workflow corretto.
