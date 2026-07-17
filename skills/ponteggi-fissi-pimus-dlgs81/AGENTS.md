# AGENTS.md - ponteggi-fissi-pimus-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **tecnico** (ingegnere/architetto/geometra), all'**impresa/datore di lavoro** e
al **preposto** per i **ponteggi fissi** a elementi portanti prefabbricati e per il **Pi.M.U.S.**:
quando serve il **progetto** firmato, quale **documentazione** tenere in cantiere, come inquadrare il
**Pi.M.U.S.**, la **sorveglianza** del preposto e la **formazione** degli addetti, ai sensi del **D.Lgs.
9 aprile 2008, n. 81, Titolo IV, Capo II, Sezione V, artt. 131-138**.

**E' una skill documentale per il tecnico**: inquadra obblighi, soggetti e contenuti; **non redige** il
progetto/relazione/Pi.M.U.S., **non esegue** il calcolo di resistenza e stabilita', **non rilascia**
l'autorizzazione ministeriale.

## Nota sull'area e sulla complementarita'

Area **sicurezza-lavoro-cantieri**. Complementare a `pos-allegato-xv-checker` e a
`coordinatori-sicurezza-cantieri-dlgs81` (POS/PSC e coordinamento nel Titolo IV), a
`dispositivi-protezione-individuale-dlgs81` (DPI anticaduta) e a `segnaletica-salute-sicurezza-dlgs81`
(segnaletica di pericolo richiamata dall'art. 136 c. 5). Specifica per la **Sezione V (Ponteggi
fissi)**: non copre i ponteggi in legno, i ponti su cavalletti e le altre opere provvisionali della
Sezione IV se non nei richiami (artt. 125-126).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-131-138**: D.Lgs. 81/2008, pagina indice Normattiva pinnata a `!vig=2026-07-17`
  (hash `18fbc542...`; codice 008G0104, idGruppo 23). Artt. 131 (v2), 132 (v1), 133 (v1), 134 (v1),
  135 (v1), 136 (v2), 137 (v2), 138 (v2) caricati via `caricaArticolo` (formato AKN) e trascritti
  verbatim.

Trascrizione in `references/fonti/dlgs-81-2008-131-138.md`; estratto operativo in
`references/estratti/ponteggi-checklist.md`.

## Punti chiave (verificati sul testo)

- **Progetto** (art. 133): dovuto per ponteggi **> 20 m**, per configurazioni **fuori schema-tipo** o
  per **opere provvisionali** di notevole importanza e complessita'; **calcolo + disegno esecutivo**
  **firmati da ingegnere/architetto abilitato** (c. 2). Copie in cantiere (c. 3).
- **Esenzione dal calcolo** entro **schema-tipo** (artt. 132 c. 1 lett. g, 134 c. 2); modifiche subito
  sul disegno.
- **Documentazione** (art. 134): autorizzazione + progetto/disegni + **Pi.M.U.S.** (lavori in quota,
  Allegato XXII), esibiti agli organi di vigilanza.
- **Pi.M.U.S.** (art. 136): redatto dal **datore di lavoro a mezzo di persona competente**; sorveglianza
  del **preposto**; **formazione** teorico-pratica (Allegato XXI).
- **Autorizzazione ministeriale** al fabbricante con **relazione tecnica** (artt. 131-132), rinnovo
  decennale, marchio (art. 135); **manutenzione**/revisione del preposto (art. 137); **norme
  particolari** su parapetto 95 cm, fermapiede 15 cm, distacco tavole 20 cm (art. 138).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** il progetto, la relazione tecnica o il **Pi.M.U.S.**; non **eseguire** il calcolo di
  resistenza e stabilita'; non **rilasciare** l'autorizzazione ministeriale.
- Non riprodurre gli **Allegati XVIII/XIX/XXI/XXII** ne' le norme **UNI EN 12810/12811/74**: rinvio.
- Non confondere l'esenzione dal **calcolo** (schema-tipo) con l'esenzione dal **Pi.M.U.S.** (sempre
  dovuto per i lavori in quota).

### Cosa fare
- Stabilire se serve il progetto firmato (art. 133) o vale lo schema-tipo; elencare la documentazione di
  cantiere (art. 134); inquadrare Pi.M.U.S., sorveglianza e formazione (art. 136).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 81/2008 pinnato a nuovo `!vig=` (nuovo hash) e rileggere gli
artt. 131-138, verificando le modifiche dei doppi tondi `(( ))` (es. D.Lgs. 106/2009 su artt. 131, 136,
137, 138).

## Validatori

- Non ancora assegnato (Livello 2 con RSPP/coordinatore o esperto ponteggi).

## Stato attuale

- Versione: 0.1.0-alpha (closes #352)
- Task files: 2 (`inquadra-progetto-documentazione.md`, `inquadra-pimus-montaggio.md`)
- Esempi: 2 (ponteggio > 20 m e fuori schema: progetto firmato; ponteggio a schema-tipo in quota:
  Pi.M.U.S., sorveglianza e formazione)
