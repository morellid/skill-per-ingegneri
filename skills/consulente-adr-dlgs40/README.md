# consulente-adr-dlgs40

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con consulente DGSA da completare)

Skill di **supporto documentale agli obblighi relativi al consulente per la
sicurezza dei trasporti di merci pericolose** (DGSA) ai sensi del **D.Lgs.
40/2000**.

**Non e' una skill di calcolo**: determina obbligo di nomina, esenzioni,
adempimenti, qualificazione e sanzioni; non redige la relazione annuale ne' la
relazione d'incidente, non tratta le regole tecniche dell'ADR.

## Target

Imprese di trasporto/carico-scarico di merci pericolose, consulenti (DGSA),
uffici della motorizzazione civile.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `verifica-obbligo-nomina` | Dato il profilo dell'impresa (attivita', quantitativi, occasionalita'), determina se deve nominare il consulente o se e' esente (artt. 2, 3 c. 6) |
| `checklist-adempimenti` | Verifica gli adempimenti del capo dell'impresa e del consulente (nomina, comunicazione, relazione annuale, relazione d'incidente) e le sanzioni (art. 6) |

Nucleo: ambito ed esenzioni (artt. 2, 3 c. 6), obblighi del capo dell'impresa
(nomina, comunicazione motorizzazione, relazione conservata 5 anni - art. 3),
obblighi del consulente (relazione annuale e d'incidente - art. 4),
qualificazione (art. 5), sanzioni (art. 6).

## Fonti consultate

- **D.Lgs. 4/2/2000 n. 40** (consulente merci pericolose), testo vigente su
  Normattiva (pagina indice pinnata `!vig=2026-07-14`) - artt. 2, 3, 4, 5, 6
- Quadro internazionale: **ADR 1.8.3** (UNECE) + **D.Lgs. 35/2010** (dir.
  2008/68/CE) - citati, non riprodotti

Dettaglio (URL, SHA256, trascrizione) in `references/sources.yaml`,
`references/fonti/`, `references/estratti/`.

## Limiti noti

- Non riproduce gli **allegati I e II** (compiti e materie d'esame) ne' il
  **formato della relazione annuale** (ADR 1.8.3)
- Non redige la relazione annuale ne' la relazione d'incidente
- Non tratta le **regole tecniche ADR** (classificazione, imballaggi,
  etichettatura) ne' il D.Lgs. 35/2010 oltre ai richiami
- Gli importi delle sanzioni sono espressi in lire nel testo (importi originari)

**La skill e' un supporto documentale: non sostituisce il consulente qualificato
ne' la motorizzazione civile.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
