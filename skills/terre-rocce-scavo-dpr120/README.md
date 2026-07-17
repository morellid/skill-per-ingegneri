# terre-rocce-scavo-dpr120

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con professionista ambientale / ARPA da completare)

Skill di **supporto documentale** alla **gestione delle terre e rocce da scavo**:
qualificazione come **sottoprodotto** (anziché rifiuto), **esclusione dalla disciplina rifiuti**
(riutilizzo nel sito) o gestione come rifiuto, secondo il **D.P.R. 13 giugno 2017, n. 120**
(coordinato con la Parte IV del D.Lgs. 152/2006).

**Non riproduce i valori CSC** né gli Allegati tecnici, **non esegue** campionamento/analisi e
**non sostituisce** l'ARPA: inquadra qualificazione e procedure.

## Target

Ingegneri, consulenti ambientali, imprese e direzione lavori che gestiscono terre da scavo.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `qualifica-terre-scavo` | Stabilisce se le terre sono sottoprodotto (art. 4), escluse dai rifiuti (art. 24) o rifiuto, e la dimensione del cantiere |
| `gestisci-dichiarazione-piccoli-cantieri` | Imposta la dichiarazione di utilizzo dei piccoli cantieri (allegato 6, 15 gg, Comune/ARPA, tempi, DAU) |

Nucleo: sottoprodotto (art. 4), dimensione del cantiere (art. 2: piccole ≤ 6.000 mc / grandi),
requisiti ambientali CSC (art. 20), dichiarazione di utilizzo (art. 21), utilizzo nel sito di
produzione escluse dai rifiuti (art. 24).

## Fonti consultate

- **D.P.R. 13 giugno 2017, n. 120** - artt. 1, 2, 4, 20, 21, 24 - testo vigente su Normattiva
  (indice pinnato a `!vig=2026-07-16`, codice 17G00135)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non riproduce i valori CSC** (Tab. 1, Allegato 5, Parte IV, D.Lgs. 152/2006) né gli
  **Allegati tecnici** del DPR (campionamento/analisi, modulistica): rinvia agli atti.
- **Non esegue** campionamento/analisi né redige piano/dichiarazione.
- Per i **grandi cantieri** (> 6.000 mc, VIA/AIA) il **piano di utilizzo** (artt. 9 e ss.) è solo
  richiamato.
- È complementare a `trasporto-rifiuti-fir-dlgs152` e `bonifica-siti-contaminati-dlgs152`.

**La skill è un supporto documentale: non sostituisce l'ARPA, il professionista ambientale né la
lettura del D.P.R. 120/2017 (e dei suoi Allegati) e delle CSC del D.Lgs. 152/2006.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
