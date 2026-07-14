# AGENTS.md - bonifica-siti-contaminati-dlgs152

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **procedura di bonifica dei siti contaminati** (Parte
quarta Titolo V del D.Lgs. 152/2006): definizioni (CSC, CSR, sito contaminato,
MISE, MISO, bonifica), procedura operativa del responsabile, procedimento su
iniziativa della PA, aree di ridotte dimensioni, sanzioni. Target: tecnici
ambientali, gestori, uffici regione/provincia/comune/ARPA.

**E' una skill documentale**: non legge i valori CSC, non esegue l'analisi di
rischio, non redige il piano di caratterizzazione ne' il progetto di bonifica.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-152-2006**: D.Lgs. 3/4/2006 n. 152 (TUA), testo multivigente su
  Normattiva. Binario = pagina indice pinnata `!vig=2026-07-14` (hash stabile
  af54f5e0..., pattern della skill aua-dpr59-dossier). Articoli 240 (v. 2), 242
  (v. 11), 244 (v. 3), 249, 257 (v. 2) letti via AJAX (caricaArticolo) e
  trascritti verbatim in `references/fonti/dlgs-152-2006.md`.

Estratto operativo: `references/estratti/bonifica-siti-checklist.md`.

## Punti chiave (verificati sul testo)

- **CSC** (art. 240 lett. b): valori dell'**Allegato 5**, soglia di ingresso alla
  procedura. **CSR** (lett. c): livelli di accettabilita' sito specifici
  determinati con l'**analisi di rischio** (Allegato 1).
- **Sito potenzialmente contaminato** = superate le CSC (lett. d); **sito
  contaminato** = superate le **CSR** (lett. e); **non contaminato** = sotto CSC
  o sotto CSR (lett. f).
- **Procedura (art. 242)**: prevenzione **24 ore** (c. 1); se sotto CSC ->
  autocertificazione **48 ore** (c. 2); se sopra CSC -> notizia + piano di
  caratterizzazione **30 giorni**, autorizzazione regione **30 giorni** (c. 3);
  analisi di rischio, risultati **6 mesi**, approvazione **60 giorni** (c. 4);
  esito < CSR chiusura / >= CSR progetto di bonifica (c. 5).
- **PA (art. 244)**: comunicazione a regione/provincia/comune (c. 1); provincia
  **diffida con ordinanza** il responsabile (c. 2), notificata al proprietario
  (c. 3); se nessuno provvede, interviene l'amministrazione (art. 250).
- **Aree ridotte (art. 249)**: procedure semplificate Allegato 4.
- **Sanzioni (art. 257)**: superamento CSR senza bonifica conforme arresto 6
  mesi-1 anno o ammenda 2.600-26.000; mancata comunicazione arresto 3 mesi-1 anno
  o ammenda 1.000-26.000; sostanze pericolose 1-2 anni e 5.200-52.000; osservanza
  progetti = non punibilita' (c. 4).

## Convenzioni specifiche

### Cosa NON fare
- Non riprodurre i **valori CSC** (Allegato 5), non calcolare le **CSR** (analisi
  di rischio, Allegato 1), non redigere caratterizzazione/progetti.
- Non confondere **CSC** (soglia normativa) e **CSR** (soglia sito specifica);
  non confondere **potenzialmente contaminato** (CSC) e **contaminato** (CSR).
- Non citare a memoria termini/sanzioni: citare l'articolo (240, 242, 244, 249,
  257).
- Non trattare i **SIN** (art. 252) come se fossero procedura ordinaria.

### Cosa fare
- Seguire la sequenza dei termini dell'art. 242 e citarli esatti.
- Distinguere il ramo sotto-CSC (chiusura rapida) dal ramo pieno.
- Indicare gli attori (responsabile, comune, provincia, regione, conferenza di
  servizi) e il ramo PA (art. 244).
- Chiudere con il rinvio agli allegati e ai tecnici/autorita' competenti.

## Aggiornamento della fonte Normattiva

Testo multivigente (TUA, molto emendato): se si aggiorna la skill, ri-pinnare la
URL a nuova `!vig=YYYY-MM-DD`, riscaricare la pagina indice (nuovo hash) e
rileggere via AJAX gli articoli modificati (usare le versioni piu' alte:
attualmente art. 242 v. 11, art. 244 v. 3, art. 240/257 v. 2).

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con tecnico ambientale/geologo).

## Stato attuale

- Versione: 0.1.0-alpha (closes #62)
- Task files: 2 (`diagnosi-procedura.md`, `checklist-adempimenti.md`)
- Esempi: 2 (sversamento sotto CSC; superamento CSC in area dismessa)
