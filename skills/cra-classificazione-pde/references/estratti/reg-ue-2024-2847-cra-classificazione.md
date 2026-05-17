# Estratto - Classificazione PDE e procedura di valutazione della conformita' (CRA)

Estratto curato dal Regolamento (UE) 2024/2847 (Cyber Resilience Act), focalizzato sui tre nodi che la skill `cra-classificazione-pde` deve coprire:

1. Verifica se un prodotto rientra nell'ambito CRA (Art. 2-3, definizione di PDE).
2. Classificazione del PDE (default, importante Classe I, importante Classe II, critico) sulla base degli artt. 7-8 e degli Allegati III-IV.
3. Selezione del modulo di valutazione della conformita' applicabile (Art. 32) e della documentazione tecnica richiesta (Art. 31 + Allegato VII).

Fonte primaria: `references/fonti/reg-ue-2024-2847-cra.md` (trascrizione fedele del PDF ufficiale `not_in_repo/reg-ue-2024-2847-cra.pdf`, SHA256 `7c9ae1d683e7fbafef4ce5898b33279bb6f5f6746df3c4a08911c1a0d3a31db3`).

---

## 1. Ambito di applicazione: che cos'e' un PDE soggetto a CRA

**Art. 3 punto 1**: «prodotto con elementi digitali»: qualsiasi prodotto software o hardware e le relative soluzioni di elaborazione dati da remoto, compresi i componenti software o hardware immessi sul mercato separatamente.

**Art. 2 par. 1 (filtro positivo)**: il regolamento si applica ai PDE messi a disposizione sul mercato la cui **finalita' prevista o utilizzo ragionevolmente prevedibile include una connessione dati logica o fisica diretta o indiretta a un dispositivo o a una rete**.

**Art. 2 par. 2-4, 7 (esclusioni puntuali)**: il CRA **non si applica** ai PDE coperti da:
- Reg. (UE) 2017/745 (dispositivi medici);
- Reg. (UE) 2017/746 (diagnostici medici in vitro);
- Reg. (UE) 2019/2144 (omologazione veicoli a motore);
- Reg. (UE) 2018/1139 (aviazione civile - i PDE certificati);
- Direttiva 2014/90/UE (equipaggiamento marittimo);
- PDE sviluppati esclusivamente per sicurezza nazionale, difesa, o trattamento di informazioni classificate.

**Art. 2 par. 6**: esclusi anche i **pezzi di ricambio identici** fabbricati con le stesse specifiche.

**Art. 2 par. 5**: la Commissione puo' limitare/escludere l'applicazione del CRA quando altre norme dell'Unione coprono gli stessi rischi con livello pari o superiore (con atti delegati).

**Decision rule operativa**: un prodotto rientra nel CRA se e solo se (a) ha software o hardware con elaborazione dati, (b) la finalita' prevista o l'uso ragionevolmente prevedibile include una connessione dati a dispositivo/rete, (c) non e' tra le esclusioni del par. 2-7.

---

## 2. Classificazione del PDE

### Default: PDE "ordinario" (non importante, non critico)

Se il PDE rientra nell'ambito ex art. 2 ma non ha la **funzionalita' principale** corrispondente a una categoria dell'Allegato III (importanti) o dell'Allegato IV (critici), e' un PDE ordinario. Procedure ammesse: tutte quelle dell'art. 32 par. 1 (anche modulo A controllo interno).

### PDE importanti (Art. 7, Allegato III)

**Art. 7 par. 1**: un PDE e' considerato **importante** se la sua **funzionalita' principale** corrisponde a una categoria elencata nell'Allegato III. L'integrazione di un PDE importante in un altro prodotto non rende automaticamente quel prodotto integrante un PDE importante.

**Art. 7 par. 2 - Criteri ratio delle categorie (interpretazione)**: le categorie elencate nell'Allegato III, Classi I e II, soddisfano **almeno uno** dei criteri:
- a) il PDE svolge **principalmente funzioni essenziali per la cibersicurezza** di altri prodotti, reti o servizi (es. autenticazione, accesso, intrusion detection, sicurezza dei terminali, protezione di rete);
- b) il PDE svolge una funzione che **comporta un rischio significativo di effetti negativi** in ragione della sua intensita' e capacita' di perturbare/controllare/danneggiare un gran numero di altri prodotti o la salute/sicurezza/incolumita' degli utenti (es. funzioni centrali di sistema: gestione della rete, controllo configurazione, virtualizzazione, trattamento dati personali).

**Classe I (Allegato III) - 19 categorie** (criteri di rischio "ordinario" come PDE importante):
1. Sistemi di gestione dell'identita' / accessi privilegiati / lettori autenticazione e controllo (incl. biometrici).
2. Browser autonomi e incorporati.
3. Password manager.
4. Antivirus / antimalware.
5. PDE con funzione VPN.
6. Sistemi di gestione della rete.
7. SIEM.
8. Boot manager.
9. PKI e software per certificati digitali.
10. Interfacce di rete fisiche e virtuali.
11. Sistemi operativi.
12. Router, modem, switch (connessione Internet).
13. Microprocessori con funzionalita' di sicurezza.
14. Microcontrollori con funzionalita' di sicurezza.
15. ASIC e FPGA con funzionalita' di sicurezza.
16. Assistenti virtuali generali per case intelligenti.
17. Prodotti per case intelligenti con funzionalita' di sicurezza (serrature smart, telecamere, baby monitor, allarmi).
18. Giocattoli connessi a Internet (dir. 2009/48/CE) con funzionalita' sociali interattive o geolocalizzazione.
19. Wearable personali per monitoraggio salute (non coperti dai Reg. 2017/745 / 2017/746), e wearable per bambini.

**Classe II (Allegato III) - 4 categorie** (rischio piu' elevato; valutazione con organismo notificato obbligatoria):
1. Ipervisori e sistemi di runtime container che supportano l'esecuzione virtualizzata di sistemi operativi e ambienti simili.
2. Firewall, sistemi di rilevamento e prevenzione delle intrusioni (IDS/IPS).
3. Microprocessori a prova di manomissione.
4. Microcontrollori a prova di manomissione.

**Art. 7 par. 4**: entro l'11 dicembre 2025 la Commissione adotta un **atto di esecuzione** con la descrizione tecnica delle categorie dell'Allegato III (Classi I e II) e dell'Allegato IV.

### PDE critici (Art. 8, Allegato IV)

**Art. 8 par. 1**: la Commissione puo' adottare atti delegati per imporre che i PDE con funzionalita' principale di una categoria dell'Allegato IV debbano **ottenere un certificato europeo di cibersicurezza ad almeno livello "sostanziale"** (a norma del Reg. (UE) 2019/881). In assenza di tale atto delegato, i PDE critici sono soggetti alle procedure di cui all'**art. 32 par. 3** (le stesse della Classe II importante).

**Allegato IV - 3 categorie critiche**:
1. Dispositivi hardware con cassette di sicurezza (HSM).
2. Gateway per contatori intelligenti nell'ambito di sistemi di misurazione intelligenti (art. 2, punto 23, Direttiva (UE) 2019/944), e altri dispositivi a fini di sicurezza avanzati, compreso il trattamento crittografico sicuro.
3. Carte intelligenti o dispositivi analoghi, compresi gli elementi sicuri.

**Art. 8 par. 2**: criteri per identificare le categorie critiche, in aggiunta ai criteri dell'art. 7 par. 2:
- a) **dipendenza critica** dei soggetti essenziali (art. 3 Direttiva (UE) 2022/2555 - NIS2) dalla categoria di PDE;
- b) gli incidenti/vulnerabilita' della categoria potrebbero causare **gravi perturbazioni delle catene di approvvigionamento critiche**.

---

## 3. Procedure di valutazione della conformita' (Art. 32 + Allegato VIII)

I quattro moduli ammessi dal CRA (Allegato VIII):
- **Modulo A** (Allegato VIII, parte I): controllo interno del fabbricante, **senza organismo notificato**. Il fabbricante redige la documentazione tecnica (Allegato VII), appone la marcatura CE e compila la DoC UE, conservandola per 10 anni o per il periodo di assistenza.
- **Modulo B** (Allegato VIII, parte II): **esame UE del tipo** condotto da un organismo notificato (di scelta del fabbricante, presentazione domanda a un unico organismo). L'organismo esamina la progettazione tecnica e lo sviluppo, esamina i campioni di parti critiche, redige una relazione di valutazione, rilascia il **certificato di esame UE del tipo** se conforme, e svolge audit periodici sui processi di gestione vulnerabilita'.
- **Modulo C** (Allegato VIII, parte III): **conformita' al tipo basata sul controllo interno della produzione**, segue il modulo B. Il fabbricante garantisce la conformita' di ciascun PDE al tipo certificato; compila la DoC UE per modello.
- **Modulo H** (Allegato VIII, parte IV): **garanzia della qualita' totale**. Il fabbricante applica un sistema qualita' approvato dall'organismo notificato (per progettazione, sviluppo, produzione, gestione vulnerabilita'). L'organismo svolge audit periodici. **Il numero di identificazione dell'organismo notificato e' apposto accanto alla marcatura CE** (art. 30 par. 4).

### Matrice procedure (Art. 32) - tabella decisionale

| Categoria | Norme armonizzate / spec. comuni / certif. UE liv. sostanziale applicate? | Procedure ammesse |
| --- | --- | --- |
| PDE ordinario (non importante, non critico) - Art. 32 par. 1 | irrilevante | Modulo A, oppure B+C, oppure H, oppure certificazione UE (se disponibile e applicabile, art. 27 par. 9) |
| PDE importante Classe I (Allegato III) - Art. 32 par. 2 | applicate **integralmente** | Procedure del par. 1 (anche modulo A) |
| PDE importante Classe I (Allegato III) - Art. 32 par. 2 | non applicate o applicate solo in parte, o inesistenti | **B+C** oppure **H** |
| PDE importante Classe II (Allegato III) - Art. 32 par. 3 | irrilevante (modulo A vietato) | **B+C**, oppure **H**, oppure **certificazione UE liv. sostanziale** (se disponibile, art. 27 par. 9) |
| PDE critico (Allegato IV) - Art. 32 par. 4 | / | **Certificazione UE liv. sostanziale** se richiesto da atto delegato ex art. 8 par. 1. Altrimenti: una delle procedure del par. 3 (B+C, H, certificazione UE sostanziale) |

Note operative:
- Il **modulo A (controllo interno) non e' mai ammesso per Classe II o critici**.
- Per il modulo H il fabbricante deve apporre il numero di identificazione dell'organismo notificato accanto alla marcatura CE (art. 30 par. 4); per B+C non c'e' questo obbligo, ma il numero ON puo' essere apposto a seguito dell'esame.
- I PDE **open source qualificati** (art. 32 par. 5) rientranti nell'Allegato III possono usare le procedure del par. 1 (anche modulo A) **a condizione che la documentazione tecnica sia pubblica** al momento dell'immissione sul mercato.
- L'eventuale **certificato europeo di cibersicurezza al livello "sostanziale"** sopprime l'obbligo di valutazione da parte di terzi (art. 27 par. 9, per i requisiti corrispondenti).

---

## 4. Documentazione tecnica (Art. 31 + Allegato VII)

**Art. 31 par. 1**: la documentazione tecnica contiene tutti i dati o dettagli pertinenti relativi ai mezzi utilizzati dal fabbricante per garantire la conformita' del PDE e dei processi. Contiene **almeno gli elementi dell'Allegato VII**.

**Art. 31 par. 2**: redatta **prima dell'immissione sul mercato** e aggiornata almeno per la durata del periodo di assistenza.

**Art. 31 par. 4**: lingua del documento: **lingua ufficiale dello Stato membro in cui e' stabilito l'organismo notificato**, o lingua accettata da quest'ultimo.

**Allegato VII - elementi (8 punti)**:

1. **Descrizione generale**: finalita' prevista; versioni del software; per hardware, fotografie/illustrazioni di caratteristiche esterne, marcatura, disposizione interna; informazioni e istruzioni utilizzatore (Allegato II).

2. **Descrizione progettazione, sviluppo, produzione e gestione vulnerabilita'**:
   - progettazione e sviluppo: disegni/schemi, **descrizione dell'architettura del sistema** (come i componenti software si alimentano reciprocamente e si integrano nel processo complessivo);
   - processi di gestione delle vulnerabilita': **SBOM** (distinta base del software), **politica di divulgazione coordinata** (CVD), **prova della fornitura di un indirizzo di contatto** per segnalazione vulnerabilita', soluzioni tecniche per **distribuzione sicura aggiornamenti**;
   - processi di produzione e monitoraggio e loro convalida.

3. **Valutazione dei rischi di cibersicurezza** (a norma dell'art. 13), incluse le modalita' di applicazione dei requisiti essenziali dell'Allegato I, parte I.

4. **Informazioni rilevanti per determinare il periodo di assistenza** (art. 13 par. 8): considerazioni su durata di utilizzo prevista, aspettative ragionevoli degli utilizzatori, natura del prodotto, periodi di assistenza di prodotti analoghi.

5. **Elenco delle norme armonizzate, specifiche comuni, sistemi europei di certificazione** applicati (integralmente o in parte); qualora non applicati, **descrizione delle soluzioni alternative** adottate per soddisfare i requisiti essenziali dell'Allegato I, parti I e II.

6. **Relazioni delle prove** (test reports) eseguite per verificare la conformita' del PDE e dei processi di gestione vulnerabilita' ai requisiti essenziali.

7. **Copia della DoC UE** (Allegato V) o riferimento ad essa.

8. **SBOM** (distinta base del software), a seguito di richiesta motivata di un'autorita' di vigilanza del mercato, ove necessario per la verifica.

---

## 5. Dichiarazione di conformita' UE (Art. 28 + Allegati V e VI)

**Art. 28 par. 1**: la DoC UE attesta il rispetto dei requisiti essenziali di cibersicurezza dell'Allegato I.

**Art. 28 par. 2**: struttura tipo nell'**Allegato V**, contiene anche elementi delle procedure dell'Allegato VIII. **Resa disponibile nelle lingue richieste** dallo Stato membro di immissione/messa a disposizione.

**Art. 28 par. 3**: se al PDE si applicano piu' atti dell'Unione che prescrivono una DoC, si redige una **unica DoC UE** per tutti gli atti, con i loro riferimenti.

**Art. 28 par. 4**: con la DoC UE il fabbricante si assume la responsabilita' della conformita'.

**Contenuto minimo (Allegato V)** - 8 elementi:
1. nome, tipo, identificazione univoca del PDE;
2. nome e indirizzo del fabbricante o del rappresentante autorizzato;
3. attestazione di rilascio sotto responsabilita' esclusiva del fornitore;
4. oggetto della dichiarazione (PDE tracciabile, anche con fotografia);
5. attestazione di conformita' alla pertinente normativa di armonizzazione dell'Unione;
6. **riferimenti alle norme armonizzate utilizzate** o ad altre specifiche comuni o certificazioni di cibersicurezza;
7. ove applicabile, **nome e numero dell'organismo notificato**, descrizione della procedura di valutazione applicata, identificazione del certificato rilasciato;
8. informazioni supplementari (firma, luogo/data, nome/funzione/firma).

**DoC UE semplificata (Allegato VI)** - formula:
> "Con la presente, [nome del fabbricante] dichiara che il prodotto con elementi digitali [denominazione] e' conforme al regolamento (UE) 2024/2847. Il testo completo della DoC UE e' disponibile al seguente indirizzo Internet: ..."

Si applica art. 13 par. 20 (fornitura con il PDE).

---

## 6. Marcatura CE (Artt. 29-30)

**Art. 29**: principi generali ai sensi dell'art. 30 del Reg. (CE) 765/2008.

**Art. 30 par. 1**: marcatura visibile, leggibile, indelebile. Su software: sulla DoC UE o sul sito web di accompagnamento, in sezione facilmente accessibile.

**Art. 30 par. 2**: altezza puo' essere < 5 mm purche' visibile/leggibile.

**Art. 30 par. 3**: apposta prima dell'immissione sul mercato. Puo' essere seguita da pittogramma di rischio di cibersicurezza specifico.

**Art. 30 par. 4**: per la procedura **modulo H (garanzia qualita' totale)**, la marcatura CE e' **seguita dal numero di identificazione dell'organismo notificato**. (Per B+C il numero ON non e' obbligatorio sulla marcatura, ma le procedure prevedono la sua identificazione nella DoC e nel certificato di esame UE del tipo.)

**Art. 58 (non conformita' formali, ai fini della vigilanza del mercato)**: l'autorita' di vigilanza chiede al fabbricante di porre fine se: marcatura CE apposta in violazione, marcatura non apposta, DoC non redatta o non corretta, numero ON non apposto quando applicabile, documentazione tecnica non disponibile o incompleta.

---

## 7. Date di applicazione (Art. 71)

- **10 dicembre 2024**: entrata in vigore.
- **11 giugno 2026**: applicazione del Capo IV (notifica organismi - artt. 35-51).
- **11 settembre 2026**: applicazione dell'art. 14 (obblighi di segnalazione).
- **11 dicembre 2027**: applicazione generale del regolamento.

**Disposizioni transitorie (Art. 69)**:
- I PDE immessi prima dell'11 dicembre 2027 sono soggetti al regolamento **solo se sottoposti a modifiche sostanziali** dopo tale data.
- L'art. 14 (segnalazione) si applica anche ai PDE immessi prima dell'11 dicembre 2027 (deroga).
- I certificati di esame UE del tipo gia' rilasciati in altre normative restano validi **fino all'11 giugno 2028** (salvo scadenza anteriore).

---

## 8. Sanzioni (Art. 64) - sintesi per dimensionare il rischio

Tre fasce di sanzione amministrativa pecuniaria:
- **Non conformita' ai requisiti essenziali (Allegato I) e agli obblighi degli artt. 13 e 14**: fino a **15 000 000 EUR o 2,5 % del fatturato mondiale totale annuo**.
- **Non conformita' agli obblighi degli artt. 18-23, 28, 30 par. 1-4, 31 par. 1-4, 32 par. 1-3, 33 par. 5, 39, 41, 47, 49, 53**: fino a **10 000 000 EUR o 2 % del fatturato**.
- **Informazioni inesatte/incomplete/fuorvianti** agli organismi notificati o alle autorita' di vigilanza: fino a **5 000 000 EUR o 1 % del fatturato**.

(Si prende il maggiore tra euro e percentuale di fatturato. Microimprese/PI hanno alcune esenzioni puntuali sui termini dell'art. 14. Gestori OSS: esclusi dalle sanzioni.)

---

## 9. Punti di attenzione per il professionista (non sono affermazioni normative ma rinvii)

- L'atto di esecuzione dell'**11 dicembre 2025 (art. 7 par. 4)** sara' determinante per la **descrizione tecnica** delle categorie dell'Allegato III. Fino a quel momento la lettura delle categorie va fatta sulla base del testo letterale dell'allegato, e la skill rinvia il giudizio di confine al fabbricante/professionista firmatario.
- Gli **atti delegati ex art. 8 par. 1** definiranno quali categorie dell'Allegato IV richiederanno effettivamente la certificazione UE livello "sostanziale". In assenza di tali atti, vale il rinvio all'art. 32 par. 3.
- Per il **modulo H** servono organismi notificati (NANDO) che coprano sia la procedura sia il prodotto specifico: il fabbricante deve scegliere un organismo regolarmente notificato per il CRA dopo l'11 giugno 2026.
- Il **periodo di assistenza** minimo di 5 anni (art. 13 par. 8) e' un requisito strutturale che incide sulla classificazione documentale e sulla conservazione 10 anni dei documenti (art. 13 par. 13).
