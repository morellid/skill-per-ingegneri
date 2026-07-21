# AGENTS.md - marcatura-ce-dpi-reg-425

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **fabbricante**, all'**ufficio tecnico** e al **tecnico** per l'**inquadramento
della classificazione, della valutazione della conformità e della marcatura CE** dei **dispositivi di
protezione individuale (DPI)** come prodotti secondo il **Regolamento (UE) 2016/425**: categorie di rischio,
procedure di conformità per categoria, obblighi documentali, dichiarazione di conformità UE e marcatura CE.
Target: fabbricanti di DPI, uffici tecnici/qualità, tecnici e RSPP che verificano la conformità dei DPI come
prodotti.

**E' una skill documentale per il tecnico**: fornisce le categorie di rischio (Allegato I), le procedure di
conformità (art. 19), gli obblighi del fabbricante (artt. 8-9), la dichiarazione UE (art. 15, All. IX) e le
regole della marcatura CE (artt. 16-17); **non progetta** né **certifica** il DPI, **non esegue** prove né
l'esame UE del tipo.

## Nota sull'area e sulla complementarita'

Area **impianti-macchine-prodotti**. Appartiene al gruppo "marcatura CE / conformità dei prodotti" del repo
(`marcatura-ce-elettrici-lvd-emc-red`, `dop-marcatura-ce-prodotti-cpr`, `fascicolo-tecnico-macchine-reg-1230`,
`fascicolo-tecnico-dispositivi-medici-mdr`, `ped-classificazione-conformita`), coprendo il quadro specifico
dei **DPI come prodotti** (Reg. 2016/425). **Distinta** e complementare a `dpi-protezione-individuale-dlgs81`
(area sicurezza-lavoro-cantieri), che riguarda l'**uso e la scelta** dei DPI da parte del **datore di
lavoro** (D.Lgs 81/2008, artt. 74-79): qui si tratta il **lato prodotto/fabbricante**, non il lato uso.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **reg-ue-2016-425-dpi**: Regolamento (UE) 2016/425 (DPI), GU UE L 81 del 31.3.2016, testo EUR-Lex
  (CELEX 32016R0425), SHA256 `8b4c61bb...` (doppio download riproducibile). Articoli e allegati rilevanti
  estratti con `pdftotext -layout` e trascritti verbatim.

Trascrizione in `references/fonti/reg-ue-2016-425-dpi.md`; estratto operativo in
`references/estratti/marcatura-ce-dpi-checklist.md`.

## Punti chiave (verificati sul testo)

- **Categorie di rischio** (art. 18, All. I): I (rischi minimi), II (residuale), III (rischi gravissimi -
  morte/danni irreversibili, elenco tassativo a-m).
- **Procedure** (art. 19): cat. I → modulo A (All. IV); cat. II → modulo B (All. V) + modulo C (All. VI);
  cat. III → modulo B + modulo C2 (All. VII) o modulo D (All. VIII); deroga cat. II per DPI su misura di
  cat. III.
- **Obblighi** (artt. 8-9): RESS (All. II), documentazione tecnica (All. III), dichiarazione UE, marcatura
  CE, conservazione 10 anni; mandatario non progetta né redige la documentazione tecnica.
- **Dichiarazione UE** (art. 15, All. IX) e **marcatura CE** (artt. 16-17): per la cat. III seguita dal
  numero dell'organismo notificato.

## Convenzioni specifiche

### Cosa NON fare
- Non **progettare** né **certificare** il DPI; non **eseguire** prove o l'esame UE del tipo.
- Non **riprodurre** in dettaglio i **requisiti essenziali** (All. II) né i **moduli** (All. IV-VIII); non
  **individuare** le norme armonizzate; non **trattare** gli organismi notificati (artt. 20+).
- Non **sovrapporsi** a `dpi-protezione-individuale-dlgs81` (uso/scelta lato datore di lavoro).

### Cosa fare
- Fornire la classificazione in categoria, la procedura di conformità, gli obblighi documentali, la
  struttura della dichiarazione UE e le regole della marcatura CE, sempre con rinvio all'articolo/allegato.

## Aggiornamento delle fonti

DPI: se EUR-Lex pubblica una versione consolidata con modifiche rilevanti, riscaricare, ricalcolare l'hash
con doppio download e riallineare gli articoli. Verificare in particolare l'Allegato I (categorie) e l'art.
19 (procedure/moduli).

## Validatori

- Non ancora assegnato (Livello 2 con esperto di marcatura CE / DPI).

## Stato attuale

- Versione: 0.1.0-alpha (closes #388)
- Task files: 2 (`inquadra-categoria-procedura-dpi.md`,
  `inquadra-obblighi-dichiarazione-marcatura-dpi.md`)
- Esempi: 2 (imbracatura anticaduta - categoria III e procedura B+C2/D; guanti da giardinaggio - categoria I,
  dichiarazione UE e marcatura CE)
