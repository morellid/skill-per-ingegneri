# Task: Inquadramento misura e schede DNSH applicabili

Identifica il perimetro DNSH dell'intervento PNRR/PNC: misura, fase, schede tecniche RGS applicabili, regime DNSH e checklist da attivare.

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

## Fonti da leggere

- `references/estratti/reg-ue-2020-852-art-17.md`
- `references/estratti/reg-ue-2021-241-art-5-18.md`
- `references/estratti/circolare-rgs-22-2024.md`
- `references/estratti/guida-operativa-dnsh-2024.md`

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

### Passo 2 - Classifica le attivita'

Scomponi l'intervento in componenti tecniche. Esempi:

- edificio: demolizioni, nuova costruzione, riqualificazione energetica, impianti, fotovoltaico, materiali, cantiere;
- strada/mobilita': pavimentazioni, illuminazione, veicoli, infrastrutture ricarica, opere idrauliche;
- ICT: acquisto hardware, data center/cloud/hosting, software, smaltimento RAEE;
- rifiuti/acque: impianti trattamento, reti, fanghi, emissioni, autorizzazioni.

Per ogni componente, individua la possibile scheda tecnica della Guida RGS. Se non sei certo, non assegnare in modo definitivo: usa `Da confermare sulla mappatura RGS/misura`.

### Passo 3 - Regime DNSH

Quando la Guida distingue regime 1 e regime 2:

- **Regime 1**: l'intervento deve contribuire sostanzialmente all'obiettivo ambientale pertinente e rispettare gli altri obiettivi DNSH.
- **Regime 2**: l'intervento deve rispettare il DNSH senza dimostrare contributo sostanziale.

Non inferire il regime solo dalla tipologia di opera: verificare la mappatura misura/scheda e le indicazioni dell'amministrazione titolare.

### Passo 4 - Output

Produrre:

```markdown
# Inquadramento DNSH PNRR

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
