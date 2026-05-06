# AGENTS.md - cer-cacer-configurazione-gse

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

La skill copre la **configurazione** e la **qualifica al servizio CACER del GSE** delle tre forme di autoconsumo diffuso disciplinate dal D.Lgs. 199/2021:

- **Autoconsumatore Individuale a Distanza (AID)** - art. 30 c. 1 lett. a) n. 2;
- **Gruppo di Autoconsumatori (GAC)** - art. 30 c. 2 (con vincolo "stesso edificio o condominio" alla lett. a));
- **Comunita' di Energia Rinnovabile (CER)** - art. 31.

L'art. 32 disciplina il quadro regolatorio (ARERA, contratti, ruolo del referente), non i GAC.

Riferimenti normativi principali (regime vigente al 2026-05-07): **DM MASE 7 dicembre 2023 n. 414** come modificato dal **DM MASE 16 maggio 2025 n. 127** (estensione perimetro PNRR ai Comuni < 50.000 ab., aumento anticipazione al 30%, persone fisiche escluse dal fattore F) e da ultimo dal **DL 19 febbraio 2026 n. 19 art. 27** (re-aggancio del 30/6/2026 alla stipula accordi di concessione GSE; 24 mesi dalla comunicazione dell'accordo; limite 31/12/2027), oltre alle **Regole Operative CACER del GSE** vigenti e al **TIAD ARERA 727/2022/R/eel**.

Target: ingegneri / energy manager / EGE / ESCo / consulenti GSE / enti locali e amministratori di condominio.

## Fonti autoritative

Le fonti sono catalogate in `references/sources.yaml`. Per ognuna sono presenti URL ufficiale, data di consultazione, hash SHA256 del binario archiviato in `not_in_repo/` e licenza.

- **D.Lgs. 199/2021** (recepimento direttiva RED II) - id `dlgs-199-2021`
- **DM MASE 7 dicembre 2023 n. 414** (Decreto CACER, testo originario) - id `dm-mase-414-2023`
- **DM MASE 16 maggio 2025 n. 127** (modifiche al DM 414/2023) - id `dm-mase-127-2025`
- **DL 19 febbraio 2026 n. 19, art. 27** (Decreto PNRR 2026) - id `dl-19-2026-pnrr`
- **Delibera ARERA 727/2022/R/eel - TIAD** - id `delibera-arera-727-2022-tiad`
- **Regole Operative CACER del GSE - Allegato 1** - id `gse-regole-operative-cacer`
- **GSE - Pagina misura PNRR CACER** - id `gse-pnrr-cacer`

Estratti pertinenti gia' preparati in `references/estratti/`:
- `dlgs-199-2021-art-30-31-32.md` - mappatura corretta degli articoli (AID art. 30 c. 1 lett. a) n. 2, GAC art. 30 c. 2, CER art. 31, ARERA/contratti art. 32) e requisiti soggettivi.
- `dm-mase-414-2023.md` - perimetro cabina primaria (incentivo), soglie potenza, TIP, contributo PNRR nel **regime vigente al 2026-05-07** (DM 414/2023 + DM 127/2025 + DL 19/2026 art. 27): Comuni < 50.000 ab.; stipula accordi di concessione entro 30/6/2026; esercizio entro 24 mesi dalla comunicazione dell'accordo, max 31/12/2027; erogazione 30% / 40% / saldo.
- `tiad-arera-727-2022.md` - regolazione flussi e calcolo energia condivisa oraria.
- `gse-regole-operative-cacer.md` - flusso di qualifica, documenti, ruolo del referente.

## Articoli e punti chiave

Quando l'agent produce output deve citare il riferimento puntuale, non la legge in generale.

- **D.Lgs. 199/2021 art. 30 c. 1 lett. a) n. 2** - Autoconsumatore Individuale a Distanza (un solo soggetto, impianto e prelievo connessi tramite rete pubblica).
- **D.Lgs. 199/2021 art. 30 c. 2** - Autoconsumatori che agiscono collettivamente (GAC); la lett. a) richiede "stesso edificio o condominio".
- **D.Lgs. 199/2021 art. 31** - Comunita' di Energia Rinnovabile: forma giuridica autonoma, finalita' non di lucro come oggetto principale, controllo da parte dei soci, soggetti ammessi.
- **D.Lgs. 199/2021 art. 32** - ARERA, contratti tra clienti finali in configurazioni di autoconsumo, ruolo del referente. NON disciplina i GAC.
- **DM 7/12/2023 art. 3** - definizioni operative, soglia 1 MW per impianti incentivati, perimetro cabina primaria (sub-configurazione incentivata).
- **DM 7/12/2023 art. 4-5** - requisiti CER, contenuti minimi statuto e atto costitutivo.
- **DM 7/12/2023 art. 7** - tariffa incentivante (TIP) per energia condivisa, struttura parte fissa + correttivo zonale, durata 20 anni.
- **DM 7/12/2023 art. 8** (testo vigente al 2026-05-07: DM 414/2023 + DM 127/2025 + DL 19/2026 art. 27) - contributo PNRR a fondo perduto per impianti in Comuni con popolazione < 50.000 abitanti, intensita' fino al 40% costo, cumulabile con TIP ridotta. Tempistiche post DL 19/2026: **stipula degli accordi di concessione lato GSE entro il 30 giugno 2026**, **entrata in esercizio entro 24 mesi dalla comunicazione dell'accordo di concessione e comunque non oltre il 31 dicembre 2027** (limite invalicabile). Erogazione articolata in tre fasi: **anticipazione fino al 30%** del contributo massimo, **quota intermedia del 40%** (richiedibile dopo aver sostenuto il 40% delle spese ammissibili e comunicato la data di avvio dei lavori) e saldo.
- **DM MASE 16 maggio 2025 n. 127** - decreto modificativo dell'art. 8 e disposizioni correlate del DM 414/2023; estende il perimetro soggettivo PNRR ai Comuni < 50.000 ab., aumenta la quota di anticipazione dal 10% al 30%, applica alle persone fisiche l'esclusione del fattore di riduzione F (par. 3 dell'Allegato 1 al Decreto CACER) sulla TIP. Nel regime DM 127/2025 il termine del 30/6/2026 era ancorato al "completamento dei lavori"; il successivo **DL 19/2026 art. 27** lo ha re-ancorato alla **stipula degli accordi di concessione** lato GSE.
- **DL 19 febbraio 2026 n. 19, art. 27** ("Decreto PNRR 2026") - re-aggancio dei termini PNRR rispetto al regime DM 127/2025: stipula degli accordi entro il 30/6/2026; 24 mesi dalla comunicazione dell'accordo per l'esercizio; 31/12/2027 limite invalicabile. Regime vigente al 2026-05-07.
- **TIAD - art. 3 e 5** - definizione e calcolo dell'energia condivisa orariamente come minimo tra immessa CACER e prelevata CACER.
- **Regole Operative CACER cap. 4-5** - flusso di qualifica, documenti, scadenze, gestione referente (versione vigente sul portale GSE).

## Convenzioni specifiche

### Cosa NON fare
- Non confondere **AID**, **GAC** e **CER**: hanno articoli, requisiti soggettivi e perimetri diversi. AID = art. 30 c. 1 lett. a) n. 2, un solo titolare; GAC = art. 30 c. 2, piu' soggetti nello stesso edificio o condominio; CER = art. 31, soggetto giuridico autonomo. Non citare l'art. 32 come fonte del GAC: art. 32 disciplina ARERA/contratti.
- Non confondere il **perimetro soggettivo/giuridico della CER** (potenzialmente multi-cabina, con piu' richieste GSE) con il **perimetro tecnico della sotto-configurazione incentivata** (che resta legato a una sola cabina primaria ai fini TIP). Non escludere a priori una CER con soci sotto cabine primarie diverse.
- Non confondere **cabina primaria** con **cabina secondaria**: il perimetro corretto per la TIP e' la cabina primaria, mappata dal GSE.
- Non quantificare la TIP con un valore unico: e' una somma di parte fissa (per fascia di potenza) e correttivo zonale legato al prezzo zonale orario; va sempre calcolata su base ora.
- Non considerare il **contributo PNRR** un incentivo automatico: nel regime vigente al 2026-05-07 (DM 414/2023 + DM 127/2025 + DL 19/2026 art. 27) vale per Comuni con popolazione < 50.000 abitanti, richiede una procedura PNRR separata, riduce la TIP per evitare doppio finanziamento, ed e' soggetto alla **stipula degli accordi di concessione lato GSE entro il 30/6/2026** e all'esercizio **entro 24 mesi dalla comunicazione dell'accordo** e comunque non oltre il 31/12/2027.
- Non confondere il **referente** della CACER (rappresentante operativo verso il GSE) con il **soggetto giuridico** CER: il referente puo' essere una ESCo o un produttore terzo.
- Non produrre testi di statuto come "definitivi": vanno formalizzati secondo la forma giuridica scelta (atto pubblico presso notaio, scrittura privata autenticata, procedure RUNTS, ecc.).
- Non riprodurre testualmente l'allegato delle Regole Operative GSE oltre la breve citazione: documento del GSE con licenza propria, citare solo il riferimento e parafrasare.
- Non accettare profili di consumo inventati: se l'utente non li fornisce, chiedere parametri o usare assunzioni dichiarate, mai numeri "tipici" non sourceati.
- Non spingersi su decisioni autorizzative dell'impianto (PAS / Comunicazione / Modello Unico / AU): la skill non ha tra le fonti il DPR 380/2001 ne' il DM 19/5/2015 sul Modello Unico; rinviare al titolo abilitativo specifico come "DA VERIFICARE" se non fornito dall'utente.

### Cosa fare
- Citare sempre la **coppia articolo + comma + lettera** (es. "art. 30 c. 2 lett. a) D.Lgs. 199/2021" per il vincolo edificio/condominio del GAC) quando si esprimono requisiti soggettivi. Per la CER, il vincolo "no grandi imprese" e i requisiti sui soci sono in art. 31 D.Lgs. 199/2021: citare il comma puntuale verificandolo sul testo vigente in `references/estratti/dlgs-199-2021-art-30-31-32.md`.
- Distinguere graficamente nelle uscite: dati certi vs stime parametriche vs voci `DA VERIFICARE CON GSE / NOTAIO / COMMERCIALISTA`.
- Per il calcolo dell'energia condivisa, dichiarare esplicitamente la formula `E_cond(h) = min(E_imm_CACER(h), E_prel_CACER(h))` e l'aggregazione oraria.
- Per la TIP, presentare lo schema `TIP(h) = parte_fissa(P) + correttivo_zonale(prezzo_zonale_h)` e rinviare al valore vigente sulla pubblicazione GSE.
- Per il contributo PNRR (regime vigente al 2026-05-07: DM 414/2023 + DM 127/2025 + DL 19/2026 art. 27), ricordare le condizioni: Comune < 50.000 ab., investimento ammissibile, riduzione parte fissa TIP; **stipula degli accordi di concessione lato GSE entro il 30/6/2026**; esercizio **entro 24 mesi dalla comunicazione dell'accordo di concessione** e comunque non oltre il 31/12/2027; anticipazione fino al 30% e successiva quota intermedia del 40% (post-spesa ammissibile sostenuta al 40%).
- Indicare sempre che la **firma dei documenti tecnici e dello statuto** spetta al professionista / referente / notaio competenti.
- Quando l'utente non fornisce i POD esatti, lavorare per ipotesi e segnalare l'esigenza della verifica cabina primaria sul portale GSE.

## Validatori

- Da identificare per Livello 2: energy manager / EGE certificato UNI CEI 11339 con esperienza in qualifica CACER.

## Stato attuale

- Versione: vedi `CHANGELOG.md` (0.1.0-alpha)
- Validazione: Livello 1 (autovalidazione interna)
- Task files: 4 (`valuta-perimetro-configurazione`, `redigi-statuto-cer`, `simula-autoconsumo-condiviso`, `predisponi-qualifica-gse`)
- Esempi: 2 (`cer-comune-piccolo-pnrr` + `gac-condominio-fotovoltaico-tetto`)
