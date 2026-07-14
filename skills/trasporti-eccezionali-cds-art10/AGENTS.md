# AGENTS.md - trasporti-eccezionali-cds-art10

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al regime dei **veicoli e trasporti eccezionali** ai sensi
dell'**art. 10 del Codice della Strada** (D.Lgs. 285/1992): inquadramento, obbligo
e tipo di autorizzazione, ente competente, prescrizioni, sanzioni. Target:
imprese di autotrasporto, vettori, consulenti, uffici degli enti proprietari/
concessionari.

**E' una skill documentale**: non calcola i limiti di sagoma/massa, non individua
nel merito l'ente/il percorso, non redige la domanda ne' riproduce le Linee guida
MIT.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-285-1992**: D.Lgs. 30/4/1992 n. 285 (Codice della Strada), art. 10, testo
  multivigente su Normattiva. Binario = pagina indice pinnata `!vig=2026-07-14`
  (hash stabile fbc10b72..., pattern della skill aua-dpr59-dossier). L'art. 10
  (versione 37) e' letto via AJAX (caricaArticolo) e trascritto verbatim in
  `references/fonti/dlgs-285-1992.md`.

Estratto operativo: `references/estratti/trasporti-eccezionali-checklist.md`.

## Punti chiave (verificati sul testo)

- **Eccezionalita'** (art. 10 c. 1-2): veicolo che supera **sagoma (art. 61)** o
  **massa (art. 62)**; trasporto di cose indivisibili fuori sagoma (c. 2 lett. a)
  o generi tipizzati eccedenti congiuntamente (c. 2 lett. b, massa fino a
  38/48/86/108 t secondo gli assi).
- **Autorizzazione** (c. 6): obbligatoria; rilasciata dall'**ente proprietario o
  concessionario** (autostrade/statali/militari) o dalle **regioni** (restante
  rete). Non prescritta entro i limiti (c. 11); mai per i motoveicoli (c. 15).
- **Tipi** (c. 9): **singola** (volta per volta), **multipla** (piu' transiti),
  **periodica** (periodi di tempo); periodica semplificata per i ripetitivi
  (c. 2-bis).
- **Presupposti** (c. 10): compatibilita' con conservazione strade, stabilita'
  manufatti, sicurezza; **oneri** a carico del richiedente (c. 17).
- **Sanzioni** (c. 18-25): senza autorizzazione **794-3.206 euro** (c. 18); senza
  prescrizioni **159-641** (c. 19); senza documento a bordo **42-173** (c. 20);
  mezzi d'opera / eccedenza massa **430-1.731** (c. 21-22); solidarieta'
  proprietario/committente (c. 23); sospensione patente (c. 24).

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** i limiti di sagoma/massa: rinviare agli artt. 61 e 62.
- Non individuare nel merito l'**ente competente** o il **percorso**.
- Non redigere la domanda; non riprodurre le **Linee guida MIT** (2022) ne' il
  decreto del comma 10-bis.
- Non citare a memoria importi/sanzioni: citare il comma dell'art. 10.

### Cosa fare
- Distinguere **veicolo eccezionale** (c. 1) e **trasporto eccezionale** (c. 2).
- Verificare prima se si superano i limiti (art. 61/62), poi l'obbligo e il tipo
  di autorizzazione.
- Citare il comma per obblighi, tipi, presupposti e sanzioni.

## Aggiornamento della fonte Normattiva

Testo multivigente (art. 10 molto emendato, versione 37): se si aggiorna la skill,
ri-pinnare la URL a nuova `!vig=YYYY-MM-DD`, riscaricare la pagina indice (nuovo
hash) e rileggere via AJAX l'art. 10 (verificare la versione piu' alta).

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con esperto di autotrasporto).

## Stato attuale

- Versione: 0.1.0-alpha (closes #66)
- Task files: 2 (`inquadra-eccezionalita.md`, `checklist-autorizzazione.md`)
- Esempi: 2 (trave prefabbricata fuori sagoma; autoarticolato entro i limiti)
