# Output atteso - obbligo di rilascio del gestionale

## 1. Siete obbligati? (art. 69 C.A.D.)

Sì. Il software è stato **realizzato su specifiche indicazioni del committente pubblico**
(il Comune) e il Comune ne è **titolare**: scatta l'**obbligo** di **rendere disponibile
il codice sorgente completo di documentazione**, **in repertorio pubblico**, **sotto
licenza aperta**, in **uso gratuito** ad altre PA o soggetti che intendano adattarlo
(art. 69, c. 1). Eccezioni solo per motivate ragioni di **ordine e sicurezza pubblica,
difesa nazionale, consultazioni elettorali**.

## 2. Cosa pubblicare (Linee guida AgID, Allegato A)

1. **Licenza aperta**: scegliere e attribuire la licenza; indicare come detentore del
   copyright l'**Amministrazione committente** (il Comune).
2. **Repository** su uno strumento di code hosting, con struttura chiara.
3. **README.md** (A.7 - MUST): titolo/sottotitolo, descrizione e casi d'uso,
   prerequisiti/dipendenze, istruzioni di installazione, stato del progetto, detentori del
   copyright, manutentori, **e-mail per segnalazioni di sicurezza** (non via issue tracker).
4. **Documentazione tecnica** (A.8 - MUST): installazione, build, produzione,
   architettura, in **formato versionabile riga per riga** (HTML, Markdown, reST, LaTeX) —
   **niente ODT/DOCX/PDF**.
5. **`publiccode.yml`** nella **root** del repository e **registrazione su Developers
   Italia** (A.11) per l'indicizzazione nel catalogo.

## 3. In quanto tempo (A.9)

- Se **non** si adotta il **modello di sviluppo aperto** (rilascio contestuale allo
  sviluppo), il rilascio deve avvenire **entro 15 giorni** dall'acquisizione del software
  al termine della lavorazione (o dalla messa in collaudo/produzione, o da richiesta
  dell'Amministrazione); se a lotti, per **ciascun lotto**.

## 4. Sintesi

- **Obbligo** di rilascio (art. 69) del codice + documentazione, licenza aperta, uso
  gratuito ad altre PA.
- Pubblicare README + documentazione (formati ammessi) + `publiccode.yml`; registrare su
  Developers Italia; rispettare i **15 giorni** se non c'è sviluppo aperto.

> La skill inquadra obblighi e contenuti; la **scelta della licenza** e la validazione
> restano del Comune. **Non sostituisce** il RTD né il consulente legale.
