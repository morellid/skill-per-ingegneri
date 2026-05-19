# AGENTS.md - aua-dpr59-dossier

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Skill di supporto alla preparazione e all'autoverifica del dossier per
l'**Autorizzazione Unica Ambientale (AUA)** ai sensi del **D.P.R. 13
marzo 2013, n. 59**. Target: ingegneri ambientali, consulenti HSE,
tecnici SUAP, addetti ufficio ambiente di PMI e impianti non-AIA. La
skill aggrega titoli ambientali (scarichi, emissioni, rifiuti, acustica,
fanghi, radiazioni) ma non entra nel merito tecnico di ciascun titolo.

## Fonti autoritative

Catalogo completo in `references/sources.yaml`.

- **D.P.R. 13 marzo 2013, n. 59** (testo vigente da Normattiva,
  consultato il 2026-05-19) - sha256
  `f566907ae45ddccd6f2300ad098779de6a3f13b1df2f072e986496bcca363823`.
  Testo verbatim degli articoli 1-12 in
  `references/fonti/dpr-59-2013-articoli-1-12.md`.

Estratti pertinenti gia' preparati:

- `references/estratti/dpr-59-2013-aua-perimetro.md` - parafrasi mirata
  in 10 sezioni: ambito (art. 1), perimetro 9 titoli (art. 3), procedura
  (art. 4), durata e rinnovo (artt. 3 co. 6 e 5), modifiche (art. 6),
  autorizzazioni generali (art. 7), oneri (art. 8), transitorie (art. 10),
  poteri sostitutivi (art. 11), glossario (art. 2).

Normative collegate **citate ma non trascritte** (non riprodotte dal
D.P.R., per il testo letterale rinvio a Normattiva):

- D.Lgs. 152/2006 (Codice Ambiente): artt. 19, 20, 26, 108, 112, 208,
  215, 216, 269, 272, 281, Allegato VIII Parte II.
- L. 447/1995 (legge quadro inquinamento acustico): art. 8 co. 4 e 6.
- L. 241/1990: artt. 2, 14, 14-ter, 14-quinquies.
- D.P.R. 160/2010 (SUAP): artt. 2, 7.
- D.Lgs. 101/2020 (radiazioni ionizzanti): artt. 24, 26.
- D.Lgs. 99/1992 (fanghi in agricoltura): art. 9.
- DM 18 aprile 2005 (definizione PMI): art. 2.

## Articoli e punti chiave

- **art. 1 co. 1**: ambito AUA = PMI + impianti non-AIA.
- **art. 1 co. 2**: esclusione per progetti VIA con effetto assorbente
  (art. 26 co. 4 D.Lgs. 152/2006).
- **art. 2 co. 1**: definizioni (AUA, autorita' competente, gestore,
  SUAP, modifica sostanziale).
- **art. 3 co. 1 lett. a-g, g-bis, g-ter**: i 9 titoli incorporati.
  Lett. g-bis e g-ter aggiunte dall'art. 72 co. 1 D.Lgs. 203/2022
  (radiazioni ionizzanti).
- **art. 3 co. 2**: ampliamento regionale del perimetro.
- **art. 3 co. 3**: facolta' di non avvalersi dell'AUA per attivita'
  soggette solo a comunicazione o autorizzazione generale.
- **art. 3 co. 6**: durata 15 anni.
- **art. 4 co. 3**: 30 giorni verifica formale.
- **art. 4 co. 4**: 90 giorni se tutti i titoli ≤ 90 gg.
- **art. 4 co. 5**: 120 giorni con CdS, 150 giorni con integrazione
  ex art. 14-ter co. 8 L. 241/1990.
- **art. 5 co. 1**: rinnovo 6 mesi prima della scadenza.
- **art. 5 co. 4**: continuita' esercizio nelle more se istanza nei
  termini.
- **art. 5 co. 5**: rinnovo/revisione anticipata d'ufficio.
- **art. 6 co. 1**: comunicazione modifica + 60 gg silenzio-assenso.
- **art. 6 co. 2**: nuova domanda ex art. 4 per modifica sostanziale ex
  ante.
- **art. 6 co. 3**: 30 gg per riqualificazione modifica sostanziale.
- **art. 7**: autorizzazioni di carattere generale ex art. 272 D.Lgs.
  152/2006.
- **art. 8**: oneri istruttori.
- **art. 10 co. 1-2**: transitorie (passaggio ad AUA alla scadenza del
  primo titolo sostituito).
- **art. 11 co. 1**: poteri sostitutivi via L. 241/1990 art. 2 co. 9-bis.

## Convenzioni specifiche

### Cosa NON fare

- **Non determinare AIA o VIA**: la skill copre solo l'AUA. Per AIA e
  VIA assorbente rinviare a strumenti dedicati e al D.Lgs. 152/2006.
- **Non calcolare** portate scarichi, bilanci di massa emissivi, valori
  acustici predittivi, classificazione CER, dosi efficaci radiazioni:
  sono di competenza tecnica di settore.
- **Non inventare moduli regionali**: la skill non distribuisce
  modulistica; rinviare al SUAP e al sito istituzionale della Regione
  o Provincia Autonoma.
- **Non interpretare** giurisprudenza TAR/CdS o prassi delle ARPA: la
  skill e' source-grounded sul testo del regolamento, non sulla prassi.
- **Non confondere** modifica sostanziale ex art. 6 (di un'AUA in essere)
  con la disciplina della "modifica sostanziale" AIA (art. 5 co. 1 lett.
  l-bis del D.Lgs. 152/2006): sono regimi distinti.

### Cosa fare

- **Citare sempre articolo e comma** del D.P.R. 59/2013 a fianco di ogni
  affermazione normativa (es. "art. 4 co. 5"). Per le norme collegate
  citare l'atto con numero e articolo (es. "art. 26 co. 4 D.Lgs.
  152/2006").
- **Rinviare al SUAP e all'autorita' competente** per ogni decisione
  formale. La skill produce report di autoverifica, non istanze pronte.
- **Ricordare il limite regionale**: l'art. 3 co. 2 autorizza ampliamenti
  del perimetro AUA da parte di Regioni e Province Autonome. La skill
  non conosce le discipline regionali: invitare l'utente a verificare.
- **Strutturare l'output come report Markdown** con sezioni numerate,
  in modo che l'utente possa inserirlo come allegato tecnico alla propria
  istruttoria interna.
- **Chiudere con un'Avvertenza** che ricordi: (1) la skill non sostituisce
  il professionista firmatario; (2) la determinazione formale e' del
  SUAP/autorita' competente; (3) la normativa regionale puo' modificare
  termini e perimetro.

## Validatori

- Validatori Livello 2 e Livello 3 da identificare per la fase di
  promozione oltre la versione alpha (vedi `methodology/validazione.md`).

## Stato attuale

- Versione: vedi `CHANGELOG.md` (0.1.0-alpha)
- Validazione: Livello 1 (validate.sh) in corso. Livello 2 e 3 non
  ancora effettuati.
- Task files: 5 (`check-applicabilita.md`, `mappa-titoli-art3.md`,
  `pianifica-termini.md`, `pianifica-rinnovo.md`,
  `triage-modifica-art6.md`).
- Esempi: 1 conforme + 1 problematico in `examples/`.
