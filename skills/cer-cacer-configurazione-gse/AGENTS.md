# AGENTS.md - cer-cacer-configurazione-gse

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

La skill copre la **configurazione** e la **qualifica al servizio CACER del GSE** delle tre forme di autoconsumo diffuso disciplinate dal D.Lgs. 199/2021: **Autoconsumatore Individuale a Distanza (AID)**, **Gruppo di Autoconsumatori (GAC)**, **Comunita' di Energia Rinnovabile (CER)**. Riferimento normativo principale: **DM MASE 7 dicembre 2023 n. 414** + **Regole Operative CACER del GSE** + **TIAD ARERA 727/2022/R/eel**.

Target: ingegneri / energy manager / EGE / ESCo / consulenti GSE / enti locali e amministratori di condominio.

## Fonti autoritative

Le fonti sono catalogate in `references/sources.yaml`. Per ognuna sono presenti URL ufficiale, data di consultazione, hash SHA256 del binario archiviato in `not_in_repo/` e licenza.

- **D.Lgs. 199/2021** (recepimento direttiva RED II) - id `dlgs-199-2021`
- **DM MASE 7 dicembre 2023 n. 414** (Decreto CACER) - id `dm-mase-414-2023`
- **Delibera ARERA 727/2022/R/eel - TIAD** - id `delibera-arera-727-2022-tiad`
- **Regole Operative CACER del GSE - Allegato 1** - id `gse-regole-operative-cacer`

Estratti pertinenti gia' preparati in `references/estratti/`:
- `dlgs-199-2021-art-30-31-32.md` - definizioni AID, GAC, CER e requisiti soggettivi.
- `dm-mase-414-2023.md` - perimetro cabina primaria, soglie potenza, TIP, contributo PNRR per Comuni < 5.000 ab.
- `tiad-arera-727-2022.md` - regolazione flussi e calcolo energia condivisa oraria.
- `gse-regole-operative-cacer.md` - flusso di qualifica, documenti, ruolo del referente.

## Articoli e punti chiave

Quando l'agent produce output deve citare il riferimento puntuale, non la legge in generale.

- **D.Lgs. 199/2021 art. 30** - Autoconsumatore Individuale a Distanza (un solo soggetto, impianto e prelievo connessi tramite rete pubblica).
- **D.Lgs. 199/2021 art. 31** - Comunita' di Energia Rinnovabile: forma giuridica autonoma, finalita' non di lucro come oggetto principale, controllo da parte dei soci, soggetti ammessi.
- **D.Lgs. 199/2021 art. 32** - Gruppi di Autoconsumatori che agiscono collettivamente (stesso edificio o condominio, accordo privato).
- **DM 7/12/2023 art. 3** - definizioni operative, soglia 1 MW per impianti incentivati, perimetro cabina primaria.
- **DM 7/12/2023 art. 4-5** - requisiti CER, contenuti minimi statuto e atto costitutivo.
- **DM 7/12/2023 art. 7** - tariffa incentivante (TIP) per energia condivisa, struttura parte fissa + correttivo zonale, durata 20 anni.
- **DM 7/12/2023 art. 8** - contributo PNRR a fondo perduto per impianti in Comuni con popolazione < 5.000 abitanti, intensita' fino al 40% costo, cumulabile con TIP ridotta.
- **TIAD - art. 3 e 5** - definizione e calcolo dell'energia condivisa orariamente come minimo tra immessa CACER e prelevata CACER.
- **Regole Operative CACER cap. 4-5** - flusso di qualifica, documenti, scadenze, gestione referente.

## Convenzioni specifiche

### Cosa NON fare
- Non confondere **AID**, **GAC** e **CER**: hanno requisiti soggettivi e perimetri diversi. AID = un solo titolare; GAC = piu' soggetti nello stesso edificio/condominio; CER = soggetto giuridico autonomo, soci anche distanti ma nella stessa cabina primaria.
- Non confondere **cabina primaria** (perimetro CACER per accesso TIP) con **cabina secondaria**: il perimetro corretto e' la cabina primaria, mappata dal GSE.
- Non quantificare la TIP con un valore unico: e' una somma di parte fissa (per fascia di potenza) e correttivo zonale legato al prezzo zonale orario; va sempre calcolata su base ora.
- Non considerare il **contributo PNRR** un incentivo automatico: vale solo per Comuni < 5.000 ab., richiede una procedura PNRR separata e riduce la TIP per evitare doppio finanziamento.
- Non confondere il **referente** della CACER (rappresentante operativo verso il GSE) con il **soggetto giuridico** CER: il referente puo' essere una ESCo o un produttore terzo.
- Non produrre testi di statuto come "definitivi": vanno sempre passati al notaio per atto pubblico.
- Non riprodurre testualmente l'allegato delle Regole Operative GSE oltre la breve citazione: documento del GSE con licenza propria, citare solo il riferimento e parafrasare.
- Non accettare profili di consumo inventati: se l'utente non li fornisce, usare assunzioni parametriche (es. fattori di simultaneita' tipici) ed esplicitarle.

### Cosa fare
- Citare sempre la coppia **art. + comma** (es. "art. 31 c. 2 lett. a) D.Lgs. 199/2021") quando si esprimono requisiti soggettivi della CER.
- Distinguere graficamente nelle uscite: dati certi vs stime parametriche vs voci `DA VERIFICARE CON GSE / NOTAIO / COMMERCIALISTA`.
- Per il calcolo dell'energia condivisa, dichiarare esplicitamente la formula `E_cond(h) = min(E_imm_CACER(h), E_prel_CACER(h))` e l'aggregazione oraria.
- Per la TIP, presentare lo schema `TIP(h) = parte_fissa(P) + correttivo_zonale(prezzo_zonale_h)` e rinviare al valore vigente sulla pubblicazione GSE.
- Per il contributo PNRR, ricordare le condizioni: Comune < 5.000 ab., investimento ammissibile, riduzione TIP, scadenze PNRR.
- Indicare sempre che la **firma dei documenti tecnici e dello statuto** spetta al professionista / referente / notaio competenti.
- Quando l'utente non fornisce i POD esatti, lavorare per ipotesi e segnalare l'esigenza della verifica cabina primaria sul portale GSE.

## Validatori

- Da identificare per Livello 2: energy manager / EGE certificato UNI CEI 11339 con esperienza in qualifica CACER.

## Stato attuale

- Versione: vedi `CHANGELOG.md` (0.1.0-alpha)
- Validazione: Livello 1 (autovalidazione interna)
- Task files: 4 (`valuta-perimetro-configurazione`, `redigi-statuto-cer`, `simula-autoconsumo-condiviso`, `predisponi-qualifica-gse`)
- Esempi: 2 (`cer-comune-piccolo-pnrr` + `gac-condominio-fotovoltaico-tetto`)
