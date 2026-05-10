# Task: Verifica conformita' matrice criteri OEPV

Analizza una matrice criteri/sottocriteri contenuta nel disciplinare di gara e verifica la conformita' all'art. 108 D.Lgs. 36/2023, segnalando le criticita' che possono esporre la procedura a ricorso TAR/Consiglio di Stato.

## Obiettivo

Produrre un report strutturato che indichi, per ciascun aspetto della matrice:
- **Esito**: conforme / non conforme / da chiarire / rischio ricorso
- **Riferimento normativo** preciso (art. e comma)
- **Problema rilevato** e motivazione
- **Raccomandazione** per correggere o mitigare

## Input richiesti

1. **Testo della matrice criteri** come appare nel disciplinare di gara (criteri, sottocriteri, pesi, metodi di valutazione)
2. **Tipo di contratto**: lavori / servizi / forniture
3. **Oggetto e importo a base d'asta** (EUR)
4. **Informazioni aggiuntive opzionali**:
   - Se e' specificato il metodo di riproporzionamento
   - Se e' specificata la formula per l'offerta economica
   - Se sono indicati i descrittori per i criteri discrezionali
   - Se e' menzionato il bonus parita' di genere

## Fonti normative

Leggere prima di procedere:
- `references/estratti/dlgs-36-art107-108.md`
- `references/estratti/dlgs-36-art93.md`
- `references/estratti/anac-lg-n2-metodologia-oepv.md`

## Procedura

### Passo 1 - Verifica obblighi formali dell'art. 108

Controllare sistematicamente:

| Requisito | Riferimento | Da verificare |
|-----------|-------------|---------------|
| OEPV obbligatorio (se applicabile) | Art. 108 co. 2 | Il contratto rientra nelle categorie obbligatorie? Se si', e' stato scelto OEPV? |
| Criterio non ammesso (prezzo piu' basso su servizi alta intensita' manodopera) | Art. 108 co. 3 | Se il contratto e' ad alta intensita' manodopera, il criterio non puo' essere solo il prezzo |
| Pesi indicati per ogni criterio | Art. 108 co. 7 | Ogni criterio ha un peso numerico? I pesi sommano a 100? |
| Subcriteri e sub-pesi (se presenti) | Art. 108 co. 7 | I sottocriteri hanno pesi coerenti con il criterio padre? |
| Limite punteggio economico 10% (IT strategico) | Art. 108 co. 4 | Il contratto e' IT interesse nazionale? Il punteggio economico e' <= 10%? |
| Limite punteggio economico 30% (alta intensita' manodopera) | Art. 108 co. 4 | Il contratto e' ad alta intensita' manodopera? Il punteggio economico e' <= 30%? |
| Criterio parita' di genere previsto | Art. 108 co. 7 + D.Lgs. 198/2006 art. 46-bis | La SA ha previsto il maggior punteggio per le imprese con requisiti art. 46-bis D.Lgs. 198/2006? Questo e' l'UNICO criterio esplicitamente obbligatorio nel co. 7. |
| Criteri premiali facoltativi (welfare, CO2) | Art. 108 co. 7 (facoltativo) | Se inclusi, sono collegati all'oggetto (art. 108 co. 6)? Se non inclusi, non e' una non-conformita' normativa (sono facoltativi). |
| Formula offerta economica specificata | Art. 108 co. 7 + giurisprudenza | La formula e' esplicitata nel disciplinare o solo "formula proporzionale" generico? |
| Metodo riproporzionamento specificato | ANAC LG n.2 + giurisprudenza | E' indicato se si applica il riproporzionamento per i criteri discrezionali? |
| Criteri collegati all'oggetto del contratto | Art. 108 co. 6 | Tutti i criteri sono pertinenti all'appalto? Nessun criterio soggettivo sull'operatore? |
| Nessun punto per opere extra rispetto al progetto (lavori) | Art. 108 co. 11 | Per lavori: nessun criterio premia opere aggiuntive non previste nel progetto a base di gara |

### Passo 2 - Verifica qualita' dei criteri discrezionali

I criteri discrezionali sono la fonte principale di ricorsi TAR. Verificare:

1. **Descrittori presenti**: il disciplinare deve descrivere cosa la commissione valuta per quel criterio, non solo il nome del criterio. Un criterio chiamato "qualita' tecnica" senza descrittori e' **a rischio alto**
2. **Verificabilita' nell'offerta**: il criterio deve essere valutabile sulla base dell'offerta tecnica presentata, non su elementi extra-gara
3. **Non duplicazione**: due criteri che valutano la stessa cosa con nomi diversi espongono a contestazione
4. **Proporzionalita' dei pesi**: un peso molto alto su un unico criterio discrezionale vago concentra il rischio

Indicatori di rischio per criteri discrezionali:
- "Qualita' dell'offerta" senza descrittori -> **rischio alto**
- "Esperienza pregressa" come criterio discrezionale invece che tabellare -> **rischio medio** (preferibile tabellare)
- "Solidita' economica dell'impresa" come criterio tecnico -> **non conforme** (art. 108 co. 6: solo criteri collegati all'oggetto)
- "Referenze su contratti simili" come criterio tecnico -> **non conforme** se non collegato a caratteristiche dell'offerta (confonde requisiti di partecipazione con valutazione offerta)

### Passo 3 - Verifica della formula offerta economica

La formula economica deve essere esplicitata nel disciplinare. Formule accettabili:

**Formula lineare** (piu' comune, TAR-stabile):
- Pe_i = Vmax × (Prezzomin / Prezzo_i)
- Interpretazione: offerta piu' bassa = Vmax; le altre proporzionalmente meno

**Formula bilineare con soglia di anomalia** (rara, sconsigliata per semplicita'):
- Complessa, rischio di incomprensione da parte degli offerenti
- Da evitare salvo casi specifici motivati

**Problemi frequenti**:
- "Punteggio proporzionale al ribasso offerto" senza formula specifica: **da chiarire** (vago)
- "Interpolazione lineare" senza esplicitare Rmax o Prezzomin: **rischio medio** (ambiguo)
- Nessuna formula indicata: **non conforme** (gli offerenti non possono verificare il calcolo)

### Passo 4 - Output

```markdown
# Verifica conformita' matrice criteri OEPV
**Gara**: [oggetto]
**Tipo contratto**: [lavori/servizi/forniture]
**Importo**: EUR [importo]
**Data verifica**: [data]

---

## Esito complessivo: [CONFORME / CONFORME CON RISERVA / NON CONFORME / RISCHIO ALTO]

[Sintesi dei problemi principali trovati o assenza di problemi]

---

## Verifica requisiti formali art. 108

| Requisito | Esito | Riferimento | Note |
|-----------|-------|-------------|------|
| OEPV obbligatorio / applicato correttamente | CONFORME/NON CONFORME | Art. 108 co. 2 | ... |
| Pesi indicati e sommano a 100 | ... | Art. 108 co. 7 | ... |
| Limite punteggio economico rispettato | ... | Art. 108 co. 4 | ... |
| Criterio parita' di genere (obbligatorio) presente | ... | Art. 108 co. 7 + D.Lgs. 198/2006 art. 46-bis | ... |
| Formula economica esplicitata | ... | Art. 108 co. 7 | ... |
| Criteri collegati all'oggetto | ... | Art. 108 co. 6 | ... |

---

## Analisi criteri per criterio

| Criterio | Peso | Metodo | Esito | Criticita' | Priorita' |
|----------|------|--------|-------|------------|-----------|
| [nome] | XX | Discrezionale | CONFORME/RISCHIO | [problema] | Alta/Media/Bassa |
| ... | | | | | |

---

## Problemi rilevati (prioritizzati)

### Priorita' ALTA (possono determinare annullamento del bando o della procedura)

**1. [problema]**
[Descrizione dettagliata, riferimento normativo, giurisprudenza pertinente se disponibile]
Azione correttiva: [cosa fare]

### Priorita' MEDIA (riducono la qualita' della gara o espongono a contestazione)

**2. [problema]**
...

### Priorita' BASSA (best practice non seguite, rischio contenuto)

**3. [problema]**
...

---

## Raccomandazioni finali

1. [Raccomandazione sintetica]
2. ...

---

## Avvertenze

- Questa verifica e' basata sul testo della matrice fornita; non sostituisce la revisione legale del disciplinare completo
- La giurisprudenza TAR/CdS in materia OEPV e' in evoluzione: le raccomandazioni si basano sulle massime consolidate alla data di redazione
- In caso di gara sopra soglia europea con criteri tecnici complessi, si raccomanda parere legale preventivo
```

## Principali motivi di ricorso TAR su gare OEPV (da conoscere)

1. **Criteri discrezionali troppo vaghi**: la commissione non ha parametri per valutare; l'esito appare arbitrario (Cons. Stato, sez. V, costante giurisprudenza)
2. **Subcriteri non pubblicati nel bando/disciplinare**: se vengono introdotti criteri di valutazione dopo l'apertura delle offerte, la gara e' illegittima
3. **Formula economica non esplicitata**: l'offerente non puo' verificare il calcolo del proprio punteggio
4. **Riproporzionamento non dichiarato**: se la commissione applica il riproporzionamento senza averlo dichiarato nel disciplinare, il risultato e' contestabile
5. **Commissario incompatibile**: mancata dichiarazione assenza cause di esclusione (art. 93 D.Lgs. 36/2023)
6. **Punteggio economico sproporzionato**: anche senza limite esplicito (tranne IT e manodopera), un peso economico del 70-80% sulla qualita'/prezzo non e' proporzionato per servizi tecnici e puo' essere impugnato
7. **Criteri su caratteristiche del soggetto invece che dell'offerta**: l'art. 108 co. 6 vieta criteri che valutano l'impresa (solidita' finanziaria, referenze) come criteri di aggiudicazione (appartengono ai requisiti di partecipazione)
8. **Punti per lavori aggiuntivi (lavori)**: art. 108 co. 11 vieta i punti per varianti o opere non previste nel progetto a base di gara

## Casi limite da gestire

### Gara con un solo offerente ammesso
Segnalare che in caso di offerta unica il riproporzionamento assegna comunque V=1 a quell'offerente per tutti i criteri discrezionali. Non e' un errore della matrice, ma un esito possibile.

### Matrice molto semplice (1-2 criteri)
Non e' illegale, ma per contratti complessi una matrice con pochi criteri puo' non valorizzare adeguatamente la qualita' e puo' essere impugnata per "motivazione insufficiente della scelta della ponderazione". Suggerire maggiore articolazione.

### Pesi con range (es. "tra 20 e 30 punti")
L'art. 108 co. 7 ammette pesi con range (min/max), purche' il gap sia "adeguato". Se il range e' molto ampio (es. 10-50 punti per lo stesso criterio), segnalare come rischio di contestazione per eccessiva discrezionalita'.

### Criteri ambientali CAM come criterio premiante
Ammissibile e anzi consigliato (coerente con art. 57 D.Lgs. 36/2023 sui CAM). Verificare pero' che i criteri CAM premianti siano aggiuntivi rispetto ai criteri CAM obbligatori del DM 256/2022 e non ne duplichino il contenuto.

## Limiti di questo task

- La verifica si basa sul testo della matrice fornita; non analizza l'intero disciplinare di gara
- Non sostituisce la revisione legale in caso di gare di importo rilevante o ad alto rischio
- La giurisprudenza TAR/CdS e' in evoluzione: la skill riporta i principi consolidati, non le sentenze piu' recenti
- Non valuta la coerenza tra i criteri e il capitolato tecnico della gara specifica

## Esempi

Vedi `examples/`:
- `non-conforme-matrice-lavori/` - matrice per appalto lavori con criteri vaghi e formula economica assente
