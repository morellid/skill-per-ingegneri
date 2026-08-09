# Regimi autorizzativi degli impianti FER e Modello Unico Parte III (D.Lgs. 190/2024)

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere di
> dominio da completare)

Inquadra il **regime amministrativo** di un intervento su impianti di produzione di energia da
**fonti rinnovabili** secondo il **D.Lgs. 25 novembre 2024, n. 190**: **attività libera** (art. 7,
Allegato A), **procedura abilitativa semplificata - PAS** (art. 8, Allegato B), **autorizzazione
unica** (art. 9, Allegato C), con i relativi termini e documenti. Copre inoltre l'adempimento del
**Modello Unico Parte III** adottato dal **D.M. MASE 15 luglio 2026, n. 223**, da trasmettere alla
piattaforma **SUER** per gli impianti in attività libera.

## Target

Ingegneri, progettisti e consulenti energetici che devono qualificare il titolo abilitativo di un
impianto FER (fotovoltaico, eolico, idroelettrico, biomasse, geotermico, accumuli, elettrolizzatori
e opere connesse), o assistere il proponente negli adempimenti successivi all'entrata in esercizio.

## Cosa fa

| Sotto-attività | File | Output |
|---|---|---|
| Classifica il regime amministrativo (attività libera / PAS / AU) | `tasks/classifica-regime-amministrativo.md` | Regime applicabile con voce di allegato, amministrazione competente, termini e documentazione |
| Imposta la trasmissione del Modello Unico Parte III a SUER | `tasks/adempi-modello-unico-parte-iii.md` | Soggetto obbligato, termine ordinario o transitorio, verifiche preliminari sul dies a quo |

Esempi eseguibili in `examples/`: un caso **conforme** (FV 90 kW in falda su capannone esistente,
attività libera + Modello Unico) e un caso **problematico** (due lotti a terra frazionati sotto
1 MW che il progetto unico dell'art. 6 c. 3 riporta in autorizzazione unica).

## Relazione con altre skill

- `via-screening-sia-dlgs152` - la verifica di assoggettabilità a VIA e la VIA sono presupposti del
  procedimento di autorizzazione unica (art. 9 c. 1), ma le soglie degli allegati del D.Lgs.
  152/2006 non sono coperte qui.
- `autorizzazione-paesaggistica-ordinaria-dlgs42` e `autorizzazione-paesaggistica-semplificata-dpr31`
  - il D.Lgs. 190/2024 disciplina l'autorizzazione paesaggistica con termini propri per l'attività
  libera (art. 7 cc. 4-6) e la assorbe nella conferenza di servizi dell'AU (art. 9 c. 10).
- `accessi-passi-carrabili-cds` - le interferenze con fasce di rispetto stradali e i nuovi accessi
  fanno salire il regime alla PAS (art. 7 c. 8).
- `edilizia-libera-cila-scia-dpr380` - i titoli edilizi ordinari restano il riferimento per le opere
  non riconducibili all'impianto FER.
- `cer-cacer-configurazione-gse` - la configurazione CACER/CER a valle presuppone un impianto
  legittimamente autorizzato secondo i regimi trattati qui.

## Fonti consultate

- **D.Lgs. 25 novembre 2024, n. 190** - testo consolidato Normattiva al 9 agosto 2026 (artt. 1, 5,
  6, 7, 8, 9 e Allegati A, B, C), GU Serie generale n. 291 del 12/12/2024.
- **D.M. MASE 15 luglio 2026, n. 223** - PDF firmato pubblicato sul sito istituzionale MASE.

Dettaglio con URL, SHA256 e trascrizioni in `references/sources.yaml`, `references/fonti/` e
`references/estratti/`.

## Limiti noti

- **Non presenta istanze** e non compila moduli.
- **Non riproduce i campi del Modello Unico Parte III**: l'Allegato 1 non è contenuto nel PDF del
  decreto pubblicato.
- La **data di entrata in vigore del D.M. 223/2026** non è determinabile dal decreto, che entra in
  vigore il giorno successivo alla pubblicazione sul sito MASE (art. 3 c. 1) senza indicarne la
  data. Di conseguenza il termine di 15 giorni per la messa a disposizione del modello su SUER e
  quello di 6 mesi per gli impianti già in esercizio sono espressi in forma **relativa**: la data
  va verificata su mase.gov.it.
- **Fuori scope v0.1**: criteri di individuazione delle **aree idonee** (art. 11-bis) e delle **zone
  di accelerazione** (art. 12), Allegato C-bis, Allegato D, modelli unici PAS e AU del D.M.
  441/2025, discipline regionali di adeguamento (art. 1 c. 3), regime delle concessioni idroelettriche
  e geotermiche, soglie VIA del D.Lgs. 152/2006.
- Le regioni possono **innalzare le soglie** degli Allegati A e B e devono adeguarsi entro 180
  giorni (art. 1 c. 3): l'esito va sempre riscontrato sulla normativa regionale vigente.
- La skill è un **supporto documentale**: non sostituisce l'asseverazione del tecnico abilitato né
  la valutazione dell'amministrazione competente.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
