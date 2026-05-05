# POS Allegato XV Checker

> **Versione**: 0.1.0-alpha (in sviluppo)
> **Stato**: scaffold creato, contenuto normativo in preparazione

Skill di supporto alla compilazione assistita e alla verifica di un Piano Operativo di Sicurezza (POS) rispetto ai contenuti minimi dell'Allegato XV del D.Lgs. 9 aprile 2008 n. 81.

## Target

Ingegneri civili, coordinatori per la sicurezza in fase di esecuzione (CSE) e in fase di progettazione (CSP), datori di lavoro di imprese esecutrici, consulenti sicurezza.

## Cosa fa

Due flussi operativi:

1. **Compilazione assistita POS** - raccolta dati, struttura sezione per sezione, bozza con campi mancanti evidenziati.
2. **Verifica / precheck POS** - controlli su bozza o POS esistente.

Quattro sotto-verifiche distinte su un POS esistente o su una bozza:

1. **Completezza voci Allegato XV** - tutti i contenuti minimi obbligatori sono presenti?
2. **Coerenza rischi-misure** - le misure sono adeguate ai rischi identificati?
3. **Costi sicurezza** - computo dei costi non soggetti a ribasso corretto?
4. **Coordinamento e interferenze** - gestione interferenze e coordinamento con altre imprese documentata?

La skill puo' anche usare, se richiesto, l'impostazione dei **modelli semplificati** del Decreto Interministeriale 9 settembre 2014 come traccia di compilazione.

Per dettagli tecnici vedi [SKILL.md](SKILL.md).

## Installazione

Istruzioni da completare quando lo schema di distribuzione e' fissato (Claude Code + Agent SDK). Per ora: clonare il repo e caricare la skill manualmente.

## Fonti consultate

Vedi [references/sources.yaml](references/sources.yaml) per elenco completo con hash e date.

Fonti primarie:
- D.Lgs. 9 aprile 2008 n. 81 e s.m.i. - "Testo Unico Sicurezza sul Lavoro"
- D.Lgs. 81/2008 Allegato XV - "Contenuti minimi dei piani di sicurezza nei cantieri temporanei o mobili"
- Decreto Interministeriale 9 settembre 2014 - modelli semplificati per POS, PSC, FO e PSS

## Limiti noti

- **Alpha**: non ancora validata da dominio terzo
- **Non verifica congruita' con PSC** (serve skill separata)
- **Non sostituisce il sopralluogo** del CSE
- **Non produce un POS definitivo pronto al deposito**: solo bozza assistita + verifiche

Vedi [SKILL.md](SKILL.md) sezione "Limiti" per elenco completo.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).

## Disclaimer

Questa skill e' strumento di supporto. Non sostituisce il giudizio professionale del coordinatore o del datore di lavoro. Ogni output richiede revisione umana.
