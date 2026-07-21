# AGENTS.md - dop-marcatura-ce-prodotti-cpr

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **fabbricante**, all'**ufficio tecnico-qualità** e al **tecnico** per
l'**inquadramento della redazione della Dichiarazione di Prestazione (DoP)** e dell'**apposizione della
marcatura CE** dei **prodotti da costruzione** secondo il **Regolamento (UE) n. 305/2011 (CPR)**: obbligo e
deroghe alla DoP, contenuto e modello, marcatura CE, sistemi di valutazione e verifica della costanza della
prestazione (VVCP) e obblighi degli operatori economici. Target: fabbricanti di prodotti da costruzione,
uffici tecnici/qualità, tecnici e direttori lavori che verificano i prodotti.

**E' una skill documentale per il tecnico**: fornisce i requisiti della DoP (artt. 4-7, All. III), le regole
della marcatura CE (artt. 8-9), i sistemi VVCP (All. V) e gli obblighi degli operatori (artt. 11-16); **non
redige** la DoP, **non individua** la norma armonizzata o il sistema VVCP del singolo prodotto, **non
esegue** prove né valutazioni.

## Nota sull'area e sulla complementarita'

Area **impianti-macchine-prodotti**. Appartiene al gruppo "marcatura CE / conformità dei prodotti" del repo
(`marcatura-ce-elettrici-lvd-emc-red`, `fascicolo-tecnico-macchine-reg-1230`, `istruzioni-uso-macchine-reg-1230`,
`fascicolo-tecnico-dispositivi-medici-mdr`, `ped-classificazione-conformita`, `ped`), coprendo il quadro
specifico dei **prodotti da costruzione** (CPR), distinto dalle direttive di prodotto (macchine, elettrici,
dispositivi medici, attrezzature a pressione). Non si sovrappone alle skill NTC (progettazione strutturale):
qui si tratta la **conformità del prodotto**, non il calcolo delle opere.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **reg-ue-305-2011-cpr**: Regolamento (UE) n. 305/2011 (CPR), GU UE L 88 del 4.4.2011, testo EUR-Lex
  (CELEX 32011R0305), SHA256 `2e98d2f0...` (doppio download riproducibile). Articoli e allegati rilevanti
  estratti con `pdftotext -layout` e trascritti verbatim.

Trascrizione in `references/fonti/reg-ue-305-2011-cpr.md`; estratto operativo in
`references/estratti/dop-marcatura-ce-checklist.md`.

## Punti chiave (verificati sul testo)

- **DoP** (artt. 4-7): obbligo per prodotti coperti da hEN o ETA; deroghe (art. 5); contenuto (art. 6:
  prodotto-tipo, VVCP, hEN/ETA, uso previsto, caratteristiche essenziali, livelli/classi/descrizione, NPD);
  modello Allegato III; fornitura (art. 7).
- **Marcatura CE** (artt. 8-9): solo se redatta la DoP; unica marcatura; elementi che la seguono.
- **Sistemi VVCP** (All. V): 1+, 1 (certificazione prodotto), 2+ (certificazione FPC), 3 (laboratorio di
  prova), 4 (solo fabbricante).
- **Operatori** (artt. 11-16): fabbricante (documentazione tecnica, 10 anni); mandatario (no documentazione
  tecnica); importatore; distributore; art. 15 (nome/marchio proprio o modifica → obblighi del fabbricante).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** la DoP al posto dell'operatore; non **individuare** la norma armonizzata applicabile né
  il **sistema VVCP** del prodotto (dipendono dalla hEN/decisione della Commissione); non **eseguire** prove
  o certificazioni.
- Non **trattare** in dettaglio la **valutazione tecnica europea (ETA/EAD)** (artt. 19-27) né gli
  **organismi notificati** (artt. 39-56); non **riprodurre** il modello di DoP del **Reg. delegato (UE)
  574/2014**.

### Cosa fare
- Fornire i requisiti della DoP, le regole della marcatura CE, i sistemi VVCP e gli obblighi degli
  operatori, sempre con rinvio all'articolo/allegato CPR.

## Aggiornamento delle fonti

CPR: se EUR-Lex pubblica una versione consolidata con modifiche rilevanti (es. la revisione del CPR - Reg.
UE 2024/3110), riscaricare, ricalcolare l'hash con doppio download e riallineare gli articoli. Verificare in
particolare il modello di DoP (Reg. delegato 574/2014) e gli eventuali nuovi obblighi degli operatori.

## Validatori

- Non ancora assegnato (Livello 2 con esperto di marcatura CE / prodotti da costruzione).

## Stato attuale

- Versione: 0.1.0-alpha (closes #386)
- Task files: 2 (`inquadra-contenuto-dop.md`, `inquadra-marcatura-ce-vvcp.md`)
- Esempi: 2 (contenuto DoP e sigla NPD per un aggregato; sistema VVCP 2+ e contenuto della marcatura CE)
