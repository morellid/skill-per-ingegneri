# carico-incendio-classe-resistenza-dm

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con professionista antincendio/ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista antincendio / strutturale** per la **determinazione del
carico d'incendio specifico di progetto q_f,d** di un compartimento e della conseguente **classe di
resistenza al fuoco** richiesta agli elementi costruttivi, secondo il **DM 9 marzo 2007** ("Prestazioni di
resistenza al fuoco delle costruzioni nelle attività soggette al controllo del CNVVF").

**Non esegue** il progetto prestazionale con curve naturali né le **analisi termiche/meccaniche** e **non
sostituisce** il professionista: fornisce la formula q_f,d = δ_q1·δ_q2·δ_n·q_f, i coefficienti tabellari
(Tab. 1-3), i livelli di prestazione (I-V), le classi e le Tabelle 4-5. È il **calcolo di dettaglio** che le
NTC 2018 §3.6.1 rinviano a questo DM.

## Target

Professionisti antincendio e ingegneri strutturisti che devono determinare il carico d'incendio specifico di
progetto e la classe di resistenza al fuoco richiesta secondo il DM 9 marzo 2007.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `calcola-carico-incendio-specifico-progetto` | Carico d'incendio specifico q_f (m_i, ψ_i) e di progetto q_f,d = δ_q1·δ_q2·δ_n·q_f con le Tabelle 1, 2 e 3 (punti 1-2) |
| `determina-livello-classe-resistenza` | Livelli di prestazione I-V, classe per il livello II (30/60) e per il livello III (Tabella 4), curve nominali e Tabella 5 (punti 3-4) |

Nucleo: **carico d'incendio** q = Σ g_i·H_i·m_i·ψ_i, **q_f = q/A**, **q_f,d = δ_q1·δ_q2·δ_n·q_f** (Tab. 1-3),
**livelli** I-V, **classi** 15-360 min (Tab. 4 per il livello III, Tab. 5 per le curve naturali) e **curve
nominali** (standard θ_g = 20 + 345·log10(8t+1)).

## Relazione con altre skill

- **Complementare** a `resistenza-fuoco-strutture-ntc` (NTC 2018 §3.6.1): quella inquadra il framework e
  **rinvia** a questo DM per il calcolo del carico d'incendio; questa fornisce i coefficienti (Tab. 1-3) e le
  classi (Tab. 4-5). È **distinta** da `prevenzione-incendi-attivita-procedimenti-dpr151` (procedimenti
  amministrativi VVF).

## Fonti consultate

- **DM 9 marzo 2007** - **G.U. Serie Generale n. 74 del 29/3/2007 - Suppl. Ord. n. 87** (PDF Gazzetta
  Ufficiale, SHA256 `c7003438...`). Scansione **GURITEL**: contenuto letto renderizzando le pagine in
  immagine (`pdftoppm`) e trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** il progetto prestazionale con **curve naturali/modelli d'incendio** né le **analisi
  termiche/meccaniche** degli elementi.
- **Non fornisce** le proprietà dei materiali ad alta temperatura (**Eurocodici parte 1-2**) né i valori di
  H_i (**UNI EN ISO 1716**); **non** riproduce le **regole tecniche verticali** VVF né il DM 14/9/2005
  (livelli IV-V).
- **Non tratta** i procedimenti antincendio (DPR 151/2011) né il framework NTC (skill
  `resistenza-fuoco-strutture-ntc`).

**La skill è un supporto documentale: non sostituisce il professionista antincendio né il progettista strutturale, né la lettura del DM 9 marzo 2007 e delle regole tecniche di prevenzione incendi applicabili.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
