# Task: Redazione guidata del piano di lavoro amianto

Costruisce una **bozza strutturata** di piano di lavoro per demolizione o rimozione di amianto, allineata ai contenuti minimi dell'**art. 256 D.Lgs. 81/2008** e alle principali misure tecniche del **DM 6 settembre 1994**.

## Obiettivo

Produrre un documento in markdown pronto per revisione interna, con:

- tutte le voci minime dell'art. 256, comma 4;
- sezioni operative su lavoratori, DPI, decontaminazione, rifiuti e protezione terzi;
- campi `DA COMPLETARE` quando i dati non sono disponibili.

## Input richiesti

### Anagrafica del cantiere
- committente / sito / indirizzo
- impresa esecutrice
- referente tecnico
- organo di vigilanza competente, se noto

### Descrizione del materiale
- tipologia MCA
- ubicazione
- quantita' stimata
- compatto/friabile
- stato di conservazione

### Lavori previsti
- rimozione o demolizione
- data prevista inizio
- durata stimata
- eventuale urgenza
- tecnica prevista

### Lavoratori
- numero addetti
- nominativi o ruoli
- evidenza di formazione specifica
- sorveglianza sanitaria / medico competente

### Misure operative
- DPI previsti
- modalita' di confinamento o segregazione, se necessarie
- decontaminazione personale
- attrezzature e macchine
- pulizia finale e verifica assenza rischio
- raccolta, imballaggio e smaltimento materiali
- protezione di terzi e aree limitrofe

## Fonti

Leggere prima:

- `references/estratti/dlgs-213-2025-amianto-art-250-251-256-258-259.md`
- `references/estratti/dm-6-9-1994-amianto.md`

## Procedura

### Passo 1 - Prepara l'intestazione

Usa una struttura come questa:

```markdown
# Piano di lavoro per demolizione/rimozione amianto

**Riferimenti normativi**:
- art. 251 D.Lgs. 81/2008
- art. 256 D.Lgs. 81/2008
- art. 258 D.Lgs. 81/2008
- art. 259 D.Lgs. 81/2008
- DM 6 settembre 1994

**Versione bozza**: v0.1
**Data redazione**: [...]
**Stato**: bozza da verificare e firmare
```

### Passo 2 - Compila le sezioni obbligatorie dell'art. 256

La bozza deve coprire esplicitamente tutte queste voci:

| Riferimento | Contenuto da inserire |
|---|---|
| art. 256, c. 4, lett. a) | perche' la rimozione avviene prima della demolizione o perche' non e' possibile farlo |
| lett. b) | DPI forniti ai lavoratori |
| lett. c) | modalita' di verifica finale assenza rischio |
| lett. d) | protezione e decontaminazione del personale |
| lett. e) | protezione dei terzi e raccolta/smaltimento |
| lett. f) | misure rafforzate se prevedibile superamento valori limite |
| lett. g) | natura lavori, data inizio, durata |
| lett. h) | luogo di esecuzione |
| lett. i) | tecniche lavorative |
| lett. l) | attrezzature e dispositivi |

### Passo 3 - Integra le misure tecniche del DM 6/9/1994

Nella bozza inserisci almeno:

- caratterizzazione preliminare del materiale;
- valutazione sintetica del contesto (materiale, friabilita', ambiente aperto/chiuso);
- misure per evitare o ridurre la dispersione di fibre;
- organizzazione della decontaminazione;
- logica di scelta dei DPI respiratori;
- gestione degli indumenti e dei materiali contaminati;
- indicazioni su pulizia finale e condizioni per ripresa di altre attivita'.

### Passo 4 - Se mancano dati, non inventarli

Usa campi come:

- `DA CONFERMARE`
- `DA INTEGRARE CON SOPRALLUOGO`
- `DA DEFINIRE CON MEDICO COMPETENTE`
- `DA VERIFICARE SU PROCEDURA AZIENDALE / FORNITORE`

### Passo 5 - Chiudi con la sezione procedurale

Ricorda sempre nella bozza:

- invio almeno 30 giorni prima dell'inizio lavori, salvo urgenza motivata;
- indicazione separata di eventuali allegati;
- necessita' di revisione finale prima della trasmissione.

## Output

Il task produce un documento markdown strutturato come segue:

```markdown
# Piano di lavoro per demolizione/rimozione amianto

## 1. Dati generali
- [...]

## 2. Descrizione del materiale contenente amianto
- [...]

## 3. Natura dei lavori, durata e cronoprogramma
- [...]

## 4. Misure ex art. 256, comma 4
### a) Rimozione prima della demolizione
### b) DPI
### c) Verifica finale assenza rischio
### d) Protezione e decontaminazione del personale
### e) Protezione dei terzi e gestione materiali/rifiuti
### f) Misure rafforzate in caso di esposizione elevata
### g) Data inizio e durata
### h) Luogo di esecuzione
### i) Tecniche lavorative
### l) Attrezzature e dispositivi

## 5. Formazione e sorveglianza sanitaria
- [...]

## 6. Allegati da predisporre o verificare
- [...]

## 7. Avvertenza finale
Documento di supporto da verificare, completare e firmare prima della trasmissione.
```
