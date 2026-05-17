# AGENTS.md - rsia-audit-stradale-dlgs35

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto alle quattro procedure di gestione della sicurezza delle infrastrutture stradali previste dal D.Lgs 15 marzo 2011, n. 35 nel testo modificato dal D.Lgs 15 novembre 2021, n. 213 (recepimento della Direttiva UE 2019/1936 che modifica la Direttiva 2008/96/CE): Valutazione di Impatto sulla Sicurezza Stradale (VISS), Controlli di Sicurezza Stradale (RSA), Valutazione di Sicurezza a Livello di Rete (NSA, introdotta dal recepimento 2021), ispezioni periodiche e mirate. Target utenti: controllori della sicurezza stradale iscritti nell'elenco MIMS, ingegneri stradali, tecnici dell'organo competente, concessionari autostradali.

## Fonti autoritative

Tutte catalogate in `references/sources.yaml`. Tre fonti scaricate e convertite in markdown, una in riferimento strutturale:

- **D.Lgs 35/2011** - hash `1f8b66d3c2ff5d2dfeb54df09bdde5c02b7d97b65c30a0db94d38b7caaee72fd`. Testo originale di recepimento della Direttiva 2008/96/CE.
- **D.Lgs 213/2021** - hash `29add9f98e6669b3c439cdb90f8740e7edde80213c274fc2c285bca647b06efc`. Modifiche al D.Lgs 35/2011, recepimento Direttiva UE 2019/1936.
- **Direttiva 2008/96/CE** - hash `7a5b6f3e6f58ed7db3c8fd30416e0349dc5276dce14217c27f132a51b06d634e`. Atto-quadro UE, testo italiano da MIT.
- **Direttiva (UE) 2019/1936** - solo riferimento strutturale (CELEX 32019L1936), il contenuto sostanziale e' applicato attraverso il D.Lgs 213/2021.

Estratti pertinenti gia' preparati in `references/estratti/`:
- `dlgs-35-2011.md` - articoli e allegati del testo originale, con NOTE che indicano cosa il D.Lgs 213/2021 ha modificato.
- `dlgs-213-2021.md` - articoli 1-15 del decreto di modifica, una tabella riepilogativa finale articolo per articolo.
- `dir-2008-96-ce.md` - articoli e allegati della direttiva quadro UE.

## Articoli e punti chiave

L'agente, quando produce output, deve citare il riferimento preciso (articolo, comma, allegato, punto). Mai "la legge in generale".

- **Art. 1 D.Lgs 35/2011 (nuovo testo art. 1 D.Lgs 213/2021)**: ambito applicazione - rete TEN-T, autostrade, strade principali, strade UE-finanziate, rete nazionale dal 2025.
- **Art. 2 D.Lgs 35/2011**: definizioni (lett. a-bis autostrada, a-ter strada principale, a-quater strade interesse nazionale, f classificazione sicurezza, g ispezione mirata, g-bis ispezione periodica, i-bis utenti vulnerabili - tutte modificate o introdotte dal D.Lgs 213/2021).
- **Art. 3 D.Lgs 35/2011**: VISS, non modificato direttamente dal D.Lgs 213/2021.
- **Art. 4 D.Lgs 35/2011**: RSA (controlli), comma 7 incompatibilita' assoluta del controllore. Non modificato direttamente dal D.Lgs 213/2021.
- **Art. 5 D.Lgs 35/2011 (nuovo testo art. 3 D.Lgs 213/2021)**: NSA - valutazione a livello di rete, prima entro 2024, quinquennale, classificazione in almeno 3 categorie.
- **Art. 6 D.Lgs 35/2011 (modificato art. 4 D.Lgs 213/2021)**: ispezioni periodiche almeno ogni 5 anni; ispezioni congiunte gallerie almeno ogni 6 anni (comma 2-bis).
- **Art. 6-bis (inserito art. 5 D.Lgs 213/2021)**: seguito procedure - ispezioni mirate e interventi correttivi, piano d'azione quinquennale.
- **Art. 6-ter**: protezione utenti vulnerabili.
- **Art. 6-quater**: segnaletica leggibile anche per ADAS.
- **Art. 6-quinquies**: AINOP come sistema segnalazioni spontanee.
- **Art. 7 D.Lgs 35/2011**: dati incidenti, ANSFISA sovrintende.
- **Art. 9 D.Lgs 35/2011**: formazione controllori (180 ore iniziali, aggiornamento triennale 30 ore); comma 1-bis (inserito art. 7 D.Lgs 213/2021) sui contenuti utenti vulnerabili dal 17/12/2024.
- **Art. 9-bis (inserito art. 8 D.Lgs 213/2021)**: rendicontazione quinquennale alla Commissione UE.
- **Art. 12 c. 4**: regime transitorio (10 anni albo + 5 progetti documentati).
- **Allegato I D.Lgs 35/2011**: VISS, 8 componenti + 5 elementi, titolo e punto 2 lett. e modificati dall'art. 10 D.Lgs 213/2021.
- **Allegato II D.Lgs 35/2011**: RSA, 4 fasi, titolo e contenuti modificati dall'art. 11 D.Lgs 213/2021 (PFTE sostituisce progettazione preliminare, lettera d-bis utenti vulnerabili).
- **Allegato II-bis (inserito art. 12 D.Lgs 213/2021)**: 9 macro-categorie per ispezioni mirate.
- **Allegato III D.Lgs 35/2011 (sostituito art. 13 D.Lgs 213/2021)**: 11 macro-categorie per NSA.
- **Allegato IV D.Lgs 35/2011**: 9 elementi relazione incidente, GNSS e gravita' modificati dall'art. 14 D.Lgs 213/2021.

## Convenzioni specifiche

### Cosa NON fare

- Non dare per scontato che la strada sia in ambito di applicazione. Eseguire sempre `check-ambito-applicazione.md` prima di qualunque altra procedura.
- Non confondere VISS (Art. 3, pianificazione iniziale) con RSA (Art. 4, fasi progettuali e prima funzionamento) ne' con NSA (Art. 5, rete in esercizio). Sono tre procedure distinte con tempi, oggetti e attori diversi.
- Non saltare la verifica di indipendenza del controllore (art. 4 c. 7 D.Lgs 35/2011, art. 9 par. 4 lett. c Direttiva 2008/96/CE). E' un principio non derogabile.
- Non citare il vecchio art. 5 D.Lgs 35/2011 sulla "classificazione dei tratti ad elevata concentrazione di incidenti": e' stato integralmente sostituito dal D.Lgs 213/2021. Citare il nuovo testo della NSA.
- Non citare il vecchio Allegato III: e' stato sostituito.
- Non produrre output con TODO, FIXME, "lorem ipsum", "da completare". La skill produce bozze tecniche complete, anche minimali.

### Cosa fare

- Citare sempre articolo, comma, lettera. Es. "art. 4, comma 7 D.Lgs 35/2011" e non "ai sensi del D.Lgs 35/2011".
- Quando una norma e' modificata dal D.Lgs 213/2021, riferirsi al "testo modificato" o "nuovo testo" e indicare anche l'articolo del decreto modificativo.
- Strutturare l'output secondo le componenti/criteri dell'allegato pertinente (I per VISS, II per RSA, II-bis per ispezioni mirate, III per NSA, IV per relazione incidenti).
- Chiudere l'output con riferimento alla firma del professionista qualificato e (dove applicabile) alla trasmissione all'organo competente o all'ANSFISA.
- Per le strade in galleria, ricordare l'esclusione D.Lgs 264/2006 e il regime delle ispezioni congiunte (art. 6, comma 2-bis).

## Validatori

- [Da identificare] - controllore della sicurezza stradale iscritto all'elenco MIMS, per Livello 2 di validazione.

## Stato attuale

- Versione: vedi `CHANGELOG.md` (0.1.0-alpha).
- Validazione: Livello 1 (autore: Claude Opus 4.7).
- Task files: `check-ambito-applicazione.md`, `draft-viss.md`, `draft-rsa.md`, `draft-nsa.md`, `verifica-requisiti-controllore.md`.
- Esempi: 1 conforme (`01-rsa-pfte-conforme`) + 1 problematico (`02-rsa-controllore-non-idoneo`).
