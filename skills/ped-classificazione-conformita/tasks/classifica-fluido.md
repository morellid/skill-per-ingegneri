# Task: classifica il fluido (gruppo 1 vs gruppo 2)

## Obiettivo

Determinare se il fluido contenuto nell'attrezzatura a pressione appartiene al **gruppo 1** o al **gruppo 2** ai sensi dell'art. 9 c. 1 del D.Lgs 26/2016. Il gruppo del fluido e' uno dei tre assi della classificazione (PS, V/DN, gruppo) che determinano la categoria nelle tabelle 1-9 dell'Allegato II.

## Input richiesti

Chiedi all'utente:

- Identificazione chimica del fluido (nome IUPAC o commerciale) o miscela.
- Stato fisico alle condizioni operative: gas / vapore (incluso vapore d'acqua) o liquido.
- Temperatura massima ammissibile **TS** (gradi C).
- Per i fluidi liquidi: **punto di infiammabilita'** (flash point) noto dalla scheda di sicurezza.
- Classificazione di pericolo del fluido secondo il **Regolamento CE 1272/2008 (CLP)**, presa dalla scheda di sicurezza (es. Flam. Liq. 2, Acute Tox. 3 oral, ecc.).
- In caso di miscela, classificazione armonizzata della miscela CLP.

Se l'utente non dispone delle classi CLP, fermati e chiedi: senza scheda di sicurezza non si puo' assegnare il gruppo.

## Fonti

- `references/estratti/dlgs-26-2016-classificazione-moduli.md` sezione 2 (gruppi di fluidi).
- `references/fonti/dlgs-26-2016.md` art. 9 c. 1 lett. a) (elenco 17 classi) e lett. b) (gruppo 2 come residuo).

## Procedura

1. **Test "TS > punto di infiammabilita'"** (solo fluidi liquidi): se la temperatura massima ammissibile TS supera il punto di infiammabilita' del fluido, il fluido ricade in **gruppo 1** indipendentemente dalla sua classificazione CLP (art. 9 c. 1 lett. a, incipit). Per i fluidi gas/vapore questo test non si applica.
2. **Test classi CLP**: verifica se il fluido o la miscela rientra in una delle seguenti 17 classi di pericolo CLP (riferimento testuale dell'art. 9 c. 1 lett. a). Se si', e' **gruppo 1**:
   1. esplosivi instabili, o esplosivi delle divisioni 1.1, 1.2, 1.3, 1.4 e 1.5;
   2. gas infiammabili, categorie 1 e 2;
   3. gas comburenti, categoria 1;
   4. liquidi infiammabili, categoria 1 e 2;
   5. liquidi infiammabili della categoria 3, **solo se TS > punto di infiammabilita'**;
   6. solidi infiammabili, categorie 1 e 2;
   7. sostanze o miscele auto-reattive dei tipi da A a F;
   8. liquidi piroforici, categoria 1;
   9. solidi piroforici, categoria 1;
   10. sostanze e miscele che, a contatto con l'acqua, liberano gas infiammabili, categorie 1, 2 e 3;
   11. liquidi comburenti, categorie 1, 2 e 3;
   12. solidi comburenti, categorie 1, 2 e 3;
   13. perossidi organici dei tipi da A a F;
   14. tossicita' acuta orale, categorie 1 e 2;
   15. tossicita' acuta per via cutanea, categorie 1 e 2;
   16. tossicita' acuta per inalazione, categorie 1, 2 e 3;
   17. tossicita' specifica per organi bersaglio-esposizione singola, categoria 1.
3. **Fallback gruppo 2**: se nessuno dei due test sopra si applica, il fluido e' **gruppo 2** (art. 9 c. 1 lett. b: tutte le sostanze e miscele non elencate alla lettera a).
4. **Recipienti multi-scomparto** (art. 9 c. 2): se il recipiente ha piu' scomparti, assegna il gruppo dello scomparto piu' critico (gruppo 1 prevale sul gruppo 2). Se uno scomparto contiene piu' fluidi, vale il fluido che porta alla categoria piu' elevata.
5. **Gas instabili**: se il fluido e' un gas instabile, segnala che si applica una eccezione testuale dell'Allegato II (recipienti gas instabili categoria I o II per tabella 1 -> categoria III; tubazioni gas instabili categoria I o II per tabella 6 -> categoria III). Vedi `tasks/determina-categoria.md`.

## Output

```
Classificazione fluido - <nome fluido / miscela>

Stato fisico: <gas/vapore / liquido>
TS dichiarata: <TS> gradi C
Punto di infiammabilita': <valore o "non applicabile">
Classi CLP applicabili: <elenco classi dalla scheda di sicurezza>

Esiti dei test:
- Test TS > punto infiammabilita': <SI / NO / non applicabile>
- Match con una delle 17 classi di pericolo art. 9 c. 1 lett. a): <SI (classe X) / NO>

Gruppo assegnato: <gruppo 1 / gruppo 2>

Note:
- <se gas instabile: nota su eccezione tabella 1 o 6>
- <se TS > punto infiammabilita' decisivo: nota su lett. a incipit>

Rinvio:
- La classificazione CLP del fluido (categorie, classi di pericolo) e' di responsabilita'
  del produttore del fluido (scheda di sicurezza). La skill assume corretta tale
  classificazione e la riporta.
- Il fabbricante dell'attrezzatura resta responsabile della verifica finale.
```

## Limiti

- La skill non classifica il fluido secondo CLP: prende come input la classificazione gia' fatta dal produttore (scheda di sicurezza).
- Per miscele complesse non classificate armonizzate la skill non puo' procedere e segnala la necessita' di una classificazione CLP della miscela.
- Non esiste "gruppo 3" o variante: il D.Lgs 26/2016 prevede solo i due gruppi (1 e 2).
- Il test "TS > punto di infiammabilita'" si applica solo ai fluidi liquidi: per gas/vapore non e' pertinente.
