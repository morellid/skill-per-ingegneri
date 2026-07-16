# segnalazione-agibilita-dpr380

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico abilitato / SUE da completare)

Skill di **supporto documentale** alla **segnalazione certificata di agibilità (SCA)**:
presupposti, soggetti, termine, interventi soggetti, sanzione, agibilità parziale, documentazione
allegata e deroghe igienico-sanitarie, secondo l'**art. 24 del D.P.R. 6 giugno 2001, n. 380**
(art. 25 abrogato dal D.Lgs. 222/2016).

**Non redige né presenta** la SCA, **non compila** la modulistica regionale/comunale e **non
sostituisce** il direttore dei lavori né il professionista abilitato: inquadra il metodo documentale.

## Target

Ingegneri, architetti e direttori dei lavori che devono preparare o verificare la SCA a fine lavori.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `prepara-sca` | Individua soggetto, termine (15 gg), interventi soggetti e compone l'elenco della documentazione da allegare (c. 5) |
| `verifica-agibilita-parziale` | Verifica i presupposti dell'agibilità parziale (c. 4) e delle deroghe igienico-sanitarie asseverabili (c. 5-bis/ter) |

Nucleo: **strumento** SCA (c. 1); **soggetto/termine** 15 gg al SUE e **interventi** (c. 2);
**sanzione** 77-464 euro (c. 3); **agibilità parziale** (c. 4); **documentazione** allegata (c. 5);
**deroghe** igienico-sanitarie (c. 5-bis/ter: altezza 2,40 m, monostanza 20/28 mq); **utilizzo**
dalla presentazione e **controlli** (c. 6-7).

## Fonti consultate

- **D.P.R. 6 giugno 2001, n. 380** - art. 24 (art. 25 abrogato) - testo vigente su Normattiva
  (indice pinnato a `!vig=2026-07-16`, codice 001G0429)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige né presenta** la SCA e **non compila** la modulistica regionale/comunale: rinvio al
  SUE e a `modulistica-edilizia-unificata`.
- **Non esegue** il collaudo statico (art. 67 → `denuncia-opere-strutturali-l1086`) né le
  certificazioni di impianti (DM 37/2008) o accessibilità (DM 236/1989).
- **Non sostituisce** il direttore dei lavori né il professionista abilitato; non tratta il regime
  edilizio dell'intervento se non come richiamo.

**La skill è un supporto documentale: non sostituisce il direttore dei lavori né il professionista
abilitato, né la lettura dell'art. 24 del D.P.R. 380/2001 e degli atti richiamati.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
