# verifiche-periodiche-ascensori-dpr162

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico verificatore/ditta di manutenzione da completare)

Skill di **supporto documentale all'iter di esercizio, verifiche periodiche e
manutenzione degli ascensori** (montacarichi e apparecchi assimilati) ai sensi
del **DPR 162/1999** (testo vigente, artt. 12-16).

**Non e' una skill di calcolo tecnico**: determina obblighi, periodicita' e
soggetti, non definisce le regole tecniche di installazione (norme UNI EN).

## Target

Proprietari e amministratori di condominio, ingegneri, ditte di manutenzione,
tecnici della sicurezza.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `diagnosi-adempimenti` | Dato l'impianto e il contesto: adempimenti di messa in esercizio (comunicazione al comune entro 60 gg, matricola entro 30 gg), periodicita' della verifica periodica (2 anni) e soggetto verificatore, verifiche straordinarie, manutenzione, libretto e targa |
| `checklist-esercizio` | Verifica la completezza degli adempimenti (dichiarazione di conformita', comunicazione, matricola, contratto di manutenzione, verifiche, libretto, targa) |

Periodicita' (art. 13/15): **verifica periodica ogni 2 anni**; manutenzione con
controlli sui dispositivi di sicurezza **almeno ogni 6 mesi (ascensori) / 1 anno
(montacarichi)**.

## Fonti consultate

- **D.P.R. 30/4/1999 n. 162**, testo vigente su Normattiva (pagina indice pinnata
  `!vig=2026-07-14`) - artt. 12-16 (esercizio, verifiche, manutenzione, libretto
  e targa; testo in vigore dal 2017)

Dettaglio (URL, SHA256, trascrizione) in `references/sources.yaml`,
`references/fonti/`, `references/estratti/`.

## Limiti noti

- Non copre l'immissione sul mercato / marcatura CE dei componenti (artt. 1-11,
  D.Lgs. 17/2010)
- Non definisce le regole tecniche di installazione (norme UNI EN 81) ne' esegue
  calcoli
- Non redige la modulistica comunale ne' i portali telematici
- Non calcola le date concrete delle scadenze

**La skill e' un supporto documentale: non sostituisce il proprietario, il
manutentore o il soggetto verificatore.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
