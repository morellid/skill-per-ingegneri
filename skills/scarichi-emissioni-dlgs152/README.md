# scarichi-emissioni-dlgs152

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con consulente ambientale da completare)

Skill di **supporto documentale alle autorizzazioni ambientali singole**
(residuali rispetto ad AUA e AIA) per lo **scarico di acque reflue industriali**
(art. 124 D.Lgs. 152/2006) e per le **emissioni in atmosfera** degli stabilimenti
(art. 269).

**Non e' una skill di calcolo**: determina obbligo, autorita', durata, rinnovo,
regime delle modifiche e sanzioni; non legge i valori limite ne' redige le
domande.

## Target

Gestori di impianti, consulenti ambientali, uffici provincia / regione / ente di
governo dell'ambito.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `inquadra-autorizzazione` | Dato l'impianto (tipo di scarico/emissione, recapito, AUA/AIA), determina quale autorizzazione singola serve, l'autorita' competente, la durata e i casi di nuova autorizzazione o comunicazione |
| `checklist-domanda-rinnovo` | Verifica contenuti della domanda, termini di rilascio/rinnovo e sanzioni (artt. 137, 279) |

Nucleo: **scarico** (art. 124: autorizzazione preventiva, provincia/ente
d'ambito, 90 gg, durata 4 anni) ed **emissioni** (art. 269: domanda con progetto
e relazione tecnica, durata 15 anni), con **AUA/AIA** che, se applicabili,
assorbono questi titoli.

## Fonti consultate

- **D.Lgs. 3/4/2006 n. 152** (TUA), testo vigente su Normattiva (pagina indice
  pinnata `!vig=2026-07-14`) - artt. 124, 137 (Parte terza) e 269, 279 (Parte
  quinta)

Dettaglio (URL, SHA256, trascrizione) in `references/sources.yaml`,
`references/fonti/`, `references/estratti/`.

## Limiti noti

- Non riproduce i **valori limite** (Allegato 5 parte terza; Allegati I-V parte
  quinta): rinvia agli allegati
- Non decide l'inquadramento **AUA** (DPR 59/2013) o **AIA** (art.
  29-quattuordecies): lo segnala e rinvia
- Non redige domande, progetti o relazioni tecniche
- Non copre in dettaglio scarichi urbani/domestici, autocontrolli e monitoraggi

**La skill e' un supporto documentale: non sostituisce l'autorita' competente ne'
i tecnici incaricati.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
