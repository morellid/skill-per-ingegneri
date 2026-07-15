# istruzioni-uso-macchine-reg-1230

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto marcatura CE macchine da completare)

Skill di **supporto documentale alla redazione e alla verifica di completezza
delle istruzioni per l'uso** (manuale di uso e manutenzione) di una **macchina** o
**prodotto correlato** ai sensi dell'**allegato III, punto 1.7.4** del **Reg. (UE)
2023/1230** (Regolamento Macchine).

**Non e' una skill di progettazione**: struttura e verifica il manuale; non esegue
la valutazione dei rischi, non seleziona norme armonizzate e non misura i valori.
E' **complementare** al fascicolo tecnico.

## Target

Fabbricanti, uffici tecnici, ingegneri meccanici/di prodotto.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `redigi-istruzioni` | Struttura le istruzioni per l'uso applicando i principi generali (1.7.4.1) e coprendo il contenuto minimo a-u (1.7.4.2), con lingua e formato |
| `verifica-completezza-istruzioni` | Verifica la completezza di un manuale esistente rispetto alle lettere a-u e alle prescrizioni trasversali (uso scorretto prevedibile, lingua, formato) |

Nucleo: **principi generali** di redazione (uso previsto e uso scorretto
ragionevolmente prevedibile), **contenuto minimo** a-u (incluse le informazioni
sull'**emissione di rumore aereo**), prescrizioni su **lingua** e **formato**
(digitale con copia cartacea gratuita su richiesta).

## Fonti consultate

- **Reg. (UE) 2023/1230** (Regolamento Macchine) - allegato III punto 1.7.4 e art.
  10 §7-8, testo su eur-lex (online-only)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- Non esegue la **valutazione dei rischi** ne' individua i **RES/norme armonizzate**
- Non **misura** rumore/massa ne' progetta le misure di protezione
- Non redige il **fascicolo tecnico** (allegato IV) ne' le **dichiarazioni UE**
  (allegato V): vedi `fascicolo-tecnico-macchine-reg-1230`

**La skill e' un supporto documentale: non sostituisce il fabbricante, il
progettista ne' la valutazione dei rischi.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
