# CHANGELOG - marcatura-ce-dpi-reg-425

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-19

### Added (closes #388)
- Prima versione della skill di supporto al **fabbricante / ufficio tecnico** per l'**inquadramento della
  classificazione, della valutazione della conformità e della marcatura CE** dei **dispositivi di
  protezione individuale (DPI)** come prodotti secondo il **Regolamento (UE) 2016/425**, nell'area
  `impianti-macchine-prodotti`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **Regolamento (UE) 2016/425 (DPI)** - GU UE L 81 del 31.3.2016 - testo EUR-Lex (CELEX 32016R0425) -
    SHA256: 8b4c61bb477557b572b4794f58702d4523ed72058e94311e3e7158aaad95f67d (doppio download riproducibile).
  - Articoli e allegati rilevanti estratti con `pdftotext -layout` e trascritti verbatim in
    `references/fonti/reg-ue-2016-425-dpi.md` (artt. 8-9, 15, 16-18, 19, Allegati I e IX).
- Estratto operativo `references/estratti/marcatura-ce-dpi-checklist.md`.
- Due task: `inquadra-categoria-procedura-dpi.md` e `inquadra-obblighi-dichiarazione-marcatura-dpi.md`.
- Due esempi: imbracatura anticaduta (categoria III, procedura B + C2/D con organismo notificato); guanti da
  giardinaggio (categoria I, modulo A, dichiarazione UE e marcatura CE senza organismo notificato).

### Contenuto ancorato al testo
- Obblighi del fabbricante (progettazione secondo i requisiti essenziali di salute e sicurezza dell'Allegato
  II, documentazione tecnica dell'Allegato III, procedura di conformità dell'art. 19, dichiarazione UE,
  marcatura CE, conservazione decennale, identificazione e istruzioni) e del mandatario (artt. 8-9).
  Dichiarazione di conformità UE con la struttura tipo dell'Allegato IX (art. 15). Principi e regole di
  apposizione della marcatura CE, con il numero dell'organismo notificato per la categoria III (artt.
  16-17). Classificazione dei DPI nelle categorie di rischio I (rischi minimi: lesioni meccaniche
  superficiali, prodotti di pulizia poco aggressivi/acqua, superfici calde <= 50 gradi, luce solare,
  condizioni atmosferiche non estreme), II (rischi diversi da I e III) e III (rischi gravissimi: sostanze/
  miscele pericolose, carenza di ossigeno, agenti biologici, radiazioni ionizzanti, alta temperatura >= 100
  gradi, bassa temperatura <= -50 gradi, cadute dall'alto, scosse elettriche/lavoro sotto tensione,
  annegamento, tagli da seghe a catena, getti ad alta pressione, ferite da proiettile/coltello, rumore
  nocivo) dell'Allegato I (art. 18). Procedure di valutazione della conformità per categoria (art. 19):
  categoria I modulo A (All. IV); categoria II modulo B (All. V) + modulo C (All. VI); categoria III modulo
  B + modulo C2 (All. VII) o modulo D (All. VIII), con deroga per i DPI su misura di categoria III.

### Scope e limiti
- Non progetta né certifica il DPI, non esegue le prove né l'esame UE del tipo, non riproduce in dettaglio i
  requisiti essenziali dell'Allegato II né i moduli degli Allegati IV-VIII, non individua le norme
  armonizzate applicabili, non tratta gli organismi notificati (artt. 20+). Non sostituisce l'organismo
  notificato né il fabbricante. È distinta da `dpi-protezione-individuale-dlgs81` (uso/scelta lato datore di
  lavoro, D.Lgs 81/2008 artt. 74-79).

### Note di sviluppo
- Appartiene al gruppo "marcatura CE / conformità dei prodotti" del repo, complementare (lato prodotto) alla
  skill sull'uso dei DPI. Validazione Livello 2 con esperto di marcatura CE dei DPI.
