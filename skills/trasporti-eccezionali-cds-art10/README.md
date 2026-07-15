# trasporti-eccezionali-cds-art10

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto di autotrasporto da completare)

Skill di **supporto documentale al regime dei veicoli e dei trasporti
eccezionali** ai sensi dell'**art. 10 del Codice della Strada** (D.Lgs.
285/1992).

**Non e' una skill di calcolo**: inquadra l'eccezionalita', l'obbligo e il tipo
di autorizzazione, i presupposti e le sanzioni; non calcola sagoma/massa, non
individua nel merito l'ente/il percorso, non redige la domanda.

## Target

Imprese di autotrasporto, vettori, consulenti, uffici degli enti proprietari/
concessionari.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `inquadra-eccezionalita` | Dato il veicolo/trasporto (sagoma, massa, tipo di carico, assi), determina se e' eccezionale, se serve l'autorizzazione e chi la rilascia, e il tipo (singola/multipla/periodica) |
| `checklist-autorizzazione` | Verifica presupposti, prescrizioni e adempimenti dell'autorizzazione e le sanzioni (art. 10 c. 18-25) |

Nucleo: inquadramento (art. 10 c. 1-2, eccedenza sagoma art. 61 / massa art. 62),
obbligo ed ente competente (c. 6), tipi singola/multipla/periodica (c. 9),
presupposti (c. 10), sanzioni (c. 18-25).

## Fonti consultate

- **D.Lgs. 30/4/1992 n. 285** (Codice della Strada), **art. 10**, testo vigente su
  Normattiva (pagina indice pinnata `!vig=2026-07-14`). Articoli richiamati: 61
  (sagoma), 62 (massa), 13 (autorizzazioni), 54 (categorie)

Dettaglio (URL, SHA256, trascrizione) in `references/sources.yaml`,
`references/fonti/`, `references/estratti/`.

## Limiti noti

- Non calcola i **limiti di sagoma (art. 61) e massa (art. 62)** ne' le categorie
  (art. 54): rinvia agli articoli
- Non individua nel merito l'**ente competente** o il **percorso** ne' redige la
  domanda
- Non riproduce le **Linee guida MIT** sui trasporti eccezionali (2022) ne' il
  decreto attuativo del comma 10-bis

**La skill e' un supporto documentale: non sostituisce l'ente proprietario/
concessionario ne' il tecnico incaricato.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
