# AGENTS.md - nis2-self-assessment

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Self-assessment di conformita' al **D.Lgs. 4 settembre 2024, n. 138** (recepimento italiano della Direttiva (UE) 2022/2555 - NIS 2) per organizzazioni italiane private e pubbliche. La skill copre quattro angoli: perimetro (essenziale/importante/fuori), gap analysis sulle misure di base ACN (Determinazione 379907/2025 vigente dal 15/01/2026), verifica di significativita' di un incidente (codici IS-1..4 + soglie telco art. 6 co. 2), obblighi di governance dell'organo di amministrazione.

Target utente: CISO, IT manager, DPO, ingegneri dell'informazione, consulenti cybersecurity di organizzazioni italiane potenzialmente in ambito NIS. Per le PA centrali gia' incluse nel PSNC (DL 105/2019) la skill resta applicabile in quanto le PA centrali Allegato III lett. a) sono comunque soggetti essenziali NIS2 (art. 6 co. 1 lett. e); cambia il coordinamento delle notifiche (art. 1 co. 8 DL 105/2019 come modificato da art. 44 D.Lgs. 138/2024). Non assumere esclusione automatica del perimetro NIS per i soggetti PSNC.

## Fonti autoritative

- **D.Lgs. 138/2024** (id `dlgs-138-2024` in `sources.yaml`) - decreto di recepimento italiano. Riferimento normativo primario.
- **Direttiva (UE) 2022/2555 - NIS 2** (id `dir-2022-2555-nis2`) - direttiva madre. Citata solo per concetti strutturali; l'attuazione operativa segue il decreto italiano.
- **Regolamento di esecuzione (UE) 2024/2690** (id `reg-ese-2024-2690`) - applica direttamente a un sottoinsieme di soggetti (DNS, cloud, data center, social, ecc.). Per gli altri soggetti italiani il riferimento e' la Determinazione ACN.
- **Determinazione ACN n. 379907 del 18/12/2025** (id `acn-det-379907-2025`, vigente dal 15/01/2026) - misure di base distinte per soggetti importanti (Allegato 1, 37 sottocategorie) ed essenziali (Allegato 2, 43 sottocategorie), strutturate sul Framework Nazionale Cybersecurity ed. 2025; codici di incidente significativo di base IS-1..3 (importanti, Allegato 3) e IS-1..4 (essenziali, Allegato 4); soglie quantitative aggiuntive solo per operatori telco all'art. 6 co. 2.
- **Determinazione ACN n. 164179 del 14/04/2025** (id `acn-det-164179-2025`) - SUPERATA dalla 379907/2025 dal 15/01/2026; mantenuta in catalogo come riferimento storico.
- **Pagina riepilogativa ACN** (id `acn-portale-normativa`) - indice atti generali, da consultare per nuove determinazioni.

Estratti gia' preparati in `references/estratti/`:
- `dlgs-138-2024-perimetro.md` - art. 3, art. 6, art. 7 + note dimensionali Racc. 2003/361/CE
- `dlgs-138-2024-misure-art23.md` - art. 23 organi di amministrazione + art. 24 misure di gestione del rischio
- `dlgs-138-2024-incident-art25.md` - art. 25 obblighi di notifica
- `dlgs-138-2024-allegati-i-iv.md` - Allegati I-IV (settori e tipologie)
- `acn-det-379907-articoli.md` - artt. 1-9 della Determinazione 379907/2025 (vigente dal 15/01/2026)
- `acn-misure-base-importanti.md` - Allegato 1 Det. 379907/2025 (37 sottocategorie)
- `acn-misure-base-essenziali.md` - Allegato 2 Det. 379907/2025 (43 sottocategorie)
- `acn-incidenti-significativi.md` - Allegati 3-4 Det. 379907/2025 (codici IS-1..4) + soglie telco art. 6 co. 2
- `reg-ese-2024-2690-ambito.md` - ambito del Reg. UE 2024/2690

## Articoli e punti chiave

- **Art. 2 D.Lgs. 138/2024 - Definizioni**: cataloga termini chiave (incidente, quasi-incidente, rischio, gestione degli incidenti, minaccia informatica significativa, approccio multi-rischio, ecc.). I concetti operativi di "soggetto essenziale" e "soggetto importante" sono nell'art. 6.
- **Art. 3 - Ambito di applicazione**: regola di applicazione (size-cap rule). Si applica ai soggetti delle tipologie di Allegati I-II che superano i massimali per le piccole imprese (Racc. 2003/361/CE art. 2 par. 2 dell'allegato), con esclusione dell'art. 3 par. 4 della Raccomandazione (co. 3) e applicazione indipendente dalle dimensioni per soggetti critici (Dir. 2022/2557), fornitori di reti pubbliche di comunicazione elettronica, prestatori di servizi fiduciari, gestori TLD, fornitori DNS e di servizi di registrazione domini (co. 5), PA in Allegato III (co. 6), tipologie Allegato IV individuate (co. 8) e impresa collegata che soddisfa criteri (co. 10).
- **Art. 6 - Soggetti essenziali e soggetti importanti**: essenziali (co. 1) = soggetti Allegato I che superano i massimali per le **medie imprese** (Racc. 2003/361/CE Allegato art. 2 par. 1: PMI = occupati < 250 AND (fatturato annuo <= 50M EUR OR totale di bilancio annuo <= 43M EUR); quindi NON-PMI = occupati >= 250 **OPPURE** (fatturato > 50M EUR **AND** bilancio > 43M EUR)) - piu' soggetti critici (Dir. 2022/2557), fornitori reti pubbliche di comunicazione elettronica considerati medie imprese, prestatori servizi fiduciari qualificati e gestori TLD/DNS indipendentemente dalle dimensioni, **PA centrali** Allegato III co. 1 lett. a) indipendentemente dalle dimensioni. Importanti (co. 3) = tutti gli altri soggetti in ambito.
- **Art. 7 - Identificazione ed elencazione**: dal **1 gennaio al 28 febbraio** di ogni anno i soggetti si registrano/aggiornano sulla piattaforma ACN. Entro il **31 marzo** ACN redige l'elenco e comunica l'inserimento. Dal **15 aprile al 31 maggio** integrazione dati (IP pubblici, domini, ecc.). Notifica modifiche entro **14 giorni**.
- **Art. 23 - Organi di amministrazione e direttivi**: (a) **approvano** le modalita' di implementazione delle misure di cui all'art. 24; (b) **sovrintendono** all'implementazione degli obblighi del decreto e dell'art. 7; (c) sono **responsabili delle violazioni**. Devono inoltre seguire una formazione in materia di sicurezza informatica e promuovere formazione coerente per i dipendenti. Sono informati periodicamente o tempestivamente sugli incidenti notificati ex artt. 25-26.
- **Art. 24 - Obblighi misure di gestione del rischio**: misure tecniche, operative e organizzative adeguate e proporzionate, basate su un approccio multi-rischio, con almeno **10 elementi minimi** (co. 2 lett. a-l):
  - a) politiche di analisi dei rischi e di sicurezza dei sistemi informativi e di rete;
  - b) gestione degli incidenti (incluse procedure e strumenti di notifica artt. 25-26);
  - c) continuita' operativa (backup, disaster recovery, gestione delle crisi);
  - d) sicurezza della catena di approvvigionamento (rapporti con fornitori diretti);
  - e) sicurezza dell'acquisizione, sviluppo e manutenzione (incluse vulnerability disclosure);
  - f) politiche e procedure per valutare l'efficacia delle misure;
  - g) pratiche di igiene cyber di base e formazione;
  - h) politiche e procedure su crittografia e cifratura;
  - i) sicurezza e affidabilita' del personale, controllo degli accessi, gestione asset;
  - l) MFA o autenticazione continua, comunicazioni protette, sistemi di emergenza protetti.
- **Art. 25 - Obblighi di notifica di incidente significativo**:
  - **24 ore**: pre-notifica al CSIRT Italia (atto illegittimo/malevolo? impatto transfrontaliero?) (co. 5 lett. a)
  - **72 ore**: notifica con valutazione iniziale gravita'/impatto + IoC ove disponibili (co. 5 lett. b)
  - **1 mese** dalla notifica: relazione finale (descrizione, root cause, misure di mitigazione, impatto transfrontaliero) (co. 5 lett. d)
  - Incidente in corso: relazione mensile + relazione finale entro 1 mese dalla chiusura (co. 5 lett. e)
  - Soglia incidente significativo (co. 4): a) grave perturbazione operativa o perdite finanziarie per il soggetto; b) ripercussioni su altre persone fisiche/giuridiche con perdite materiali/immateriali considerevoli.
  - Deroga: prestatori di servizi fiduciari notificano la b) entro **24 ore** (co. 6).
- **Art. 38 - Sanzioni amministrative**:
  - Soggetti **essenziali** (privati): fino a **10M EUR o 2% fatturato annuo mondiale** dell'esercizio precedente, se superiore (co. 9 lett. a). Minimo: 1/20 del massimo edittale.
  - Soggetti **importanti** (privati): fino a **7M EUR o 1.4% fatturato annuo mondiale**, se superiore (co. 9 lett. b). Minimo: 1/30 del massimo.
  - PA Allegato III e tipologie Allegato IV punto 1 e 4 a controllo pubblico, essenziali: **25.000 - 125.000 EUR** (co. 9 lett. c); importanti: ridotte di 1/3 (co. 9 lett. d).
  - Violazioni di registrazione/aggiornamento (art. 7) e collaborazione (commi 10-11): essenziali fino a **0.1% fatturato**; importanti fino a **0.07% fatturato**.
  - Sanzione amministrativa accessoria: **incapacita' a svolgere funzioni dirigenziali** per gli organi di amministrazione e i CEO/legali rappresentanti se il soggetto non ottempera alla diffida (co. 6).
- **Allegati I e II**: 10 settori altamente critici (Allegato I) + 7 altri settori critici (Allegato II) per ~ 17 settori complessivi.
  - Allegato I (alta criticita'): 1. Energia (elettrica, teleriscaldamento/raffrescamento, petrolio, gas, idrogeno); 2. Trasporti (aereo, ferroviario, vie d'acqua, su strada); 3. Settore bancario; 4. Infrastrutture dei mercati finanziari; 5. Settore sanitario; 6. Acqua potabile; 7. Acque reflue; 8. Infrastrutture digitali; 9. Gestione dei servizi TIC (B2B); 10. Spazio.
  - Allegato II (altri critici): 1. Servizi postali e di corriere; 2. Gestione dei rifiuti; 3. Fabbricazione/produzione/distribuzione sostanze chimiche; 4. Produzione/trasformazione/distribuzione alimenti; 5. Fabbricazione (dispositivi medici, computer/elettronica/ottica, apparecchiature elettriche, macchinari, autoveicoli, altri mezzi di trasporto); 6. Fornitori di servizi digitali (mercati online, motori di ricerca, social network, registrar domini); 7. Ricerca.
- **Allegato III**: PA italiane (centrali, regionali, locali, altri soggetti pubblici). Le PA centrali (lett. a) sono soggetti essenziali indipendentemente dalle dimensioni (art. 6 co. 1 lett. e).
- **Allegato IV**: trasporto pubblico locale; istituti di istruzione che svolgono ricerca; soggetti di interesse culturale; societa' in house, partecipate e a controllo pubblico (D.Lgs. 175/2016).
- **Determinazione ACN 379907/2025 Allegato 1 (importanti, 37 sottocat / 87 requisiti) e Allegato 2 (essenziali, 43 sottocat / 112 requisiti)**: misure di base organizzate per funzioni/categorie/sottocategorie/requisiti del Framework Nazionale Cybersecurity ed. 2025. Tempi di adeguamento (art. 3): **18 mesi** per le misure, **9 mesi** per la notifica incidenti, decorrenti dalla **comunicazione di inserimento** ricevuta da ciascun soggetto.

## Convenzioni specifiche

### Cosa NON fare
- Non scambiare gli articoli: art. 23 e' **organi di amministrazione**, art. 24 e' **misure**. Errore frequente: assegnare i 10 ambiti minimi all'art. 23. Sono al **co. 2 dell'art. 24**.
- Non confondere **"soggetto essenziale" NIS2** con altre nozioni di "infrastruttura critica" (PSNC, codice comunicazioni elettroniche, OES sotto NIS originale). Sono perimetri distinti.
- Non assumere che il Reg. UE 2024/2690 sia vincolante per tutti i soggetti italiani: si applica solo al sottoinsieme dell'art. 1 del Regolamento (DNS, cloud, data center, social, mercati online, motori di ricerca, servizi gestiti/sicurezza gestiti, servizi fiduciari).
- Non fornire la classificazione di perimetro come fosse una decisione finale: e' un orientamento. La classificazione ufficiale la fa il soggetto stesso sulla piattaforma ACN, sotto la propria responsabilita' (art. 7).
- Non confondere i termini di notifica: pre-notifica 24h, notifica 72h, report finale 1 mese (art. 25). Non scambiarli con i termini GDPR (72h notifica al Garante, art. 33 GDPR), che si applicano in parallelo per data breach con dati personali.
- Non sostituire le specifiche tecniche del Framework Nazionale Cybersecurity con valutazioni "a sentimento": l'output deve mappare gap a sottocategorie precise.

### Cosa fare
- Citare sempre l'articolo, il comma e la lettera precisi (es. "art. 24 co. 2 lett. d) D.Lgs. 138/2024" oppure "Det. ACN 379907/2025 Allegato 2 funzione PROTECT categoria PR.AA sottocategoria PR.AA-03").
- Per il perimetro, applicare la valutazione in cascata: (1) il settore rientra in Allegato I o II? (2) le tipologie di soggetto si applicano (Allegato I/II + III/IV)? (3) la size-cap rule e' superata (medie/grandi)? (4) c'e' applicazione indipendente dalle dimensioni (art. 3 commi 5, 6, 8, 9, 10)? (5) c'e' classificazione speciale come essenziale ex art. 6 co. 1 lett. b)-e)? Anche un solo trigger basta per essere "in ambito"; per essere "essenziale" servono i criteri di art. 6 co. 1.
- Distinguere chiaramente fra obblighi del soggetto e obblighi dell'organo di amministrazione (art. 24 vs art. 23): sono distinti e cumulativi.
- Per la verifica incidente, applicare prima i criteri art. 25 co. 4 (perturbazione operativa / perdite finanziarie / ripercussioni su altre persone), poi i codici IS-1..4 degli Allegati 3-4 della Determinazione ACN 379907/2025; per gli operatori telco verificare anche le soglie quantitative dell'art. 6 co. 2.
- Concludere ogni output con il rinvio a CISO/compliance/legale e con il richiamo all'art. 38 sulle sanzioni.

## Validatori

- Da identificare. Profilo target: CISO o consulente cybersecurity con esperienza diretta su mandati NIS2 attivi (non Vitale, non Frontoni - settori diversi). Idealmente almeno un profilo con esperienza ACN o CSIRT.

## Stato attuale

- Versione: vedi `CHANGELOG.md` (v0.1.0-alpha)
- Validazione: Livello 1 (auto-validazione autore) - Livello 2 da pianificare
- Task files: 4 (`valuta-perimetro`, `gap-analysis-misure`, `verifica-incidente-significativo`, `check-obblighi-governance`)
- Estratti normativi: 9 estratti preparati
- Esempi: 2 (utility energetica essenziale + PMI manifattura importante)
- Skill non ancora testata su organizzazione reale - validazione Livello 2 prioritaria
