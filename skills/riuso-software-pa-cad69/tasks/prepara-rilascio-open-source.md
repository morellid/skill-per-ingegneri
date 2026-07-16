# Task: prepara-rilascio-open-source

Struttura il **rilascio in open source** del software della PA ai sensi dell'**art. 69
C.A.D.** e delle **Linee guida AgID** (Allegato A).

## Input richiesti

- Software da rilasciare e sua **titolarita'** (realizzato su specifiche del committente
  pubblico?).
- Strumento di **code hosting** e organizzazione della PA.

## Procedura

1. **Verifica dell'obbligo** (art. 69): se la PA e' titolare di software realizzato su
   specifiche del committente pubblico, sussiste l'obbligo di rilascio (salvo eccezioni:
   ordine/sicurezza pubblica, difesa, elezioni).
2. **Licenza aperta**: scegliere e **attribuire** la licenza; individuare la titolarita'
   (copyright dell'Amministrazione committente).
3. **README.md** (A.7): compilare i contenuti **MUST** (titolo/sottotitolo, descrizione e
   casi d'uso, prerequisiti/dipendenze, istruzioni di installazione, stato del progetto,
   detentori del copyright, manutentori, **e-mail per segnalazioni di sicurezza**).
4. **Documentazione** (A.8): allegare la documentazione tecnica (installazione,
   build, produzione, architettura) in **formato versionabile riga per riga** (HTML,
   Markdown, reStructuredText, LaTeX); **ODT/DOCX/PDF non ammessi**.
5. **Tempi** (A.9): se non si adotta il modello di **sviluppo aperto**, rilasciare **entro
   15 giorni** dall'acquisizione/collaudo/produzione (per ciascun lotto).
6. **Registrazione su Developers Italia** (A.11): pubblicare il file **`publiccode.yml`**
   nella **root** del repository (formato: https://github.com/italia/publiccode.yml) e
   registrare l'organizzazione di code-hosting.

## Output atteso

- Checklist del rilascio: licenza, README (voci MUST), documentazione (formati),
  scadenza dei 15 giorni, `publiccode.yml` + registrazione su Developers Italia.

## Avvertenze

- La **scelta e validazione della licenza** e la compilazione **campo-per-campo** del
  `publiccode.yml` restano dell'Amministrazione/fornitore (rinvio al formato ufficiale).
- La skill struttura obblighi e contenuti; **non redige** il codice ne' la documentazione.
