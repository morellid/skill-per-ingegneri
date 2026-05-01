# Note di dominio - Frazionamento con deposito comunale duplicato

## Perche' questo esempio e' rappresentativo

Caso tipico di **errore di transizione normativa**: il geometra applica per inerzia il regime previgente (deposito comunale a cura del professionista, art. 30 co. 5 DPR 380/2001) anche dopo l'entrata in vigore (1/7/2025) del nuovo regime telematico (art. 30 co. 5-bis introdotto da art. 25 D.Lgs. 1/2024 e operativo con Provv. AdE 30/12/2024 e Risoluzione AdE 40/E del 9/6/2025).

L'errore e' particolarmente insidioso perche':

1. il geometra tiene un comportamento "diligente" (deposito al Comune + attestazione + dichiarazione DSAN coerente con il deposito), ma applica la **disciplina sbagliata** per il periodo di trasmissione;
2. la Risoluzione 40/E 2025 (nota 4) prevede esplicitamente che il deposito comunale duplicato rende l'atto "privo di effetti" e quindi NON approvabile - non e' una semplice irregolarita' formale;
3. il rifiuto arriva dopo la trasmissione, con potenziale impatto sul rogito programmato.

L'esempio permette alla skill di esercitare il task `diagnosi-rifiuti-telematici.md` (mapping messaggio Ufficio -> causa -> correzione) e di rinforzare la regola operativa: **per FR/FM/SC dal 1/7/2025, mai deposito comunale a cura del professionista**.

## Fonti applicate

- `references/estratti/dpr-380-2001-art-30.md` - confronto regime co. 5 vs co. 5-bis
- `references/estratti/risoluzione-40-2025-deposito-telematico.md` - ambito FR/FM/SC, dichiarazione riga 9, workflow Portale Comuni, **nota 4 sul deposito comunale duplicato**
- `references/sources.yaml`: `ade-provvedimento-30-12-2024-deposito-telematico` (decorrenza 1/7/2025)

## Analisi critica della responsabilita'

Il geometra non ha agito con dolo: ha attestato un fatto vero (deposito al Comune del 6/8/2025) e ha rispettato la versione obbligatoria di Pregeo (10.6.5 - APAG 2.15). Tuttavia, per il combinato disposto di:

- art. 1176 co. 2 c.c. (diligenza professionale);
- art. 2236 c.c. (responsabilita' del professionista);
- art. 76 DPR 445/2000 (sanzioni penali per false dichiarazioni o mendacio - non integrato nel caso, ma profilo da considerare in casi piu' gravi);
- responsabilita' civile verso il committente per il ritardo nell'aggiornamento catastale e l'eventuale slittamento del rogito;

il geometra dovrebbe:

1. ridepositare l'atto correttamente, **a proprie spese** (i tributi catastali del primo invio rifiutato sono comunque dovuti? verificare con UPT - generalmente sono restituiti per atti respinti in fase di trasmissione, ma la prassi varia);
2. comunicare al committente l'incidente in modo trasparente;
3. valutare con la propria compagnia assicurativa eventuali profili di RC professionale, soprattutto se il ritardo causa danno (mancata stipula del rogito alla data prefissata, perdita di una caparra, ecc.);
4. aggiornare le proprie procedure interne per evitare errori analoghi su atti FR/FM/SC futuri.

## Variante - se il rogito fosse imminente

Se il rifiuto arrivasse a pochi giorni dal rogito (es. 13/9/2025 per rogito 15/9/2025), il geometra dovrebbe:

- **immediatamente** avvisare il notaio per concordare un differimento del rogito;
- valutare se richiedere al notaio una **scrittura privata di differimento** o una promessa di vendita con clausola sospensiva (legato all'approvazione del nuovo Pregeo);
- ri-trasmettere l'atto via Sister il prima possibile e verificare l'esito quotidianamente.

## Validazione di dominio

Esempio non ancora validato da geometra terzo. Da sottoporre a Livello 2 di validazione (`methodology/validazione.md`).
