# AGENTS.md - diagnosi-energetica-dlgs102

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'**obbligo di diagnosi energetica** delle grandi imprese e
delle imprese a forte consumo di energia (art. 8 D.Lgs. 102/2014, attuazione dir.
2012/27/UE). Target: energy manager, EGE, ESCo, consulenti energetici, imprese
obbligate.

**E' una skill documentale**: non esegue la diagnosi, non calcola consumi/
risparmi, non riproduce l'allegato 2 ne' le norme tecniche a pagamento.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-102-2014**: D.Lgs. 4/7/2014 n. 102, testo multivigente su Normattiva.
  Binario = pagina indice pinnata `!vig=2026-07-14` (hash stabile ffce5063...,
  pattern della skill aua-dpr59-dossier). Articoli 2, 8, 16 letti via AJAX
  (caricaArticolo) e trascritti verbatim in `references/fonti/dlgs-102-2014.md`.

Estratto operativo: `references/estratti/diagnosi-energetica-checklist.md`.

## Punti chiave (verificati sul testo)

- **Grande impresa** (art. 2): **> 250 occupati E fatturato > 50 mln euro**,
  **oppure** totale di bilancio > 43 mln euro. **Tep** = 41,86 GJ.
- **Obbligo** (art. 8 c. 1): grandi imprese -> diagnosi dei siti produttivi
  **entro 5/12/2015 e poi ogni 4 anni**; esecutori **ESCo/EGE certificati** (UNI
  CEI 11352/11339, art. 8 c. 2); risultati comunicati all'**ENEA**.
- **Energivore** (art. 8 c. 3, DM MiSE 21/12/2017): obbligo **indipendentemente
  dalla dimensione** + attuazione di almeno un intervento o ISO 50001.
- **Esenzioni**: consumi annui **< 50 tep** (c. 3-bis); **ISO 50001** con diagnosi
  conforme all'allegato 2 (c. 1, non si applica la periodicita').
- **Controlli ENEA** (c. 6): campione **>= 3%**; **100%** auditor interni.
- **Sanzioni** (art. 16): mancata diagnosi **4.000-40.000 euro**; non conforme
  **2.000-20.000**; dopo diffida (90 gg) **1.500-15.000**; energivore senza
  intervento **1.000-10.000** (c. 13-bis). Irroga il MIMIT (gia' MiSE).

## Convenzioni specifiche

### Cosa NON fare
- Non eseguire la diagnosi ne' calcolare consumi/risparmi.
- Non riprodurre l'allegato 2 ne' le norme UNI CEI 11352/11339, ISO 50001 (a
  pagamento): citarle come riferimento.
- Non stabilire nel merito se un'impresa e' "energivora": rinvio al DM MiSE
  21/12/2017 e all'elenco CSEA.
- Non citare "a memoria" soglie/scadenze/sanzioni: citare sempre l'articolo (2, 8,
  16).
- Non confondere il criterio dimensionale (art. 2) con il criterio di consumo
  (< 50 tep, art. 8 c. 3-bis).

### Cosa fare
- Applicare correttamente la definizione di grande impresa (congiunzione "> 250 E
  > 50 mln" oppure disgiunzione "> 43 mln di bilancio").
- Verificare le esenzioni (50 tep, ISO 50001) prima di concludere l'obbligo.
- Citare periodicita', soggetto certificato, ENEA e sanzioni con l'articolo.
- Chiudere con il rinvio all'ENEA/auditor certificato e all'impresa.

## Aggiornamento della fonte Normattiva

Testo multivigente: se si aggiorna la skill, ri-pinnare la URL a nuova
`!vig=YYYY-MM-DD`, riscaricare la pagina indice (nuovo hash) e rileggere via AJAX
gli articoli modificati (artt. 8 e 16 in vigore dal 29-7-2020).

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con EGE/energy manager).

## Stato attuale

- Versione: 0.1.0-alpha (closes #45)
- Task files: 2 (`verifica-obbligo.md`, `checklist-adempimento.md`)
- Esempi: 2 (grande impresa manifatturiera obbligata; grande impresa di servizi
  esente < 50 tep)
