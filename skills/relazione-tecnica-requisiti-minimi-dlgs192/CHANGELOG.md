# CHANGELOG - relazione-tecnica-requisiti-minimi-dlgs192

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0-alpha] - 2026-08-09

Trigger normativo: **D.Lgs. 9 gennaio 2026, n. 5** (attuazione della direttiva UE 2023/2413, RED
III), pubblicato in **GU Serie generale n. 15 del 20 gennaio 2026**, che con gli artt. 29-30 modifica
gli Allegati III e IV del D.Lgs. 8 novembre 2021, n. 199. Rileva per questa skill perche' l'Allegato
III stabilisce che calcoli, verifiche e motivazioni di deroga sugli obblighi FER si scrivono **dentro
la relazione tecnica ex art. 8, c. 1, del D.Lgs. 192/2005**.

### Added (closes #488)
- Fonte scaricata, hashata e letta (Regola zero):
  - **GU Serie generale n. 15 del 20 gennaio 2026** (PDF del fascicolo integrale, 121 pagine)
    SHA256: 3d13cb9afa45d5c3f9c737e892f30af5ba7df08733bb891a9f51dd534d73c3a1
    (D.Lgs. 5/2026, codice redazionale 26G00018).
  - Trascrizione verbatim in `references/fonti/dlgs-5-2026-allegato-iii.md`: art. 29 (pagg. GU
    21-22), incipit dell'art. 30 (pag. GU 22) e testo risultante dell'Allegato III dalle "Note
    all'art. 29" (pagg. GU 54-55).
  - **Scheda Normattiva del D.Lgs. 5/2026** pinnata `!vig=2026-08-09`
    SHA256: 1a67500175fe6f8a3d545212af0d3f0cb3c7f8d473c12ea7fada779b6245d831.
    Trascritta in `references/fonti/dlgs-5-2026-entrata-in-vigore.md` per la sola data di entrata
    in vigore ("Entrata in vigore del provvedimento: 04/02/2026"), che il PDF di Gazzetta non
    contiene: senza questa fonte la data sarebbe un'affermazione normativa non ancorata.
- Estratto operativo `references/estratti/obblighi-fer-allegato-iii.md`.
- Nuovo task `tasks/verifica-obblighi-fer-edifici.md`.
- Nuova sezione "Obblighi FER negli edifici" in `SKILL.md`, con rimando incrociato dall'estratto
  `relazione-tecnica-checklist.md` (sezione 2) per distinguere la valutazione di fattibilita' dei
  sistemi alternativi del c. 1-bis, che **non** assolve gli obblighi FER, dagli obblighi quantitativi
  dell'Allegato III.

### Contenuto ancorato al testo
- Ambito esteso: entrano esplicitamente le **ristrutturazioni importanti di secondo livello** e le
  **ristrutturazioni dell'impianto termico** (Allegato III, Sezione A punto 1).
- Quote di copertura FER (Sezione B punto 1): nuova costruzione 60% ACS **e** 60% della somma
  ACS + climatizzazione invernale + estiva; ristrutturazione importante di primo livello 40% e 40%
  sulle stesse basi; ristrutturazione importante di secondo livello 15% della somma climatizzazione
  invernale + estiva; ristrutturazione dell'impianto termico 15% sulla stessa base.
- Edifici pubblici: +5 punti percentuali sulle quote e +10% sulla potenza elettrica (punto 5).
- Deroga al divieto di effetto Joule per unita' immobiliari in classe energetica B o superiore
  (punto 2).
- Potenza elettrica FER con k = 0,025 (edifici esistenti) e k = 0,05 (nuova costruzione) sulla
  superficie in pianta al netto delle pertinenze (punto 3).
- Esonero per allaccio a teleriscaldamento/teleraffrescamento efficiente a copertura integrale
  (punto 4).
- Impossibilita' tecnica o non convenienza economica da motivare nella relazione ex art. 8 c. 1
  esaminando tutte le opzioni tecnologiche; comunicazione al Comune quando la relazione non e' dovuta;
  obbligo compensativo su EP H,C,W,nren limitato a edifici nuovi e ristrutturazioni importanti di
  primo livello, con efficienze di Tabella 1 (1,54 clim. invernale; 1,28 clim. estiva; 1,28 ACS)
  (Sezione D).
- Verifica dei Comuni sulla relazione e trasmissione di copia al GSE (Sezione E).

### Scope e limiti
- La **qualificazione** dell'intervento (primo/secondo livello, ristrutturazione dell'impianto
  termico) resta rinviata al DM 26/6/2015 come modificato dal DM MASE 28/10/2025: e' un input, non un
  output della skill.
- Non riprodotti: Allegato II del D.Lgs. 199/2021 (requisiti e specifiche tecniche degli impianti),
  resto dell'Allegato IV (requisiti minimi di prodotto), linee guida CTI previste dalla Sezione C
  punto 4.
- La **formula** della potenza elettrica FER (Sezione B punto 3) e' pubblicata come **immagine** nel
  PDF di Gazzetta e non e' estraibile come testo: la skill riporta i soli parametri descritti a parole
  nella fonte e rinvia alla lettura dell'originale.

### Note di sviluppo
- **Decorrenza da verificare**: il D.Lgs. 5/2026 non contiene un articolo di entrata in vigore
  (l'ultimo e' l'art. 51, clausola di invarianza finanziaria). La data non e' ricavabile dal PDF di
  Gazzetta ed e' quindi presa da una fonte dedicata, la scheda Normattiva dell'atto, che attesta
  l'entrata in vigore al 4 febbraio 2026: 180 giorni dopo cade il 3 agosto 2026. La formula
  "decorsi centottanta giorni dall'entrata in vigore del presente decreto"
  e' pero' collocata dentro l'Allegato III del D.Lgs. 199/2021 ed e' testualmente ambigua: la skill
  segnala l'incertezza invece di risolverla d'ufficio. Riverificare all'emanazione di eventuali
  chiarimenti MASE.
- La Sezione B punto 6 prevede la rideterminazione almeno quinquennale degli obblighi a decorrere dal
  1° gennaio 2026: pianificare la riverifica.
- Noto per v0.3: aggiungere un esempio dedicato al caso "ristrutturazione dell'impianto termico con
  obbligo FER 15%" quando saranno disponibili le linee guida CTI con i calcoli numerici.

## [0.1.0-alpha] - 2026-07-17

### Added (closes #346)
- Prima versione della skill di supporto al **tecnico** (progettista, direttore dei lavori) per la
  **relazione tecnica di progetto attestante la rispondenza ai requisiti minimi energetici** (la
  "relazione ex legge 10"), ai sensi del **D.Lgs. 19 agosto 2005, n. 192, art. 8** (con l'art. 15
  cc. 1, 3, 4), nell'area `energia-incentivi`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 192/2005** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: bfaa533634a0bcd106b0a5d52d07b1a6f841b7c85960a8de069eeef0c952741d
    (codice 005G0219). Artt. 8 (versione 5, idGruppo 1) e 15 (versione 4, idGruppo 3) via
    `caricaArticolo` (formato AKN).
  - Trascrizione verbatim in `references/fonti/dlgs-192-2005-art8-15.md` (art. 8 per intero; art. 15
    cc. 1, 3, 4).
- Estratto operativo `references/estratti/relazione-tecnica-checklist.md`.
- Due task: `inquadra-relazione-deposito.md` e `inquadra-asseverazione-sanzioni.md`.
- Due esempi: relazione per nuova costruzione con sistemi alternativi ed esclusione PdC 12 kW; fine
  lavori senza asseverazione (inefficacia, sanzione al DL, controlli del Comune).

### Contenuto ancorato al testo
- Relazione redatta dai progettisti e depositata dal proprietario in doppia copia con la DIA/titolo
  abilitativo, con esclusioni (PdC <= 15 kW; sostituzione generatore sotto soglia DM 37/2008) - art.
  8 c. 1; valutazione di fattibilità dei sistemi alternativi ad alta efficienza per nuove
  costruzioni/ristrutturazioni importanti - c. 1-bis; asseverazione di conformità e AQE del direttore
  dei lavori a fine lavori, pena l'inefficacia della fine lavori - c. 2; conservazione, accertamenti
  e ispezioni del Comune in corso d'opera o entro 5 anni - cc. 3-5; dichiarazione sostitutiva di atto
  notorio - art. 15 c. 1; sanzione professionista 700-4200 euro - c. 3; sanzione direttore dei lavori
  1000-6000 euro - c. 4.

### Scope e limiti
- Non redige la relazione né esegue i calcoli/verifiche (rinvio a `trasmittanza-termica-opache-dm2015`
  e al DM 26/6/2015), non riproduce gli schemi di relazione del decreto MiSE, non copre l'APE (art. 6,
  skill `attestato-prestazione-energetica-dlgs192`) né i commi 2 e 5-10 dell'art. 15. Non sostituisce
  il progettista/direttore dei lavori.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 192/2005 pinnato (nuovo hash) e
  verificare le modifiche (es. D.Lgs. 48/2020) e l'evoluzione del decreto attuativo MiSE.
- Validazione Livello 2 con termotecnico / certificatore energetico.
