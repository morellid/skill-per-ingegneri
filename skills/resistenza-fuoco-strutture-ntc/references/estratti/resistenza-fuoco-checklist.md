# Estratto operativo - Resistenza al fuoco delle strutture (NTC 2018 §3.6.1)

> Parafrasi ancorata a `references/fonti/ntc2018-par-3-6-1.md`. Ogni voce cita il paragrafo/tabella/formula
> NTC. La skill **inquadra** definizioni, prestazioni, classi, curve e verifiche; **non** calcola il carico
> d'incendio (rinvio DM 9/3/2007) né esegue le analisi termiche/meccaniche.

## 1. Definizioni (§3.6.1.1)

- **Capacità portante (R)**: attitudine della struttura a conservare resistenza meccanica sotto il fuoco.
- **Capacità di compartimentazione**: stabilità + **isolamento termico (I)** + **tenuta (E)** ai fumi/gas.
- **Resistenza al fuoco**: capacità portante + compartimentazione degli elementi di separazione.
- **Carico d'incendio specifico di progetto**: **qf,d = qf · δq1 · δq2 · δn** [3.6.1], con:
  - **qf** = carico d'incendio nominale [MJ/m²];
  - **δq1 ≥ 1,00** (rischio in relazione alla superficie del compartimento);
  - **δq2 ≥ 0,80** (rischio in relazione al tipo di attività);
  - **δn = Π δni ≥ 0,20** (misure di protezione: estinzione automatica, rivelatori, idranti, squadre…).
  - Il **calcolo di dettaglio** dei fattori è nel **DM 9 marzo 2007** (fuori scope).

## 2. Richieste di prestazione (§3.6.1.2, Tab. 3.5.IV)

| Livello | Prestazione |
|---|---|
| **I** | Nessun requisito (collasso accettabile / rischio trascurabile). |
| **II** | Resistenza per il tempo di **evacuazione** in luogo sicuro. |
| **III** | Resistenza per il tempo congruo con la **gestione dell'emergenza**. |
| **IV** | **Limitato danneggiamento** dopo l'incendio. |
| **V** | **Totale funzionalità** dopo l'incendio. |

- Per attività soggette al controllo VVF o con regole tecniche di prevenzione incendi, livelli e classi sono
  fissati dalle disposizioni del Ministero dell'Interno (**D.Lgs. 139/2006**).

## 3. Classi di resistenza al fuoco (§3.6.1.3)

- **15, 20, 30, 45, 60, 90, 120, 180, 240, 360** → **tempo in minuti primi** durante il quale la resistenza al
  fuoco deve essere garantita, riferite alle **curve nominali**.

## 4. Procedura di analisi (§3.6.1.5)

Passi: (1) individuare l'**incendio di progetto**; (2) analisi dell'**evoluzione della temperatura**; (3)
analisi del **comportamento meccanico**; (4) **verifiche di sicurezza**.

- **Incendio di progetto** (§3.6.1.5.1): curva **nominale** (per il tempo pari alla classe, senza
  raffreddamento) o **naturale** (intera durata, incl. raffreddamento). Curve nominali:
  - **standard** (cellulosici): **θg = 20 + 345·log10(8t + 1)** [°C] [3.6.2];
  - **idrocarburi**: **θg = 1080·(1 − 0,325·e^(−0,167t) − 0,675·e^(−2,5t)) + 20** [3.6.3];
  - **esterna**: **θg = 660·(1 − 0,687·e^(−0,32t) − 0,313·e^(−3,8t)) + 20** [3.6.4].
- **Evoluzione della temperatura** (§3.6.1.5.2): propagazione del calore (irraggiamento/convezione), eventuali
  materiali protettivi.
- **Comportamento meccanico** (§3.6.1.5.3): riduzione della resistenza dei materiali con la temperatura;
  azioni in **combinazione eccezionale** (permanenti + variabili concomitanti); no concomitanza con altre
  eccezionali o sisma; sollecitazioni indirette (dilatazioni contrastate) ove non trascurabili.
- **Verifiche di sicurezza** (§3.6.1.5.4): resistenza meccanica mantenuta per il **tempo della classe** (curva
  nominale) o per l'intera durata (curva naturale).

## Cosa la skill NON fa

- **Non calcola** il carico d'incendio (i fattori δni sono nel **DM 9/3/2007**) né esegue le **analisi
  termiche/meccaniche**; **non** fornisce le proprietà dei materiali ad alta temperatura (**Eurocodici parte
  1-2**).
- **Non individua** le classi/livelli specifici delle **regole tecniche VVF** (D.Lgs 139/2006, DM 3/8/2015 RTO);
  **non** sostituisce il progettista strutturale né il professionista antincendio.
- **Non tratta** la prevenzione incendi come procedimento amministrativo (→ skill
  `prevenzione-incendi-attivita-procedimenti-dpr151`).
