# AGENTS.md - cbam-declarant-trimestrale

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto al **dichiarante CBAM autorizzato** (importatore stabilito UE o rappresentante doganale indiretto) nella fase definitiva del Carbon Border Adjustment Mechanism, applicabile dal **1° gennaio 2026** ai sensi del Regolamento (UE) 2023/956 come modificato dal Regolamento (UE) 2025/2083 (Omnibus CBAM).

La skill copre i quattro nuclei di adempimento lato dichiarante: verifica della necessita' di qualifica + applicabilita' delle deroghe (Y128/Y134-Y238), pianificazione dell'**obbligo trimestrale del 50 %** sui certificati CBAM (Art. 22 §2, dal 2027), redazione della **dichiarazione CBAM annuale** (Art. 6, entro 30/9, prima volta 2027 per anno 2026) e mappatura dell'**esposizione sanzionatoria** (Art. 26).

Resta fuori scope: procedura di autorizzazione nel registro CBAM (Reg. esec. 3210/2024 - flusso operativo), calcolo emissioni effettive ex Allegato IV punti 2-3 (richiede dati impianto del gestore paese terzo + verifica Art. 8), determinazione caso per caso dell'ambito merceologico (Allegato I), atti delegati e di esecuzione di secondo livello in continua evoluzione.

## Fonti autoritative

- **Regolamento (UE) 2023/956 (CBAM) - testo consolidato 20/10/2025** - SHA256 e binary path in `references/sources.yaml` con id `reg-ue-2023-956-cbam-consolidato`. Trascrizione fedele degli articoli della fase definitiva (Capo I-V, Allegati I, III, IV, V, VII) in `references/fonti/reg-ue-2023-956-cbam-consolidato.md`. Il marker `▼M1` segnala disposizioni modificate dal Reg. 2025/2083.
- **Regolamento (UE) 2025/2083 (Omnibus CBAM)** - id `reg-ue-2025-2083-cbam-omnibus`. Trascrizione integrale considerando + dispositivo in `references/fonti/reg-ue-2025-2083-cbam-omnibus.md`.
- **Circolare ADM n. 36/2025 del 24/12/2025** - id `circ-adm-36-2025-cbam`. Trascrizione in `references/fonti/circ-adm-36-2025-cbam.md`. Operativa per ADM Italia (codici TARIC, articolazioni territoriali).
- **Avviso ADM del 21/10/2025** - id `avviso-adm-cbam-211025`. Trascrizione in `references/fonti/avviso-adm-cbam-211025.md`.

Estratti curati gia' preparati in `references/estratti/`:
- `reg-ue-2023-956-articoli-fase-definitiva.md` - sezioni A-F (ambito, qualifica, dichiarazione, certificati, sanzioni, tempistiche).
- `reg-ue-2025-2083-considerando-chiave.md` - considerando 2-38 raggruppati per tema.
- `circ-adm-36-2025-codici-taric.md` - tabella codici TARIC + formalismo Y128.
- `avviso-adm-conseguenze-non-conformita.md` - blocco/rifiuto sdoganamento/sanzioni.

## Articoli e punti chiave

Quando l'agent produce output, **cita sempre articolo e paragrafo** del Reg. 2023/956 consolidato (es. "Art. 22 §2 lettera b ▼M1"); il marker `▼M1` distingue le disposizioni introdotte/modificate dall'Omnibus. Riferimenti piu' frequenti:

- **Art. 2 §1**: ambito oggettivo (merci Allegato I, perfezionamento attivo Art. 256 CDU).
- **Art. 2 §3 ▼M1**: esclusione attivita' militari (Y135).
- **Art. 2 §3bis ▼M1**: esclusione elettricita'/idrogeno piattaforma continentale/ZEE Allegato III (Y136).
- **Art. 2 §4**: esclusione territori Allegato III punto 1 / Y134; Y237 per merci di origine UE.
- **Art. 2bis ▼M1 + Allegato VII punto 1**: esenzione de minimis, soglia unica **50 t** di massa netta su base annua civile (cumulativo ferro/acciaio + alluminio + fertilizzanti + cemento; **non** elettricita' ne' idrogeno). Codice TARIC **Y137**.
- **Art. 3 punto 15 ▼M1**: definizione di "importatore" (include il conto di appuramento Art. 175 §5 Reg. del. 2015/2446).
- **Art. 4**: obbligo di importazione solo da dichiarante CBAM autorizzato.
- **Art. 5 §1ter ▼M1**: chi prevede di superare la soglia deve presentare domanda **prima** del superamento.
- **Art. 5 §§2-2bis ▼M1**: rappresentante doganale indiretto sempre autorizzato (anche se importatore esentato Art. 2bis); soggetto agli stessi obblighi dell'importatore.
- **Art. 6 §1 ▼M1**: dichiarazione CBAM annuale entro **30 settembre**, prima volta nel **2027 per l'anno 2026**.
- **Art. 6 §2 ▼M1 lettere a-d**: contenuto (quantitativo comprese merci sotto soglia, emissioni incorporate, numero certificati con detrazioni Art. 9 e adeguamento Art. 31, relazione di verifica solo se emissioni effettive).
- **Art. 7 §2 ▼M1**: scelta tra emissioni effettive (Allegato IV punti 2-3) e valori predefiniti (Allegato IV punto 4.1).
- **Art. 8 §1 ▼M1**: verifica accreditata obbligatoria **solo** per emissioni effettive.
- **Art. 9 ▼M1**: detrazione del carbon price pagato in paese terzo (con certificazione di persona indipendente; conservazione 4 anni).
- **Art. 17 §7bis ▼M1**: **deroga transitoria** - chi presenta domanda entro **31/3/2026** puo' continuare a importare fino alla decisione e comunque non oltre il **27/9/2026** (codice TARIC Y238). Se respinta -> sanzioni Art. 26 §2bis sulle emissioni nel periodo.
- **Art. 20 §1 ▼M1**: vendita certificati via **piattaforma centrale comune** dal **1/2/2027**.
- **Art. 21 §1 ▼M1**: prezzo settimanale = media chiusure quote EU ETS della settimana.
- **Art. 21 §1bis ▼M1**: **deroga 2026** - prezzo = media trimestrale ETS del trimestre di importazione.
- **Art. 22 §1 ▼M1**: restituzione entro **30/9**, prima volta 2027 per anno 2026.
- **Art. 22 §2 ▼M1**: **obbligo trimestrale 50 %** dal 2027 - certificati su conto a fine trimestre ≥ 50 % delle emissioni incorporate cumulate dall'inizio dell'anno, calcolate via (a) valori predefiniti **senza maggiorazione** del punto 4.1 Allegato IV, oppure (b) numero certificati restituiti per l'anno precedente se stesse merci/NC/paesi. Tiene conto dell'adeguamento Art. 31.
- **Art. 22 §2bis ▼M1**: chi supera la soglia in corso d'anno rispetta l'obbligo entro la fine del trimestre successivo.
- **Art. 23 ▼M1**: riacquisto eccedenza entro 31 ottobre; limite = certificati che il dichiarante doveva acquistare ex Art. 22 §2 nell'anno; certificati 2027 per 2026 riacquistabili solo nel 2027.
- **Art. 24 §1 ▼M1**: cancellazione automatica certificati il **1° novembre di ogni anno** per i certificati acquistati nell'anno anteriore all'anno civile precedente.
- **Art. 25 §1 ▼M1**: ADM/autorita' doganali autorizzano l'importazione solo da dichiarante CBAM autorizzato (fatto salvo Art. 2bis).
- **Art. 25bis ▼M1**: monitoraggio soglia (lista importatori >90 % soglia trasmessa periodicamente; accordi non genuini di frazionamento = grave violazione Art. 17 §2 lettera a).
- **Art. 26 §1 ▼M1**: sanzione per ogni certificato non restituito = **importo Art. 16 §3 Direttiva 2003/87/CE** (€100 indicizzato + maggiorazione §4) applicabile **nell'anno di importazione**.
- **Art. 26 §1bis ▼M1**: riduzione possibile se informazioni inesatte da terzi (verificatore o persona indipendente che certifica il prezzo del carbonio).
- **Art. 26 §2 ▼M1**: importazione non consentita o autorizzazione respinta -> **da 3 a 5 volte** la sanzione §1.
- **Art. 26 §2bis ▼M1**: non autorizzati che superano la soglia -> sanzione su **tutte** le emissioni dell'anno civile; il pagamento dispensa da dichiarazione/restituzione. Riduzione se superamento ≤ **10 %** della soglia o caso Art. 17 §7bis respinto (mai sotto il livello §1).
- **Art. 26 §4bis ▼M1**: calcolo delle quantita' di certificati ai fini §1 e §2 - **massa netta + valori predefiniti + adeguamento Art. 31**.

Per ADM Italia (Circolare 36/2025):
- **Codici TARIC** Y128 (numero conto CBAM), Y134-Y137 (deroghe), Y237 (origine UE), Y238 (domanda 31/3/2026).
- **Formalismo Y128**: `CBAM-XX-YYYY-AAANNNNNNNNNNN` (es. `CBAM-IT-2025-ABC00000000001`); nel messaggio Hx il `<ReferenceNumber>` segue lo schema `YYYY-XX- CBAM-XX-YYYY-AAANNNNNNNNNNN`.
- **MASE** = autorita' nazionale competente CBAM; **ADM** = controllo doganale.

## Convenzioni specifiche

### Cosa NON fare

- **Non confondere la soglia "de minimis" CBAM (50 t massa netta cumulativa annua, Art. 2bis + Allegato VII) con la franchigia "merci di valore trascurabile" del Reg. 1186/2009** (150 EUR per spedizione): nella fase definitiva la franchigia 1186/2009 non e' piu' rilevante (vedi considerando 2 del Reg. 2025/2083).
- **Non assumere che "elettricita'" o "idrogeno" rientrino nell'esenzione de minimis**: Art. 2bis §4 ▼M1 li esclude esplicitamente.
- **Non confondere "Y134" (deroga territori Allegato III) con "Y237" (merci di origine UE)**: la distinzione e' merceologica/origine, non politica.
- **Non confondere "Y238" (deroga transitoria Art. 17 §7bis) con "Y128" (numero conto del dichiarante autorizzato)**: Y238 e' temporaneo (max 27/9/2026), Y128 e' lo strumento ordinario.
- **Non calcolare emissioni effettive**: l'Art. 8 §1 richiede verifica da verificatore accreditato di Allegato VI. La skill puo' usare valori predefiniti Art. 7 §2 lettera b (Allegato IV punto 4.1) ma non sostituisce la verifica.
- **Non determinare l'importo specifico della sanzione Art. 26 §1**: rinvia testualmente all'importo Art. 16 §3 Direttiva 2003/87/CE (€100 indicizzato all'IPC EU dal 2013); l'importo per l'anno di importazione e' fissato dalla Commissione e va consultato presso l'autorita'.
- **Non emettere giudizi sul carattere "non genuino" di frazionamenti**: e' giudizio di elusione (Art. 27 §2 lettera b) riservato al professionista/autorita' competente.
- **Non assumere che il pagamento della sanzione Art. 26 §1 dispensi dall'obbligo di restituzione**: lo dispensa **solo** la sanzione §2bis (non autorizzato che supera soglia). Art. 26 §3 ▼M1.
- **Non confondere "adeguamento per assegnazione gratuita" (Art. 31) con "detrazione carbon price paese terzo" (Art. 9)**: sono due meccanismi distinti.

### Cosa fare

- **Citare sempre articolo + paragrafo + (se applicabile) lettera** (es. "Art. 22 §2 lettera b ▼M1"). Il marker `▼M1` segnala che la disposizione e' stata introdotta/modificata dall'Omnibus 2025/2083.
- **Sempre indicare la data di applicazione** quando si cita un obbligo (Art. 36 + Reg. 2025/2083 Art. 2): 1/1/2026 per fase definitiva ordinaria, 1/1/2027 per obbligo trimestrale 50 % (Art. 22 §2), 1/2/2027 per vendita certificati piattaforma centrale (Art. 20 §§1, 3-5).
- **Distinguere importatore stabilito UE / rappresentante doganale indiretto / importatore non stabilito UE**: gli obblighi del Capo II (Art. 5) si applicano in modo diverso (vedi considerando 7-8 Reg. 2025/2083).
- **Per ogni report**: includere sezione "Punti che richiedono giudizio del professionista" e disclaimer standard nel paragrafo "Avvertenza" finale.
- **Classificazioni**: usare le etichette tipiche della check-list normativa (es. **APPLICABILE** / **NON APPLICABILE** / **DA VERIFICARE**) con motivazione esplicita.
- **Per il calcolo certificati 50 %**: distinguere chiaramente i due metodi Art. 22 §2 lettere a-b (valori predefiniti senza maggiorazione vs. media certificati anno precedente per stesse merci/paesi).
- **Per la mappa sanzionatoria**: distinguere §1 (mancata restituzione), §2 (importazione non consentita o autorizzazione respinta - moltiplicatore 3x-5x), §2bis (non autorizzato che supera soglia - su tutte le emissioni dell'anno; dispensa da dichiarazione e restituzione).
- **Per Italia**: rinviare a MASE per il procedimento autorizzatorio (autorita' competente nazionale ex Art. 11 Reg. CBAM) e ad ADM per i controlli doganali.

## Validatori

- Nessun validatore di Livello 2 identificato per `v0.1.0-alpha`. Per promozione a 0.2 e' necessaria validazione da responsabile compliance dogane / consulente CBAM di importatore o rappresentante doganale indiretto **diverso dall'autore**.

## Stato attuale

- Versione: vedi `CHANGELOG.md` (`0.1.0-alpha`).
- Validazione: Livello 1 (autore + lettura adversarial delle fonti).
- Task files: 4 (check qualifica/deroghe, plan equilibrio trimestrale, draft dichiarazione annuale, assess rischio sanzionatorio).
- Esempi: 1 conforme + 1 problematico (vedi `examples/`).
