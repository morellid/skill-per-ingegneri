# Task: Verifica ambito di applicazione del D.Lgs 35/2011

## Obiettivo

Stabilire se una determinata strada (in progettazione, in costruzione o gia' aperta al traffico) ricade nel campo di applicazione del D.Lgs 35/2011 nel testo modificato dal D.Lgs 213/2021. Senza questa verifica le altre sotto-attivita' della skill non hanno senso.

## Input richiesti

Per stabilire l'ambito chiedere all'utente:

1. **Tipologia di strada** secondo l'art. 2 del Codice della Strada (D.Lgs 285/1992): autostrada (tipo A), strada extraurbana principale (tipo B), strada extraurbana secondaria (tipo C), strada locale extraurbana (tipo F), strada urbana, ecc.
2. **Inclusione nella rete stradale transeuropea (TEN-T)**: SI / NO.
3. **Inclusione nell'elenco delle strade di interesse nazionale** ai sensi del D.Lgs 461/1999.
4. **Fase**: in progettazione, in costruzione, gia' aperta al traffico.
5. **Anno di apertura al traffico** (per individuare il regime transitorio).
6. **Finanziamento**: la strada o il progetto ha usufruito di finanziamenti UE (totali o parziali)? SI / NO.
7. **Localizzazione**: in area urbana o extraurbana?
8. **Esclusioni**: la strada e' una galleria stradale soggetta al D.Lgs 264/2006? E' una pista ciclabile? E' una strada non destinata al traffico generale (es. strada di accesso a siti industriali, agricoli, forestali)?

## Fonti

- Estratto del D.Lgs 35/2011 art. 1 (nuovo testo introdotto dall'art. 1 D.Lgs 213/2021): cfr. `references/estratti/dlgs-213-2021.md` sezione "Art. 1".
- Estratto del D.Lgs 35/2011 art. 2 (nuove definizioni: autostrada, strada principale, strade di interesse nazionale): cfr. `references/estratti/dlgs-213-2021.md` sezione "Art. 2".

## Procedura

Applicare nell'ordine i criteri di inclusione/esclusione del nuovo art. 1 D.Lgs 35/2011.

### Step 1 - Esclusioni preliminari

- Se la strada e' una galleria stradale soggetta al D.Lgs 264/2006: **fuori ambito** (art. 1, comma 7).
- Se la strada e' una pista ciclabile o altra strada non aperta al traffico automobilistico generale: **fuori ambito** (art. 1, comma 3, esclusioni).
- Se la strada e' di accesso a siti industriali, agricoli o forestali (non destinata al traffico generale): **fuori ambito** (art. 1, comma 3, esclusioni).

### Step 2 - Inclusione automatica (comma 2)

Se la strada rientra in uno dei seguenti casi, il decreto si applica sempre (in progettazione, in costruzione, gia' aperta al traffico):

- Parte della rete stradale transeuropea (TEN-T) come definita dal regolamento UE 1315/2013.
- **Autostrada** ai sensi dell'art. 2, comma 1, lettera a-bis del D.Lgs 35/2011 (strada appositamente progettata e costruita per il traffico motorizzato che non serve le proprieta' che la costeggiano e che soddisfa i tre criteri: carreggiate distinte separate da fascia divisoria, nessuna intersezione a raso, designazione specifica).
- **Strada principale** ai sensi dell'art. 2, comma 1, lettera a-ter del D.Lgs 35/2011 (strada situata al di fuori dell'area urbana che collega importanti citta' o regioni, classificata di tipo "B-Strade extraurbane principali" ai sensi dell'art. 2, comma 2 del Codice della Strada).

### Step 3 - Inclusione condizionata (comma 3)

Se la strada non rientra nel comma 2 ma:

- E' situata in area extraurbana, e
- Ha usufruito di finanziamenti UE (totali o parziali), e
- Non rientra nelle esclusioni (piste ciclabili, accessi a siti industriali/agricoli/forestali),

allora il decreto si applica.

### Step 4 - Inclusione differita (comma 4)

A decorrere dal **1 gennaio 2025**, il decreto si applica anche alle altre strade della **rete di interesse nazionale** (D.Lgs 461/1999), diverse da quelle gia' incluse ai commi 2 e 3, a prescindere dalla fase (progettazione, costruzione, esercizio).

### Step 5 - Strade di competenza regionale/locale (comma 6)

Entro il **31 dicembre 2024** le Regioni e Province autonome dovevano dettare la disciplina di gestione della sicurezza per le strade di propria competenza non gia' ricomprese nei commi 2 e 3. La verifica di applicabilita' su questi tratti dipende dal corrispondente atto regionale.

## Output

Risposta strutturata con queste sezioni:

1. **Esito**: la strada/il progetto rientra nel campo di applicazione del D.Lgs 35/2011 (SI / NO / SI dal 1/1/2025 / SI ma con regime regionale).
2. **Base normativa**: indicare il comma applicabile dell'art. 1 (es. "comma 2 - autostrada" oppure "comma 4 - rete di interesse nazionale dal 2025").
3. **Procedure che si applicano**: elencare quali tra VISS (art. 3), RSA (art. 4), NSA (art. 5 nuovo testo), ispezioni periodiche (art. 6) e ispezioni mirate (art. 6-bis) sono rilevanti in base alla fase del progetto/strada.
4. **Note transitorie**: se applicabile, segnalare scadenze (es. prima NSA entro il 2024 art. 5 comma 3; rendicontazione 31/10/2025 art. 9-bis).
5. **Rinvio professionista**: la verifica formale di inclusione nell'elenco delle strade trasmesso alla Commissione UE ai sensi dell'art. 1, comma 5 e' del MIMS.

## Limiti

- L'inclusione formale di una strada nell'elenco trasmesso alla Commissione UE (art. 1, comma 5 D.Lgs 35/2011) e' competenza del Ministero delle Infrastrutture e della Mobilita' Sostenibili: la skill non puo' consultare l'elenco ufficiale.
- La classificazione tecnica di tipo "B" ai sensi del Codice della Strada richiede una valutazione tecnica formale degli elementi geometrici, di accesso e di velocita' che esula dallo scopo di questa skill.
- Per le strade di competenza regionale/locale (art. 1, comma 6), la disciplina applicabile dipende dall'atto regionale di recepimento, che la skill non analizza.
