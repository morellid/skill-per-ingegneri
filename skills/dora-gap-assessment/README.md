# DORA Gap Assessment - Reg. (UE) 2022/2554

> Versione: 0.1.0-alpha
> Stato: alpha (validazione di Livello 1 - autore + adversarial review)

Skill di supporto al gap assessment di un'entita' finanziaria UE rispetto al Regolamento (UE) 2022/2554 (DORA - Digital Operational Resilience Act), direttamente applicabile in Italia dal 17/01/2025.

## Target

CISO, ICT risk manager, compliance officer, internal auditor di entita' finanziarie (banca, istituto di pagamento, istituto di moneta elettronica, impresa di investimento, impresa di assicurazione/riassicurazione, gestore di FIA, depositario centrale di titoli, controparte centrale, prestatore di servizi crittoasset MiCA, ecc.) e consulenti che li supportano nella preparazione/aggiornamento del proprio quadro DORA.

**Non destinata a**: autorita' di sorveglianza, fornitori critici TIC dal lato sorveglianza (Capo V Sez. II di DORA - fuori scope).

## Cosa fa

Per ciascuno dei 5 Pillar di DORA, la skill:

1. Richiede all'utente l'identificazione dell'entita' (categoria DORA, applicabilita' del quadro semplificato art. 16, qualifica di microimpresa, ecc.).
2. Richiede gli input documentali e operativi del Pillar selezionato.
3. Per ciascun obbligo DORA del Pillar, classifica lo stato: **CONFORME** / **PARZIALE** / **NON CONFORME** / **NON APPLICABILE** (con motivazione).
4. Produce un report markdown con sintesi, dettaglio per area, punti che richiedono il giudizio del professionista, e avvertenza.

Sotto-attivita' (file in `tasks/`):

- **Pillar 1 - Gestione del rischio TIC** (DORA artt. 5-16): governance, quadro, sistemi, identificazione, protezione, individuazione, risposta/ripristino, backup, formazione, comunicazione. 57 voci di controllo + 8 specifiche per quadro semplificato. [`tasks/check-pillar-1-ict-risk-mgmt.md`]
- **Pillar 2 - Incidenti** (artt. 17-23): processo di gestione, classificazione, segnalazione (iniziale/intermedia/finale), comunicazione clienti, estensione pagamenti. 20 voci. [`tasks/check-pillar-2-incidents.md`]
- **Pillar 3 - Testing** (artt. 24-27): programma di test, test di sistemi, TLPT, requisiti dei tester. 22 voci. [`tasks/check-pillar-3-testing.md`]
- **Pillar 4 - Fornitori terzi TIC** (artt. 28-30): strategia, registro delle informazioni, valutazione preliminare, rischio di concentrazione, clausole contrattuali minime, strategie di uscita. 42 voci. [`tasks/check-pillar-4-third-party.md`]
- **Pillar 5 - Condivisione informazioni** (art. 45): facolta' di partecipazione ai meccanismi, requisiti, notifica all'autorita'. 10 voci. [`tasks/check-pillar-5-info-sharing.md`]

Per il dettaglio operativo vedi `SKILL.md`.

## Installazione

Vedi `README.md` alla root del repo per istruzioni generali di installazione delle skill in Claude Code e in OpenAI Codex.

## Fonti consultate

- **Regolamento (UE) 2022/2554 (DORA)** - testo PE-CONS 41/22 (trilogue-finale, identico in contenuto a GU UE L 333 del 27/12/2022).
  - Dettagli: `references/sources.yaml` (id `reg-ue-2022-2554-dora`, SHA256 verificato).
  - Trascrizione integrale degli artt. 1-30, 45, 64 in `references/fonti/reg-ue-2022-2554-dora.md`.
  - Estratti curati per pillar in `references/estratti/reg-ue-2022-2554-dora.md`.

## Limiti noti

La skill **non**:

- Sostituisce il giudizio del professionista responsabile sui confini interpretativi (art. 4 proporzionalita', art. 16 quadro semplificato, qualificazione di "funzione essenziale o importante" art. 3 n. 22, di "grave incidente TIC" art. 3 n. 10, di "minaccia significativa" art. 3 n. 13).
- Produce documenti pronti al deposito presso autorita' competenti ne' attestazioni di conformita'.
- Copre il Capo V Sez. II (artt. 31-44, sorveglianza dei fornitori critici dal lato autorita') ne' il Capo VII (autorita' competenti, artt. 46-56) ne' le disposizioni sanzionatorie/finali (Capo VIII salvo art. 64).
- Valuta gli RTS/ITS DORA di secondo livello (rinvii negli artt. 15, 16, 18, 20, 26, 28, 30).
- Produce mappature verso framework esterni (NIS2, ISO/IEC 27001, NIST CSF, EBA ICT Guidelines).
- Genera documenti di policy interna pronti per la firma del CISO o dell'organo di gestione.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
