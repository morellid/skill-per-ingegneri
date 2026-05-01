# Task: Costruzione matrice criteri/sottocriteri OEPV

Guida il RUP o la stazione appaltante nella costruzione di una matrice di valutazione conforme all'art. 108 D.Lgs. 36/2023, con criteri, sottocriteri, pesi e metodo di valutazione appropriati all'oggetto del contratto.

## Obiettivo

Produrre una **bozza di matrice criteri/sottocriteri** che possa essere integrata nel disciplinare di gara, comprendente:
- Elenco criteri con peso (ponderazione) e metodo di valutazione
- Eventuale suddivisione in sottocriteri con peso parziale
- Metodo di attribuzione del punteggio per ciascun criterio/sottocriterio (tabellare, discrezionale, formula)
- Note sulle vincoli normativi applicabili (limiti punteggio economico, OEPV obbligatorio, criteri premianti obbligatori art. 108 co. 7)

## Input richiesti

1. **Tipo di contratto**: lavori / servizi / forniture
2. **Oggetto sintetico**: descrizione dell'appalto (es. "servizi di architettura e ingegneria per ristrutturazione scuola", "appalto integrato per nuova palestra comunale")
3. **Importo a base d'asta** (EUR, IVA esclusa)
4. **Criterio di aggiudicazione gia' scelto** (OEPV qualita'/prezzo oppure OEPV costo/efficacia oppure da verificare)
5. **Aspetti qualitativi prioritari** che il committente vuole valorizzare (es. esperienza del team, innovazione metodologica, tempi di consegna, sostenibilita', ecc.)
6. **Vincoli specifici** se presenti (es. contratto ad alta intensita' manodopera, IT interesse strategico, progettazione inclusa)

Se l'utente non fornisce tutti gli input, chiedi quelli mancanti prima di procedere.

## Fonti normative

Leggere prima di procedere:
- `references/estratti/dlgs-36-art107-108.md`
- `references/estratti/anac-lg-n2-metodologia-oepv.md`

## Procedura

### Passo 1 - Verifica applicabilita' OEPV e vincoli

Prima di costruire la matrice, verificare:

1. **OEPV obbligatorio?** (art. 108 co. 2):
   - Servizi architettura/ingegneria >= 140.000 EUR -> SI, obbligatorio
   - Forniture/servizi alta tecnologia/innovazione >= 140.000 EUR -> SI, obbligatorio
   - Appalto integrato con progettazione -> SI, obbligatorio
   - Servizi sociali / ristorazione -> SI, obbligatorio
   - Lavori standard senza componente progettuale -> NO, ma ammesso
   - Se OEPV non obbligatorio e oggetto standardizzato: segnalare che il prezzo piu' basso e' ammesso

2. **Limite punteggio economico** (art. 108 co. 4):
   - Appalto IT interesse strategico nazionale -> max 10%
   - Servizi/lavori alta intensita' manodopera -> max 30%
   - Tutti gli altri -> nessun limite esplicito, ma giustificare la scelta (motivazione proporzionalita')
   
3. **Criteri premianti obbligatori** (art. 108 co. 7): il testo dice "e' sempre previsto il maggiore punteggio possibile" per **tutte e tre** le categorie seguenti:
   - **Produttori di beni a basse emissioni di CO2**: obbligatorio per contratti di forniture e lavori con componente significativa di materiali da costruzione; per servizi puri (intellettuali) la fattispecie e' meno diretta ma la cautela suggerisce di includerlo o motivarne l'esclusione
   - **Imprese con misure di welfare aziendale**: applicabile a tutti i contratti; verificare che la SA abbia definito cosa si intende per "misure di welfare" (es. asili nido aziendali, flessibilita' oraria, buoni pasto: specificare nel disciplinare)
   - **Certificazione parita' di genere** (UNI/PdR 125:2022 o equivalente, D.Lgs. 198/2006 art. 46-bis): applicabile a tutti i contratti; il punteggio deve essere il massimo disponibile per un singolo sottocriterio
   - Se la SA omette una delle tre categorie, la matrice e' esposta a contestazione. Documentare nel disciplinare la ragione dell'eventuale esclusione con riferimento all'oggetto specifico del contratto (art. 108 co. 6: criterio collegato all'oggetto).

### Passo 2 - Proposta struttura criteri

Proporre una struttura articolata in criteri e sottocriteri. Linee guida generali:

**Per servizi di architettura e ingegneria (tipico):**
- Criterio A - Qualita' tecnica dell'offerta / metodologia: 30-40 punti
  - A1 Approccio metodologico e comprensione del progetto: 10-15 punti (discrezionale)
  - A2 Innovazioni e soluzioni tecniche proposte: 5-10 punti (discrezionale)
  - A3 Piano di lavoro e cronoprogramma: 5-10 punti (discrezionale/tabellare)
- Criterio B - Caratteristiche del team: 20-30 punti
  - B1 Qualificazione e esperienza del responsabile: 10-15 punti (tabellare - anni esperienza + titoli)
  - B2 Qualificazione specialisti del team: 5-10 punti (tabellare)
- Criterio C - Criteri premianti obbligatori art. 108 co. 7: 8-15 punti (tutti e tre obbligatori)
  - C1 Parita' di genere (certificazione UNI/PdR 125 o equiv.): 3-5 punti (tabellare on/off) [OBBLIGATORIO]
  - C2 Welfare aziendale (misure concrete: specificare nel disciplinare): 2-5 punti (tabellare/discrezionale) [OBBLIGATORIO]
  - C3 Basse emissioni CO2 (per servizi: dichiarazione politica ambientale o certificazione; per forniture/lavori: materiali a basse emissioni): 2-5 punti (tabellare on/off) [OBBLIGATORIO, collegare all'oggetto]
- Criterio D - Tempistiche di consegna: 5-10 punti (formula quantitativa - riduzione tempi proposta)
- Criterio E - Offerta economica: 30 punti (formula lineare)
  Totale: 100 punti

**Per lavori (tipico, quando OEPV scelto):**
- Criterio A - Qualita' esecutiva e organizzazione del cantiere: 20-30 punti
  - A1 Piano organizzativo cantiere: 10-15 punti (discrezionale)
  - A2 Misure per la riduzione dei disagi: 5-10 punti (discrezionale)
- Criterio B - Caratteristiche tecniche dei materiali e soluzioni migliorative: 10-20 punti
  - B1 Soluzioni migliorative rispetto al capitolato: 8-12 punti (tabellare/discrezionale)
  - B2 Sostenibilita' ambientale (CAM migliorativi, basse emissioni CO2): 5-10 punti (tabellare on/off) [copre criterio obbligatorio CO2 art. 108 co. 7]
- Criterio C - Criteri premianti obbligatori art. 108 co. 7: 8-12 punti
  - C1 Parita' di genere (certificazione UNI/PdR 125 o equiv.): 3-5 punti (tabellare on/off) [OBBLIGATORIO]
  - C2 Welfare aziendale (misure concrete: specificare nel disciplinare): 3-5 punti (tabellare/discrezionale) [OBBLIGATORIO]
  Nota: per lavori, il criterio CO2 (B2) conta anche per l'obbligo art. 108 co. 7 purche' il peso sia il massimo disponibile per un singolo sottocriterio.
- Criterio D - Tempi di esecuzione: 5-10 punti (formula: riduzione % del tempo contrattuale)
- Criterio E - Offerta economica: 30-40 punti (formula lineare)
  Totale: 100 punti

> Questi sono schemi indicativi. Adattare all'oggetto specifico. I pesi devono riflettere le priorita' reali della stazione appaltante e devono essere motivati.

### Passo 3 - Metodi di attribuzione punteggio

Per ogni criterio/sottocriterio indicare il metodo:

**Tabellare (on/off o scala discreta)**:
- Si/no: il requisito e' soddisfatto (peso pieno) o non e' soddisfatto (0)
- Scala discreta: es. 0 / 5 / 10 in funzione del livello dichiarato
- Adatto per: titoli di studio, anni esperienza, certificazioni, presenza di requisiti dichiarabili

**Discrezionale (giudizio della commissione)**:
- Ogni commissario assegna un coefficiente da 0 a 1 (o 0-10) in modo autonomo e non collegiale
- La commissione, riunita, fa la media dei coefficienti individuali
- Si riproporziona: il coefficiente del miglior offerente diventa 1
- Adatto per: qualita' narrativa delle relazioni tecniche, originalita' metodologica, adeguatezza dei piani
- ATTENZIONE: i criteri discrezionali devono avere sub-elementi descrittori sufficientemente dettagliati per non essere impugnati come "troppo vaghi"

**Formula quantitativa**:
- Per parametri numerici: tempo offerto, percentuale di riduzione, numero di risorse, ecc.
- Formula lineare crescente: V(a) = Ra / Rmax (dove Ra = valore offerta, Rmax = valore migliore offerta)
- Formula lineare decrescente (per variabili tipo "tempo" dove meno = meglio): V(a) = Rmin / Ra
- Adatto per: tempi, quantita' di personale aggiuntivo, prestazioni misurabili

**Offerta economica - formula lineare**:
- Pe_i = Vmax × (Prezzomin / Prezzo_i)
- Dove: Vmax = punteggio massimo per il prezzo, Prezzomin = offerta piu' bassa
- L'offerente con il prezzo piu' basso ottiene Vmax; gli altri proporzionalmente meno
- Specificare sempre la formula nel disciplinare per evitare impugnative

### Passo 4 - Output

```markdown
# Bozza matrice criteri/sottocriteri OEPV
**Gara**: [oggetto]
**Tipo contratto**: [lavori/servizi/forniture]
**Importo base d'asta**: EUR [importo]
**Criterio aggiudicazione**: OEPV qualita'/prezzo (art. 108 co. 1 D.Lgs. 36/2023)
**OEPV obbligatorio**: [si/no - art. 108 co. 2, motivazione]

---

## Matrice criteri

| Criterio | Sottocriterio | Peso max | Metodo | Note |
|----------|---------------|----------|--------|------|
| A - [nome] | - | [XX] | - | |
| | A1 - [nome] | [XX] | Tabellare/Discrezionale/Formula | [descrizione breve] |
| | A2 - [nome] | [XX] | ... | ... |
| B - [nome] | - | [XX] | - | |
| ... | | | | |
| **Offerta economica** | - | **[XX]** | Formula lineare | Pe_i = Vmax × (Prezzomin / Prezzo_i) |
| **TOTALE** | | **100** | | |

---

## Vincoli applicati

- Punteggio economico: [XX]% ([entro limiti art. 108 co. 4 / limite 10% per IT / limite 30% per alta intensita' manodopera])
- Criteri premianti obbligatori art. 108 co. 7 (tutti e tre verificati):
  - Parita' di genere: incluso nel criterio [X], sottocriterio [Xn], peso [X] punti (massimo disponibile)
  - Welfare aziendale: incluso nel criterio [X], sottocriterio [Xn], peso [X] punti (massimo disponibile)
  - Basse emissioni CO2: [incluso come criterio [X], sottocriterio [Xn] / motivazione esclusione se inapplicabile all'oggetto]

---

## Metodi di valutazione - dettaglio

### Criteri discrezionali
Per ogni criterio discrezionale: ogni commissario assegna un coefficiente da 0 a 1 in modo autonomo; la commissione calcola la media e riproporziona rispetto al miglior offerente (V = media_i / max(media)).

### Criterio offerta economica
Formula: Pe_i = [Vmax] × (Prezzo_minimo / Prezzo_i)
Dove Prezzo_minimo = prezzo piu' basso tra le offerte ammesse.

---

## Note per il disciplinare di gara

1. Questa matrice e' una bozza: va inserita verbatim nel disciplinare di gara con la formula di calcolo per ciascun criterio
2. I criteri discrezionali devono essere corredati di descrittori sufficientemente precisi per guidare la commissione
3. La commissione deve essere nominata dopo la scadenza delle offerte (art. 93 co. 9 D.Lgs. 36/2023)
4. I coefficienti discrezionali sono attribuiti singolarmente da ciascun commissario prima della riunione collegiale

---

## Criticita' residue da risolvere prima della pubblicazione

[elenco dei punti ancora da definire dalla SA]
```

## Casi limite da gestire

### Importo sotto soglia (< 140.000 EUR per servizi) + servizio non standardizzato
L'OEPV non e' obbligatorio ma puo' essere scelto. Segnalare che per servizi professionali anche sotto soglia, l'OEPV e' spesso consigliato dalla prassi ANAC per ridurre il rischio impugnativa.

### Appalto integrato (progettazione + esecuzione)
Obbligatorio per legge l'OEPV. I criteri devono valorizzare sia la qualita' progettuale che le caratteristiche esecutive. Attenzione: non devono essere assegnati punti per varianti/opere aggiuntive rispetto al progetto esecutivo posto a base di gara (art. 108 co. 11).

### Contratto con fattori di merito per PMI / prossimita' territoriale
L'art. 108 co. 7 consente criteri che favoriscano PMI, start-up innovative, produzione locale di materiali da costruzione a basse emissioni. Includere se pertinente all'oggetto, motivando nel disciplinare la coerenza con gli obiettivi dell'appalto.

### Commissione monocriterio (solo prezzo)
Se il criterio e' il prezzo piu' basso (ammesso solo per forniture/servizi standardizzati non ad alta intensita' di manodopera), questa sotto-attivita' non si applica. La skill segnala l'incompatibilita' e rinvia al RUP.

## Limiti di questo task

- La matrice prodotta e' una bozza: richiede revisione del RUP e, per gli importi che lo richiedono, validazione legale
- I pesi suggeriti sono indicativi: la scelta finale dei pesi e' discrezionale della SA e deve essere motivata negli atti preparatori
- La skill non valuta la coerenza dei criteri con i requisiti tecnici del capitolato (e.g. che i criteri discrezionali siano effettivamente valutabili dalla commissione sulla base dell'offerta)
- Non sostituisce il parere del consulente legale in caso di procedure complesse o contenziose

## Esempi

Vedi `examples/`:
- `conforme-servizi-architettura/` - matrice OEPV per servizi di progettazione >= 140k (OEPV obbligatorio)
