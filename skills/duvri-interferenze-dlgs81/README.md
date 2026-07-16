# duvri-interferenze-dlgs81

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con RSPP/esperto sicurezza da completare)

Skill di **supporto documentale** agli obblighi del **datore di lavoro committente** nei
contratti d'appalto, d'opera o di somministrazione e alla redazione del **DUVRI**
(Documento Unico di Valutazione dei Rischi da Interferenze) ai sensi dell'**art. 26 del
D.Lgs. 81/2008**.

**Non valuta i rischi specifici** dell'appaltatore, **non quantifica i costi** e **non
copre i cantieri edili del Titolo IV** (per cui valgono PSC/POS).

## Target

Datori di lavoro committenti, RSPP e consulenti che affidano lavori/servizi/forniture con
possibili interferenze.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `verifica-idoneita-e-informazione` | Verifica dell'idoneita' tecnico-professionale (c.1 a) e informazione sui rischi specifici e sulle misure di emergenza (c.1 b) |
| `imposta-duvri` | Determina se il DUVRI e' dovuto (esclusioni c.3-bis), ne struttura i contenuti (interferenze -> misure, aggiornamento) e imposta i costi non ribassabili (c.5) |

Nucleo: **idoneita' tecnico-professionale** (c.1), **cooperazione/coordinamento** (c.2),
**DUVRI** ed esclusioni (c.3, 3-bis), **costi della sicurezza** non ribassabili (c.5),
tessera di riconoscimento e responsabilita' solidale (c.8).

## Fonti consultate

- **D.Lgs. 81/2008 art. 26** - testo vigente su Normattiva (indice pinnato a `!vig=`)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non valuta i rischi specifici** propri dell'attivita' dell'appaltatore (restano nel suo
  DVR).
- **Non quantifica** i costi della sicurezza da interferenza.
- **Non copre i cantieri Titolo IV** (PSC/POS -> `pos-allegato-xv-checker`) ne' redige il
  **DVR** del committente (art. 28-29 -> `dvr-generico`).

**La skill e' un supporto documentale: non sostituisce il datore di lavoro committente,
l'RSPP ne' il coordinamento tra le imprese.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
