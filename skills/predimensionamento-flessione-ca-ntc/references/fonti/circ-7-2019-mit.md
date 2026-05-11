# Fonte: Circolare MIT n. 7 del 21/01/2019 (GU n. 35 del 11/02/2019 - Suppl. Ord. n. 5)

**Titolo**: Istruzioni per l'applicazione dell'aggiornamento delle "Norme tecniche per le costruzioni" di cui al decreto ministeriale 17 gennaio 2018
**Circolare**: MIT n. 7 del 21 gennaio 2019
**Pubblicazione**: GU n. 35 dell'11/02/2019 - Supplemento Ordinario n. 5
**SHA256 PDF**: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
**File**: not_in_repo/circ-7-2019.pdf (348 pagine)
**Data di lettura**: 2026-05-11
**Estratto da**: pdftotext su not_in_repo/circ-7-2019.pdf; paragrafi rilevanti per
la skill predimensionamento-flessione-ca-ntc identificati a partire dalla pagina 84
del Supplemento Ordinario n. 5.

---

## Trascrizione fedele dei paragrafi rilevanti per la skill predimensionamento-flessione-ca-ntc

### par. C4.1.2 - VERIFICHE AGLI STATI LIMITE (GU p. 84)

[Estratto dal PDF, righe 6644-6652 del testo estratto con pdftotext]

> C4.1.2   VERIFICHE AGLI STATI LIMITE
> C4.1.2.1 MATERIALI

---

### par. C4.1.2.1.2.1 - Diagrammi di progetto tensione-deformazione del calcestruzzo (GU p. 84)

[Estratto dal PDF, righe 6656-6820 del testo estratto con pdftotext]

> La principale novita' rispetto alle NTC precedenti e' costituita dai diagrammi di
> progetto tensione-deformazione per il calcestruzzo confinato.
>
> Il confinamento del calcestruzzo, che si consegue utilizzando staffe chiuse, legature
> interne e dettagli costruttivi in accordo con quanto illustrato nel par. 7.4.6, ha lo
> scopo di incrementare la resistenza ultima e la duttilita' delle sezioni, per quanto
> di competenza del calcestruzzo.
>
> Per il diagramma tensione-deformazione del calcestruzzo confinato, la norma consente
> l'utilizzo di modelli analitici di comprovata validita', che siano rappresentativi del
> reale comportamento del materiale in stato di tensione triassiale. In assenza di
> specifiche valutazioni le NTC, in linea con l'UNI EN 1998-2, forniscono un diagramma
> tensione-deformazione per il calcestruzzo confinato del tipo parabola-rettangolo.

**Nota**: il par. C4.1.2.1.2.1 della Circolare commenta esclusivamente il calcestruzzo
confinato (staffe). Non ridefinisce i parametri lambda ed eta dello stress-block per
calcestruzzo non confinato in flessione semplice. Questi sono definiti da NTC 2018
Fig. 4.1.1(c) per Classe 1 (fck <= 50 MPa).

---

### par. C4.1.2.3 - STATI LIMITE ULTIMI (GU p. 89)

[Estratto dal PDF, righe 7286-7350 del testo estratto con pdftotext]

> C4.1.2.3   STATI LIMITE ULTIMI
> C4.1.2.3.4 Resistenza flessionale e duttilita' massima in presenza e in assenza di
>            sforzo assiale

---

### par. C4.1.2.3.4.2 - Verifiche di resistenza e duttilita' (GU p. 89)

[Estratto dal PDF, righe 7294-7350 del testo estratto con pdftotext]

> Con riferimento alla verifica di resistenza dei pilastri di c.a. soggetti a sola
> compressione assiale, la prescrizione circa l'eccentricita' minima dell'azione assiale
> da tenere in conto puo' essere implicitamente soddisfatta valutando NRd con la formula
>
>   NRd = 0,8 * Ac * fcd + As,tot * fyd     [C4.1.11]
>
> con Ac area del calcestruzzo e As,tot area totale d'armatura.
>
> Rispetto alle precedenti NTC e' fornita una migliore e piu' esplicita articolazione
> delle verifiche di duttilita'. Tali verifiche sono espressamente richieste al Capitolo 7
> della norma per la progettazione in presenza di azioni sismiche; pertanto la norma
> fornisce la definizione di duttilita' di curvatura, indicando le modalita' pratiche per
> il calcolo della corrispondente capacita' a livello di sezione.

**Nota**: il par. C4.1.2.3.4.2 della Circolare commenta la verifica di resistenza e
duttilita' in generale. Non introduce un limite numerico x/d specifico per le sezioni
in flessione semplice. Il limite x/d <= 0,45 si trova al par. 4.1.1.1 del NTC 2018
(ridistribuzione momenti nelle travi continue).

---

### par. C4.1.2.2.2 - Stato limite di deformazione (GU p. 86)

[Estratto dal PDF, righe 6820-6850 del testo estratto con pdftotext]

La Circolare al par. C4.1.2.2.2 fornisce indicazioni sulle frecce massime ammesse per
travi e solette. In assenza di verifica esplicita, la limitazione di rapporto luce/altezza
l/h (formula C4.1.4) puo' essere usata come criterio indiretto. Non riguarda il calcolo
di MRd per singola sezione.

---

## Ricerca del limite x/d <= 0,45 nella Circolare

A seguito di ricerca sistematica nella Circolare 7/2019 (pdftotext completo, grep su
"0,45" e "0.45"), **il valore numerico 0,45 non compare nel testo della Circolare**.
Il limite x/d <= 0,45 non e' introdotto dalla Circolare.

Confronto con NTC 2018: il valore 0,45 compare al par. 4.1.1.1 del NTC 2018 (riga 6266
del testo estratto), nel contesto della ridistribuzione dei momenti nelle travi continue.

**Conclusione operativa per la skill**: l'avvertenza x/d > 0,45 nella skill deve citare
NTC 2018 par. 4.1.1.1 (ridistribuzione momenti, travi continue) e non la Circolare
C4.1.2. La formula MRd = As * fyd * z resta valida per qualsiasi sezione con eps_s >= eps_yd,
indipendentemente da x/d. Il limite x/d e' rilevante solo per la ridistribuzione e per
le zone sismiche (NTC par. 7.4).

---

## Valori costanti verificati da lettura PDF

La Circolare 7/2019 non introduce nuovi valori numerici per i parametri di calcolo
dello stress-block (lambda, eta, eps_cu, alpha_cc, gamma_c, gamma_s). Conferma
l'applicabilita' dei modelli NTC 2018 par. 4.1.2.1.2.
