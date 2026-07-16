# Fonte verbatim - Circolare AgID 18 aprile 2017, n. 2/2017 (Misure minime di sicurezza ICT per le PA - ABSC)

> Misure minime di sicurezza ICT per le pubbliche amministrazioni (MMS-PA), basate
> sugli AgID Basic Security Control(s) (ABSC), con tre livelli di attuazione
> (Minimo, Standard, Alto). Trascrizione VERBATIM dal testo pubblicato in Gazzetta
> Ufficiale.
>
> **Atto**: Circolare AgID 18 aprile 2017, n. 2/2017 (codice redazionale 17A03060),
> GU Serie Generale n. 103 del 5-05-2017, in attuazione dell'art. 14-bis del C.A.D.
> (D.Lgs. 82/2005) e della direttiva PCM 1 agosto 2015.
> **Fonte**: Gazzetta Ufficiale - PDF ufficiale della G.U. n. 103/2017.
> SHA256 PDF: 24e4956ef483426bb9ebbdc425d941c150830436bdc4ba7fa71e558dc7986725
> URL: https://www.gazzettaufficiale.it/eli/gu/2017/05/05/103/sg/pdf
> Il testo della circolare (artt.) e' letto anche via caricaArticolo; le tabelle degli
> ABSC (Allegato 1) e il modulo di implementazione (Allegato 2) sono in formato
> grafico nel PDF (pagg. ~67-73). Accesso: 2026-07-16.
>
> NOTA: nelle tabelle dell'Allegato 1 ogni controllo (ABSC_ID gerarchico x.y.z) e'
> marcato con le colonne booleane "Minimo", "Standard", "Alto". La resa testuale della
> tabella dal PDF non conserva in modo affidabile l'allineamento delle colonne X:
> per il livello ESATTO di ciascun controllo consultare le colonne nel PDF citato.

---

## Circolare - testo (artt.)

### Premessa

```
Premessa.
  L'art. 14-bis del decreto legislativo  7  marzo  2005,  n.  82,  di
seguito C.A.D., al comma 2, lettera a), tra  le  funzioni  attribuite
all'AgID, prevede, tra l'altro, l'emanazione di  regole,  standard  e
guide tecniche, nonche' di vigilanza e controllo sul  rispetto  delle
norme di cui al medesimo C.A.D., anche attraverso l'adozione di  atti
amministrativi generali, in materia di sicurezza informatica.
  La direttiva del 1° agosto 2015 del Presidente  del  Consiglio  dei
ministri impone  l'adozione  di  standard  minimi  di  prevenzione  e
reazione ad eventi cibernetici. Al fine di agevolare  tale  processo,
individua nell'Agenzia per l'Italia digitale l'organismo  che  dovra'
rendere prontamente disponibili  gli  indicatori  degli  standard  di
riferimento, in linea con quelli posseduti dai maggiori  partner  del
nostro Paese e dalle organizzazioni internazionali di cui l'Italia e'
parte.
  La presente circolare sostituisce la circolare AgID n.  1/2017  del
17 marzo 2017 (pubblicata nella Gazzetta Ufficiale n. 79 del 4 aprile
2017).
                               Art. 1
                                Scopo
  Obiettivo della  presente  circolare  e'  indicare  alle  pubbliche
amministrazioni le misure minime per la  sicurezza  ICT  che  debbono
essere adottate al fine di  contrastare  le  minacce  piu'  comuni  e
frequenti cui sono soggetti i loro sistemi informativi.
  Le  misure  minime  di  cui  al  comma  precedente  sono  contenute
nell'allegato 1, che  costituisce  parte  integrante  della  presente
circolare.
```

### Art. 2

```
Art. 2
                    Amministrazioni destinatarie
  Destinatari  della  presente  circolare  sono  i  soggetti  di  cui
all'art. 2, comma 2 del C.A.D.
```

### Art. 3

```
Art. 3
                   Attuazione delle misure minime
  Il responsabile della struttura per l'organizzazione, l'innovazione
e le tecnologie di cui all'art.17 del C.A.D., ovvero, in sua assenza,
il dirigente  allo  scopo  designato,  ha  la  responsabilita'  della
attuazione delle misure minime di cui all'art. 1.
```

### Art. 4

```
Art. 4
               Modulo di implementazione delle MMS-PA
  Le  modalita'  con  cui  ciascuna  misura  e'  implementata  presso
l'amministrazione debbono essere sinteticamente riportate nel  modulo
di implementazione di cui all'allegato 2, anch'esso parte  integrante
della presente circolare.
  Il modulo di implementazione dovra' essere firmato digitalmente con
marcatura temporale dal soggetto di cui all'art. 3 e dal responsabile
legale della struttura.  Dopo  la  sottoscrizione  esso  deve  essere
conservato e, in caso di incidente informatico, trasmesso al  CERT-PA
insieme con la segnalazione dell'incidente stesso.
```

### Art. 5

```
Art. 5
                         Tempi di attuazione
  Entro il 31 dicembre 2017 le amministrazioni dovranno  attuare  gli
adempimenti di cui agli articoli precedenti.
    Roma, 18 aprile 2017
                                            Il Presidente: Samaritani
```

## Allegato 1 - Generalita' e scopo (verbatim, pag. ~66)

```
1. GENERALITÀ.
       1.1. SCOPO.
       Il presente documento contiene le misure minime di sicurezza ICT per le pubbliche amministrazioni le quali costituiscono parte integrante
delle linee guida per la sicurezza ICT delle pubbliche amministrazioni.
       Questo documento è emesso in attuazione della direttiva del Presidente del Consiglio dei ministri 1° agosto 2015 e costituisce un’anticipazione
urgente della regolamentazione completa in corso di emanazione, al fine di fornire alle pubbliche amministrazioni dei criteri di riferimento per stabilire
se il livello di protezione offerto da un’infrastruttura risponda alle esigenze operative, individuando anche gli interventi idonei per il suo adeguamento.
   1.2      STORIA DELLE MODIFICHE

          Ver.                      Descrizione delle modifiche                                               Data emissione
          1.0                             Prima versione                                                       26/04/2016


   1.3      RIFERIMENTI
```

## Allegato 1 - Struttura degli ABSC e livelli di attuazione (verbatim, pag. ~67)

```
livello ci fosse una granularità ancora eccessiva, soprattutto sotto il profilo implementativo, che avrebbe costretto soprattutto le piccole amministra-
zioni ad introdurre misure esagerate per la propria organizzazione. Per tale ragione è stato introdotto un ulteriore terzo livello, nel quale la misura
di secondo livello viene decomposta in misure elementari, ancora una volta implementabili in modo indipendente. Pertanto un ABSC è identificato
da un identificatore gerarchico a tre livelli x, y, z, dove x e y sono i numeri che identificano il CSC concettualmente corrispondente e z individua
ciascuno dei controlli di livello 3 in cui questo è stato raffinato.
      Al primo livello, che corrisponde ad una famiglia di controlli destinati al perseguimento del medesimo obiettivo, è associata una tabella che li
contiene tutti. Nella prima colonna, sviluppata gerarchicamente su tre livelli, viene definito l’identificatore univoco di ciascuno di essi. La succes-
siva colonna «Descrizione» specifica il controllo attraverso una definizione sintetica.
      Nella terza colonna, «FNSC» (Framework nazionale di sicurezza cibernetica), viene indicato l’identificatore della Subcategory del Framework
Core del Framework nazionale per la Cyber Security, proposto con il 2015 Italian Cyber Security Report del CIS «La Sapienza» presentato lo scorso
4 febbraio 2016, al quale il controllo è riconducibile. Pur non intendendo costituire una contestualizzazione del Framework, le misure minime con-
cretizzano praticamente le più importanti ed efficaci azioni che questo guida ad intraprendere. Per il diverso contesto di provenienza ed il differente
obiettivo che i due strumenti intendono perseguire, le misure minime pongono l’accento sopra gli aspetti di prevenzione piuttosto che su quelli di
risposta e ripristino.
      Le ultime tre colonne sono booleane e costituiscono una linea guida che indica quali controlli dovrebbero essere implementati per ottenere un
determinato livello di sicurezza. La prima, «Minimo», specifica il livello sotto il quale nessuna amministrazione può scendere: i controlli in essa
indicati debbono riguardarsi come obbligatori. La seconda, «Standard», può essere assunta come base di riferimento nella maggior parte dei casi,
mentre la terza, «Alto», può riguardarsi come un obiettivo a cui tendere.
      Il raggiungimento di elevati livelli di sicurezza, quando è molto elevata la complessità della struttura e l’eterogeneità dei servizi erogati, può
essere eccessivamente oneroso se applicato in modo generalizzato. Pertanto ogni amministrazione dovrà avere cura di individuare al suo interno
gli eventuali sottoinsiemi, tecnici e/o organizzativi, caratterizzati da omogeneità di requisiti ed obiettivi di sicurezza, all’interno dei quali potrà
applicare in modo omogeneo le misure adatte al raggiungimento degli obiettivi stessi.
      Le amministrazioni NSC, per l’infrastruttura che gestisce dati NSC, dovrebbero collocarsi almeno a livello “standard” in assenza di requisiti
più elevati.
```

## Allegato 1 - Le 8 famiglie di controlli ABSC (verbatim: titolo e descrizione, pagg. ~68-73)

### ABSC 1 (CSC 1): INVENTARIO DEI DISPOSITIVI AUTORIZZATI E NON AUTORIZZATI

> Gestire attivamente tutti i dispositivi hardware sulla rete (tracciandoli, inventariandoli e mantenendo aggiornato l’inventario) in modo che l’accesso sia dato solo ai dispositivi autorizzati, mentre i dispositivi non autorizzati e non gestiti siano individuati e sia loro impedito l’accesso

### ABSC 2 (CSC 2): INVENTARIO DEI SOFTWARE AUTORIZZATI E NON AUTORIZZATI

> Gestire attivamente (inventariare, tracciare e correggere) tutti i software sulla rete in modo che sia installato ed eseguito solo software autorizzato, mentre il software non autorizzato e non gestito sia individuato e ne venga impedita l’installazione o l’esecuzione

### ABSC 3 (CSC 3): PROTEGGERE LE CONFIGURAZIONI DI HARDWARE E SOFTWARE SUI DISPOSITIVI MOBILI, LAPTOP, WORKSTATION E SERVER

> Istituire, implementare e gestire attivamente (tracciare, segnalare, correggere) la configurazione di sicurezza di laptop, server e workstation utilizzando una gestione della configurazione e una procedura di controllo delle variazioni rigorose, allo scopo di evitare che gli attacchi informatici possano sfruttare le vul- nerabilità di servizi e configurazioni.

### ABSC 4 (CSC 4): VALUTAZIONE E CORREZIONE CONTINUA DELLA VULNERABILITÀ

> Acquisire, valutare e intraprendere continuamente azioni in relazione a nuove informazioni allo scopo di individuare vulnerabilità, correggere e minimizzare la finestra di opportunità per gli attacchi informatici.

### ABSC 5 (CSC 5): USO APPROPRIATO DEI PRIVILEGI DI AMMINISTRATORE

> Regole, processi e strumenti atti ad assicurare il corretto utilizzo delle utenze privilegiate e dei diritti amministrativi.

### ABSC 8 (CSC 8): DIFESE CONTRO I MALWARE

> Controllare l’installazione, la diffusione e l’esecuzione di codice maligno in diversi punti dell’azienda, ottimizzando al tempo stesso l’utilizzo dell’automazione per consentire il rapido aggiornamento delle difese, la raccolta dei dati e le azioni correttive.

### ABSC 10 (CSC 10): COPIE DI SICUREZZA

> Procedure e strumenti necessari per produrre e mantenere copie di sicurezza delle informazioni critiche, così da consentirne il ripristino in caso di neces- sità.

### ABSC 13 (CSC 13): PROTEZIONE DEI DATI

> Processi interni, strumenti e sistemi necessari per evitare l’esfiltrazione dei dati, mitigarne gli effetti e garantire la riservatezza e l’integrità delle informazioni rilevanti

