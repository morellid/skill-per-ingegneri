# skill-per-ingegneri

Repository collettivo di skill AI per la pratica dell'ingegneria italiana.

## Cosa contiene

Skill AI in formato dual-agent (compatibili sia con [Anthropic Claude Code](https://claude.com/claude-code) sia con [OpenAI Codex](https://developers.openai.com/codex)), scritte in italiano, basate esclusivamente su fonti normative ufficiali (D.Lgs., decreti attuativi, linee guida pubbliche). Ogni skill e' pensata per essere usata da ingegneri iscritti all'Albo come supporto - non sostituto - nella redazione e verifica di documenti tecnici e adempimenti.

Ogni skill e' anche utilizzabile da agent che leggono lo standard aperto [`AGENTS.md`](AGENTS.md) (Codex, Cursor, Windsurf, GitHub Copilot, Devin, Amp, Antigravity, ...).

Contiene anche:
- **Metodologia replicabile** per generare nuove skill (`methodology/`)
- **Template e script** per scaffolding e validazione (`templates/`, `scripts/`)
- **Riferimenti bibliografici** strutturati con hash delle fonti (`sources.yaml` per ogni skill)

## Skill disponibili

| Skill | Ambito | Riferimenti normativi |
|---|---|---|
| [`pos-allegato-xv-checker`](skills/pos-allegato-xv-checker/) | Guida la compilazione assistita e verifica completezza e coerenza di un Piano Operativo di Sicurezza (POS) di cantiere | D.Lgs. 81/2008 art. 96-97, Allegato XV + DI 9/9/2014 modelli semplificati |
| [`dvr-generico`](skills/dvr-generico/) | Stesura, verifica e aggiornamento del Documento di Valutazione dei Rischi (DVR) cross-settoriale | D.Lgs. 81/2008 art. 17, 28, 29 |
| [`gdpr-registro-dpia`](skills/gdpr-registro-dpia/) | Registro delle attivita' di trattamento e Valutazione d'Impatto (DPIA), con modulo tracking pixel e-mail | GDPR art. 30, 35, 36 + provv. Garante + Linee guida tracking pixel (provv. 284/2026) |
| [`nis2-self-assessment`](skills/nis2-self-assessment/) | Self-assessment NIS2 (perimetro, gap analysis misure ACN, elenco fornitori rilevanti, categorizzazione attivita' e servizi, notifica incidenti, governance) | D.Lgs. 138/2024 + Det. ACN 379907/2025 + Det. ACN 127437/2026 + Det. ACN 127434/2026 + Det. ACN 155238/2026 |
| [`ai-act-compliance`](skills/ai-act-compliance/) | Classificazione sistemi AI + obblighi provider/deployer/GPAI/trasparenza | Reg. UE 2024/1689 (AI Act) |
| [`accessibilita-siti-app-l4-2004`](skills/accessibilita-siti-app-l4-2004/) | Supporto documentale agli obblighi di accessibilita' dei siti web e delle applicazioni mobili (Legge Stanca, L. 4/2004, agg. D.Lgs. 106/2018 di recepimento dir. UE 2016/2102): chi e' obbligato (soggetti pubblici e assimilati art. 3 c. 1; grandi privati con fatturato medio > 500 mln art. 3 c. 1-bis), esclusioni (art. 3 c. 2), obblighi negli appalti IT e nullita' dei contratti per siti/app non accessibili (art. 4), requisiti tecnici delle linee guida AgID che recepiscono EN 301 549 e WCAG (art. 11), vigilanza/monitoraggio AgID (art. 7), responsabilita' dirigenziale (pubblico) e sanzione AgID fino al 5% del fatturato (grandi privati) (art. 9). Non esegue l'audit tecnico WCAG ne' redige la dichiarazione di accessibilita' | L. 4/2004 (Legge Stanca) artt. 2, 3, 4, 7, 9, 11 (testo vigente Normattiva, dir. UE 2016/2102) |
| [`spettro-risposta-ntc`](skills/spettro-risposta-ntc/) | Calcolo code-driven dello spettro di risposta elastico orizzontale (TR, ag/F0/Tc*, S, eta, TB/TC/TD, Se(T)) per SLO/SLD/SLV/SLC | NTC 2018 par. 3.2 + Circ. 7/2019 |
| [`periodo-proprio-t1-ntc`](skills/periodo-proprio-t1-ntc/) | Stima code-driven del periodo proprio T1: formula [7.3.6] NTC (T1 = 2*sqrt(d)) e formula [C7.3.2] Circolare (T1 = C1*H^(3/4), C1 = 0,085/0,075/0,050), check limiti della stima (H <= 40 m, massa uniforme), condizione T1 <= 2,5*TC e lambda per le forze [7.3.7] | NTC 2018 par. 7.3.3.2 + Circ. 7/2019 par. C7.3.3.2 |
| [`combinazioni-carico-ntc`](skills/combinazioni-carico-ntc/) | Generazione/verifica code-driven delle combinazioni delle azioni SLU/SLE/sismiche/eccezionali per edifici civili e industriali correnti | NTC 2018 par. 2.5.3 + Tab. 2.5.I + Tab. 2.6.I |
| [`carichi-atmosferici-ntc`](skills/carichi-atmosferici-ntc/) | Calcolo code-driven della pressione del vento p (par. 3.3) e del carico neve sulla copertura q_s (par. 3.4) per edifici civili e industriali correnti, dato sito (parametri zonali, altitudine), categoria di esposizione I-V, geometria (z, c_p, alpha falda, classe esposizione neve); output v_b/c_r/q_r/c_e/p e q_sk/mu_1/c_E/q_s con citazione paragrafi NTC | NTC 2018 par. 3.3 + par. 3.4 + Circ. 7/2019 par. C3.3-C3.4 |
| [`pfte-allegato-i7-checker`](skills/pfte-allegato-i7-checker/) | Checklist e verifica completezza degli elaborati di un PFTE / progetto esecutivo di lavori pubblici, integrato dal correttivo 2024 | D.Lgs. 36/2023 art. 41 + Allegato I.7 + D.Lgs. 209/2024 |
| [`modulistica-edilizia-unificata`](skills/modulistica-edilizia-unificata/) | Determina il modulo edilizio unificato (Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / PdC / Sanatoria art. 36 / 36-bis) per un intervento e l'elenco degli allegati richiesti, integrato con le modifiche del Salva Casa | DPR 380/2001 + D.Lgs. 222/2016 Tabella A + DL 69/2024 conv. L. 105/2024 + Modulistica unificata 27/3/2025 |
| [`transizione-5-0-asseverazione`](skills/transizione-5-0-asseverazione/) | Asseverazione tecnica ex ante / ex post per il credito d'imposta Piano Transizione 5.0 (calcolo riduzione consumi >=3% struttura o >=5% processo, conversione tep, modelli MIMIT), inclusa la fase post-chiusura con credito 89,77% per le pratiche tecnicamente ammissibili | DL 19/2024 art. 38 + DM MIMIT-MEF 24/7/2024 + Circolare MIMIT 25877/2024 + DL 38/2026 art. 8 (conv. L. 88/2026) |
| [`diagnosi-energetica-dlgs102`](skills/diagnosi-energetica-dlgs102/) | Supporto documentale all'obbligo di diagnosi energetica delle grandi imprese e delle imprese energivore (art. 8 D.Lgs. 102/2014): determina se l'impresa e' obbligata (grande impresa: > 250 occupati e fatturato > 50 mln, oppure bilancio > 43 mln; energivore a prescindere dalla dimensione), le esenzioni (< 50 tep, ISO 50001 con diagnosi conforme), la periodicita' quadriennale, i soggetti esecutori (ESCo/EGE certificati UNI CEI 11352/11339), la comunicazione ENEA, i controlli e le sanzioni (artt. 2, 8, 16). Non esegue la diagnosi ne' calcola consumi | D.Lgs. 102/2014 artt. 2, 8, 16 (testo vigente Normattiva, attuazione dir. 2012/27/UE) |
| [`dnsh-pnrr-checker`](skills/dnsh-pnrr-checker/) | Verifica documentale DNSH per interventi PNRR e, solo se la misura lo richiama espressamente, per interventi PNC: mappatura misura, schede tecniche RGS, checklist ex ante/ex post, piano evidenze e report per gara/SAL/collaudo/ReGiS | Reg. UE 2020/852 art. 17 + Reg. UE 2021/241 art. 5 e 18 + Circolare RGS 22/2024 + Guida operativa DNSH RGS 2024 + DL 77/2021 art. 14 |
| [`piano-lavoro-amianto`](skills/piano-lavoro-amianto/) | Precheck, redazione guidata e verifica del piano di lavoro per demolizione o rimozione di amianto, nel testo vigente dell'art. 256 D.Lgs. 81/2008 aggiornato dal D.Lgs. 213/2025 | D.Lgs. 81/2008 art. 251, 256, 258, 259 + D.Lgs. 213/2025 + DM 6/9/1994 |
| [`atex-luoghi-lavoro-dlgs81`](skills/atex-luoghi-lavoro-dlgs81/) | Supporto documentale alla protezione dei lavoratori dai rischi da atmosfere esplosive (ATEX luoghi di lavoro, Titolo XI D.Lgs. 81/2008, dir. 1999/92/CE): ambito ed esclusioni (art. 287), definizione di atmosfera esplosiva (art. 288), obblighi del datore di lavoro (art. 289), valutazione del rischio di esplosione (art. 290), classificazione delle aree in zone (art. 293, allegato XLIX) con prescrizioni minime (allegato L), documento sulla protezione contro le esplosioni - DPCE (art. 294), verifiche installazioni elettriche nelle zone (art. 296, DPR 462/2001), sanzioni (art. 297). Non classifica le zone, non redige il DPCE, non copre la marcatura ATEX degli apparecchi (2014/34/UE) | D.Lgs. 81/2008 Titolo XI artt. 287-290, 293, 294, 296, 297 (testo vigente Normattiva, dir. 1999/92/CE) |
| [`ambienti-confinati-dpr177`](skills/ambienti-confinati-dpr177/) | Supporto documentale alla qualificazione delle imprese/lavoratori autonomi e alle procedure di sicurezza per i lavori in ambienti sospetti di inquinamento o confinati (DPR 177/2011): requisiti dell'art. 2 (>= 30% forza lavoro con esperienza triennale, preposti esperti, formazione con verifica, DPI e addestramento, DURC, CCNL, divieto di subappalto non autorizzato) e procedure dell'art. 3 in appalto (informazione preventiva >= 1 giorno, rappresentante del committente, procedura con fase di soccorso e coordinamento SSN/VVF) | DPR 177/2011 artt. 1-4 (testo vigente Normattiva) + D.Lgs. 81/2008 artt. 26, 66, 121, All. IV p.3 |
| [`catasto-pregeo-docfa-atti-telematici`](skills/catasto-pregeo-docfa-atti-telematici/) | Assistente alla redazione e al check pre-trasmissione degli atti telematici di aggiornamento del Catasto Terreni (Pregeo 10) e del Catasto Fabbricati (Docfa 4): scelta tipologia atto Pregeo (TM/FR/FM/SC/TP), causale e categoria Docfa, EP/ES/ET/Quadro D, deposito telematico frazionamenti dal 1/7/2025, diagnosi rifiuti telematici via Sister | DPR 380/2001 art. 30 + DM 28/1998 + Circ. AdE 3/2009 + Vademecum Docfa v1.0 (7/2022) + Risoluzione AdE 40/E del 9/6/2025 |
| [`pratiche-edilizie-lr65-2014-toscana`](skills/pratiche-edilizie-lr65-2014-toscana/) | Determina il titolo abilitativo edilizio (Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / PdC) per interventi in Toscana e genera la checklist documenti richiesti, con specificita' regionali (sismica DGRT 421/2014, DPGR 1/R/2022 Genio Civile, vincolo paesaggistico, Piano Operativo) | LR Toscana 65/2014 + DPR 380/2001 + DPGR 1/R/2022 + DPR 31/2017 (paesaggio) |
| [`fattibilita-idraulica-toscana-lr41`](skills/fattibilita-idraulica-toscana-lr41/) | Supporto documentale alla fattibilita' delle trasformazioni nelle aree a pericolosita' per alluvioni in Toscana (L.R. 41/2018): inquadra il sito (aree a pericolosita' per alluvioni frequenti/poco frequenti) e la magnitudo idraulica (moderata/severa/molto severa in funzione di battente e velocita', art. 2), le opere per raggiungere il rischio medio R2 (opere idrauliche, sopraelevazione, difesa locale, art. 8), le limitazioni nelle aree a pericolosita' frequente (ospedali, strutture strategiche, impianti AIA, art. 10) e le condizioni per la nuova costruzione (art. 11) e per il patrimonio esistente (art. 12). Non legge le mappe di pericolosita' ne' dimensiona le opere | LR Toscana 41/2018 artt. 2, 7, 8, 10, 11, 12 (testo vigente Raccolta Normativa; attuazione d.lgs. 49/2010) |
| [`cer-cacer-configurazione-gse`](skills/cer-cacer-configurazione-gse/) | Configurazione di CER (art. 31), GAC (art. 30 c. 2) o AID (art. 30 c. 1 lett. a) n. 2) con verifica perimetro cabina primaria, redazione guidata dello statuto, simulazione semplificata di energia condivisa, TIP, tariffa di restituzione e contributo PNRR per Comuni < 50.000 ab. (regime vigente al 2026-05-07: DM 414/2023 + DM 127/2025 + DL 19/2026 art. 27), e checklist documentale per la qualifica al portale GSE | D.Lgs. 199/2021 artt. 30-31-32 + DM MASE 7/12/2023 n. 414 + DM MASE 16/5/2025 n. 127 + DL 19/2/2026 n. 19 art. 27 + Delibera ARERA 727/2022/R/eel (TIAD) + Regole Operative CACER del GSE |
| [`sismabonus-classificazione-rischio-pam`](skills/sismabonus-classificazione-rischio-pam/) | Calcolo code-driven della classe di rischio sismico DM 58/2017 (sismabonus, metodo convenzionale): PAM come area trapezoidale della Curva di Individuazione su SLID/SLO/SLD/SLV/SLC + coda SLR, IS-V = PGA_C(SLV)/PGA_D(SLV), classe finale = peggiore tra classe PAM (8 classi A+..G) e classe IS-V (7 classi A+..F), salto classi tra stato di fatto e stato di progetto | DM 58/2017 + DM 65/2017 + DM 24/2020 + DM 329/2020 (Allegato A) + NTC 2018 cap. 3.2 e cap. 8 + Circ. 7/2019 |
| [`bandi-tipo-anac-checker`](skills/bandi-tipo-anac-checker/) | Verifica la conformita' di un disciplinare di gara agli schemi ANAC (bandi-tipo) obbligatori per le stazioni appaltanti; identifica deroghe non giustificate, clausole mancanti, riferimenti obsoleti (D.Lgs. 50/2016) e anomalie a rischio TAR prima della pubblicazione | D.Lgs. 36/2023 + Bandi-tipo ANAC (n. 1/2023 agg. Delibera 148/2026, n. 2/2026 SIA Delibera 153/2026) |
| [`oepv-valutatore-offerte-tecniche`](skills/oepv-valutatore-offerte-tecniche/) | Costruzione della matrice criteri/sottocriteri OEPV, valutazione delle offerte tecniche con metodo aggregativo-compensatore, verifica di conformita' all'art. 108 di una matrice gia' redatta, con schema dedicato per i SIA sopra soglia (Bando tipo ANAC n. 2/2026) | D.Lgs. 36/2023 art. 108 + D.Lgs. 209/2024 (correttivo) + ANAC Bando tipo n. 2/2026 (Delibera n. 153/2026) |
| [`specifiche-tecniche-ict-appalti-dlgs36`](skills/specifiche-tecniche-ict-appalti-dlgs36/) | Supporto documentale alle specifiche tecniche di una procedura d'appalto ICT della PA (modalita' di formulazione, clausola "o equivalente", divieto di marchi, etichettature) e alla fase preliminare di analisi comparativa delle soluzioni software e riuso/titolarita' del codice; non redige il capitolato, non sceglie la soluzione, non valuta le offerte | D.Lgs. 36/2023 artt. 79-80 e allegato II.5 + D.Lgs. 82/2005 (CAD) artt. 68-69 |
| [`cra-classificazione-pde`](skills/cra-classificazione-pde/) | Classificazione di un prodotto con elementi digitali (PDE) ai sensi del CRA (default / importante Classe I / Classe II / critico) e selezione del modulo di valutazione della conformita' (A, B+C, H, certificazione europea) + struttura documentazione tecnica Allegato VII | Reg. UE 2024/2847 (Cyber Resilience Act) |
| [`dora-gap-assessment`](skills/dora-gap-assessment/) | Gap assessment di un'entita' finanziaria (banca, IMEL, IP, SIM, assicurazione, MiCA CASP, ecc.) rispetto ai 5 pillar DORA, applicabile dal 17/1/2025 | Reg. UE 2022/2554 (DORA) artt. 5-30, 45 |
| [`ped-classificazione-conformita`](skills/ped-classificazione-conformita/) | Classificazione di un'attrezzatura a pressione (recipiente, tubazione, accessorio di sicurezza o a pressione, insieme) nelle categorie I/II/III/IV e selezione del modulo di valutazione della conformita' applicabile, marcatura e dichiarazione richieste | D.Lgs. 26/2016 (recepimento Direttiva PED 2014/68/UE) |
| [`dm37-2008-dichiarazione-conformita`](skills/dm37-2008-dichiarazione-conformita/) | Compilazione e verifica della Dichiarazione di Conformita' (DdC) degli impianti tecnologici (7 categorie a-g modello Allegato I), determinazione degli allegati obbligatori e dell'obbligo di progetto da professionista ex Art. 5 | DM 22/1/2008 n. 37 |
| [`relazione-cam-dm-24-11-2025`](skills/relazione-cam-dm-24-11-2025/) | Redazione e verifica della Relazione CAM di progetto ex criterio 2.1.1 DM MASE 24/11/2025 (nuovi CAM edilizia in vigore dal 2/2/2026, abrogano il DM 256/2022): scelta del regime (nuovo DM vs transitorio), tabella di applicabilita' dei criteri e Schede Tipo secondo il modello MASE, check di relazioni esistenti. Sostituisce `relazione-cam-dm256-2022` | DM MASE 24/11/2025 (GU n. 281/2025) + Circolare MASE 10/4/2026 + Modello MASE 2/2/2026 + D.Lgs. 36/2023 art. 57 |
| [`rsia-audit-stradale-dlgs35`](skills/rsia-audit-stradale-dlgs35/) | Supporto alle quattro procedure di gestione della sicurezza delle infrastrutture stradali: VISS (impatto sui progetti), RSA (controlli sulle fasi progettuali), NSA (valutazione a livello di rete), ispezioni periodiche/mirate sulle strade in esercizio | D.Lgs. 35/2011 modificato dal D.Lgs. 213/2021 (recepimento Dir. UE 2019/1936) |
| [`via-screening-sia-dlgs152`](skills/via-screening-sia-dlgs152/) | Supporto documentale alla Valutazione di Impatto Ambientale (VIA): verifica di assoggettabilita' (screening, art. 19) con procedura e termini perentori, checklist dello Studio Preliminare Ambientale (All. IV-bis) e dei criteri (All. V), adeguamento regionale delle soglie (DM 30/03/2015); struttura e checklist di completezza dello Studio di Impatto Ambientale - SIA (12 punti Allegato VII). Non decide l'assoggettabilita' ne' sostituisce l'autorita' competente | D.Lgs. 152/2006 Parte Seconda artt. 19, 22 + Allegati IV-bis, V, VII (testo vigente) + DM 30/03/2015 |
| [`bonifica-siti-contaminati-dlgs152`](skills/bonifica-siti-contaminati-dlgs152/) | Supporto documentale alla procedura di bonifica dei siti contaminati (D.Lgs. 152/2006 Parte quarta Titolo V): definizioni CSC/CSR, sito potenzialmente contaminato/contaminato/non contaminato, MISE/MISO/messa in sicurezza permanente (art. 240); procedura del responsabile (art. 242: prevenzione entro 24 ore, autocertificazione entro 48 ore se sotto CSC, piano di caratterizzazione entro 30 giorni, analisi di rischio entro 6 mesi, conferenza di servizi); ordinanza della PA (art. 244); aree di ridotte dimensioni (art. 249); sanzioni penali (art. 257). Non legge i valori CSC, non esegue l'analisi di rischio ne' redige il piano di caratterizzazione | D.Lgs. 152/2006 Parte quarta Titolo V artt. 240, 242, 244, 249, 257 (testo vigente Normattiva) |
| [`pums-validator-dm397`](skills/pums-validator-dm397/) | Verifica della conformita' formale e di completezza di un Piano Urbano di Mobilita' Sostenibile (PUMS) per comuni > 100.000 ab., citta' metropolitane o associazioni di comuni che superano la soglia | DM 397/2017 + DM 396/2019 + DM 29/2021 + DM 444/2021 + Vademecum MIMS 2022 |
| [`valutazione-impatto-clima-acustico-l-447`](skills/valutazione-impatto-clima-acustico-l-447/) | Documentazione previsionale di impatto acustico (art. 8 c. 2 e c. 4) e valutazione previsionale di clima acustico (art. 8 c. 3) da allegare a SCIA/PdC/autorizzazione: mapping applicabilita', check contenuti minimi della relazione, riferimenti puntuali ai valori limite | L. 447/1995 art. 8 + DPCM 14/11/1997 + DM 16/3/1998 |
| [`mappatura-acustica-strategica-dlgs194`](skills/mappatura-acustica-strategica-dlgs194/) | Supporto documentale agli obblighi di mappatura acustica strategica e piani d'azione contro il rumore ambientale (D.Lgs. 194/2005, dir. 2002/49/CE): soglie di applicabilita' (agglomerati > 100.000 ab., aeroporti > 50.000 movimenti/anno, assi ferroviari > 30.000 treni/anno, assi stradali > 3.000.000 veicoli/anno), soggetti obbligati (autorita' regionale/gestori), deliverable art. 3 (mappe) e art. 4 (piani), scadenze quinquennali, Lden/Lnight, informazione del pubblico, sanzioni | D.Lgs. 194/2005 artt. 1-11 (testo vigente Normattiva) |
| [`valutazione-cem-srb-art-87-cce`](skills/valutazione-cem-srb-art-87-cce/) | Pratica di autorizzazione SRB (stazioni radio base, ripetitori, ponti radio) ex art. 87 CCE: check completezza istanza/SCIA, mapping iter (Ente locale + parere ARPA), checklist per la relazione predittiva CEM secondo CEI 211-7 | D.Lgs. 259/2003 art. 87 + DPCM 8/7/2003 + L. 36/2001 art. 14 + CEI 211-7 |
| [`cbam-declarant-trimestrale`](skills/cbam-declarant-trimestrale/) | Adempimenti del dichiarante CBAM autorizzato nella fase definitiva (dal 1/1/2026): verifica qualifica e applicabilita' deroghe (soglia 50 t, art. 17 §7bis con TARIC Y238 fino al 27/9/2026), pianificazione obbligo trimestrale 50% sui certificati CBAM (Art. 22 §2 dal 2027), dichiarazione annuale Art. 6 (prima volta 30/9/2027 per anno 2026), esposizione sanzionatoria Art. 26 | Reg. UE 2023/956 (CBAM) modificato da Reg. UE 2025/2083 |
| [`cedimenti-edometrici-ntc`](skills/cedimenti-edometrici-ntc/) | Calcolo code-driven del cedimento di consolidazione primaria per strati (eq. 7-2/7-4/7-6 FHWA NHI-06-088, codice internazionale ex cap. 12 NTC 2018: OCR, caso NC/OC/UC, S in mm, casi non coperti rifiutati) + verifica documentale della verifica SLE cedimenti (Ed <= Cd) | NTC 2018 par. 6.2.4.3 + cap. 12 + Circolare 7/2019 + FHWA NHI-06-088 (2006) par. 7.5.2 |
| [`capacita-portante-fondazione-ntc`](skills/capacita-portante-fondazione-ntc/) | Calcolo code-driven della capacita' portante di fondazioni superficiali (eq. 8-1..8-9 FHWA NHI-06-089, codice internazionale ex cap. 12 NTC 2018: fattori Nc/Nq/Ngamma, forma, falda, dimensioni efficaci) e verifica GEO a carico limite NTC 6.4.2.1 in Approccio 2 (q_Rd = qult/2,3, confronto Ed <= Rd); casi fuori ambito rifiutati | NTC 2018 par. 6.4.2.1 + cap. 12 + Circolare 7/2019 par. C6.4.2.1 + FHWA NHI-06-089 (2006) par. 8.4 |
| [`costruzioni-esistenti-ntc-cap8`](skills/costruzioni-esistenti-ntc-cap8/) | Consultazione del cap. 8 NTC 2018 (costruzioni esistenti): classificazione degli interventi (riparazione/locale, miglioramento, adeguamento - par. 8.4), casi di adeguamento obbligatorio a-e e soglie del rapporto zeta_E (a,b,d -> 1,0; c,e -> 0,80), soglie zeta_E per il miglioramento per classe d'uso, livelli di conoscenza LC1/LC2/LC3 e fattori di confidenza FC 1,35/1,2/1,0 (Tab. C8.5.IV); non calcola, non sostituisce il progettista | NTC 2018 cap. 8 (parr. 8.3, 8.4, 8.5.4) + Circolare 7/2019 cap. C8 (C8.3, C8.4, C8.5.4, Tab. C8.5.IV) |
| [`trasmittanza-termica-opache-dm2015`](skills/trasmittanza-termica-opache-dm2015/) | Calcolo code-driven della trasmittanza U di strutture opache stratificate (U = 1/R_tot) e verifica dei limiti per zona climatica del DM 26/06/2015 (Appendice B riqualificazione / Appendice A edificio di riferimento), con incremento +30% per isolamento interno; lambda e R_si/R_se sono input utente (norme UNI non riprodotte), verifica 1D preliminare (i limiti includono i ponti termici) | DM 26/06/2015 (MiSE, requisiti minimi) Allegato 1 par. 5.2 + Appendici A e B |
| [`predimensionamento-flessione-ca-ntc`](skills/predimensionamento-flessione-ca-ntc/) | Calcolo code-driven di M_Rd di sezione rettangolare in c.a. singolarmente armata in flessione semplice SLU (stress-block rettangolare equivalente eta=1, lambda=0.8): f_cd, f_yd, eps_yd, profondita' asse neutro x, x/d, eps_s, braccio z, M_Rd in kNm, verifica duttilita' x/d <= 0.45. Solo fck <= 50 MPa (Classe 1) e sezioni singolarmente armate | NTC 2018 par. 4.1.2.1 e 4.1.2.3.4.2 + Circolare 7/2019 par. C4.1.2 |
| [`fascicolo-tecnico-macchine-reg-1230`](skills/fascicolo-tecnico-macchine-reg-1230/) | Redazione e verifica del fascicolo tecnico di una macchina, prodotto correlato o quasi-macchina ai sensi del nuovo Regolamento Macchine UE: qualificazione del prodotto, scelta procedura di valutazione conformita' (art. 25, Allegato I, moduli A/B/C/G/H), checklist contenuti Allegato IV parti A e B, struttura dichiarazioni UE Allegato V parti A e B (sostituisce Dir. 2006/42/CE dal 14/1/2027) | Reg. UE 2023/1230 (Regolamento Macchine) |
| [`aua-dpr59-dossier`](skills/aua-dpr59-dossier/) | Supporto alla preparazione e all'autoverifica del dossier per l'Autorizzazione Unica Ambientale (AUA) per PMI e impianti non-AIA: verifica applicabilita' (PMI / non-AIA / non-VIA assorbente), mapping dei 9 titoli incorporabili ex art. 3 co. 1 (lett. a-g, g-bis, g-ter), pianificazione termini procedurali (30/90/120/150 giorni + conferenza di servizi), pianificazione rinnovo a 6 mesi dalla scadenza (durata 15 anni), triage modifica sostanziale / non sostanziale ex art. 6 | D.P.R. 13/3/2013 n. 59 + D.Lgs. 152/2006 (richiamato) + L. 447/1995 art. 8 + D.Lgs. 101/2020 artt. 24-26 (lett. g-bis/g-ter dal D.Lgs. 203/2022) + L. 241/1990 + D.P.R. 160/2010 |
| [`scarichi-emissioni-dlgs152`](skills/scarichi-emissioni-dlgs152/) | Supporto documentale alle autorizzazioni ambientali singole (residuali rispetto ad AUA e AIA) per lo scarico di acque reflue industriali (art. 124: autorizzazione preventiva, provincia/ente d'ambito, 90 giorni, durata 4 anni, rinnovo un anno prima) e per le emissioni in atmosfera degli stabilimenti (art. 269: domanda con progetto e relazione tecnica, durata 15 anni), con nuova autorizzazione/comunicazione per trasferimento/ampliamento/modifica e sanzioni penali/amministrative (artt. 137, 279). Non legge i valori limite degli allegati ne' redige le domande | D.Lgs. 152/2006 artt. 124, 137 (Parte terza) + 269, 279 (Parte quinta) (testo vigente Normattiva) |
| [`denuncia-opere-strutturali-l1086`](skills/denuncia-opere-strutturali-l1086/) | Diagnosi degli adempimenti procedurali strutturali e sismici del DPR 380/2001 per interventi edilizi in Italia: denuncia opere in c.a./c.a.p./metalliche (art. 65), collaudo statico (art. 67), preavviso e autorizzazione preventiva in zona sismica (artt. 93, 94, 94-bis), classificazione interventi rilevanti / minore rilevanza / privi di rilevanza ex art. 94-bis, coordinamento art. 65 e art. 93 c. 5, esclusioni commi 8-bis e 8-ter | DPR 380/2001 artt. 65, 67, 83, 93, 94, 94-bis (testo multivigente Normattiva) |
| [`verifiche-messa-a-terra-dpr462`](skills/verifiche-messa-a-terra-dpr462/) | Supporto documentale agli adempimenti del DPR 462/2001 per impianti di messa a terra, dispositivi contro le scariche atmosferiche e impianti in luoghi con pericolo di esplosione nei luoghi di lavoro: periodicita' della verifica periodica (5 anni ordinari; 2 anni per cantieri, locali medici, ambienti a maggior rischio incendio, luoghi con pericolo di esplosione), soggetti abilitati (ASL/ARPA o organismi), messa in esercizio e denuncia entro 30 gg (dichiarazione di conformita' = omologazione), prima verifica a campione, banca dati INAIL (art. 7-bis) | DPR 462/2001 artt. 1-8 (testo vigente Normattiva) |
| [`verifiche-periodiche-ascensori-dpr162`](skills/verifiche-periodiche-ascensori-dpr162/) | Supporto documentale all'iter di esercizio, verifiche periodiche/straordinarie e manutenzione di ascensori, montacarichi e assimilati (DPR 162/1999, artt. 12-16): messa in esercizio (comunicazione al comune entro 60 gg, matricola entro 30 gg), verifica periodica ogni 2 anni e soggetti abilitati (ASL/ARPA, ITL, MIT, organismi notificati, organismi di ispezione di tipo A), verifiche straordinarie, manutenzione (controlli almeno semestrali), libretto e targa | DPR 162/1999 artt. 12-16 (testo vigente Normattiva) |
| [`trasporto-rifiuti-fir-dlgs152`](skills/trasporto-rifiuti-fir-dlgs152/) | Supporto documentale agli obblighi del trasporto dei rifiuti (D.Lgs. 152/2006): formulario di identificazione dei rifiuti - FIR (art. 193: obbligo, quattro copie con firme di produttore/detentore, trasportatore e destinatario, modello/RENTRI art. 188-bis, imballaggio ed etichettatura dei pericolosi, esclusioni), iscrizione all'Albo nazionale gestori ambientali (art. 212: requisito per raccolta/trasporto, semplificazione per i produttori iniziali che trasportano i propri rifiuti non pericolosi o pericolosi fino a 30 kg/30 litri al giorno), sanzioni (art. 258: 1.600-10.000 euro senza formulario, reclusione 1-3 anni per pericolosi senza formulario). Non classifica il rifiuto ne' redige il FIR | D.Lgs. 152/2006 artt. 193, 212, 258 (testo vigente Normattiva) |
| [`mog-231-reati-ambientali`](skills/mog-231-reati-ambientali/) | Supporto documentale alla parte speciale ambientale del Modello di Organizzazione, Gestione e Controllo (MOG) ex D.Lgs 231/2001: mappa i reati presupposto ambientali dell'art. 25-undecies (ecoreati c.p. 452-bis ss.; D.Lgs 152/2006 su scarichi/rifiuti/bonifica/emissioni; L. 150/1992 CITES; L. 549/1993 ozono; D.Lgs 202/2007 navi) con le sanzioni a quote e interdittive, e struttura i controlli della parte speciale (attivita' a rischio, protocolli, flussi verso l'OdV, sistema disciplinare) ai sensi degli artt. 6-7. Non redige il Modello ne' effettua la valutazione legale | D.Lgs. 231/2001 art. 25-undecies + artt. 6-7 e 9 (testo vigente Normattiva) |
| [`consulente-adr-dlgs40`](skills/consulente-adr-dlgs40/) | Supporto documentale agli obblighi relativi al consulente per la sicurezza dei trasporti di merci pericolose (DGSA, D.Lgs. 40/2000): se un'impresa deve nominarlo ed esenzioni (ambito trasporto/carico-scarico art. 2; quantitativi limitati o trasporti occasionali art. 3 c. 6), obblighi del capo dell'impresa (nomina, comunicazione alla motorizzazione civile, conservazione della relazione 5 anni, art. 3), obblighi del consulente (relazione annuale e a ogni evento modificativo, relazione d'incidente al Ministero dei trasporti, art. 4), qualificazione con certificato di formazione professionale (art. 5), sanzioni e vigilanza (art. 6). Non redige la relazione ne' tratta le regole tecniche ADR | D.Lgs. 40/2000 artt. 2, 3, 4, 5, 6 (testo vigente Normattiva; quadro ADR 1.8.3) |
| [`trasporti-eccezionali-cds-art10`](skills/trasporti-eccezionali-cds-art10/) | Supporto documentale al regime dei veicoli e dei trasporti eccezionali (art. 10 del Codice della Strada, D.Lgs. 285/1992): inquadramento dell'eccezionalita' (eccedenza dei limiti di sagoma art. 61 o massa art. 62; cose indivisibili; generi tipizzati con massa fino a 38/48/86/108 t), obbligo di autorizzazione alla circolazione ed ente competente (ente proprietario/concessionario, regioni), tipi di autorizzazione (singola/multipla/periodica), presupposti e prescrizioni (percorsi, periodi, scorta), sanzioni (da 794 a 3.206 euro senza autorizzazione, sospensione patente). Non calcola sagoma/massa ne' redige la domanda | D.Lgs. 285/1992 (Codice della Strada) art. 10 (testo vigente Normattiva) |
| [`notifica-seveso-dlgs105`](skills/notifica-seveso-dlgs105/) | Supporto documentale agli obblighi degli stabilimenti a rischio di incidente rilevante (Seveso III, D.Lgs. 105/2015): assoggettabilita' ed esclusioni (art. 2), classificazione come stabilimento di soglia inferiore o superiore (colonne 2/3 allegato 1, regola della sommatoria), notifica al CTR/Regione/ISPRA/Prefettura/Comune/VVF (art. 13, modulo allegato 5, termini 180/60 giorni o 1 anno), politica di prevenzione e SGS per tutti (art. 14), rapporto di sicurezza per la sola soglia superiore (art. 15), sanzioni penali e diffida/sospensione/chiusura (art. 28). Non legge le soglie sostanza-specifiche ne' redige il rapporto di sicurezza | D.Lgs. 105/2015 artt. 2, 3, 13, 14, 15, 28 (testo vigente Normattiva, attuazione dir. 2012/18/UE Seveso III) |
| [`relazione-geologica-geotecnica-ntc`](skills/relazione-geologica-geotecnica-ntc/) | Controllo di completezza della relazione geologica e della relazione geotecnica richieste dalle NTC 2018, controllo di coerenza tra le due relazioni (e con la relazione di calcolo) e bozza di indice commentato della relazione geotecnica - supporto documentale che non sostituisce il professionista firmatario | NTC 2018 (DM 17/01/2018) parr. 6.1-6.2.6 + Circolare C.S.LL.PP. 7/2019 parr. C6.2, C9.1 lett. g, C10.1 |

Ogni skill ha un proprio `README.md` con dettaglio target, sotto-attivita' e limiti noti.

## Struttura

```
skill-per-ingegneri/
├── AGENTS.md                    # guida cross-agent (Codex, Cursor, Copilot, ...)
├── skills/                      # le skill pubblicate (elenco completo: tabella sopra)
│   ├── pos-allegato-xv-checker/
│   │   ├── SKILL.md             # punto d'ingresso + routing (license: MIT in frontmatter)
│   │   ├── agents/
│   │   │   └── openai.yaml      # UI metadata per Codex
│   │   ├── tasks/               # istruzioni dettagliate per sotto-attivita'
│   │   ├── references/          # metadata fonti + estratti normativi
│   │   ├── examples/            # casi d'uso validi e problematici
│   │   └── CHANGELOG.md
│   └── <altre-skill>/           # stessa struttura per ciascuna skill
├── methodology/                 # come si genera e mantiene una skill
├── templates/                   # scaffold dual-agent per nuove skill
└── scripts/                     # utility CLI (new-skill, validate, fetch-sources)
```

## Come installare e usare le skill

Ogni skill in `skills/<nome>/` e' un pacchetto autonomo. Si installa nella directory skills del tuo agent.

| Agent | Path target |
|---|---|
| Anthropic Claude Code | `~/.claude/skills/<nome-skill>/` |
| OpenAI Codex | `~/.agents/skills/<nome-skill>/` |

### Installazione di una singola skill

```bash
# Claude Code
cp -r skills/pos-allegato-xv-checker ~/.claude/skills/

# Codex
cp -r skills/pos-allegato-xv-checker ~/.agents/skills/
```

### Installazione di tutto il catalogo via symlink

```bash
# Claude Code
mkdir -p ~/.claude/skills
for s in skills/*/; do
  ln -sfn "$(pwd)/$s" "$HOME/.claude/skills/$(basename "$s")"
done

# Codex
mkdir -p ~/.agents/skills
for s in skills/*/; do
  ln -sfn "$(pwd)/$s" "$HOME/.agents/skills/$(basename "$s")"
done
```

I symlink permettono di aggiornare tutte le skill installate con `git pull` nel repo.

### Installazione via Claude Code plugin marketplace

Le skill sono distribuite anche come marketplace nativo Claude Code: un plugin per ogni area del catalogo. Dentro Claude Code:

```
/plugin marketplace add morellid/skill-per-ingegneri
/plugin install <area-id>@skill-per-ingegneri
```

Dove `<area-id>` e' uno tra: `sicurezza-lavoro-cantieri`, `strutture-geotecnica`, `edilizia-urbanistica-catasto`, `appalti-opere-pubbliche`, `energia-incentivi`, `ambiente-territorio-mobilita`, `impianti-macchine-prodotti`, `software-dati-cybersecurity`. Le skill installate sono namespacciate (es. `/strutture-geotecnica:spettro-risposta-ntc`).

In alternativa, da terminale via il CLI [`vercel-labs/skills`](https://github.com/vercel-labs/skills):

```bash
npx skills@latest add morellid/skill-per-ingegneri
```

Il manifest e' in `.claude-plugin/marketplace.json`, **rigenerato automaticamente** da `scripts/build_catalog.py`.

### Installazione drag-and-drop su Claude.ai

Ogni skill e' distribuita anche come `.zip` autonomo nelle [GitHub Releases](https://github.com/morellid/skill-per-ingegneri/releases). Utile se usi Claude solo via web (claude.ai) e non hai installato Claude Code.

1. Apri l'ultima release: https://github.com/morellid/skill-per-ingegneri/releases/latest
2. Scarica il file `<skill-id>.zip` della skill che ti interessa (es. `pos-allegato-xv-checker.zip`).
3. Vai su https://claude.ai/customize/skills e fai upload (o drag-and-drop) del file `.zip`.

Lo zip contiene la skill completa (`SKILL.md`, `tasks/`, `examples/`, `references/`, `LICENSE`) in una singola directory top-level. Non serve estrarlo prima dell'upload.

### Codex `$skill-installer`

Da una sessione Codex (per skill singole):

```
$skill-installer https://github.com/<user>/skill-per-ingegneri/skills/pos-allegato-xv-checker
```

### Uso

Riavvia il tuo agent dopo l'installazione. Poi fai una domanda nel dominio della skill:

> "Verifica questo POS rispetto all'Allegato XV..."
>
> "Aiutami a redigere un DVR per un'azienda di 30 dipendenti"
>
> "Serve una DPIA per il nostro nuovo sistema di scoring clienti?"

L'agent caricara' la skill appropriata. In Codex puoi anche invocare esplicitamente: `/skills <nome-skill>`.

### Uso da altri agent (Cursor, Windsurf, GitHub Copilot, Devin, Amp, ...)

Per agent che leggono lo standard aperto [AGENTS.md](https://agents.md/), referenzia questo repo come submodule e aggiungi un puntatore al tuo progetto. Vedi [`AGENTS.md`](AGENTS.md) per i dettagli e le convenzioni.

Istruzioni dettagliate per ogni singola skill nel rispettivo `README.md` dentro `skills/<nome>/`.

## Come contribuire

Vedi [CONTRIBUTING.md](CONTRIBUTING.md). In sintesi:
- Solo fonti normative ufficiali (niente interpretazioni personali senza riferimento)
- Validazione da parte di un ingegnere di dominio prima del release
- Disclaimer di responsabilita' professionale obbligatorio in ogni skill
- Semver per skill, CHANGELOG aggiornato

## Principi

1. **Supporto, non sostituto**. Ogni skill emette output che richiede verifica e firma del professionista. Nessuna skill produce documenti auto-firmati o pronti al deposito senza revisione umana.
2. **Tracciabilita' delle fonti**. Ogni affermazione normativa e' riconducibile a un documento identificato da hash e data di consultazione (vedi `sources.yaml`).
3. **Lingua italiana**. Gli adempimenti sono italiani: istruzioni, output e riferimenti normativi sono in italiano. Struttura del codice e metadata in inglese per compatibilita' internazionale.
4. **Progressive disclosure**. Ogni skill e' monolitica ma carica solo i dettagli che servono per la specifica sotto-attivita' richiesta dall'utente.

## Autore

Davide Morelli <morelli.davide@gmail.com>

## Licenza

MIT. Vedi [LICENSE](LICENSE).

## Avvertenza

Le skill in questo repository sono strumenti di supporto e non sostituiscono il giudizio professionale. L'utilizzo improprio o non verificato degli output e' responsabilita' esclusiva dell'utente.
