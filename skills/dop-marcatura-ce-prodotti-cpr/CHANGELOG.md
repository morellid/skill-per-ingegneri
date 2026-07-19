# CHANGELOG - dop-marcatura-ce-prodotti-cpr

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-19

### Added (closes #386)
- Prima versione della skill di supporto al **fabbricante / ufficio tecnico-qualità** per l'**inquadramento
  della redazione della Dichiarazione di Prestazione (DoP)** e dell'**apposizione della marcatura CE** dei
  **prodotti da costruzione** secondo il **Regolamento (UE) n. 305/2011 (CPR)**, nell'area
  `impianti-macchine-prodotti`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **Regolamento (UE) n. 305/2011 (CPR)** - GU UE L 88 del 4.4.2011 - testo EUR-Lex (CELEX 32011R0305) -
    SHA256: 2e98d2f0db29719ba516ca4e1fe2e6a99a4665c402c1049e0b8d382a9657e966 (doppio download riproducibile).
  - Articoli e allegati rilevanti estratti con `pdftotext -layout` e trascritti verbatim in
    `references/fonti/reg-ue-305-2011-cpr.md` (artt. 4-16, Allegati III e V).
- Estratto operativo `references/estratti/dop-marcatura-ce-checklist.md`.
- Due task: `inquadra-contenuto-dop.md` e `inquadra-marcatura-ce-vvcp.md`.
- Due esempi: contenuto della DoP e uso della sigla NPD per un aggregato coperto da norma armonizzata;
  sistema VVCP 2+ e contenuto della marcatura CE.

### Contenuto ancorato al testo
- Obbligo di redigere la DoP quando il prodotto rientra in una norma armonizzata o ha una valutazione
  tecnica europea, e le deroghe (esemplare unico o su ordinazione non in serie, fabbricazione in cantiere,
  metodi tradizionali/conservazione del patrimonio) (artt. 4-5). Contenuto della DoP (prodotto-tipo,
  sistema/i VVCP dell'Allegato V, norma armonizzata/ETA, uso previsto, caratteristiche essenziali,
  prestazione in livelli/classi/descrizione, sigla NPD per le caratteristiche non dichiarate), informazioni
  REACH e fornitura cartacea/elettronica/sito web (artt. 6-7). Regole della marcatura CE: marcatura apposta
  solo se redatta la DoP, marcatura unica di conformità, ed elementi che la seguono (anno, fabbricante,
  codice prodotto-tipo, numero DoP, livello/classe, specifica tecnica armonizzata, numero organismo
  notificato, uso previsto) (artt. 8-9). Sistemi di valutazione e verifica della costanza della prestazione
  (VVCP) 1+/1/2+/3/4 con i compiti del fabbricante, del controllo della produzione in fabbrica e
  dell'organismo notificato (Allegato V). Obblighi degli operatori economici: fabbricante con documentazione
  tecnica conservata 10 anni, mandatario che non redige la documentazione tecnica, importatore, distributore
  e la regola dell'art. 15 (chi immette col proprio nome/marchio o modifica il prodotto assume gli obblighi
  del fabbricante) (artt. 11-16). Modello di DoP dell'Allegato III.

### Scope e limiti
- Non redige la DoP al posto dell'operatore, non individua la norma armonizzata applicabile né il sistema
  VVCP del singolo prodotto (dipendono dalla hEN o dalla decisione della Commissione), non esegue prove né
  valutazioni, non tratta in dettaglio la valutazione tecnica europea (ETA, artt. 19-27) né gli organismi
  notificati (artt. 39-56), non riproduce il modello di DoP aggiornato dal Reg. delegato (UE) 574/2014. Non
  sostituisce la norma armonizzata di prodotto né il fabbricante.

### Note di sviluppo
- Appartiene al gruppo "marcatura CE / conformità dei prodotti" del repo, distinto dalle direttive di
  prodotto (macchine, elettrici, dispositivi medici, attrezzature a pressione). Validazione Livello 2 con
  esperto di marcatura CE dei prodotti da costruzione.
