# NTC 2018 - Verifiche allo SLD: spostamenti di interpiano (par. 7.3.6 e 7.3.6.1)

> Trascrizione verbatim dal PDF del Supplemento Ordinario n. 8 alla Gazzetta Ufficiale n. 42 del 20 febbraio
> 2018 (D.M. 17 gennaio 2018 - "Aggiornamento delle Norme tecniche per le costruzioni"), pp. 221-222.
> SHA256 del PDF: `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`.
> Estratto con `pdftotext -layout` (pagine PDF 225-226); i sei limiti [7.3.11a]-[7.3.15] e gli operatori
> relazionali (<= per a-d, < per e) verificati anche sull'immagine renderizzata della pagina PDF 226 (pdftoppm),
> perche' `pdftotext` restituisce il simbolo <= in modo non affidabile.

---

## 7.3.6. RISPETTO DEI REQUISITI NEI CONFRONTI DEGLI STATI LIMITE

Per tutti gli elementi strutturali primari e secondari, gli elementi non strutturali e gli impianti si deve
verificare che il valore di ciascuna domanda di progetto, definito dalla tabella 7.3.III per ciascuno degli
stati limite richiesti, sia inferiore al corrispondente valore della capacità di progetto.

Le verifiche degli elementi strutturali primari (ST) si eseguono, come sintetizzato nella tabella 7.3.III, in
dipendenza della Classe d'Uso (CU):

- nel caso di comportamento strutturale non dissipativo, in termini di rigidezza (RIG) e di resistenza (RES),
  senza applicare le regole specifiche dei dettagli costruttivi e della progettazione in capacità;
- nel caso di comportamento strutturale dissipativo, in termini di rigidezza (RIG), di resistenza (RES) e di
  duttilità (DUT) (quando richiesto), applicando le regole specifiche dei dettagli costruttivi e della
  progettazione in capacità.

Le verifiche degli elementi strutturali secondari si effettuano solo in termini di duttilità.

Le verifiche degli elementi non strutturali (NS) e degli impianti (IM) si effettuano in termini di funzionamento
(FUN) e stabilità (STA), come sintetizzato nella tabella 7.3.III, in dipendenza della Classe d'Uso (CU).

**Tab. 7.3.III - Stati limite di elementi strutturali primari, elementi non strutturali e impianti** (sintesi):

- **SLE - SLO**: per gli elementi strutturali (ST) delle CU III e IV, verifica di **rigidezza (RIG)**; per gli
  elementi non strutturali (NS) delle CU III e IV, **funzionamento (FUN)**.
- **SLE - SLD**: per gli elementi strutturali (ST) delle CU I, II, III e IV, verifica di **rigidezza (RIG)**
  (per le CU III e IV vale anche la resistenza RES allo SLD).
- **SLU - SLV**: resistenza (RES) per gli ST; stabilità (STA) per NS e impianti.
- **SLU - SLC**: duttilità (DUT) per gli ST, nei casi esplicitamente indicati.

(Nel dettaglio: per le CU I e II la verifica di rigidezza degli elementi strutturali si riferisce allo **SLD**;
per le CU III e IV si riferisce allo **SLO**.)

Le verifiche allo stato limite di prevenzione del collasso (SLC), a meno di specifiche indicazioni, si svolgono
soltanto in termini di duttilità e solo qualora le verifiche in duttilità siano espressamente richieste (v.
§7.3.6.1).

## 7.3.6.1. ELEMENTI STRUTTURALI (ST)

### VERIFICHE DI RIGIDEZZA (RIG)

La condizione in termini di rigidezza sulla struttura si ritiene soddisfatta qualora la conseguente deformazione
degli elementi strutturali non produca sugli elementi non strutturali danni tali da rendere la costruzione
temporaneamente inagibile.

Nel caso delle costruzioni civili e industriali, qualora la temporanea inagibilità sia dovuta a spostamenti di
interpiano eccessivi, questa condizione si può ritenere soddisfatta quando gli spostamenti di interpiano
ottenuti dall'analisi in presenza dell'azione sismica di progetto corrispondente allo SL e alla CU considerati
siano inferiori ai limiti indicati nel seguito.

Per le **CU I e II** ci si riferisce allo **SLD** (v. Tab. 7.3.III) e deve essere:

a) per **tamponature collegate rigidamente alla struttura**, che interferiscono con la deformabilità della
   stessa:

   - q·dr <= 0,0050 · h    per **tamponature fragili**                    [7.3.11a]
   - q·dr <= 0,0075 · h    per **tamponature duttili**                    [7.3.11b]

b) per **tamponature progettate in modo da non subire danni** a seguito di spostamenti d'interpiano drp, per
   effetto della loro deformabilità intrinseca oppure dei collegamenti alla struttura:

   - q·dr <= drp <= 0,0100 · h                                            [7.3.12]

c) per costruzioni con **struttura portante di muratura ordinaria**:

   - q·dr <= 0,0020 · h                                                   [7.3.13]

d) per costruzioni con **struttura portante di muratura armata**:

   - q·dr <= 0,0030 · h                                                   [7.3.14]

e) per costruzioni con **struttura portante di muratura confinata**:

   - q·dr < 0,0025 · h                                                    [7.3.15]

dove:

- **dr** è lo spostamento di interpiano, cioè la differenza tra gli spostamenti del solaio superiore e del solaio
  inferiore, calcolati, nel caso di analisi lineare, secondo il § 7.3.3.3 o, nel caso di analisi non lineare,
  secondo il § 7.3.4, sul modello di calcolo **non comprensivo delle tamponature**;
- **h** è l'altezza del piano.

Per le **CU III e IV** ci si riferisce allo **SLO** (v. Tab. 7.3.III) e gli spostamenti d'interpiano devono
essere **inferiori ai 2/3 dei limiti** in precedenza indicati.

In caso di coesistenza di diversi tipi di tamponamento o struttura portante nel medesimo piano della costruzione,
deve essere assunto il **limite di spostamento più restrittivo**. Qualora gli spostamenti di interpiano siano
**superiori a 0,005 h (caso b)**, le verifiche della capacità di spostamento degli elementi non strutturali vanno
estese a tutte le tamponature, alle tramezzature interne ed agli impianti.

---

## Note sulla trascrizione

- **Fonte unica**: PDF ufficiale della Gazzetta Ufficiale (S.O. n. 8 alla G.U. n. 42 del 20/02/2018), la stessa
  usata dalle altre skill NTC del repo (SHA256 `dda1e397...`), con hash riproducibile via doppio download e
  validato live dalla CI del repo su ogni PR.
- **I sei limiti** [7.3.11a]-[7.3.15] e gli **operatori relazionali** sono stati verificati sull'immagine
  renderizzata della pagina PDF 226 (pdftoppm -r 150 -png): i casi a-d usano il segno **<=** (minore o uguale),
  il caso e (muratura confinata) usa il segno **<** (strettamente minore). Valori: 0,0050 h (fragili), 0,0075 h
  (duttili), 0,0100 h (progettate per non danneggiarsi), 0,0020 h (muratura ordinaria), 0,0030 h (armata),
  0,0025 h (confinata).
- **Classi d'uso**: CU I e II -> SLD; CU III e IV -> SLO con limiti pari ai **2/3** di quelli indicati.
- **dr** e' calcolato sul modello **senza tamponature**; **q** e' il fattore di comportamento; **h** l'altezza di
  piano.
- **Regole aggiuntive**: coesistenza -> limite piu' restrittivo; dr > 0,005 h (caso b) -> estensione delle
  verifiche a tamponature, tramezzature e impianti.
- Il **calcolo degli spostamenti** (analisi) e' disciplinato dai §7.3.3.3 (lineare) e §7.3.4 (non lineare), fuori
  dall'ambito di questa skill.
