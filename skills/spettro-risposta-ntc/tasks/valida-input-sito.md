# Task: validazione input sito per calcolo spettro NTC

## Obiettivo

Verificare la coerenza degli input prima di eseguire il calcolo dello spettro. Intercetta errori comuni:
- Categorie di sottosuolo S1/S2 (analisi specifiche dovute, par. 3.2.2)
- Vita nominale incoerente con la classe d'uso dichiarata
- Probabilita' di superamento o tempi di ritorno fuori range del reticolo
- Parametri ag/F0/Tc* inseriti in unita' errate (es. ag in m/s^2 invece che g)
- Numero di valori dei parametri di pericolosita' non pari a 9

## Quando usare questo task

- "Verifico se i miei input sono ok prima di calcolare lo spettro"
- "Sono coerenti VN e classe d'uso per una scuola?"
- "Il mio sito e' nel reticolo INGV?"

## Input richiesti

Stessi del task `calcola-spettro.md`, in versione preliminare.

## Procedura

1. **Categoria di sottosuolo**:
   - Se l'utente dichiara A/B/C/D/E -> ok, prosegui.
   - Se l'utente dichiara S1 o S2 -> blocca: NTC par. 3.2.2 prescrive analisi specifiche di risposta sismica locale. Il modulo Python solleva `ValueError` esplicito.
   - Se l'utente dichiara un altro valore -> blocca: chiedi chiarimento.

2. **Coerenza VN / classe d'uso**:
   - VN >= 100 e classe d'uso IV: ok per opere strategiche (ospedali, caserme, ecc.)
   - VN = 50 e classe d'uso II: caso ordinario residenziale
   - VN = 50 con classe d'uso IV oppure VN = 100 con classe d'uso I -> warning: chiedi conferma esplicita all'utente
   - VN < 35: warning, V_R sara' clampata a 35 anni (par. 2.4.3 NTC)
   - Se la destinazione d'uso menzionata e' sensibile (scuola, ospedale, edificio strategico) e la classe d'uso e' I o II -> chiedi conferma

3. **Tempi di ritorno**:
   - Calcola V_R = V_N * C_U (clamp a 35 anni)
   - Calcola TR per ciascuno stato limite (P_VR da Tab. 3.2.I)
   - Verifica che ciascun TR sia in [30, 2475] anni: se fuori, segnala errore con la sua causa probabile (es. SLO con VR molto piccolo -> TR < 30; SLC con VR molto grande -> TR > 2475)

4. **Parametri di pericolosita'**:
   - Numero di valori per ag, F0, Tc*: deve essere 9 ciascuno
   - Range di sanita':
     - ag in [0.001, 1.0] (in g): se ag > 1.0 g sospetto unita' errate; se ag < 0.001 g sospetto sito non sismico (verifica)
     - F0 in [2.0, 3.5]: range tipico italiano
     - Tc* in [0.10, 0.60] s: range tipico italiano
   - Monotonia: ag, F0, Tc* sono in genere non decrescenti con TR (non e' garantito da legge: se osservi inversioni segnala come warning)

5. **Categoria topografica e altezza relativa**:
   - T1: ok per qualsiasi caso
   - T2/T3/T4: chiedi se l'edificio e' in **sommita'** del rilievo (ST applicato in pieno) o se e' a quota intermedia (interpolazione lineare di ST tra base 1.0 e sommita', NTC par. 3.2.3.2.1, formula 3.2.5)
   - **Limite della skill**: la versione corrente applica ST in sommita'. Per quote intermedie il professionista deve correggere il risultato manualmente con NTC eq. 3.2.5

## Output atteso

Report strutturato:

```
=== Validazione input sito ===

[OK]  Categoria di sottosuolo: C
[OK]  Categoria topografica: T1
[OK]  V_N = 50 anni, classe d'uso II -> V_R = 50 anni (par. 2.4.3 NTC)
[OK]  TR di calcolo: SLO=30, SLD=50, SLV=475, SLC=975 anni - tutti in [30, 2475]
[OK]  Parametri di pericolosita': 9 valori per ag/F0/Tc*
[OK]  ag in [0.030, 0.420] g - range plausibile
[OK]  F0 in [2.50, 2.76] - range plausibile
[OK]  Tc* in [0.20, 0.36] s - range plausibile

VALIDAZIONE SUPERATA -> procedi con tasks/calcola-spettro.md
```

oppure, se ci sono problemi:

```
=== Validazione input sito ===

[BLOCCANTE]  Categoria di sottosuolo S2: NTC par. 3.2.2 prescrive analisi
             specifiche di risposta sismica locale. Calcolo non eseguibile
             con questa skill.
[WARN]       VN=50 classe d'uso IV -> V_R=100 anni: confermare che la
             vita nominale dichiarata sia coerente con un'opera "strategica"
             di classe IV (ospedale, scuola, edificio di protezione civile).

VALIDAZIONE NON SUPERATA -> rivedere input prima di procedere
```

## Limiti

- Il task non valida coordinate lat/lon contro il reticolo INGV (la skill non incorpora il reticolo).
- Il task non sostituisce la relazione geologica/geotecnica per la determinazione di Vs,30 e della categoria di sottosuolo.
