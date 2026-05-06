# AGENTS.md - cer-cacer-configurazione-gse

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

La skill copre la **configurazione** e la **qualifica al servizio CACER del GSE** delle tre forme di autoconsumo diffuso disciplinate dal D.Lgs. 199/2021:

- **Autoconsumatore Individuale a Distanza (AID)** - art. 30 c. 1 lett. a) n. 2;
- **Gruppo di Autoconsumatori (GAC)** - art. 30 c. 2 (con vincolo "stesso edificio o condominio" alla lett. a));
- **Comunita' di Energia Rinnovabile (CER)** - art. 31.

L'art. 32 disciplina il quadro regolatorio (ARERA, contratti, ruolo del referente), non i GAC.

Riferimenti normativi principali: **DM MASE 7 dicembre 2023 n. 414** come modificato dal **DM MASE 16 maggio 2025 n. 127** (estensione perimetro PNRR ai Comuni < 50.000 ab., nuove scadenze, anticipo al 30%) + **Regole Operative CACER del GSE** + **TIAD ARERA 727/2022/R/eel**.

Target: ingegneri / energy manager / EGE / ESCo / consulenti GSE / enti locali e amministratori di condominio.

## Fonti autoritative

Le fonti sono catalogate in `references/sources.yaml`. Per ognuna sono presenti URL ufficiale, data di consultazione, hash SHA256 del binario archiviato in `not_in_repo/` e licenza.

- **D.Lgs. 199/2021** (recepimento direttiva RED II) - id `dlgs-199-2021`
- **DM MASE 7 dicembre 2023 n. 414** (Decreto CACER, testo originario) - id `dm-mase-414-2023`
- **DM MASE 16 maggio 2025 n. 127** (modifiche al DM 414/2023) - id `dm-mase-127-2025`
- **Delibera ARERA 727/2022/R/eel - TIAD** - id `delibera-arera-727-2022-tiad`
- **Regole Operative CACER del GSE - Allegato 1** - id `gse-regole-operative-cacer`
- **GSE - Pagina misura PNRR CACER < 50.000 ab.** - id `gse-pnrr-cacer`

Estratti pertinenti gia' preparati in `references/estratti/`:
- `dlgs-199-2021-art-30-31-32.md` - mappatura corretta degli articoli (AID art. 30 c. 1 lett. a) n. 2, GAC art. 30 c. 2, CER art. 31, ARERA/contratti art. 32) e requisiti soggettivi.
- `dm-mase-414-2023.md` - perimetro cabina primaria (incentivo), soglie potenza, TIP, contributo PNRR nel **regime vigente post DM 127/2025** (Comuni < 50.000 ab., scadenze 30/6/2026 e 31/12/2027, anticipo 30%).
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
- **DM 7/12/2023 art. 8** (testo vigente post DM 127/2025) - contributo PNRR a fondo perduto per impianti in Comuni con popolazione < 50.000 abitanti, intensita' fino al 40% costo, cumulabile con TIP ridotta. Scadenza accordi di concessione 30/6/2026, esercizio entro 24 mesi e comunque entro 31/12/2027, anticipo richiedibile 30%.
- **DM MASE 127/2025** - decreto modificativo dell'art. 8 e disposizioni correlate del DM 414/2023; estende il perimetro soggettivo PNRR e applica alle persone fisiche l'esclusione del fattore di riduzione F sulla TIP.
- **TIAD - art. 3 e 5** - definizione e calcolo dell'energia condivisa orariamente come minimo tra immessa CACER e prelevata CACER.
- **Regole Operative CACER cap. 4-5** - flusso di qualifica, documenti, scadenze, gestione referente (versione vigente sul portale GSE).

## Convenzioni specifiche

### Cosa NON fare
- Non confondere **AID**, **GAC** e **CER**: hanno articoli, requisiti soggettivi e perimetri diversi. AID = art. 30 c. 1 lett. a) n. 2, un solo titolare; GAC = art. 30 c. 2, piu' soggetti nello stesso edificio o condominio; CER = art. 31, soggetto giuridico autonomo. Non citare l'art. 32 come fonte del GAC: art. 32 disciplina ARERA/contratti.
- Non confondere il **perimetro soggettivo/giuridico della CER** (potenzialmente multi-cabina, con piu' richieste GSE) con il **perimetro tecnico della sotto-configurazione incentivata** (che resta legato a una sola cabina primaria ai fini TIP). Non escludere a priori una CER con soci sotto cabine primarie diverse.
- Non confondere **cabina primaria** con **cabina secondaria**: il perimetro corretto per la TIP e' la cabina primaria, mappata dal GSE.
- Non quantificare la TIP con un valore unico: e' una somma di parte fissa (per fascia di potenza) e correttivo zonale legato al prezzo zonale orario; va sempre calcolata su base ora.
- Non considerare il **contributo PNRR** un incentivo automatico: nel regime vigente post **DM 127/2025** vale per Comuni con popolazione < 50.000 abitanti, richiede una procedura PNRR separata, riduce la TIP per evitare doppio finanziamento, ed e' soggetto alle scadenze 30/6/2026 (accordi) e 31/12/2027 (esercizio).
- Non confondere il **referente** della CACER (rappresentante operativo verso il GSE) con il **soggetto giuridico** CER: il referente puo' essere una ESCo o un produttore terzo.
- Non produrre testi di statuto come "definitivi": vanno formalizzati secondo la forma giuridica scelta (atto pubblico presso notaio, scrittura privata autenticata, procedure RUNTS, ecc.).
- Non riprodurre testualmente l'allegato delle Regole Operative GSE oltre la breve citazione: documento del GSE con licenza propria, citare solo il riferimento e parafrasare.
- Non accettare profili di consumo inventati: se l'utente non li fornisce, chiedere parametri o usare assunzioni dichiarate, mai numeri "tipici" non sourceati.
- Non spingersi su decisioni autorizzative dell'impianto (PAS / Comunicazione / Modello Unico / AU): la skill non ha tra le fonti il DPR 380/2001 ne' il DM 19/5/2015 sul Modello Unico; rinviare al titolo abilitativo specifico come "DA VERIFICARE" se non fornito dall'utente.

### Cosa fare
- Citare sempre la coppia **art. + comma** (es. "art. 31 c. 2 lett. a) D.Lgs. 199/2021") quando si esprimono requisiti soggettivi della CER.
- Distinguere graficamente nelle uscite: dati certi vs stime parametriche vs voci `DA VERIFICARE CON GSE / NOTAIO / COMMERCIALISTA`.
- Per il calcolo dell'energia condivisa, dichiarare esplicitamente la formula `E_cond(h) = min(E_imm_CACER(h), E_prel_CACER(h))` e l'aggregazione oraria.
- Per la TIP, presentare lo schema `TIP(h) = parte_fissa(P) + correttivo_zonale(prezzo_zonale_h)` e rinviare al valore vigente sulla pubblicazione GSE.
- Per il contributo PNRR (regime vigente post DM 127/2025), ricordare le condizioni: Comune < 50.000 ab., investimento ammissibile, riduzione parte fissa TIP, scadenze 30/6/2026 e 31/12/2027, anticipo fino al 30%.
- Indicare sempre che la **firma dei documenti tecnici e dello statuto** spetta al professionista / referente / notaio competenti.
- Quando l'utente non fornisce i POD esatti, lavorare per ipotesi e segnalare l'esigenza della verifica cabina primaria sul portale GSE.

## Validatori

- Da identificare per Livello 2: energy manager / EGE certificato UNI CEI 11339 con esperienza in qualifica CACER.

## Stato attuale

- Versione: vedi `CHANGELOG.md` (0.1.0-alpha)
- Validazione: Livello 1 (autovalidazione interna)
- Task files: 4 (`valuta-perimetro-configurazione`, `redigi-statuto-cer`, `simula-autoconsumo-condiviso`, `predisponi-qualifica-gse`)
- Esempi: 2 (`cer-comune-piccolo-pnrr` + `gac-condominio-fotovoltaico-tetto`)
