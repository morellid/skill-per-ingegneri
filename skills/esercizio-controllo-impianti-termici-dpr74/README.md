# esercizio-controllo-impianti-termici-dpr74

> Versione: 0.2.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con termotecnico / manutentore abilitato da completare)

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

Dalla v0.2.0-alpha la skill **avverte** anche che un intervento di **ristrutturazione dell'impianto
termico** rientra nel campo di applicazione dell'**Allegato III del D.Lgs. 199/2021** come modificato
dal **D.Lgs. 5/2026** (RED III), con obbligo di copertura da fonti rinnovabili del **15%** della
somma dei consumi per climatizzazione invernale ed estiva. La verifica va fatta **a monte**
dell'intervento e la trattazione completa è nella skill `relazione-tecnica-requisiti-minimi-dlgs192`.

## Fonti consultate

- **D.P.R. 16 aprile 2013, n. 74** - artt. 3, 4, 5, 6, 7, 8 e Allegato A - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-16`, codice 13G00114)
- **D.Lgs. 9 gennaio 2026, n. 5** (RED III) - art. 29, limitatamente al campo di applicazione
  dell'Allegato III, alla quota FER del 15% e alla Sezione D punto 1 - GU Serie generale n. 15 del
  20 gennaio 2026 (codice 26G00018)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non riproduce i campi dei modelli RCEE** (Allegato A, formato tabellare) né il **libretto di
  impianto** (DM 10/2/2014): rinvia agli atti.
- **Non esegue** il controllo/manutenzione né redige il RCEE.
- **Non copre** la disciplina **regionale** di dettaglio (periodicità, catasto impianti, bollino).
- **Non tratta** gli obblighi FER dell'Allegato III del D.Lgs. 199/2021: avverte e rinvia a
  `relazione-tecnica-requisiti-minimi-dlgs192`. Non calcola le quote di copertura e **non qualifica**
  l'intervento come ristrutturazione dell'impianto termico ai sensi del DM 26/6/2015 come modificato
  dal DM MASE 28/10/2025.
- È complementare a `trasmittanza-termica-opache-dm2015` (involucro) e `diagnosi-energetica-dlgs102`
  (diagnosi imprese).

**La skill è un supporto documentale: non sostituisce il manutentore abilitato, l'autorità
competente per le ispezioni né la lettura del D.P.R. 74/2013 (Allegato A) e del DM 10/2/2014.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
