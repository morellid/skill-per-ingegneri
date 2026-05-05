# AGENTS.md - piano-lavoro-amianto

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Questa skill copre il **piano di lavoro per demolizione o rimozione di amianto** previsto dall'**art. 256 del D.Lgs. 81/2008**, con integrazione delle misure tecniche del **DM 6 settembre 1994**. Il target sono ingegneri, RSPP, coordinatori sicurezza, consulenti HSE e imprese specializzate che devono fare precheck, redigere o verificare il piano prima della trasmissione all'organo di vigilanza.

## Fonti autoritative

Tutte catalogate in `references/sources.yaml` con URL, data di accesso e hash:

- **D.Lgs. 31 dicembre 2025 n. 213 - GU n. 6 del 09/01/2026** - hash `79e6b58...`
- **DM 6 settembre 1994 - allegato tecnico** - hash `3955c8b...`

Estratti pertinenti gia' preparati in `references/estratti/`:
- `dlgs-213-2025-amianto-art-250-251-256-258-259.md` - sintesi operativa degli articoli amianto del D.Lgs. 81/2008 nel testo vigente dal 24/01/2026
- `dm-6-9-1994-amianto.md` - criteri tecnici su bonifica, scelta dell'intervento, DPI, decontaminazione e raccolta dati

## Articoli e punti chiave

Quando produci output, cita SEMPRE il riferimento specifico:

- **Art. 250 D.Lgs. 81/2008**: contenuto minimo della notifica all'organo di vigilanza; dal 24/01/2026 la notifica e' "prima dell'inizio dei lavori"
- **Art. 251 D.Lgs. 81/2008**: esposizione al piu' basso valore tecnicamente possibile, DPI vie respiratorie, decontaminazione, ambienti chiusi
- **Art. 256 commi 2-6 D.Lgs. 81/2008**: piano di lavoro, contenuti minimi, preavviso di 30 giorni, urgenza, sostituzione della notifica art. 250
- **Art. 258 D.Lgs. 81/2008**: formazione periodica, contenuti della formazione e formazione aggiuntiva per demolizione/rimozione
- **Art. 259 D.Lgs. 81/2008**: sorveglianza sanitaria preposta e periodica
- **DM 6 settembre 1994 - Allegato**: criteri per valutazione preliminare, bonifica, decontaminazione e organizzazione operativa
- **DM 6 settembre 1994 - Allegato 4**: criteri per scelta dei DPI delle vie respiratorie

## Convenzioni specifiche

### Cosa NON fare
- Non dire che la sola notifica art. 250 basta quando il caso ricade in **demolizione o rimozione**: in quel caso il riferimento corretto e' l'**art. 256**.
- Non inventare quantita', stato del materiale, procedure di confinamento, layout di decontaminazione o allegati non forniti dall'utente.
- Non trasformare il piano in una certificazione di conformita' o in un'autorizzazione implicita dell'ASL/ATS/SPSAL.
- Non assumere automaticamente dettagli su Albo gestori, trasporto o laboratorio di monitoraggio se la fonte non e' stata fornita.

### Cosa fare
- Distinguere sempre tra **materiale compatto/friabile**, **ambiente aperto/chiuso** e **intervento di sola gestione/manutenzione** versus **rimozione/demolizione**.
- Se il perimetro non e' chiaro, usare stati come `Da confermare` o `Preliminare`, non conclusioni nette.
- Per ogni carenza del piano, indicare gravita' (`Critica`, `Alta`, `Media`) e riferimento preciso.
- Ricordare che il testo degli articoli amianto e' qui trattato nel **testo vigente dal 24 gennaio 2026**.

## Validatori

- Validatore di dominio da individuare per Livello 2.

## Stato attuale

- Versione: vedi `CHANGELOG.md`
- Validazione: Livello 1
- Task files: `valuta-obbligo-e-precheck.md`, `redigi-piano-lavoro.md`, `verifica-piano-lavoro.md`
- Esempi: 2 casi iniziali (1 strutturato + 1 problematico)
