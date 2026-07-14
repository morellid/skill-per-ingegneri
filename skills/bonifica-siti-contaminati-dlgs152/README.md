# bonifica-siti-contaminati-dlgs152

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico ambientale/geologo da completare)

Skill di **supporto documentale alla procedura di bonifica dei siti contaminati**
ai sensi del **Titolo V della Parte quarta del D.Lgs. 152/2006**.

**Non e' una skill di calcolo**: mappa definizioni, procedura, termini, attori e
sanzioni; non legge i valori CSC, non esegue l'analisi di rischio ne' redige il
piano di caratterizzazione.

## Target

Tecnici ambientali, geologi, gestori di siti, uffici regione / provincia /
comune / ARPA.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `diagnosi-procedura` | Dato l'evento (potenziale contaminazione, contaminazione storica, esito indagine preliminare), individua lo step dell'art. 242, i termini e gli attori, distinguendo sotto/sopra CSC e sopra CSR |
| `checklist-adempimenti` | Verifica completezza degli adempimenti e dei termini (comunicazioni, autocertificazione, caratterizzazione, analisi di rischio) e le sanzioni (art. 257) |

Nucleo: **definizioni** CSC/CSR e sito contaminato (art. 240), **procedura**
operativa del responsabile (art. 242), **ordinanza** della PA (art. 244), **aree
ridotte** (art. 249), **sanzioni** (art. 257).

## Fonti consultate

- **D.Lgs. 3/4/2006 n. 152** (TUA), Parte quarta Titolo V, testo vigente su
  Normattiva (pagina indice pinnata `!vig=2026-07-14`) - artt. 240, 242, 244,
  249, 257

Dettaglio (URL, SHA256, trascrizione) in `references/sources.yaml`,
`references/fonti/`, `references/estratti/`.

## Limiti noti

- Non riproduce i **valori CSC** (Allegato 5) ne' calcola le **CSR** (analisi di
  rischio, Allegato 1): rinvia agli allegati
- Non redige il **piano di caratterizzazione** (Allegato 2), il progetto di
  bonifica ne' i piani di monitoraggio
- Non tratta i **SIN** (art. 252) ne' oneri reali e privilegi (artt. 250, 253)
  oltre ai richiami

**La skill e' un supporto documentale: non sostituisce il tecnico competente ne'
l'autorita' (regione, provincia, comune, ARPA).**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
