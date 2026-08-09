# CHANGELOG - esercizio-controllo-impianti-termici-dpr74

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0-alpha] - 2026-08-09

Trigger normativo: **D.Lgs. 9 gennaio 2026, n. 5** (attuazione della direttiva UE 2023/2413, RED
III), **GU Serie generale n. 15 del 20 gennaio 2026**. L'art. 29 include gli **interventi di
ristrutturazione dell'impianto termico** nel campo di applicazione dell'Allegato III del D.Lgs.
199/2021: la sostituzione del generatore non e' piu' automaticamente neutra sul piano degli obblighi
di integrazione delle fonti rinnovabili.

### Added (closes #488)
- Fonte scaricata, hashata e letta (Regola zero), con scopo deliberatamente ristretto:
  - **GU Serie generale n. 15 del 20 gennaio 2026** (PDF del fascicolo integrale)
    SHA256: 3d13cb9afa45d5c3f9c737e892f30af5ba7df08733bb891a9f51dd534d73c3a1
    (D.Lgs. 5/2026, codice redazionale 26G00018).
  - Trascrizione verbatim in `references/fonti/dlgs-5-2026-allegato-iii-estratto.md`: art. 29 c. 1
    lett. b) punto 2 (campo di applicazione, pag. GU 21), lett. c) punto 2 lett. d) (quota FER del
    15%, pag. GU 21) e Sezione D punto 1 dell'Allegato III risultante dalle "Note all'art. 29"
    (pag. GU 55).
  - **Scheda Normattiva del D.Lgs. 5/2026** pinnata `!vig=2026-08-09`
    SHA256: 1a67500175fe6f8a3d545212af0d3f0cb3c7f8d473c12ea7fada779b6245d831.
    Trascritta in `references/fonti/dlgs-5-2026-entrata-in-vigore.md` per la sola data di entrata
    in vigore ("Entrata in vigore del provvedimento: 04/02/2026"), che il PDF di Gazzetta non
    contiene.
- Nuova sezione "Avvertenza: la sostituzione del generatore puo' far scattare un obbligo FER" in
  `SKILL.md`, con rinvio esplicito a `relazione-tecnica-requisiti-minimi-dlgs192`.
- Nuova sezione 5-bis nell'estratto `references/estratti/impianti-termici-checklist.md`.

### Contenuto ancorato al testo
- Allegato III, **Sezione A punto 1**: il campo di applicazione include ora gli "edifici esistenti
  oggetto di interventi di ristrutturazione dell'impianto termico", per i quali la richiesta del
  titolo edilizio sia presentata decorsi 180 giorni dall'entrata in vigore del decreto.
- Allegato III, **Sezione B punto 1, lett. d)**: copertura del **15%** della somma dei consumi
  previsti per la climatizzazione invernale e la climatizzazione estiva.
- Allegato III, **Sezione D punto 1**: motivazione dell'impossibilita' tecnica o della non
  convenienza economica nella relazione ex art. 8 c. 1 del D.Lgs. 192/2005; **quando quella relazione
  non e' dovuta, comunicazione al Comune** secondo le modalita' da esso individuate. E' il punto che
  chiude il vuoto per la sostituzione del generatore sotto la soglia del DM 37/2008.

### Scope e limiti
- La skill **avverte e rinvia**: non calcola le quote di copertura, non tratta le altre categorie di
  intervento, non riproduce le Sezioni B punto 3, C ed E dell'Allegato III. Trattazione completa in
  `relazione-tecnica-requisiti-minimi-dlgs192` v0.2.0-alpha.
- La **qualificazione** dell'intervento come ristrutturazione dell'impianto termico resta rinviata al
  DM 26/6/2015 come modificato dal DM MASE 28/10/2025: e' un input, non un output.

### Note di sviluppo
- **Decorrenza da verificare**: il D.Lgs. 5/2026 non contiene un articolo di entrata in vigore
  (l'ultimo e' l'art. 51, clausola di invarianza finanziaria). La data non e' ricavabile dal PDF di
  Gazzetta ed e' quindi presa da una fonte dedicata, la scheda Normattiva dell'atto, che attesta
  l'entrata in vigore al 4 febbraio 2026: 180 giorni dopo cade il 3 agosto 2026. La formula "decorsi centottanta giorni dall'entrata in vigore del presente decreto"
  e' inserita dentro l'Allegato III del D.Lgs. 199/2021 ed e' testualmente ambigua: la skill segnala
  l'incertezza invece di risolverla d'ufficio.
- Noto per v0.3: valutare un esempio dedicato "sostituzione caldaia condominiale con verifica FER a
  monte" se la casistica si consolida; oggi l'esempio equivalente vive nella skill
  `relazione-tecnica-requisiti-minimi-dlgs192`
  (`examples/obblighi-fer-sostituzione-generatore/`), che e' la sede della trattazione completa.

## [0.1.0-alpha] - 2026-07-16

### Added (closes #255)
- Prima versione della skill di supporto ai criteri di **esercizio, conduzione, controllo e
  manutenzione** degli **impianti termici** per la climatizzazione, ai sensi del **D.P.R. 16
  aprile 2013, n. 74**, nell'area `energia-incentivi`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.P.R. 16 aprile 2013, n. 74** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: 13aa0ad0fb0edbe235455d2b79f2173ec2dc3dff8c28abc5b606e9d4cb8e32f5 (codice 13G00114).
    Artt. 3, 4, 5, 6, 7, 8 via `caricaArticolo`, trascritti verbatim in
    `references/fonti/dpr-74-2013.md`.
- Estratto operativo `references/estratti/impianti-termici-checklist.md`.
- Due task: `verifica-limiti-esercizio.md` e `imposta-controllo-manutenzione.md`.
- Due esempi: riscaldamento in zona climatica E (temperatura e periodi/orari); terzo
  responsabile in unita' residenziale singola vs condominio.

### Contenuto ancorato al testo
- Temperature massime (art. 3: 18C+2 industriale / 20C+2 altri; estiva >= 26C-2); limiti di
  esercizio per zona climatica A-F (art. 4) e ordinanze del sindaco (art. 5); responsabile e
  terzo responsabile con limiti alla delega (art. 6); controllo e manutenzione da ditte abilitate
  DM 37/2008 (art. 7); controllo di efficienza energetica per impianti > 10/12 kW con RCEE (art. 8).

### Scope e limiti
- Non riproduce i **modelli RCEE** (Allegato A, in formato tabellare) ne' il **libretto di
  impianto** (DM 10/2/2014). Non esegue il controllo/manutenzione ne' redige il RCEE. Non copre
  la disciplina regionale di dettaglio (periodicita', catasto impianti, bollino). Complementare a
  `trasmittanza-termica-opache-dm2015` e `diagnosi-energetica-dlgs102`.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.P.R. 74/2013 pinnato (nuovo hash);
  verificare il DM 10/2/2014 e la disciplina regionale.
- Validazione Livello 2 con termotecnico / manutentore abilitato.
