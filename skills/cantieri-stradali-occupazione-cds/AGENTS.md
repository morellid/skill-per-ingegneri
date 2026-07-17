# AGENTS.md - cantieri-stradali-occupazione-cds

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'**occupazione della sede stradale** (art. 20) e alle **opere,
depositi e cantieri stradali** (art. 21) del **Codice della Strada** (D.Lgs. 285/1992):
regime autorizzatorio, obblighi di sicurezza e segnalazione, sanzioni. Target: tecnici,
imprese, enti proprietari/gestori della strada.

**È una skill documentale**: non rilascia autorizzazioni, non redige il piano di segnaletica
temporanea e non riproduce il regolamento/disciplinare tecnico.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **cds-285-1992-20-21**: D.Lgs. 30/4/1992 n. 285 (CdS), artt. 20 e 21, testo su Normattiva.
  Binario = pagina indice pinnata `!vig=2026-07-17` (hash stabile e541dc1a..., codice
  092G0306; stesso indice della skill trasporti-eccezionali-cds-art10). Articoli letti via
  AJAX (caricaArticolo, idGruppo 2) e trascritti verbatim in
  `references/fonti/cds-285-1992-20-21.md`.

Estratto operativo: `references/estratti/cantieri-stradali-checklist.md`.

## Punti chiave (verificati sul testo)

- **Occupazione** (art. 20): vietata su strade **A/B/C/D** (incl. fiere/mercati), ammessa a
  condizioni su **E/F** (itinerario alternativo o zone storico-ambientali); chioschi/edicole
  fuori centri abitati non sulle fasce di rispetto; marciapiedi: max metà larghezza, **>= 2
  m** liberi, fuori triangoli di visibilità; sanzione 173-694 euro + rimozione.
- **Cantieri** (art. 21): **preventiva autorizzazione/concessione** dell'ente competente
  (art. 26); accorgimenti per sicurezza/fluidità e visibilità del personale giorno e notte;
  delimitazione/segnalazione demandate al **regolamento** (c. 3); sanzione 866-3.464 euro +
  rimozione.
- Gli **importi sanzioni** sono i vigenti (adeguamenti biennali ex art. 195 c. 3).

## Convenzioni specifiche

### Cosa NON fare
- Non **rilasciare** autorizzazioni/concessioni (art. 26): rinviare all'ente.
- Non **redigere** il piano di segnaletica temporanea né gli schemi di cantiere.
- Non riprodurre il **Regolamento (DPR 495/1992, artt. 30-43)** né il **DM 10/7/2002**:
  rinvio.
- Non trattare la **sicurezza dei lavoratori** nei cantieri (D.Lgs. 81/2008): fuori
  perimetro.
- Non citare a memoria: citare l'articolo/comma (20, 21) e gli importi vigenti.

### Cosa fare
- Partire dalla **classificazione** della strada (tipo A-F, art. 2) e dall'ente
  proprietario/gestore.
- Distinguere **occupazione** (art. 20) da **cantiere/opere/depositi** (art. 21).
- Tenere la skill distinta da `trasporti-eccezionali-cds-art10` (art. 10) e dalle skill
  sicurezza cantieri.

## Aggiornamento della fonte Normattiva

Testo multivigente: se si aggiorna la skill, ri-pinnare la URL a nuova `!vig=YYYY-MM-DD`,
riscaricare la pagina indice (nuovo hash) e rileggere via AJAX gli articoli (attenzione agli
adeguamenti biennali degli importi delle sanzioni).

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con esperto CdS/gestione strade).

## Stato attuale

- Versione: 0.1.0-alpha (closes #329)
- Task files: 2 (`inquadra-cantiere-stradale.md`, `inquadra-occupazione-suolo.md`)
- Esempi: 2 (apertura cantiere temporaneo su strada tipo E; dehors su marciapiede e mercato
  su strada tipo C)
