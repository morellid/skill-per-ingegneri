# coordinatori-sicurezza-cantieri-dlgs81

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con CSP/CSE esperto / RSPP di settore edile da completare)

Skill di **supporto documentale** al regime dei **cantieri temporanei o mobili** (Titolo IV) e al
ruolo dei **coordinatori per la sicurezza** (CSP e CSE): definizioni, obblighi del
**committente/responsabile dei lavori**, del **CSP** e del **CSE**, secondo gli **artt. 89-92 del
D.Lgs. 9 aprile 2008, n. 81**.

**Non nomina** i coordinatori, **non redige** PSC/POS/fascicolo e **non sostituisce** il
committente, il CSP, il CSE né l'organo di vigilanza: inquadra ruoli, nomine e obblighi.

## Target

Ingegneri, committenti, responsabili dei lavori e coordinatori per la sicurezza che devono
impostare ruoli e adempimenti in un cantiere Titolo IV.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `verifica-obbligo-coordinatori` | Stabilisce se vanno nominati CSP e CSE (più imprese anche non contemporanee), con l'esonero per lavori privati < 100.000 euro |
| `obblighi-committente-cantiere` | Imposta le verifiche del committente (idoneità, DURC, patente, notifica preliminare) e i casi di sospensione del titolo abilitativo |

Nucleo: **definizioni** (art. 89), **obblighi del committente** (art. 90: nomina **CSP/CSE** quando
più imprese, verifica idoneità/DURC/patente, **notifica preliminare** ex art. 99, **sospensione del
titolo** in assenza di PSC/fascicolo/notifica/DURC, esonero < 100.000 euro), **CSP** (art. 91: PSC
+ fascicolo), **CSE** (art. 92: vigilanza su PSC/POS, contestazione, **sospensione diretta** in
pericolo grave e imminente).

## Fonti consultate

- **D.Lgs. 9 aprile 2008, n. 81** (T.U. sicurezza) - Titolo IV, artt. 89-92 - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-16`, codice 008G0104)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non nomina** i coordinatori né verifica i loro requisiti (art. 98).
- **Non redige** PSC/POS/fascicolo né riproduce gli allegati (X, XV, XVI, XVII): rinvio agli atti
  e a `pos-allegato-xv-checker`.
- **Non sostituisce** il committente, il CSP, il CSE né l'organo di vigilanza; non tratta gli
  obblighi delle imprese/lavoratori (artt. 95-97) se non come richiamo.

**La skill è un supporto documentale: non sostituisce il committente, il CSP, il CSE né l'organo
di vigilanza, né la lettura degli artt. 89-92 del D.Lgs. 81/2008 e degli allegati richiamati.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
