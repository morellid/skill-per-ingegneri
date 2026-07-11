# AGENTS.md - transizione-5-0-asseverazione

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

La skill copre la **redazione e verifica della certificazione tecnica ex ante ed ex post** del **Piano Transizione 5.0**, credito d'imposta per investimenti delle imprese in beni 4.0 (Allegati A/B L. 232/2016), autoproduzione FER per autoconsumo e formazione, condizionati al raggiungimento di soglie minime di riduzione dei consumi energetici (>=3% sulla struttura produttiva o >=5% sul processo interessato dall'investimento). Riferimento normativo principale: **art. 38 DL 19/2024 + DM MIMIT-MEF 24/7/2024 + circolare MIMIT 25877/2024**. Dal 2026 la skill copre anche la **fase post-chiusura**: pratiche "tecnicamente ammissibili" rimaste senza copertura e pagate con il credito d'imposta dell'89,77% ex **art. 8 DL 38/2026 (conv. L. 88/2026)**. Target utente: **valutatori indipendenti** ammessi al rilascio delle certificazioni ai sensi dell'art. 15 co. 6 DM (EGE UNI CEI 11339, ESCo UNI CEI 11352, ingegneri sez. A/B, periti industriali con esperienza in efficienza energetica processi produttivi).

## Fonti autoritative

Catalogate in `references/sources.yaml`:

- **DL 19/2024 art. 38** (id `dl-19-2024-art-38`) - testo consolidato Normattiva, conv. con mod. da L. 56/2024
- **DM 24/7/2024** (id `dm-24-07-2024-transizione50`) - GU n. 183 del 06/08/2024, codice 24A04160
- **Circolare MIMIT 25877/2024** (id `circolare-mimit-16-08-2024`) - prot. AOO_PI 0025877.16-08-2024
- **FAQ MIMIT 10/4/2025** (id `faq-mimit-transizione50`) - documento di aggiornamento periodico
- **Circolare MISE 18/12/2014** (id `circolare-mise-18-12-2014-tep`) - coefficienti tep
- **GSE Portale Transizione 5.0** (id `gse-portale-transizione50`) - portale operativo
- **DL 38/2026 art. 8** (id `dl-38-2026-art-8`) - GU n. 72 del 27/03/2026, codice 26G00057; testo originale (35%, 537 mln)
- **DL 42/2026 art. 1** (id `dl-42-2026`) - GU n. 78 del 03/04/2026, codice 26G00061; abrogato dalla L. 88/2026 con salvezza degli effetti
- **L. 88/2026** (id `legge-88-2026-conversione`) - GU n. 117 del 22/05/2026, codici 26G00109 (legge) e 26A02590 (testo coordinato); fonte del testo vigente dell'art. 8
- **Avviso MIMIT 29/04/2026** (id `avviso-mimit-29-04-2026`) - ricevute di conferma, codice tributo 7079, obblighi dei beneficiari

Norme proprietarie (rinvio strutturale, no embed):
- **UNI CEI 11339:2009** (id `uni-cei-11339-ege`)
- **UNI CEI 11352:2014** (id `uni-cei-11352-esco`)

Rinvii a fonti normative complementari:
- **L. 232/2016** allegati A/B (id `legge-232-2016-allegati-A-B`)
- **DPR 445/2000** (id `dpr-445-2000`)
- **Codice penale artt. 359, 481** (id `codice-penale-359-481`)
- **Reg. UE 2020/852 art. 17** (id `regolamento-ue-2020-852-tassonomia`)

Estratti pertinenti in `references/estratti/`:
- `dl-19-2024-art-38.md` - inquadramento del Piano e soglie
- `dm-24-07-2024-articoli-chiave.md` - articoli chiave del decreto attuativo
- `circolare-mimit-criteri-risparmio.md` - criteri tecnici di calcolo
- `circolare-mimit-modelli-certificazioni.md` - modelli Allegati VIII, IX, X, XI
- `faq-mimit-soggetti-certificatori.md` - FAQ MIMIT chiave
- `circolare-mise-2014-tep.md` - coefficienti di conversione tep
- `dl-38-2026-credito-pratiche-ammissibili.md` - credito 89,77% pratiche tecnicamente ammissibili, contributo comma 3-bis

Trascrizioni verbatim delle fonti 2026 in `references/fonti/`: `dl-38-2026-art-8.md`, `dl-42-2026.md`, `legge-88-2026-conversione.md`, `avviso-mimit-29-04-2026.md`. Per il testo vigente dell'art. 8 usare sempre il testo coordinato trascritto in `legge-88-2026-conversione.md`.

## Articoli e punti chiave

Quando l'agent produce output, **cita sempre l'articolo preciso**. Riferimenti piu' frequenti:

### DL 19/2024
- **Art. 38 co. 1-2 DL**: ambito soggettivo (residenti in Italia, esclusioni)
- **Art. 38 co. 4 DL**: investimenti agevolabili e **soglie minime** (3% struttura / 5% processo)
- **Art. 38 co. 7 DL**: aliquote per scaglioni e fasce di risparmio
- **Art. 38 co. 11 DL**: certificazioni ex ante / ex post

### DM 24/7/2024
- **Art. 4 co. 3-4 DM**: avvio (1/1/2024) e completamento (31/12/2025)
- **Art. 5 DM**: DNSH e attivita' escluse (combustibili fossili, ETS, discariche, rifiuti pericolosi)
- **Art. 6 DM**: beni materiali/immateriali allegati A/B L. 232/2016, esclusioni TUIR
- **Art. 7 DM**: autoproduzione FER per autoconsumo (no biomasse)
- **Art. 8 DM**: formazione (limite 10% beni A/B+FER, max 300.000 EUR, 12 ore minimo)
- **Art. 9 co. 1-6 DM**: criteri determinazione risparmi (baseline ex ante, normalizzazione, scenario controfattuale, conversione tep)
- **Art. 10 DM**: intensita' beneficio (aliquote 35-15-5% / 40-20-10% / 45-25-15% per scaglione + fascia)
- **Art. 12 DM**: procedura (prenotazione, ordini 20%, completamento <= 28/2/2026)
- **Art. 15 co. 1 DM**: oggetto certificazioni ex ante / ex post
- **Art. 15 co. 6 DM lett. a/b/c**: soggetti abilitati (EGE/ESCo/ingegnere-perito)
- **Art. 15 co. 7 DM**: terzieta' e indipendenza
- **Art. 15 co. 8 DM**: polizza assicurativa
- **Art. 16 DM**: perizia tecnica caratteristiche/interconnessione (rinvio L. 232/2016 art. 1 co. 11)
- **Art. 17 DM**: certificazione contabile
- **Art. 18 DM**: DNSH come condizione di accesso
- **Art. 19-20 DM**: vigilanza e controlli (5 anni di conservazione)

### Circolare MIMIT 25877/2024
- **Cap. 1**: tabella aliquote (con esempi)
- **Cap. 2.1**: definizioni operative struttura produttiva e processo interessato (esempi 1-4 con figure 1-17)
- **Cap. 2.2**: scenario controfattuale (3 alternative UE/SEE in 5 anni)
- **Cap. 2 tab. 2**: indicatori di prestazione per settore
- **Cap. 4**: DNSH e schede applicabili (Allegato VII A-F2)
- **Allegato III**: dichiarazione di terzieta' del valutatore
- **Allegato V**: attestazione possesso perizia tecnica + certificazione contabile
- **Allegato VIII**: modello Certificazione Ex Ante
- **Allegato IX**: modello Relazione Tecnica Ex Ante
- **Allegato X**: modello Certificazione Ex Post
- **Allegato XI**: modello Relazione Tecnica Ex Post

### DL 38/2026 art. 8 (conv. L. 88/2026) - fase post-chiusura
- **Art. 8 co. 1**: credito d'imposta 89,77% per le pratiche "tecnicamente ammissibili" rimaste senza copertura (base: allegati A/B L. 232/2016 + spese di formazione; plafond 1.302,3 mln per il 2026)
- **Art. 8 co. 2**: comunicazione GSE del credito utilizzabile entro il 30/4/2026 (attuata con ricevute su piattaforma Transizione 5.0 dal 29/4/2026 - Avviso MIMIT)
- **Art. 8 co. 3**: compensazione esclusiva F24 (codice tributo 7079) entro il 31/12/2026, decorsi 5 giorni dalla comunicazione GSE; nessun limite di compensazione; irrilevanza reddito/IRAP; rinvio all'art. 38 DL 19/2024 e al DM 24/7/2024 "anche ai fini delle attivita' di controllo"
- **Art. 8 co. 3-bis**: contributo separato per FER autoconsumo, sistemi di accumulo (DNSH) e spese di certificazione (57,7/80/60 mln per 2026/2027/2028); erogazione MIMIT con decreto attuativo non ancora pubblicato; il contributo non concorre alla formazione del reddito ne' della base IRAP (clausola aggiunta in sede di conversione, assente nel DL 42/2026)
- **L. 88/2026 art. 1 co. 2**: abrogazione del DL 42/2026 con salvezza di atti, provvedimenti, effetti e rapporti giuridici

### Riferimenti penali
- **DPR 445/2000 art. 76**: sanzioni penali per false dichiarazioni in DSAN
- **Codice penale art. 359**: persone esercenti un servizio di pubblica necessita' (qualifica del certificatore)
- **Codice penale art. 481**: falsita' ideologica in certificati di soggetti che esercitano un servizio di pubblica necessita'

## Convenzioni specifiche

### Cosa NON fare

- **Non confondere la certificazione tecnica (art. 15 DM)** con la **perizia tecnica caratteristiche/interconnessione** (art. 16 DM, art. 1 co. 11 L. 232/2016) ne' con la **certificazione contabile** (art. 17 DM): sono tre adempimenti distinti, con soggetti firmatari potenzialmente diversi.
- **Non sottovalutare il DNSH** (art. 5 e 18 DM): il principio prevale sul calcolo dei risparmi. Un progetto con riduzione consumi del 50% ma con investimento connesso a combustibili fossili **NON e' ammissibile**.
- **Non rilasciare certificazione senza sopralluogo**: i modelli Allegati VIII/X richiedono espressamente che il certificatore dichiari di aver verificato i dati "anche mediante l'effettuazione di sopralluoghi presso la struttura produttiva".
- **Non includere autoproduzione FER e formazione nel calcolo della soglia 3%/5%**: la soglia minima e' calcolata **esclusivamente sui beni 4.0** (allegati A/B), come dispone l'art. 38 co. 4 DL.
- **Non confondere "struttura produttiva" e "processo interessato"**: sono perimetri alternativi (3% vs 5%), non cumulabili. La scelta segue le regole degli esempi 1-4 del cap. 2.1 della circolare MIMIT.
- **Non emettere giudizi su "modifiche sostanziali"** in senso favorevole al cliente: se la modifica rientra nelle voci della FAQ MIMIT 2.10 (aggiunta tipologie beni, modifica perimetro, incremento potenza FER, formazione diversa), **e' sostanziale** e l'impresa deve aver rinunciato e ripresentato.
- **Non emettere certificazione ex post se i dati ex post non rispettano la soglia minima 3%/5%**: si determina la decadenza dal beneficio (art. 20 DM).
- **Non utilizzare FAQ MIMIT obsolete**: il MIMIT aggiorna periodicamente le FAQ. Verificare la versione vigente prima dell'asseverazione.
- **Non interpretare l'esperienza in efficienza energetica del certificatore non-EGE/ESCo**: l'art. 15 co. 6 lett. c DM richiede "competenze e comprovata esperienza" ma non fissa criteri quantitativi: la valutazione e' rimessa al MIMIT in sede di vigilanza.
- **Non procedere senza dichiarazione di terzieta'** (Allegato III): se il certificatore ha avuto consulenze nei 3 anni precedenti con il beneficiario, **non puo' rilasciare la certificazione**.

### Cosa fare

- **Citare sempre articolo + comma + lettera** del DM 24/7/2024 (es. "art. 15 co. 6 lett. a DM 24/7/2024 - EGE certificato UNI CEI 11339"), non il decreto in generale.
- **Inquadrare l'intervento prima del calcolo**: tipologia investimenti, importo, perimetro (struttura/processo), soggetto certificatore.
- **Applicare il filtro DNSH come prerequisito**: la verifica art. 5 DM e' separata e prevale sulla verifica delle soglie di risparmio.
- **Esprimere i consumi sempre in tep** (rinvio circ. MISE 18/12/2014): mostrare i fattori di conversione applicati per ciascun vettore.
- **Documentare le fonti** degli indicatori di prestazione (BREF, BAT, letteratura, offerte mercato): la circolare MIMIT cap. 2 lo richiede espressamente.
- **Esplicitare l'algoritmo di calcolo** nei modelli VIII e X, e svilupparlo nelle relazioni tecniche IX e XI.
- **Conservare il foglio di calcolo dell'algoritmo** come elemento centrale della documentazione probatoria (art. 19 DM, conservazione 5 anni).
- **Per scenario controfattuale**, richiedere 3 alternative reali con marca, modello, prestazione, prezzo, fonte (art. 9 co. 5 DM).
- **In ex post, dichiarare esplicitamente le modifiche** rispetto all'ex ante (modello Allegato X) o l'assenza di modifiche; se modifiche sostanziali, rinviare alla rinuncia.
- **Concludere ogni output con il rinvio professionale**: revisione e firma del valutatore indipendente, rischio penale (artt. 359, 481 c.p. + art. 76 DPR 445/2000), conservazione 5 anni.

## Validatori

- Da identificare per Livello 2 validation. Profilo richiesto: **EGE certificato UNI CEI 11339** o **ESCo certificata UNI CEI 11352** con esperienza diretta in asseverazioni Transizione 4.0 / 5.0 gia' presentate al GSE; oppure ingegnere specializzato in DNSH PNRR (audit Ragioneria Generale dello Stato).

## Stato attuale

- Versione: vedi `CHANGELOG.md`
- Validazione: Livello 1 (autore-driven, fonti pubbliche)
- Task files:
  - `verifica-ammissibilita.md`
  - `calcola-riduzione-consumi.md`
  - `struttura-certificazione-ex-ante.md`
  - `struttura-certificazione-ex-post.md`
- Esempi: 1 conforme (manifatturiero meccanico, 3,2 mln EUR, processo interessato, riduzione 10,10% -> Fascia 2) + 1 non conforme (cogenerazione gas naturale, violazione DNSH)
