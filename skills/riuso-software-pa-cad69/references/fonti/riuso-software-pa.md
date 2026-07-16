# Fonte verbatim - Riuso e rilascio in open source del software della PA

> Obbligo di analisi comparativa nell'acquisizione (art. 68 C.A.D.) e obbligo di
> rilascio in riuso sotto licenza aperta del software della PA (art. 69 C.A.D.), con
> le Linee guida operative AgID (documentazione, README, publiccode.yml, tempi,
> registrazione su Developers Italia).

## Atto 1 - D.Lgs. 7 marzo 2005, n. 82 (C.A.D.) - artt. 68-69

> **Fonte**: Normattiva, pagina indice pinnata a `!vig=2026-07-16` (codice 005G0104).
> URL: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82!vig=2026-07-16
> SHA256 pagina indice: 5e75c6b9215888cba2dd5d118c6aa3baf6b3d26eee09d54af7c2f84e20f28222
> Artt. 68-69 caricati via AJAX (caricaArticolo) e trascritti verbatim. Accesso: 2026-07-16.

---

### Art. 68 - Analisi comparativa delle soluzioni

```
Art. 68
 Analisi comparativa delle soluzioni

1. Le pubbliche amministrazioni acquisiscono programmi informatici o parti di essi nel rispetto dei principi di economicità e di efficienza, tutela degli investimenti, riuso e neutralità tecnologica, a seguito di una valutazione comparativa di tipo tecnico ed economico tra le seguenti soluzioni disponibili sul mercato: 

 

a) software sviluppato per conto della pubblica amministrazione; 

b) riutilizzo di software o parti di esso sviluppati per conto della pubblica amministrazione; 

c) software libero o a codice sorgente aperto; 

d) software fruibile in modalità cloud computing; 

e) software di tipo proprietario mediante ricorso a licenza d'uso; 

f) software combinazione delle precedenti soluzioni. 

1-bis. A tal fine, le pubbliche amministrazioni prima di procedere all'acquisto, secondo le procedure di cui al codice di cui al decreto legislativo ((n. 50 del 2016)), effettuano una valutazione comparativa delle diverse soluzioni disponibili sulla base dei seguenti criteri: 

 

a) costo complessivo del programma o soluzione quale costo di acquisto, di implementazione, di mantenimento e supporto; 

b) livello di utilizzo di formati di dati e di interfacce di tipo aperto nonché di standard in grado di assicurare l'interoperabilità e la cooperazione applicativa tra i diversi sistemi informatici della pubblica amministrazione; 

c) garanzie del fornitore in materia di livelli di sicurezza, conformità alla normativa in materia di protezione dei dati personali, livelli di servizio tenuto conto della tipologia di software acquisito. 

1-ter. Ove dalla valutazione comparativa di tipo tecnico ed economico, secondo i criteri di cui al comma 1-bis, risulti motivatamente l'impossibilità di accedere a soluzioni già disponibili all'interno della pubblica amministrazione, o a software liberi o a codici sorgente aperto, adeguati alle esigenze da soddisfare, è consentita l'acquisizione di programmi informatici di tipo proprietario mediante ricorso a licenza d'uso. La valutazione di cui al presente comma è effettuata secondo le modalità e i criteri definiti dall'AgID. 

2. COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179. 

2-bis. COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179. 

3. 
((COMMA ABROGATO DAL D.LGS. 13 DICEMBRE 2017, N. 217)). 

4. COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179. 

 (28) 

-------------
AGGIORNAMENTO (28)

 Il D.Lgs. 26 agosto 2016, n. 179 ha disposto (con l'art. 61, comma 2, lettera d)) che l'espressione «chiunque» ovunque ricorra, si intende come «soggetti giuridici».
```

### Art. 69 - Riuso delle soluzioni e standard aperti

```
Art. 69
(Riuso delle soluzioni e standard aperti)

1. Le pubbliche amministrazioni che siano titolari di soluzioni e programmi informatici realizzati su specifiche indicazioni del committente pubblico, hanno l'obbligo di rendere disponibile il relativo codice sorgente, completo della documentazione e rilasciato in repertorio pubblico sotto licenza aperta, in uso gratuito ad altre pubbliche amministrazioni o ai soggetti giuridici che intendano adattarli alle proprie esigenze, salvo motivate ragioni di ordine e sicurezza pubblica, difesa nazionale e consultazioni elettorali. 

2. Al fine di favorire il riuso dei programmi informatici di proprietà delle pubbliche amministrazioni, ai sensi del comma 1, nei capitolati o nelle specifiche di progetto è previsto, ((salvo che ciò risulti eccessivamente oneroso per comprovate ragioni di carattere tecnico-economico, che l'amministrazione committente sia sempre titolare di tutti i diritti sui programmi e i servizi delle tecnologie dell'informazione e della comunicazione, appositamente sviluppati per essa)). 

((

2-bis. Al medesimo fine di cui al comma 2, il codice sorgente, la documentazione e la relativa descrizione tecnico funzionale di tutte le soluzioni informatiche di cui al comma 1 sono pubblicati attraverso una o più piattaforme individuate dall'AgID con proprie Linee guida.

))
```

## Atto 2 - Linee guida AgID su acquisizione e riuso di software per le PA

> **Fonte**: Agenzia per l'Italia Digitale (AgID), documento ufficiale (adottato ex
> art. 71 C.A.D.), versione pubblicata. Host istituzionale.
> URL: https://www.agid.gov.it/sites/default/files/repository_files/lg-acquisizione-e-riuso-software-per-pa-docs_pubblicata.pdf
> SHA256 PDF: 41925c4dae94c5a8b7ab5b39be03563dc80e033705b503710792d297cd225a43
> (101 pagine; riproducibile, doppio download). Estratti verbatim delle sezioni
> operative. Accesso: 2026-07-16.

---

### Allegato A, A.7 - File README (estratto verbatim, pagg. ~36-37)

```
A.7 File README

Il repository deve contenere un file denominato README.md contenente:
     • (MUST) il titolo del repository ed un sottotitolo descrittivo;
     • (MUST) descrizione estesa del repository in un linguaggio comprensibile anche dai non addetti ai lavori
       (evitare acronimi e gergo tecnico), in particolare:
          – contesto di utilizzo e casi d’uso;
          – finalità del software;
          – screenshot (se il software dispone di interfaccia grafica, anche web);
          – link ad eventuali pagine istituzionali relative al progetto o al contesto di utilizzo;
     • (MUST) link ad eventuale documentazione aggiuntiva non inclusa nel presente repository;
     • (MUST) spiegazione struttura del repository anche a beneficio dei potenziali contributori (struttura delle
       directory e dei branch);
     • (MUST) elenco dettagliato prerequisiti e dipendenze (sistemi operativi, librerie, framework eccetera) con
       esplicita indicazione di eventuali dipendenze da software commerciali;
     • (MUST) istruzioni per l’installazione:
          – procedura di installazione di requisiti e dipendenze;
          – build system (se previsto dal progetto);
          – comandi per la compilazione o il deployment, possibilmente automatizzati da uno script/Makefile (se
            previsto dal progetto);
     • (MUST) eventuali indicazioni sullo status del progetto:
          – stato di alpha/beta/stabile eccetera;



36               Appendice A. Allegato A: Guida alla pubblicazione di software come open source
                 Linee guida su acquisizione e riuso di software per le pubbliche amministrazioni


         – importanti limitazioni o known issues;
    • (SHOULD) link ad eventuali sistemi di Continuous Integration (TravisCI, CircleCI), code coverage
      (copertura del codice) ed altre metriche associati al repository;
    • (SHOULD) documentazione relativa all’eventuale utilizzo di sistemi per semplificare e accelerare il de-
      ployment in ambiente di sviluppo, test e produzione (ad esempio immagini Docker o altri sistemi di
      virtualizzazione con predisposizione di immagini preconfigurate);
    • (MUST) nomi dei detentori di copyright, ovvero l’Amministrazione committente;
    • (MUST) nomi dei soggetti incaricati del mantenimento del progetto open source (è richiesto il nome
      dell’azienda e facoltativamente si possono aggiungere nomi delle persone incaricate);
    • (MUST) indirizzo e-mail a cui inviare segnalazioni di sicurezza (specificare che le segnalazioni di sicurezza
      non vanno inviate attraverso l’issue tracker pubblico ma devono essere inviate confidenzialmente a tale
      indirizzo e-mail);


A.8 Documentazione

È necessario (MUST) allegare al software la documentazione necessaria ad:
    • installare le dipendenze;
    • installare un ambiente di sviluppo da zero (meglio se corredata da script, immagini di container, Makefile o
      altri strumenti per rendere l’operazione rapida);
    • compilare il software (ove applicabile);
    • installare il software in ambiente di produzione;
    • comprendere l’architettura del software (a beneficio di soggetti terzi che intendano riusarlo od integrarlo).
```

### Allegato A, A.8 - Documentazione (estratto verbatim, pag. ~37)

```
Se nel capitolato è prevista anche la stesura di documentazione sull’utilizzo del software rivolta agli utenti finali
(«manuale utente» o simile documento), l’obbligo di rilascio si estende anche ad essa. Per tale documentazio-
ne sono consentiti anche formati binari, purché aperti, modificabili e multipiattaforma (resta dunque escluso il
formato PDF).


A.9 Tempi di rilascio

All’inizio della lavorazione, l’Incaricato concorda con l’Amministrazione il piano di rilascio in open source del
software durante lo sviluppo. Le Linee Guida suggeriscono di adottare un modello di sviluppo aperto, che pre-
veda il rilascio contestuale allo sviluppo sin dall’inizio. Questo modello consente anche ad altre amministrazioni
di venire a conoscenza delle attività di sviluppo, anche prima della prima messa in produzione, diminuendo la
probabilità che due amministrazioni sviluppino in modo indipendente software analoghi.
Qualora non si opti per un modello di sviluppo aperto, il rilascio in open source deve essere effettuato (MUST)
entro 15 giorni dal momento dell’acquisizione del software da parte dell’Amministrazione committente al termine
della lavorazione, ovvero dal momento in cui detto software viene immesso in collaudo o in produzione, ovvero
da una richiesta dell’Amministrazione che può comunque essere trasmessa all’Incaricato in qualsiasi fase. Se la
lavorazione è articolata in più lotti, i presenti termini di rilascio si applicano a ciascun lotto.
A partire dal momento del rilascio, qualsiasi successiva modifica deve essere pubblicata tempestivamente nel
```

### Allegato A, A.9 - Tempi di rilascio (estratto verbatim, pag. ~37)

```


A.8. Documentazione                                                                                              37
Linee guida su acquisizione e riuso di software per le pubbliche amministrazioni


rilascio e collaudo l’Incaricato può usare le funzionalità di branching offerte dal sistema di controllo di versione
prescelto (MAY).


A.10 Sicurezza

Ricordando che la sicurezza del software è un tema importante di cui tenere conto durante il ciclo di sviluppo e
che non verrà trattato in questo documento, si indicano qui alcuni principi base su attenzioni specifiche da adottare
durante il processo di rilascio.
È necessario (MUST) rimuovere dal codice sorgente qualsiasi password o certificato o altra credenziale relativi a
sistemi reali (anche di test); a tale scopo si deve ricorrere a file di configurazione separati o a blacklist nel sistema
di controllo di versione (ad esempio, il file .gitignore o .hgignore). Qualora si intenda integrare il repository con un
meccanismo di deployment automatico e dunque si necessiti di mantenere delle credenziali, è possibile utilizzare
i meccanismi sicuri di cifratura previsti per la piattaforma di code hosting e per i sistemi di Continuous Integration
```

### Allegato A, A.11 - Registrazione su Developers Italia e file publiccode.yml (estratto verbatim, pag. ~38)

```
A.11 Registrazione del repository su Developers Italia

Non appena il repository pubblico è stato aperto, è necessario (MUST) effettuare la registrazione su Developers
Italia, per garantire che venga indicizzato e presentato nel motore di ricerca presente sul sito.
La registrazione avviene seguendo due passaggi:
     1. Pubblicazione di un file publiccode.yml nella directory root del repository. «publiccode.yml» è uno
        standard che identifica il progetto come «software utile per la Pubblica Amministrazione», e contem-
        poraneamente offre una serie di informazioni utili alla valutazione del software stesso per il riuso. Ta-
        le file verrà rilevato automaticamente dall’indicizzatore (crawler) di Developers Italia al fine della ge-
        nerazione della relativa scheda nel catalogo. La documentazione sul formato può essere trovata qui:
        https://github.com/italia/publiccode.yml
     2. Aggiunta dello strumento di code-hosting al motore di ricerca. Al fine di accertarsi che Developers
        Italia identifichi correttamente il repository come di proprietà della pubblica amministrazione, è necessario
        registrare lo strumento di code-hosting (o meglio, la «organizzazione» all’interno dello stesso) la prima
        volta che viene usato, associandolo alla Pubblica Amministrazione. La procedura è da seguire è dettagliata
        qui: https://onboarding.developers.italia.it




38                Appendice A. Allegato A: Guida alla pubblicazione di software come open source
                                                                                            APPENDICE              B
```
