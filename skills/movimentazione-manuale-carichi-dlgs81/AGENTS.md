# AGENTS.md - movimentazione-manuale-carichi-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'inquadramento degli obblighi in materia di **movimentazione
manuale dei carichi (MMC)**: campo di applicazione e definizioni, obblighi del datore
di lavoro, informazione/formazione/addestramento, secondo il **D.Lgs. 81/2008, Titolo
VI** (artt. 167-169). Target: datori di lavoro, RSPP/ASPP, ingegneri della sicurezza,
ergonomi, medici competenti.

**È una skill documentale**: inquadra obblighi e livelli formativi; **non calcola**
l'indice di sollevamento né la massa di riferimento (Allegato XXXIII, ISO 11228),
**non redige** il DVR-MMC, non sostituisce il datore di lavoro, l'RSPP o il medico
competente.

## Nota sull'area

Area **sicurezza-lavoro-cantieri**. Copre il **sovraccarico biomeccanico** da MMC
(Titolo VI): complementare a `valutazione-rischio-rumore-dlgs81`,
`valutazione-rischio-vibrazioni-dlgs81` (Titolo VIII, agenti fisici) e a
`sorveglianza-sanitaria-medico-competente-dlgs81` (art. 41, richiamato dall'art. 168).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-mmc**: D.Lgs. 81/2008, pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `18fbc542...`; codice 008G0104; stesso indice delle altre
  skill D.Lgs. 81). Artt. 167, 168, 169, idGruppo 30, flagTipoArticolo 0, caricati via
  `caricaArticolo` e trascritti verbatim.

Trascrizione in `references/fonti/dlgs-81-2008-mmc.md`; estratto operativo in
`references/estratti/mmc-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 167**: campo di applicazione (rischi di patologie da sovraccarico
  biomeccanico, in particolare dorso-lombari); MMC = trasporto/sostegno di un carico
  (sollevare/deporre/spingere/tirare/portare/spostare); patologie osteoarticolari,
  muscolo-tendinee, nervo-vascolari.
- **Art. 168**: c. 1 evitare la MMC con attrezzature meccaniche; c. 2 se non evitabile,
  misure/mezzi tenendo conto dell'allegato XXXIII (a organizzazione posti, b valutazione
  anche in progettazione, c riduzione rischi per fattori individuali/ambiente/esigenze,
  d sorveglianza sanitaria art. 41); c. 3 norme tecniche come criteri di riferimento
  (buone prassi/linee guida altrimenti).
- **Art. 169**: c. 1 informazione (peso/caratteristiche) e formazione (rischi/esecuzione);
  c. 2 addestramento (corrette manovre e procedure).

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** l'indice di sollevamento, la massa di riferimento o i moltiplicatori:
  sono nell'Allegato XXXIII e nelle ISO 11228 (non riprodotte).
- Non **inventare** soglie di peso (es. 25/20/30 kg): non sono negli artt. 167-169.
- Non **redigere** il DVR-MMC né esprimere giudizi di sorveglianza sanitaria.

### Cosa fare
- **Inquadrare** l'applicabilità e gli obblighi (evitare/ridurre, valutazione,
  sorveglianza, formazione), con rinvio all'Allegato XXXIII/ISO 11228 e ai soggetti
  competenti (datore di lavoro, RSPP, medico competente).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 81/2008 pinnato a nuovo `!vig=` (nuovo hash)
e rileggere gli artt. 167-169 (testo tra `(( ))`). L'Allegato XXXIII e le ISO 11228 sono
citati come rinvio, non riprodotti.

## Validatori

- Non ancora assegnato (Livello 2 con RSPP / medico competente / ergonomo).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`inquadra-obblighi-mmc.md`, `imposta-informazione-formazione.md`)
- Esempi: 2 (obblighi datore per mansione di magazzino - artt. 167-168; informazione/formazione/addestramento - art. 169)
