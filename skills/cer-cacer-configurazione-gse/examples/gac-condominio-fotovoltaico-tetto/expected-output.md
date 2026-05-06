# Output atteso - GAC condominiale con FV in copertura

L'output deve **correggere la richiesta dell'utente** (che chiede una CER) verso la configurazione effettivamente coerente: **GAC** ai sensi dell'art. 32 D.Lgs. 199/2021, e segnalare il problema della grande impresa.

## 1. Pre-fattibilita' (task `valuta-perimetro-configurazione`)

```markdown
# Scheda di pre-fattibilita' CACER

## 1. Soggetti coinvolti
- 24 persone fisiche
- 2 attivita' commerciali, di cui:
  - 1 PMI (bar a gestione familiare)
  - 1 GRANDE IMPRESA (filiale di catena nazionale, > 250 dipendenti)
- Grandi imprese: SI -> incompatibili con la qualita' di socio CER (art. 31 c. 2 D.Lgs. 199/2021).
- Referente ipotizzato: amministratore di condominio (DA CONFERMARE con delega in assemblea).

## 2. Posizione e perimetro
- POD prelievo: 26 POD, tutti nello stesso edificio condominiale, BT.
- POD immissione: 1 POD su copertura del medesimo edificio.
- Cabina primaria: rispettata per definizione (stesso edificio).
- Stesso edificio/condominio: SI.

## 3. Impianti FER
- Tecnologia: FV in copertura
- Potenza: 80 kW (fascia < 200 kW, soglia 1 MW rispettata)
- Stato: in progetto

## 4. Configurazione consigliata
- Configurazione: **GAC** (art. 32 D.Lgs. 199/2021), motivazione:
  - tutti i soggetti sono nello **stesso edificio condominiale**;
  - non e' necessario costituire un soggetto giuridico autonomo (la CER richiederebbe l'esclusione della grande impresa, riducendo la base partecipanti);
  - il GAC si struttura come accordo privato / regolamento condominiale, con l'amministratore come referente.
- Configurazioni alternative compatibili:
  - **CER**: tecnicamente possibile escludendo la grande impresa, ma piu' onerosa in termini di governance e atto pubblico; perde 1 dei 2 POD commerciali e quindi parte dei consumi.

## 5. Verifiche obbligatorie residue
- [ ] Esclusione formale della grande impresa dalla qualita' di "socio CER" se si vuole comunque una CER (in alternativa GAC senza vincolo di esclusione, ma il negozio rimane un partecipante GAC ammesso).
- [ ] Delibera assembleare condominiale che:
  - approva l'impianto e l'investimento;
  - approva il regolamento di partecipazione GAC;
  - nomina il referente con poteri verso il GSE.
- [ ] Verifica titolo abilitativo per FV 80 kW in copertura (Modello Unico se applicabile, Comunicazione altrimenti).
- [ ] Verifica ripartizione benefici tra unita' immobiliari (criterio millesimale o per consumo).
- [ ] Niente contributo PNRR: Comune > 5.000 ab.

## 6. Avvertenza finale
La presente scheda e' un supporto preliminare. La qualifica formale del servizio
CACER e' rilasciata dal GSE secondo le Regole Operative vigenti. La forma
giuridica non e' richiesta per il GAC, ma serve la delibera assembleare e il
regolamento. La grande impresa NON puo' essere socia di una CER ma puo'
partecipare al GAC come autoconsumatore.
```

## 2. Statuto / Regolamento

L'output del task `redigi-statuto-cer` deve **chiarire all'utente** che, nella configurazione GAC, **non serve uno statuto in senso proprio**, bensi' un **regolamento di partecipazione** (o accordo privato) approvato in assemblea condominiale, contenente:

- elenco partecipanti (POD);
- ruolo dell'amministratore come referente;
- mandato del referente verso il GSE;
- criteri di ripartizione dei benefici (es. millesimale, per consumo, mix);
- modalita' di adesione di nuovi inquilini e di recesso;
- gestione dell'impianto e manutenzione.

Se l'utente insiste sulla CER, l'output deve segnalare:

- la grande impresa va **esclusa come socia**;
- la CER va costituita come ente autonomo presso notaio;
- la rigidita' aggiuntiva e' giustificata solo se ci sono finalita' di comunita' che il GAC non copre.

## 3. Simulazione

```markdown
# Simulazione semplificata CACER

## 1. Ipotesi di calcolo
- FV in copertura, 80 kW
- Producibilita': 1.250 kWh/kWp/anno (Pianura Padana)
- Livello di tensione: BT
- Profilo utenze: prevalentemente residenziale + 2 attivita' commerciali
- Fattore di condivisione `eta_share`: 0.40 (mix residenziale + commerciale diurno, no accumulo)
- Comune > 5.000 ab. -> NO contributo PNRR
- Valori TIP/TR: parametrici, DA VERIFICARE su pubblicazione GSE/ARERA vigente

## 2. Bilancio energetico annuo
| Voce | kWh/anno |
|---|---|
| Energia immessa CACER | 80 * 1.250 = 100.000 |
| Energia prelevata CACER | 95.000 |
| Energia condivisa stimata | 0.40 * min(100.000; 95.000) = 38.000 |

## 3. Flussi economici (stima parametrica)
| Voce | EUR/anno | Note |
|---|---|---|
| TIP | 38.000 * (T_fissa(< 200 kW) + correttivo zonale) - DA QUANTIFICARE | durata 20 anni |
| TR | 38.000 * tr_unitaria(BT) - DA QUANTIFICARE | |
| Contributo PNRR | NON ACCESSIBILE (Comune > 5.000 ab.) | - |

## 4. Avvertenze
- Stima parametrica, calcolo ufficiale GSE.
- TIP e TR vanno aggiornate alla data di qualifica.
- Valutare se il negozio (grande impresa) sia ammesso come autoconsumatore GAC: nel GAC i partecipanti sono autoconsumatori, e la condizione "non grande impresa" propria della CER non si applica con la stessa severita' al GAC; verificare per scrupolo le Regole Operative GSE vigenti.

## 5. Disclaimer
Documento di supporto, non costituisce promessa di flussi economici futuri.
```

## 4. Checklist GSE

- Configurazione GAC: regolamento di partecipazione approvato in assemblea condominiale, mandato dell'amministratore, elenco POD, dati impianto FV 80 kW (titolo abilitativo da Modello Unico se applicabile), schema unifilare, codice CENSIMP, dichiarazione non doppio incentivo.
- Niente sezione PNRR.
- Avvertenza esplicita che la sezione "CER" della checklist NON si applica al GAC.

## Conclusione

L'errore tipico che la skill deve **correggere** in questo esempio e':

1. l'utente vuole una CER ma la configurazione naturale e' GAC (stesso edificio);
2. la presenza di una grande impresa rende la CER piu' complicata (esclusione obbligatoria), ma e' compatibile con il GAC.
