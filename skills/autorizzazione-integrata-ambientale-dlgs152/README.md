# autorizzazione-integrata-ambientale-dlgs152

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico ambientale / autorità competente o ARPA da completare)

Skill di **supporto documentale** all'**Autorizzazione Integrata Ambientale (AIA/IPPC)**: domanda,
procedura di rilascio, contenuto e condizioni (VLE su BAT), rinnovo/riesame, rispetto delle condizioni
e controlli/ispezioni, secondo il **D.Lgs. 3 aprile 2006, n. 152, Parte II, Titolo III-bis** (artt.
29-ter, 29-quater, 29-sexies, 29-octies, 29-decies).

**Non redige** la domanda/AIA, **non individua** le BAT e **non sostituisce** il gestore, l'autorità
competente o ISPRA/ARPA: inquadra procedura, contenuto e controlli.

## Target

Ingegneri, gestori di installazioni IPPC e consulenti ambientali.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-domanda-aia` | Verifica l'assoggettabilità (rinvio All. VIII/XII) e compone i contenuti della domanda (art. 29-ter) e i passi della procedura (art. 29-quater) |
| `verifica-condizioni-controlli` | Inquadra il contenuto/condizioni su BAT (art. 29-sexies), il riesame (art. 29-octies) e i controlli/inosservanze (art. 29-decies) |

Nucleo: **domanda** (art. 29-ter); **procedura** con conferenza di servizi e termine di 150 giorni
(art. 29-quater); **contenuto e VLE su BAT** (art. 29-sexies); **rinnovo/riesame** (art. 29-octies);
**controlli e ispezioni ISPRA/ARPA** e inosservanze (art. 29-decies).

## Fonti consultate

- **D.Lgs. 3 aprile 2006, n. 152** (Parte II, Titolo III-bis) - artt. 29-ter, 29-quater, 29-sexies,
  29-octies, 29-decies - testo vigente su Normattiva (indice pinnato a `!vig=2026-07-17`, codice
  006G0171)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** la domanda né l'AIA e **non compila** la modulistica dell'autorità competente.
- **Non individua** le **BAT** applicabili né i **BAT-AEL**: rinvia alle conclusioni sulle BAT (BREF).
- **Non riproduce** gli **Allegati VIII/XII** (attività IPPC e soglie): l'assoggettabilità va
  verificata sugli allegati.
- **Non sostituisce** il gestore, l'autorità competente o ISPRA/ARPA; non tratta le sanzioni (art.
  29-quattuordecies).

**La skill è un supporto documentale: non sostituisce il gestore, l'autorità competente né ISPRA/ARPA,
né la lettura del Titolo III-bis del D.Lgs. 152/2006 e degli allegati richiamati.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
