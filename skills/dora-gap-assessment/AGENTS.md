# AGENTS.md - dora-gap-assessment

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Gap assessment di un'entita' finanziaria UE (banca, istituto di pagamento, impresa di investimento, impresa di assicurazione, etc.) rispetto al Regolamento (UE) 2022/2554 (DORA - Digital Operational Resilience Act), direttamente applicabile in Italia dal 17/01/2025. Target utente: CISO, ICT risk manager, compliance officer, internal auditor di entita' finanziarie, o consulente che li supporta.

La skill copre **solo gli obblighi lato entita' finanziaria** (artt. 1-30, 45, 64 di DORA): gli obblighi di sorveglianza dei fornitori critici lato autorita' (Capo V Sez. II, artt. 31-44), le competenze delle autorita' (Capo VII, artt. 46-56) e le disposizioni sanzionatorie/finali sono fuori scope.

## Fonti autoritative

- **Regolamento (UE) 2022/2554 (DORA)** - versione PE-CONS 41/22 (testo trilogue-finale identico in contenuto alla versione pubblicata in GU UE L 333 del 27/12/2022). SHA256 e binary path registrati in `references/sources.yaml` con id `reg-ue-2022-2554-dora`. Trascrizione integrale degli artt. 1-30, 45, 64 in `references/fonti/reg-ue-2022-2554-dora.md`.

Estratti curati per pillar gia' preparati in `references/estratti/`:
- `reg-ue-2022-2554-dora.md` - indice navigabile per Pillar (1-5) + sezione Ambito (artt. 1-4) e Tempistiche (art. 64). Ogni voce rimanda all'articolo/paragrafo esatto del file `fonti/`.

## Articoli e punti chiave

Quando l'agent produce output, **cita sempre articolo e paragrafo** (es. "art. 18 par. 1 lettera a"), non la norma in generale. Riferimenti piu' frequentemente citati:

- **Art. 2 par. 1 lettere a-u**: ambito soggettivo (21 categorie di entita' finanziarie).
- **Art. 2 par. 3**: esclusioni (AIF, microassicuratori, enti pensione minimi, ecc.).
- **Art. 3 n. 10**: "grave incidente connesso alle TIC".
- **Art. 3 n. 13**: "minaccia informatica significativa".
- **Art. 3 n. 22**: "funzione essenziale o importante".
- **Art. 3 n. 60**: "microimpresa".
- **Art. 4**: principio di proporzionalita'.
- **Art. 5**: governance e organizzazione (responsabilita' dell'organo di gestione, lettere a-l).
- **Art. 6**: quadro per la gestione del rischio TIC; **par. 8** lettere a-h: strategia di resilienza operativa digitale.
- **Artt. 7-13**: sistemi/identificazione/protezione/individuazione/risposta-ripristino/backup/apprendimento.
- **Art. 16 par. 1**: quadro semplificato (lettere a-h).
- **Art. 18 par. 1 lettere a-f**: criteri di classificazione gravita' incidente.
- **Art. 19 par. 4 lettere a-c**: notifica iniziale, intermedia, finale.
- **Art. 23**: estensione del Capo III agli incidenti di pagamento.
- **Art. 26 par. 1**: TLPT con cadenza almeno triennale.
- **Art. 26 par. 8**: identificazione delle entita' tenute al TLPT.
- **Art. 28 par. 3**: registro delle informazioni; comunicazione annuale; informativa tempestiva.
- **Art. 28 par. 8**: strategie di uscita per servizi a supporto di funzioni essenziali o importanti.
- **Art. 30 par. 2**: clausole contrattuali minime per **tutti** gli accordi TIC (lettere a-i).
- **Art. 30 par. 3**: clausole **aggiuntive** per accordi a supporto di funzioni essenziali o importanti (lettere a-f).
- **Art. 45 par. 1**: meccanismi di condivisione (facolta', non obbligo); par. 3 notifica all'autorita'.

## Convenzioni specifiche

### Cosa NON fare

- **Non interpretare come obblighi** le facolta' (es. art. 45 par. 1 "possono"); distinguere chiaramente nell'output.
- **Non valutare gli RTS/ITS di secondo livello** (rinvii negli artt. 15, 16, 18, 20, 26, 28, 30): la skill mappa rispetto al testo di "livello 1". Se l'utente cita RTS specifici, indicarli come fuori scope.
- **Non confondere artt. 28-30 (lato entita') con artt. 31-44 (lato autorita')**: il task di Pillar 4 non valuta la sorveglianza sui fornitori critici dal lato della BCE/ESMA/EBA.
- **Non rilasciare attestazioni**: la skill produce mappature, non pareri di conformita'.
- **Non determinare autonomamente la qualificazione di "funzione essenziale o importante"** (art. 3 n. 22), ne' di "grave incidente TIC" (art. 3 n. 10), ne' di "minaccia significativa" (art. 3 n. 13): tutte rinviate al giudizio del professionista.
- **Non confondere DORA con NIS2, GDPR, EBA Guidelines on ICT Risk**: pur essendoci sovrapposizioni, le 4 normative hanno obblighi distinti.

### Cosa fare

- **Citare sempre articolo + paragrafo + lettera** (esempio: "art. 28 par. 3, registro delle informazioni; comunicazione annuale alle autorita' competenti").
- **Distinguere accordi "per tutti" vs "per funzioni essenziali o importanti"** in tutti gli output del Pillar 4 (art. 30 par. 2 vs par. 3).
- **Per ogni report**: includere sezione "Punti che richiedono giudizio del professionista" e disclaimer standard nel paragrafo "Avvertenza" finale.
- **Classificazioni**: CONFORME / PARZIALE / NON CONFORME / NON APPLICABILE (quest'ultima sempre con motivazione esplicita, tipicamente art. 16 par. 1 o art. 2 par. 3 o art. 3 n. 60).
- **Per il quadro semplificato (art. 16 par. 1)**: marcare gli items relativi agli artt. 5-15 come "NON APPLICABILE - art. 16 par. 1" e applicare solo i punti a-h dell'art. 16.
- **Per le microimprese (art. 3 n. 60)**: applicare le specifiche esclusioni testuali del Regolamento (es. art. 6 par. 6 audit, art. 11 par. 4-7 testing periodico, art. 13 par. 7 monitoraggio tecnologico, art. 25 par. 3 modalita' di test, art. 30 par. 3 lettera e deroga audit).

## Validatori

- Nessun validatore di Livello 2 identificato per v0.1.0-alpha. Per promozione a 0.2 e' necessaria validazione da CISO/compliance officer di entita' finanziaria diversa dall'autore.

## Stato attuale

- Versione: vedi `CHANGELOG.md` (`0.1.0-alpha`).
- Validazione: Livello 1 (autore + adversarial review fresh-context).
- Task files: 5 (uno per pillar).
- Esempi: 1 conforme + 1 problematico (vedi `examples/`).
