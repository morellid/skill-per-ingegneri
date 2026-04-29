# Task: Genera checklist elaborati PFTE

Produce la lista strutturata degli elaborati obbligatori per un PFTE, con citazione precisa di articolo e lettera dell'Allegato I.7 D.Lgs. 36/2023, in funzione delle variabili di inquadramento dell'opera.

## Obiettivo

Restituire all'utente:
- Una **checklist** ordinata di tutti gli elaborati che devono comporre il PFTE per la sua opera specifica.
- Per ciascun elaborato: la **citazione normativa** (Allegato I.7 art. X co. Y lett. Z), la **obbligatorieta'** (sempre / condizionale), la **condizione di applicabilita'** (se condizionale), un eventuale rinvio all'articolo dell'Allegato I.7 che descrive i contenuti minimi.
- Un set di **avvertenze** sui documenti pre-progettuali (DOCFAP, DIP, quadro esigenziale) e sugli elaborati aggiuntivi richiesti per appalto integrato.

## Input richiesti

Variabili minime da raccogliere all'inizio (chiedere all'utente se non fornite):

1. **Categoria intervento**:
   - nuova costruzione
   - manutenzione ordinaria
   - manutenzione straordinaria
   - restauro / risanamento conservativo
   - ristrutturazione
   - lavori su beni culturali (D.Lgs. 42/2004)
   - altro (specificare)

2. **Importo lavori** (stima, in EUR): rilevante per il DOCFAP - obbligatorio sopra soglia europea (rinvio dinamico ad art. 14 D.Lgs. 36/2023), facoltativo per importi 150.001 EUR - soglia europea (Allegato I.7 art. 2 co. 5-6).

3. **Procedure espropriative necessarie**: si / no.

4. **Soggezione a VIA / VAS / verifica di assoggettabilita'**: si (VIA dovuta), no, in screening (verifica di assoggettabilita' in corso o conclusa), dubbio. La lett. d (SIA) si attiva solo se l'opera e' effettivamente soggetta a VIA: lo screening con esito "no VIA" non attiva lett. d. La lett. s (monitoraggio ambientale) si attiva solo per opere soggette a VIA o quando la SA lo richieda espressamente.

5. **BIM applicabile** (art. 43 D.Lgs. 36/2023): si / no.
   - Soglie indicative (DM 312/2021 e successivi aggiornamenti): obbligo per opere sopra soglie variabili nel tempo. Se l'utente non sa, chiedere se la stazione appaltante ha incluso il BIM nel DIP.

6. **Modalita' di affidamento prevista**:
   - PFTE come base di gara (appalto integrato) -> elaborati aggiuntivi (art. 21 Allegato I.7)
   - Esecutivo come base di gara -> PFTE puo' essere meno dettagliato
   - PPP / concessione / project financing -> art. 6-bis Allegato I.7 + piano economico-finanziario

7. **Regime manutenzione** (solo se categoria 1 e' manutenzione):
   - art. 41 co. 5 (omissione PFTE, esecutivo arricchito)
   - art. 41 co. 5-bis (affidamento su PFTE senza esecutivo - correttivo 2024)
   - PFTE + esecutivo entrambi (regime ordinario)

8. **Verifica preventiva interesse archeologico applicabile**: si / no / da valutare.

Se l'utente fornisce solo input parziali, **procedi con la checklist** generando un albero a piu' rami che evidenzi i punti dipendenti dalle variabili mancanti, e segnala in chiaro quali voci possono attivarsi/disattivarsi.

## Fonti normative

Leggere prima di procedere:
- `references/estratti/dlgs-36-art-41.md` - testo strutturato art. 41
- `references/estratti/allegato-i7-pfte.md` - struttura completa Allegato I.7 + elenco art. 6 co. 7
- `references/estratti/dlgs-209-2024-modifiche.md` - modifiche del correttivo

## Procedura

### Passo 1 - Inquadramento opera

Riassumi all'utente cio' che hai capito dell'opera:

> "Sto generando la checklist PFTE per: [tipologia], importo [X EUR], espropri [si/no], VIA [si/no], BIM [si/no], modalita' [appalto integrato / esecutivo base di gara]. Confermi?"

Se l'utente conferma, procedi. Se corregge, aggiorna l'inquadramento.

### Passo 2 - Documenti pre-progettuali

Indica nella prima sezione della checklist se servono documenti che **precedono** il PFTE:

| Doc | Quando obbligatorio | Riferimento |
|-----|---------------------|-------------|
| Quadro esigenziale | Sempre prima del PFTE | All. I.7 art. 1 |
| DOCFAP | Obbligatorio sopra soglia europea (art. 14 D.Lgs. 36/2023). Facoltativo (a discrezione SA) per importi 150.001 EUR - soglia europea | All. I.7 art. 2 co. 5-6 |
| DIP | Sempre, redatto dal RUP, prima dell'avvio della progettazione | All. I.7 art. 3 |

Se il DOCFAP e' obbligatorio per l'opera in esame, segnalarlo come **prerequisito** e ricordare che il PFTE recepisce le scelte fatte nel DOCFAP.

### Passo 3 - Elaborati PFTE (art. 6 co. 7)

Genera la checklist degli elaborati nell'ordine delle lettere a-t. Per ogni voce indica:
- **Lettera** della norma (a, b, c, ...)
- **Nome elaborato**
- **Articolo Allegato I.7** dove e' descritto il contenuto minimo
- **Obbligatorieta'**: sempre / condizionale (se condizionale, specifica la condizione)
- **Stato per l'opera in esame** in base alle variabili: required / non-applicabile / da-valutare

Tabella di riferimento (vedi `allegato-i7-pfte.md` per il dettaglio):

| Lett. | Elaborato | Articolo | Quando obbligatorio |
|-------|-----------|----------|---------------------|
| a | Relazione generale | 7 | Sempre |
| b | Relazione tecnica con indagini, accertamenti, rilievi e studi specialistici | 8 | Sempre |
| c | Relazione di verifica preventiva interesse archeologico | 9 | Quando applicabile (Allegato I.8) |
| d | Studio di impatto ambientale (SIA) | 10 | Solo se opera soggetta a VIA (lo screening con esito negativo NON attiva la lett. d) |
| e | Relazione di sostenibilita' dell'opera | 11 | Sempre |
| f | Rilievi plano-altimetrici e studio di consistenza | (in art. 6) | Sempre |
| g | Modelli informativi + relazione specialistica modellazione | 13, 13-bis | Se BIM (art. 43) |
| h | Elaborati grafici delle opere | 12 | Sempre |
| i | Computo estimativo dell'opera (calcolo sommario) | 16 | Sempre |
| l | Quadro economico di progetto | 5, 17 | Sempre |
| m | Piano economico-finanziario di massima | (in art. 6) | Solo PPP / concessione / project financing |
| n | Cronoprogramma | 18 | Sempre |
| o | Piano di sicurezza e coordinamento (PSC) | 15 | Sempre quando applicabili presupposti D.Lgs. 81/2008 |
| p | Capitolato informativo | 13-ter | Solo se appalto integrato + BIM |
| q | Piano preliminare di manutenzione | 19 | Sempre |
| r | Piano preliminare monitoraggio geotecnico e strutturale | (in art. 8) | Sempre |
| s | Piano preliminare monitoraggio ambientale | (in art. 8) | Solo per opere soggette a VIA o quando la stazione appaltante lo richieda |
| t | Piano particellare di esproprio preliminare | 20 | Solo se necessarie procedure espropriative |

> **Numerazione legale**: le lettere j, k, w, x, y sono omesse per convenzione legislativa italiana.

### Passo 4 - Elaborati aggiuntivi per appalto integrato

Se la modalita' di affidamento e' **appalto integrato** (PFTE base di gara), aggiungere:

- **Disciplinare descrittivo e prestazionale** (art. 14) sviluppato a livello idoneo all'aggiudicazione
- **PSC** (art. 15) sviluppato in modo da consentire la quantificazione dei costi della sicurezza non ribassabili
- **Capitolato informativo** (art. 13-ter) se BIM si applica
- **Schema di contratto** (richiamato in art. 21)

Riferimento: Allegato I.7 art. 21.

### Passo 5 - Manutenzioni - regimi alternativi

Se categoria 1 = manutenzione ordinaria/straordinaria, distinguere:

**Caso A - regime ex art. 41 co. 5** (omissione PFTE, esecutivo arricchito):
- Non si redige PFTE separato.
- L'esecutivo deve contenere tutti gli elementi che sarebbero stati nel PFTE omesso.

**Caso B - regime ex art. 41 co. 5-bis** (correttivo 2024, affidamento su PFTE):
- Si redige solo il PFTE (no esecutivo).
- **Eccezione**: NON applicabile a manutenzione straordinaria con **rinnovo o sostituzione di parti strutturali dell'opera o di impianti** (per tali interventi resta richiesto l'esecutivo).
- L'**Allegato I.7 art. 6 co. 8-bis** prescrive il set **minimo obbligatorio**:
  1. **Relazione generale** (art. 7)
  2. **Computo metrico estimativo**
  3. **Elenco prezzi unitari**
  4. **Piano di sicurezza e coordinamento** (art. 15)
- Tutti gli altri elaborati a-t sono **non obbligatori** in questo regime, salvo che la specificita' dell'opera o il DIP del RUP lo richieda. Lo standard professionale tende a includere anche **cronoprogramma** (n) e **descrizione tecnica** dell'opera per consentire all'aggiudicatario l'esecuzione.

**Caso C - regime ordinario** (PFTE + esecutivo): applica la checklist piena.

Chiedere esplicitamente all'utente quale regime e' applicabile - non scegliere tu.

### Passo 6 - Output

Produrre il report nel formato:

```markdown
# Checklist elaborati PFTE - art. 41 + Allegato I.7 D.Lgs. 36/2023

**Data**: [oggi]
**Inquadramento intervento**:
- Categoria: [...]
- Importo stimato: [...]
- Espropri: [...]
- VIA: [...]
- BIM: [...]
- Modalita' affidamento: [...]
- Regime manutenzione (se applicabile): [...]

## 0. Documenti pre-progettuali

| Doc | Stato | Riferimento |
|-----|-------|-------------|
| Quadro esigenziale | Required | All. I.7 art. 1 |
| DOCFAP | [Required / Non-applicabile] | All. I.7 art. 2 |
| DIP (RUP) | Required | All. I.7 art. 3 |

## 1. Elaborati PFTE (art. 6 co. 7)

| Lett. | Elaborato | Stato | Articolo dettaglio | Note |
|-------|-----------|-------|--------------------|----|
| a | Relazione generale | Required | All. I.7 art. 7 | |
| b | Relazione tecnica + indagini | Required | All. I.7 art. 8 | |
| c | Verifica preventiva archeologica | [Required / Non-applicabile / Da-valutare] | All. I.7 art. 9 | Vedi All. I.8 per modalita' |
| d | Studio di impatto ambientale | [Required / Non-applicabile] | All. I.7 art. 10 | Solo se opera soggetta a VIA |
| ... | ... | ... | ... | ... |

## 2. Elaborati aggiuntivi (se appalto integrato)

[se applicabile]

## 3. Elementi non valutabili automaticamente dalla skill

- Adeguatezza tecnica del contenuto degli elaborati (giudizio del progettista)
- Conformita' a norme di settore non incluse nel Codice (NTC, antincendio, accessibilita', acustica, energia)
- Coerenza con il DIP redatto dal RUP (la skill non legge il DIP)
- Soglie di obbligo BIM aggiornate al momento del bando

## 4. Avvertenze e rinvio professionale

- L'elenco e' generato sulla base delle variabili dichiarate; verificare con il **RUP** che il DIP confermi l'inquadramento.
- Per opere su **beni culturali** (D.Lgs. 42/2004) puo' essere richiesta documentazione aggiuntiva non coperta dall'Allegato I.7.
- Per **opere strategiche** ex L. 443/2001 e disposizioni speciali, valutare regimi specifici.
- L'output non sostituisce la **verifica della progettazione ex art. 42** del Codice ne' il giudizio del progettista firmatario.

**La presente checklist e' uno strumento di supporto e non sostituisce il giudizio professionale.**
```

## Casi limite da gestire

### Importo borderline soglia europea
Se l'utente dichiara un importo molto vicino alla soglia europea per i lavori (rinvio dinamico ad art. 14 D.Lgs. 36/2023), **segnalare** che la soglia e' aggiornata ogni due anni da regolamento delegato UE e che il DOCFAP, se non obbligatorio, resta **comunque richiedibile** dalla SA per importi 150.001 EUR - soglia europea (Allegato I.7 art. 2 co. 6: "ove la stazione appaltante ne ravvisi la necessita'").

### BIM non chiaro
Se l'utente non sa se il BIM e' applicabile, chiedere:
- "Il DIP cita la gestione informativa digitale o l'art. 43 del Codice?"
- "L'opera supera le soglie di obbligo BIM previste dai DM attuativi vigenti?"
Se rimane incerto, marcare gli elaborati BIM (g, p) come `Da-valutare con RUP` invece di forzare una scelta.

### Mix manutenzione + adeguamento
Se l'intervento mescola manutenzione e adeguamento sismico/funzionale, non e' "pura manutenzione": applicare il regime ordinario (Caso C) e segnalare che la classificazione finale spetta al RUP.

### Opera in variante urbanistica
Ricordare l'art. 41 co. 7: il PFTE sostituisce preliminare + definitivo. Tipicamente impone elaborati piu' completi su rilievi, vincoli, espropri.

## Limiti di questo task

- Genera la **lista degli elaborati**, non i contenuti tecnici.
- Non valuta se l'importo dichiarato e' realistico (e' input dell'utente).
- Non integra automaticamente la **modulistica regionale** o disposizioni di stazioni appaltanti specifiche (es. ANAS, RFI, Provveditorato).
- Non sostituisce il **DIP** redatto dal RUP, che e' la fonte primaria di prescrizione degli elaborati per il caso concreto.

## Esempi

Vedi `examples/`:
- `conforme-nuova-costruzione/` - checklist completa per nuova scuola con espropri
- `manutenzione-straordinaria-incompleto/` - manutenzione con elaborati mancanti
