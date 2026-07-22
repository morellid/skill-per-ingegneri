# vita-nominale-classi-uso-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista** per l'**inquadramento della vita nominale di progetto V_N,
delle classi d'uso e del periodo di riferimento per l'azione sismica V_R** secondo le **NTC 2018** (D.M. 17
gennaio 2018), **paragrafo 2.4**.

**Non definisce** lo spettro di risposta né **calcola** i periodi di ritorno T_R degli stati limite (§3.2) e
**non sostituisce** il progettista: fornisce i valori tabellari (V_N 10/50/100 anni, C_U 0,7/1,0/1,5/2,0) e la
formula V_R = V_N · C_U [2.4.1].

## Target

Ingegneri e tecnici che, all'avvio di un progetto strutturale, devono dichiarare la **vita nominale di progetto**,
la **classe d'uso** e il **periodo di riferimento per l'azione sismica** della costruzione secondo le NTC 2018
par. 2.4.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-vita-nominale-classe-uso` | Fissa V_N (Tab. 2.4.I: 10/50/100 anni, fase di costruzione ≥ P_N e ≥ 5 anni) e la classe d'uso I-IV (§2.4.1, §2.4.2) |
| `inquadra-periodo-riferimento-vr` | Ricava V_R = V_N·C_U [2.4.1] con C_U (Tab. 2.4.II: 0,7/1,0/1,5/2,0) e ne indica l'uso a valle verso il §3.2 (§2.4.3) |

Nucleo: la vita nominale **V_N** (Tab. 2.4.I), la **classe d'uso** I-IV (§2.4.2) e il periodo di riferimento
**V_R = V_N · C_U** [2.4.1] con il coefficiente d'uso **C_U** della Tab. 2.4.II.

## Relazione con altre skill

- **A monte** di `spettro-risposta-ntc` (§3.2): V_R è il periodo di riferimento da cui si ricavano i periodi di
  ritorno T_R e lo spettro. Nessuna altra skill inquadra V_N/C_U/V_R. Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 2.4.1-2.4.3** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim; la formula [2.4.1] e le Tab. 2.4.I/2.4.II verificate anche sull'immagine della pagina.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non definisce** lo **spettro di risposta** né i **periodi di ritorno T_R** / le probabilità di superamento
  degli stati limite (§3.2).
- **Non tratta** la valutazione delle **opere esistenti** né le **combinazioni delle azioni** (§2.5).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista, né la lettura diretta del par. 2.4 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
