# cra-segnalazione-art14

> Versione: 0.1.0-alpha
> Stato: in sviluppo (Livello 1, autore + review adversariale)

Skill di supporto agli **obblighi di segnalazione di vulnerabilita' attivamente sfruttate e incidenti gravi** posti al fabbricante di prodotti con elementi digitali (PDE) dall'**art. 14 del Regolamento (UE) 2024/2847 - Cyber Resilience Act (CRA)**, applicabili **dall'11 settembre 2026** ai sensi dell'art. 71, par. 2.

## Target

Security engineer e PSIRT, ingegneri di prodotto e firmware, responsabili tecnici e compliance manager del fabbricante che devono decidere se un evento fa scattare l'obbligo di notifica, entro quando, a chi e con quale contenuto.

## Cosa fa

Quattro sotto-attivita':

1. **Qualificare l'evento** (`tasks/qualifica-evento-segnalabile.md`): applica la definizione di "vulnerabilita' attivamente sfruttata" (art. 3, punto 42) e il doppio test dell'incidente grave (art. 6, punto 6, NIS2 + art. 14, par. 5), e fissa il momento da cui decorrono le 24 ore.
2. **Costruire la sequenza degli adempimenti** (`tasks/costruisci-sequenza-notifiche.md`): timeline datata delle due catene (24h / 72h / 14 giorni dal rimedio per le vulnerabilita'; 24h / 72h / un mese dalla trasmissione per gli incidenti) e contenuto minimo di ciascuna notifica, separando cio' che e' dovuto da cio' che e' condizionato.
3. **Individuare il CSIRT coordinatore** (`tasks/individua-csirt-coordinatore.md`): criterio dello stabilimento principale e cascata a)-d) dell'art. 14, par. 7; per l'Italia, CSIRT Italia presso ACN (art. 16, c. 1, D.Lgs. 138/2024).
4. **Verificare i prerequisiti interni** (`tasks/check-prerequisiti-interni.md`): punto di contatto, politica CVD, SBOM, registro delle vulnerabilita' con data e ora di ricezione, canale verso gli utilizzatori.

## Cosa NON fa (limiti noti)

- **Non descrive la registrazione o l'accesso alla piattaforma unica di segnalazione dell'art. 16: e' fuori scope in v0.1 perche' le fonti normative lette non lo disciplinano.** L'art. 16, par. 1, dice solo che l'ENISA la istituisce e che Stati membri ed ENISA predispongono i propri terminali. Nessun testo su account, credenziali, onboarding o URL. Va verificato sui canali ufficiali ENISA e ACN/CSIRT Italia.
- Non trasmette notifiche e non produce documenti pronti all'invio: struttura il contenuto minimo dovuto.
- Non fissa il formato delle notifiche: l'atto di esecuzione dell'art. 14, par. 10, e' una facolta' della Commissione, e questa skill non ha verificato ne' letto eventuali atti adottati in base a quel paragrafo. Lo stesso vale per l'atto delegato dell'art. 14, par. 9.
- Non nomina i CSIRT coordinatori di Stati membri diversi dall'Italia: le designazioni nazionali NIS2 non sono fra le fonti lette.
- Non classifica il PDE ne' valuta la conformita': usa `cra-classificazione-pde`.
- Non copre gli obblighi di notifica del D.Lgs. 138/2024 (NIS2) e non stabilisce equivalenze fra i due regimi: di quel decreto sono stati letti i soli artt. 2, 15 e 16, non le disposizioni che ne definiscono l'ambito soggettivo.
- Non esegue il triage tecnico della vulnerabilita' ne' valuta l'attendibilita' forense delle prove di sfruttamento.
- Non quantifica il rischio sanzionatorio: riporta i massimali dell'art. 64 e segnala i due punti di coordinamento che il testo lascia aperti (portata della deroga del par. 10; data di applicazione dell'art. 64) senza risolverli.
- Non cita la politica nazionale di divulgazione coordinata delle vulnerabilita' ex art. 16, c. 4, D.Lgs. 138/2024, ne' il D.L. 82/2021: citati dalle fonti, non letti.

## Installazione

Per installare la skill in Claude Code:

```bash
ln -s "$(pwd)/skills/cra-segnalazione-art14" "$HOME/.claude/skills/cra-segnalazione-art14"
```

Per Codex (OpenAI):

```bash
ln -s "$(pwd)/skills/cra-segnalazione-art14" "$HOME/.agents/skills/cra-segnalazione-art14"
```

## Fonti consultate

- **Regolamento (UE) 2024/2847** del Parlamento europeo e del Consiglio del 23 ottobre 2024 (Cyber Resilience Act) - CELEX 32024R2847. ELI: <http://data.europa.eu/eli/reg/2024/2847/oj>.
- **Direttiva (UE) 2022/2555** (NIS2) - CELEX 32022L2555: richiamata dall'art. 3, punti 43 e 45, del CRA per le definizioni di "incidente" e "quasi incidente", e dall'art. 14, par. 7, per la figura del CSIRT coordinatore (art. 12, par. 1).
- **Decreto legislativo 4 settembre 2024, n. 138** (GU Serie generale n. 230 dell'1 ottobre 2024): designa il CSIRT Italia coordinatore ai fini dell'art. 12 NIS2 (art. 16, c. 1) e ne colloca il funzionamento presso l'ACN (art. 2, c. 1, lett. i).

Dettaglio completo, SHA256 e path locale dei file in `references/sources.yaml`. Trascrizioni verbatim in `references/fonti/`, estratti operativi in `references/estratti/`.

## Disclaimer

Strumento di supporto alla qualificazione e alla tracciatura di un adempimento normativo. Non sostituisce il giudizio del responsabile della conformita' del fabbricante ne' la consulenza legale. La decisione se un evento sia una vulnerabilita' attivamente sfruttata o un incidente grave, e la responsabilita' della notifica, restano interamente del fabbricante.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
