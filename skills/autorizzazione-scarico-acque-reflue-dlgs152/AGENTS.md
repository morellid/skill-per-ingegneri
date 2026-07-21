# AGENTS.md - autorizzazione-scarico-acque-reflue-dlgs152

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **tecnico ambientale/degli impianti** e al **titolare dello scarico** per
l'**autorizzazione allo scarico di acque reflue** (criteri generali) e per la **domanda** di
autorizzazione degli **scarichi industriali**, ai sensi del **D.Lgs. 3 aprile 2006, n. 152, Parte III,
artt. 124 e 125**. Target: tecnici ambientali, progettisti di impianti di depurazione, titolari di
scarichi.

**E' una skill documentale per il tecnico**: inquadra obblighi, competenze, termini e contenuti; **non
redige** la domanda ne' progetta l'impianto di depurazione, **non applica** i valori limite di
emissione.

## Nota sull'area e sulla complementarita'

Area **ambiente-territorio-mobilita**. Distinta da `autorizzazione-integrata-ambientale-dlgs152` (AIA,
installazioni IPPC) e dalle skill sui rifiuti (`classificazione-rifiuti-dlgs152`, `sottoprodotti-
end-of-waste-dlgs152`): questa copre la **tutela delle acque** (autorizzazione allo scarico, Parte III).
L'autorizzazione allo scarico puo' confluire nell'**AUA** (DPR 59/2013) per talune imprese - rinvio.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-152-2006-124-125**: D.Lgs. 152/2006, pagina indice Normattiva pinnata a `!vig=2026-07-17` (hash
  `c2175fe5...`; codice 006G0171, idGruppo 25, dataPubblicazioneGazzetta 2006-04-14). Artt. 124 (v3) e
  125 (v1) caricati via `caricaArticolo` (formato AKN) e trascritti verbatim.

Trascrizione in `references/fonti/dlgs-152-2006-124-125.md`; estratto operativo in
`references/estratti/autorizzazione-scarico-checklist.md`.

## Punti chiave (verificati sul testo)

- **Obbligo** (124, c. 1): tutti gli scarichi **preventivamente autorizzati**; **titolare** (c. 2):
  attivita'/scarico finale/consorzio.
- **Regimi** (cc. 3-6): domestiche/fognarie e termali definiti dalle **regioni**; domestiche in
  fognatura **sempre ammesse**; **autorizzazione provvisoria** dei depuratori.
- **Competenza/termine** (c. 7): **provincia** o **ente di governo dell'ambito** (pubblica fognatura);
  **90 giorni**.
- **Validita'/rinnovo** (c. 8): **4 anni**; rinnovo **1 anno prima**; **sostanze pericolose (art. 108)**
  rinnovo espresso **6 mesi**.
- **Prescrizioni/spese/modifiche** (cc. 9-12): prescrizioni tecniche; **spese a carico del richiedente**;
  **nuova autorizzazione** se lo scarico cambia (art. 124, c. 12).
- **Domanda industriale** (art. 125): caratteristiche quali/quantitative, volume annuo, ricettore, punto
  di prelievo, sistema di scarico/depurazione; **Tab. 3/A** → capacita' di produzione e fabbisogno
  orario.

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** la domanda ne' **progettare** l'impianto di depurazione o lo scarico.
- Non **applicare** i **valori limite di emissione** dell'**Allegato 5 alla Parte III** (Tab.
  1/2/3/3-A/4): rinvio.
- Non trattare come procedura l'**AUA** (DPR 59/2013) ne' l'**AIA**: rinvio alle skill/temi dedicati.

### Cosa fare
- Inquadrare obbligo, titolare, competenza, termini, validita'/rinnovo, prescrizioni e modifiche (124) e
  il contenuto della domanda per gli scarichi industriali (125).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 152/2006 pinnato a nuovo `!vig=` (nuovo hash) e rileggere gli
artt. 124-125, verificando le modifiche dei doppi tondi `(( ))`.

## Validatori

- Non ancora assegnato (Livello 2 con tecnico ambientale/idraulico).

## Stato attuale

- Versione: 0.1.0-alpha (closes #366)
- Task files: 2 (`inquadra-autorizzazione-scarico.md`, `inquadra-domanda-scarico-industriale.md`)
- Esempi: 2 (nuovo scarico industriale in pubblica fognatura; ampliamento con/senza modifica dello
  scarico)
