---
name: istruzioni-uso-macchine-reg-1230
description: "Supporto documentale alla redazione e alla verifica di completezza delle istruzioni per l'uso (manuale di uso e manutenzione) di una macchina o di un prodotto correlato ai sensi dell'allegato III, punto 1.7.4, del Regolamento (UE) 2023/1230 (Regolamento Macchine). Aiuta ad applicare i principi generali di redazione (copertura dell'uso previsto e dell'uso scorretto ragionevolmente prevedibile; operatori non professionali) e a coprire il contenuto minimo obbligatorio (lettere a-u: identificazione del fabbricante, designazione, accesso alla dichiarazione UE, descrizione e uso previsto, avvertenze sugli usi non ammessi, montaggio/installazione, riduzione di rumore e vibrazioni, messa in servizio e formazione, rischi residui, DPI, stabilita', trasporto/movimentazione/stoccaggio con la massa, protocollo in caso di infortunio/avaria e sblocco, regolazione e manutenzione in sicurezza, pezzi di ricambio, informazioni sull'emissione di rumore aereo), oltre alle prescrizioni su lingua e formato digitale/cartaceo. Use when a manufacturer or machinery engineer must draft or check the instructions/manual of a machine or related product under the new EU Machinery Regulation 2023/1230; it is a documentary aid, complementary to the technical file, and does not perform the risk assessment, does not select harmonised standards and does not measure noise or other values."
license: MIT
area: impianti-macchine-prodotti
title: "Istruzioni per l'uso delle macchine (Reg. UE 2023/1230, All. III 1.7.4)"
summary: "Redazione e verifica di completezza delle istruzioni per l'uso (manuale) di macchina o prodotto correlato ex allegato III punto 1.7.4 Reg. (UE) 2023/1230: principi generali (uso previsto e uso scorretto prevedibile) e contenuto minimo a-u, lingua e formato."
normative_refs:
  - "Reg. (UE) 2023/1230 (Regolamento Macchine) - allegato III punto 1.7.4 e art. 10 §7-8"
version: 0.1.0-alpha
status: alpha
tags:
  - reg-ue-2023-1230
  - macchine
  - istruzioni-per-uso
  - manuale-uso-manutenzione
  - marcatura-ce
---

# Istruzioni per l'uso delle macchine (Reg. UE 2023/1230, All. III 1.7.4)

## Quando usare questa skill

Usala quando devi **redigere** o **verificare la completezza** delle **istruzioni
per l'uso** (manuale di uso e manutenzione) di una **macchina** o di un **prodotto
correlato**, ai sensi dell'**allegato III, punto 1.7.4** del **Reg. (UE) 2023/1230**
(Regolamento Macchine, che sostituisce la dir. 2006/42/CE dal 14/1/2027):

- applicare i **principi generali** di redazione (coprire l'**uso previsto** e
  l'**uso scorretto ragionevolmente prevedibile**; operatori non professionali)
  (1.7.4.1);
- coprire il **contenuto minimo obbligatorio** (elenco **a-u**), comprese le
  informazioni sull'**emissione di rumore aereo** (u.i-iii) (1.7.4.2);
- rispettare le prescrizioni su **lingua** e **formato** (digitale con copia
  cartacea gratuita su richiesta) (art. 10 §7-8).

**Non e' una skill di progettazione**: non esegue la valutazione dei rischi, non
individua i RES applicabili ne' le norme armonizzate, non misura il rumore o altri
valori. E' **complementare** al fascicolo tecnico (skill
`fascicolo-tecnico-macchine-reg-1230`).

## Cosa NON fa (limiti)

- Non esegue la **valutazione dei rischi** ne' individua i **rischi residui** (dati
  del progetto): li **riporta** nelle istruzioni.
- Non seleziona le **norme armonizzate** (UNI/CEN, a pagamento) ne' individua i RES
  applicabili (allegato III nel suo complesso).
- Non **misura** i valori (rumore aereo, massa) ne' progetta le misure di
  protezione/DPI.
- Non redige il **fascicolo tecnico** (allegato IV) ne' le **dichiarazioni UE**
  (allegato V): vedi `fascicolo-tecnico-macchine-reg-1230`.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`redigi-istruzioni`](tasks/redigi-istruzioni.md) | Struttura le istruzioni per l'uso applicando i principi generali (1.7.4.1) e coprendo il contenuto minimo a-u (1.7.4.2), con le prescrizioni su lingua e formato |
| [`verifica-completezza-istruzioni`](tasks/verifica-completezza-istruzioni.md) | Verifica la completezza di un manuale esistente rispetto alle lettere a-u e alle prescrizioni trasversali (lingua, formato, uso scorretto prevedibile) |

## Riferimenti normativi

- **Reg. (UE) 2023/1230** (Regolamento Macchine) - **allegato III, punto 1.7.4**
  (Istruzioni per l'uso: 1.7.4.1 principi generali, 1.7.4.2 contenuto a-u) e
  **art. 10 §7-8** (fornitura, lingua, formato digitale/cartaceo, accesso alla
  dichiarazione UE).

Dettaglio in `references/sources.yaml`,
`references/fonti/reg-ue-2023-1230-istruzioni.md`,
`references/estratti/istruzioni-uso-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: i contenuti sostanziali (rischi residui, misure
di protezione, valori di rumore, misure di manutenzione sicura) derivano dalla
valutazione dei rischi e dalla progettazione, che restano in capo al **fabbricante**
e al progettista. La marcatura CE, la firma della dichiarazione UE e la
responsabilita' per la conformita' del prodotto sono del fabbricante. La skill
**non sostituisce** il fabbricante, il progettista ne' la valutazione dei rischi.
