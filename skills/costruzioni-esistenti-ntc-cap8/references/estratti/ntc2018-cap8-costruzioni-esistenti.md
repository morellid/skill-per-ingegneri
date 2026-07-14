# Estratto operativo - NTC 2018 cap. 8 + Circolare C8 (costruzioni esistenti)

Estratto curato per la consultazione. Ogni voce e' parafrasi/citazione delle
trascrizioni verificate in `references/fonti/ntc2018-dm-17-01-2018.md` (NTC
cap. 8) e `references/fonti/circ-7-2019-mit.md` (Circolare C8). Le soglie e i
valori riportati qui sono citabili a un paragrafo preciso del PDF letto.

## 1. Le tre categorie di intervento (NTC par. 8.4)

| Categoria | Definizione (NTC 8.4) | Valutazione della sicurezza | Collaudo statico |
|---|---|---|---|
| **Riparazione o intervento locale** | Interessa singoli elementi; non riduce le condizioni di sicurezza preesistenti e non cambia significativamente il comportamento globale | Solo locale/parti interessate (NTC 8.4.1); no valutazione globale, ma se rafforzamento locale -> valutare l'incremento del livello di sicurezza locale (C8.4.1) | No |
| **Miglioramento** | Aumenta la sicurezza preesistente senza necessariamente raggiungere i livelli del par. 8.4.3 | Obbligatoria, estesa all'intera struttura (NTC 8.4.2) | Si' |
| **Adeguamento** | Aumenta la sicurezza conseguendo i livelli fissati al par. 8.4.3 | Obbligatoria, riferita all'intera costruzione post-intervento (NTC 8.4.3) | Si' |

Nota (NTC 8.4): solo miglioramento e adeguamento sono sottoposti a collaudo
statico. Per beni culturali in zona a rischio sismico (art. 29 c. 4 D.Lgs.
42/2004) e' sempre possibile limitarsi al miglioramento.

## 2. Quando l'ADEGUAMENTO e' obbligatorio (NTC par. 8.4.3) e soglia di zeta_E

L'adeguamento e' obbligatorio quando si intenda:

| Caso | Descrizione (NTC 8.4.3) | Soglia zeta_E |
|---|---|---|
| **a)** | Sopraelevare la costruzione | **zeta_E >= 1,0** |
| **b)** | Ampliare con opere strutturalmente connesse tali da alterarne significativamente la risposta | **zeta_E >= 1,0** |
| **c)** | Variazioni di destinazione d'uso con incremento dei carichi globali verticali in fondazione **> 10%** (comb. caratteristica eq. 2.5.2, soli carichi gravitazionali) | **zeta_E >= 0,80** |
| **d)** | Insieme sistematico di opere che porti a un sistema strutturale diverso dal precedente; per edifici, nuovi elementi verticali portanti su cui grava >= 50% dei carichi gravitazionali per piano | **zeta_E >= 1,0** |
| **e)** | Modifiche di classe d'uso che conducano a classe III uso scolastico o classe IV | **zeta_E >= 0,80** |

- Nei casi a), b), d) -> **zeta_E >= 1,0**; nei casi c), e) -> **zeta_E >= 0,80**
  (NTC 8.4.3).
- La Circolare C8.4.3 assimila al caso c) (soglia 0,8) anche l'adeguamento
  sismico deciso dal proprietario a seguito di inadeguatezza riscontrata con la
  valutazione ex par. 8.3, purche' NON ricadente nei casi a), b) o d).
- Resta sempre l'obbligo di verifica locale delle singole parti (anche in c/e).
- Cordoli sommitali / variazioni di copertura senza incremento di superficie
  abitabile: non sono "ampliamento" ex a); non obbligano l'adeguamento salvo
  ricorra una delle condizioni b), c), d), e) (NTC 8.4.3 + C8.4.3).

## 3. Soglie di zeta_E per il MIGLIORAMENTO (NTC par. 8.4.2 + C8.4.2)

Per la combinazione sismica zeta_E puo' essere < 1, ma:

| Classe d'uso | Vincolo su zeta_E dopo il miglioramento |
|---|---|
| Classe III ad uso scolastico e classe IV | **zeta_E >= 0,6** |
| Restanti classe III e classe II | **zeta_E incrementato di >= 0,1** rispetto allo stato di fatto |
| (verifica del solo sistema di isolamento) | **zeta_E >= 1,0** |

## 4. zeta_E e zeta_V,i (NTC par. 8.3 + C8.3)

- **zeta_E** = azione sismica massima sopportabile / azione sismica massima di
  progetto per una nuova costruzione sul medesimo suolo e con le stesse
  caratteristiche. Parametro di confronto: salvo casi particolari,
  l'accelerazione al suolo **ag*S** (C8.3).
- **zeta_V,i** = massimo sovraccarico verticale variabile sopportabile dalla
  parte i-esima / sovraccarico di progetto per una nuova costruzione (NTC 8.3).

## 5. Livelli di conoscenza e fattori di confidenza (NTC 8.5.4 + Circ. C8.5.4)

I tre livelli (informazione crescente) e i relativi FC (valori dalla
Circolare C8.5.4; **non** presenti nel testo NTC):

| Livello | Requisiti minimi (C8.5.4) | **FC** |
|---|---|---|
| **LC1** | Analisi storico-critica, rilievo geometrico completo, indagini **limitate** sui dettagli, prove **limitate** sui materiali | **1,35** |
| **LC2** | Come LC1 ma indagini **estese** sui dettagli e prove **estese** sui materiali | **1,20** |
| **LC3** | Analisi storico-critica, rilievo completo e accurato, indagini **esaustive**, prove **esaustive** (o documenti progettuali originali verificati) | **1,00** |

Aspetti che definiscono il LC (NTC 8.5.4): geometria, dettagli costruttivi,
proprieta' dei materiali, connessioni tra elementi e modalita' di collasso.

**Uso dell'FC (NTC 8.7.2, Circ. C8.5.4.2):**
- c.a./acciaio: le resistenze medie dei materiali si **dividono per l'FC** della
  Tabella C8.5.IV (e per i coefficienti parziali nel caso di meccanismi fragili;
  solo per l'FC nel caso di meccanismi duttili - NTC 8.7.2).
- muratura (C8.5.4.1): la conoscenza si gradua scegliendo i valori di tabella
  (minimi per LC1, medi per LC2, aggiornati con prove per LC3), oltre al quadro
  generale dell'FC del par. C8.5.4.
- Per i materiali **nuovi o aggiunti** si usano le proprieta' di calcolo come
  per le nuove costruzioni (NTC 8.7.2).
- FC = 1 (LC3) si applica solo ai parametri per cui sono state fatte le prove
  esaustive; per gli altri l'FC resta coerente con le prove eseguite (C8.5.4).

## 6. Quando e' obbligatoria la VALUTAZIONE DELLA SICUREZZA (NTC par. 8.3)

Deve effettuarsi al ricorrere anche di **una sola** delle situazioni:
- riduzione evidente di capacita' resistente/deformativa (degrado, deformazioni,
  danneggiamenti da azioni ambientali/eccezionali/uso anomalo);
- provati gravi errori di progetto o costruzione;
- cambio di destinazione d'uso con variazione significativa dei carichi variabili
  e/o passaggio a classe d'uso superiore;
- interventi non dichiaratamente strutturali che riducano capacita'/rigidezza di
  elementi strutturali in modo consistente;
- ogni qualvolta si eseguano gli interventi strutturali di cui al par. 8.4;
- opere in assenza/difformita' dal titolo abilitativo o dalle norme tecniche
  vigenti al momento della costruzione.

Esclusione (C8.3): la sola revisione della normativa o della zonazione delle
azioni ambientali NON obbliga la valutazione.

**Verifica del sistema di fondazione** (NTC 8.3): obbligatoria solo se sussistono
condizioni di instabilita' globale oppure: dissesti importanti da cedimenti
(anche pregressi); possibili ribaltamento/scorrimento per morfologia,
modifiche del profilo del terreno o sisma di progetto; possibile liquefazione.
Altrimenti il tecnico deve esplicitare nella relazione l'assenza di tali
condizioni (C8.3).

## 7. Stati limite di riferimento (NTC par. 8.3)

- Valutazione e progetto possono riferirsi ai **soli SLU**, salvo classe d'uso IV
  (anche SLE del par. 7.3.6, con livelli prestazionali eventualmente ridotti).
- Per la combinazione sismica gli SLU possono riferirsi a SLV o, in alternativa,
  SLC (par. 7.3.6).

## 8. Elaborati minimi del progetto di miglioramento/adeguamento (NTC 8.7.5)

a) analisi/verifica della struttura prima dell'intervento (carenze + livello di
azione sismica per cui si raggiunge lo SLU, e SLE se richiesto); b) scelta
motivata del tipo di intervento; c) scelta motivata di tecniche/materiali;
d) dimensionamento preliminare dei rinforzi e degli elementi aggiuntivi;
e) analisi della struttura post-intervento; f) verifica della struttura
post-intervento (livello di azione sismica per cui si raggiunge lo SLU).

## Fuori ambito di questa skill (rinvio al progettista)

- Il **calcolo** di zeta_E, delle capacita' degli elementi, delle analisi
  (lineari/non lineari, statiche/dinamiche): la skill NON esegue verifiche
  strutturali (par. 8.7.1-8.7.4 e cap. 7).
- La scelta e il dimensionamento delle tecniche di intervento.
- I valori di tabella dei parametri meccanici (Tabelle C8.5.I/II/III) e le
  correlazioni: non sono trascritti integralmente (fuori dallo scopo Q&A).
- Ogni contenuto e' di supporto alla consultazione: la valutazione della
  sicurezza e la relazione ex par. 8.3 sono responsabilita' del progettista.
