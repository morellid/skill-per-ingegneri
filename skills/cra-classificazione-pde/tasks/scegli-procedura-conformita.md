# Task: Scelta del modulo di valutazione della conformita'

## Obiettivo

A partire dalla categoria del PDE gia' determinata (output del task `classifica-pde.md`), individuare le **procedure di valutazione della conformita'** ammesse ai sensi dell'art. 32 del Regolamento (UE) 2024/2847, segnalando:

- quali moduli sono **ammessi** (A, B+C, H, certificazione europea ex art. 27 par. 9 o art. 8 par. 1);
- in quali casi **interviene un organismo notificato**;
- quando il **numero ON** deve essere apposto accanto alla marcatura CE (art. 30 par. 4);
- la documentazione che la procedura comporta.

## Input richiesti

Chiedere all'utente, prima di applicare la procedura:

1. **Categoria CRA** del PDE (output del task `classifica-pde.md`: ordinario / importante Classe I / importante Classe II / critico).
2. **Norme armonizzate**: il fabbricante intende applicare **integralmente** le norme armonizzate, specifiche comuni o un sistema europeo di certificazione di livello "sostanziale"? (Determinante per i PDE Classe I.)
3. **Tipo di organizzazione del fabbricante**: ha un sistema qualita' approvato (rilevante per scelta del modulo H) o preferisce un modello a esame del tipo per modello (B+C)?
4. **Disponibilita' di un sistema europeo di certificazione della cibersicurezza** per la categoria specifica (Reg. (UE) 2019/881): si' / no / da verificare con ENISA.
5. **Software libero e open source qualificato** (art. 3 punto 48 e art. 32 par. 5)?
6. Per i **PDE critici**: e' gia' stato adottato un atto delegato ex art. 8 par. 1 che richiede certificazione europea obbligatoria? (Se no: vale il rinvio all'art. 32 par. 3.)

## Fonti

Procedura ancorata a:
- `references/estratti/reg-ue-2024-2847-cra-classificazione.md` sezione "3. Procedure di valutazione della conformita'".
- `references/fonti/reg-ue-2024-2847-cra.md` (art. 27 par. 9, art. 30, art. 32, Allegato VIII).

## Procedura

**Step A - Determina le procedure ammesse in base alla categoria**

A1. **PDE ordinario** (default, art. 32 par. 1):
- Modulo A (controllo interno) - Allegato VIII parte I;
- Modulo B + Modulo C (esame UE del tipo + conformita' al tipo) - Allegato VIII parti II + III;
- Modulo H (garanzia della qualita' totale) - Allegato VIII parte IV;
- Ove disponibile e applicabile: sistema europeo di certificazione della cibersicurezza (art. 27 par. 9).

A2. **PDE importante Classe I** (Art. 32 par. 2):
- Verifica con l'utente: il fabbricante intende applicare integralmente le **norme armonizzate** / specifiche comuni / certificazione UE di livello "sostanziale"?
  - Se **si'** (applicazione integrale): tutte le procedure del par. 1 sono ammesse (incluso modulo A);
  - Se **no** o **applicazione parziale** o **norme inesistenti**: solo **B+C** o **H** sono ammesse. Modulo A vietato.

A3. **PDE importante Classe II** (Art. 32 par. 3):
- Modulo B + Modulo C; oppure
- Modulo H; oppure
- Certificazione europea di cibersicurezza con livello almeno "sostanziale" (art. 27 par. 9).
- **Modulo A vietato**.

A4. **PDE critico** (Art. 32 par. 4):
- Se la Commissione ha adottato un **atto delegato ex art. 8 par. 1** che richiede certificazione obbligatoria: **certificato europeo di cibersicurezza** al livello richiesto (almeno "sostanziale").
- Se condizioni dell'art. 8 par. 1 **non sono soddisfatte** (es. atto delegato non adottato per quella categoria): si applicano le procedure dell'art. 32 par. 3 (come Classe II).

A5. **Open source qualificato** (Art. 32 par. 5): se il PDE si qualifica come software libero e open source ex art. 3 punto 48 e rientra nelle categorie dell'Allegato III, il fabbricante **puo' utilizzare le procedure dell'art. 32 par. 1** (incluso modulo A), purche' la **documentazione tecnica sia messa a disposizione del pubblico** al momento dell'immissione sul mercato.

**Step B - Coinvolgimento dell'organismo notificato**

- **Modulo A**: nessun organismo notificato.
- **Modulo B + Modulo C**: organismo notificato per la parte B (esame UE del tipo) e audit periodici sui processi di gestione delle vulnerabilita' (parte II punto 8). Per la parte C il controllo della produzione e' interno al fabbricante.
- **Modulo H**: organismo notificato approva il sistema qualita' e svolge sorveglianza con audit periodici (parte IV punti 3 e 4). **Il numero di identificazione dell'organismo notificato e' apposto accanto alla marcatura CE** (art. 30 par. 4).
- **Certificazione europea di cibersicurezza** (Reg. (UE) 2019/881): l'ente di valutazione e' quello previsto dal sistema europeo applicabile (rinvia all'ENISA). L'emissione di un certificato a livello "sostanziale" sopprime l'obbligo di valutazione di terzi per i requisiti corrispondenti (art. 27 par. 9, terzo periodo).

**Step C - Documentazione attesa**

Per ciascun modulo, la documentazione minima e':

C1. **Modulo A** (Allegato VIII parte I):
- Documentazione tecnica (art. 31 + Allegato VII);
- DoC UE (art. 28 + Allegato V), copia conservata 10 anni o periodo di assistenza (se piu' lungo);
- Apposizione marcatura CE (art. 30, **senza numero ON**).

C2. **Modulo B + C** (Allegato VIII parti II + III):
- Domanda di esame UE del tipo a un singolo organismo notificato (parte II punto 3) con dichiarazione di unicita' della domanda;
- Documentazione tecnica (art. 31 + Allegato VII) incl. analisi e valutazione dei rischi;
- Documentazione di supporto attestante l'adeguatezza delle soluzioni di progettazione;
- Certificato di esame UE del tipo rilasciato dall'organismo notificato (parte II punto 6);
- Per ciascun PDE prodotto: DoC UE per modello (parte III punto 3.2);
- Audit periodici sui processi di gestione vulnerabilita' (parte II punto 8);
- Apposizione marcatura CE (art. 30); numero ON **non obbligatorio** accanto alla marcatura.

C3. **Modulo H** (Allegato VIII parte IV):
- Domanda di valutazione del sistema qualita' a un singolo organismo notificato (punto 3.1) con dichiarazione di unicita';
- Documentazione tecnica per un modello di ciascuna categoria (punto 3.1 lett. b);
- Documentazione del sistema qualita' (punto 3.2) incl. obiettivi di qualita', struttura organizzativa, specifiche di progettazione, procedure, tecniche di controllo, esami e prove, documentazione qualita';
- Sorveglianza dell'organismo notificato (punto 4) incl. audit periodici e accesso ai locali;
- DoC UE per ciascun modello, conservata 10 anni o periodo di assistenza;
- Apposizione marcatura CE **seguita dal numero di identificazione dell'organismo notificato** (art. 30 par. 4).

C4. **Certificazione europea di cibersicurezza** (art. 27 par. 9 e art. 8 par. 1):
- Procedura definita dal sistema europeo applicabile (Reg. (UE) 2019/881);
- DoC UE redatta dal fabbricante, con riferimento al certificato europeo (Allegato V punto 6);
- Per i PDE critici, livello "sostanziale" minimo o quello superiore richiesto dall'atto delegato art. 8 par. 1.

**Step D - Output sintetico**

Indica all'utente:
- Procedura/e ammessa/e per la categoria;
- Procedura raccomandata in funzione di disponibilita' di norme armonizzate, sistema qualita', dimensione del fabbricante (PMI - art. 32 par. 6 - hanno tariffe ridotte);
- Documentazione richiesta in sintesi;
- Trattamento marcatura CE e numero ON;
- Rinvio al task `check-documentazione-tecnica.md` per la verifica puntuale dell'Allegato VII.

## Output atteso

```
1. Categoria CRA del PDE:
   - [PDE ordinario / Importante Classe I / Importante Classe II / Critico]
   - Riferimento: Art. [32 par. 1/2/3/4] del Regolamento (UE) 2024/2847.

2. Procedure ammesse:
   - [Modulo A] - SI / NO + motivazione (per Classe I dipende da applicazione integrale norme armonizzate)
   - [Modulo B + C] - SI / NO
   - [Modulo H] - SI / NO
   - [Certificazione europea di cibersicurezza] - SI (livello minimo "sostanziale") / NO

3. Procedura consigliata (con motivazione operativa):
   - [Modulo X] perche' [norme armonizzate disponibili / sistema qualita' approvato / categoria critica con atto delegato art. 8 par. 1 / disponibilita' certificazione europea / ecc.]

4. Coinvolgimento organismo notificato:
   - [Nessuno / Esame UE del tipo (modulo B) + audit periodici (modulo B + C) / Approvazione e sorveglianza sistema qualita' (modulo H) / Ente del sistema europeo di certificazione]
   - Numero ON accanto alla marcatura CE: [SI (solo modulo H) / NO]

5. Documentazione richiesta (sintesi):
   - Documentazione tecnica ex art. 31 + Allegato VII (sempre)
   - DoC UE ex art. 28 + Allegato V (sempre), conservata 10 anni o periodo di assistenza se piu' lungo (art. 13 par. 13)
   - Eventuali certificati: [esame UE del tipo / approvazione sistema qualita' / certificato europeo]

6. Note operative:
   - Se modulo H: numero ON sulla marcatura CE (art. 30 par. 4).
   - Se PMI/start-up: tariffe ridotte (art. 32 par. 6) e modulo semplificato documentazione (art. 33 par. 5).
   - Se OSS qualificato: par. 1 ammesso con doc tecnica pubblica (art. 32 par. 5).
   - L'organismo notificato deve essere selezionato dalla banca dati NANDO della Commissione europea (art. 43 par. 2).

7. Prossimo passo:
   - Prosegui con task `check-documentazione-tecnica.md` per verificare la documentazione tecnica.

Disclaimer: la scelta del modulo e dell'organismo notificato e' responsabilita' del fabbricante o del rappresentante autorizzato. La skill suggerisce le procedure ammesse, non costituisce parere legale ne' garantisce l'esito favorevole della valutazione.
```

## Limiti

- Non valida la **designazione effettiva** dell'organismo notificato: il fabbricante deve scegliere un organismo notificato attivo per il CRA (NANDO) dopo l'11 giugno 2026 (Capo IV, art. 71 par. 2).
- Non si pronuncia sulla **disponibilita' concreta** di un sistema europeo di certificazione di cibersicurezza per una specifica categoria: rinvia all'ENISA e agli atti di esecuzione applicabili.
- Non valuta la **convenienza economica** tra B+C e H per un fabbricante: la scelta dipende da considerazioni industriali (modello a serie/varianti, organizzazione qualita') che esulano dalla skill.
- Non valuta se le **norme armonizzate** sono "applicate integralmente" ex art. 32 par. 2: e' una valutazione tecnica che richiede l'analisi del progetto. La skill segnala il bivio e rinvia al fabbricante.
