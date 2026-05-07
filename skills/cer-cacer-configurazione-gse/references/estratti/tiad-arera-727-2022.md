# Estratto - Delibera ARERA 727/2022/R/eel - TIAD

> Fonte: id `delibera-arera-727-2022-tiad` in [`../sources.yaml`](../sources.yaml).
> URL: https://www.arera.it/atti-e-provvedimenti/dettaglio/it/22/727-22
> Consultazione: 2026-05-06.
> Licenza: pubblico dominio (atto di Autorita' indipendente).

Sintesi strutturata. Per il testo integrale e per gli aggiornamenti successivi (delibere di revisione TIAD) consultare la fonte.

## Cosa regola il TIAD

- Definisce le **configurazioni di autoconsumo diffuso** sotto il profilo della regolazione di rete (AID, GAC, CER) coerenti con il D.Lgs. 199/2021.
- Disciplina i **flussi fisici** misurati al POD (energia immessa e prelevata) per ogni membro CACER.
- Definisce il **calcolo dell'energia condivisa** che alimenta gli incentivi del DM 7/12/2023 e i corrispettivi di **restituzione** delle componenti tariffarie sull'energia condivisa.
- Stabilisce i **flussi informativi** tra distributore di rete, GSE e referente CACER.

## Concetti chiave usati dalla skill

### Energia condivisa oraria

La definizione operativa adottata e':

```
E_cond(h) = min( sum_i E_imm,i(h) ,  sum_j E_prel,j(h) )
```

dove:
- `E_imm,i(h)` e' l'energia immessa in rete dal generico impianto FER `i` afferente alla CACER nell'ora `h`;
- `E_prel,j(h)` e' l'energia prelevata dalla rete dal generico POD `j` afferente alla CACER nell'ora `h`.

L'energia condivisa annua e' la sommatoria oraria di `E_cond(h)` su 8.760 ore (8.784 negli anni bisestili).

### Tariffa di Restituzione (TR)

- Sull'energia condivisa il GSE riconosce al referente la **restituzione di alcune componenti tariffarie** (in particolare componenti di rete, perdite di rete) che, in via convenzionale, non sarebbero da pagare poiche' il flusso energia condivisa avviene su un perimetro limitato.
- Il valore della TR varia per **livello di tensione** (BT vs MT) ed e' aggiornato periodicamente da ARERA.
- La TR si somma alla TIP del DM 7/12/2023, ma copre logicamente i corrispettivi di rete, non l'incentivo.

### Flussi GSE / referente

- Il referente riceve TIP e TR dal GSE su base mensile/trimestrale.
- Il referente ridistribuisce ai membri secondo il **regolamento interno** o lo statuto.
- I membri continuano a pagare la propria bolletta al fornitore in modo invariato; il beneficio CACER e' un trasferimento "extra-bolletta" attraverso il referente.

## Implicazioni operative per la skill

- Quando l'utente chiede la **simulazione**, l'agent deve usare un'aggregazione oraria. Se non sono disponibili profili di consumo orari, l'agent **non assume un fattore di condivisione di default** (`eta_share`): il valore va dichiarato dall'utente o dal progettista con la propria fonte/motivazione, e la stima resta parametrica.
- L'agent non puo' restituire un calcolo "ufficiale": il calcolo finale e' del GSE su dati di misura validati.
- L'agent cita il TIAD per i flussi e per la TR, ma per la TIP rinvia al DM 7/12/2023 (e al DM 127/2025 per il regime PNRR vigente).
