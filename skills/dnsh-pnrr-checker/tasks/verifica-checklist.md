# Task: Verifica checklist DNSH ex ante / ex post

Verifica una checklist DNSH compilata o da compilare, distinguendo requisiti, evidenze, non applicabilita' motivate e integrazioni necessarie.

## Obiettivo

Restituire:

- esito di ogni requisito DNSH;
- motivazione sintetica e fonte;
- evidenza documentale richiesta;
- lacune da integrare prima di gara/SAL/collaudo/rendicontazione;
- rischi di non conformita' o risposte `NA` non motivate.

## Input richiesti

1. Scheda tecnica RGS applicata e regime.
2. Fase della checklist: ex ante o ex post.
3. Testo o tabella della checklist se gia' disponibile.
4. Elaborati a supporto: relazione tecnica, capitolato, CAM, computo, autorizzazioni, certificazioni, foto, verbali, dichiarazioni fornitori, prove/collaudi.
5. Eventuali prescrizioni del bando/decreto/atto d'obbligo.

Se il caso e' PNC, chiedi sempre l'atto della misura che richiama il DNSH o le checklist equivalenti. In assenza di tale fonte, la verifica puo' essere solo preliminare.

## Procedura

### Passo 1 - Normalizza gli esiti

Usa solo questi stati:

- `Conforme`: requisito coperto da evidenza coerente.
- `Non conforme`: requisito violato o evidenza contraria.
- `Non applicabile motivato`: il requisito non si applica e la motivazione e' esplicita.
- `Da integrare`: requisito potenzialmente applicabile ma evidenza assente/incompleta.
- `Da confermare su fonte di misura`: manca la fonte specifica PNRR/PNC o, nei casi PNC, non e' documentato il richiamo al DNSH.

### Passo 2 - Verifica qualita' delle risposte

Per ogni riga della checklist:

| Controllo | Criterio |
|---|---|
| Risposta `SI` | Deve avere evidenza documentale identificabile |
| Risposta `NO` | Deve generare non conformita' o azione correttiva |
| Risposta `NA` | Deve avere motivazione tecnica e perimetro escluso |
| Evidenza | Deve essere nominata, datata, riferita a elaborato o allegato |
| Fase | Deve essere coerente con ex ante/ex post |

### Passo 3 - Attenzione alle evidenze ricorrenti

Valuta se servono:

- prescrizioni DNSH nel capitolato e negli atti di gara;
- CAM pertinenti ai sensi del Codice dei contratti pubblici, quando richiamati dalla Guida;
- relazione DNSH o sezione DNSH nella relazione di sostenibilita'/PFTE;
- analisi rischio climatico e soluzioni di adattamento, se richieste;
- dichiarazioni fornitori, certificazioni prodotto, EPD, schede tecniche materiali;
- piano gestione rifiuti/cantiere, tracciabilita' conferimenti, formulari;
- autorizzazioni ambientali e pareri enti competenti;
- verbali DL/collaudo, foto, prove in sito, certificati di regolare esecuzione.

### Passo 4 - Output

```markdown
# Verifica checklist DNSH

**Scheda tecnica**: [...]
**Regime**: [...]
**Fase**: [ex ante | ex post]
**Intervento**: [...]

## 1. Esito riga per riga
| Requisito | Fonte | Risposta proposta/esistente | Evidenza | Esito | Azione richiesta |
|---|---|---|---|---|---|

## 2. Non conformita'
| ID | Gravita' | Descrizione | Azione correttiva | Responsabile |
|---|---|---|---|---|

## 3. Integrazioni documentali
- [...]

## 4. Risposte NA da motivare
- [...]

## 5. Esito complessivo
- [Checklist coerente | Checklist integrabile | Checklist non conforme | Verifica sospesa per dati insufficienti]

## 6. Avvertenza professionale
La verifica e' documentale e deve essere validata dal tecnico/RUP/soggetto attuatore prima di firma e caricamento su ReGiS.
```
