# CHANGELOG - marcatura-ce-elettrici-lvd-emc-red

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-15

### Added (closes #60)
- Prima versione della skill di supporto documentale alla marcatura CE dei
  prodotti elettrici/elettronici secondo LVD 2014/35/UE, EMC 2014/30/UE e RED
  2014/53/UE.
- Fonti lette e trascritte (Regola zero), tutte su eur-lex e trattate come
  **online-only** (`binary_path: null`, `sha256: null`): eur-lex non e'
  riproducibile con hash stabile e blocca gli IP datacenter di GitHub Actions
  (stesso approccio della skill ai-act-compliance):
  - **Dir. 2014/35/UE (LVD)** - campo (art. 1), obiettivi di sicurezza (all. I),
    Modulo A (all. III), dichiarazione UE (all. IV): `dir-2014-35-lvd.md`.
  - **Dir. 2014/30/UE (EMC)** - requisiti essenziali (all. I), procedure (art. 14),
    Moduli A e B+C (all. II-III): `dir-2014-30-emc.md`.
  - **Dir. 2014/53/UE (RED)** - requisiti essenziali (art. 3), procedure (art. 17),
    Moduli A/B+C/H (all. II-IV), documentazione e dichiarazioni (all. V-VII):
    `dir-2014-53-red.md`.
- Estratto operativo `references/estratti/marcatura-ce-elettrici-checklist.md`.
- Due task: `individua-direttive.md` e `scegli-procedura-conformita.md`.
- Due esempi: alimentatore da rete (LVD + EMC, Modulo A) e apparecchiatura radio
  (RED, scelta del modulo e organismo notificato).

### Note di source-grounding e scope
- La skill lavora a **livello di direttiva** (ambito, moduli, documentazione,
  marcatura CE). Le **norme armonizzate** (EN a pagamento) danno presunzione di
  conformita' e sono citate, non riprodotte. Le **prove** e la responsabilita'
  della conformita' restano al fabbricante/laboratorio/organismo notificato.
- Recepimenti nazionali: D.Lgs. 86/2016 (LVD), 80/2016 (EMC), 128/2016 (RED)
  (citati come riferimento).

### Note di sviluppo
- Fonti eur-lex online-only: a ogni aggiornamento rileggere gli articoli/allegati
  citati (ed eventuali atti delegati, es. RED sul caricabatterie comune - dir.
  2022/2380).
- Validazione Livello 2 da effettuare con esperto marcatura CE elettrica.
