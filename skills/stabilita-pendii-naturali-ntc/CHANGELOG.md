# CHANGELOG - stabilita-pendii-naturali-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-20

### Added (closes #409)
- Prima versione della skill di supporto al **progettista geotecnico** e al **geologo** per l'**inquadramento
  dello studio e della verifica di stabilita' dei pendii naturali** secondo le **NTC 2018** (DM 17 gennaio
  2018), **paragrafo 6.3**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 6.3 estratto con `pdftotext -layout` (pp. GU 187-188) e trascritto verbatim in
    `references/fonti/ntc2018-par-6-3.md`.
- Estratto operativo `references/estratti/stabilita-pendii-checklist.md`.
- Due task: `inquadra-verifica-stabilita-pendio.md` e `inquadra-indagini-interventi-monitoraggio.md`.
- Due esempi: coefficiente di sicurezza F = tau_f/tau su valori caratteristici (illustrazione F = 60/40 = 1,5);
  criterio di scelta delle superfici di scorrimento per un pendio in frana e per un pendio non in frana.

### Contenuto ancorato al testo
- Ambito (§6.3): pendii naturali, anche in condizioni sismiche (rinvio §7.11.3.5); interventi di
  stabilizzazione. Prescrizioni generali e indagini (§6.3.1): osservazioni e rilievi di superficie, notizie
  storiche, movimenti in atto, dati idrogeologici/pluviometrici, verifiche su specifiche indagini geotecniche.
  Modellazione geologica (§6.3.2) e geotecnica (§6.3.3): rilievo plano-altimetrico esteso a monte e valle,
  successione stratigrafica, pressioni interstiziali, superficie/i di scorrimento, numero minimo di verticali,
  modello geotecnico di sottosuolo (§6.2.2). Verifiche di sicurezza (§6.3.4): coefficiente di sicurezza
  F = tau_f/tau (resistenza al taglio disponibile / tensione di taglio agente) lungo la superficie di
  scorrimento, con parametri geotecnici e azioni al VALORE CARATTERISTICO (a differenza degli altri interventi
  geotecnici, non si applicano i coefficienti parziali A1/A2, M ed R); pendii in frana lungo le superfici
  accertate, altrimenti ricerca della superficie critica (grado di sicurezza piu' basso); pressioni
  interstiziali nelle condizioni piu' sfavorevoli; margine di sicurezza accettabile giustificato dal
  progettista (livello di conoscenze, affidabilita' dei dati, modello di calcolo, conseguenze di
  un'eventuale frana). Interventi di stabilizzazione (§6.3.5) e controlli/monitoraggio (§6.3.6): spostamenti,
  pressioni interstiziali, soglie di attenzione e di allarme.

### Scope e limiti
- Non calcola il coefficiente di sicurezza né esegue le verifiche (metodi dell'equilibrio limite/numerici), non
  definisce il modello geologico/geotecnico né progetta gli interventi, non tratta la stabilita' sismica
  (§7.11.3.5) né le opere in materiali sciolti/fronti di scavo (§6.8), non riproduce la Circolare 21/1/2019
  n. 7. Non sostituisce il progettista geotecnico/geologo.

### Note di sviluppo
- Complementa `opere-sostegno-ntc` (§6.5), `tiranti-ancoraggio-ntc` (§6.6) e `relazione-geologica-geotecnica-ntc`
  (che esclude i §6.3-6.12), condividendo la stessa fonte GU. Validazione Livello 2 con ingegnere
  geotecnico/geologo.
