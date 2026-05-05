# Task: Verifica di un piano di lavoro amianto esistente

Controlla completezza, coerenza normativa e principali lacune operative di un piano di lavoro amianto gia' scritto.

## Obiettivo

Restituire:

- elenco delle carenze formali rispetto all'art. 256;
- incoerenze rispetto ad art. 251, 258, 259 e DM 6/9/1994;
- priorita' di correzione (`Critica`, `Alta`, `Media`);
- sintesi finale su trasmissibilita' del piano.

## Input richiesti

1. Testo del piano o sezioni rilevanti.
2. Eventuali allegati gia' presenti.
3. Dati minimi del cantiere, se non contenuti nel piano.
4. Eventuale indicazione di urgenza.

## Fonti

Leggere prima:

- `references/estratti/dlgs-213-2025-amianto-art-250-251-256-258-259.md`
- `references/estratti/dm-6-9-1994-amianto.md`

## Procedura

### Passo 1 - Verifica il perimetro

Se il documento non riguarda demolizione o rimozione di amianto/MCA, segnala subito che la verifica art. 256 e' solo parziale o non pertinente.

### Passo 2 - Checklist minima art. 256

Controlla una per una le voci dell'art. 256, comma 4:

| Voce | Domanda |
|---|---|
| lett. a) | Spiega la rimozione prima della demolizione o la relativa eccezione? |
| lett. b) | Elenca DPI idonei? |
| lett. c) | Prevede come si verifica l'assenza di rischio prima della ripresa di altre attivita'? |
| lett. d) | Descrive protezione e decontaminazione del personale? |
| lett. e) | Descrive protezione terzi e raccolta/smaltimento? |
| lett. f) | Gestisce l'ipotesi di superamento dei valori limite, se pertinente? |
| lett. g) | Indica natura lavori, data inizio e durata? |
| lett. h) | Indica il luogo dei lavori? |
| lett. i) | Descrive le tecniche lavorative? |
| lett. l) | Indica attrezzature e dispositivi? |

### Passo 3 - Controlli di coerenza

Verifica se il piano e' coerente con:

- **art. 251**: riduzione esposizione, DPI respiratori, decontaminazione, ambiente chiuso;
- **art. 258**: formazione dichiarata in modo credibile;
- **art. 259**: sorveglianza sanitaria richiamata;
- **DM 6/9/1994**: tecnica di bonifica coerente con materiale e contesto, gestione indumenti contaminati, procedure di pulizia e decontaminazione.

Esempi di finding:

- materiale dichiarato friabile ma tecnica descritta come se fosse compatto;
- ambiente chiuso senza adeguata gestione di segregazione/protezione;
- DPI citati in modo generico senza alcun criterio o senza coerenza con le lavorazioni;
- assenza di procedura di decontaminazione;
- assenza di protezione dei terzi o di gestione dei rifiuti.

### Passo 4 - Timeline procedurale

Controlla se il piano:

- prevede invio almeno 30 giorni prima dell'inizio lavori;
- oppure, nei casi di urgenza, motiva correttamente l'urgenza e indica **data e orario di inizio**;
- evita di duplicare/confondere la notifica art. 250 quando e' gia' nel perimetro art. 256.

## Output

```markdown
# Verifica piano di lavoro amianto

**Esito sintetico**: [Adeguato | Integrabile | Critico]
**Perimetro**: [...]

## 1. Carenze art. 256
| Priorita' | Riferimento | Carenza | Azione richiesta |
|---|---|---|---|

## 2. Incoerenze tecnico-operative
| Priorita' | Fonte | Osservazione | Azione richiesta |
|---|---|---|---|

## 3. Dati mancanti
- [...]

## 4. Valutazione finale
- [...]

## 5. Avvertenza professionale
La verifica e' documentale e non sostituisce controllo tecnico, sopralluogo e validazione del professionista responsabile.
```
