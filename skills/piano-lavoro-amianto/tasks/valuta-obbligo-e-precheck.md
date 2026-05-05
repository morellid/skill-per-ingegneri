# Task: Valuta obbligo e precheck del piano di lavoro amianto

Stabilisce se il caso rientra nel perimetro del **piano di lavoro ex art. 256 D.Lgs. 81/2008** e costruisce la lista minima di dati da raccogliere prima della redazione.

## Obiettivo

Restituire un esito chiaro tra:

- `Piano art. 256 richiesto`
- `Caso preliminare da approfondire`
- `Fuori perimetro di questa skill`

insieme ai dati mancanti, ai prerequisiti di impresa/lavoratori e alla timeline minima di invio.

## Input richiesti

1. Descrizione dell'intervento.
2. Luogo dei lavori.
3. Tipo di materiale contenente amianto, se noto.
4. Stato del materiale: compatto/friabile, integro/degradato, interno/esterno.
5. Attivita' prevista: rimozione, demolizione, incapsulamento, confinamento, manutenzione, campionamento, bonifica, smaltimento.
6. Impresa esecutrice e numero lavoratori coinvolti.
7. Eventuale urgenza.
8. Eventuali dati gia' disponibili su formazione, visite mediche, DPI, decontaminazione, gestione rifiuti.

## Fonti

Leggere prima:

- `references/estratti/dlgs-213-2025-amianto-art-250-251-256-258-259.md`
- `references/estratti/dm-6-9-1994-amianto.md`

## Procedura

### Passo 1 - Classifica il perimetro

Usa questo schema:

| Caso | Esito |
|---|---|
| Demolizione o rimozione di amianto/MCA da edificio, struttura, apparecchio, impianto o mezzo di trasporto | `Piano art. 256 richiesto` |
| Attivita' con esposizione ad amianto ma non chiaramente demolizione/rimozione | `Caso preliminare da approfondire` |
| Richiesta di solo censimento, campionamento o parere astratto senza dati di cantiere | `Fuori perimetro di questa skill` |

Se il caso e' dubbio, non forzare la conclusione.

### Passo 2 - Verifica i prerequisiti minimi

Controlla se sono almeno dichiarati:

- impresa incaricata;
- lavoratori coinvolti;
- esistenza di formazione specifica ai sensi dell'art. 258;
- sorveglianza sanitaria ai sensi dell'art. 259;
- impostazione preliminare di DPI, decontaminazione e gestione rifiuti.

Se mancano questi elementi, segnala che il piano puo' essere solo **bozza incompleta**.

### Passo 3 - Chiarisci il rapporto tra art. 250 e art. 256

- Se l'esito e' `Piano art. 256 richiesto`, ricorda che:
  - il piano va inviato all'organo di vigilanza almeno **30 giorni prima** dell'inizio dei lavori;
  - nei casi di urgenza va esplicitata la motivazione e vanno indicati **data e orario di inizio**;
  - l'invio del piano **sostituisce** gli adempimenti dell'art. 250.
- Se non sei nel perimetro art. 256 ma c'e' esposizione ad amianto, segnala che l'utente deve verificare separatamente gli obblighi dell'art. 250.

### Passo 4 - Precheck tecnico

Elenca come `Mancante` o `Disponibile` almeno questi dati:

- localizzazione precisa del cantiere;
- tipo di MCA e quantita' presunta;
- natura dei lavori e durata;
- tecnica di intervento prevista;
- numero lavoratori e turnazione;
- misure per protezione e decontaminazione del personale;
- misure per protezione dei terzi;
- gestione materiali rimossi e rifiuti;
- caratteristiche di attrezzature/dispositivi;
- eventuale necessita' di ambienti confinati o chiusi.

## Output

```markdown
# Precheck piano di lavoro amianto

**Esito**: [Piano art. 256 richiesto | Caso preliminare da approfondire | Fuori perimetro di questa skill]
**Motivazione**: [...]
**Riferimenti principali**: [art. 250 / art. 256 / DM 6 settembre 1994]

## 1. Classificazione del caso
- Tipo intervento: [...]
- Materiale: [...]
- Ambiente: [...]
- Motivo dell'esito: [...]

## 2. Prerequisiti
| Voce | Stato | Note |
|---|---|---|
| Impresa esecutrice | [...] | [...] |
| Formazione lavoratori | [...] | [...] |
| Sorveglianza sanitaria | [...] | [...] |
| DPI respiratori | [...] | [...] |
| Decontaminazione | [...] | [...] |

## 3. Dati da raccogliere prima della redazione
- [...]

## 4. Timeline procedurale
- [...]

## 5. Avvertenza professionale
L'esito e' preliminare e non sostituisce la verifica del professionista responsabile prima della trasmissione all'organo di vigilanza.
```
