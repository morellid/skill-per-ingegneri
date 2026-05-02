# Task: Redazione guidata della Relazione CAM (bozza)

Guida dialogica per la redazione della Relazione Tecnica dei Requisiti Ambientali ai sensi del DM 23/06/2022 n. 256. Per ciascun criterio CAM applicabile, chiede i dati tecnici al progettista e genera la bozza della sezione corrispondente.

## Obiettivo

Produrre una **bozza strutturata della Relazione Tecnica dei Requisiti Ambientali** pronta per essere revisionata, integrata e firmata dal progettista, con:
- Intestazione e premessa normativa corrette
- Sezioni corrispondenti ai criteri CAM obbligatori applicabili (sezioni 2.3, 2.4, 2.5, 2.6 del DM 256/2022 Allegato)
- Per ogni criterio: descrizione del criterio, scelta progettuale, dati tecnici a supporto, documentazione di verifica indicata
- Sezione opzionale sui criteri premianti adottati (2.7/3.2/4.3 a seconda del tipo di affidamento), se gara OEPV

## Input richiesti

Prima di iniziare la redazione, raccogliere (o verificare dall'output del task `identifica-criteri-applicabili.md` se gia' eseguito):

1. **Tipologia di intervento** (NC/R1/R2/MS) e classificazione motivata.
2. **Descrizione sintetica del progetto**: committente, oggetto, localizzazione, destinazione d'uso, superficie utile, n. piani.
3. **Numero del capitolato/CIG** (se disponibile, per testata della relazione).
4. **Data presunta di gara** (per verificare vigenza del DM 256/2022 alla data del bando).
5. **Lista dei materiali principali previsti**: per determinare quali sottocriteri della sezione 2.5 (prodotti da costruzione) sono applicabili.
6. **Dati impiantistici**: tipo di impianto termico, raffrescamento, produzione ACS, fotovoltaico/solare termico (per criteri 2.4.2 e 2.4.3).
7. **Tipo di gara**: prezzo piu' basso o OEPV (per criteri premianti).
8. **Tipo di affidamento**: solo progettazione, solo lavori, o congiunto (per individuare sezione criteri premianti).

Se l'utente non ha ancora eseguito il task di identificazione, eseguire prima il Passo 1 (classificazione) del task `identifica-criteri-applicabili.md`.

## Fonti normative

Leggere prima di procedere:

- `references/estratti/dm-256-2022-articoli-chiave.md`
- `references/estratti/dm-256-2022-allegato-criteri-2x.md` (testo criteri obbligatori 2.3-2.6)
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

Il presente progetto e' soggetto all'applicazione dei Criteri Ambientali Minimi (CAM) per l'edilizia pubblica, ai sensi del DM 23 giugno 2022 n. 256 (GU n. 183 del 06/08/2022), in vigore dal 4 dicembre 2022, e dell'art. 57 del D.Lgs. 31 marzo 2023 n. 36 (Codice dei Contratti Pubblici).

La presente Relazione dimostra la conformita' del progetto ai criteri obbligatori del DM 256/2022 applicabili alla tipologia di intervento [NC/R1/R2/MS], ai sensi del criterio 2.2.1 (Relazione CAM) dell'Allegato al DM 256/2022. I criteri non applicabili alla tipologia di intervento sono indicati come tali con motivazione.
---

### Passo 2 - Sezione per ciascun criterio applicabile

Per ogni criterio obbligatorio applicabile, generare una sezione strutturata come segue. Chiedere all'utente i dati specifici prima di generare ciascuna sezione, oppure - se l'utente ha fornito una descrizione del progetto sufficientemente dettagliata - generare la sezione con gli spazi da completare evidenziati con `[DA COMPLETARE: ...]`.

**Struttura standard di ciascuna sezione**:

```
## Criterio [numero] - [titolo]

**Applicabilita'**: [SI / NON APPLICABILE - motivazione]

**Requisito minimo DM 256/2022 Allegato**: [testo sintetico del criterio]

**Soluzione progettuale adottata**:
[Descrizione della scelta tecnica del progettista]

**Conformita' dichiarata**:
[Affermazione di conformita' con dati tecnici verificabili]

**Documentazione di verifica**:
- [Documento 1]: [disponibile / da richiedere al fornitore / da produrre in corso d'opera]
- [Documento 2]: ...

**Riferimento normativo**: Criterio [numero] Allegato DM 23/06/2022 n. 256
```

Segue la struttura specifica per ciascuna sezione dell'Allegato DM 256/2022:

---

#### Sezione 2.3 - Specifiche tecniche territoriali-urbanistiche

*Solo per NC e ristrutturazione urbanistica. Per R1, R2, MS: indicare "Non applicabile - l'intervento non e' una nuova costruzione ne' una ristrutturazione urbanistica".*

Per ciascuno dei sottocriteri 2.3.1-2.3.9, generare una sezione con la struttura standard. I dati da raccogliere per i principali sottocriteri:

**2.3.2 Permeabilita'**: chiedere il coefficiente di deflusso delle superfici non edificate (richiesto <0,50). Se non disponibile, indicare come "da calcolare nella tavola delle superfici impermeabili".

**2.3.3 Isola di calore**: chiedere SRI dei pavimenti esterni/parcheggi (richiesto >=29), tipo di copertura prevista (verde, ventilata, o materiali con SRI >=29/76), percentuale di verde sulla superficie permeabile (richiesto >=60%).

**2.3.9 Risparmio idrico**: chiedere portate dei rubinetti e consumi delle cassette WC. Richiesto: lavabi <=6 l/min, docce <=8 l/min, cassette a doppio scarico <=6 l (pieno) e <=3 l (ridotto).

---

#### Sezione 2.4 - Specifiche tecniche progettuali per gli edifici

Per ciascuno dei criteri 2.4.1-2.4.14, generare una sezione con la struttura standard. I dati principali da raccogliere:

**2.4.1 Diagnosi energetica** (solo R1/R2 con superficie >=1.000 mq): chiedere se e' disponibile la diagnosi energetica e chi l'ha redatta (EGE certificato UNI CEI 11339 o ESCo certificata UNI CEI 11352).

**2.4.2 Prestazione energetica** (NC e R1): chiedere il tipo di sistema impiantistico previsto e la classe energetica target. Richiesto: edificio a energia quasi zero (NZEB). Comfort termico estivo: dichiarare rispetto della massa superficiale >=250 kg/m² per pareti opache verticali, oppure Yie <0,09 W/m²K, oppure verifica dinamica oraria (temperatura operante estiva secondo UNI EN ISO 52016-1, |theta_o,t - theta_rif| <4°C per >85% delle ore dal 20 giugno al 21 settembre).

**2.4.3 Impianti illuminazione**: chiedere se sono previsti sistemi di gestione automatica e tipo di lampade. Richiesto: LED con durata minima 50.000 ore per uffici e scuole; gestione automatica per edifici non residenziali e aree comuni.

**2.4.5 Aerazione/VMC** (NC e R1): chiedere il tipo di sistema di ventilazione. Richiesto per NC: classe II UNI EN 16798-1 (*very low polluting building*), VMC con recupero di calore.

**2.4.7 Illuminazione naturale** (NC e ristrutturazione urbanistica): chiedere se e' disponibile il calcolo del fattore di luce diurna. Richiesto per uffici: 300 lux al 50% dei punti di misura e 100 lux al 95%, verificato con UNI EN 17037.

**2.4.9 Tenuta all'aria**: chiedere il valore n50 previsto. Richiesto per NC: n50 <2 (valore minimo obbligatorio); n50 <1 e' premiante.

**2.4.11 Comfort acustico**: chiedere se e' disponibile la relazione acustica previsionale. Richiesto: classe II del prospetto 1 della UNI 11367.

**2.4.12 Radon**: chiedere se il sito e' in zona a rischio radon (Piano nazionale radon D.Lgs. 101/2020). Richiesto: <=200 Bq/m³ (valore medio annuo); dichiarare le strategie progettuali adottate.

**2.4.13 Piano di manutenzione**: chiedere se il progetto prevede la rappresentazione BIM. Richiesto: archivio tecnico dell'edificio con BIM (IFC, con indicazione del livello LOD UNI 11337-4) e piano di fine vita con elenco materiali riutilizzabili/riciclabili.

**2.4.14 Disassemblaggio e fine vita**: chiedere la percentuale in peso dei componenti edilizi (esclusi impianti) disassemblabili o recuperabili. Richiesto: >=70% peso/peso.

---

#### Sezione 2.5 - Specifiche tecniche per i prodotti da costruzione

Per ciascuna categoria di materiale effettivamente presente nel progetto, generare una sotto-sezione con la struttura standard. Chiedere all'utente per ogni categoria:
- Il materiale e' previsto nel progetto? (SI/NO)
- Se SI: fornitore previsto o tipo di prodotto? Certificazione disponibile?

Per le categorie non usate, indicare: "Categoria non applicabile - il progetto non prevede l'utilizzo di [materiale]."

**Soglie minime per i criteri principali della sezione 2.5** (da inserire nelle sezioni corrispondenti):

- **2.5.1 Emissioni indoor**: pitture, pavimenti plastici, adesivi, rivestimenti interni: COV totali <=1.500 µg/m³, formaldeide <60 µg/m³, acetaldeide <300 µg/m³ (tabella completa in extract criteri-2x).
- **2.5.2 Calcestruzzi**: >=5% materia riciclata/recuperata/sottoprodotti sul peso.
- **2.5.3 Prefabbricati calcestruzzo**: >=5% (CAC: >=7,5%).
- **2.5.4 Acciaio strutturale**: forno elettrico non legato >=75%; legato >=60%; ciclo integrale >=12%.
- **2.5.5 Laterizi**: muratura/solai >=15%; coperture/facciavista >=7,5%.
- **2.5.6 Legno**: certificazione FSC o PEFC (origine sostenibile) oppure >=70% riciclato (con catena di custodia certificata).
- **2.5.7 Isolanti**: tabella per materiale (cellulosa 80%, lana vetro 60%, lana roccia 15%, EPS 15%, XPS 10%, PUR rigido 2%); no SVHC >0,1%; no ODP; lane minerali conformi Nota Q o R.
- **2.5.8 Tramezzature/contropareti/controsoffitti a secco**: >=10% (gesso >=5%).
- **2.5.10.2 Pavimenti resilienti plastici**: >=20%; gomma >=10%.
- **2.5.11 Serramenti in PVC**: >=20%.
- **2.5.12 Tubazioni PVC/PP**: >=20%.

Per il criterio 2.5.1, i mezzi di prova alternativi ai test sono le etichettature: AgBB, Blue Angel, Eco INSTITUT-Label, EMICODE EC1/EC1+, Indoor Air Comfort, M1 Emission Classification, CATAS quality award Plus (CQA) CAM edilizia Plus, Cosmob Qualitas Praemium INDOOR HI-QUALITY Plus.

---

#### Sezione 2.6 - Specifiche tecniche progettuali relative al cantiere

Generare le sezioni per i criteri 2.6.1-2.6.4 applicabili:

**2.6.1 Prestazioni ambientali del cantiere**: generare la sezione elencando le misure ambientali di cantiere previste. Indicare che le misure saranno inserite nel Piano di Sicurezza e Coordinamento (PSC) e nel capitolato speciale. La sezione deve coprire: misure antipolvere, antirumore, risparmio idrico, protezione suolo e acque sotterranee, raccolta differenziata, fase delle macchine (Fase III A min da gennaio 2022; Fase IV da gennaio 2024; Fase V da gennaio 2026).

**2.6.2 Demolizione selettiva** (solo se previste demolizioni o ristrutturazioni): chiedere se il progetto prevede demolizioni e la stima quantitativa dei rifiuti per categoria (codici EER: 170101, 170102, 170103, 170201, 170202, 170203, 170401-170406, 170504, 170604, 170802). Richiesto: >=70% in peso dei rifiuti non pericolosi (esclusi scavi) avviati a recupero.

**2.6.3 Conservazione strato superficiale del terreno** (solo se ci sono movimenti di terra): generare la sezione con l'indicazione della rimozione e accantonamento degli orizzonti "O" e "A" per riutilizzo in aree a verde.

**2.6.4 Rinterri e riempimenti** (solo se previsti): chiedere il tipo di rinterro. Richiesto: per rinterri, riutilizzo materiale di scavo; per miscele betonabili, >=70% riciclato; per miscele legate con leganti idraulici, >=30% riciclato.

---

### Passo 3 - Sezione criteri premianti (solo se OEPV)

Se la gara e' OEPV, per ogni criterio premiante che il progettista intende adottare, generare una sotto-sezione con:
- Numero e titolo del criterio premiante (dalla sezione 2.7, 3.2 o 4.3, a seconda del tipo di affidamento)
- Prestazione dichiarata (superiore al minimo di base)
- Documentazione di supporto richiesta

Se il progettista non ha ancora deciso quali criteri premianti adottare, presentare la lista completa dei criteri applicabili (da `references/estratti/dm-256-2022-allegato-criteri-premianti.md`) e chiedere quali intende includere.

### Passo 4 - Conclusioni e lista documenti di verifica

Generare una sezione conclusiva con:
1. **Dichiarazione di conformita'**: il progettista dichiara che il progetto e' conforme ai CAM obbligatori applicabili del DM 256/2022 ai sensi del criterio 2.2.1.
2. **Tabella riassuntiva criteri**: elenco di tutti i criteri con esito (CONFORME / NON APPLICABILE - motivazione / DA VERIFICARE in corso d'opera).
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
- I dati tecnici inseriti nelle sezioni (percentuali di riciclato, valori n50, portate idriche, livelli di illuminamento) devono essere verificati e confermati sulla base delle specifiche tecniche reali dei prodotti scelti.
- La skill non verifica la coerenza interna fra le scelte dei diversi criteri.
- Non produce i documenti tecnici di verifica (APE, piano gestione rifiuti, piano di cantiere, relazione acustica): la skill ne indica la struttura minima e i contenuti richiesti, ma la loro redazione e' compito del professionista.
