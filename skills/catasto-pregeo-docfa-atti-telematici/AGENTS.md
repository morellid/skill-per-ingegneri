# AGENTS.md - catasto-pregeo-docfa-atti-telematici

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Skill di assistenza alla redazione e al check pre-trasmissione degli atti telematici di aggiornamento del **Catasto Terreni** (procedura **Pregeo 10**) e del **Catasto Fabbricati** (procedura **Docfa 4**) presso l'Agenzia delle Entrate via portale Sister. Norme di riferimento principali: art. 30 DPR 380/2001 (Testo Unico Edilizia), DM 28/1998 (definizione UIU), Circolare AdE Territorio 3 del 16/10/2009 (Pregeo 10), Risoluzione AdE 40/E del 9/6/2025 (deposito telematico frazionamenti dal 1/7/2025), Vademecum Do.C.Fa. v1.0 (luglio 2022). Target: geometri, ingegneri, architetti, dottori agronomi, periti agrari, periti edili abilitati alla trasmissione telematica (Provv. AdE 11/3/2015 prot. 35112) e dipendenti PA in regime facoltativo (Provv. AdE 28/1/2021 prot. 27427).

## Fonti autoritative

Cfr. `references/sources.yaml`. Le fonti che hanno binari archiviati in `not_in_repo/` con SHA256 verificato sono:

- **Circolare AdE Territorio 3 del 16/10/2009** (Pregeo 10) - id `ade-circolare-3-2009-pregeo10`, sha256 `580012be6b445f7f3fa9889593775fa331c3aa23dfefdd1f5ec62a2d9306d15f`
- **Risoluzione AdE 40/E del 9/6/2025** (deposito telematico frazionamenti) - id `ade-risoluzione-40-2025-deposito-telematico`, sha256 `8b39d6265029f056dbfe96ee10b165ca9736379d0d2e02deb0e6e0f305315130`
- **Vademecum Do.C.Fa. v1.0 - luglio 2022** - id `ade-vademecum-docfa-v1`, sha256 `7ee7fbe724921d589448bc5d6f3322cc40e284c1d3498a37594162c6c299d6a0`

Le altre fonti (Normattiva per leggi/decreti, pagine istituzionali AdE per istruzioni operative Docfa, software Pregeo, Quaderno Docfa, Sister) sono catalogate per URL ma non archiviate (testi soggetti ad aggiornamento continuo, hash non significativo).

Estratti gia' preparati in `references/estratti/`:

- `dpr-380-2001-art-30.md` - regime di deposito presso il Comune ante e post 1/7/2025 (commi 5 e 5-bis)
- `dm-28-1998-uiu.md` - definizione di unita' immobiliare urbana e mappa Gruppo F (F/1-F/7)
- `circolare-3-2009-pregeo10.md` - tipologie atti Pregeo 10, controlli automatici, cause di rifiuto
- `risoluzione-40-2025-deposito-telematico.md` - ambito FR/FM/SC, dichiarazioni riga 9, workflow Portale Comuni
- `vademecum-docfa-categorie-causali.md` - categorie A/B/C/D/E/F, causali Quadro A/B Docfa
- `vademecum-docfa-elaborato-planimetrico.md` - EP, ES, ET (CF/AL/AC/CI/CS), planimetrie, Quadro D

## Articoli e punti chiave

Quando l'agent produce output, deve citare il riferimento preciso, non la legge in generale.

- **Art. 30 co. 5 DPR 380/2001**: presupposto di approvazione catastale = deposito presso il Comune dei Tipi di Frazionamento (regime ante 1/7/2025 e regime residuale per atti non telematici).
- **Art. 30 co. 5-bis DPR 380/2001** (introdotto da art. 25 D.Lgs. 1/2024): per atti FR/FM/SC presentati telematicamente dal 1/7/2025, il deposito e' effettuato dall'AdE sul Portale dei Comuni; comunicazione via PEC `depositofrazionamenticatastali@pec.agenziaentrate.it`.
- **Art. 2 DM 28/1998**: definizione di unita' immobiliare urbana (autonomia funzionale e reddituale, appartenenza alla stessa ditta).
- **Art. 3 co. 2 DM 28/1998**: beni iscrivibili senza rendita catastale (mappatura ai Gruppi F).
- **Art. 38 e 47 DPR 445/2000**: forma delle DSAN. **Art. 76 DPR 445/2000**: sanzioni penali per false dichiarazioni (artt. 359 e 481 c.p.).
- **Circolare AdE 3/2009 par. 2.3 e Allegato 2**: tipologie codificate degli atti Pregeo (riga 9 libretto delle misure - menu "elenco atto aggiornamento").
- **Circolare AdE 3/2009 par. 5**: tipologie escluse dall'approvazione automatica (TP, atti su acque/strade, estratti autoallestiti, atti in esenzione tributi, particelle demaniali).
- **Circolare AdE 3/2009 par. 6 lett. d**: l'atto e' "inidoneo alla registrazione" se i controlli con esito negativo non sono giustificati nella relazione tecnica strutturata.
- **Risoluzione AdE 40/E 2025 nota 4**: deposito comunale a cura del professionista per FR/FM/SC dopo il 1/7/2025 -> atto privo di effetti, non approvabile.
- **Risoluzione AdE 40/E 2025 nota 5**: eccezione tavolare (Pregeo 10.6.5 con patch dedicata, giustificazione in Relazione Tecnica Libera).
- **Vademecum Docfa cap. 1.1.1**: criteri di perimetrazione UIU (autonomia funzionale e reddituale + appartenenza alla stessa ditta).
- **Vademecum Docfa cap. 1.2.4**: condizioni operative per l'attribuzione delle categorie F/1, F/2, F/3, F/4, F/5, F/6, F/7 (vincoli di applicabilita').
- **Vademecum Docfa cap. 2.4.2**: dichiarazioni obbligatorie nel Quadro D - elenco indicativo non esaustivo.
- **Vademecum Docfa cap. 3.1.1**: casistiche obbligatorie di Elaborato Planimetrico.
- **Vademecum Docfa cap. 3.1.3**: rappresentazione delle Entita' Tipologiche (CF, AL, AC, CI, CS) per le sole dichiarazioni di accatastamento.
- **DPR 138/1998 Allegato C**: criteri per la determinazione della superficie catastale UIU dei Gruppi A, B, C.

## Convenzioni specifiche

### Cosa NON fare

- **Non inventare codici di tipologia** in riga 9 del libretto Pregeo: il menu a tendina "elenco atto aggiornamento" e' tassativo (Circ. 3/2009 par. 2.3 + Circ. 44/E 2016 + Risoluzione 40/E 2025). Se il caso non rientra nelle tipologie codificate, l'atto va trattato in modalita' tradizionale (par. 5 Circ. 3/2009).
- **Non riprodurre testo libero** nelle dichiarazioni della relazione tecnica strutturata Pregeo: solo le formule predefinite di cui all'Allegato 4 della Circ. 3/2009 (e successive integrazioni) sono accettate dall'approvazione automatica.
- **Non proporre l'attestazione di deposito comunale** per atti FR/FM/SC trasmessi telematicamente dopo il 1/7/2025: e' causa diretta di rigetto (Risoluzione 40/E 2025 nota 4).
- **Non proporre la categoria F/2** per immobili "non individuabili ne' perimetrabili" (privi di copertura E con muri sotto 1 m) o per immobili iscrivibili in altra categoria (Vademecum cap. 1.2.4).
- **Non proporre la categoria F/3** in dichiarazione di variazione per UIU gia' censite produttive di reddito (Vademecum cap. 1.2.4 - "non e' ammissibile").
- **Non proporre la categoria F/4** all'unica UIU oggetto di intervento edilizio: ammessa solo se l'intervento riguarda fabbricato composto da piu' UIU (Vademecum cap. 1.2.4).
- **Non determinare la rendita catastale o la superficie catastale numerica**: la skill rinvia al professionista (tariffe d'estimo per zona censuaria, coefficienti DPR 138/1998 Allegato C).
- **Non sostituire il sopralluogo fisico** per perimetrazione UIU, individuazione BCC/BCNC, accertamento stato di degrado (F/2) o stato avanzamento lavori (F/3).
- **Non avviare il workflow di accatastamento Docfa** prima dell'approvazione del Tipo Mappale (Pregeo) che istituisce la particella urbana e la categoria F/6 di servizio (Vademecum cap. 1.2.4 - F/6).

### Cosa fare

- **Citare sempre la fonte normativa precisa**: articolo, comma, capitolo del Vademecum, paragrafo della circolare, nota della Risoluzione 40/E 2025.
- **Verificare prima di tutto la versione del software** in uso (Pregeo 10.6.5 - APAG 2.15 obbligatoria dal 1/7/2025; Docfa 4.00.5 vigente). Se l'utente usa una versione obsoleta, segnalare il rischio di respingimento del canale telematico (Risoluzione 40/E 2025 nota 5).
- **Per ogni atto Pregeo/Docfa, distinguere fra**: redazione (check pre-invio) e diagnosi rifiuto (analisi del messaggio di sospensione). Le procedure differiscono.
- **Per i workflow misti Pregeo -> Docfa**, ricordare la sequenza obbligata: (1) Tipo Mappale Pregeo; (2) approvazione AdE; (3) iscrizione automatica F/6 della particella urbana; (4) Docfa di accatastamento (causale Nuova Costruzione o Unita' afferenti); (5) eventuale voltura post-rogito.
- **Strutturare gli output** come checklist conforme/non conforme + bozza di dichiarazione + rinvio al manuale operativo del software per la compilazione campo-per-campo.
- **Concludere ogni output** con: limiti di verifica della skill, rinvio al professionista firmatario, segnalazione rischio penale ex artt. 359 e 481 c.p. + art. 76 DPR 445/2000.

## Validatori

- *(non ancora identificato)* - validatore di dominio per Livello 2 (geometra o ingegnere edile con esperienza Pregeo+Docfa).

## Stato attuale

- Versione: vedi `CHANGELOG.md` (0.1.0-alpha)
- Validazione: Livello 1 (self-check)
- Task files: 5 (`scelta-tipo-pregeo-e-check.md`, `scelta-causale-categoria-docfa.md`, `check-pre-trasmissione-docfa.md`, `diagnosi-rifiuti-telematici.md`, `workflow-pregeo-docfa.md`)
- Esempi: 1 conforme + 1 problematico (2 totali)
