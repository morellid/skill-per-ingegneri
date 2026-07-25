# fascicolo-opera-manutenzione-dlgs81

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con coordinatore per la sicurezza CSP/CSE abilitato da completare)

Skill di **supporto documentale** al **coordinatore per la sicurezza in fase di progettazione (CSP)**, al **CSE** e al
**committente** per la **predisposizione**, l'**aggiornamento** e la **verifica di completezza** del **Fascicolo con le
caratteristiche dell'opera** secondo il **D.Lgs 81/2008**, **art. 91 comma 1 lett. b)** e **Allegato XVI**: titolarità
e ciclo di vita, struttura in tre capitoli, distinzione tra misure in dotazione dell'opera e ausiliarie, informazioni
per la manutenzione in sicurezza.

**Non redige** il fascicolo al posto del coordinatore né **progetta** le misure concrete (linee vita, ganci) e **non
sostituisce** il coordinatore firmatario: inquadra la struttura e i contenuti. È **distinta** da
`psc-piano-sicurezza-coordinamento-dlgs81` (PSC) e da `pos-allegato-xv-checker` (POS).

## Target

Coordinatori per la sicurezza (CSP/CSE) e committenti che devono predisporre, aggiornare o verificare la completezza
del Fascicolo dell'opera secondo il D.Lgs 81/2008 art. 91 e Allegato XVI.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-struttura-e-schede-fascicolo` | Titolarità/ciclo di vita (artt. 91-92, Introduzione) e struttura in 3 capitoli con le schede I, II-1/2/3, III-1/2/3 |
| `imposta-misure-per-interventi-successivi` | Capitolo II: distinzione misure in dotazione/ausiliarie, i 7 elementi, informazioni per l'uso in sicurezza e la manutenzione nel tempo |

Nucleo: il **CSP predispone** il fascicolo (art. 91 c.1 lett. b), il **CSE lo adegua** (art. 92), il **committente lo
aggiorna** nella vita dell'opera; **non** per la manutenzione ordinaria; **3 capitoli** (opera/soggetti; rischi e
misure per gli interventi successivi; documentazione); **misure in dotazione** (linee vita, ganci) vs **ausiliarie**
(ponteggi, DPI); **7 elementi**; **scheda II-3** con verifiche/manutenzione/periodicità.

## Relazione con altre skill

- Copre il **Fascicolo dell'opera** (Allegato XVI). **Distinta** da `psc-piano-sicurezza-coordinamento-dlgs81` (PSC,
  art. 100 + Allegato XV), `pos-allegato-xv-checker` (POS) e `coordinatori-sicurezza-cantieri-dlgs81` (artt. 89-92).
  Condivide la fonte (Testo coordinato INL del D.Lgs 81/2008).

## Fonti consultate

- **D.Lgs 9 aprile 2008 n. 81** - **art. 91-92 e Allegato XVI** - Testo coordinato Edizione gennaio 2025 (INL), SHA256
  `f593e18...`, estratto con `pdftotext`. Edizione INL non ufficiale: per uso autoritativo cross-checkare su
  Normattiva/Gazzetta Ufficiale.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** il fascicolo al posto del coordinatore né **progetta** le misure concrete (linee vita/ganci — norme
  UNI di buona tecnica); non compila le schede.
- **Non tratta** il **PSC** (art. 100 + Allegato XV, → skill `psc-piano-sicurezza-coordinamento-dlgs81`), il **POS**
  (Allegato XV punto 3.2, → skill `pos-allegato-xv-checker`), i **ruoli/obblighi** di CSP/CSE (artt. 89-92, → skill
  `coordinatori-sicurezza-cantieri-dlgs81`) né la **notifica preliminare** (art. 99); non sostituisce il coordinatore
  firmatario.

**La skill è un supporto documentale: non sostituisce il coordinatore per la sicurezza firmatario del fascicolo né la lettura dell'art. 91 e dell'Allegato XVI del D.Lgs 81/2008.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
