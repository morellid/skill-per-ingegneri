# controllo-manutenzione-antincendio-dm2021

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico/professionista antincendio abilitato da completare)

Skill di **supporto documentale** per il **controllo e la manutenzione degli impianti, attrezzature ed altri sistemi di
sicurezza antincendio** nei luoghi di lavoro, secondo il **D.M. 1° settembre 2021** (attuativo dell'**art. 46 c. 3 lett.
a) punto 3 del D.Lgs 81/2008**), in vigore dal **25 settembre 2022**: distinzione tra sorveglianza, controllo periodico
e manutenzione, impostazione del registro dei controlli, individuazione della norma UNI di riferimento, verifica della
qualificazione dei manutentori.

**Non fissa le periodicità puntuali** (che discendono dalle norme UNI di prodotto), **non certifica** il registro e
**non rilascia** la qualifica dei manutentori (attestata dai Vigili del fuoco). È **distinta** da
`piano-emergenza-antincendio-dm2021` (D.M. 2/9/2021) e da `prevenzione-incendi-attivita-procedimenti-dpr151` (DPR
151/2011).

## Target

RSPP, datori di lavoro, tecnici antincendio, responsabili della manutenzione e manutentori che devono organizzare e
documentare il regime di controllo e manutenzione antincendio di un'attività.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-registro-e-livelli-controllo` | Imposta il registro dei controlli (All. I), distingue sorveglianza/controllo periodico/manutenzione (art. 1) e collega ogni sistema alla norma UNI di riferimento (Tabella 1) |
| `verifica-qualificazione-manutentori` | Verifica che manutenzione e controllo periodico siano eseguiti da tecnici manutentori qualificati (art. 4 + Allegato II) e inquadra il regime transitorio |

Nucleo: **tre livelli** (sorveglianza del lavoratore istruito; controllo periodico e manutenzione del tecnico
qualificato); **registro dei controlli** predisposto dal datore di lavoro, aggiornato e disponibile per gli organi di
controllo; **Tabella 1** con le norme UNI per tipologia; **tecnico manutentore qualificato** (formazione + valutazione
+ attestazione VVF; regime transitorio per chi ha ≥3 anni di attività).

## Relazione con altre skill

- Copre il **D.M. 1/9/2021** (controllo e manutenzione). **Distinta** da `piano-emergenza-antincendio-dm2021` (D.M.
  2/9/2021, gestione emergenza), `prevenzione-incendi-attivita-procedimenti-dpr151` (DPR 151/2011),
  `carico-incendio-classe-resistenza-dm` (D.M. 9/3/2007) e `resistenza-fuoco-strutture-ntc`.

## Fonti consultate

- **D.M. 1° settembre 2021** — GU Serie Generale n. 230 del 25/09/2021, PDF ufficiale Gazzetta Ufficiale, SHA256
  `560643c7...` (doppio download riproducibile), estratto con `pdftotext`. Testo di legge liberamente riproducibile
  (art. 5 L. 633/1941).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- Non fissa le **periodicità puntuali** dei controlli: discendono dalle **norme UNI di prodotto** (es. UNI 9994-1 per
  gli estintori) richiamate nella Tabella 1, soggette a diritto d'autore e non trascritte.
- Non **rilascia/attesta** la qualifica del manutentore (è del Corpo nazionale dei vigili del fuoco) né certifica il
  registro.
- Non tratta la **gestione dell'emergenza** (D.M. 2/9/2021, → `piano-emergenza-antincendio-dm2021`), la
  **progettazione** antincendio (D.M. 3/9/2021), il **DPR 151/2011** (→ `prevenzione-incendi-attivita-procedimenti-dpr151`)
  né il **carico d'incendio** (D.M. 9/3/2007, → `carico-incendio-classe-resistenza-dm`).

**La skill è un supporto documentale: non fissa le periodicità puntuali, non certifica il registro e non sostituisce il tecnico manutentore qualificato né il professionista antincendio.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
