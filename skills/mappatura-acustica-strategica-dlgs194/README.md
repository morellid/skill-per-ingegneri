# mappatura-acustica-strategica-dlgs194

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico acustico/ente competente da completare)

Skill di **supporto documentale agli obblighi di mappatura acustica strategica e
piani d'azione** contro il rumore ambientale ai sensi del **D.Lgs. 194/2005**
(attuazione della direttiva 2002/49/CE - END).

**Non e' una skill di calcolo/modellazione**: determina applicabilita', soggetti,
deliverable e scadenze, non produce le mappe ne' i piani.

## Target

Enti locali e regioni, gestori di infrastrutture di trasporto, ingegneri e
consulenti acustici/ambientali.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `diagnosi-applicabilita` | Dato l'elemento (agglomerato/asse/aeroporto) e i dati dimensionali: verifica le soglie (art. 2), individua il soggetto obbligato (autorita' regionale / gestore), i deliverable (mappe art. 3, piani art. 4) e le scadenze quinquennali |
| `checklist-adempimenti` | Verifica la completezza degli adempimenti (mappe/mappatura, piani, trasmissione dati, informazione del pubblico) |

Soglie (art. 2): agglomerato > 100.000 ab.; aeroporto > 50.000 movimenti/anno;
asse ferroviario > 30.000 treni/anno; asse stradale > 3.000.000 veicoli/anno.

## Fonti consultate

- **D.Lgs. 19/8/2005 n. 194**, testo vigente su Normattiva (pagina indice pinnata
  `!vig=2026-07-14`) - artt. 1-11 (attuazione dir. 2002/49/CE)

Dettaglio (URL, SHA256, trascrizione) in `references/sources.yaml`,
`references/fonti/`, `references/estratti/`.

## Limiti noti

- Non produce le mappe acustiche strategiche ne' i piani d'azione
- Non esegue la modellazione acustica ne' il calcolo di Lden/Lnight (CNOSSOS-EU,
  dir. (UE) 2015/996)
- Non riproduce gli allegati tecnici 1-6
- Non copre l'inquinamento acustico "ordinario" della L. 447/1995 oltre ai
  richiami (per quello vedi `valutazione-impatto-clima-acustico-l-447`)

**La skill e' un supporto documentale: non sostituisce l'autorita' competente, il
gestore o il tecnico acustico.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
