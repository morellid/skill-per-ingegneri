# trasporto-rifiuti-fir-dlgs152

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto rifiuti/Albo da completare)

Skill di **supporto documentale agli obblighi del trasporto dei rifiuti** ai
sensi del **D.Lgs. 152/2006** (Parte quarta): formulario di identificazione dei
rifiuti (FIR), iscrizione all'Albo nazionale gestori ambientali, sanzioni.

**Non e' una skill di calcolo**: non classifica il rifiuto, non redige il
formulario, non riproduce il modello del FIR ne' le regole dell'Albo.

## Target

Produttori di rifiuti, trasportatori, gestori ambientali, uffici dell'Albo.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `inquadra-obblighi` | Dato il soggetto (produttore, trasportatore conto terzi/proprio, tipo e quantita' di rifiuto), determina l'obbligo del FIR (art. 193) e dell'iscrizione all'Albo (art. 212) o l'applicabilita' delle semplificazioni |
| `checklist-fir` | Verifica la corretta gestione del formulario (copie, firme, distribuzione) e le sanzioni (art. 258) |

Nucleo: **formulario FIR** (art. 193: obbligo, quattro copie, firme, RENTRI,
esclusioni), **iscrizione all'Albo** (art. 212: requisito per raccolta/trasporto;
semplificazione per i propri rifiuti, soglia 30 kg/30 l per i pericolosi),
**sanzioni** (art. 258).

## Fonti consultate

- **D.Lgs. 3/4/2006 n. 152** (TUA), Parte quarta, testo vigente su Normattiva
  (pagina indice pinnata `!vig=2026-07-14`) - artt. 193, 212, 258. Richiami: art.
  188-bis (RENTRI), art. 190 (registri), ADR

Dettaglio (URL, SHA256, trascrizione) in `references/sources.yaml`,
`references/fonti/`, `references/estratti/`.

## Limiti noti

- Non riproduce il **modello del formulario** ne' la disciplina del **RENTRI**
  (art. 188-bis) e dei decreti attuativi
- Non riproduce le **categorie/classi** dell'Albo
- Non tratta i **registri di carico/scarico** (art. 190), il **MUD** ne' l'ADR
  oltre ai richiami
- Non stabilisce la **classificazione** del rifiuto (codici EER) ne' redige il FIR

**La skill e' un supporto documentale: non sostituisce il gestore, il
trasportatore ne' l'Albo.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
