# Task: Verifica completezza voci Allegato XV

Verifica che il POS fornito contenga tutte le voci obbligatorie previste dal punto 3.2.1 dell'Allegato XV del D.Lgs. 81/2008 e s.m.i.

## Obiettivo

Produrre un report strutturato che indichi per ciascuna voce obbligatoria se e' presente, assente o inadeguata, con citazione normativa precisa per ogni carenza rilevata.

## Input richiesti

- Testo completo del POS in forma leggibile (markdown, testo, estratto PDF)
- Opzionali:
  - Natura del cantiere (edilizia civile, ristrutturazione, demolizione, scavi, ...)
  - Tipologia impresa (affidataria/esecutrice/subappaltatrice)
  - Dimensione impresa (familiare, < 10 addetti, > 10 addetti)
  - Presenza/assenza del PSC (cambia l'articolazione di alcune voci del POS)

Se l'input e' solo parziale (es. estratto di alcune sezioni), segnalarlo nel report e specificare che la verifica e' limitata a cio' che e' stato fornito.

## Fonti normative

Leggere prima di procedere:
- `references/estratti/allegato-xv-testo.md` punto 3.2.1 (contenuti obbligatori POS)
- `references/estratti/dlgs-81-art-96-97.md` (obbligo di redazione e verifica congruenza)

## Procedura

### Passo 1 - Parsing del POS

Leggere il POS e identificare le sezioni. I POS italiani seguono spesso intestazioni simili a:
- "Dati impresa" / "Anagrafica impresa" / "Identificazione impresa"
- "Organigramma sicurezza"
- "Descrizione attivita'"
- "Attrezzature e opere provvisionali"
- "Sostanze pericolose"
- "Rumore" / "Valutazione rumore"
- "Misure di prevenzione e protezione"
- "Procedure"
- "DPI"
- "Formazione e informazione"

Mappare ciascuna sezione del POS alla voce corrispondente dell'Allegato XV punto 3.2.1.

### Passo 2 - Verifica delle 10 voci obbligatorie

Per ciascuna delle voci a) - l) del punto 3.2.1, verificare:

#### Voce a) Dati identificativi dell'impresa esecutrice

Deve contenere tutti e 7 i sotto-punti:
1. Nominativo datore di lavoro, indirizzi e riferimenti telefonici sede legale e uffici cantiere
2. Specifica attivita' e singole lavorazioni svolte in cantiere dall'impresa esecutrice e lavoratori autonomi subaffidatari
3. Nominativi addetti pronto soccorso, antincendio, evacuazione, gestione emergenze; RLS o RLST
4. Nominativo medico competente ove previsto
5. Nominativo RSPP
6. Nominativi direttore tecnico di cantiere e capocantiere
7. Numero e qualifiche lavoratori dipendenti e autonomi

Classificare **ogni sotto-punto** come `presente`, `assente`, `inadeguato`.

#### Voce b) Specifiche mansioni di sicurezza

Le mansioni inerenti la sicurezza di ogni figura nominata devono essere descritte, non solo elencate. Un semplice elenco nomi-ruolo senza specifica delle mansioni di sicurezza specifiche e' **inadeguato**.

#### Voce c) Descrizione attivita' di cantiere, modalita' organizzative e turni

Il POS deve descrivere cosa fara' l'impresa, come, quando. Turni di lavoro se applicabili (cantieri notturni, festivi, a piu' turni).

#### Voce d) Elenco ponteggi, ponti su ruote a torre, opere provvisionali di notevole importanza, macchine, impianti

Elenco **concreto** di cio' che sara' usato in cantiere. Se il POS contiene solo formule generiche ("saranno utilizzate le attrezzature previste dal PSC") senza elenco specifico, classificare come `inadeguato`.

#### Voce e) Sostanze e miscele pericolose + schede di sicurezza

Se il POS cita sostanze pericolose, devono essere **allegate le schede di sicurezza** (SDS). Se dichiara "nessuna sostanza pericolosa", verificare plausibilita' rispetto alla natura del cantiere.

#### Voce f) Esito valutazione rumore

Puo' essere:
- Rinvio al DVR aziendale se disponibile
- Valutazione specifica per il cantiere se le condizioni lo richiedono
- Dichiarazione di classi di rischio (inferiore/superiore a 80 dB(A), 85 dB(A))

#### Voce g) Misure preventive e protettive **integrative** rispetto al PSC

Nota chiave: le misure del POS sono **integrative** al PSC, non duplicative. Se il POS copia/incolla le misure del PSC senza aggiungere specificita' rispetto alle proprie lavorazioni, segnalare come `potenzialmente inadeguato`.

#### Voce h) Procedure complementari e di dettaglio richieste dal PSC

Presente solo quando il PSC esplicitamente richiede procedure dettagliate. Se il PSC non le richiede, voce non obbligatoria (marcarla come `non-applicabile`). Se il PSC le richiede e il POS non le contiene, classificare `assente - non conforme`.

#### Voce i) Elenco DPI

Elenco concreto dei DPI forniti ai lavoratori. Generico "saranno forniti i DPI previsti dalla normativa" e' `inadeguato`. Devono essere elencati per tipologia di rischio/lavorazione.

#### Voce l) Documentazione informazione e formazione

Documentazione che l'informazione e formazione ex art. 36-37 D.Lgs. 81/2008 e' stata erogata ai lavoratori occupati in cantiere. Puo' essere sotto forma di attestati, registri, dichiarazione.

### Passo 3 - Casi particolari

- **Mere forniture**: art. 96 co. 1-bis esenta le "mere forniture di materiali o attrezzature" dalla redazione POS. Se il POS e' stato redatto ma l'attivita' descritta e' una mera fornitura, segnalare l'incoerenza. In tali casi si applica l'art. 26 (cooperazione e coordinamento).
- **Cantieri senza PSC**: se non esiste PSC (lavori edilizi con unica impresa e fuori campo PSS), le voci g) e h) del POS che rinviano al PSC diventano autosufficienti.
- **Sottoappalti**: se il POS copre attivita' subappaltate, ciascun subappaltatore dovrebbe avere proprio POS. Verificare se il POS fornito include correttamente subappaltatori o se ne mancano.

### Passo 4 - Generazione output

Produrre un report markdown nel formato seguente:

```markdown
# Verifica completezza POS - Allegato XV punto 3.2.1

**Data verifica**: [data]
**POS analizzato**: [identificativo se fornito]
**Contesto cantiere**: [se dichiarato]

## Esito sintetico

[CONFORME | CONFORME CON NOTE MINORI | INCOMPLETO | NON CONFORME]

Voci presenti: X/10
Voci con sotto-punti completi: Y/Z (per la voce a con 7 sotto-punti)

## Dettaglio per voce

### a) Dati identificativi dell'impresa esecutrice
- [ ] 1. Nominativo DdL, indirizzi e riferimenti: [presente/assente/inadeguato - motivo]
- [ ] 2. Attivita' e lavorazioni specifiche: ...
- [ ] 3. Addetti PS/AI/emergenze + RLS: ...
- [ ] 4. Medico competente: ...
- [ ] 5. RSPP: ...
- [ ] 6. Direttore tecnico e capocantiere: ...
- [ ] 7. Numero e qualifiche lavoratori: ...

### b) Specifiche mansioni di sicurezza
[esito]

[... continua per c) - l) ...]

## Problemi rilevati

| # | Voce | Problema | Riferimento normativo | Priorita' |
|---|------|----------|----------------------|-----------|
| 1 | a.4 | Nominativo medico competente assente, ma l'impresa dichiara oltre X lavoratori soggetti a sorveglianza sanitaria | Allegato XV 3.2.1 a.4, art. 41 D.Lgs. 81 | Alta |
| ... |

## Raccomandazioni

- Integrare la voce X con [...]
- Chiarire se [...]
- ...

## Limiti di questa verifica

- Verifica su documento, non su cantiere
- Non verifica la correttezza delle dichiarazioni (es. effettiva nomina e formazione dei soggetti citati)
- Non giudica adeguatezza tecnica delle misure specifiche rispetto al cantiere reale
- La sanzione di cui all'art. 159 co. 1 (ammenda 2.847,69 - 5.695,36 euro per POS con elementi Allegato XV mancanti) e' citata come riferimento di severita', non come quantificazione applicabile al caso specifico

## Rinvio al professionista firmatario

**La presente verifica non sostituisce la revisione del CSE o del datore di lavoro firmatario del POS.** La responsabilita' finale sulla conformita' e adeguatezza del piano resta al professionista firmatario.
```

## Casi limite da gestire

### POS incompleto per mancata estrazione
Se il parsing del POS e' difficoltoso (formato strano, testo illeggibile, sezioni mancanti perche' non fornite), dichiararlo esplicitamente nel report e limitare la verifica a cio' che e' leggibile.

### POS troppo generico
Se il POS e' formalmente completo ma pieno di formule generiche (classico "copia-incolla boilerplate"), segnalarlo ma non classificarlo come `incompleto` sulla base di questa sola evidenza. Suggerire verifica di dominio.

### Riferimenti normativi obsoleti
Se il POS cita il D.Lgs. 163/2006 (Codice Appalti abrogato), segnalarlo come bandiera rossa sul fatto che il POS potrebbe essere datato e necessitare di revisione generale.

## Limiti di questo task

- Verifica **formale** sulla presenza delle voci, non sulla loro adeguatezza tecnica rispetto al cantiere specifico
- Non valuta l'effettiva applicabilita' delle misure descritte (e' compito di check-coerenza-rischi per il matching, ma l'adeguatezza assoluta richiede giudizio di dominio)
- Non sostituisce l'analisi del cantiere fisico ne' la valutazione del CSE
- Non verifica l'autenticita' delle firme, delle nomine, dei CV delle figure citate

## Esempi

Vedi `examples/` per:
- `conforme-cantiere-piccolo/`: POS ben redatto per impresa edile piccola
- `incompleto-voci-mancanti/`: POS con 3-4 voci assenti
- (opzionali) `borderline-boilerplate/`: POS formalmente completo ma generico
