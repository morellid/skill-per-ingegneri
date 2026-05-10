# Task: Inquadramento misura e schede DNSH applicabili

Identifica il perimetro DNSH dell'intervento PNRR o, nei soli casi documentati, PNC: misura, fase, schede tecniche RGS applicabili, regime DNSH e checklist da attivare.

## Obiettivo

Restituire all'utente:

- inquadramento della misura e dell'intervento;
- schede tecniche DNSH probabilmente applicabili;
- regime 1 / regime 2 quando la Guida lo prevede;
- checklist ex ante/ex post da compilare;
- fonti da acquisire prima di concludere la verifica;
- punti da confermare sul bando/decreto/atto d'obbligo della specifica misura.

## Input richiesti

Chiedere se non forniti:

1. Missione, componente, investimento/sub-investimento, linea di finanziamento.
2. CUP, soggetto attuatore, amministrazione titolare, fonte PNRR/PNC.
3. Oggetto: lavori, servizi, forniture, ICT, impianti, edifici, strade, mobilita', rifiuti, acque, energia.
4. Localizzazione, vincoli ambientali/paesaggistici, presenza aree Natura 2000 o rischio climatico noto.
5. Fase: programmazione, PFTE, progetto esecutivo, gara, esecuzione, SAL, collaudo, rendicontazione.
6. Documenti disponibili: bando/decreto, relazione tecnica, computo, capitolato, CAM, autorizzazioni, checklist gia' compilate.

Se l'utente fornisce solo dati parziali, procedi con una mappatura preliminare e marca gli esiti come `Da confermare`.
Se il caso e' PNC e manca l'atto della misura che richiama il DNSH, non produrre una mappatura definitiva.

## Fonti da leggere

- `references/estratti/reg-ue-2020-852-art-17.md`
- `references/estratti/reg-ue-2021-241-art-5-18.md`
- `references/estratti/circolare-rgs-22-2024.md`
- `references/estratti/guida-operativa-dnsh-2024.md`
- `references/estratti/dl-77-2021-art-14-pnc.md`
- `references/estratti/ministero-salute-principio-dnsh-pnc.md`

## Procedura

### Passo 1 - Inquadra la misura

Riassumi i dati disponibili:

| Campo | Valore | Fonte/nota |
|---|---|---|
| Missione / componente / investimento | [...] | [...] |
| CUP / soggetto attuatore | [...] | [...] |
| Oggetto intervento | [...] | [...] |
| Fase | [...] | [...] |
| Fonte specifica di misura disponibile | si'/no | [...] |

Se la fonte specifica di misura manca, dichiara: "La mappatura e' preliminare: la scheda DNSH definitiva deve essere verificata sul bando/decreto/atto d'obbligo e sui template ReGiS vigenti".
Se il caso e' PNC e manca un atto che richiami il DNSH, dichiara anche: "Per il PNC la skill non puo' assumere automaticamente l'applicabilita' della Guida RGS 2024: serve una fonte misura-specifica".

### Passo 2 - Classifica le attivita'

Scomponi l'intervento in componenti tecniche. Esempi:

- edificio: demolizioni, nuova costruzione, riqualificazione energetica, impianti, fotovoltaico, materiali, cantiere;
- strada/mobilita': pavimentazioni, illuminazione, veicoli, infrastrutture ricarica, opere idrauliche;
- ICT: acquisto hardware, data center/cloud/hosting, software, smaltimento RAEE;
- rifiuti/acque: impianti trattamento, reti, fanghi, emissioni, autorizzazioni.

Per ogni componente, individua la possibile scheda tecnica della Guida RGS. Se non sei certo, non assegnare in modo definitivo: usa `Da confermare sulla mappatura RGS/misura`.
Per i casi PNC, assegna schede RGS solo se l'atto della misura le richiama espressamente o se il collegamento e' motivato e documentabile.

### Passo 3 - Regime DNSH

La Guida RGS 2024 distingue due regimi (p. 12-13):

- **Regime 1**: la misura deve contribuire sostanzialmente a uno degli obiettivi climatici o ambientali e rispettare il DNSH per tutti gli altri. Si applica quando:
  - il campo di intervento ha tagging climatico 100% (contributo sostanziale alla mitigazione), oppure
  - il campo di intervento ha tagging ambientale 100% (contributo sostanziale a un altro obiettivo), oppure
  - la scheda di autovalutazione PNRR o la Decisione di esecuzione del Consiglio lo indica esplicitamente.
- **Regime 2**: la misura deve solo garantire di non arrecare danno significativo a nessuno dei sei obiettivi ambientali, senza contributo sostanziale.

Il Regime applicabile emerge dalla **mappatura ufficiale** della Guida RGS, che va consultata e riportata. L'associazione mappatura-scheda ha carattere indicativo: le Amministrazioni titolari possono adattarla alle specificita' concrete degli interventi (Guida p. 17). Non inferire il regime autonomamente: verificare la mappatura misura/scheda e le indicazioni dell'Amministrazione titolare.

Per PNC, se il regime non emerge dall'atto della misura o da un allegato ufficiale, segnalare come `Da confermare su fonte di misura`.

### Passo 4 - Output

Produrre:

```markdown
# Inquadramento DNSH

## 1. Dati intervento
[tabella]

## 2. Componenti tecniche
| Componente | Descrizione | Scheda DNSH candidata | Regime | Note |
|---|---|---|---|---|

## 3. Checklist da attivare
| Scheda | Ex ante | Ex post | Fase corrente | Responsabile |
|---|---|---|---|---|

## 4. Fonti mancanti
- [...]

## 5. Esito preliminare
- [Mappatura completa | Mappatura parziale | Dati insufficienti]

## 6. Avvertenza
La mappatura deve essere confermata su bando/decreto/atto d'obbligo, Guida RGS vigente e template ReGiS della misura.
```
