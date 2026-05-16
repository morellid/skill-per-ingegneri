# Task: Checklist della documentazione tecnica (Allegato VII)

## Obiettivo

Verificare se la **documentazione tecnica** redatta dal fabbricante per un PDE copre i requisiti dell'**art. 31** e dell'**Allegato VII** del Regolamento (UE) 2024/2847. Output: punch list dei punti coperti, dei punti mancanti, e delle integrazioni richieste prima dell'immissione sul mercato.

Pre-requisito: aver chiarito categoria del PDE e procedura di conformita' scelta (output dei task `classifica-pde.md` e `scegli-procedura-conformita.md`).

## Input richiesti

Chiedere all'utente, prima di applicare la procedura:

1. **Indice attuale** della documentazione tecnica (sezioni o capitoli presenti).
2. **Categoria del PDE** e **procedura di conformita'** scelta.
3. **Lingua** della documentazione (rilevante per l'art. 31 par. 4).
4. **Se applicato il modulo B**: la documentazione contiene la **dichiarazione di unicita' della domanda** all'organismo notificato (Allegato VIII parte II punto 3.2)?
5. **Periodo di assistenza** dichiarato dal fabbricante (art. 13 par. 8).
6. **Norme armonizzate, specifiche comuni o sistemi europei di certificazione** applicati o ai quali si fa riferimento.

## Fonti

Procedura ancorata a:
- `references/estratti/reg-ue-2024-2847-cra-classificazione.md` sezione "4. Documentazione tecnica".
- `references/fonti/reg-ue-2024-2847-cra.md` (art. 13 par. 4, art. 31, Allegato I, Allegato II, Allegato V, Allegato VII).

## Procedura

Verifica per ciascuno degli **8 punti dell'Allegato VII** che la documentazione tecnica:

### Punto 1 - Descrizione generale del PDE

- [ ] **1.a** Finalita' prevista del PDE (cfr. art. 3 punto 23).
- [ ] **1.b** Versioni del software importanti per la conformita' (es. release, build, hash di firma codice).
- [ ] **1.c** Per prodotti hardware: fotografie o illustrazioni delle caratteristiche esterne, della marcatura e della disposizione interna.
- [ ] **1.d** Informazioni e istruzioni per l'utilizzatore (Allegato II), 9 punti minimo: dati di contatto, punto di contatto unico per vulnerabilita', identificazione, finalita' prevista, circostanze d'uso che possono comportare rischi, URL DoC UE, tipo di assistenza e data finale del periodo di assistenza, istruzioni dettagliate (installazione, smantellamento sicuro, disattivazione aggiornamenti automatici, integrazione in altri PDE), eventuale SBOM accessibile.

### Punto 2 - Descrizione progettazione, sviluppo, produzione e gestione vulnerabilita'

- [ ] **2.a** Informazioni sulla progettazione e sviluppo: disegni/schemi e **descrizione dell'architettura del sistema** che spieghi come i componenti software si basano l'uno sull'altro o si alimentano reciprocamente e si integrano nel processo complessivo.
- [ ] **2.b** Informazioni sui **processi di gestione delle vulnerabilita'** (Allegato I parte II):
  - [ ] Distinta base del software (**SBOM**) in formato di uso comune leggibile da dispositivo automatico, con almeno **le dipendenze di primo livello** (Allegato I parte II punto 1);
  - [ ] **Politica di divulgazione coordinata delle vulnerabilita' (CVD)** (Allegato I parte II punto 5);
  - [ ] **Prova della fornitura di un indirizzo di contatto** per la segnalazione delle vulnerabilita' (Allegato I parte II punto 6);
  - [ ] Descrizione delle **soluzioni tecniche** per la distribuzione sicura degli aggiornamenti (Allegato I parte II punti 7-8).
- [ ] **2.c** Informazioni sui **processi di produzione e monitoraggio** del PDE e sulla loro convalida.

### Punto 3 - Valutazione dei rischi di cibersicurezza

- [ ] **3.** Valutazione dei rischi di cibersicurezza ex art. 13, par. 2 e 3, comprese le **modalita' di applicazione dei requisiti essenziali dell'Allegato I, parte I** (i 13 requisiti lett. a-m del punto 2). La valutazione e' documentata e aggiornata durante il periodo di assistenza. Se alcuni requisiti dell'Allegato I parte I non sono applicabili, la documentazione fornisce **chiara giustificazione** (art. 13 par. 4).

### Punto 4 - Determinazione del periodo di assistenza

- [ ] **4.** Informazioni rilevanti di cui si e' tenuto conto per determinare il periodo di assistenza ex art. 13 par. 8: durata di utilizzo prevista, aspettative ragionevoli degli utilizzatori, natura del prodotto e sua finalita', periodi di assistenza di prodotti analoghi del mercato. **Il periodo di assistenza e' di almeno 5 anni**; se la durata di utilizzo prevista e' inferiore, il periodo corrisponde alla durata di utilizzo prevista.

### Punto 5 - Norme armonizzate, specifiche comuni, certificazione europea

- [ ] **5.** Elenco delle **norme armonizzate applicate** integralmente o in parte (riferimenti pubblicati in GU UE), delle **specifiche comuni** ex art. 27, dei **sistemi europei di certificazione** ex Reg. (UE) 2019/881. Per ogni norma/specifica/sistema: applicazione integrale o parziale (indicare le parti applicate). Per parti non coperte da norme armonizzate: **descrizione delle soluzioni alternative** adottate per soddisfare i requisiti essenziali dell'Allegato I, parti I e II.

### Punto 6 - Relazioni delle prove

- [ ] **6.** **Relazioni delle prove** (test reports) effettuate per verificare la conformita' del PDE e dei processi di gestione delle vulnerabilita' ai requisiti essenziali applicabili dell'Allegato I, parti I e II. Possono essere prove interne, di laboratori esterni, o eseguite/fatte eseguire dall'organismo notificato (per modulo B parte II punto 4.3-4.4).

### Punto 7 - Copia della DoC UE

- [ ] **7.** **Copia della Dichiarazione di conformita' UE** redatta ai sensi dell'art. 28 e con il contenuto minimo dell'Allegato V (8 elementi). Verificare in particolare:
  - identificazione univoca PDE;
  - nome/indirizzo fabbricante (o rappresentante autorizzato);
  - attestazione di rilascio sotto responsabilita' esclusiva del fornitore;
  - oggetto della dichiarazione;
  - attestazione di conformita' alla normativa di armonizzazione dell'Unione;
  - **riferimenti alle norme armonizzate** utilizzate o ad altre specifiche/certificazioni;
  - se applicabile, **nome e numero dell'organismo notificato**, descrizione procedura e certificato rilasciato;
  - firma, luogo, data, nome, funzione.

### Punto 8 - SBOM su richiesta

- [ ] **8.** La **SBOM** e' tenuta a disposizione, a seguito di richiesta motivata di un'autorita' di vigilanza del mercato, a condizione che cio' sia necessario per verificare la conformita' ai requisiti essenziali dell'Allegato I.

### Requisiti formali aggiuntivi

- [ ] **Documentazione redatta prima dell'immissione sul mercato** (art. 31 par. 2).
- [ ] **Lingua**: una delle lingue ufficiali dello Stato membro in cui e' stabilito l'organismo notificato, o lingua accettata da quest'ultimo (art. 31 par. 4). Per il modulo A (controllo interno), la lingua e' quella del registrante presso le autorita' di vigilanza del Paese di immissione.
- [ ] **Aggiornata almeno per la durata del periodo di assistenza** (art. 31 par. 2).
- [ ] Se il PDE e' soggetto anche ad altri atti dell'Unione che prevedono documentazione tecnica: **unica documentazione tecnica** che integra tutti gli elementi (art. 31 par. 3).
- [ ] **Conservazione 10 anni** o periodo di assistenza se piu' lungo (art. 13 par. 13).

## Output atteso

Report strutturato come segue:

```
1. Sintesi delle coperture:
   - Punti coperti: N/8
   - Punti parzialmente coperti: M
   - Punti mancanti (BLOCKER per immissione sul mercato): K

2. Dettaglio per ogni punto dell'Allegato VII:
   - Punto 1 (descrizione generale): [coperto / parziale / mancante] - note specifiche
   - Punto 2 (progettazione, sviluppo, vulnerabilita'): [...] (focus su SBOM, CVD, contatto, distribuzione aggiornamenti)
   - Punto 3 (valutazione rischi): [...] (verifica che ogni requisito Allegato I parte I lettera a-m sia trattato o giustificato come non applicabile)
   - Punto 4 (periodo di assistenza): [...] (verifica >= 5 anni)
   - Punto 5 (norme/specifiche/certificazioni): [...]
   - Punto 6 (test reports): [...]
   - Punto 7 (DoC UE): [...] (verifica 8 elementi Allegato V)
   - Punto 8 (SBOM su richiesta): [...]

3. Requisiti formali:
   - Documentazione antecedente all'immissione (art. 31 par. 2): [OK / KO]
   - Lingua adeguata all'organismo notificato (art. 31 par. 4): [OK / KO]
   - Aggiornamento per periodo di assistenza (art. 31 par. 2): [previsto / non previsto]
   - Conservazione 10 anni (art. 13 par. 13): [previsto / non previsto]

4. Azioni richieste (in ordine di priorita'):
   - [BLOCKER 1: ...]
   - [BLOCKER 2: ...]
   - [Integrazione consigliata: ...]

Disclaimer: questa checklist e' un ausilio alla verifica formale. Non sostituisce ne' la valutazione tecnica di adeguatezza dei contenuti (di responsabilita' del fabbricante e dell'organismo notificato per i moduli B+C e H), ne' l'esame UE del tipo, ne' la sorveglianza del sistema qualita'.
```

## Limiti

- Il task **non valuta l'adeguatezza tecnica** dei contenuti (es. se la SBOM coglie effettivamente tutte le dipendenze di primo livello, se la valutazione dei rischi e' tecnicamente robusta): valuta solo la **presenza/copertura** dei punti formali.
- Il task **non sostituisce** l'esame dell'organismo notificato (per modulo B+C: Allegato VIII parte II punto 4) o la sorveglianza del sistema qualita' (per modulo H: parte IV punto 4).
- Il task non si pronuncia sulle **soluzioni tecniche** che soddisfano i requisiti dell'Allegato I parte I e parte II: si limita a verificare che la documentazione descriva tali soluzioni.
- Il task non verifica la **conformita' dei contenuti delle istruzioni utilizzatore** (Allegato II) rispetto alla realta' del prodotto (compito del fabbricante e degli auditor).
