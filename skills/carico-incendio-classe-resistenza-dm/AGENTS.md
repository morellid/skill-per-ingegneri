# AGENTS.md - carico-incendio-classe-resistenza-dm

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista antincendio / strutturale** per la **determinazione del carico
d'incendio specifico di progetto q_f,d** di un compartimento e della conseguente **classe di resistenza al
fuoco** richiesta agli elementi costruttivi, secondo il **DM 9 marzo 2007** ("Prestazioni di resistenza al
fuoco delle costruzioni nelle attività soggette al controllo del CNVVF"): formula del carico d'incendio,
coefficienti tabellari (δ_q1, δ_q2, δ_n), livelli di prestazione e classi.

**È una skill documentale per il tecnico**: fornisce la formula q_f,d = δ_q1·δ_q2·δ_n·q_f, le Tabelle 1-3
dei coefficienti, i livelli I-V, le Tabelle 4 e 5 delle classi e le curve nominali; **non** esegue il
progetto prestazionale con curve naturali né le analisi termiche/meccaniche, e **non** fornisce le
proprietà dei materiali ad alta temperatura.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. La skill copre il **calcolo di dettaglio del carico d'incendio** che la skill
`resistenza-fuoco-strutture-ntc` (NTC 2018 §3.6.1) dichiara esplicitamente **fuori scope** ("il calcolo del
carico d'incendio è nel DM 9/3/2007"). Le due skill sono **complementari**: la prima inquadra il framework
NTC, questa fornisce i coefficienti numerici (Tab. 1-3) e le tabelle di classe (Tab. 4-5). È **distinta** da
`prevenzione-incendi-attivita-procedimenti-dpr151` (procedimenti amministrativi VVF ai sensi del DPR
151/2011). Restano fuori scope: il progetto prestazionale con curve naturali/modelli d'incendio, le regole
tecniche verticali VVF, gli Eurocodici parte 1-2 e i valori di H_i (UNI EN ISO 1716).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dm-9-3-2007**: PDF della G.U. Serie Generale n. 74 del 29/3/2007 - Suppl. Ord. n. 87 (DM 9 marzo 2007),
  SHA256 `c7003438...` (doppio download riproducibile dallo stesso URL eli). Scansione **GURITEL**:
  `pdftotext` non estrae testo utile; formula, tabelle e curve sono state lette renderizzando le pagine in
  immagine (`pdftoppm`) e trascritte verbatim.

Trascrizione in `references/fonti/dm-9-3-2007.md`; estratto operativo in
`references/estratti/carico-incendio-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **Carico d'incendio specifico** (punto 1): q = Σ g_i·H_i·m_i·ψ_i [MJ]; q_f = q/A; m_i = 0,80 legno/1,00
  altri; ψ_i = 0 / 0,85 / 1.
- **Carico d'incendio di progetto** (punto 2): q_f,d = δ_q1·δ_q2·δ_n·q_f; δ_q1 Tab. 1 (1,00-2,00 per
  superficie); δ_q2 Tab. 2 (0,80/1,00/1,20 per rischio); δ_n = Π δ_ni Tab. 3 (misure di protezione).
- **Livelli** (punto 3): I-V; I non ammesso; livello II classe 30/60; livello III Tabella 4 (per q_f,d).
- **Classi**: 15, 20, 30, 45, 60, 90, 120, 180, 240, 360 minuti.
- **Curve** (punto 4): standard θ_g = 20 + 345·log10(8t+1); idrocarburi; esterna; Tabella 5 (curve naturali).

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire** il progetto prestazionale con curve naturali/modelli d'incendio né le analisi
  termiche/meccaniche; non **fornire** le proprietà dei materiali ad alta temperatura (Eurocodici parte 1-2)
  né i valori di H_i (UNI EN ISO 1716).
- Non **riprodurre** le regole tecniche verticali VVF né il DM 14/9/2005 (livelli IV-V); non **trattare** i
  procedimenti amministrativi antincendio (→ skill DPR 151/2011).

### Cosa fare
- Fornire la formula q_f,d = δ_q1·δ_q2·δ_n·q_f, i coefficienti tabellari, i livelli e le classi (Tab. 4-5) e
  le curve nominali, sempre con rinvio al punto/tabella del DM.

## Aggiornamento delle fonti

DM: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
rileggere via immagine (GURITEL). Verificare la formula q_f,d, le Tabelle 1-3 (δ), le Tabelle 4-5 (classi) e
le curve nominali. Attenzione: il PDF S.O. n. 87 contiene anche il DM 16 febbraio 2007 (classificazione).

## Validatori

- Non ancora assegnato (Livello 2 con professionista antincendio/ingegnere strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #443)
- Task files: 2 (`calcola-carico-incendio-specifico-progetto.md`, `determina-livello-classe-resistenza.md`)
- Esempi: 2 (calcolo di q_f,d per un compartimento con misure di protezione; determinazione della classe per
  il livello III via Tabella 4)
