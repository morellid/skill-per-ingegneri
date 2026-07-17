# esercizio-controllo-impianti-termici-dpr74

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con termotecnico / manutentore abilitato da completare)

Skill di **supporto documentale** ai criteri di **esercizio, conduzione, controllo e
manutenzione** degli **impianti termici** per la climatizzazione (invernale ed estiva), secondo
il **D.P.R. 16 aprile 2013, n. 74** (attuativo del D.Lgs. 192/2005).

**Non riproduce i modelli RCEE** (Allegato A) né il libretto di impianto (DM 10/2/2014), **non
esegue** il controllo/manutenzione e **non sostituisce** il manutentore abilitato: inquadra
criteri e adempimenti.

## Target

Ingegneri termotecnici, responsabili di impianto, ditte di manutenzione e amministratori di
condominio.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `verifica-limiti-esercizio` | Verifica temperature massime e limiti di esercizio per zona climatica (periodi/orari, deroghe comunali) |
| `imposta-controllo-manutenzione` | Imposta responsabile/terzo responsabile, controllo e manutenzione (DM 37/2008) e il controllo di efficienza energetica con RCEE |

Nucleo: temperature massime (art. 3: 20/18 °C +2), limiti di esercizio per zona A-F (art. 4) e
ordinanze del sindaco (art. 5), responsabile e terzo responsabile (art. 6), controllo e
manutenzione (art. 7), controllo di efficienza energetica e RCEE per impianti > 10/12 kW (art. 8).

## Fonti consultate

- **D.P.R. 16 aprile 2013, n. 74** - artt. 3, 4, 5, 6, 7, 8 e Allegato A - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-16`, codice 13G00114)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non riproduce i campi dei modelli RCEE** (Allegato A, formato tabellare) né il **libretto di
  impianto** (DM 10/2/2014): rinvia agli atti.
- **Non esegue** il controllo/manutenzione né redige il RCEE.
- **Non copre** la disciplina **regionale** di dettaglio (periodicità, catasto impianti, bollino).
- È complementare a `trasmittanza-termica-opache-dm2015` (involucro) e `diagnosi-energetica-dlgs102`
  (diagnosi imprese).

**La skill è un supporto documentale: non sostituisce il manutentore abilitato, l'autorità
competente per le ispezioni né la lettura del D.P.R. 74/2013 (Allegato A) e del DM 10/2/2014.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
