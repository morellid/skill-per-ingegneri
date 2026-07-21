# Estratto operativo - Opere in sotterraneo (NTC 2018 par. 6.7)

Checklist di inquadramento per il progettista geotecnico/strutturale. Ogni punto e' ancorato al testo trascritto
in `../fonti/ntc2018-par-6-7.md`. La skill **inquadra**, non calcola le verifiche ne' dimensiona l'opera.

## 1. Ambito (par. 6.7)

- [ ] L'opera e' una **galleria**, **caverna** o **pozzo** costruito nel sottosuolo (asportazione del
      terreno/roccia, stabilizzazione della cavita' a breve e lungo termine, rivestimento finale)?

## 2. Prescrizioni generali (par. 6.7.1)

- [ ] Definiti il **modello geologico** e il **modello geotecnico** di riferimento?
- [ ] L'approccio progettuale prevede metodi per **prevenire/controllare** gli effetti della variazione dello
      **stato tensionale** e del **regime idraulico** dovuti allo scavo, dimostrando la **stabilita' della
      cavita' a opera ultimata**?
- [ ] Sono specificati e giustificati: **geometria/ubicazione/tracciato**; **metodi e tecniche di scavo**
      (tradizionale o meccanizzato); **interventi di stabilizzazione** e **rivestimenti** (prima fase/
      definitivi) e opere di protezione agli imbocchi; **intercettazione delle acque** e controllo delle
      pressioni interstiziali; **provvedimenti antifrana** (gallerie parietali, imbocchi); **sicurezza** per gas
      tossici/esplosivi, cavita' e venute d'acqua; **materiali di risulta** (ed eventuale inertizzazione)?

## 3. Caratterizzazione geologica (par. 6.7.2)

- [ ] Studi/indagini geologiche commisurati a complessita' geologica, vulnerabilita' ambientale, posizione e
      dimensioni dell'opera?
- [ ] Modello geologico con litotipi, **faglie e discontinuita'**, caratteristiche **sismotettoniche**,
      **franosita'**, eventuali **cavita' carsiche**, condizioni **idrogeologiche** e rischi da **gas**?

## 4. Caratterizzazione e modellazione geotecnica (par. 6.7.3)

- [ ] Indagini in sito e laboratorio per la caratterizzazione fisico-meccanica (elemento di volume e ammasso),
      con valutazione di **potenzialita' spingenti/rigonfianti** e caratteristiche lungo le discontinuita'?
- [ ] Accertato il **regime delle pressioni interstiziali** e la presenza di moti di filtrazione?
- [ ] **Modello geotecnico** idoneo alle analisi del par. 6.7.5, con zone omogenee e regime delle pressioni
      interstiziali; eventuale **metodo osservazionale** con indagini integrative in corso d'opera?

## 5. Criteri di progetto (par. 6.7.4)

- [ ] **Previsione quantitativa** degli effetti indotti dagli scavi al contorno e in superficie (in particolare
      **gallerie poco profonde in ambienti urbanizzati**)?
- [ ] Dimensionati i **rivestimenti** (prima fase e definitivi) e, quando appropriato, le **opere di protezione
      agli imbocchi**?
- [ ] Per opere in **zona di versante**: valutata la **stabilita' globale dei pendii** in corso di realizzazione
      e in esercizio? Gli interventi di miglioramento/rinforzo sono **motivati** e il loro dimensionamento
      **giustificato**?

## 6. Analisi progettuali e verifiche di sicurezza (par. 6.7.5)

- [ ] Analisi riferite alle **diverse fasi di scavo/costruzione** e alle **condizioni di esercizio**, con
      verifiche **SLU** e **SLE**?
- [ ] Considerati gli SLU **GEO** (resistenza del terreno/ammasso) e **STR** (resistenza degli elementi di
      stabilizzazione e di rivestimento, prima fase e definitivi)?
- [ ] Valutati gli **effetti sui manufatti e sulle costruzioni esistenti**?
- [ ] Considerati gli SLU idraulici **UPL** (spinte idrauliche al fronte/contorno) e **HYD** (gradienti
      idraulici, sifonamento)?
- [ ] Stabilita' di **versanti** e **fronti agli imbocchi** verificata con i criteri dei **par. 6.3** (pendii)
      e **6.8** (fronti di scavo)?
- [ ] Verifiche SLU con l'**Approccio 1**, considerando **entrambe** le combinazioni **Combinazione 1
      (A1+M1+R1)** e **Combinazione 2 (A2+M2+R2)**, con Tab. 6.2.I/6.2.II e **gamma_R dei gruppi R1 e R2 pari
      all'unita' (1,0)**?
- [ ] Verifiche **strutturali** degli elementi di rinforzo/rivestimento con i **valori caratteristici** dei
      parametri (par. 6.2.4.1.3) e verifiche **idrauliche** con il par. 6.2.4.2?
- [ ] Con **metodo osservazionale** (par. 6.2.5): previsioni su **convergenza radiale**, **deformazione
      longitudinale del fronte** e **spostamenti di superficie**, da confrontare con i valori misurati?

## 7. Controllo e monitoraggio (par. 6.7.6)

- [ ] Monitoraggio idoneo a verificare le previsioni progettuali (comportamento del terreno/ammasso, dei
      rivestimenti per ogni fase e a opera ultimata, dei manufatti esistenti), per il periodo indicato in
      progetto?
- [ ] In presenza di **fenomeni franosi**: monitorate le grandezze significative (**tensioni, spostamenti,
      pressioni interstiziali**) e gli effetti sulle opere?

## Fuori scope (rinvii)

- **Non** calcola le verifiche ne' dimensiona l'opera/rivestimenti; **non** definisce il modello geologico/
  geotecnico.
- **Sicurezza dei lavoratori** in sotterraneo e macchine di scavo (TBM) come prodotti: fuori ambito.
- **Progettazione sismica**: Cap. 7 NTC 2018.
- Stabilita' di **pendii** (par. 6.3) e **fronti di scavo** (par. 6.8): skill `stabilita-pendii-naturali-ntc` e
  `opere-materiali-sciolti-scavi-ntc`.
