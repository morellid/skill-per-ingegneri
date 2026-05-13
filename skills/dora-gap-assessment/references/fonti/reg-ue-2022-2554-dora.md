# Regolamento (UE) 2022/2554 - DORA - trascrizione fedele

- id sorgente: `reg-ue-2022-2554-dora`
- versione: PE-CONS 41/22 (Bruxelles, 17 novembre 2022, 2020/0266 (COD)), testo trilogue-finale identico nel contenuto a GU UE L 333 del 27.12.2022
- URL canonica: https://data.consilium.europa.eu/doc/document/PE-41-2022-INIT/it/pdf
- SHA256 del PDF scaricato: `4d4071b735a6ed3bfce30227a63ea2077d1f7f13a267aecf9ab234c47615e8f4`
- accessed: 2026-05-13
- licenza: dominio pubblico (atto legislativo UE)

## Nota sulla trascrizione

Questa MD e' una trascrizione fedele del testo italiano del Regolamento DORA come pubblicato nel documento PE-CONS 41/22. Sono stati rimossi solo gli artefatti tipografici del PDF (intestazioni di pagina `PE-CONS 41/22 ECOFIN IT`, numeri di pagina, marcatori di nota a pie' di pagina del tipo `+   GU: inserire...` riferiti al numero della direttiva NIS2 non ancora pubblicata al momento della firma). Il contenuto normativo (articoli, commi, lettere) e' riportato verbatim.

Articoli inclusi (rilevanti per gap assessment lato entita' finanziaria, i 5 pillar DORA):

- Capo I - Disposizioni generali: artt. 1-4
- Capo II - Gestione dei rischi informatici (Pillar 1): artt. 5-16
- Capo III - Gestione, classificazione e segnalazione incidenti (Pillar 2): artt. 17-23
- Capo IV - Test di resilienza operativa digitale (Pillar 3): artt. 24-27
- Capo V Sez. I - Rischio derivante da terzi (Pillar 4): artt. 28-30
- Capo VI - Condivisione informazioni (Pillar 5): art. 45
- Capo VIII (parziale): art. 64 (entrata in vigore)

Articoli **non** inclusi (con motivazione):

- Capo V Sez. II (artt. 31-44) - quadro di sorveglianza UE sui fornitori terzi critici di servizi TIC: riguarda autorita' di sorveglianza capofila (AEV) e fornitori critici, non l'obbligo di compliance dell'entita' finanziaria. Verifiche dell'entita' sono nei principi generali (art. 28).
- Capo VII (artt. 46-56) - autorita' competenti, sanzioni amministrative e procedurali, cooperazione: sono lato autorita', non lato entita' finanziaria.
- Capo VIII (artt. 57-63, escluso 64) - atti delegati, modifiche di altri regolamenti UE (n. 1060/2009, 648/2012, 909/2014, 600/2014, 2016/1011), procedure di riesame: non oggetto di gap assessment lato entita'.

Per il testo integrale, anche delle parti omesse, vedere il PDF in `not_in_repo/reg-ue-2022-2554-dora.pdf` con hash sopra.

---

## Intestazione

UNIONE EUROPEA

IL PARLAMENTO EUROPEO - IL CONSIGLIO

Bruxelles, 17 novembre 2022 (OR. en)

2020/0266 (COD) - PE-CONS 41/22

EF 197 - ECOFIN 699 - TELECOM 308 - CYBER 249 - CODEC 1071

REGOLAMENTO DEL PARLAMENTO EUROPEO E DEL CONSIGLIO relativo alla resilienza operativa digitale per il settore finanziario e che modifica i regolamenti (CE) n. 1060/2009, (UE) n. 648/2012, (UE) n. 600/2014, (UE) n. 909/2014 e (UE) 2016/1011.

Testo rilevante ai fini del SEE.

## Considerando (sintesi non normativa)

Il regolamento contiene 106 considerando che illustrano la ratio del provvedimento (digitalizzazione del settore finanziario, frammentazione normativa pre-DORA, necessita' di armonizzazione, coerenza con direttiva NIS2). Per il testo integrale dei considerando vedere il PDF. I considerando hanno valore interpretativo ma non contengono obblighi diretti per le entita' finanziarie; gli obblighi sono nel dispositivo (articoli) trascritto sotto.

---

## Capo I - Disposizioni generali

### Articolo 1 - Oggetto

1. Al fine di conseguire un livello comune elevato di resilienza operativa digitale, il presente regolamento stabilisce i seguenti obblighi uniformi in relazione alla sicurezza dei sistemi informatici e di rete che sostengono i processi commerciali delle entita' finanziarie:

   a) obblighi applicabili alle entita' finanziarie in materia di:
      i) gestione dei rischi delle tecnologie dell'informazione e della comunicazione (TIC);
      ii) segnalazione alle autorita' competenti degli incidenti gravi connessi alle TIC e notifica, su base volontaria, delle minacce informatiche significative;
      iii) segnalazione alle autorita' competenti, da parte delle entita' finanziarie di cui all'articolo 2, paragrafo 1, lettere da a) a d), di gravi incidenti operativi o relativi alla sicurezza dei pagamenti;
      iv) test di resilienza operativa digitale;
      v) condivisione di dati e di informazioni in relazione alle vulnerabilita' e alle minacce informatiche;
      vi) misure relative alla solida gestione dei rischi informatici derivanti da terzi;

   b) obblighi relativi agli accordi contrattuali stipulati tra fornitori terzi di servizi TIC ed entita' finanziarie;

   c) norme per l'istituzione e l'attuazione di un quadro di sorveglianza per i fornitori terzi critici di servizi TIC, allorche' forniscono i loro servizi a entita' finanziarie;

   d) norme sulla cooperazione tra autorita' competenti e norme sulla vigilanza e l'applicazione da parte delle autorita' competenti in relazione a tutte le materie trattate dal presente regolamento.

2. Quanto alle entita' finanziarie identificate come soggetti essenziali o importanti ai sensi delle norme nazionali che recepiscono l'articolo 3 della direttiva NIS2, il presente regolamento e' considerato un atto giuridico settoriale dell'Unione ai sensi dell'articolo 4 di tale direttiva.

3. Il presente regolamento lascia impregiudicata la responsabilita' degli Stati membri per quanto riguarda le funzioni essenziali dello Stato concernenti la sicurezza pubblica, la difesa e la sicurezza nazionale conformemente al diritto dell'Unione.

### Articolo 2 - Ambito di applicazione

1. Fatti salvi i paragrafi 3 e 4, il presente regolamento si applica alle entita' seguenti:

   a) enti creditizi;
   b) istituti di pagamento, compresi gli istituti di pagamento esentati a norma della direttiva (UE) 2015/2366;
   c) prestatori di servizi di informazione sui conti;
   d) istituti di moneta elettronica, compresi gli istituti di moneta elettronica esentati a norma della direttiva 2009/110/CE;
   e) imprese di investimento;
   f) fornitori di servizi per le cripto-attivita' autorizzati a norma del regolamento sui mercati delle cripto-attivita' ed emittenti di token collegati ad attivita';
   g) depositari centrali di titoli;
   h) controparti centrali;
   i) sedi di negoziazione;
   j) repertori di dati sulle negoziazioni;
   k) gestori di fondi di investimento alternativi;
   l) societa' di gestione;
   m) fornitori di servizi di comunicazione dati;
   n) imprese di assicurazione e di riassicurazione;
   o) intermediari assicurativi, intermediari riassicurativi e intermediari assicurativi a titolo accessorio;
   p) enti pensionistici aziendali o professionali;
   q) agenzie di rating del credito;
   r) amministratori di indici di riferimento critici;
   s) fornitori di servizi di crowdfunding;
   t) repertori di dati sulle cartolarizzazioni;
   u) fornitori terzi di servizi TIC.

2. Ai fini del presente regolamento le entita' di cui al paragrafo 1 lettere da a) a t) sono definite collettivamente "entita' finanziarie".

3. Il presente regolamento non si applica a:
   a) gestori di fondi di investimento alternativi di cui all'articolo 3, paragrafo 2, della direttiva 2011/61/UE;
   b) imprese di assicurazione e di riassicurazione di cui all'articolo 4 della direttiva 2009/138/UE;
   c) enti pensionistici aziendali o professionali che gestiscono schemi pensionistici che contano congiuntamente non piu' di 15 aderenti in totale;
   d) persone fisiche o giuridiche esentate a norma degli articoli 2 e 3 della direttiva 2014/65/UE;
   e) intermediari assicurativi, intermediari riassicurativi e intermediari assicurativi a titolo accessorio che sono microimprese o piccole o medie imprese;
   f) uffici dei conti correnti postali di cui all'articolo 2, paragrafo 5, punto 3), della direttiva 2013/36/UE.

4. Gli Stati membri possono escludere dall'ambito di applicazione del presente regolamento le entita' di cui all'articolo 2, paragrafo 5, punti da 4) a 23), della direttiva 2013/36/UE che sono situate nei rispettivi territori. Qualora uno Stato membro si avvalga di tale facolta', e in occasione di ogni successiva modifica, ne informa la Commissione.

### Articolo 3 - Definizioni

Ai fini del presente regolamento si applicano le definizioni seguenti:

1) "resilienza operativa digitale": la capacita' dell'entita' finanziaria di costruire, assicurare e riesaminare la propria integrita' e affidabilita' operativa, garantendo, direttamente o indirettamente tramite il ricorso ai servizi offerti da fornitori terzi di servizi TIC, l'intera gamma delle capacita' connesse alle TIC necessarie per garantire la sicurezza dei sistemi informatici e di rete utilizzati dall'entita' finanziaria, su cui si fondano la costante offerta dei servizi finanziari e la loro qualita', anche in occasione di perturbazioni;

2) "sistema informatico e di rete": un sistema informatico e di rete quali definiti all'articolo 6, punto 1), della direttiva NIS2;

3) "sistema legacy": un sistema di TIC che ha raggiunto la fine del suo ciclo di vita (fine vita), non si presta ad aggiornamenti o correzioni per motivi tecnologici o commerciali, o non e' piu' supportato dal suo fornitore o da un fornitore terzo di servizi TIC, ma e' ancora in uso e supporta le funzioni dell'entita' finanziaria;

4) "sicurezza dei sistemi informatici e di rete": la sicurezza dei sistemi informatici e di rete quale definita all'articolo 6, punto 2), della direttiva NIS2;

5) "rischi informatici": qualunque circostanza ragionevolmente identificabile in relazione all'uso dei sistemi informatici e di rete che, qualora si concretizzi, puo' compromettere la sicurezza dei sistemi informatici e di rete, di eventuali strumenti o processi dipendenti dalle tecnologie, di operazioni e processi, oppure della fornitura dei servizi causando effetti avversi nell'ambiente digitale o fisico;

6) "patrimonio informativo": una raccolta di informazioni, tangibili o intangibili, che e' importante proteggere;

7) "risorse TIC": software o hardware presenti nei sistemi informatici e di rete utilizzati dall'entita' finanziaria;

8) "incidente connesso alle TIC": un singolo evento, o una serie di eventi collegati non programmati dall'entita' finanziaria, che compromette la sicurezza dei sistemi informatici e di rete e ha un impatto avverso sulla disponibilita', autenticita', integrita' o riservatezza dei dati o sui servizi forniti dall'entita' finanziaria;

9) "incidente operativo o di sicurezza dei pagamenti": un singolo evento o una serie di eventi collegati non programmati dalle entita' finanziarie di cui all'articolo 2, paragrafo 1, lettere da a) a d), connessi alle TIC o meno, che hanno un impatto avverso sulla disponibilita', autenticita', integrita' o riservatezza, la disponibilita', l'integrita' o l'autenticita' dei dati connessi ai pagamenti o sui servizi connessi ai pagamenti forniti dall'entita' finanziaria;

10) "grave incidente TIC": un incidente connesso alle TIC che ha un impatto avverso sui sistemi informatici e di rete a supporto delle funzioni essenziali o importanti dell'entita' finanziaria;

11) "grave incidente operativo o di sicurezza dei pagamenti": un incidente operativo o di sicurezza dei pagamenti che ha un impatto avverso sui servizi connessi ai pagamenti forniti;

12) "minaccia informatica": minaccia informatica quale definita all'articolo 2, punto 8), del regolamento (UE) 2019/881;

13) "minaccia informatica significativa": una minaccia informatica le cui caratteristiche tecniche indicano che potrebbe potenzialmente causare un grave incidente TIC o un grave incidente operativo o di sicurezza dei pagamenti;

14) "attacco informatico": un incidente doloso connesso alle TIC provocato dal tentativo, da parte dell'autore della minaccia, di distruggere, rivelare, alterare, disabilitare, rubare o utilizzare senza autorizzazione un'attivita' o ancora accedervi senza autorizzazione;

15) "analisi delle minacce": informazioni aggregate, trasformate, analizzate, interpretate o arricchite per offrire il contesto necessario al processo decisionale e consentire conoscenze pertinenti e sufficienti per attenuare l'impatto di un incidente connesso alle TIC o di una minaccia informatica, compresi i dettagli tecnici dell'attacco informatico, i responsabili dell'attacco, il loro modus operandi e le loro motivazioni;

16) "vulnerabilita'": debolezza, predisposizione o difetto di una risorsa, un sistema, un processo o un controllo potenzialmente sfruttabile;

17) "test di penetrazione guidato dalla minaccia (TLPT)": un quadro che imita le tattiche, le tecniche e le procedure di attori reali della minaccia che sono percepiti come minaccia informatica autentica, che consente di eseguire un test dei sistemi di produzione attivi e critici dell'entita' finanziaria in maniera controllata, mirata e basata sull'analisi della minaccia (red team);

18) "rischi informatici TIC derivanti da terzi": rischi relativi alle TIC cui un'entita' finanziaria puo' essere esposta in relazione al ricorso, da parte di questa, a servizi TIC offerti da fornitori terzi o da subappaltatori di tali fornitori, anche mediante accordi di esternalizzazione;

19) "fornitore terzo di servizi TIC": un'impresa che fornisce servizi TIC;

20) "fornitore intragruppo di servizi TIC": un'impresa che fa parte di un gruppo finanziario e fornisce prevalentemente servizi TIC a entita' finanziarie dello stesso gruppo o a entita' finanziarie appartenenti allo stesso sistema di tutela istituzionale (institutional protection scheme), comprese le loro societa' madri, imprese figlie e succursali o altre entita' di proprieta' comune o sotto controllo comune;

21) "servizi TIC": servizi digitali e di dati forniti attraverso sistemi di TIC a uno o piu' utenti interni o esterni su base continuativa, inclusi l'hardware come servizio e i servizi hardware, comprendenti la fornitura di assistenza tecnica mediante aggiornamenti di software e firmware da parte del fornitore dell'hardware, esclusi i servizi telefonici analogici tradizionali;

22) "funzione essenziale o importante": una funzione la cui interruzione comprometterebbe sostanzialmente i risultati finanziari di un'entita' finanziaria o ancora la solidita' o la continuita' dei suoi servizi e delle sue attivita', o la cui esecuzione interrotta, carente o insufficiente comprometterebbe sostanzialmente il costante adempimento, da parte dell'entita' finanziaria, delle condizioni e degli obblighi inerenti alla sua autorizzazione o di altri obblighi previsti dalla normativa applicabile in materia di servizi finanziari;

23) "fornitore terzo critico di servizi TIC": un fornitore terzo di servizi TIC designato come critico in conformita' dell'articolo 31;

24) "fornitore terzo di servizi TIC stabilito in un paese terzo": un fornitore terzo di servizi TIC che e' una persona giuridica stabilita in un paese terzo che ha stipulato un accordo contrattuale con un'entita' finanziaria per la fornitura di servizi TIC;

25) "impresa figlia": impresa figlia ai sensi dell'articolo 2, punto 10), e dell'articolo 22 della direttiva 2013/34/UE;

26) "gruppo": un gruppo quale definito all'articolo 2, punto 11), della direttiva 2013/34/UE;

27) "impresa madre": impresa madre ai sensi dell'articolo 2, punto 9), e dell'articolo 22 della direttiva 2013/34/UE;

28) "subappaltatore di TIC stabilito in un paese terzo": un subappaltatore di TIC che e' una persona giuridica stabilita in un paese terzo che ha stipulato un accordo contrattuale con un fornitore terzo di servizi TIC o con un fornitore terzo di servizi TIC stabilito in un paese terzo;

29) "rischio di concentrazione delle TIC": l'esposizione a fornitori terzi critici di servizi TIC, singoli o molteplici e correlati tra loro, che crea un grado di dipendenza tale da detti fornitori che l'indisponibilita', i guasti o altri tipi di carenze che si verificassero presso di essi potrebbero mettere a repentaglio la capacita' di un'entita' finanziaria di assolvere funzioni essenziali o importanti oppure di assorbire altri tipi di effetti avversi, comprese perdite cospicue, o potrebbero mettere a repentaglio la stabilita' finanziaria dell'intera Unione;

30) "organo di gestione": organo di gestione quale definito all'articolo 4, paragrafo 1, punto 36), della direttiva 2014/65/UE, all'articolo 3, paragrafo 1, punto 7), della direttiva 2013/36/UE, all'articolo 2, paragrafo 1, lettera s), della direttiva 2009/65/CE, all'articolo 2, paragrafo 1, punto 45), del regolamento (UE) n. 909/2014, all'articolo 3, paragrafo 1, punto 20), del regolamento (UE) 2016/1011 e alla pertinente disposizione del regolamento sui mercati delle cripto-attivita' oppure le persone equivalenti che gestiscono di fatto l'entita' o che assolvono funzioni chiave conformemente al pertinente diritto dell'Unione o nazionale;

Punti 31)-59) [definizioni di tipologie specifiche di entita' finanziaria e fornitori - vedi PDF per testo integrale; sono rinvii definitori a regolamenti e direttive UE preesistenti senza autonomi obblighi di compliance].

60) "microimpresa": un'entita' finanziaria, diversa da una sede di negoziazione, una controparte centrale, un repertorio di dati sulle negoziazioni o un depositario centrale di titoli, che occupa meno di 10 persone e realizza un fatturato annuo e/o un totale di bilancio annuo non superiore a 2 milioni di EUR;

61) "autorita' di sorveglianza capofila": l'autorita' europea di vigilanza designata a norma dell'articolo 31, paragrafo 1, lettera b), del presente regolamento;

62) "comitato congiunto": il comitato di cui all'articolo 54 dei regolamenti (UE) n. 1093/2010, (UE) n. 1094/2010 e (UE) n. 1095/2010;

63) "piccola impresa": un'entita' finanziaria che occupa 10 o piu' persone ma meno di 50 persone e realizza un fatturato annuo e/o un totale di bilancio annuo che supera 2 milioni di EUR ma non superiore a 10 milioni di EUR;

64) "media impresa": un'entita' finanziaria che non e' una piccola impresa, occupa meno di 250 persone e realizza un fatturato annuo non superiore a 50 milioni di EUR e/o un bilancio annuo non superiore a 43 milioni di EUR;

65) "autorita' pubblica": qualsiasi ente governativo o altro ente della pubblica amministrazione, comprese le banche centrali nazionali.

### Articolo 4 - Principio di proporzionalita'

1. Le entita' finanziarie attuano le norme di cui al capo II conformemente al principio di proporzionalita', tenendo conto delle loro dimensioni e del loro profilo di rischio complessivo, nonche' della natura, della portata e della complessita' dei loro servizi, delle loro attivita' e della loro operativita'.

2. Inoltre, l'applicazione dei capi III e IV e del capo V, sezione I, da parte delle entita' finanziarie e' proporzionata alle loro dimensioni e al loro profilo di rischio complessivo, nonche' alla natura, alla portata e alla complessita' dei loro servizi, delle loro attivita' e della loro operativita', come specificamente previsto dalle pertinenti norme di tali capi.

3. Le autorita' competenti prendono in considerazione l'applicazione del principio di proporzionalita' da parte delle entita' finanziarie in sede di riesame della coerenza del quadro per la gestione dei rischi informatici sulla base delle relazioni presentate su richiesta delle autorita' competenti a norma dell'articolo 6, paragrafo 5, e dell'articolo 16, paragrafo 2.

---

## Capo II - Gestione dei rischi informatici (Pillar 1)

### Sezione I

### Articolo 5 - Governance e organizzazione

1. Le entita' finanziarie predispongono un quadro di gestione e di controllo interno che garantisce una gestione efficace e prudente di tutti i rischi informatici, conformemente all'articolo 6, paragrafo 4, al fine di acquisire un elevato livello di resilienza operativa digitale.

2. L'organo di gestione dell'entita' finanziaria definisce e approva l'attuazione di tutte le disposizioni concernenti il quadro per la gestione dei rischi informatici di cui all'articolo 6, paragrafo 1, vigila su tale attuazione e ne e' responsabile.

   Ai fini del primo comma, l'organo di gestione:

   a) assume la responsabilita' finale per la gestione dei rischi informatici dell'entita' finanziaria;
   b) predispone politiche miranti a garantire il mantenimento di standard elevati di disponibilita', autenticita', integrita' e riservatezza dei dati;
   c) definisce chiaramente ruoli e responsabilita' per tutte le funzioni connesse alle TIC e stabilisce adeguati meccanismi di governance al fine di garantire una comunicazione, una cooperazione e un coordinamento efficaci e tempestivi tra tali funzioni;
   d) ha la responsabilita' generale di definire e approvare la strategia di resilienza operativa digitale di cui all'articolo 6, paragrafo 8, compresa la determinazione del livello appropriato di tolleranza per i rischi informatici dell'entita' finanziaria, ai sensi dell'articolo 6, paragrafo 8, lettera b);
   e) approva, supervisiona e riesamina periodicamente l'attuazione della politica di continuita' operativa delle TIC e dei piani di risposta e ripristino relativi alle TIC dell'entita' finanziaria, di cui rispettivamente all'articolo 11, paragrafi 1 e 3, che possono essere adottati come politica specifica dedicata che costituisce parte integrante della politica generale di continuita' operativa e del piano di risposta e ripristino dell'entita' finanziaria;
   f) approva e riesamina periodicamente i piani interni di audit in materia di TIC dell'entita' finanziaria, gli audit in materia di TIC e le piu' importanti modifiche a essi apportate;
   g) assegna e riesamina periodicamente le risorse finanziarie adeguate per soddisfare le esigenze di resilienza operativa digitale dell'entita' finanziaria rispetto a tutti i tipi di risorse, compresi i pertinenti programmi di sensibilizzazione sulla sicurezza delle TIC e le attivita' di formazione sulla resilienza operativa digitale di cui all'articolo 13, paragrafo 6, nonche' le competenze in materia di TIC per tutto il personale;
   h) approva e riesamina periodicamente la politica dell'entita' finanziaria relativa alle modalita' per l'uso dei servizi TIC prestati dal fornitore terzo di servizi TIC;
   i) istituisce a livello aziendale canali di comunicazione che gli consentono di essere debitamente informato in merito a quanto segue:
      i) gli accordi conclusi con i fornitori terzi di servizi TIC sull'uso di tali servizi,
      ii) le relative eventuali modifiche importanti e pertinenti previste riguardo ai fornitori terzi di servizi TIC,
      iii) il potenziale impatto di tali modifiche sulle funzioni essenziali o importanti soggette agli accordi in questione, compresa una sintesi dell'analisi del rischio per valutare l'impatto di tali modifiche, nonche' almeno i gravi incidenti TIC e il loro impatto, le misure di risposta e ripristino e le misure correttive.

3. Le entita' finanziarie diverse dalle microimprese istituiscono un ruolo al fine di monitorare gli accordi conclusi con i fornitori terzi di servizi TIC per l'uso di tali servizi, oppure designano un dirigente di rango elevato quale responsabile della sorveglianza sulla relativa esposizione al rischio e sulla documentazione pertinente.

4. I membri dell'organo di gestione dell'entita' finanziaria mantengono attivamente aggiornate conoscenze e competenze adeguate per comprendere e valutare i rischi informatici e il loro impatto sulle operazioni dell'entita' finanziaria, anche seguendo una formazione specifica su base regolare, commisurata ai rischi informatici gestiti.

### Sezione II

### Articolo 6 - Quadro per la gestione dei rischi informatici

1. Nell'ambito del sistema di gestione globale del rischio, le entita' finanziarie predispongono un quadro per la gestione dei rischi informatici solido, esaustivo e adeguatamente documentato, che consenta loro di affrontare i rischi informatici in maniera rapida, efficiente ed esaustiva, assicurando un elevato livello di resilienza operativa digitale.

2. Il quadro per la gestione dei rischi informatici comprende almeno strategie, politiche, procedure, protocolli e strumenti in materia di TIC necessari per proteggere debitamente e adeguatamente tutti i patrimoni informativi e i risorse TIC, compresi software, hardware e server, nonche' tutte le pertinenti infrastrutture e componenti fisiche, quali i locali, i centri di elaborazione dati e le aree designate come sensibili, cosi' da garantire che tutti i patrimoni informativi e i risorse TIC siano adeguatamente protetti contro i rischi, compresi i danneggiamenti e l'accesso o l'uso non autorizzati.

3. Conformemente al proprio quadro per la gestione dei rischi informatici, le entita' finanziarie riducono al minimo l'impatto dei rischi informatici applicando strategie, politiche, procedure, protocolli e strumenti in materia di TIC adeguati. Forniscono alle autorita' competenti, su richiesta di queste ultime, informazioni complete e aggiornate sui rischi informatici e sul proprio quadro per la gestione dei rischi informatici.

4. Le entita' finanziarie diverse dalle microimprese attribuiscono la responsabilita' della gestione e della sorveglianza dei rischi informatici a una funzione di controllo, di cui assicurano un livello appropriato d'indipendenza per evitare conflitti d'interessi. Le entita' finanziarie garantiscono un'opportuna separazione e indipendenza tra funzioni di gestione dei rischi informatici, funzioni di controllo e funzioni di audit interno, secondo il modello delle tre linee di difesa o secondo un modello interno di controllo e gestione del rischio.

5. Il quadro per la gestione dei rischi informatici e' documentato e riesaminato almeno una volta all'anno, o periodicamente in caso di microimprese, nonche' in occasione di gravi incidenti TIC e in seguito a indicazioni o conclusioni delle autorita' di vigilanza formulate a seguito di pertinenti test di resilienza operativa digitale o di processi di audit. Il quadro e' costantemente migliorato sulla base degli insegnamenti tratti dall'attuazione e dal monitoraggio. E' presentata all'autorita' competente, su sua richiesta, una relazione in merito al riesame del quadro per la gestione dei rischi informatici.

6. Il quadro per la gestione dei rischi informatici delle entita' finanziarie, diverse dalle microimprese, e' sottoposto periodicamente a verifiche di audit interne effettuate da addetti all'audit in linea con i piani di audit delle entita' finanziarie. Tali addetti all'audit possiedono conoscenze, competenze ed esperienze adeguate in materia di rischi informatici, nonche' un'adeguata indipendenza. La frequenza e l'oggetto delle verifiche di audit in materia di TIC sono commisurati ai rischi connessi alle TIC cui e' esposta l'entita' finanziaria.

7. Sulla base delle conclusioni dell'audit interno in materia di TIC, le entita' finanziarie istituiscono un procedimento formale per darvi seguito, comprendente regole per la verifica tempestiva delle risultanze critiche e l'adozione di rimedi.

8. Il quadro per la gestione dei rischi informatici comprende una strategia di resilienza operativa digitale che definisce le modalita' di attuazione del quadro. A tal fine la strategia di resilienza operativa digitale include metodi per affrontare i rischi informatici e conseguire specifici obiettivi in materia di TIC:

   a) spiegando in che modo il quadro per la gestione dei rischi informatici sostiene gli obiettivi e la strategia commerciale dell'entita' finanziaria;
   b) fissando il livello di tolleranza per i rischi informatici, conformemente alla propensione al rischio dell'entita' finanziaria e analizzando la tolleranza d'impatto per le perturbazioni a livello di TIC;
   c) indicando chiari obiettivi in materia di sicurezza delle informazioni, compresi indicatori chiave di prestazione e parametri chiave di rischio;
   d) spiegando l'architettura di riferimento a livello di TIC e le eventuali modifiche necessarie per conseguire specifici obiettivi commerciali;
   e) delineando i differenti meccanismi introdotti per individuare incidenti connessi alle TIC, prevenire il loro impatto e proteggersi dallo stesso;
   f) documentando l'attuale situazione di resilienza operativa digitale sulla base del numero di gravi incidenti TIC segnalati, nonche' l'efficacia delle misure preventive;
   g) attuando test di resilienza operativa digitale, conformemente al capo IV del presente regolamento;
   h) delineando una strategia di comunicazione in caso di incidenti connessi alle TIC di cui e' richiesta la divulgazione a norma dell'articolo 14.

9. Le entita' finanziarie possono, nel contesto della strategia di resilienza operativa digitale di cui al paragrafo 8, definire una strategia olistica per le TIC a livello di gruppo o di entita', basata su una varieta' di fornitori, che indichi le principali dipendenze da fornitori terzi di servizi TIC e che spieghi la logica sottesa alla ripartizione degli appalti tra i fornitori terzi di servizi TIC.

10. Le entita' finanziarie possono, conformemente alla normativa settoriale dell'Unione e nazionale, esternalizzare a imprese interne o esterne al gruppo i compiti di verifica della conformita' ai requisiti in materia di gestione dei rischi informatici. In caso di esternalizzazione, l'entita' finanziaria rimane pienamente responsabile di verificare la conformita' ai requisiti in materia di gestione dei rischi informatici.

### Articolo 7 - Sistemi, protocolli e strumenti di TIC

Al fine di affrontare e gestire i rischi informatici, le entita' finanziarie utilizzano e mantengono aggiornati sistemi, protocolli e strumenti di TIC che sono:

a) idonei alle dimensioni delle operazioni a supporto dello svolgimento delle attivita' delle entita' finanziarie, conformemente al principio di proporzionalita' di cui all'articolo 4;
b) affidabili;
c) dotati di capacita' sufficiente per elaborare in maniera accurata i dati necessari per lo svolgimento delle attivita' e la tempestiva fornitura dei servizi, nonche' per sostenere i picchi di volume di ordini, messaggi od operazioni, a seconda delle necessita', anche in caso di introduzione di nuove tecnologie;
d) tecnologicamente resilienti, in modo da fare adeguatamente fronte alle esigenze di informazioni supplementari richieste da condizioni di stress del mercato o da altre situazioni avverse.

### Articolo 8 - Identificazione

1. Nell'ambito del quadro per la gestione dei rischi informatici di cui all'articolo 6, paragrafo 1, le entita' finanziarie identificano, classificano e documentano adeguatamente tutte le funzioni commerciali supportate dalle TIC, i ruoli e le responsabilita', i patrimoni informativi e le risorse TIC a supporto delle suddette funzioni, nonche' i ruoli e le dipendenze rispettivi in materia di rischi informatici. Le entita' finanziarie riesaminano, secondo necessita' e almeno una volta all'anno, l'adeguatezza di tale classificazione e di altri documenti eventualmente pertinenti.

2. Le entita' finanziarie identificano costantemente tutte le fonti di rischio relative alle TIC, in particolare l'esposizione al rischio da e verso altre entita' finanziarie, e valutano le minacce informatiche e le vulnerabilita' in materia di TIC pertinenti per le loro funzioni commerciali supportate dalle TIC, per i loro patrimoni informativi e per i loro risorse TIC. Le entita' finanziarie riesaminano periodicamente, e almeno una volta all'anno, gli scenari di rischio che esercitano un impatto su di loro.

3. Le entita' finanziarie diverse dalle microimprese effettuano una valutazione del rischio in occasione di ogni modifica di rilievo dell'infrastruttura del sistema informatico e di rete, dei processi o delle procedure che incidono sulle loro funzioni commerciali supportate dalle TIC, sui loro patrimoni informativi o sui loro risorse TIC.

4. Le entita' finanziarie identificano tutti i patrimoni informativi e le risorse TIC, compresi quelli su siti remoti, le risorse di rete e le attrezzature hardware, e mappano quelle considerate essenziali. Effettuano la mappatura della configurazione dei patrimoni informativi e delle risorse TIC, nonche' dei collegamenti e delle interdipendenze tra i diversi patrimoni informativi e risorse TIC.

5. Le entita' finanziarie identificano e documentano tutti i processi dipendenti da fornitori terzi di servizi TIC e identificano le interconnessioni con detti fornitori che offrono servizi a supporto di funzioni essenziali o importanti.

6. Ai fini dei paragrafi 1, 4 e 5, le entita' finanziarie mantengono inventari pertinenti e li aggiornano periodicamente e in occasione di ogni modifica di rilievo di cui al paragrafo 3.

7. Le entita' finanziarie diverse dalle microimprese effettuano periodicamente, almeno una volta all'anno e in ogni caso prima e dopo la connessione di tecnologie, applicazioni o sistemi, una valutazione del rischio specifica per tutti i sistemi legacy.

### Articolo 9 - Protezione e prevenzione

1. Allo scopo di proteggere adeguatamente i sistemi di TIC e nella prospettiva di organizzare misure di risposta, le entita' finanziarie monitorano e controllano costantemente la sicurezza e il funzionamento dei sistemi e degli strumenti di TIC e riducono al minimo l'impatto dei rischi informatici sui sistemi di TIC adottando politiche, procedure e strumenti adeguati per la sicurezza delle TIC.

2. Le entita' finanziarie definiscono, acquisiscono e attuano politiche, procedure, protocolli e strumenti per la sicurezza delle TIC miranti a garantire la resilienza, la continuita' e la disponibilita' dei sistemi di TIC, in particolare quelli a supporto di funzioni essenziali o importanti, nonche' a mantenere standard elevati di disponibilita', autenticita', integrita' e riservatezza dei dati conservati, in uso o in transito.

3. Al fine di conseguire gli obiettivi di cui al paragrafo 2 le entita' finanziarie usano soluzioni e processi TIC appropriati conformemente all'articolo 4. Tali soluzioni e processi TIC:

   a) garantiscono la sicurezza dei mezzi di trasferimento dei dati;
   b) riducono al minimo i rischi di corruzione o perdita di dati, di accesso non autorizzato nonche' di difetti tecnici che possono ostacolare l'attivita' commerciale;
   c) prevengono la mancanza di disponibilita', il deterioramento dell'autenticita' o dell'integrita', le violazioni della riservatezza e la perdita di dati;
   d) assicurano la protezione dei dati contro i rischi derivanti dalla gestione dei dati, compresi la cattiva amministrazione, i rischi relativi al trattamento dei dati e l'errore umano.

4. All'interno del quadro per la gestione dei rischi informatici di cui all'articolo 6, paragrafo 1, le entita' finanziarie:

   a) elaborano e documentano una politica di sicurezza dell'informazione che definisce le norme per tutelare la disponibilita', l'autenticita', l'integrita' e la riservatezza dei dati, dei patrimoni informativi e delle risorse TIC, compresi quelli dei loro clienti, se del caso;
   b) seguendo un approccio basato sul rischio, realizzano una solida struttura di gestione della rete e delle infrastrutture impiegando tecniche, metodi e protocolli adeguati, che possono includere l'applicazione di meccanismi automatizzati, per isolare i patrimoni informativi colpiti in caso di attacchi informatici;
   c) attuano politiche che limitano l'accesso fisico o logico ai patrimoni informativi e alle risorse TIC unicamente a quanto e' necessario per funzioni e attivita' legittime e approvate, e stabiliscono a tale scopo una serie di politiche, procedure e controlli concernenti i diritti di accesso e garantiscono una solida amministrazione degli stessi;
   d) attuano politiche e protocolli riguardanti robusti meccanismi di autenticazione, basati su norme pertinenti e sistemi di controllo dedicati, e misure di protezione delle chiavi crittografiche di cifratura dei dati sulla scorta dei risultati di processi approvati per la classificazione dei dati e la valutazione dei rischi informatici;
   e) attuano politiche, procedure e controlli documentati per la gestione delle modifiche delle TIC, comprese le modifiche apportate a componenti software, hardware e firmware, sistemi o parametri di sicurezza, che adottano un approccio basato sulla valutazione del rischio e sono parte integrante del processo complessivo di gestione delle modifiche dell'entita' finanziaria, in modo che tutte le modifiche apportate ai sistemi di TIC siano registrate, testate, valutate, approvate, attuate e verificate in maniera controllata;
   f) si dotano di politiche documentate, idonee ed esaustive in materia di correzioni ed aggiornamenti.

   Ai fini della lettera b) del primo comma, le entita' finanziarie progettano l'infrastruttura di connessione di rete in modo che sia possibile isolarla o segmentarla istantaneamente, al fine di ridurre al minimo e prevenire il contagio, soprattutto per i processi finanziari interconnessi.

   Ai fini della lettera e) del primo comma, il processo di gestione delle modifiche delle TIC e' approvato da linee di gestione adeguate e comprende protocolli specifici in essere.

### Articolo 10 - Individuazione

1. Le entita' finanziarie predispongono meccanismi per individuare tempestivamente le attivita' anomale, conformemente all'articolo 17, compresi i problemi di prestazione della rete delle TIC e gli incidenti a esse connessi, nonche' per individuare i potenziali singoli punti di vulnerabilita' (points of failure) importanti.

   Tutti i meccanismi di individuazione di cui al primo comma sono periodicamente testati in conformita' dell'articolo 25.

2. I meccanismi di individuazione di cui al paragrafo 1 prevedono molteplici livelli di controllo, definiscono soglie di allarme e criteri per l'attivazione e l'avvio dei processi di risposta agli incidenti connessi alle TIC, compresi meccanismi di allarme automatico per il personale incaricato della risposta agli incidenti connessi alle TIC.

3. Le entita' finanziarie dedicano risorse e capacita' sufficienti al monitoraggio dell'attivita' degli utenti e di eventuali anomalie e incidenti connessi alle TIC, in particolare attacchi informatici.

4. I fornitori di servizi di comunicazione dati predispongono inoltre sistemi in grado di controllare efficacemente le comunicazioni sulle operazioni per verificarne la completezza, individuare omissioni ed errori palesi e chiederne la ritrasmissione.

### Articolo 11 - Risposta e ripristino

1. All'interno del quadro per la gestione dei rischi informatici di cui all'articolo 6, paragrafo 1, e in base ai requisiti di identificazione stabiliti all'articolo 8, le entita' finanziarie predispongono una politica di continuita' operativa delle TIC esaustiva, la quale puo' essere adottata come una politica specifica dedicata che costituisce parte integrante della politica generale di continuita' operativa dell'entita' finanziaria.

2. Le entita' finanziarie attuano la politica di continuita' operativa delle TIC tramite accordi, piani, procedure e meccanismi appositi, appropriati e documentati, miranti a:

   a) garantire la continuita' delle funzioni essenziali o importanti dell'entita' finanziaria;
   b) rispondere in maniera rapida, appropriata ed efficace e trovare una soluzione a tutti gli incidenti connessi alle TIC, in modo da limitare i danni e privilegiare la ripresa delle attivita' e le azioni di ripristino;
   c) attivare senza ritardo piani dedicati che prevedano tecnologie, processi e misure di contenimento idonei a ciascun tipo di incidente connesso alle TIC e a scongiurare danni ulteriori, nonche' procedure mirate di risposta e ripristino stabilite in conformita' dell'articolo 12;
   d) stimare in via preliminare impatti, danni e perdite;
   e) stabilire azioni di comunicazione e gestione delle crisi che assicurino la trasmissione di informazioni aggiornate a tutto il personale interno interessato e ai portatori di interessi esterni, conformemente all'articolo 14, e comunicare tali informazioni alle autorita' competenti, conformemente all'articolo 19.

3. All'interno del quadro per la gestione dei rischi informatici di cui all'articolo 6, paragrafo 1, le entita' finanziarie attuano i piani di risposta e ripristino relativi alle TIC associati; per le entita' finanziarie diverse dalle microimprese tali piani sono soggetti a un audit interno indipendente.

4. Le entita' finanziarie predispongono, mantengono e testano periodicamente opportuni piani di continuita' operativa delle TIC, in particolare per quanto riguarda le funzioni essenziali o importanti esternalizzate o appaltate tramite accordi con fornitori terzi di servizi TIC.

5. Nell'ambito della politica generale di continuita' operativa, le entita' finanziarie effettuano un'analisi dell'impatto sulle attivita' aziendali (Business Impact Analysis - BIA) delle loro esposizioni a gravi perturbazioni delle attivita'. Nel quadro della BIA, le entita' finanziarie valutano l'impatto potenziale di gravi perturbazioni delle attivita' mediante criteri quantitativi e qualitativi, utilizzando, se del caso, dati interni ed esterni e analisi di scenario. La BIA tiene conto della criticita' delle funzioni commerciali, dei processi di supporto, delle dipendenze da terzi e dei patrimoni informativi individuati e mappati, nonche' delle loro interdipendenze. Le entita' finanziarie provvedono affinche' le risorse TIC e i servizi TIC siano progettati e utilizzati in piena conformita' con la BIA, in particolare garantendo adeguatamente la ridondanza di tutte le componenti essenziali.

6. All'interno della gestione complessiva dei rischi informatici, le entita' finanziarie:

   a) testano i piani di continuita' operativa delle TIC e i piani di risposta e ripristino relativi alle TIC in relazione ai sistemi di TIC a supporto di tutte le funzioni almeno una volta all'anno nonche' in caso di modifiche di rilievo ai sistemi di TIC a supporto di funzioni essenziali o importanti;
   b) testano i piani di comunicazione delle crisi istituiti in conformita' dell'articolo 14.

   Ai fini del primo comma, lettera a), le entita' finanziarie diverse dalle microimprese inseriscono nei piani dei test scenari di attacchi informatici e del passaggio tra le infrastrutture delle TIC primarie e la capacita' ridondante, i backup e le attrezzature ridondanti necessarie per soddisfare gli obblighi di cui all'articolo 12.

   Le entita' finanziarie riesaminano periodicamente la politica di continuita' operativa delle TIC e i piani di risposta e ripristino relativi alle TIC, tenendo conto dei risultati dei test svolti in conformita' del primo comma e delle raccomandazioni formulate sulla base dei controlli di audit o degli esami di vigilanza.

7. Le entita' finanziarie diverse dalle microimprese si dotano di una funzione di gestione delle crisi che, in caso di attivazione dei piani di continuita' operativa delle TIC o dei piani di risposta e ripristino relativi alle TIC, fissa, tra l'altro, procedure chiare per la gestione della comunicazione interna ed esterna delle crisi, in conformita' dell'articolo 14.

8. Le entita' finanziarie rendono prontamente accessibili le registrazioni delle attivita' svolte prima e durante le perturbazioni in cui vengono attivati i piani di continuita' operativa delle TIC e i piani di risposta e ripristino relativi alle TIC.

9. Le controparti centrali trasmettono alle autorita' competenti copie dei risultati dei test di continuita' operativa delle TIC o di esercizi analoghi.

10. Le entita' finanziarie, diverse dalle microimprese, comunicano alle autorita' competenti, su richiesta di queste ultime, una stima dei costi e delle perdite annuali aggregati causati da incidenti gravi connessi alle TIC.

11. A norma dell'articolo 16 dei regolamenti (UE) n. 1093/2010, (UE) n. 1094/2010 e (UE) n. 1095/2010, le AEV elaborano, tramite il comitato congiunto, entro il [18 mesi dalla data di entrata in vigore del presente regolamento] orientamenti comuni sulla stima dei costi e delle perdite annuali aggregati di cui al paragrafo 10.

### Articolo 12 - Politiche e procedure di backup - Procedure e metodi di ripristino e recupero

1. Al fine di assicurare che i sistemi e i dati di TIC siano ripristinati riducendo al minimo il periodo di inattivita' e limitando la perturbazione e le perdite, all'interno del proprio quadro per la gestione dei rischi informatici le entita' finanziarie elaborano e documentano:

   a) le politiche e procedure di backup che precisano il perimetro dei dati soggetti a backup e la frequenza minima del backup, in base alla criticita' delle informazioni o al livello di riservatezza dei dati;
   b) le procedure e i metodi di ripristino e recupero.

2. Le entita' finanziarie si dotano di sistemi di backup che possono essere attivati conformemente alle politiche e alle procedure di backup, come pure alle procedure e ai metodi di ripristino e recupero. L'attivazione dei sistemi di backup non mette a repentaglio la sicurezza dei sistemi informatici e di rete ne', la disponibilita', l'autenticita', l'integrita' o la riservatezza dei dati. I test delle procedure di backup e di ripristino nonche' delle procedure e dei metodi di recupero sono effettuati periodicamente.

3. Nel ripristino dei dati di backup effettuato utilizzando i propri sistemi, le entita' finanziarie impiegano sistemi di TIC che sono fisicamente e logicamente segregati dal sistema di TIC sorgente. I sistemi di TIC sono protetti in maniera sicura da qualsiasi accesso non autorizzato o corruzione delle TIC e consentono il tempestivo ripristino dei servizi attraverso il backup dei dati e dei sistemi ove necessario.

   Per le controparti centrali, i piani di ripristino consentono il ripristino di tutte le operazioni in corso al momento della perturbazione, cosi' da permettere alla controparte centrale di continuare a operare con certezza e di completare la liquidazione alla data programmata.

   I fornitori di servizi di comunicazione dati mantengono inoltre risorse adeguate e dispongono di attrezzature di back-up e ripristino per offrire e mantenere in ogni momento i loro servizi.

4. Le entita' finanziarie, diverse dalle microimprese, mantengono capacita' di TIC ridondanti, dotate di risorse e funzioni sufficienti e adeguate a soddisfare le esigenze commerciali. Le microimprese valutano la necessita' di mantenere tali capacita' di TIC ridondanti sulla base del loro profilo di rischio.

5. I depositari centrali di titoli mantengono almeno un sito secondario di trattamento dati dotato di risorse, capacita', funzioni e personale adeguati a soddisfare le esigenze commerciali.

   Il sito secondario di trattamento dati e':
   a) ubicato geograficamente a distanza dal sito primario per garantire che esso abbia un profilo di rischio distinto e impedire che venga colpito dall'evento che ha interessato il sito primario;
   b) in grado di garantire la continuita' delle funzioni essenziali o importanti in maniera identica al sito primario, oppure di fornire il livello di servizi necessario a garantire che l'entita' finanziaria svolga le proprie operazioni essenziali nell'ambito degli obiettivi di ripristino;
   c) immediatamente accessibile al personale dell'entita' finanziaria per garantire la continuita' delle funzioni essenziali o importanti qualora il sito primario di trattamento dati divenga indisponibile.

6. Nel determinare gli obiettivi in materia di punti di ripristino e tempi di ripristino di ciascuna funzione, le entita' finanziarie tengono conto del fatto che si tratti di una funzione essenziale o importante e del potenziale impatto complessivo sull'efficienza del mercato. Questi obiettivi in materia di tempi garantiscono che i livelli di servizi concordati siano rispettati anche in scenari estremi.

7. Durante il ripristino successivo a un incidente connesso alle TIC, le entita' finanziarie effettuano le verifiche necessarie, comprese eventuali verifiche multiple e controlli incrociati, per assicurare che sia mantenuto il piu' elevato livello di integrita' dei dati. Questi controlli sono effettuati anche al momento di ricostruire i dati provenienti da portatori di interessi esterni, per assicurare la piena coerenza di tutti i dati tra i sistemi.

### Articolo 13 - Apprendimento ed evoluzione

1. Le entita' finanziarie dispongono capacita' e personale per raccogliere informazioni in relazione alle vulnerabilita' e alle minacce informatiche, agli incidenti connessi alle TIC, in particolare agli attacchi informatici, e analizzarne i probabili effetti sulla loro resilienza operativa digitale.

2. Dopo che un grave incidente connesso alle TIC ha perturbato le loro attivita' principali, le entita' finanziarie svolgono un riesame successivo a tale incidente che analizzi le cause della perturbazione e identifichi i miglioramenti che e' necessario apportare alle operazioni riguardanti le TIC o nell'ambito della politica di continuita' operativa delle TIC di cui all'articolo 11.

   Le entita' finanziarie diverse dalle microimprese comunicano, su richiesta, alle autorita' competenti le modifiche attuate a seguito del riesame successivo all'incidente connesso alle TIC di cui al primo comma.

   Il riesame successivo all'incidente connesso alle TIC di cui al primo comma determina se le procedure stabilite siano state seguite e se le azioni adottate siano state efficaci, anche in relazione:

   a) alla tempestivita' della risposta agli allarmi di sicurezza e alla determinazione dell'impatto degli incidenti connessi alle TIC e della loro gravita';
   b) alla qualita' e alla rapidita' dell'analisi forense, ove ritenuto opportuno;
   c) all'efficacia della procedura di attivazione dei livelli successivi di intervento in caso di incidenti all'interno dell'entita' finanziaria;
   d) all'efficacia della comunicazione interna ed esterna.

3. Gli insegnamenti tratti dai test sulla resilienza operativa digitale effettuati in conformita' degli articoli 26 e 27 e da incidenti connessi alle TIC realmente avvenuti (in particolare attacchi informatici), insieme alle difficolta' riscontrate al momento dell'attivazione dei piani di continuita' operativa delle TIC e dei piani di risposta e ripristino relativi alle TIC, nonche' le informazioni pertinenti scambiate con le controparti e valutate nel corso degli esami di vigilanza sono debitamente e costantemente integrati nel processo di valutazione dei rischi informatici. Tali risultanze costituiscono la base per opportune revisioni delle relative componenti del quadro per la gestione dei rischi informatici di cui all'articolo 6, paragrafo 1.

4. Le entita' finanziarie monitorano l'efficacia dell'attuazione della loro strategia di resilienza operativa digitale stabilita all'articolo 6, paragrafo 8. Tracciano l'evoluzione nel tempo dei rischi informatici, analizzano la frequenza, i tipi, le dimensioni e l'evoluzione degli incidenti connessi alle TIC, in particolare gli attacchi informatici e i relativi schemi, al fine di comprendere il livello di esposizione ai rischi informatici - segnatamente in relazione alle funzioni essenziali o importanti - e migliorare la maturita' informatica e la preparazione dell'entita' finanziaria.

5. Il personale addetto alle TIC di grado piu' elevato comunica almeno una volta all'anno all'organo di gestione le risultanze di cui al paragrafo 3 e formula raccomandazioni.

6. Le entita' finanziarie elaborano programmi di sensibilizzazione sulla sicurezza delle TIC nonche' attivita' di formazione sulla resilienza operativa digitale, che rappresentano moduli obbligatori nei programmi di formazione del personale. Tali programmi e attivita' di formazione riguardano tutti i dipendenti e gli alti dirigenti, e presentano un livello di complessita' commisurato all'ambito delle loro funzioni. Se del caso, le entita' finanziarie includono anche i fornitori terzi di servizi TIC nei loro sistemi di formazione pertinenti, conformemente all'articolo 30, paragrafo 2, lettera i).

7. Le entita' finanziarie diverse dalle microimprese monitorano costantemente i pertinenti sviluppi tecnologici, anche al fine di comprendere i possibili effetti dell'impiego di tali nuove tecnologie sui requisiti in materia di sicurezza delle TIC e sulla resilienza operativa digitale. Si tengono aggiornate sui piu' recenti processi di gestione dei rischi informatici, in modo da contrastare efficacemente le forme nuove o gia' esistenti di attacchi informatici.

### Articolo 14 - Comunicazione

1. All'interno del quadro per la gestione dei rischi informatici di cui all'articolo 6, paragrafo 1, le entita' finanziarie predispongono piani di comunicazione delle crisi che consentano una divulgazione responsabile di informazioni riguardanti, almeno, gravi incidenti connessi alle TIC o vulnerabilita' ai clienti e alle controparti nonche' al pubblico, a seconda dei casi.

2. All'interno del quadro per la gestione dei rischi informatici, le entita' finanziarie attuano politiche di comunicazione per il personale interno e per i portatori di interessi esterni. Le politiche di comunicazione per il personale tengono conto dell'esigenza di operare un distinguo tra il personale coinvolto nella gestione dei rischi informatici, in particolare il personale responsabile della risposta e del ripristino, e il personale che e' necessario informare.

3. Nell'entita' finanziaria vi e' almeno una persona incaricata di attuare la strategia di comunicazione per gli incidenti connessi alle TIC e assolvere a tal fine la funzione di informazione al pubblico e ai media.

### Articolo 15 - Ulteriore armonizzazione di strumenti, metodi, processi e politiche di gestione del rischio relativi alle TIC

Tramite il comitato congiunto e in consultazione con l'Agenzia dell'Unione europea per la cibersicurezza (ENISA), le AEV elaborano progetti di norme tecniche di regolamentazione comuni al fine di:

a) specificare ulteriori elementi da inserire nelle strategie, nelle politiche, nelle procedure, nei protocolli e negli strumenti in materia di sicurezza delle TIC di cui all'articolo 9, paragrafo 2, allo scopo di garantire la sicurezza delle reti, introdurre salvaguardie adeguate contro le intrusioni e l'uso improprio dei dati, preservare la disponibilita', l'autenticita', l'integrita' e la riservatezza dei dati, inserire tecniche crittografiche e assicurare un'accurata e pronta trasmissione dei dati senza gravi perturbazioni ne' indebiti ritardi;

b) sviluppare ulteriori componenti dei controlli sui diritti di gestione dell'accesso di cui all'articolo 9, paragrafo 4, lettera c), e della relativa politica di risorse umane, precisando i diritti di accesso, le procedure per concedere e revocare i diritti, il monitoraggio di comportamenti anomali in relazione ai rischi informatici mediante indicatori appropriati, compresi i modelli di utilizzo della rete, gli orari, l'attivita' informatica e i dispositivi sconosciuti;

c) elaborare ulteriormente i meccanismi specificati all'articolo 10, paragrafo 1, in modo da consentire un'individuazione tempestiva delle attivita' anomale, e i criteri di cui all'articolo 10, paragrafo 2, per l'avvio dei processi di individuazione degli incidenti connessi alle TIC e di risposta agli stessi;

d) specificare ulteriormente le componenti della politica di continuita' operativa delle TIC di cui all'articolo 11, paragrafo 1;

e) specificare ulteriormente i test sui piani di continuita' operativa delle TIC di cui all'articolo 11, paragrafo 6, per garantire che tali test tengano debitamente conto degli scenari in cui la qualita' dell'esercizio di una funzione essenziale o importante si deteriora a un livello inaccettabile o viene meno, e che considerino adeguatamente il potenziale impatto dell'insolvenza o di altre disfunzioni di pertinenti fornitori terzi di servizi TIC e, se del caso, i rischi politici nelle giurisdizioni dei rispettivi fornitori;

f) specificare ulteriormente le componenti dei piani di risposta e ripristino relativi alle TIC di cui all'articolo 11, paragrafo 3;

g) specificare ulteriormente il contenuto e il formato della relazione sul riesame del quadro per la gestione dei rischi informatici di cui all'articolo 6, paragrafo 5.

All'atto dell'elaborazione di tali progetti di norme tecniche di regolamentazione, le AEV tengono conto delle dimensioni e del profilo di rischio complessivo dell'entita' finanziaria, nonche' della natura, della portata e della complessita' dei suoi servizi, delle sue attivita' e delle sue operazioni. Le AEV presentano tali progetti di norme tecniche di regolamentazione alla Commissione entro il [12 mesi dalla data di entrata in vigore del presente regolamento]. Alla Commissione e' delegato il potere di integrare il presente regolamento adottando le norme tecniche di regolamentazione di cui al primo comma in conformita' degli articoli da 10 a 14 dei regolamenti (UE) n. 1093/2010, (UE) n. 1094/2010 e (UE) n. 1095/2010.

### Articolo 16 - Quadro semplificato per la gestione dei rischi informatici

1. Gli articoli da 5 a 15 del presente regolamento non si applicano alle imprese di investimento piccole e non interconnesse e agli istituti di pagamento esentati a norma della direttiva (UE) 2015/2366; agli istituti esentati a norma della direttiva 2013/36/UE per i quali gli Stati membri hanno deciso di non applicare l'opzione di cui all'articolo 2, paragrafo 4, del presente regolamento; agli istituti di moneta elettronica esentati a norma della direttiva 2009/110/CE; e ai piccoli enti pensionistici aziendali o professionali.

   Fermo restando il primo comma, le entita' elencate al primo comma:

   a) pongono in essere e mantengono un solido e documentato quadro per la gestione dei rischi informatici che precisa i meccanismi e le misure finalizzate a una gestione rapida, efficiente e organica dei rischi informatici, anche ai fini della protezione delle pertinenti infrastrutture e componenti fisiche;
   b) monitorano costantemente la sicurezza e il funzionamento di tutti i sistemi di TIC;
   c) riducono al minimo l'impatto dei rischi informatici attraverso l'uso di sistemi, protocolli e strumenti di TIC solidi, resilienti e aggiornati e atti a supportare lo svolgimento delle loro attivita' e la fornitura di servizi e a proteggere adeguatamente la disponibilita', l'autenticita', l'integrita' e la riservatezza dei dati nei sistemi informatici e di rete;
   d) provvedono a che le fonti di rischi informatici e le anomalie dei sistemi informatici e di rete siano tempestivamente individuate e rilevate e che gli incidenti connessi alle TIC siano trattati con rapidita';
   e) individuano le principali dipendenze da fornitori terzi di servizi TIC;
   f) garantiscono la continuita' delle funzioni essenziali o importanti, attraverso piani di continuita' operativa e misure di risposta e recupero, che comprendano almeno misure di back-up e ripristino;
   g) testano periodicamente i piani e le misure di cui alla lettera f) nonche' l'efficacia dei controlli attuati in conformita' delle lettere a) e c);
   h) attuano, se del caso, le opportune conclusioni operative risultanti dai test di cui alla lettera g) e dall'analisi successiva all'incidente nel processo di valutazione dei rischi informatici ed elaborano, in funzione delle esigenze e del profilo dei rischi informatici, programmi di formazione e sensibilizzazione sulla sicurezza delle TIC per il personale e la dirigenza.

2. Il quadro per la gestione dei rischi informatici di cui al paragrafo 1, secondo comma, lettera a), e' documentato e riesaminato periodicamente e al verificarsi di incidenti gravi connessi alle TIC conformemente alle istruzioni delle autorita' di vigilanza. Il quadro e' costantemente migliorato sulla base degli insegnamenti tratti dall'attuazione e dal monitoraggio. Su sua richiesta, e' presentata all'autorita' competente una relazione sul riesame del quadro per la gestione dei rischi informatici.

3. Tramite il comitato congiunto e in consultazione con l'ENISA, le AEV elaborano progetti di norme tecniche di regolamentazione comuni al fine di specificare ulteriormente gli elementi da includere nel quadro per la gestione dei rischi informatici (par. 1, secondo comma, lettera a); gli elementi relativi ai sistemi, protocolli e strumenti per ridurre al minimo l'impatto dei rischi informatici (par. 1, secondo comma, lettera c); le componenti dei piani di continuita' operativa delle TIC (par. 1, secondo comma, lettera f); le norme riguardanti i test sui piani di continuita' operativa e l'efficacia dei controlli (par. 1, secondo comma, lettera g); il contenuto e il formato della relazione sul riesame del quadro (par. 2). Le AEV presentano detti progetti alla Commissione entro il [12 mesi dalla data di entrata in vigore del presente regolamento].

---

## Capo III - Gestione, classificazione e segnalazione degli incidenti informatici (Pillar 2)

### Articolo 17 - Processo di gestione degli incidenti connessi alle TIC

1. Le entita' finanziarie definiscono, stabiliscono e attuano un processo di gestione degli incidenti connessi alle TIC al fine di individuare, gestire e notificare tali incidenti.

2. Le entita' finanziarie registrano tutti gli incidenti connessi alle TIC e le minacce informatiche significative. Le entita' finanziarie istituiscono procedure e processi appropriati per garantire, in maniera coerente e integrata, il monitoraggio e il trattamento degli incidenti connessi alle TIC, nonche' il relativo seguito, in modo da identificare, documentare e affrontare le cause di fondo e prevenire il verificarsi di tali incidenti.

3. Il processo di gestione degli incidenti connessi alle TIC di cui al paragrafo 1:

   a) predispone indicatori di allerta precoce;
   b) stabilisce procedure per identificare, tracciare, registrare, categorizzare e classificare gli incidenti connessi alle TIC in base alla loro priorita' e gravita' e in base alla criticita' dei servizi colpiti, conformemente ai criteri di cui all'articolo 18, paragrafo 1;
   c) assegna i ruoli e le responsabilita' che e' necessario attivare per i diversi scenari e tipi di incidenti connessi alle TIC;
   d) elabora piani per la comunicazione al personale, ai portatori di interessi esterni e ai mezzi di comunicazione conformemente all'articolo 14, nonche' per la notifica ai clienti, per le procedure di attivazione dei livelli successivi di intervento, compresi i reclami dei clienti in materia di TIC, e per la comunicazione di informazioni alle entita' finanziarie che agiscono da controparti, a seconda dei casi;
   e) assicura la segnalazione almeno degli incidenti gravi connessi alle TIC agli alti dirigenti interessati e informa l'organo di gestione almeno in merito a detti incidenti, illustrandone l'impatto e la risposta e i controlli supplementari da introdurre;
   f) stabilisce procedure di risposta agli incidenti connessi alle TIC per attenuarne l'impatto e garantisce tempestivamente l'operativita' e la sicurezza dei servizi.

### Articolo 18 - Classificazione degli incidenti connessi alle TIC e delle minacce informatiche

1. Le entita' finanziarie classificano gli incidenti connessi alle TIC e ne determinano l'impatto in base ai criteri seguenti:

   a) il numero e/o la rilevanza di clienti o controparti finanziarie interessati e, ove applicabile, la quantita' o il numero di transazioni interessate dall'incidente connesso alle TIC e il fatto che tale incidente abbia provocato o meno un impatto reputazionale;
   b) la durata dell'incidente connesso alle TIC, compreso il periodo di inattivita' del servizio;
   c) l'estensione geografica dell'incidente connesso alle TIC, con riferimento alle aree colpite, in particolare se interessa piu' di due Stati membri;
   d) le perdite di dati derivanti dall'incidente connesso alle TIC, in relazione alla disponibilita', autenticita', integrita' o riservatezza dei dati;
   e) la criticita' dei servizi colpiti, comprese le operazioni dell'entita' finanziaria;
   f) l'impatto economico dell'incidente connesso alle TIC - in particolare le perdite e i costi diretti e indiretti - in termini sia assoluti che relativi.

2. Le entita' finanziarie classificano le minacce informatiche come significative in base alla criticita' dei servizi a rischio, comprese le operazioni dell'entita' finanziaria, il numero e/o la rilevanza di clienti o controparti finanziarie interessati e l'estensione geografica delle aree a rischio.

3. In consultazione con la BCE e l'ENISA, le AEV elaborano, tramite il comitato congiunto, progetti di norme tecniche di regolamentazione comuni che specificano ulteriormente gli aspetti seguenti:

   a) i criteri di cui al paragrafo 1, comprese le soglie di rilevanza per la determinazione degli gravi incidenti TIC o, ove applicabile, dei gravi incidenti operativi o relativi alla sicurezza dei pagamenti, che sono oggetto dell'obbligo di segnalazione di cui all'articolo 19, paragrafo 1;
   b) i criteri che le autorita' competenti devono applicare per valutare la rilevanza degli gravi incidenti TIC o, ove applicabile, dei gravi incidenti operativi o relativi alla sicurezza dei pagamenti per le autorita' competenti interessate in altri Stati membri, nonche' i dettagli delle segnalazioni di incidenti gravi connessi alle TIC o, ove applicabile, di gravi incidenti operativi o di sicurezza dei pagamenti da condividere con altre autorita' competenti ai sensi dell'articolo 19, paragrafi 6 e 7;
   c) i criteri di cui al paragrafo 2 del presente articolo, comprese soglie di rilevanza elevate per la determinazione delle minacce informatiche significative.

4. All'atto dell'elaborazione dei progetti di norme tecniche di regolamentazione comuni di cui al paragrafo 3 del presente articolo, le AEV tengono conto dei criteri di cui all'articolo 4, paragrafo 2, come pure delle norme internazionali, degli orientamenti e delle specifiche elaborati e pubblicati dall'ENISA, tra cui, se del caso, le specifiche riguardanti altri settori economici. Ai fini dell'applicazione dei criteri di cui all'articolo 4, paragrafo 2, le AEV tengono debitamente conto della necessita' delle microimprese e delle piccole e medie imprese di mobilitare risorse e capacita' sufficienti per garantire una gestione rapida degli incidenti connessi alle TIC. Le AEV presentano tali progetti di norme tecniche di regolamentazione comuni alla Commissione entro il [12 mesi dalla data di entrata in vigore del presente regolamento].

### Articolo 19 - Segnalazione dei gravi incidenti TIC e notifica volontaria delle minacce informatiche significative

1. Le entita' finanziarie segnalano gli gravi incidenti TIC all'autorita' competente interessata di cui all'articolo 46 a norma del paragrafo 4 del presente articolo.

   Se un'entita' finanziaria e' soggetta alla vigilanza di piu' di un'autorita' nazionale competente di cui all'articolo 46, gli Stati membri designano un'unica autorita' competente quale autorita' competente interessata responsabile dell'espletamento delle funzioni e dei compiti di cui al presente articolo.

   Gli enti creditizi classificati come significativi ai sensi dell'articolo 6, paragrafo 4, del regolamento (UE) n. 1024/2013 segnalano i gravi incidenti TIC all'autorita' nazionale competente designata ai sensi dell'articolo 4 della direttiva 2013/36/UE, che trasmette immediatamente tale segnalazione alla BCE.

   Ai fini del primo comma, le entita' finanziarie redigono, dopo aver raccolto e analizzato tutte le informazioni pertinenti, la notifica iniziale e le relazioni di cui al paragrafo 4 del presente articolo utilizzando i modelli di cui all'articolo 20 e le trasmettono all'autorita' competente. Qualora un impedimento tecnico non consenta la trasmissione della notifica iniziale utilizzando il modello, le entita' finanziarie informano in merito l'autorita' competente con mezzi alternativi.

   La notifica iniziale e le relazioni di cui al paragrafo 4 contengono tutte le informazioni necessarie all'autorita' competente per determinare la rilevanza dell'grave incidente TIC e valutarne i possibili impatti transfrontalieri.

2. Le entita' finanziarie possono, su base volontaria, notificare le minacce informatiche significative all'autorita' competente interessata qualora ritengano che la minaccia sia rilevante per il sistema finanziario, gli utenti dei servizi o i clienti. L'autorita' competente interessata puo' fornire tali informazioni alle altre autorita' pertinenti di cui al paragrafo 6.

3. Qualora si verifichi un grave incidente TIC che eserciti un impatto sugli interessi finanziari dei clienti, le entita' finanziarie, senza indebito ritardo e non appena ne vengono a conoscenza, informano i loro clienti in merito a tale incidente e alle misure che sono state adottate per attenuare gli effetti avversi dell'incidente.

   In caso di minaccia informatica significativa, le entita' finanziarie, se del caso, informano i loro clienti potenzialmente interessati in merito alle opportune misure di protezione che i clienti stessi possono prendere in considerazione.

4. Entro i termini da fissare a norma dell'articolo 20, primo comma, lettera a), punto 2), le entita' finanziarie trasmettono all'autorita' competente interessata:

   a) una notifica iniziale;
   b) una relazione intermedia dopo la notifica iniziale di cui alla lettera a), non appena lo stato originario dell'incidente cambia in maniera significativa o il trattamento dell'grave incidente TIC cambia alla luce delle nuove informazioni disponibili, seguita, a seconda dei casi, da notifiche aggiornate, ogni qualvolta sia disponibile un aggiornamento della situazione, nonche' su specifica richiesta dell'autorita' competente;
   c) una relazione finale, quando l'analisi delle cause che hanno dato origine all'incidente sia stata completata, indipendentemente dal fatto che le misure di attenuazione siano gia' state attuate, e quando al posto delle stime siano disponibili i dati dell'impatto effettivo.

5. Ai sensi del presente articolo, le entita' finanziarie possono esternalizzare, conformemente al diritto settoriale dell'Unione e nazionale, gli obblighi di segnalazione a un fornitore terzo di servizi. In caso di esternalizzazione, l'entita' finanziaria rimane pienamente responsabile di espletare gli obblighi di segnalazione degli incidenti.

6. Dopo aver ricevuto la notifica iniziale e ciascuna delle relazioni di cui al paragrafo 4, l'autorita' competente trasmette tempestivamente i dettagli dell'grave incidente TIC all'ABE/ESMA/EIOPA, alla BCE (ove pertinente), alle autorita' competenti/CSIRT designate ai sensi della direttiva NIS2, alle autorita' di risoluzione e al Comitato di risoluzione unico (SRB) e ad altre pertinenti autorita' pubbliche ai sensi del diritto nazionale, sulla base delle rispettive competenze.

7. Una volta ricevute le informazioni conformemente al paragrafo 6, l'ABE, l'ESMA o l'EIOPA e la BCE, in consultazione con l'ENISA e in collaborazione con l'autorita' competente interessata, valutano la pertinenza dell'grave incidente TIC rispetto alle autorita' competenti in altri Stati membri. A seguito di tale valutazione, l'ABE, l'ESMA o l'EIOPA inviano una notifica al riguardo il prima possibile alle autorita' competenti interessate in altri Stati membri.

8. La notifica che l'ESMA deve effettuare a norma del paragrafo 7 del presente articolo lascia impregiudicata la responsabilita' dell'autorita' competente di trasmettere urgentemente i dettagli dell'grave incidente TIC all'autorita' pertinente dello Stato membro ospitante, laddove uno dei depositari centrali di titoli svolga una cospicua attivita' transfrontaliera nello Stato membro ospitante.

### Articolo 20 - Armonizzazione dei modelli e dei contenuti per la segnalazione

In consultazione con l'ENISA e la BCE, le AEV, tramite il comitato congiunto, elaborano:

a) progetti di norme tecniche di regolamentazione comuni per stabilire il contenuto delle segnalazioni relative agli incidenti gravi connessi alle TIC al fine di rispecchiare i criteri di cui all'articolo 18, paragrafo 1, e integrare ulteriori elementi; stabilire i termini della notifica iniziale e di ciascuna relazione di cui all'articolo 19, paragrafo 4; stabilire il contenuto della notifica per le minacce informatiche significative;

b) progetti di norme tecniche di attuazione comuni per stabilire i formati, i modelli e le procedure standard con cui le entita' finanziarie devono segnalare un grave incidente TIC e notificare una minaccia informatica significativa.

Le AEV trasmettono alla Commissione i progetti di cui al primo comma entro il [18 mesi dalla data di entrata in vigore del presente regolamento].

### Articolo 21 - Centralizzazione delle segnalazioni di incidenti gravi connessi alle TIC

1. In consultazione con la BCE e l'ENISA, le AEV, tramite il comitato congiunto, redigono una relazione congiunta che valuta la fattibilita' dell'ulteriore centralizzazione delle segnalazioni degli incidenti mediante l'istituzione di un polo UE unico per la segnalazione degli incidenti gravi connessi alle TIC da parte delle entita' finanziarie.

2. La relazione congiunta di cui al paragrafo 1 comprende almeno gli elementi seguenti: prerequisiti per l'istituzione di un polo UE unico; benefici, limiti e rischi; capacita' di interoperabilita'; elementi della gestione operativa; condizioni di adesione; modalita' tecniche per l'accesso; valutazione preliminare dei costi.

3. Le AEV presentano la relazione di cui al paragrafo 1 alla Commissione, al Parlamento europeo e al Consiglio entro il [24 mesi dalla data di entrata in vigore del presente regolamento].

### Articolo 22 - Riscontri forniti dalle autorita' di vigilanza

1. Fatti salvi il contributo tecnico, la consulenza o i rimedi e il successivo seguito dato che possono essere forniti, ove applicabile, conformemente al diritto nazionale, dai CSIRT ai sensi della direttiva NIS2, l'autorita' competente, dopo aver ricevuto la notifica iniziale e ciascuna delle relazioni di cui all'articolo 19, paragrafo 4, ne accusa ricevuta e puo', ove fattibile, fornire tempestivamente all'entita' finanziaria riscontri pertinenti e proporzionali o orientamenti di alto livello, in particolare rendendo disponibili le informazioni e i dati pertinenti anonimizzati su minacce analoghe, e puo' discutere rimedi applicati a livello di entita' finanziaria e metodi per ridurre al minimo e attenuare gli effetti avversi nel settore finanziario. Fatti salvi i riscontri ricevuti dalle autorita' di vigilanza, le entita' finanziarie restano pienamente responsabili del trattamento e delle conseguenze degli incidenti connessi alle TIC segnalati a norma dell'articolo 19, paragrafo 1.

2. Le AEV, tramite il comitato congiunto, riferiscono con frequenza annuale, sulla base di dati anonimizzati e aggregati, in merito agli incidenti gravi connessi alle TIC, i cui dettagli sono forniti dalle autorita' competenti a norma dell'articolo 19, paragrafo 6, indicando almeno il numero degli incidenti gravi connessi alle TIC, la natura, l'impatto sulle operazioni delle entita' finanziarie o dei clienti, i costi sostenuti e le azioni di riparazione adottate. Le AEV emanano segnalazioni di allerta e redigono statistiche di alto livello a supporto delle valutazioni della vulnerabilita' e delle minacce connesse alle TIC.

### Articolo 23 - Incidenti operativi o relativi alla sicurezza dei pagamenti riguardanti enti creditizi, istituti di pagamento, prestatori di servizi di informazione sui conti e istituti di moneta elettronica

I requisiti contenuti nel presente capo si applicano anche agli incidenti operativi o relativi alla sicurezza dei pagamenti ovvero ai gravi incidenti operativi o relativi alla sicurezza dei pagamenti allorche' riguardano enti creditizi, istituti di pagamento, prestatori di servizi di informazione sui conti e istituti di moneta elettronica.

---

## Capo IV - Test di resilienza operativa digitale (Pillar 3)

### Articolo 24 - Requisiti generali per lo svolgimento dei test di resilienza operativa digitale

1. Allo scopo di valutare la preparazione alla gestione degli incidenti connessi alle TIC, di identificare punti deboli, carenze e lacune della resilienza operativa digitale e di attuare tempestivamente misure correttive, le entita' finanziarie diverse dalle microimprese, tenuto conto dei criteri di cui all'articolo 4, paragrafo 2, stabiliscono, mantengono e riesaminano un programma di test di resilienza operativa digitale solido ed esaustivo quale parte integrante del quadro per la gestione dei rischi informatici di cui all'articolo 6.

2. Il programma di test di resilienza operativa digitale comprende una serie di valutazioni, test, metodologie, pratiche e strumenti da applicare conformemente agli articoli 25 e 26.

3. Nello svolgimento del programma di test di resilienza operativa digitale di cui al paragrafo 1 del presente articolo, le entita' finanziarie, diverse dalle microimprese, adottano un approccio basato sul rischio che prende in considerazione i criteri di cui all'articolo 4, paragrafo 2, tenendo debitamente conto del mutevole contesto dei rischi informatici, di eventuali rischi specifici cui l'entita' finanziaria interessata e' o potrebbe essere esposta, della criticita' dei patrimoni informativi e dei servizi forniti, nonche' di qualsiasi altro fattore giudicato rilevante dall'entita' finanziaria stessa.

4. Le entita' finanziarie, diverse dalle microimprese, assicurano che i test siano svolti da soggetti indipendenti, interni o esterni. Se i test sono svolti da un soggetto incaricato dello svolgimento dei test interno, le entita' finanziarie dedicano risorse sufficienti e garantiscono che siano evitati conflitti d'interessi durante le fasi di progettazione ed esecuzione del test.

5. Le entita' finanziarie, diverse dalle microimprese, definiscono procedure e politiche per dare un ordine di priorita' ai problemi riscontrati durante lo svolgimento dei test, per classificarli e porvi rimedio; stabiliscono inoltre metodologie di convalida interne per accertare che tutti i punti deboli, le carenze o le lacune che sono stati individuati siano pienamente affrontati.

6. Le entita' finanziarie, diverse dalle microimprese, provvedono affinche', con cadenza almeno annuale, siano eseguiti test adeguati su tutti i sistemi e le applicazioni di TIC a supporto di funzioni essenziali o importanti.

### Articolo 25 - Test di strumenti e sistemi di TIC

1. Il programma di test di resilienza operativa digitale di cui all'articolo 24 prevede, conformemente ai criteri di cui all'articolo 4, paragrafo 2, l'esecuzione di test adeguati, tra cui valutazione e scansione delle vulnerabilita', analisi open source, valutazioni della sicurezza delle reti, analisi delle carenze, esami della sicurezza fisica, questionari e soluzioni di scansione del software, esami del codice sorgente (ove fattibile), test basati su scenari, test di compatibilita', test di prestazione, test end-to-end e test di penetrazione.

2. I depositari centrali di titoli e le controparti centrali effettuano valutazioni della vulnerabilita' prima di ciascun rilascio o nuovo rilascio di nuovi o gia' esistenti applicazioni e componenti infrastrutturali, e servizi TIC a supporto delle funzioni essenziali o importanti dell'entita' finanziaria.

3. Le microimprese eseguono i test di cui al paragrafo 1 combinando un approccio basato sul rischio con una pianificazione strategica dei test relativi alle TIC, tenendo debitamente conto della necessita' di mantenere un approccio equilibrato tra l'entita' delle risorse e il tempo da assegnare ai test relativi alle TIC di cui al presente articolo, da un lato, e l'urgenza, il tipo di rischio, la criticita' dei patrimoni informativi e dei servizi forniti nonche' qualsiasi altro fattore rilevante, compresa la capacita' dell'entita' finanziaria di assumere rischi calcolati, dall'altro.

### Articolo 26 - Test avanzati di strumenti, sistemi e processi di TIC basati su test di penetrazione guidati dalla minaccia (TLPT)

1. Le entita' finanziarie, diverse dalle entita' di cui all'articolo 16, paragrafo 1, primo comma, e dalle microimprese, che sono identificate conformemente al paragrafo 8, terzo comma, del presente articolo, effettuano test avanzati sotto forma di test di penetrazione basati su minacce con cadenza almeno triennale. Sulla base del profilo di rischio dell'entita' finanziaria e tenuto conto delle circostanze operative, l'autorita' competente puo', se necessario, chiedere all'entita' finanziaria di ridurre o aumentare tale frequenza.

2. Ciascun test di penetrazione guidato dalla minaccia riguarda alcune o tutte le funzioni essenziali o importanti dell'entita' finanziaria ed e' effettuato sui sistemi attivi di produzione a supporto di tali funzioni.

   Le entita' finanziarie identificano tutti i sistemi, i processi e le tecnologie TIC sottostanti a supporto delle funzioni essenziali o importanti e tutti i pertinenti servizi TIC, compresi quelli a supporto di funzioni essenziali o importanti che sono stati esternalizzate o appaltate a fornitori terzi di servizi TIC.

   Le entita' finanziarie valutano quali funzioni essenziali o importanti debbano essere interessate dai TLPT. Il risultato della valutazione determina il preciso ambito di applicazione dei TLPT ed e' convalidato dalle autorita' competenti.

3. Qualora i fornitori terzi di servizi TIC rientrino nell'ambito di applicazione dei TLPT, l'entita' finanziaria adotta le misure e le salvaguardie necessarie per garantire la partecipazione di tali fornitori terzi di servizi TIC ai TLPT ed e' sempre pienamente responsabile di garantire il rispetto del presente regolamento.

4. Fatto salvo il paragrafo 2, primo e secondo comma, laddove si ritiene ragionevolmente che la partecipazione di un fornitore terzo di servizi TIC ai TLPT di cui al paragrafo 3 possa avere un impatto avverso sulla qualita' o la sicurezza dei servizi offerti dal fornitore terzo di servizi TIC a clienti che sono entita' non rientranti nell'ambito di applicazione del presente regolamento, ovvero sulla riservatezza dei dati relativi a tali servizi, l'entita' finanziaria e il fornitore terzo di servizi TIC possono concordare per iscritto che il fornitore terzo di servizi TIC stipuli direttamente accordi contrattuali con un soggetto incaricato dello svolgimento dei test esterno, allo scopo di condurre, sotto la direzione di un'entita' finanziaria designata, un TLPT congiunto che coinvolga diverse entita' finanziarie (pooled testing) a cui il fornitore terzo di servizi TIC fornisce tali servizi.

5. Le entita' finanziarie, cooperando con i fornitori terzi di servizi TIC e altre parti coinvolte, inclusi i soggetti incaricati dello svolgimento dei test ma escluse le autorita' competenti, applicano efficaci controlli di gestione del rischio per attenuare i rischi di potenziali impatti sui dati, danni alle attivita' e perturbazioni delle funzioni essenziali o importanti, delle operazioni o dei servizi delle entita' finanziarie, delle loro controparti o del settore finanziario.

6. Alla fine dei test, dopo che le relazioni e i piani correttivi siano stati concordati, l'entita' finanziaria e, ove applicabile, i soggetti incaricato dello svolgimento dei test esterni trasmettono all'autorita', designata conformemente al paragrafo 9 o 10, una sintesi delle pertinenti risultanze, i piani correttivi e la documentazione attestante che i TLPT sono stati svolti conformemente ai requisiti.

7. Le suddette autorita' forniscono alle entita' finanziarie un attestato che conferma che i test sono stati svolti conformemente ai requisiti, come si evince dalla documentazione, in modo da consentire il riconoscimento reciproco dei TLPT tra le autorita' competenti. L'entita' finanziaria notifica all'autorita' competente interessata l'attestato, la sintesi delle pertinenti risultanze e i piani correttivi.

8. Per l'effettuazione dei TLPT, le entita' finanziarie si avvalgono di soggetti incaricati dello svolgimento dei test in conformita' dell'articolo 27. Quando ricorrono a soggetti incaricati dello svolgimento dei test interni per l'effettuazione di TLPT, le entita' finanziarie si avvalgono di un soggetto incaricato dello svolgimento dei test esterno ogni tre test. Gli enti creditizi classificati come significativi a norma dell'articolo 6, paragrafo 4, del regolamento (UE) n. 1024/2013, ricorrono esclusivamente a soggetto incaricato dello svolgimento dei test esterni conformemente all'articolo 27, paragrafo 1, lettere da a) ad e). Le autorita' competenti identificano le entita' finanziarie che hanno l'obbligo di svolgere TLPT tenendo conto dei criteri di cui all'articolo 4, paragrafo 2, sulla base della valutazione: a) dei fattori correlati all'impatto, in particolare la portata dell'impatto sul settore finanziario dei servizi forniti e delle attivita' svolte dall'entita' finanziaria; b) dei possibili problemi di stabilita' finanziaria, tra cui il carattere sistemico dell'entita' finanziaria a livello di Unione o nazionale; c) dello specifico profilo dei rischi informatici, livello di maturita' delle TIC dell'entita' finanziaria o caratteristiche tecnologiche.

9. Gli Stati membri possono designare un'autorita' pubblica unica nel settore finanziario responsabile delle questioni relative ai TLPT nel settore finanziario a livello nazionale.

10. In assenza di una designazione a norma del paragrafo 9 e fatto salvo il potere di identificare le entita' finanziarie tenute a svolgere TLPT, un'autorita' competente puo' delegare l'esercizio di alcuni o di tutti i compiti di cui al presente articolo e all'articolo 27 a un'altra autorita' nazionale nel settore finanziario.

11. Di concerto con la BCE, le AEV elaborano progetti di norme tecniche di regolamentazione comuni conformemente al quadro di riferimento TIBER-EU al fine di specificare ulteriormente: i criteri di applicazione del paragrafo 8 secondo comma; i requisiti e le norme che disciplinano il ricorso a soggetto incaricato dello svolgimento dei test interni; i requisiti concernenti l'ambito dei TLPT di cui al paragrafo 2, l'approccio e la metodologia da seguire per i test in ciascuna fase, i risultati, la chiusura e le fasi correttive; il tipo di cooperazione di vigilanza necessario per svolgere i TLPT e facilitare il riconoscimento reciproco di tali test. Le AEV presentano tali progetti alla Commissione entro il [18 mesi dalla data di entrata in vigore del presente regolamento].

### Articolo 27 - Requisiti per i soggetti incaricati dello svolgimento dei TLPT

1. Per lo svolgimento dei test di penetrazione basati su minacce, le entita' finanziarie ricorrono unicamente a soggetti incaricati dello svolgimento dei test che:

   a) possano vantare il piu' alto grado di idoneita' e reputazione;
   b) possiedano capacita' tecniche e organizzative e dimostrino esperienza specifica nel campo delle analisi delle minacce, dei test di penetrazione e dei test red team;
   c) siano certificati da un ente di accreditamento in uno Stato membro o rispettino codici formali di condotta o quadri etici;
   d) forniscano una garanzia indipendente o una relazione di audit concernente la solida gestione dei rischi derivanti dallo svolgimento di TLPT, comprese la dovuta protezione delle informazioni riservate dell'entita' finanziaria e il risarcimento dei rischi commerciali dell'entita' finanziaria;
   e) siano debitamente e pienamente coperti da un'assicurazione di responsabilita' professionale, anche contro i rischi di colpa e negligenza.

2. Quando ricorrono a soggetto incaricato dello svolgimento dei test interni, le entita' finanziare devono provvedere affinche', oltre all'obbligo di cui al paragrafo 1, siano soddisfatte le condizioni seguenti:

   a) tale ricorso e' stato approvato dall'autorita' competente interessata o dall'autorita' pubblica unica designata conformemente all'articolo 26, paragrafi 9 e 10;
   b) l'autorita' competente interessata ha verificato che l'entita' finanziaria dispone di risorse dedicate sufficienti e che essa ha garantito che siano evitati conflitti d'interessi durante le fasi di progettazione ed esecuzione del test;
   c) il soggetto che fornisce analisi delle minacce e' esterno all'entita' finanziaria.

3. Le entita' finanziarie garantiscono che i contratti conclusi con i soggetti incaricati dello svolgimento dei test esterni prevedano una solida gestione dei risultati dei TLPT e che qualsiasi trattamento dei dati, comprese la generazione, la conservazione, l'aggregazione, l'elaborazione, la segnalazione, la comunicazione o la distruzione, non comporti rischi per l'entita' finanziaria.

---

## Capo V Sezione I - Principi fondamentali di una solida gestione dei rischi informatici derivanti da terzi (Pillar 4)

### Articolo 28 - Principi generali

1. Le entita' finanziarie gestiscono i rischi informatici derivanti da terzi quali componenti integranti dei rischi informatici nel contesto del proprio quadro per la gestione di detti rischi di cui all'articolo 6, paragrafo 1, e conformemente ai principi indicati di seguito:

   a) le entita' finanziarie che hanno stipulato accordi contrattuali per l'utilizzo di servizi TIC per lo svolgimento delle proprie operazioni commerciali rimangono sempre pienamente responsabili del rispetto e dell'adempimento di tutti gli obblighi previsti dal presente regolamento e dalla normativa applicabile in materia di servizi finanziari;
   b) la gestione dei rischi informatici derivanti da terzi da parte delle entita' finanziarie si svolge nel rispetto del principio di proporzionalita', tenendo conto:

      i) della natura, della portata, della complessita' e dell'importanza delle dipendenze connesse alle TIC;
      ii) dei rischi derivanti dagli accordi contrattuali per l'utilizzo di servizi TIC conclusi con fornitori terzi di servizi TIC, tenendo conto della criticita' o dell'importanza dei rispettivi servizi, processi o funzioni e del potenziale impatto sulla continuita' e la disponibilita' delle attivita' e dei servizi finanziari a livello individuale e di gruppo.

2. Nel contesto del quadro per la gestione dei rischi informatici TIC, le entita' finanziarie diverse dalle entita' di cui all'articolo 16, paragrafo 1, primo comma, e dalle microimprese adottano e riesaminano periodicamente una strategia per i rischi informatici derivanti da terzi, tenendo conto della strategia basata su una varieta' di fornitori di cui all'articolo 6, paragrafo 9, ove applicabile. Tale strategia comprende una politica per l'utilizzo dei servizi TIC a supporto di funzioni essenziali o importanti prestati da fornitori terzi e si applica su base individuale e, se del caso, su base subconsolidata e consolidata. Sulla base di una valutazione del profilo di rischio complessivo dell'entita' finanziaria e della portata e della complessita' dei servizi operativi, l'organo di gestione riesamina periodicamente i rischi individuati in relazione agli accordi contrattuali per l'utilizzo di servizi TIC a supporto di funzioni essenziali o importanti.

3. Nel contesto del quadro per la gestione dei rischi informatici, le entita' finanziarie mantengono e aggiornano a livello di entita', e su base subconsolidata e consolidata, un registro di informazioni su tutti gli accordi contrattuali per l'utilizzo di servizi TIC prestati da fornitori terzi.

   Gli accordi contrattuali di cui al primo comma sono opportunamente documentati, distinguendo quelli che si riferiscono a servizi TIC a supporto di funzioni essenziali o importanti dagli altri.

   Le entita' finanziarie comunicano almeno una volta all'anno alle autorita' competenti il numero di nuovi accordi per l'utilizzo di servizi TIC, le categorie di fornitori terzi di servizi TIC, il tipo di accordi contrattuali e le funzioni e i servizi TIC forniti.

   Su richiesta, le entita' finanziarie mettono a disposizione dell'autorita' competente il registro delle informazioni completo o, a seconda della richiesta, determinate sezioni del registro insieme alle informazioni giudicate necessarie per consentire l'efficace vigilanza sull'entita' finanziaria.

   Le entita' finanziarie informano tempestivamente l'autorita' competente in merito a eventuali accordi contrattuali previsti per l'utilizzo di servizi TIC a supporto di funzioni essenziali o importanti, nonche' del momento in cui una funzione diventa essenziale o importante.

4. Prima di stipulare un accordo contrattuale per l'utilizzo di servizi TIC, le entita' finanziarie:

   a) valutano se l'accordo contrattuale riguardi l'utilizzo di servizi TIC a supporto di una funzione essenziale o importante;
   b) verificano se siano soddisfatte le condizioni di vigilanza per la conclusione del contratto;
   c) identificano e valutano tutti i rischi pertinenti relativi all'accordo contrattuale, compresa la possibilita' che tale accordo contrattuale possa aggravare il rischio di concentrazione delle TIC di cui all'articolo 29;
   d) effettuano controlli di dovuta diligenza (due diligence) sui potenziali fornitori terzi di servizi TIC e ne garantiscono l'idoneita' lungo tutto il processo di selezione e valutazione;
   e) individuano e valutano i conflitti d'interessi che possano derivare dall'accordo contrattuale.

5. Le entita' finanziarie possono stipulare accordi contrattuali soltanto con fornitori terzi di servizi TIC che soddisfano standard appropriati in materia di sicurezza delle informazioni. Laddove tali accordi contrattuali riguardino funzioni essenziali o importanti, le entita' finanziarie, prima di concludere detti accordi, prendono in debita considerazione l'utilizzo da parte dei fornitori terzi di servizi TIC degli standard di qualita' piu' aggiornati ed elevati in materia di sicurezza delle informazioni.

6. Nell'esercizio dei diritti di accesso, ispezione e audit nei confronti del fornitore terzo di servizi TIC, le entita' finanziarie predeterminano, sulla base di un approccio basato sul rischio, la frequenza delle verifiche di audit e delle ispezioni nonche' i settori da sottoporre ad audit, aderendo a standard di audit comunemente accettate in conformita' di eventuali indicazioni di vigilanza sull'uso e l'integrazione di tali standard di audit.

   Laddove gli accordi contrattuali conclusi con fornitori terzi di servizi TIC per l'utilizzo di servizi TIC comportino un'elevata complessita' tecnica, l'entita' finanziaria verifica che i revisori, indipendentemente dal fatto che siano revisori interni o esterni o siano un gruppo di revisori, possiedano competenze e conoscenze adeguate per svolgere efficacemente gli audit e le valutazioni del caso.

7. Le entita' finanziarie stabiliscono clausole che consentano la risoluzione degli accordi contrattuali per l'utilizzo di servizi TIC in una qualsiasi delle circostanze seguenti:

   a) rilevante violazione, da parte del fornitore terzo di servizi TIC, di leggi, regolamenti o condizioni contrattuali applicabili;
   b) circostanze, identificate nel corso del monitoraggio dei rischi informatici derivanti da terzi, ritenute suscettibili di alterare l'esercizio delle funzioni previsto a norma dell'accordo contrattuale, tra cui modifiche di rilievo che incidano sull'accordo o sulla situazione del fornitore terzo di servizi TIC;
   c) punti deboli del fornitore terzo di servizi TIC emersi riguardo alla sua gestione complessiva dei rischi informatici e, in particolare, nel modo in cui il fornitore garantisce la disponibilita', autenticita', integrita' e riservatezza dei dati, siano essi dati personali o altrimenti sensibili, oppure dei dati non personali;
   d) laddove l'autorita' competente non sia piu' in grado di vigilare efficacemente sull'entita' finanziaria per via delle condizioni dell'accordo contrattuale in questione o delle circostanze ivi afferenti.

8. Per i servizi TIC a supporto di funzioni essenziali o importanti, le entita' finanziarie predispongono strategie di uscita. Tali strategie tengono conto dei rischi che possono emergere a livello dei fornitori terzi di servizi TIC, in particolare possibili disfunzioni dei fornitori stessi, il deterioramento della qualita' dei servizi TIC forniti, una perturbazione dell'attivita' commerciale conseguente a una fornitura di servizi TIC inadeguata o carente, oppure gravi rischi connessi all'adeguatezza e alla continuita' dell'esercizio del rispettivo servizio TIC oppure la risoluzione di accordi contrattuali con fornitori terzi di servizi TIC in una delle circostanze di cui al paragrafo 7.

   Le entita' finanziarie garantiscono di poter porre termine agli accordi contrattuali senza:

   a) perturbare le proprie attivita' commerciali;
   b) limitare il rispetto dei requisiti normativi;
   c) pregiudicare la continuita' e la qualita' dei servizi forniti ai clienti.

   I piani di uscita sono esaustivi, documentati e, conformemente ai criteri di cui all'articolo 4, paragrafo 2, sottoposti a test adeguati e riesaminati periodicamente.

   Le entita' finanziarie identificano soluzioni alternative ed elaborano piani di transizione che consentano loro di trasferire i servizi TIC previsti dal contratto e i relativi dati dal fornitore terzo di servizi TIC, in maniera sicura e nella loro interezza, a fornitori alternativi oppure reintegrarli al proprio interno.

   Le entita' finanziarie dispongono di misure di emergenza idonee per mantenere la continuita' operativa qualora si verifichino le circostanze di cui al primo comma.

9. Le AEV, tramite il comitato congiunto, elaborano progetti di norme tecniche di attuazione per definire modelli standard in relazione al registro delle informazioni di cui al paragrafo 3, comprese le informazioni comuni a tutti gli accordi contrattuali per l'utilizzo di servizi TIC. Le AEV presentano tali progetti di norme tecniche di attuazione alla Commissione entro il [12 mesi dalla data di entrata in vigore del presente regolamento].

10. Le AEV, tramite il comitato congiunto, elaborano progetti di norme tecniche di regolamentazione per precisare ulteriormente il contenuto dettagliato della politica di cui al paragrafo 2, in relazione agli accordi contrattuali per l'utilizzo di servizi TIC a supporto di funzioni essenziali o importanti prestati da fornitori terzi di servizi TIC. Le AEV presentano detti progetti di norme tecniche di regolamentazione alla Commissione il [12 mesi dalla data di entrata in vigore del presente regolamento].

### Articolo 29 - Valutazione preliminare del rischio di concentrazione delle TIC a livello di entita'

1. All'atto dell'identificazione e della valutazione dei rischi di cui all'articolo 28, paragrafo 4, lettera c), le entita' finanziarie tengono conto altresi' dell'eventualita' che la prevista conclusione di un accordo contrattuale relativo a servizi TIC a supporto di funzioni essenziali o importanti possa avere una delle seguenti conseguenze:

   a) la conclusione di un contratto con un fornitore terzo di servizi TIC non facilmente sostituibile; o
   b) la presenza di molteplici accordi contrattuali relativi alla prestazione di servizi TIC a supporto di funzioni essenziali o importanti con lo stesso fornitore terzo oppure con fornitori terzi strettamente connessi.

   Le entita' finanziarie vagliano i benefici e i costi di soluzioni alternative, quali il ricorso a diversi fornitori terzi di servizi TIC, verificando se e come le soluzioni previste soddisfino le esigenze commerciali e consentano di conseguire gli obiettivi fissati nella propria strategia di resilienza digitale.

2. Qualora gli accordi contrattuali per l'utilizzo di servizi TIC a supporto di funzioni essenziali o importanti prevedano la possibilita' che un fornitore terzo di servizi TIC subappalti a sua volta servizi TIC a supporto di una funzione essenziale o importante ad altri fornitori terzi di servizi TIC, le entita' finanziarie vagliano i benefici e i rischi che possono derivare da tale subappalto, in particolare nel caso di un subappaltatore di TIC stabilito in un paese terzo.

   Qualora gli accordi contrattuali riguardino servizi TIC a supporto delle funzioni essenziali o importanti, le entita' finanziarie tengono in debita considerazione le disposizioni del diritto fallimentare applicabili in caso di fallimento del fornitore terzo di servizi TIC come pure eventuali restrizioni relative all'urgente ripristino dei dati dell'entita' finanziaria.

   Qualora gli accordi contrattuali per l'utilizzo di servizi TIC a supporto di funzioni essenziali o importanti siano conclusi con un fornitore terzo di servizi TIC stabilito in un paese terzo, le entita' finanziarie, in aggiunta alle considerazioni di cui al secondo comma, tengono conto altresi' del rispetto delle norme dell'UE sulla protezione dei dati e dell'effettiva applicazione della legge in tale paese terzo.

   Qualora gli accordi contrattuali per l'utilizzo di servizi TIC a supporto di funzioni essenziali o importanti prevedano un subappalto, le entita' finanziarie valutano se e come catene di subappalti potenzialmente lunghe e complesse possano incidere sulla loro capacita' di monitorare pienamente le funzioni appaltate e sulla capacita' dell'autorita' competente di vigilare efficacemente, a tal proposito, sull'entita' finanziaria.

### Articolo 30 - Principali disposizioni contrattuali

1. I diritti e gli obblighi dell'entita' finanziaria e del fornitore terzo di servizi TIC sono attribuiti chiaramente e definiti per iscritto. Il testo integrale del contratto comprende gli accordi sul livello dei servizi ed e' contenuto in un documento scritto disponibile alle parti in formato cartaceo oppure in un documento in altro formato scaricabile, durevole e accessibile.

2. Gli accordi contrattuali per l'utilizzo di servizi TIC comprendono almeno gli elementi seguenti:

   a) la descrizione chiara e completa di tutte le funzioni che il fornitore terzo di servizi TIC deve svolgere e tutti i servizi TIC che deve prestare, comprese l'indicazione dell'eventuale autorizzazione a subappaltare un servizio TIC a sostegno di una funzione essenziale o importante o parti significative di essa e, in caso affermativo, le condizioni di tale subappalto;
   b) le localita', segnatamente le regioni o i paesi, in cui si devono svolgere le funzioni e prestare i servizi TIC appaltati o subappaltati e in cui si devono trattare i dati, compreso il luogo di conservazione, nonche' l'obbligo, per il fornitore terzo di servizi TIC, di segnalare in anticipo all'entita' finanziaria l'intenzione di cambiare tale o tali localita';
   c) le disposizioni in materia di disponibilita', autenticita', integrita' e riservatezza in relazione alla protezione dei dati, compresi i dati personali;
   d) le disposizioni relative alle garanzie di accesso, ripristino e restituzione, in un formato facilmente accessibile, di dati personali e non personali trattati dall'entita' finanziaria in caso di insolvenza, risoluzione o interruzione delle operazioni commerciali del fornitore terzo di servizi TIC o in caso di risoluzione degli accordi commerciali;
   e) le descrizioni dei livelli di servizio, compresi relativi aggiornamenti e revisioni;
   f) l'obbligo per il fornitore terzo di servizi TIC di prestare assistenza all'entita' finanziaria senza costi aggiuntivi o a un costo stabilito ex ante, qualora si verifichi un incidente connesso alle TIC relativo al servizio TIC fornito all'entita' finanziaria;
   g) l'obbligo per il fornitore terzo di servizi di TIC di operare senza riserve con le autorita' competenti e con le autorita' di risoluzione dell'entita' finanziaria, comprese le persone da queste nominate;
   h) i diritti di risoluzione e il relativo termine minimo di preavviso per la risoluzione degli accordi contrattuali, conformemente alle attese delle autorita' competenti e delle autorita' di risoluzione;
   i) le condizioni riguardanti la partecipazione dei fornitori terzi di servizi TIC ai programmi di sensibilizzazione sulla sicurezza delle TIC e alle attivita' di formazione sulla resilienza operativa digitale delle entita' finanziarie conformemente all'articolo 13, paragrafo 6.

3. Gli accordi contrattuali per l'utilizzo di servizi TIC a supporto di funzioni essenziali o importanti comprendono, in aggiunta agli elementi di cui al paragrafo 2, almeno quanto segue:

   a) la descrizione completa dei livelli di servizio, comprendente i relativi aggiornamenti e revisioni con precisi obiettivi quantitativi e qualitativi, in termini di prestazioni, nell'ambito dei livelli di servizio concordati, in modo da consentire un monitoraggio efficace da parte dell'entita' finanziaria dei servizi TIC e l'applicazione, senza indebito ritardo, di opportune azioni correttive qualora i livelli di servizio concordati non siano rispettati;
   b) termini di preavviso e obblighi di segnalazione per il fornitore terzo di servizi TIC nei confronti dell'entita' finanziaria, tra cui la notifica di eventuali sviluppi che potrebbero esercitare un impatto significativo sulla capacita' del fornitore terzo di servizi TIC di prestare servizi a supporto di funzioni essenziali o importanti efficacemente, in linea con i livelli di servizio concordati;
   c) l'obbligo per il fornitore terzo di servizi TIC di attuare e testare i piani operativi d'emergenza e di predisporre misure, strumenti e politiche per la sicurezza delle TIC che offrano un adeguato livello di sicurezza per la fornitura dei servizi da parte dell'entita' finanziaria, in linea con il proprio quadro normativo;
   d) l'obbligo per il fornitore terzo di servizi TIC di partecipare e cooperare pienamente al TLPT dell'entita' finanziaria di cui agli articoli 26 e 27;
   e) il diritto di monitorare costantemente le prestazioni del fornitore terzo di servizi TIC, che comporta quanto segue:

      i) diritti incondizionati di accesso, ispezione e audit da parte dell'entita' finanziaria - o di un terzo designato a tal fine - e dell'autorita' competente nonche' il diritto di ottenere copia della documentazione pertinente in loco, se di importanza critica per le operazioni del fornitore terzo di servizi TIC, il cui effettivo esercizio non sia impedito o limitato da altri accordi contrattuali o politiche di attuazione;
      ii) il diritto di concordare livelli di garanzia alternativi, qualora siano interessati i diritti di altri clienti;
      iii) l'obbligo per il fornitore terzo di servizi TIC di cooperare senza riserve nel corso delle ispezioni e degli audit in loco svolti dalle autorita' competenti, dall'autorita' di sorveglianza capofila, dall'entita' finanziaria o da un terzo designato; e
      iv) l'obbligo di fornire dettagli sull'ambito di applicazione, sulle procedure da seguire e sulla frequenza di tali ispezioni e audit;

   f) le strategie di uscita, in particolare la definizione di un adeguato periodo di transizione obbligatorio:

      i) durante il quale il fornitore terzo di servizi TIC continuera' a prestare i suoi servizi TIC o a esercitare le sue funzioni allo scopo di ridurre il rischio di perturbazioni presso l'entita' finanziaria o di garantire la sua efficace risoluzione e ristrutturazione;
      ii) che permetta all'entita' finanziaria di migrare verso un altro fornitore terzo di servizi TIC oppure di adottare soluzioni interne coerenti con la complessita' del servizio prestato.

   In deroga alla lettera e), il fornitore terzo di servizi TIC e l'entita' finanziaria che e' una microimpresa possono convenire che i diritti di accesso, ispezione e audit dell'entita' finanziaria possano essere delegati a un terzo indipendente, nominato dal fornitore terzo di servizi TIC, e che l'entita' finanziaria possa richiedere in qualsiasi momento al terzo informazioni e garanzie sulle prestazioni del fornitore terzo di servizi TIC.

4. All'atto della negoziazione degli accordi contrattuali, le entita' finanziarie e i fornitori terzi di servizi TIC prendono in considerazione il ricorso a clausole contrattuali standard elaborate dalle autorita' pubbliche per servizi specifici.

5. Le AEV, tramite il comitato congiunto, elaborano progetti di norme tecniche di regolamentazione per specificare ulteriormente gli elementi di cui al paragrafo 2, lettera a), che l'entita' finanziaria deve determinare e valutare quando subappalta servizi TIC a supporto di funzioni essenziali o importanti. Le AEV presentano tali progetti di norme tecniche di regolamentazione alla Commissione entro il [18 mesi dalla data di entrata in vigore del presente regolamento].

---

## Capo VI - Meccanismi di condivisione delle informazioni (Pillar 5)

### Articolo 45 - Meccanismi di condivisione delle informazioni e delle analisi delle minacce informatiche

1. Le entita' finanziarie possono scambiarsi reciprocamente informazioni e analisi delle minacce informatiche, tra cui indicatori di compromissione, tattiche, tecniche e procedure, segnali di allarme per la cibersicurezza e strumenti di configurazione, nella misura in cui tale condivisione di informazioni e dati:

   a) mira a potenziare la resilienza operativa digitale delle entita' finanziarie, in particolare aumentando la consapevolezza in merito alle minacce informatiche, contenendo o inibendo la capacita' di diffusione delle minacce informatiche, sostenendo le capacita' di difesa, le tecniche di individuazione delle minacce, le politiche di mitigazione o le fasi di risposta e ripristino;
   b) si svolge entro comunita' fidate di entita' finanziarie;
   c) si realizza mediante meccanismi di condivisione delle informazioni che tutelano la natura potenzialmente sensibile delle informazioni condivise e sono disciplinati da norme di condotta pienamente rispettose della riservatezza dell'attivita' economica, della protezione dei dati personali ai sensi del regolamento (UE) 2016/679 e delle linee guida sulla politica in materia di concorrenza.

2. Ai fini del paragrafo 1, lettera c), i meccanismi di condivisione delle informazioni definiscono le condizioni per la partecipazione e, se del caso, definiscono i dettagli concernenti il coinvolgimento delle autorita' pubbliche e la veste in cui queste possono partecipare ai meccanismi di condivisione delle informazioni, il coinvolgimento dei fornitori terzi di servizi TIC, nonche' gli elementi operativi tra cui l'utilizzo di piattaforme informatiche apposite.

3. Le entita' finanziarie notificano alle autorita' competenti la propria partecipazione ai meccanismi di condivisione delle informazioni di cui al paragrafo 1, al momento della convalida della propria adesione o, se del caso, della cessazione dell'adesione, quando quest'ultima abbia effetto.

---

## Capo VIII - Disposizioni transitorie e finali (estratto)

### Articolo 64 - Entrata in vigore e applicazione

Il presente regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione europea.

Esso si applica a decorrere dal [24 mesi dalla data di entrata in vigore del presente regolamento].

Il presente regolamento e' obbligatorio in tutti i suoi elementi e direttamente applicabile in ciascuno degli Stati membri.

(Riferimento: il regolamento e' stato pubblicato in GU UE L 333 del 27/12/2022; entrato in vigore il 16/01/2023; si applica dal 17/01/2025.)
