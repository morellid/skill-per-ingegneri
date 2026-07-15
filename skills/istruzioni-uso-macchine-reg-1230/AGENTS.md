# AGENTS.md - istruzioni-uso-macchine-reg-1230

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **redazione** e alla **verifica di completezza** delle
**istruzioni per l'uso** (manuale di uso e manutenzione) di una **macchina** o
**prodotto correlato** ai sensi dell'**allegato III, punto 1.7.4** del **Reg. (UE)
2023/1230**. Target: fabbricanti, uffici tecnici, ingegneri meccanici/di prodotto.

**E' una skill documentale**: non esegue la valutazione dei rischi, non individua i
RES/norme armonizzate, non misura i valori. E' **complementare** alla skill
`fascicolo-tecnico-macchine-reg-1230` (fascicolo tecnico, allegato IV).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **reg-ue-2023-1230-istruzioni**: Reg. (UE) 2023/1230, allegato III punto 1.7.4 +
  art. 10 §7-8. Fonte eur-lex trattata come **online-only** (`binary_path: null`,
  `sha256: null`): eur-lex non e' riproducibile con hash stabile e blocca gli IP
  datacenter di GitHub Actions (stesso approccio della skill ai-act-compliance).
  Il punto 1.7.4 (1.7.4.1 principi generali, 1.7.4.2 contenuto a-u) e' trascritto
  verbatim in `references/fonti/reg-ue-2023-1230-istruzioni.md`.

Estratto operativo: `references/estratti/istruzioni-uso-checklist.md`.

## Punti chiave (verificati sul testo)

- **1.7.4.1**: le istruzioni coprono l'**uso previsto** e l'**uso scorretto
  ragionevolmente prevedibile** (a); per **operatori non professionali**, redazione
  adeguata al loro livello (b).
- **1.7.4.2**: contenuto minimo "se del caso" nelle lettere **a-u**; la lett. **u**
  riguarda l'**emissione di rumore aereo** con soglie L_pA 70 dB(A), L_pC 63 Pa
  (130 dB), L_WA se L_pA > 80 dB(A).
- **Lingua/formato (art. 10 §7)**: lingua comprensibile per gli utilizzatori;
  **deroga** per la manutenzione destinata a personale specializzato del
  fabbricante (una sola lingua UE); formato digitale ammesso con **copia cartacea
  gratuita su richiesta** al momento dell'acquisto.

## Convenzioni specifiche

### Cosa NON fare
- Non eseguire la **valutazione dei rischi** ne' individuare i **RES/norme
  armonizzate** (a pagamento).
- Non **misurare** rumore/massa ne' progettare le misure di protezione.
- Non redigere il **fascicolo tecnico** (allegato IV) ne' le **dichiarazioni UE**
  (allegato V): rinviare a `fascicolo-tecnico-macchine-reg-1230`.

### Cosa fare
- Applicare i principi generali (1.7.4.1) e coprire le lettere a-u (1.7.4.2).
- Applicare le regole di lingua/formato (art. 10 §7) e la deroga manutenzione.
- Chiudere con il rinvio al fabbricante / valutazione dei rischi.

## Aggiornamento della fonte

eur-lex online-only: a ogni aggiornamento rileggere il punto 1.7.4 dell'allegato
III e l'art. 10 del Reg. (UE) 2023/1230 (ed eventuali atti delegati/di esecuzione).

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con esperto marcatura CE macchine).

## Stato attuale

- Versione: 0.1.0-alpha (closes #56)
- Task files: 2 (`redigi-istruzioni.md`, `verifica-completezza-istruzioni.md`)
- Esempi: 2 (operatori non professionali; lingua manutenzione/formato)
