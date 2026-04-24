# Note di dominio - caso `costi-analitico-corretto`

## Cosa stiamo testando

Che la skill riconosca come **conforme** un computo analitico dei costi sicurezza ben strutturato, con tabelle per categoria, prezziario citato, e conformita' art. 97 co. 3-bis.

## Scelte progettuali del caso

- **POS di impresa affidataria**: include il dettaglio dei costi e la ripartizione verso esecutori. Non tutti i POS contengono questa struttura - quelli delle esecutrici subappaltatrici spesso rinviano al PSC e alla quota loro assegnata.
- **Prezziario regionale Toscana**: riferimento autoritativo realistico per un cantiere in Toscana. La skill dovrebbe riconoscere il riferimento a un prezziario regionale come segnale positivo.
- **7 categorie coperte**: test che la skill sappia matching tutte le lettere a)-g) del 4.1.1.
- **Percentuale 7,83%**: deliberatamente alta (range tipico edilizia civile 2-6%). Motivata dalla presenza di sfasamenti espliciti. La skill dovrebbe segnalare "alto ma giustificabile" invece di "eccessivo".
- **Sfasamento esplicito**: voce f) con quantificazione di 5 giorni x EUR 1.800. Molti POS sottostimano o omettono questa voce.
- **Art. 97 co. 3-bis**: trasferimento senza ribasso agli esecutori esplicitato. Test critico per POS affidataria.
- **Interpello 25/2014**: manutenzione annuale estintori quantificata - conforme all'interpello (che stabilisce che la manutenzione degli apprestamenti rientra nei costi sicurezza).

## Output atteso

`CONFORME CON NOTE` con 2 note di priorita' media/bassa:
- Nota su possibile inclusione formazione generale nella voce e) (carico impresa, non sicurezza)
- Nota su verifica del cronoprogramma per sfasamento

## Cose che la skill DOVREBBE fare

- Riconoscere tabelle analitiche come segnale positivo (non solo testo libero).
- Accettare la citazione del prezziario come conformita' metodologica.
- Calcolare la percentuale e contestualizzarla rispetto al range tipico.
- Riconoscere la conformita' all'art. 97 co. 3-bis quando esplicitata.
- Segnalare ambiguita' sulla formazione (dove generale vs specifica puo' sovrapporsi).

## Cose che la skill NON dovrebbe fare

- **Falso positivo** per percentuale "alta": 7,83% e' fuori range modale ma giustificato.
- **Falso positivo** per voce g) "gestione area deposito comune" apparentemente generica: e' una voce legittima per "misure di coordinamento uso comune" del 4.1.1 lett. g).
- **Pretendere di verificare** i prezzi unitari contro prezziario esterno (non disponibile).

## Complicazioni da gestire

- **Formazione specifica vs generale**: zona grigia. L'art. 37 D.Lgs. 81 prevede formazione generale obbligatoria come carico impresa. La formazione specifica (nuovi rischi, procedure particolari del cantiere) puo' essere costo sicurezza. La skill deve segnalare la zona grigia, non dirimerla.
- **Ponteggio nolo = posa + smontaggio inclusi?**: per prassi, il nolo di ponteggio (mq/mese) include posa/smontaggio/manutenzione nel prezzo unitario. Conforme al 4.1.3.

## Cosa imparare

- Un POS ben fatto sui costi ha: tabelle analitiche, prezziario citato, percentuale calcolata, 7 categorie coperte, trasferimento esplicito agli esecutori.
- La skill aggiunge valore soprattutto nel segnalare la sottile differenza tra "formazione obbligatoria" (non sicurezza) e "formazione specifica" (sicurezza).
- La conformita' al 4.1.3 (analitica, prezziario, utilizzo) e' verificabile dalla struttura del testo.

## Fonte della struttura

Fittizio. Struttura ispirata a POS affidataria di media-alta qualita' per edilizia commerciale in Toscana. Prezzi unitari plausibili ma non validati contro prezziario reale.
