# Task: Redazione guidata della Relazione CAM (bozza)

Guida dialogica per la redazione della Relazione Tecnica dei Requisiti Ambientali ai sensi del DM 23/06/2022 n. 256. Per ciascun criterio CAM applicabile, chiede i dati tecnici al progettista e genera la bozza della sezione corrispondente.

## Obiettivo

Produrre una **bozza strutturata della Relazione Tecnica dei Requisiti Ambientali** pronta per essere revisionata, integrata e firmata dal progettista, con:
- Sezioni corrispondenti a ciascun criterio CAM di base applicabile (Criterio 2 del DM 256/2022)
- Per ogni criterio: descrizione del criterio, scelta progettuale, dati tecnici a supporto, documentazione di verifica indicata
- Sezione opzionale sui criteri premianti adottati (Criterio 4), se gara OEPV

## Input richiesti

Prima di iniziare la redazione, raccogliere (o verificare dall'output del task `identifica-criteri-applicabili.md` se gia' eseguito):

1. **Tipologia di intervento** (NC/R1/R2/MS) e classificazione motivata.
2. **Descrizione sintetica del progetto**: committente, oggetto, localizzazione, destinazione d'uso, superficie utile, n. piani.
3. **Numero del capitolato/CIG** (se disponibile, per testata della relazione).
4. **Data presunta di gara** (per verificare vigenza del DM 256/2022 alla data del bando).
5. **Lista dei materiali principali previsti**: per determinare quali sottocriteri 2.3.x sono applicabili.
6. **Dati impiantistici**: tipo di impianto termico, raffrescamento, produzione ACS, fotovoltaico (per criterio 2.5).
7. **Aree esterne a verde**: superficie, presenza di irrigazione, specie previste (per criterio 2.6).
8. **Importo lavori stimato** (per criterio 2.9).
9. **Tipo di gara**: prezzo piu' basso o OEPV (per criteri premianti).

Se l'utente non ha ancora eseguito il task di identificazione, eseguire prima il Passo 1 (classificazione) del task `identifica-criteri-applicabili.md`.

## Fonti normative

Leggere prima di procedere:

- `references/estratti/dm-256-2022-articoli-chiave.md`
- `references/estratti/dm-256-2022-allegato-criteri-2x.md` (testo criteri di base)
- `references/estratti/dm-256-2022-allegato-criteri-premianti.md` (solo se OEPV)
- `references/estratti/dlgs-36-2023-art57.md`

## Procedura

### Passo 1 - Intestazione e premessa della relazione

Generare l'intestazione standard:

---
**RELAZIONE TECNICA DEI REQUISITI AMBIENTALI**
ai sensi del DM 23 giugno 2022 n. 256 - Criteri Ambientali Minimi per l'edilizia pubblica

**Oggetto**: [descrizione intervento]
**Committente**: [nome SA]
**Progettista**: [da completare]
**Localizzazione**: [comune, via, provincia]
**Classificazione intervento DM 256/2022**: [NC / R1 / R2 / MS]
**Data**: [data redazione]

**Premessa normativa**

Il presente progetto e' soggetto all'applicazione dei Criteri Ambientali Minimi (CAM) per l'edilizia pubblica, ai sensi del DM 23 giugno 2022 n. 256 (GU n. 183 del 06/08/2022), in vigore dall'08 ottobre 2022, e dell'art. 57 del D.Lgs. 31 marzo 2023 n. 36 (Codice dei Contratti Pubblici).

La presente Relazione dimostra la conformita' del progetto ai criteri di base (Criterio 2) del DM 256/2022 applicabili alla tipologia di intervento [NC/R1/R2/MS]. I criteri non applicabili alla tipologia di intervento sono indicati come tali con motivazione.
---

### Passo 2 - Sezione per ciascun criterio applicabile

Per ogni criterio di base applicabile, generare una sezione strutturata come segue. Chiedere all'utente i dati specifici prima di generare ciascuna sezione, oppure - se l'utente ha fornito una descrizione del progetto sufficientemente dettagliata - generare la sezione con gli spazi da completare evidenziati con `[DA COMPLETARE: ...]`.

**Struttura standard di ciascuna sezione**:

```
## Criterio [numero] - [titolo]

**Applicabilita'**: [SI / NON APPLICABILE - motivazione]

**Requisito minimo DM 256/2022**: [testo sintetico del criterio]

**Soluzione progettuale adottata**:
[Descrizione della scelta tecnica del progettista]

**Conformita' dichiarata**:
[Affermazione di conformita' con dati tecnici: es. "Il calcestruzzo strutturale impiegato conterra' almeno il 5% in peso di aggregati riciclati certificati..."]

**Documentazione di verifica disponibile / da richiedere**:
- [Documento 1]: [disponibile in progetto / da richiedere al fornitore / da produrre in corso d'opera]
- [Documento 2]: ...

**Riferimento normativo**: Criterio [numero] Allegato DM 23/06/2022 n. 256
```

Segue la struttura specifica per ciascun criterio:

---

#### Criterio 2.1 - Qualita' del suolo

Chiedere all'utente:
- Il sito e' stato precedentemente edificato o e' su area vergine?
- Sono disponibili risultati di indagini ambientali (analisi terreno)?
- Il sito e' o e' stato inserito in un'anagrafe dei siti da bonificare?

Generare la sezione con:
- Dichiarazione di assenza di contaminazione (o riferimento alla bonifica completata)
- Indicazione della preferenza per la riqualificazione (se applicabile)
- Documento di verifica: certificato/dichiarazione su assenza contaminazione

---

#### Criterio 2.2 - Durabilita', adattabilita' e flessibilita'

Chiedere all'utente:
- Tipo di struttura (c.a., acciaio, legno, muratura)?
- Vita utile di progetto prevista per la struttura e per gli elementi di involucro?
- Sono previsti impianti accessibili per manutenzione senza demolizioni?

Generare la sezione con:
- Vita utile dichiarata per categoria di elemento
- Indicazione dell'accessibilita' degli impianti
- Documento di verifica: relazione tecnica strutturale con vita utile; tavole impianti

---

#### Criterio 2.3 - Materiali da costruzione

Per ogni categoria di materiale effettivamente presente nel progetto (2.3.2-2.3.13), generare una sotto-sezione. Chiedere all'utente per ogni categoria:
- Il materiale e' previsto nel progetto? (SI/NO)
- Se SI: fornitore previsto o tipo di prodotto? Certificazione disponibile?

Per le categorie non usate, indicare sinteticamente: "Categoria non applicabile - il progetto non prevede l'utilizzo di [materiale]."

Per le categorie usate, generare la sezione con:
- Percentuale di riciclato richiesta e dichiarata (o da dichiarare)
- Certificazioni richieste (FSC/PEFC per legno; EPD/dichiarazione produttore per altri)
- Documento di verifica: scheda tecnica fornitore / certificato

---

#### Criterio 2.4 - Sistemi di risparmio idrico

Chiedere all'utente:
- Il progetto include interventi sugli impianti idro-sanitari?
- Tipologia di edificio e numero di utenti previsto?
- Superficie del tetto e delle aree verdi?

Generare la sezione con:
- Specifiche dei rubinetti e cassette WC (portate e consumi)
- Se applicabile: descrizione sistema raccolta meteorica
- Se applicabile: sistema di contatori per edifici >= 1.000 mq
- Documento di verifica: schede tecniche sanitari; schema idraulico

---

#### Criterio 2.5 - Efficienza energetica

Chiedere all'utente:
- Tipo di impianto termico (pompa di calore, caldaia, teleriscaldamento)?
- Sistema di raffrescamento (se previsto)?
- Impianto fotovoltaico o solare termico (se previsto)?
- Classe energetica target?

Generare la sezione con:
- Descrizione del sistema impiantistico
- Classe energetica target (A3 per NC, miglioramento >= 2 classi per R1)
- Riferimento al calcolo energetico/APE di progetto
- Documento di verifica: APE di progetto; relazione impianti

---

#### Criterio 2.6 - Requisiti per le aree verdi

(Solo se applicabile: NC o R1 con verde >= 500 mq)

Chiedere all'utente:
- Superficie a verde prevista (mq)?
- Specie vegetali previste? Lista disponibile?
- Tipo di impianto di irrigazione?

Generare la sezione con:
- Percentuale specie autoctone dichiarata
- Tipo di substrato e compost
- Sistema di irrigazione (a goccia/subirrigazione con sensori umidita')
- Percentuale superfici permeabili
- Documento di verifica: planimetria verde; elenco specie; schema irriguo

---

#### Criterio 2.7 - Gestione rifiuti da C&D

Chiedere all'utente:
- Sono previste demolizioni?
- Stima quantitativa dei principali flussi di rifiuto?

Generare la sezione con:
- Piano di gestione rifiuti (struttura minima)
- Stima quantitativa per categoria (calcestruzzo, laterizi, metalli, legno, misto)
- Target di recupero (>= 70% in peso per rifiuti non pericolosi)
- Modalita' di demolizione selettiva prevista
- Documento di verifica: piano gestione rifiuti C&D

---

#### Criterio 2.8 - Cantiere sostenibile

Generare la sezione con le misure ambientali di cantiere previste:
- Misure antipolvere (bagnatura, barriere)
- Misure antirumore (attrezzature Stage IIIA/IV)
- Gestione acque di cantiere
- Raccolta differenziata rifiuti in cantiere
- Indicare che le misure saranno inserite nel Piano di Sicurezza e Coordinamento (PSC) e nel capitolato speciale
- Documento di verifica: piano di cantiere con misure ambientali (da allegare al capitolato)

---

#### Criterio 2.9 - Sistema di gestione ambientale esecutore

(Solo se importo lavori >= 5.538.000 EUR)

Generare la sezione con:
- Requisito ISO 14001/EMAS dell'appaltatore come clausola di gara
- Indicazione che la verifica avverra' in sede di qualificazione
- Documento di verifica: certificato ISO 14001 o EMAS (da richiedere all'appaltatore)

---

### Passo 3 - Sezione criteri premianti (solo se OEPV)

Per ogni criterio premiante che il progettista intende adottare, generare una sotto-sezione con:
- Numero e titolo del criterio premiante (Criterio 4.x)
- Prestazione dichiarata (superiore al minimo di base)
- Documentazione di supporto

Se il progettista non ha ancora deciso quali criteri premianti adottare, presentare la lista completa dei criteri 4.x applicabili (da `references/estratti/dm-256-2022-allegato-criteri-premianti.md`) e chiedere quali intende includere.

### Passo 4 - Conclusioni e lista documenti di verifica

Generare una sezione conclusiva con:
1. **Dichiarazione di conformita'**: il progettista dichiara che il progetto e' conforme ai CAM di base applicabili del DM 256/2022.
2. **Tabella riassuntiva criteri**: elenco di tutti i criteri con esito (CONFORME / NON APPLICABILE / DA VERIFICARE in corso d'opera).
3. **Lista documenti da allegare o produrre**: raccolta di tutti i documenti di verifica elencati nelle singole sezioni, con indicazione di disponibilita' attuale.
4. **Avvertenze**: elementi non verificabili dalla skill (qualita' effettiva dei materiali a fornitura, attestati di conformita' finale, verifiche in corso d'opera).

## Output

Documento strutturato pronto per revisione con:
- Intestazione relazione
- Una sezione per ogni criterio applicabile (con o senza dati tecnici, a seconda di quanto fornito)
- Sezione criteri premianti (se OEPV)
- Conclusioni e lista documenti

Il formato del documento deve essere compatibile con l'inserimento in una relazione tecnica di progetto (titoli con ##, tabelle markdown, testo formale in italiano).

## Limiti

- La bozza prodotta dalla skill e' un supporto alla redazione; non sostituisce la verifica tecnica del progettista firmatario.
- I dati tecnici inseriti nelle sezioni (percentuali di riciclato, classi energetiche, portate idriche) devono essere verificati e confermati sulla base delle specifiche tecniche reali dei prodotti scelti.
- La skill non verifica la coerenza interna fra le scelte dei diversi criteri (es. compatibilita' strutturale di un calcestruzzo con aggregati riciclati con la classe di resistenza richiesta dal progettista strutturale).
- Non produce i documenti tecnici di verifica (APE, piano gestione rifiuti, piano di cantiere): la skill ne indica la struttura minima e i contenuti richiesti, ma la loro redazione e' compito del professionista.
