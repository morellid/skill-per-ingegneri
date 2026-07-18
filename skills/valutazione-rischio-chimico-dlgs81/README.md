# valutazione-rischio-chimico-dlgs81

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con RSPP / chimico / medico competente da completare)

Skill di **supporto documentale** al **datore di lavoro**, all'**RSPP** e al **tecnico della sicurezza**
per la **valutazione del rischio chimico** da agenti chimici pericolosi e le relative **misure di
prevenzione e protezione**, ai sensi del **D.Lgs. 9 aprile 2008, n. 81 (Testo unico sicurezza), Titolo
IX, Capo I, artt. 222-227**.

**Non redige** il DVR né la valutazione del rischio chimico, **non esegue** misurazioni né applica
algoritmi di stima e **non sostituisce** il datore di lavoro, l'RSPP, il medico competente o il chimico:
inquadra obblighi, contenuti e gerarchia delle misure.

## Target

Datori di lavoro, RSPP, tecnici della sicurezza e chimici che devono inquadrare la valutazione del
rischio chimico e le relative misure.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-valutazione-rischio-chimico` | Definizioni (222), contenuti e criteri della valutazione ex art. 28 (223), deroga per rischio basso/irrilevante (224) |
| `inquadra-misure-emergenze-formazione` | Gerarchia delle misure specifiche e misurazioni (225), incidenti/emergenze (226), informazione e formazione (227) |

Nucleo: **definizioni** e VLEP (art. 222), **valutazione** nel DVR ex art. 28 (art. 223), **misure
generali** e deroga rischio basso/irrilevante (art. 224), **misure specifiche** con gerarchia e
misurazioni (art. 225), **emergenze** (art. 226), **informazione e formazione** (art. 227).

## Fonti consultate

- **D.Lgs. 9 aprile 2008, n. 81** (Testo unico sicurezza) - Titolo IX, Capo I, artt. 222-227 - testo
  vigente su Normattiva (indice pinnato a `!vig=2026-07-17`, codice 008G0104, idGruppo 41).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** il DVR né la valutazione del rischio chimico; **non esegue** misurazioni né applica
  algoritmi di stima (es. modelli tipo MoVaRisCh).
- **Non riproduce** gli Allegati XXXVIII/XLI né i regolamenti CLP (1272/2008) e REACH (1907/2006).
- **Non tratta** cancerogeni/mutageni (Titolo IX Capo II), amianto (Capo III) né le atmosfere esplosive
  (Titolo XI) se non nei richiami.

**La skill è un supporto documentale: non sostituisce il datore di lavoro, l'RSPP, il medico competente
o il chimico, né la lettura degli artt. 222-227 del D.Lgs. 81/2008 e dei relativi allegati.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
