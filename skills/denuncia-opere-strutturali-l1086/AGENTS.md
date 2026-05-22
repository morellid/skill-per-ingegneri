# AGENTS.md - denuncia-opere-strutturali-l1086

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

La skill copre gli adempimenti procedurali strutturali e sismici del DPR
380/2001 per interventi edilizi in Italia: denuncia opere in c.a./c.a.p./
metalliche (art. 65), collaudo statico (art. 67), preavviso, autorizzazione
preventiva e classificazione interventi in zona sismica (artt. 83, 93, 94,
94-bis). Target: ingegnere strutturista, direttore dei lavori, costruttore.

## Fonti autoritative

- **DPR 6 giugno 2001 n. 380** (testo multivigente Normattiva al 2026-05-22) -
  id `dpr-380-2001-testo-unico-edilizia` in `references/sources.yaml`,
  sha256 `6ab58aead12307a5fa6d4da6cafaf0c0976c7ec3470a9ff4eedab81b60d1224c`.

Trascrizione fedele: `references/fonti/dpr-380-2001-testo-unico-edilizia.md`.

Estratti operativi:
- `references/estratti/dpr-380-art-65-denuncia-ca.md` - denuncia c.a./c.a.p./
  metalliche.
- `references/estratti/dpr-380-art-67-collaudo.md` - collaudo statico.
- `references/estratti/dpr-380-artt-93-94-94bis-zone-sismiche.md` - artt. 83,
  93, 94, 94-bis (zona sismica).

## Articoli e punti chiave

- **Art. 65 c. 1**: la denuncia e' del costruttore, prima dell'inizio dei lavori,
  via PEC o portale telematico, allo sportello unico.
- **Art. 65 c. 3**: gli allegati obbligatori sono progetto firmato dal
  progettista + relazione illustrativa firmata da progettista e direttore lavori.
- **Art. 65 c. 5**: le varianti vanno denunciate prima dell'esecuzione, con la
  stessa forma e gli stessi allegati.
- **Art. 65 c. 6**: relazione a struttura ultimata entro 60 giorni, depositata
  dal DL, allegati cert. prove materiali, indicazioni c.a.p., esiti prove di
  carico.
- **Art. 65 c. 8-bis**: esclusione dei commi 6-7-8 per gli interventi b.2
  (riparazioni / interventi locali su esistenti) e c.1 (privi di rilevanza) di
  art. 94-bis comma 1.
- **Art. 67 c. 2**: collaudatore ingegnere o architetto iscritto albo da almeno
  10 anni, non intervenuto in progettazione/direzione/esecuzione.
- **Art. 67 c. 5**: il collaudatore ha 60 giorni dalla comunicazione di
  completamento copertura.
- **Art. 67 c. 8-bis e 8-ter**: dichiarazione di regolare esecuzione del DL al
  posto del certificato di collaudo per riparazioni/interventi locali (8-bis) e
  per gli interventi b.2 e c.1 di art. 94-bis (8-ter).
- **Art. 83**: ambito Capo IV. Zone sismiche definite dai decreti del MIT
  (comma 2) e individuate dalle regioni (comma 3).
- **Art. 93 c. 1-4**: preavviso scritto al SUE in zona sismica + progetto in
  doppio esemplare + asseverazione progettista (NTC, coerenza, prescrizioni
  sismiche urbanistiche).
- **Art. 93 c. 5**: il preavviso ex art. 93 vale anche come denuncia ex art. 65
  (pratica unica).
- **Art. 94 c. 2 e 2-bis**: 30 giorni per autorizzazione UTR, silenzio assenso
  trascorso il termine; attestazione su richiesta entro 15 giorni.
- **Art. 94-bis c. 1 lett. a)**: interventi rilevanti (a.1 adeguamento/
  miglioramento in zona 1 e zona 2 con ag 0,20-0,25 g; a.2 nuove costruzioni
  che si discostano dalle usuali tipologie, escluse zone 3 e 4; a.3 edifici
  strategici, escluse zone 3 e 4).
- **Art. 94-bis c. 1 lett. b)**: interventi di minore rilevanza (b.1 adeguamento/
  miglioramento in zona 2 con ag 0,15-0,20 g e zona 3; b.2 riparazioni e
  interventi locali; b.3 nuove costruzioni che non rientrano in a.2; b.3-bis
  presenza occasionale persone / edifici agricoli punto 2.4.2 NTC 2018).
- **Art. 94-bis c. 1 lett. c)**: interventi privi di rilevanza (c.1).
- **Art. 94-bis c. 3**: autorizzazione preventiva obbligatoria per gli interventi
  rilevanti.
- **Art. 94-bis c. 4**: autorizzazione preventiva non dovuta per minore
  rilevanza e privi di rilevanza.

## Convenzioni specifiche

### Cosa NON fare

- Non scegliere la classificazione ex art. 94-bis al posto del progettista
  strutturale. La qualificazione di "intervento locale", "riparazione",
  "miglioramento", "adeguamento", "usuale tipologia" e "particolare complessita'
  strutturale" e' un giudizio tecnico delle NTC 2018, non procedurale.
- Non confondere zone sismiche e valori di `ag`: l'art. 94-bis usa due soglie
  dentro la zona 2 (0,15-0,20 g e 0,20-0,25 g) che fanno scattare
  classificazioni diverse.
- Non suggerire di presentare due pratiche separate (art. 65 + art. 93) in zona
  sismica: il comma 5 dell'art. 93 stabilisce che il preavviso vale anche come
  denuncia.
- Non promettere che il silenzio assenso ex art. 94 c. 2-bis vale sempre: per
  edifici strategici le regioni possono aver introdotto limitazioni.
- Non interpretare l'elencazione operativa ex art. 94-bis c. 2 senza riferimento
  all'atto regionale specifico vigente nel comune di intervento.

### Cosa fare

- Citare sempre l'**articolo, comma e lettera** del DPR 380 a fondamento di
  ogni indicazione (es. "art. 94-bis comma 1 lett. a) n. 1", non "art. 94-bis"
  da solo).
- Rinviare alla disciplina regionale per la classificazione operativa
  art. 94-bis comma 2.
- Rinviare al progettista strutturale firmatario per ogni qualificazione
  tecnica NTC (adeguamento, miglioramento, intervento locale, usuale tipologia).
- Concludere ogni output con la sezione "Avvertenze" che richiama la
  responsabilita' del professionista firmatario e i limiti di scope della skill.
- In zona sismica, indicare sempre il canale **unico** (SUE -> UTR) e ricordare
  che il preavviso ex art. 93 assorbe la denuncia ex art. 65.

## Validatori

(Nessun validatore di Livello 2 identificato per la v0.1.0-alpha. La skill
attende un ingegnere strutturista con esperienza in pratiche genio civile per
la promozione a stable.)

## Stato attuale

- Versione: 0.1.0-alpha (vedi `CHANGELOG.md`).
- Validazione: Livello 1 (source-grounded sul DPR 380 Normattiva).
- Task files: 4 (`diagnosi-adempimenti-struttura.md`,
  `checklist-denuncia-art-65.md`, `checklist-zona-sismica-art-93-94.md`,
  `checklist-collaudo-art-67.md`).
- Esempi: 1 conforme (`villetta-ca-zona-3-conforme/`) + 1 problematico
  (`scuola-zona-2-problema-classificazione/`).
