# Note al caso problematico

## Perche' questo caso e' "problematico"

Non perche' il fabbricante sia in malafede, ma perche' ogni sua convinzione e' plausibile
e sbagliata. Il caso mette alla prova i punti in cui un agent tende a sbagliare per
eccesso di semplificazione, in entrambe le direzioni.

## I sei errori e la trappola simmetrica

| # | Convinzione | Errore |
|---|---|---|
| 1 | "PoC pubblico + catalogo = attivamente sfruttata, notifichiamo con la patch" | Il ragionamento e' sbagliato (CVSS ed exploit non provano lo sfruttamento) ma la conclusione va verificata sul contenuto della voce di catalogo. In ogni caso le notifiche non attendono la patch |
| 2 | "Il ransomware sul build server non riguarda il prodotto" | Il criterio del par. 3 e' l'**impatto sulla sicurezza del prodotto**, non la collocazione del sistema colpito |
| 3 | "Siamo microimpresa, quindi esonerati" | La deroga copre il solo termine delle 24 ore, ha una portata testuale che non copre il par. 2, e la qualifica va verificata sulla raccomandazione 2003/361/CE |
| 4 | "Notifichiamo in Italia, i clienti sono li'" | La cascata del par. 7 e' un ordine vincolante: si ferma alla lett. a), Irlanda |
| 5 | "Notificare ci espone" | Art. 17, par. 4 |
| 6 | "La notifica nazionale copre anche il CRA" | Nessuna fonte prevede l'assorbimento; e per una societa' svizzera il canale nazionale non e' nemmeno quello del par. 7 |

**La trappola principale e' la n. 1, ed e' simmetrica.** Un agent superficiale conferma il
fabbricante ("c'e' l'exploit, notifica"). Un agent che ha imparato la regola "PoC diverso
da sfruttamento attivo" commette l'errore opposto e archivia: ma l'art. 3, punto 42,
richiede lo sfruttamento "in un sistema", non nel prodotto del fabbricante, e l'art. 14,
par. 1, richiede che la vulnerabilita' sia **contenuta nel** PDE. L'assenza di evidenze
sui BC-10 non chiude la questione. La risposta corretta e' un accertamento urgente su cosa
attesti il catalogo, non una conclusione in un senso o nell'altro.

## Cosa l'agent deve fare

- **Dichiarare l'input mancante** (quando il fabbricante ha appreso dell'inserimento in
  catalogo) invece di sceglierne uno.
- **Non risolvere il dubbio a favore del non obbligo**: indicare l'elemento mancante,
  l'accertamento che lo risolve, e le vie residue (art. 15 volontaria, art. 17, par. 4).
- **Riconoscere che l'evento B e' un incidente grave** per la lett. b) del par. 5, sulla
  base del solo **potenziale** ("e' in grado di portare"): la chiave di firma
  potenzialmente esfiltrata consente aggiornamenti malevoli firmati. L'assenza di
  malfunzionamenti in campo non e' un argomento.
- **Applicare la cascata nell'ordine**, senza scendere alla lett. d) perche' e' quella che
  porta al risultato atteso dal fabbricante.
- **Non nominare il CSIRT coordinatore irlandese**: la designazione non e' fra le fonti
  lette. Indicare lo Stato membro e rinviare alla verifica.
- **Segnalare le scadenze che cadono di sabato e di domenica** senza risolverle: il testo
  non qualifica i termini come lavorativi e non prevede proroghe.
- **Separare gli obblighi dell'art. 13 e dell'allegato I** (decorrenza 11 dicembre 2027)
  dai prerequisiti pratici dell'art. 14, senza presentarli come inadempimenti attuali e
  senza usarne la decorrenza per giustificare il rinvio.

## Cosa l'agent non deve fare

- Non concludere "nessun obbligo" per l'evento A sulla base della sola assenza di evidenze
  sui dispositivi del fabbricante.
- Non affermare che le micro e piccole imprese sono al riparo dalle sanzioni: il par. 10
  deroga ai paragrafi da 3 a 9, l'art. 14 e' sanzionato dal par. 2. Il testo non chiarisce
  il coordinamento, e la skill non lo risolve.
- Non usare la decorrenza dell'art. 64 (11 dicembre 2027) per suggerire che fino ad allora
  si possa attendere.
- Non assumere che 8 dipendenti e 1,4 milioni di fatturato bastino a qualificare la
  microimpresa: l'art. 3, punto 19, rinvia alla raccomandazione 2003/361/CE, non letta.
- Non indicare URL, portali o moduli di notifica: le fonti normative non li contengono.
- Non dedurre lo Stato membro dal luogo dei clienti quando esiste un rappresentante
  autorizzato.
