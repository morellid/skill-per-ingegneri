# fattibilita-idraulica-toscana-lr41

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con geologo/ingegnere idraulico toscano da completare)

Skill di **supporto documentale alla fattibilita' delle trasformazioni nelle aree
a pericolosita' per alluvioni in Toscana** ai sensi della **L.R. 41/2018**.

**Non e' una skill di calcolo**: inquadra magnitudo idraulica, opere richieste,
limitazioni e condizioni; non legge le mappe di pericolosita', non misura
battente/velocita' ne' dimensiona le opere/i volumi.

## Target

Progettisti, tecnici comunali, geologi/ingegneri idraulici, uffici del Genio
Civile (Toscana).

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `verifica-fattibilita` | Dato il sito (area a pericolosita' frequente/poco frequente; battente e velocita' -> magnitudo) e l'intervento, determina l'ammissibilita' e le opere di messa in sicurezza richieste |
| `checklist-interventi` | Verifica le limitazioni (art. 10) e le condizioni delle opere (art. 8) per l'intervento, con rinvio agli atti di pianificazione di bacino |

Nucleo: **magnitudo idraulica** moderata/severa/molto severa (art. 2), **opere**
per il rischio medio R2 (art. 8), **limitazioni** nelle aree a pericolosita'
frequente (art. 10), condizioni per la **nuova costruzione** (art. 11) e per il
**patrimonio esistente** (art. 12).

## Fonti consultate

- **L.R. Toscana 24/7/2018 n. 41** (rischio alluvioni e tutela dei corsi
  d'acqua), testo vigente sulla Raccolta Normativa del Consiglio regionale (pagina
  a testo completo) - artt. 2, 7, 8, 10, 11, 12 (attuazione d.lgs. 49/2010)

Dettaglio (URL, SHA256, trascrizione) in `references/sources.yaml`,
`references/fonti/`, `references/estratti/`.

> Nota sulla scheda #49: la issue cita il DPGR 5/R/2020, che pero' disciplina il
> deposito/controllo delle indagini geologiche, idrauliche e sismiche, non la
> fattibilita' idraulica. La fonte corretta e' la **L.R. 41/2018**, usata qui.

## Limiti noti

- Non individua la **classe di pericolosita'** del sito ne' misura **battente/
  velocita'**: rinvia al PGRA/Piani di bacino e alla relazione idraulica
- Non progetta le opere ne' calcola i **volumi** di compenso/laminazione
- Non riproduce il **DPGR 5/R/2020** ne' le mappe di pericolosita'
- Vale solo per la **Toscana**

**La skill e' un supporto documentale: non sostituisce il PGRA, il progettista ne'
l'autorita' idraulica/comunale.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
