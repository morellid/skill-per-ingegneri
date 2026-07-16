# Estratto operativo - riuso e rilascio open source del software PA

> Checklist parafrasata dalle fonti in `references/fonti/riuso-software-pa.md` (C.A.D.
> artt. 68-69 e Linee guida AgID, Allegato A). NON sostituisce la scelta della licenza
> ne' la lettura della documentazione del formato publiccode.yml.

## 1. Acquisizione - analisi comparativa (art. 68)

- [ ] Prima di acquisire, effettuare la **valutazione comparativa tecnico-economica** tra:
      (a) software sviluppato ad hoc; (b) **riuso** di software di altre PA; (c) **software
      libero/open source**; (d) **cloud**; (e) **proprietario** (licenza d'uso).
- [ ] Applicare i principi: economicita', efficienza, tutela degli investimenti, **riuso**,
      **neutralita' tecnologica**.
- [ ] Cercare soluzioni a riuso/Open Source su **Developers Italia** prima di sviluppare ex novo.

## 2. Obbligo di rilascio (art. 69)

- [ ] Se la PA e' **titolare** di software realizzato **su specifiche indicazioni del
      committente pubblico** -> **obbligo** di rendere disponibile il **codice sorgente
      completo di documentazione**, in **repertorio pubblico**, sotto **licenza aperta**,
      in **uso gratuito** ad altre PA/soggetti.
- [ ] Eccezioni: motivate ragioni di **ordine e sicurezza pubblica, difesa nazionale,
      consultazioni elettorali**.

## 3. Rilascio in open source (Linee guida AgID, Allegato A)

- [ ] **Licenza aperta**: sceglierla e attribuirla; individuare la **titolarita'**
      (copyright dell'Amministrazione committente).
- [ ] **Materiali da rilasciare** e **organizzazione del repository** (struttura chiara).
- [ ] **README.md** (A.7 - MUST): titolo/sottotitolo, descrizione e casi d'uso,
      prerequisiti/dipendenze, istruzioni di installazione, stato del progetto, detentori
      del copyright, manutentori, **e-mail per segnalazioni di sicurezza** (non via issue
      tracker pubblico).
- [ ] **Documentazione** (A.8 - MUST): installazione dipendenze/ambiente, build,
      installazione in produzione, architettura; **formato versionabile riga per riga**
      (HTML, Markdown, reStructuredText, LaTeX). **ODT/DOCX/PDF non ammessi.**
- [ ] **Tempi** (A.9): se non si adotta il **modello di sviluppo aperto**, rilascio
      **entro 15 giorni** (MUST) dall'acquisizione/collaudo/produzione (per ciascun lotto).

## 4. Registrazione su Developers Italia (A.11)

- [ ] Pubblicare un file **`publiccode.yml`** nella **directory root** del repository (il
      crawler di Developers Italia lo rileva e genera la scheda nel catalogo). Formato
      documentato su https://github.com/italia/publiccode.yml.
- [ ] Registrare lo **strumento di code-hosting** (l'organizzazione) associandolo alla PA.

## Avvertenze

- La **scelta della licenza** e la **validazione** della documentazione/publiccode.yml
  restano dell'Amministrazione: la checklist inquadra obblighi e contenuti.
- Il **dettaglio campo-per-campo** del publiccode.yml e' nella documentazione del formato,
  non riprodotto qui.
