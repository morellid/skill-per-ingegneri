# Task: Piano evidenze e report DNSH

Prepara un piano documentale DNSH e una bozza di report/relazione, collegando requisiti, elaborati, capitolato, SAL, collaudo e rendicontazione.

## Obiettivo

Produrre:

- matrice requisiti-evidenze;
- piano di acquisizione documenti per fase;
- clausole operative da recepire in progetto/capitolato;
- bozza di relazione DNSH o report di verifica;
- elenco criticita' e controlli non automatizzabili.

## Input richiesti

1. Esito dell'inquadramento schede DNSH.
2. Checklist ex ante/ex post applicabili.
3. Elaborati disponibili e mancanti.
4. Fase procedurale e scadenza.
5. Ruoli: RUP, progettista, DL, impresa, fornitori, collaudatore, consulente ambientale.

## Procedura

### Passo 1 - Matrice evidenze

Per ogni scheda/requisito crea:

| Requisito DNSH | Fase | Evidenza minima | Documento/elaborato | Responsabile | Stato |
|---|---|---|---|---|---|

Stati ammessi: `Disponibile`, `Da produrre`, `Da aggiornare`, `Non applicabile motivato`, `Da verificare`.

### Passo 2 - Piano per fase

Separare sempre:

- **Progettazione / ex ante**: relazioni, scelte progettuali, CAM, prescrizioni, autorizzazioni, analisi rischio climatico.
- **Affidamento**: clausole DNSH nel capitolato, requisiti forniture, obblighi impresa, subappaltatori, documenti da consegnare.
- **Esecuzione / SAL**: verbali, formulari, foto, certificati materiali, controlli DL.
- **Collaudo / ex post**: prove, dichiarazioni finali, certificati, report as-built, checklist finale.
- **Rendicontazione ReGiS**: file definitivi, nominazione coerente, tracciabilita' CUP/CIG/SAL.

### Passo 3 - Bozza di report

Il report deve essere asciutto e verificabile. Non dichiarare conformita' finale se mancano evidenze.

Formato:

```markdown
# Report DNSH - [intervento]

## 1. Premessa e fonti
[Misura, fonti UE/RGS, fonte specifica di misura]

## 2. Descrizione intervento
[Oggetto, localizzazione, fase, importo, CUP]

## 3. Mappatura schede DNSH
[Tabella schede/regime/checklist]

## 4. Verifica requisiti
[Matrice requisiti-evidenze]

## 5. Prescrizioni da recepire
- [Progetto]
- [Capitolato/gara]
- [Esecuzione]
- [Collaudo/rendicontazione]

## 6. Criticita' e integrazioni
- [...]

## 7. Esito
- [Conforme con evidenze complete | Conforme con integrazioni puntuali | Non conforme | Verifica sospesa]

## 8. Avvertenza
Documento di supporto: la validazione finale resta in capo a tecnico competente, RUP e soggetto attuatore.
```

### Passo 4 - Controlli finali

Prima di consegnare:

- verifica che ogni requisito abbia almeno una evidenza o una motivazione `NA`;
- segnala documenti mancanti con responsabile e scadenza;
- distingui prescrizioni progettuali da prove ex post;
- rinvia esplicitamente al template ReGiS vigente.
