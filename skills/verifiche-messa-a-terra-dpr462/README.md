# verifiche-messa-a-terra-dpr462

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con perito elettrotecnico/RSPP da completare)

Skill di **supporto documentale agli adempimenti del DPR 462/2001** per gli
impianti elettrici di **messa a terra**, i dispositivi di protezione contro le
**scariche atmosferiche** e gli impianti elettrici in **luoghi con pericolo di
esplosione**, collocati nei luoghi di lavoro.

**Non e' una skill di calcolo tecnico**: determina obblighi, periodicita' e
soggetti, non definisce le regole tecniche degli impianti (norme CEI).

## Target

Datori di lavoro, ingegneri e periti elettrotecnici, RSPP, consulenti della
sicurezza, installatori.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `diagnosi-adempimenti` | Dato il tipo di impianto e l'ambiente: applicabilita' del DPR 462/2001, periodicita' della verifica periodica (5 anni / 2 anni), soggetti abilitati (ASL/ARPA o organismi), adempimenti di messa in esercizio e denuncia, comunicazione INAIL |
| `checklist-adempimenti` | Verifica la completezza degli adempimenti (dichiarazione di conformita', denuncia entro 30 gg, prima verifica, verifiche periodiche, verbali, comunicazione INAIL art. 7-bis, variazioni) |

Regola di periodicita' (art. 4/6): **5 anni** per messa a terra/scariche
atmosferiche ordinari; **2 anni** per cantieri, locali ad uso medico, ambienti a
maggior rischio in caso di incendio e luoghi con pericolo di esplosione.

## Fonti consultate

- **D.P.R. 22/10/2001 n. 462**, testo vigente su Normattiva (pagina indice
  pinnata `!vig=2026-07-14`) - artt. 1-8 (art. 7-bis banca dati INAIL in vigore
  dal 1-3-2020)

Dettaglio (URL, SHA256, trascrizione) in `references/sources.yaml`,
`references/fonti/`, `references/estratti/`.

> Nota: l'**ISPESL** citato nel DPR e' oggi confluito nell'**INAIL** (DL 78/2010).

## Limiti noti

- Non definisce le regole tecniche di realizzazione/verifica (norme CEI, es. CEI
  64-8, CEI EN 62305) ne' esegue calcoli
- Non fornisce gli importi delle tariffe (decreto ISPESL 7/7/2005, non trascritto)
- Non gestisce la modulistica INAIL puntuale ne' i portali telematici
- Non copre gli obblighi generali del D.Lgs. 81/2008 oltre al richiamo del datore
  di lavoro
- Non calcola le date concrete delle scadenze

**La skill e' un supporto documentale: non sostituisce l'installatore,
l'organismo verificatore o il datore di lavoro nei rispettivi adempimenti.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
