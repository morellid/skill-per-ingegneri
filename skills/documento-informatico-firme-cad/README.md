# documento-informatico-firme-cad

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto di diritto dell'informatica / notaio da completare)

Skill di **supporto documentale** al **valore giuridico del documento informatico** e delle
**firme elettroniche** secondo il **Codice dell'amministrazione digitale (D.Lgs. 7 marzo 2005,
n. 82)**, artt. 20, 21 e 24.

**Non appone né verifica firme**, **non valuta** la validità del singolo atto e **non
sostituisce** il professionista, il notaio né il giudice: inquadra valore probatorio e tipi di
firma.

## Target

Ingegneri e professionisti che firmano digitalmente elaborati, depositano atti telematici o
gestiscono documenti in formato digitale.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `valuta-valore-documento` | Stabilisce se un documento informatico soddisfa la forma scritta / art. 2702 c.c. o è liberamente valutabile (art. 20), secondo il tipo di firma |
| `inquadra-firma-atto` | Individua il tipo di firma richiesto (a pena di nullità per gli atti art. 1350 c.c.) e verifica i requisiti del certificato (art. 21, 24) |

Nucleo: **art. 20** (forma scritta ed **efficacia art. 2702 c.c.** con firma digitale/
qualificata/avanzata o processo con requisiti AgID; libera valutazione negli altri casi;
presunzione di riconducibilità al titolare), **art. 21** (atti **art. 1350 c.c.** a pena di
nullità con firma qualificata/digitale; atto pubblico informatico), **art. 24** (firma digitale
univoca; **certificato qualificato** valido; firma su certificato revocato = mancata
sottoscrizione).

## Fonti consultate

- **D.Lgs. 7 marzo 2005, n. 82** (CAD) - artt. 20, 21, 24 - testo vigente su Normattiva (indice
  pinnato a `!vig=2026-07-16`, codice 005G0104)
- **Linee guida AgID** (art. 71 CAD) e **Reg. UE 910/2014 (eIDAS)** - citati (regole tecniche)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non riproduce** le Linee guida AgID né l'eIDAS: rinvio per le regole tecniche (formazione,
  firme, validazione temporale, conservazione).
- **Non appone né verifica** firme, **non valuta** la validità del singolo atto.
- **Non sostituisce** il professionista, il notaio né il giudice; non tratta conservazione
  (artt. 43-44) e copie/duplicati (artt. 22-23-bis).

**La skill è un supporto documentale: non sostituisce il professionista, il notaio né il
giudice, né la lettura degli artt. 20/21/24 del CAD e delle Linee guida AgID / eIDAS.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
