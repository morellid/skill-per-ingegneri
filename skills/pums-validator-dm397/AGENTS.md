# AGENTS.md - pums-validator-dm397

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Validazione formale di Piani Urbani di Mobilita' Sostenibile (PUMS) ai sensi del DM 4 agosto 2017 n. 397, come modificato dai DM 28 agosto 2019 n. 396, DM 26 gennaio 2021 n. 29 e DM 12 novembre 2021 n. 444, con riferimento operativo al Vademecum MIMS 2022. Target utente: tecnici di amministrazioni comunali (>100.000 ab.), citta' metropolitane, professionisti incaricati della redazione/aggiornamento di PUMS, valutatori di istanze TRM e mobilita' ciclistica.

## Fonti autoritative

Tutte catalogate in `references/sources.yaml`:

- **DM 397/2017** (GU n. 233 del 5/10/2017, S.O. 53) - hash `867acba97777daef4f43648b4e49744d32f07549ef2656b8e3d71d49abb2b053`
- **DM 396/2019** (Modifica del DM 397/2017) - hash `e8be2a96fd957704b4dba507bfe85db4279acaff8e40530815b0a25cfec0e599`
- **DM 29/2021** (Proroga termini PUMS, sostituisce art. 3 c.1 DM 397/2017) - hash `2312c2ab1ccec23bf86e2172a723531c0d3792267c8c81041f79a6ed3adabd74`
- **DM 444/2021** (Termine unitario 1/1/2023; sostituisce art. 1 c.2 DM 397/2017 estendendolo a mobilita' ciclistica; abroga art. 7 c.3 DM 396/2019) - hash `6c8e29e0ef8e846436433cd01ff82769ea732bfba5c182030fefeb78c9f919af`
- **Vademecum MIMS 2022** (Indirizzi operativi PUMS, 27/09/2022) - hash `9078694ed2ff41c635ff41ccfee80fae1ba7c95471ad7aa98aef1898d9966f6d`

Fonti convertite in markdown committato:
- `references/fonti/dm-4-8-2017-397-pums.md`
- `references/fonti/dm-28-8-2019-396-pums.md`
- `references/fonti/dm-26-1-2021-29-pums.md`
- `references/fonti/dm-12-11-2021-444-pums.md`
- `references/fonti/vademecum-pums-mit-2022.md`

Estratti curati per la validazione:
- `references/estratti/dm-4-8-2017-397-pums.md` - struttura del decreto base, 8 passi procedura, art. 1 c.2 nel testo vigente (DM 444/2021), termine vigente 1/1/2023
- `references/estratti/dm-28-8-2019-396-pums.md` - sintesi novita' 2019, Tabella 1 nuova (17 macro-obiettivi + indicatori), nota di abrogazione art. 7 c.3
- `references/estratti/dm-26-1-2021-29-pums.md` - sostituzione art. 3 c.1 DM 397/2017 (4 aprile / 4 agosto 2021), modifica art. 7 c.1 DM 396/2019
- `references/estratti/dm-12-11-2021-444-pums.md` - termine unitario 1/1/2023, nuovo testo art. 1 c.2 DM 397/2017 (gate finanziamenti TRM e ciclistica), criterio premiale 2022, abrogazione art. 7 c.3 DM 396/2019, piattaforma Osservatorio TPL
- `references/estratti/vademecum-pums-mit-2022.md` - terminologia "Linee guida italiane", indirizzi operativi 3.1-3.6, Riquadro I quadro conoscitivo

## Articoli e punti chiave

- **DM 397/2017 art. 1 c.2 (nel testo da ultimo sostituito dal DM 444/2021 art. 2 c.1)**: gate di accesso alle risorse statali stanziate dal 1 gennaio 2023 per nuovi interventi TRM e mobilita' ciclistica = adozione del PUMS. Per comuni > 100.000 ab. ricompresi in citta' metropolitana e capoluoghi di citta' metropolitana: condizione assolta dall'adozione del PUMS della citta' metropolitana.
- **DM 397/2017 art. 3 c.1 (nel testo da ultimo sostituito dal DM 444/2021 art. 1)**: obbligo di adozione del PUMS per comuni > 100.000 ab., citta' metropolitane, associazioni di comuni con popolazione cumulativa > 100.000 ab.; **termine unitario fissato al 1 gennaio 2023**. Termini precedenti (24 mesi, 36 mesi, 4 aprile / 4 agosto 2021) sono storici.
- **DM 397/2017 art. 4 c.1**: aggiornamento almeno quinquennale + valutazione 12 mesi pre-affidamento TPL.
- **DM 397/2017 Allegato 1 lett. a-h**: procedura in 8 passi (gruppo di lavoro, quadro conoscitivo, partecipazione, obiettivi, scenari, VAS, adozione+approvazione, monitoraggio).
- **DM 396/2019 art. 5**: sostituzione integrale della Tabella 1 con la nuova Tabella 1 (17 macro-obiettivi minimi, aree A/B/C/D, indicatori specifici) dell'Allegato 1 al DM 396/2019.
- **DM 396/2019 art. 3**: l'art. 3 c.1 DM 397/2017 non si applica agli enti di area vasta non citta' metropolitane.
- **DM 396/2019 art. 7 c.3**: ABROGATO dall'art. 4 del DM 444/2021. Non e' invocabile (ne' il primo periodo - primo rapporto + atto di Giunta - ne' il secondo periodo - PUMS adottati prima del DM 397/2017).
- **DM 444/2021 art. 2 c.2**: periodo 1/1/2022 - 31/12/2022 = criterio premiale (non condizione di accesso).
- **DM 444/2021 art. 3**: verifica dell'ottemperanza tramite piattaforma dell'Osservatorio nazionale TPL.
- **Vademecum 3.6**: piano di monitoraggio con cadenza biennale obbligatoria, tempo "0", soggetti, budget, cruscotti. La triade di target a 2/3, 5, 10 anni e' indirizzo operativo del Vademecum: l'orizzonte di 10 anni e' di Piano (decreto), mentre 2/3 e 5 anni sono raccomandazioni Vademecum.

## Convenzioni specifiche

### Cosa NON fare
- **Non confondere Tabella 1 originale e Tabella 1 nuova**. La nuova (DM 396/2019) ha sostituito integralmente l'originale (DM 397/2017): un PUMS che cita ancora la prima e' formalmente difforme.
- **Non confondere adozione di Giunta e approvazione di Consiglio**. Allegato 1 lett. g) DM 397/2017 distingue i due atti. Il gate dell'art. 1 c.2 DM 397/2017 (nuovo testo DM 444/2021) si misura sull'**adozione**, non sull'approvazione; quest'ultima rileva sul piano della conformita' generale del PUMS.
- **Non assimilare "Piano della Mobilita' Sostenibile" generico al PUMS** disciplinato dal DM 397/2017. Il nome non basta: serve la conformita' procedurale e contenutistica.
- **Non considerare la VAS opzionale**: l'Allegato 1 lett. f) la pone come passo della procedura. Eventuali esclusioni vanno motivate dall'autorita' competente per la VAS.
- **Non citare come vigenti norme superate o abrogate**. In particolare: l'art. 7 c.3 del DM 396/2019 e' abrogato (DM 444/2021 art. 4); i termini "24 mesi", "36 mesi" e "4 aprile / 4 agosto 2021" sono storici.
- **Non trattare la triade target 2/3-5-10 anni come obbligo di decreto**. Solo l'orizzonte di 10 anni e' richiesto dal DM 397/2017 (Allegato 1, Premessa); i target a 2/3 e 5 anni sono indirizzi operativi del Vademecum 2022 e vanno classificati come "Vademecum alignment gap" se mancanti.
- **Non confondere il gate dell'art. 1 c.2 con la conformita' generale del PUMS**. Sono piani distinti: il gate richiede solo l'adozione; la conformita' generale comprende procedura, obiettivi, indicatori e monitoraggio. Negli esempi e nei report, separare i due esiti.

### Cosa fare
- Citare sempre con precisione: "art. 3 c.1 DM 397/2017 nel testo da ultimo sostituito dal DM 444/2021 art. 1" o "art. 5 DM 396/2019", non "il decreto sui PUMS".
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
