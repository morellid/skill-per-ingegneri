# accertamento-conformita-sanatoria-dpr380

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico edilizio / esperto di sanatorie da completare)

Skill di **supporto documentale** al **progettista** (geometra/architetto/ingegnere) e al **tecnico
incaricato** per l'**accertamento di conformità** (permesso di costruire o SCIA **in sanatoria**) degli
interventi edilizi abusivi, ai sensi del **D.P.R. 6 giugno 2001, n. 380 (Testo unico edilizia), Titolo
IV, artt. 36, 36-bis e 37**, come modificati dal **DL 69/2024 ("salva-casa"), conv. L. 105/2024**.

**Non redige** la domanda né la dichiarazione di conformità, **non qualifica** l'abuso, **non calcola**
l'oblazione né il valore venale e **non sostituisce** il progettista, lo sportello unico per l'edilizia
o gli enti competenti: inquadra presupposti, doppia conformità, oblazione, termini ed effetti.

## Target

Progettisti (geometri, architetti, ingegneri), uffici tecnici e sportelli unici per l'edilizia che devono
inquadrare l'accertamento di conformità di un abuso edilizio.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-articolo-doppia-conformita` | Stabilisce quale articolo si applica (36/36-bis/37) e quale doppia conformità è richiesta in base al tipo di abuso |
| `inquadra-procedura-oblazione-termini` | Inquadra dichiarazione del professionista, oblazione, profili sismici/paesaggistici, termini ed esito (art. 36-bis; art. 37) |

Nucleo: **art. 36** (assenza titolo/totale difformità, doppia conformità piena, 60 gg silenzio-rifiuto),
**art. 36-bis** (parziale difformità/variazioni essenziali, doppia conformità attenuata del salva-casa,
45 gg silenzio-assenso), **art. 37** (assenza/difformità dalla SCIA, sanzione e rinvio all'art. 36-bis).

## Fonti consultate

- **D.P.R. 6 giugno 2001, n. 380** (Testo unico edilizia) - artt. 36, 36-bis, 37 - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-17`, codice 001G0429, idGruppo 9). Modifiche del DL 69/2024
  (salva-casa), conv. L. 105/2024.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** la domanda di sanatoria né la dichiarazione di conformità del professionista.
- **Non qualifica** l'abuso (assenza/totale/parziale/variazione essenziale) né **calcola** l'oblazione o
  il valore venale.
- **Non tratta** il **condono** (leggi speciali: L. 47/1985 capo IV, L. 724/1994, L. 326/2003) né lo
  stato legittimo (art. 9-bis) se non nei richiami.

**La skill è un supporto documentale: non sostituisce il progettista, lo sportello unico per l'edilizia
o gli enti competenti, né la lettura degli artt. 36-37 del D.P.R. 380/2001 e delle norme del salva-casa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
