# movimentazione-manuale-carichi-dlgs81

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con RSPP / medico competente / ergonomo da completare)

Skill di **supporto documentale** all'inquadramento degli obblighi in materia di
**movimentazione manuale dei carichi (MMC)**: campo di applicazione e definizioni,
obblighi del datore di lavoro, informazione/formazione/addestramento, secondo il
**D.Lgs. 81/2008, Titolo VI (artt. 167-169)**.

**Non calcola** l'indice di sollevamento né la massa di riferimento (Allegato XXXIII,
ISO 11228), **non redige** il DVR-MMC e **non sostituisce** il datore di lavoro, l'RSPP
o il medico competente: inquadra obblighi e livelli formativi.

## Target

Datori di lavoro, RSPP/ASPP, ingegneri della sicurezza, ergonomi e medici competenti.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-obblighi-mmc` | Verifica se l'attività rientra nella MMC (art. 167) e ricostruisce gli obblighi del datore (evitare/ridurre, valutazione, sorveglianza sanitaria; art. 168) |
| `imposta-informazione-formazione` | Imposta informazione, formazione e addestramento dei lavoratori (art. 169), distinguendo i tre livelli |

Nucleo: **definizioni** (art. 167); **obblighi del datore** - evitare con mezzi
meccanici, valutazione (allegato XXXIII), riduzione, sorveglianza sanitaria art. 41
(art. 168); **informazione/formazione/addestramento** (art. 169).

## Fonti consultate

- **D.Lgs. 9/4/2008 n. 81** (Testo unico sicurezza) - Titolo VI, artt. 167-169 - testo
  vigente su Normattiva (indice pinnato a `!vig=2026-07-17`, codice 008G0104)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** l'**indice di sollevamento** né la **massa di riferimento**/i
  moltiplicatori: i criteri numerici sono nell'**Allegato XXXIII** e nelle norme
  tecniche **ISO 11228-1/2/3** (rinvio degli artt. 168-169), non riprodotti.
- **Non redige** il DVR-MMC né la relazione ergonomica.
- **Non esprime** giudizi di **sorveglianza sanitaria** (art. 41).
- **Non tratta** in dettaglio i **movimenti ripetitivi** degli arti superiori (ISO
  11228-3) se non nel richiamo generale al sovraccarico biomeccanico.
- **Non sostituisce** il datore di lavoro, l'RSPP o il medico competente.

**La skill è un supporto documentale: non sostituisce il datore di lavoro, l'RSPP né il
medico competente, né la lettura degli artt. 167-169 del D.Lgs. 81/2008.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
