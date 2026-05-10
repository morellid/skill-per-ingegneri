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

1. **OEPV obbligatorio?** (art. 108 co. 2 - le 6 fattispecie della GU 2023):
   - a) Servizi sociali / ristorazione / alta intensita' manodopera -> SI, obbligatorio
   - b) Servizi architettura/ingegneria/tecnici >= 140.000 EUR -> SI, obbligatorio
   - c) Servizi/forniture alta tecnologia/innovazione >= 140.000 EUR -> SI, obbligatorio
   - d) Dialogo competitivo / partenariato innovazione -> SI, obbligatorio
   - e) Appalto integrato (progettazione + esecuzione) -> SI, obbligatorio
   - f) Lavori ad alto contenuto tecnologico / innovativi -> SI, obbligatorio
   - Lavori standard senza componente progettuale / tecnologica -> NO, ammesso ma non obbligatorio
   - Se OEPV non obbligatorio e oggetto standardizzato: segnalare che il prezzo piu' basso e' ammesso (co. 3)

2. **Limite punteggio economico** (art. 108 co. 4):
   - Appalto IT interesse strategico nazionale -> max 10%
   - Servizi/lavori alta intensita' manodopera -> max 30%
   - Tutti gli altri -> nessun limite esplicito, ma giustificare la scelta (motivazione proporzionalita')
   
3. **Criterio premiante obbligatorio** (art. 108 co. 7): il testo dell'art. 108 co. 7 D.Lgs. 36/2023 (GU 2023) impone esplicitamente un solo obbligo:
   - **Certificazione parita' di genere** (D.Lgs. 198/2006 art. 46-bis): la SA "prevede nei bandi di gara, negli avvisi e negli inviti, il maggior punteggio da attribuire alle imprese che attestano [...] il possesso dei requisiti di cui all'articolo 46-bis". L'autocertificazione e' ammessa. E' l'**unico criterio premiante esplicitamente obbligatorio** nel co. 7.
   - **Criteri premiali facoltativi** (co. 7): la SA puo' inserire criteri premiali per PMI, operatori locali (principio di prossimita'), basse emissioni CO2, welfare aziendale, start-up innovative. Questi sono facoltativi, non obbligatori ai sensi del co. 7. Se inclusi, devono essere connessi all'oggetto (art. 108 co. 6).
   - **Nota**: versioni precedenti di questa skill elencavano CO2 e welfare come obbligatori ("sempre previsto"). Questa affermazione non e' rintracciabile nel testo GU 2023 dell'art. 108 co. 7. L'errore e' corretto in questa versione.
   - Verificare il testo consolidato su Normattiva per verificare se il D.Lgs. 209/2024 correttivo ha modificato il co. 7.

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
- Criterio C - Criteri premianti art. 108 co. 7: 8-15 punti
  - C1 Parita' di genere (D.Lgs. 198/2006 art. 46-bis, autocertificazione ammessa): 3-5 punti (tabellare on/off) [OBBLIGATORIO art. 108 co. 7]
  - C2 Welfare aziendale (misure concrete: specificare nel disciplinare): 2-5 punti (tabellare/discrezionale) [FACOLTATIVO - criterio premiale]
  - C3 Basse emissioni CO2 (per servizi: dichiarazione politica ambientale o certificazione; per forniture/lavori: materiali a basse emissioni): 2-5 punti (tabellare on/off) [FACOLTATIVO - criterio premiale, collegare all'oggetto art. 108 co. 6]
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
- Criterio C - Criteri premianti art. 108 co. 7: 8-12 punti
  - C1 Parita' di genere (D.Lgs. 198/2006 art. 46-bis): 3-5 punti (tabellare on/off) [OBBLIGATORIO art. 108 co. 7]
  - C2 Welfare aziendale (misure concrete: specificare nel disciplinare): 3-5 punti (tabellare/discrezionale) [FACOLTATIVO - criterio premiale]
  Nota: per lavori, il criterio CO2 (B2) e' un criterio premiale facoltativo (non obbligatorio ai sensi del co. 7); se incluso deve essere connesso all'oggetto (art. 108 co. 6).
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
- Criterio premiante obbligatorio art. 108 co. 7:
  - Parita' di genere (D.Lgs. 198/2006 art. 46-bis): incluso nel criterio [X], sottocriterio [Xn], peso [X] punti [OBBLIGATORIO]
- Criteri premiali facoltativi inclusi (se presenti):
  - Welfare aziendale: [incluso nel criterio [X], sottocriterio [Xn] / non incluso]
  - Basse emissioni CO2: [incluso nel criterio [X], sottocriterio [Xn], con collegamento all'oggetto art. 108 co. 6 / non incluso]

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
