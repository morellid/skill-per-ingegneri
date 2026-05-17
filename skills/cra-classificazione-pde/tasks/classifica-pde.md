# Task: Classificazione del PDE

## Obiettivo

Identificare la categoria in cui ricade un prodotto con elementi digitali (PDE), ai sensi degli artt. 7 e 8 e degli Allegati III e IV del **Regolamento (UE) 2024/2847**:

- **PDE ordinario** (default - art. 32 par. 1);
- **PDE importante - Classe I** (Allegato III, Classe I - art. 32 par. 2);
- **PDE importante - Classe II** (Allegato III, Classe II - art. 32 par. 3);
- **PDE critico** (Allegato IV - art. 32 par. 4).

Pre-requisito: aver eseguito (o aver concluso a colpo d'occhio) il task `check-ambito-applicabilita.md`. Se il PDE e' fuori ambito, questo task non si applica.

## Input richiesti

Chiedere all'utente, prima di applicare la procedura:

1. **Denominazione e tipologia commerciale** del prodotto.
2. **Funzionalita' principale**: qual e' la **funzione principale** del prodotto come immesso sul mercato? (Non la funzione secondaria.) Esempio: "Il prodotto e' un firewall hardware con secondaria capacita' di logging" -> funzionalita' principale = firewall.
3. **Esiste integrazione con altro prodotto**? Il prodotto e' venduto come componente integrato in altri prodotti (relevant per il caveat art. 7 par. 1 secondo periodo).
4. **Si tratta di software libero e open source** ex art. 3 punto 48?
5. **Stato delle norme armonizzate**: il fabbricante intende applicare integralmente le norme armonizzate, specifiche comuni o un sistema europeo di certificazione di livello "sostanziale"? (Rilevante per Classe I.)

## Fonti

Procedura ancorata a:
- `references/estratti/reg-ue-2024-2847-cra-classificazione.md` sezione "2. Classificazione del PDE".
- `references/fonti/reg-ue-2024-2847-cra.md` (art. 7, art. 8, Allegato III, Allegato IV).

## Procedura

**Step A - Confronto con Allegato IV (PDE critici)**

A1. La funzionalita' principale del PDE corrisponde a una delle **3 categorie dell'Allegato IV**?
- 1. Dispositivi hardware con cassette di sicurezza (HSM);
- 2. Gateway per contatori intelligenti nell'ambito di sistemi di misurazione intelligenti (art. 2, punto 23, Direttiva (UE) 2019/944), e altri dispositivi a fini di sicurezza avanzati, compreso il trattamento crittografico sicuro;
- 3. Carte intelligenti o dispositivi analoghi, compresi gli elementi sicuri.

A2. Se si': il PDE e' **CRITICO** (Art. 8 + Allegato IV). Vai allo Step D (matrice procedure).

A3. Se no: prosegui allo Step B.

**Step B - Confronto con Allegato III Classe II**

B1. La funzionalita' principale corrisponde a una delle **4 categorie di Classe II**?
- 1. Ipervisori e sistemi di runtime container che supportano l'esecuzione virtualizzata di sistemi operativi e ambienti simili;
- 2. Firewall, sistemi di rilevamento e prevenzione delle intrusioni (IDS/IPS);
- 3. Microprocessori a prova di manomissione;
- 4. Microcontrollori a prova di manomissione.

B2. Se si': il PDE e' **IMPORTANTE - Classe II** (Art. 7 par. 1 + Allegato III Classe II). Vai allo Step D.

B3. Se no: prosegui allo Step C.

**Step C - Confronto con Allegato III Classe I**

C1. La funzionalita' principale corrisponde a una delle **19 categorie di Classe I**? Elenco:
1. Sistemi di gestione dell'identita' / accessi privilegiati / lettori autenticazione e controllo (incl. biometrici).
2. Browser autonomi e incorporati.
3. Sistemi di gestione delle password.
4. Software antivirus / antimalware (cerca, rimuove, mette in quarantena software maligni).
5. PDE con funzione di rete privata virtuale (VPN).
6. Sistemi di gestione della rete.
7. Sistemi di gestione delle informazioni e degli eventi di sicurezza (SIEM).
8. Boot manager.
9. Infrastrutture a chiave pubblica (PKI) e software per il rilascio di certificati digitali.
10. Interfacce di rete fisiche e virtuali.
11. Sistemi operativi.
12. Router, modem per la connessione a Internet e switch.
13. Microprocessori con funzionalita' legate alla sicurezza.
14. Microcontrollori con funzionalita' legate alla sicurezza.
15. ASIC e FPGA con funzionalita' legate alla sicurezza.
16. Assistenti virtuali di uso generale per case intelligenti (smart home).
17. Prodotti per case intelligenti con funzionalita' di sicurezza (serrature smart, telecamere, baby monitor, allarmi).
18. Giocattoli connessi a Internet disciplinati dalla Direttiva 2009/48/CE con funzionalita' sociali interattive (parlare, filmare) o geolocalizzazione.
19. Wearable personali per monitoraggio salute (non coperti da Reg. 2017/745 o 2017/746) e wearable destinati ai bambini.

C2. Se si': il PDE e' **IMPORTANTE - Classe I** (Art. 7 par. 1 + Allegato III Classe I). Vai allo Step D.

C3. Se no: il PDE e' **ORDINARIO** (default, art. 32 par. 1). Vai allo Step D.

**Step D - Output con matrice procedure**

Indica all'utente:
- Categoria CRA;
- Articolo del regolamento che la fonda (Art. 7 par. 1 / Art. 8 par. 1);
- Allegato di riferimento (III Classe I / III Classe II / IV);
- Quali procedure di valutazione della conformita' sono ammesse (rimanda all'art. 32 e al task `scegli-procedura-conformita.md`).

Caveat applicabili:

- **Integrazione (Art. 7 par. 1 secondo periodo)**: se il PDE che corrisponde a una categoria dell'Allegato III e' integrato in un altro prodotto, **il prodotto integrante non diventa automaticamente** un PDE importante. La classificazione del prodotto integrante va fatta separatamente sulla sua propria funzionalita' principale.
- **Open source qualificato (Art. 32 par. 5)**: per i fabbricanti di PDE che si qualificano come software liberi e open source rientranti in Allegato III, e' ammesso usare le procedure dell'art. 32 par. 1 (incluso modulo A) **a condizione che la documentazione tecnica sia messa a disposizione del pubblico** al momento dell'immissione sul mercato.
- **Atto di esecuzione attesa (Art. 7 par. 4)**: entro l'11 dicembre 2025 la Commissione adotta un atto di esecuzione con la **descrizione tecnica** delle categorie dell'Allegato III (Classi I e II) e dell'Allegato IV. Per categorie di confine, segnala il dubbio e rinvia al testo dell'atto di esecuzione quando pubblicato.
- **Atti delegati attesi (Art. 8 par. 1)**: per i PDE dell'Allegato IV, la Commissione adottera' atti delegati per imporre che ottengano un certificato europeo di cibersicurezza ad almeno livello "sostanziale". Fino a tali atti, vale il rinvio all'art. 32 par. 3 (procedure di Classe II importante).

## Output atteso

```
1. Categoria del PDE:
   - [PDE ordinario / PDE importante Classe I / PDE importante Classe II / PDE critico]

2. Motivazione:
   - Funzionalita' principale dichiarata: "..."
   - Categoria di riferimento: Allegato [III Classe I/II o IV], punto N: "<denominazione esatta dall'Allegato>"
   - Fondamento normativo: Art. [7 par. 1 / 8 par. 1] del Regolamento (UE) 2024/2847.

3. Caveat applicabili:
   - [Integrazione in altro prodotto: si/no, se si' nota il caveat dell'Art. 7 par. 1 secondo periodo]
   - [Open source qualificato: si/no, se si' nota il caveat dell'Art. 32 par. 5 - doc tecnica pubblica]
   - [Categorie di confine: rinvio all'atto di esecuzione attesa (Art. 7 par. 4) o all'atto delegato attesa (Art. 8 par. 1)]

4. Procedure ammesse (sintesi):
   - [B+C, H, certificazione UE, modulo A (se ammesso) - elenco rapido]
   - Per il dettaglio operativo, prosegui con task `scegli-procedura-conformita.md`.

Disclaimer: questa classificazione e' un ausilio alla riflessione tecnica. La responsabilita' della corretta inquadramento del prodotto nelle classi dell'Allegato III/IV ricade sul fabbricante o sul rappresentante autorizzato ex art. 13 e 18-21 del Regolamento (UE) 2024/2847.
```

## Limiti

- Il task **non interpreta categorie di confine**: se la funzionalita' principale potrebbe rientrare in piu' categorie (es. un firewall hardware che include anche IDS), il task indica la categoria piu' restrittiva (Classe II) e segnala il dubbio.
- Il task non valuta la **modifica sostanziale** ex art. 3 punto 30 di un PDE gia' immesso sul mercato: per i PDE immessi prima dell'11 dicembre 2027, l'applicabilita' del regolamento dipende dall'eventuale modifica sostanziale ex art. 69 par. 2.
- Il task non si pronuncia sull'**applicabilita' degli atti delegati** che modificheranno gli Allegati III/IV (art. 7 par. 3 e art. 8 par. 2): per modifiche di questi allegati, ritestare il prodotto rispetto al testo aggiornato.
