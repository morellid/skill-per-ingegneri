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
