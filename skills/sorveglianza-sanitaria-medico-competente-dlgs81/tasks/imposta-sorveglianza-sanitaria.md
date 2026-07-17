# Task: imposta-sorveglianza-sanitaria

Stabilisce **quando** la sorveglianza sanitaria e' dovuta e quali **visite mediche** si applicano,
ai sensi del **D.Lgs. 81/2008** (art. 41, cc. 1-4).

## Input richiesti

- **Rischi** cui sono esposti i lavoratori (dal **DVR**) e presenza di **rischi normati** che
  attivano la sorveglianza (es. rumore, vibrazioni, agenti chimici/cancerogeni/biologici,
  movimentazione manuale dei carichi, videoterminali, ecc.).
- Situazioni: **assunzione**, **cambio mansione**, **rientro dopo assenza > 60 giorni**, richiesta
  del lavoratore, attivita' ad **elevato rischio infortuni** (alcol/sostanze).

## Procedura

1. **Obbligatorieta'** (art. 41, c. 1): la sorveglianza e' dovuta nei **casi previsti dalla
   normativa** e in base alla **valutazione dei rischi**; oppure su **richiesta del lavoratore**
   (se correlata ai rischi). Se non ci sono rischi normati ne' altre condizioni, la sorveglianza
   puo' non essere obbligatoria.
2. **Individua le visite applicabili** (art. 41, c. 2): **preventiva/preassuntiva** (idoneita' alla
   mansione), **periodica** (di norma **annuale**, salvo diversa cadenza in base al rischio), **su
   richiesta**, **cambio mansione**, **cessazione**, **ripresa dopo > 60 gg**, **alcol/sostanze**
   per attivita' ad elevato rischio.
3. **Rispetta i divieti** (c. 3): niente accertamento di **gravidanza** ne' casi vietati; ricorda
   che le visite sono **a cura e spese del datore** (c. 4) e che il **protocollo sanitario** e' del
   **medico competente**.

## Output atteso

- Elenco delle visite dovute per la situazione data, con la **periodicita'** (di norma annuale o
  diversa motivata), il richiamo all'obbligatorieta' (rischi normati / DVR) e i divieti.

## Avvertenze

- La **definizione del protocollo sanitario** (esami, periodicita' puntuale) e' del **medico
  competente**: la skill inquadra il quadro, non lo sostituisce.
- L'attivazione dipende dai **rischi del DVR** (skill `dvr-generico`) e dalla normativa di settore.
