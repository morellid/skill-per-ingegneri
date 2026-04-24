# Task: Verifica costi sicurezza non soggetti a ribasso

Verifica il computo dei costi per la sicurezza indicati o richiamati nel POS (tipicamente integrato al PSC), controllando completezza delle categorie previste dall'Allegato XV punto 4.1.1, conformita' metodologica al punto 4.1.3, e coerenza con la natura/entita' dell'opera.

## Obiettivo

Produrre un report strutturato che indichi:
- Presenza/assenza delle 7 categorie di costi previste dal punto 4.1.1
- Conformita' metodologica (computo analitico, non "a corpo" indistinto)
- Congruita' qualitativa con la tipologia di cantiere
- Eventuali discrepanze tra costi PSC, costi POS, e costi non soggetti a ribasso

Nota importante: il POS **non e' il documento dove si STIMANO i costi della sicurezza** - quello e' il PSC. Il POS conferma, richiama o integra. La verifica del POS sui costi e' quindi una verifica incrociata di:
- Il POS ha recepito correttamente i costi del PSC?
- Il POS descrive gli apprestamenti coerenti con i costi stimati?
- L'impresa affidataria ha verificato la congruenza (art. 97 co. 3 lett. b)?

## Input richiesti

- Sezione del POS relativa ai costi della sicurezza o al recepimento dei costi PSC
- Idealmente: estratto del PSC con la stima dei costi della sicurezza
- Importo complessivo lavori
- Tipologia cantiere (edilizia civile, OOPP, ristrutturazione, demolizione, impianti)
- Se si verifica una variante: valore della variante

## Fonti normative

Leggere prima:
- `references/estratti/allegato-xv-testo.md` punto 4 (stima dei costi della sicurezza) - tutte le sotto-sezioni 4.1.1 - 4.1.6
- `references/estratti/dlgs-81-art-96-97.md` art. 97 co. 3 lett. b) (congruenza POS/PSC) e 3-bis (subappalto e oneri sicurezza senza ribasso)

## Procedura

### Passo 1 - Identificazione della sezione costi

Nel POS, cercare:
- Sezione esplicita "costi sicurezza" o "oneri sicurezza"
- Rinvio al PSC con recepimento/accettazione
- Tabella di sintesi con importo complessivo "non soggetto a ribasso"

Se la sezione costi nel POS e' assente:
- Accettabile se e' tipologia "POS di impresa esecutrice a valle di un PSC" e il POS dichiara espressamente accettazione del PSC. I costi sono nel PSC, non nel POS.
- Non accettabile se il POS dovrebbe sostituirsi al PSC (cantieri senza CSC) o se e' un PSS integrato con POS.

### Passo 2 - Verifica delle 7 categorie 4.1.1

Per ogni categoria dell'Allegato XV punto 4.1.1 lettere a)-g), verificare presenza nei costi:

| Cat | Descrizione (Allegato XV 4.1.1) | Voci tipiche da cercare |
|-----|----------------------------------|-------------------------|
| a | Apprestamenti previsti nel PSC | Ponteggi, trabattelli, parapetti, andatoie, armature scavi, recinzioni, servizi igienici cantiere, spogliatoi, infermeria, camera medicazione |
| b | Misure/DPI per lavorazioni interferenti | DPI specifici per interferenze (non DPI ordinari, che sono costi generali impresa), barriere, teli, soluzioni anti-interferenza |
| c | Impianti terra/scariche atm./antincendio/evacuazione fumi | Impianto messa a terra, SPD/scaricatori, estintori, idranti, aspiratori fumi |
| d | Mezzi e servizi di protezione collettiva | Segnaletica sicurezza, avvisatori acustici, illuminazione emergenza, mezzi estinguenti (oltre minimo), servizi emergenza |
| e | Procedure contenute nel PSC per motivi di sicurezza | Ore di formazione specifica; ore di briefing; procedure speciali che richiedono tempo quantificato |
| f | Interventi per sfasamento spaziale/temporale interferenze | Ore aggiuntive per sfasare lavorazioni; tempo di fermo concordato per interferenze; squadre di coordinamento |
| g | Misure di coordinamento per uso comune | Riunioni di coordinamento (ore); gestione area comune (stoccaggio, mensa); coordinatore operativo |

### Passo 3 - Verifica metodologica (punto 4.1.3)

Il punto 4.1.3 prescrive che la stima sia:
1. **Congrua**: adeguata all'entita' e tipologia del cantiere
2. **Analitica per voci singole**: non "a corpo indistinto"
3. **Riferita a elenchi prezzi standard o specializzati** (prezziari regionali, DEI, specifici), O **listini ufficiali vigenti nell'area**, O **elenco prezzi committente**
4. **Basata su analisi costi da indagini di mercato** solo se non e' applicabile un elenco prezzi
5. **Costo di utilizzo specifico del cantiere**, che comprende quando applicabile: posa in opera, smontaggio, manutenzione, ammortamento

Flag se il computo:
- Dichiara "costi sicurezza a corpo: EUR X" senza dettaglio analitico -> **NON CONFORME al 4.1.3**
- Non cita la fonte dei prezzi usati -> segnalare come carenza metodologica
- Usa solo "costi per DPI" senza distinguere DPI ordinari (carico impresa) da DPI sicurezza specifici (non soggetti a ribasso)

### Passo 4 - Verifica percentuale su importo lavori

Calcolare: `% costi sicurezza = costi sicurezza / importo lavori`.

Valori di riferimento **qualitativi** (non vincolanti, per orientamento):

| Tipologia cantiere | Range tipico % | Note |
|--------------------|----------------|------|
| Ristrutturazione leggera, manutenzione | 1-3% | Entita' contenuta |
| Edilizia civile nuova, bassa complessita' | 2-4% | Range modale |
| Edilizia civile complessa (altezza, interferenze) | 3-6% | Apprestamenti importanti |
| Opere pubbliche, infrastrutture | 3-8% | Variabilita' alta |
| Demolizione con interferenze abitate | 4-10% | Costi protezione terze parti |
| Opere speciali (monumentali, sotterranee) | 5-15%+ | Molto variabile |

**Attenzione**: questi sono riferimenti qualitativi. Un valore fuori range non e' di per se' errore, ma segnale per verifica approfondita. Valori troppo bassi (<1%) spesso indicano sottostima; valori molto alti vanno giustificati.

### Passo 5 - Verifica art. 97 co. 3 lett. b) - congruenza

L'impresa affidataria (datore di lavoro) ha l'obbligo di **verificare la congruenza dei POS delle imprese esecutrici rispetto al proprio**. Inoltre art. 97 co. 3-bis: "In relazione ai lavori affidati in subappalto, ove gli apprestamenti, gli impianti e le altre attivita' di cui al punto 4 dell'allegato XV siano effettuati dalle imprese esecutrici, l'impresa affidataria corrisponde ad esse senza alcun ribasso i relativi oneri della sicurezza."

Verifiche:
- Il POS cita il riconoscimento della quota oneri sicurezza (se sub-appaltatore)?
- Il POS dell'affidataria conferma trasferimento senza ribasso agli esecutori?
- Coerenza tra quota sicurezza del subappalto e costi corrispondenti nel PSC?

### Passo 6 - Output

```markdown
# Verifica costi sicurezza

**Data verifica**: [data]
**POS analizzato**: [id]
**Contesto cantiere**: [tipologia, importo lavori]

## Sintesi

- Importo lavori: EUR X
- Costi sicurezza dichiarati: EUR Y (Z% sull'importo lavori)
- Categorie Allegato XV 4.1.1 coperte: N/7
- Metodologia: [CONFORME 4.1.3 | PARZIALMENTE CONFORME | NON CONFORME]
- Range percentuale: [INTERNO AI VALORI TIPICI | FUORI RANGE - VERIFICARE]

**Esito complessivo**: [CONFORME | CONFORME CON NOTE | INADEGUATO | NON VERIFICABILE]

## Verifica per categoria

| Categoria 4.1.1 | Voci trovate nel POS/PSC | Importo | Stato |
|----------------|---------------------------|---------|-------|
| a) Apprestamenti | Ponteggio, recinzione, ... | EUR X | OK |
| b) DPI lavorazioni interferenti | ... | ... | ... |
| c) Impianti terra/antincendio/fumi | ... | ... | ... |
| d) Protezione collettiva | ... | ... | ... |
| e) Procedure sicurezza | ... | ... | ... |
| f) Sfasamento interferenze | ... | ... | ... |
| g) Coordinamento uso comune | ... | ... | ... |

## Verifica metodologica (punto 4.1.3)

- Computo analitico per voci singole: [SI | NO | PARZIALE]
- Riferimento a prezziario/elenco prezzi: [SI, indicato X | NO | NON SPECIFICATO]
- Dettaglio costo utilizzo (posa + smontaggio + manutenzione): [SI | NO | PARZIALE]
- Note metodologiche: ...

## Problemi rilevati

| # | Categoria | Problema | Riferimento | Priorita' |
|---|-----------|----------|-------------|-----------|
| 1 | a | Apprestamenti dichiarati "a corpo EUR X" senza dettaglio | All. XV 4.1.3 | Alta |
| ... |

## Raccomandazioni

- Richiedere dettaglio analitico per [categoria]
- Verificare congruenza con PSC per [voce]
- ...

## Congruenza con art. 97 (solo se applicabile)

- L'impresa affidataria ha verificato la congruenza del POS con il proprio? [SI/NO/NON DOCUMENTATO]
- Il POS cita il trasferimento senza ribasso degli oneri alle imprese esecutrici? [SI/NO/NON APPLICABILE]

## Limiti di questa verifica

- Verifica su documento. Congruita' effettiva dei costi al cantiere specifico richiede valutazione CSE.
- Se non disponibile il PSC, la verifica del POS e' parziale (il POS puo' solo confermare/accettare quello che e' nel PSC).
- La skill non dispone di prezziari regionali aggiornati. Non puo' verificare puntualmente i prezzi unitari, solo la metodologia del computo.
- Interpelli rilevanti (es. INTERPELLO N. 25/2014 sui costi di manutenzione apprestamenti, N. 13/2016 su piattaforma elevabile mobile come costo sicurezza) possono influenzare casi specifici.

## Rinvio al professionista firmatario

**La verifica dei costi della sicurezza nella sua dimensione contrattuale ed economica spetta al committente (tramite CSP e, se nominato, al RUP) e al CSE. Il datore di lavoro dell'impresa affidataria e' responsabile della verifica di congruenza dei POS delle imprese esecutrici (art. 97 co. 3 lett. b).**
```

## Casi limite

### POS di impresa esecutrice senza sezione costi
Accettabile se il PSC contiene la stima ufficiale e il POS dichiara accettazione. Nel report indicare: "Verifica costi rinvenuti nel PSC, il POS conferma accettazione ex art. 100 D.Lgs. 81 - OK come struttura". Richiedere il PSC per verifica completa.

### PSS integrato con POS (cantiere senza PSC)
Il PSS deve integrare gli elementi del POS (art. 3.2.2 Allegato XV). Il PSS **non include** la stima dei costi ex punto 3.1.1, ma per cantieri in ambito pubblico l'amministrazione deve comunque stimare i costi (punto 4.1.2). Verificare la posizione specifica del committente.

### Costi dichiarati come "inclusi nel prezzo complessivo"
Non conforme. L'Allegato XV 4.1.4 richiede che i costi sicurezza siano **identificati nell'importo totale** ed **individuino la parte da non assoggettare a ribasso**. Formule di inclusione generica violano questa prescrizione.

### Percentuale molto bassa o molto alta
Non e' automaticamente errore:
- Bassa: possibile in cantieri di manutenzione leggera con apprestamenti minimi
- Alta: possibile in cantieri con forti interferenze, demolizione amianto, opere speciali

Indicarla come "da verificare per congruita' con la natura specifica del cantiere", non come violazione.

### Mere forniture (art. 96 co. 1-bis)
Le mere forniture di materiali/attrezzature sono escluse dall'obbligo POS. Se il cantiere e' solo fornitura, non ha senso valutare costi sicurezza del POS (non dovrebbe esistere). Le spese si regolano sotto art. 26 DUVRI.

## Limiti di questo task

- Non dispone di prezziari per verifica puntuale prezzi unitari.
- Non verifica se il quanto dichiarato (es. mq di ponteggio) e' coerente col cantiere reale.
- Non e' verifica della congruita' contrattuale ma metodologica.
- Non sostituisce la verifica del RUP/CSE.

## Esempi

Vedi `examples/`:
- `costi-analitico-corretto/` - computo con dettaglio analitico, 7 categorie, prezziario citato
- `costi-boilerplate-non-conforme/` - costi dichiarati "a corpo" senza dettaglio
