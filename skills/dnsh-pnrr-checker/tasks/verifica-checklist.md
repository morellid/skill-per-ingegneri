# Task: Verifica checklist DNSH ex ante / ex post

Verifica una checklist DNSH compilata o da compilare, distinguendo requisiti, evidenze, non applicabilita' motivate e integrazioni necessarie.

## Obiettivo

Restituire:

- esito di ogni punto di controllo nel formato ufficiale della Guida RGS;
- motivazione sintetica e fonte normativa per ogni voce;
- evidenza documentale richiesta o gia' disponibile;
- lacune da integrare prima di gara/SAL/collaudo/rendicontazione;
- rischi di non conformita' (in particolare: NO ex post implica non conformita' al DNSH).

## Formato ufficiale della checklist (Guida RGS 2024, p. 20-21)

Le check list della Guida usano **tre risposte possibili**: SI / NO / Non applicabile, piu' un campo "commento" obbligatorio per motivare NA e NO. Non usare stati diversi nel check ufficiale; gli stati operativi sottostanti (es. "Da integrare") possono comparire solo nel commento o nell'analisi aggiuntiva.

| Risposta | Checklist ex ante | Checklist ex post |
|---|---|---|
| **SI** | Il vincolo e' stato preso in considerazione in fase progettuale; indicare l'evidenza, incluse certificazioni equivalenti; CAM inseriti in gara = adempimento DNSH (raccomandato) | Il requisito e' soddisfatto; OK anche con misure di mitigazione adottate o certificazioni equivalenti |
| **NON APPLICABILE** | Il progetto non ha attivita' che giustificano la verifica di quel vincolo; le ragioni devono essere esplicitate nel campo "commento" | Specificare le motivazioni nel campo "commento" |
| **NO** | Il vincolo e' applicabile ma non ancora tenuto in conto; nel commento indicare come e' possibile sanarlo e le tempistiche | **ATTENZIONE**: NO ex post nei casi in cui il vincolo non e' stato rispettato e non e' sanabile implica **non conformita' al DNSH del progetto** (Guida p. 21) |

Le check list compilate devono essere **sottoscritte e datate** dal soggetto attuatore o dall'Amministrazione titolare.

## Input richiesti

1. Scheda tecnica RGS applicata e regime (1 o 2).
2. Fase della checklist: ex ante o ex post.
3. Testo o tabella della checklist se gia' disponibile.
4. Elaborati a supporto: relazione tecnica, capitolato, CAM, computo, autorizzazioni, certificazioni, foto, verbali, dichiarazioni fornitori, prove/collaudi.
5. Fase attuativa ReGiS di riferimento (selezione progetti, affidamento, rendicontazione intermedia, rendicontazione finale/saldo).
6. Eventuali prescrizioni del bando/decreto/atto d'obbligo o Operational Arrangements.

Se il caso e' PNC, chiedi sempre l'atto della misura che richiama il DNSH o le checklist equivalenti. In assenza di tale fonte, la verifica puo' essere solo preliminare.

## Procedura

### Passo 1 - Verifica qualita' delle risposte

Per ogni punto di controllo della checklist:

| Controllo | Criterio (Guida RGS 2024, pp. 20-21) |
|---|---|
| Risposta `SI` | Deve avere evidenza documentale identificabile; eventuali certificazioni equivalenti da indicare puntualmente |
| Risposta `NON APPLICABILE` | Deve avere motivazione tecnica nel campo "commento"; il perimetro escluso deve essere esplicitato |
| Risposta `NO` ex ante | Deve indicare nel commento come sanare la lacuna e le tempistiche |
| Risposta `NO` ex post | Configura non conformita' al DNSH del progetto; segnalare con massima evidenza |
| Evidenza | Deve essere identificabile (elaborato, certificato, verbale, dichiarazione, formulario) |
| Fase | Deve essere coerente con ex ante/ex post e con l'avanzamento della misura |

### Passo 2 - Attenzione alle evidenze ricorrenti

Valuta se servono:

- prescrizioni DNSH nel capitolato e negli atti di gara (art. 57 D.lgs. 36/2023 per CAM);
- CAM pertinenti richiamati dalla Guida RGS 2024 Appendice 2 (soprattutto Regime 2; valutare caso per caso per Regime 1);
- relazione DNSH o sezione DNSH nella relazione di sostenibilita'/PFTE;
- analisi rischio climatico: metodologia semplificata (Appendice 1 Guida) per interventi < 10 MLN euro; Orientamenti tecnici 2021/C 373/01 per interventi > 10 MLN euro;
- dichiarazioni fornitori, certificazioni prodotto, EPD, schede tecniche materiali;
- piano gestione rifiuti/cantiere, tracciabilita' conferimenti, formulari;
- autorizzazioni ambientali (VIA/VAS/AIA/AUA) e pareri enti competenti;
- verbali DL/collaudo, foto, prove in sito, certificati di regolare esecuzione.

### Passo 3 - Output

```markdown
# Verifica checklist DNSH

**Scheda tecnica**: [...]
**Regime**: [1 | 2]
**Fase checklist**: [ex ante | ex post]
**Fase attuativa ReGiS**: [selezione progetti | affidamento | rendicontazione intermedia | rendicontazione finale]
**Intervento**: [...]

## 1. Punti di controllo
| # | Requisito | Risposta (SI/NO/NA) | Commento/evidenza | Criticita' |
|---|---|---|---|---|

## 2. Non conformita' (NO ex ante da sanare)
| # | Vincolo | Come sanare | Tempistica | Responsabile |
|---|---|---|---|---|

## 3. Non conformita' gravi (NO ex post)
| # | Vincolo | Conseguenza DNSH | Note |
|---|---|---|---|

## 4. Risposte NA senza motivazione
- [...]

## 5. Integrazioni documentali consigliate
- [...]

## 6. Esito complessivo
- [Checklist conforme | Checklist con lacune sanabili (NO ex ante) | Checklist non conforme (NO ex post) | Verifica sospesa per dati insufficienti]

## 7. Avvertenza
La checklist e' indicativa (Guida RGS 2024, p. 20). L'Amministrazione titolare puo' specializzarla.
La checklist compilata deve essere sottoscritte e datata prima del caricamento su ReGiS.
La validazione resta in capo al tecnico/RUP/soggetto attuatore.
```
