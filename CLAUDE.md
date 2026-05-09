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
