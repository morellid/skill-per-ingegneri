# AGENTS.md - mog-231-reati-ambientali

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **parte speciale ambientale** del Modello di
Organizzazione, Gestione e Controllo (MOG) ex D.Lgs 231/2001: mappatura dei reati
presupposto ambientali (art. 25-undecies) e struttura dei controlli (artt. 6-7).
Target: HSE/ingegneri ambientali, compliance officer, membri dell'Organismo di
Vigilanza.

**E' una skill documentale di compliance** (come le altre skill normative del repo
- GDPR, NIS2, DORA, Seveso, ADR): non redige il Modello, non riproduce il testo dei
singoli reati e non effettua la valutazione legale.

## Nota sull'area di catalogo

Collocata in **ambiente-territorio-mobilita** (dominio ambientale), coerentemente
con la scelta del repo di catalogare le skill di compliance per **dominio** (es.
GDPR/NIS2/DORA in software-dati-cybersecurity). La parte speciale ambientale del
231 riguarda scarichi, rifiuti, emissioni e bonifiche, gia' coperti come aspetti
tecnici dalle skill ambientali del repo, di cui questa e' il complemento sul
versante della responsabilita' dell'ente.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-231-2001**: D.Lgs 231/2001, pagina indice Normattiva pinnata a
  `!vig=2026-07-15` (hash 73e26d0e...). Artt. 6, 7 e 25-undecies caricati via AJAX
  (caricaArticolo) e trascritti verbatim in `references/fonti/dlgs-231-2001.md`.

Estratto operativo: `references/estratti/reati-ambientali-231-mappa.md`.

## Punti chiave (verificati sul testo)

- **Art. 25-undecies** enumera i reati presupposto ambientali e le sanzioni:
  ecoreati del c.p. (452-bis inquinamento, 452-quater disastro, 452-quinquies
  colposi, 452-sexies materiale radioattivo, 452-octies associazione, 452-terdecies
  omessa bonifica, 452-quaterdecies traffico organizzato rifiuti, 727-bis, 733-bis);
  D.Lgs 152/2006 (art. 137 scarichi, 256/256-bis rifiuti, 257 bonifica, 258/259/
  260-bis tracciabilita', 279 emissioni); L. 150/1992 (CITES); L. 549/1993 (ozono);
  D.Lgs 202/2007 (navi). Sanzioni **a quote** + **interdittive** (art. 9) +
  **interdizione definitiva** (art. 16, c. 3) per i casi piu' gravi.
- **Art. 6**: funzione esimente; esigenze del modello (attivita' a rischio,
  protocolli, gestione risorse, flussi OdV, sistema disciplinare, whistleblowing);
  OdV; enti piccoli / societa' di capitali.
- **Art. 7**: soggetti sottoposti all'altrui direzione.

## Convenzioni specifiche

### Cosa NON fare
- Non riprodurre ne' interpretare il **testo dei singoli reati** (c.p.; D.Lgs
  152/2006; L. 150/1992; L. 549/1993; D.Lgs 202/2007): citarli per numero.
- Non redigere il **Modello 231** ne' i protocolli operativi.
- Non effettuare la **valutazione legale** della responsabilita' ne' quantificare le
  sanzioni (la quota la fissa il giudice).

### Cosa fare
- Mappare i reati presupposto ambientali applicabili all'ente e le sanzioni.
- Strutturare la parte speciale (artt. 6-7): attivita' a rischio, protocolli, flussi
  OdV, sistema disciplinare.
- Rinviare, per gli aspetti tecnici, alle skill ambientali del repo
  (scarichi/emissioni, rifiuti/FIR, bonifica).

## Aggiornamento della fonte

Normattiva: riscaricare la pagina indice pinnata a un nuovo `!vig=` (nuovo hash) e
rileggere l'art. 25-undecies (frequentemente novellato: da ultimo D.L. 116/2025 e L.
91/2025) e gli artt. 6-7.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con legale 231 / esperto compliance
  ambientale).

## Stato attuale

- Versione: 0.1.0-alpha (closes #63)
- Task files: 2 (`mappa-reati-presupposto.md`, `struttura-parte-speciale.md`)
- Esempi: 2 (gestione rifiuti art. 256; scarichi industriali art. 137 ed esimente)
