# AGENTS.md - pums-validator-dm397

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Validazione formale di Piani Urbani di Mobilita' Sostenibile (PUMS) ai sensi del DM 4 agosto 2017 n. 397, come modificato dal DM 28 agosto 2019 n. 396, con riferimento operativo al Vademecum MIMS 2022. Target utente: tecnici di amministrazioni comunali (>100.000 ab.), citta' metropolitane, professionisti incaricati della redazione/aggiornamento di PUMS, valutatori di istanze TRM.

## Fonti autoritative

Tutte catalogate in `references/sources.yaml`:

- **DM 397/2017** (GU n. 233 del 5/10/2017, S.O. 53) - hash `867acba97777daef4f43648b4e49744d32f07549ef2656b8e3d71d49abb2b053`
- **DM 396/2019** (Modifica del DM 397/2017) - hash `e8be2a96fd957704b4dba507bfe85db4279acaff8e40530815b0a25cfec0e599`
- **Vademecum MIMS 2022** (Indirizzi operativi PUMS, 27/09/2022) - hash `9078694ed2ff41c635ff41ccfee80fae1ba7c95471ad7aa98aef1898d9966f6d`

Fonti convertite in markdown committato:
- `references/fonti/dm-4-8-2017-397-pums.md`
- `references/fonti/dm-28-8-2019-396-pums.md`
- `references/fonti/vademecum-pums-mit-2022.md`

Estratti curati per la validazione:
- `references/estratti/dm-4-8-2017-397-pums.md` - struttura del decreto base, 8 passi procedura, Tabella 1 originale (superseded)
- `references/estratti/dm-28-8-2019-396-pums.md` - sintesi novita' 2019, Tabella 1 nuova (17 macro-obiettivi + indicatori), criteri TRM
- `references/estratti/vademecum-pums-mit-2022.md` - terminologia "Linee guida italiane", indirizzi operativi 3.1-3.6, Riquadro I quadro conoscitivo

## Articoli e punti chiave

- **DM 397/2017 art. 3 c.1**: obbligo di redazione per comuni > 100.000 ab., citta' metropolitane, associazioni di comuni.
- **DM 397/2017 art. 4 c.1**: aggiornamento almeno quinquennale + valutazione 12 mesi pre-affidamento TPL.
- **DM 397/2017 Allegato 1 lett. a-h**: procedura in 8 passi (gruppo di lavoro, quadro conoscitivo, partecipazione, obiettivi, scenari, VAS, adozione+approvazione, monitoraggio).
- **DM 396/2019 art. 5**: sostituzione integrale della Tabella 1 con la nuova Tabella 1 (17 macro-obiettivi minimi, aree A/B/C/D, indicatori specifici) dell'Allegato 1 al DM 396/2019.
- **DM 396/2019 art. 2**: estensione dell'obbligo di cui all'art. 1 c.2 DM 397/2017 ai comuni > 100.000 ab. non in citta' metropolitane, ai fini dell'accesso ai finanziamenti TRM.
- **DM 396/2019 art. 7 c.3 secondo periodo**: clausola transitoria limitata a PUMS adottati **prima** della pubblicazione del DM 397/2017, purche' aggiornati in linea con i criteri del DM 397/2017.
- **Vademecum 3.6**: piano di monitoraggio con cadenza biennale obbligatoria, tempo "0", soggetti, budget, cruscotti.

## Convenzioni specifiche

### Cosa NON fare
- **Non confondere Tabella 1 originale e Tabella 1 nuova**. La nuova (DM 396/2019) ha sostituito integralmente l'originale (DM 397/2017): un PUMS che cita ancora la prima e' formalmente difforme.
- **Non confondere adozione di Giunta e approvazione di Consiglio**. Allegato 1 lett. g) DM 397/2017 distingue i due atti.
- **Non assimilare "Piano della Mobilita' Sostenibile" generico al PUMS** disciplinato dal DM 397/2017. Il nome non basta: serve la conformita' procedurale e contenutistica.
- **Non considerare la VAS opzionale**: l'Allegato 1 lett. f) la pone come passo della procedura. Eventuali esclusioni vanno motivate dall'autorita' competente per la VAS.

### Cosa fare
- Citare sempre con precisione: "art. 3 c.1 DM 397/2017" o "art. 5 DM 396/2019", non "il decreto sui PUMS".
- Strutturare ogni report per le 5 sotto-attivita' (`tasks/check-*.md`) con tabella riassuntiva CONFORME/NON CONFORME/NON DETERMINABILE.
- Categorizzare i rilievi in **BLOCCANTI**, **NON BLOCCANTI**, **NON DETERMINABILI** e proporre raccomandazione operativa.
- Chiudere ogni report con l'avvertenza di rinvio: professionista firmatario, Tavolo Tecnico PUMS, autorita' VAS, amministrazione finanziatrice.

### Limiti di responsabilita'
La skill produce check-list formali, non sostituisce: il giudizio del professionista firmatario, la valutazione del Tavolo Tecnico PUMS, il parere motivato VAS, ne' la decisione dell'amministrazione che valuta l'istanza di finanziamento. Le Linee guida regionali integrative non sono catalogate in questa versione.

## Validatori

- Da identificare per validazione Livello 2 (ingegnere dei trasporti / mobilita' urbana di amministrazione comunale diverso dall'autore).

## Stato attuale

- Versione: vedi `CHANGELOG.md` (0.1.0-alpha).
- Validazione: Livello 1 (autore singolo, fonti verificate).
- Task files: `check-ambito-obbligo.md`, `check-procedura-redazione-pums.md`, `check-obiettivi-pums.md`, `check-indicatori-tabella1.md`, `check-monitoraggio-aggiornamento.md`.
- Esempi: 1 conforme + 1 problematico.
