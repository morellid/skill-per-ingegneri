# DM 58/2017 Allegato A punto 2.2 - Indice di Sicurezza per la Vita IS-V

> Fonte: DM 58/2017 Allegato A (testo aggiornato dal DM 65/2017, DM 24/2020, DM 329/2020).
> Consultata su: https://www.mit.gov.it/normativa/decreto-ministeriale-numero-58-del-28022017
> Data accesso: 2026-05-07
> Licenza: dominio pubblico (atto normativo italiano)

## Definizione

L'**Indice di Sicurezza Strutturale per la Vita (IS-V)** e' definito dal rapporto tra:
- l'**Accelerazione di Picco al Suolo di Capacita'** PGA_C(SLV) che determina il raggiungimento dello Stato Limite di salvaguardia della Vita per l'edificio
- l'**Accelerazione di Picco al Suolo di Domanda** PGA_D(SLV) che le NTC 2018 prescrivono al sito per il medesimo Stato Limite

## Formula

```
IS-V = PGA_C(SLV) / PGA_D(SLV)
```

espresso come frazione adimensionale; per la Tab. classi IS-V (Allegato A punto 2.3) moltiplicare per 100 per ottenere la percentuale.

## Significato fisico

- **IS-V > 100%**: l'edificio sopporta accelerazioni superiori a quelle di domanda al sito - sicurezza > requisito normativo (classe A+).
- **IS-V = 100%**: l'edificio sopporta esattamente le accelerazioni di domanda - sicurezza piena ma "al limite" (classe A).
- **IS-V < 100%**: l'edificio NON sopporta le accelerazioni di domanda al SLV - margine di sicurezza ridotto rispetto al requisito normativo per nuove costruzioni; per edifici esistenti puo' essere accettabile in funzione della classe d'uso, della destinazione e della vita residua.

## Note operative

- L'IS-V usa la PGA al sito al periodo zero. Non confondere con l'ordinata di spettro Se(T=0): per la componente orizzontale Se(T=0) = a_g x S x F_0 x eta x (T_B/T_B) / F_0 = a_g x S (al periodo nullo, F_0 e eta vanno via). Quindi PGA_D = a_g x S, dove S = S_S x S_T (Tab. 3.2.IV e 3.2.V NTC 2018).
- Per edifici **esistenti** l'IS-V e' sempre minore o uguale a quello richiesto per nuove costruzioni (per definizione dell'analisi di vulnerabilita'). Edifici fuori zona sismica con domanda molto bassa possono comunque avere IS-V > 100% senza interventi.
- L'IS-V e' un parametro **separato** dal PAM: due edifici con stesso IS-V possono avere PAM molto diversi, perche' il PAM dipende anche dal comportamento agli SL meno severi (SLO, SLD).

## Riferimenti puntuali

- DM 58/2017 Allegato A punto 2.2 (testo coordinato DM 329/2020): definizione e formula IS-V
- DM 58/2017 Allegato A punto 2.3: tabella classi IS-V (vedi `dm-58-2017-allegato-a-tabelle-classi.md`)
- NTC 2018 par. 3.2 + Allegato A: calcolo PGA_D al sito (vedi anche skill `spettro-risposta-ntc` nel repo)
- NTC 2018 cap. 8: calcolo PGA_C dell'edificio (analisi di vulnerabilita')
