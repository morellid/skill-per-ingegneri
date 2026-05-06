# CHANGELOG - cer-cacer-configurazione-gse

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed (review interno + 2 round di revisione adversariale Codex, 2026-05-06 / 2026-05-07)
- Mappatura corretta degli articoli del D.Lgs. 199/2021: AID = art. 30 c. 1 lett. a) n. 2, GAC = art. 30 c. 2 (con vincolo "stesso edificio o condominio" alla lett. a)), CER = art. 31, art. 32 = ARERA / contratti / referente (NON GAC).
- Recepimento del **DM MASE 16 maggio 2025 n. 127** che modifica il DM 414/2023: soglia PNRR estesa da Comuni < 5.000 ab. a Comuni < 50.000 ab.; **completamento dei lavori** entro il **30/6/2026**; **entrata in esercizio** entro **24 mesi dalla data di completamento dei lavori** e comunque entro il **31/12/2027**; erogazione PNRR articolata in **tre fasi**: anticipazione fino al 30% del contributo + quota intermedia del 40% (richiedibile dopo aver sostenuto il 40% delle spese ammissibili e comunicato l'avvio dei lavori) + saldo finale; estensione alle persone fisiche dell'esclusione del fattore di riduzione F.
- Verifica letterale dei termini sopra sulle Regole Operative GSE CACER (Allegato 1, versione 16/7/2025), in particolare lin. 2553-2555 e par. 2.2.2.1 / 2.2.3.2.
- Distinzione esplicita tra **perimetro soggettivo della CER** (potenzialmente multi-cabina) e **perimetro tecnico della sotto-configurazione incentivata** (vincolo cabina primaria ai fini TIP).
- Rimosso ogni numero "tipico" non sourceato (h_eq per FV/eolico/idro/biomassa, range `eta_share` 0.30-0.70, "30-50% per residenziale"): ora i parametri vanno dichiarati dall'utente con relativa fonte/motivazione.
- Rimosse le asserzioni sull'iter autorizzativo dell'impianto ("per 350 kW serve PAS", "Modello Unico se applicabile") che eccedevano le fonti della skill: ora marcate `DA VERIFICARE` con rinvio a DPR 380/2001 + D.Lgs. 28/2011 + DM 19/5/2015 + normativa regionale (fuori scope skill).
- Soft-end del linguaggio "atto pubblico presso notaio" come unica via di formalizzazione: ora form-dependent (atto pubblico / scrittura privata autenticata / RUNTS / ecc.).
- Sostituito il placeholder fittizio `PLACEHOLDER_TO_BE_COMPUTED_AT_FETCH` con `null` in tutti i campi `sha256` di `sources.yaml`, in linea con la convenzione del repo.
- Citazione corretta dell'art. 31 (rimosso il riferimento errato `art. 31 c. 2 lett. a)` come esempio di citazione "puntuale" dei requisiti CER nell'AGENTS.md della skill).
- Esempio GAC condominio: rimossa l'equivocazione tra art. 31 e art. 30 c. 2 sul vincolo grandi imprese; il vincolo riguarda la qualita' di socio CER, non l'autoconsumatore GAC.

### Added
- Nuova fonte `dm-mase-127-2025` in `sources.yaml`.
- Nuova fonte `gse-pnrr-cacer` (pagina GSE attuazione misure PNRR per CACER < 50.000 ab.).

## [0.1.0-alpha] - 2026-05-06

### Added
- Prima versione alpha della skill `cer-cacer-configurazione-gse`.
- Task files:
  - `valuta-perimetro-configurazione.md` - verifica cabina primaria + scelta AID/GAC/CER.
  - `redigi-statuto-cer.md` - bozza statuto/atto costitutivo CER (DM 7/12/2023 art. 4-5).
  - `simula-autoconsumo-condiviso.md` - calcolo semplificato energia condivisa, TIP, TR, contributo PNRR.
  - `predisponi-qualifica-gse.md` - checklist documentale per qualifica al servizio CACER.
- Fonti normative catalogate in `references/sources.yaml`:
  - D.Lgs. 199/2021 art. 30-32
  - DM MASE 7 dicembre 2023 n. 414
  - Delibera ARERA 727/2022/R/eel (TIAD)
  - Regole Operative CACER del GSE (Allegato 1)
- Esempi:
  - `cer-comune-piccolo-pnrr` - CER su Comune piccolo (1.812 ab.) con cumulo TIP + contributo PNRR.
  - `gac-condominio-fotovoltaico-tetto` - Gruppo Autoconsumatori condominiale con FV in copertura.

### Note di sviluppo
- Skill non ancora validata da dominio terzo (energy manager / EGE indipendente).
- Da considerare draft finche' non passa validazione Livello 2 (vedi `methodology/validazione.md`).
- Verificare aggiornamenti TIAD ARERA e Regole Operative GSE prima dell'uso operativo: il framework CACER e' stato oggetto di aggiornamenti frequenti dopo l'avvio del servizio (gennaio 2024), incluso il DM MASE 127/2025.
