# AGENTS.md - verifiche-periodiche-ascensori-dpr162

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'iter di **esercizio, verifiche periodiche/straordinarie
e manutenzione degli ascensori** (montacarichi e assimilati <= 0,15 m/s) ai sensi
del DPR 162/1999, artt. 12-16. Target: proprietari/amministratori di condominio,
ingegneri, ditte di manutenzione, tecnici della sicurezza.

**E' una skill documentale**: non copre l'immissione sul mercato/marcatura CE
(artt. 1-11), non definisce regole tecniche di installazione (UNI EN), non calcola
le date delle scadenze.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-162-1999**: D.P.R. 30/4/1999 n. 162, testo multivigente su Normattiva.
  Binario = pagina indice pinnata `!vig=2026-07-14` (hash stabile ad0fc818...,
  pattern della skill aua-dpr59-dossier). Articoli 12-16 letti via AJAX
  (caricaArticolo) e trascritti verbatim in `references/fonti/dpr-162-1999.md`.

Estratto operativo: `references/estratti/verifiche-ascensori-checklist.md`.

## Punti chiave (verificati sul testo)

- **Messa in esercizio** (art. 12): comunicazione al comune **entro 60 giorni**
  dalla dichiarazione di conformita' (con ditta di manutenzione DM 37/2008 e
  soggetto delle verifiche periodiche); **matricola entro 30 giorni**; oltre 60
  giorni -> verbale di verifica straordinaria di attivazione; divieto di esercizio
  senza comunicazione -> sospensione del servizio.
- **Verifica periodica** (art. 13): **ogni 2 anni**; soggetti: ASL/ARPA, ITL
  (stabilimenti industriali/agricoli), MIT (pubblico trasporto), organismi
  notificati, **organismi di ispezione di tipo A accreditati** (UNI CEI EN ISO/IEC
  17020, ACCREDIA); verbale al proprietario e manutentore; esito negativo ->
  comune. Spese a carico del proprietario.
- **Verifica straordinaria** (art. 14): dopo esito negativo (fermo fino a
  straordinaria favorevole), incidente di notevole importanza (fermo immediato),
  modifiche costruttive.
- **Manutenzione** (art. 15): ditta/persona abilitata (certificato del prefetto /
  DM 37/2008); controlli **almeno ogni 6 mesi (ascensori) / 1 anno (montacarichi)**
  su paracadute, limitatore, funi, isolamento; annotazione sul libretto; pericolo
  in atto -> fermo.
- **Libretto e targa** (art. 16): libretto con verbali/visite/dichiarazioni;
  targa con soggetto verifiche, matricola, portata.

## Convenzioni specifiche

### Cosa NON fare
- Non trattare l'immissione sul mercato / marcatura CE dei componenti (artt.
  1-11): fuori scope.
- Non definire regole tecniche (UNI EN 81) ne' calcolare parametri.
- Non citare i termini "a memoria": citare sempre l'articolo (12-16).
- Non confondere i soggetti verificatori per contesto (condominio: ASL/ARPA o
  organismo di tipo A; industria: ITL; pubblico trasporto: MIT).
- Non calcolare le date concrete delle scadenze al posto dell'utente.

### Cosa fare
- Citare l'articolo preciso per ogni obbligo/periodicita'.
- Applicare la regola sul soggetto verificatore in base al contesto.
- Segnalare il rischio di sospensione del servizio in caso di inosservanza.
- Chiudere con il rinvio a proprietario, manutentore e soggetto verificatore.

## Aggiornamento della fonte Normattiva

Testo multivigente: se si aggiorna la skill, ri-pinnare la URL a nuova
`!vig=YYYY-MM-DD`, riscaricare la pagina indice (nuovo hash) e rileggere via AJAX
gli articoli modificati.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con tecnico verificatore / ditta
  di manutenzione ascensori).

## Stato attuale

- Versione: 0.1.0-alpha (closes #43)
- Task files: 2 (`diagnosi-adempimenti.md`, `checklist-esercizio.md`)
- Esempi: 2 (nuovo ascensore condominiale - messa in esercizio; verifica periodica
  con esito negativo - fermo e straordinaria)
