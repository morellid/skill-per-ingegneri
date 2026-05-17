# Expected output: HomeNet R3

## 1. Ambito di applicazione (task check-ambito-applicabilita)

**Esito: RIENTRA nell'ambito del CRA**.

- Il prodotto e' un PDE ex art. 3 punto 1 (hardware con firmware + app companion).
- Connessione dati: si', e' la funzione costitutiva.
- Esclusioni esaminate: nessuna applicabile.

## 2. Classificazione (task classifica-pde)

- **Categoria CRA: PDE importante Classe I**.
- Funzionalita' principale: router Wi-Fi domestico.
- Categoria di riferimento: **Allegato III Classe I punto 12**: "Router, modem per la connessione a Internet e switch".
- Fondamento normativo: **Art. 7 par. 1** del Regolamento (UE) 2024/2847.

## 3. Procedure ammesse (task scegli-procedura-conformita) - BLOCKER

Per la Classe I (art. 32 par. 2):

- **Modulo A: ammesso SOLO se** il fabbricante applica integralmente norme armonizzate, specifiche comuni o certificazione europea di livello "sostanziale".
- Il fabbricante dichiara di "voler tenere conto" delle norme armonizzate ma **non si impegna ad applicarle integralmente** -> **modulo A NON utilizzabile**.
- Procedure ammesse alternative: B+C (Allegato VIII parti II + III) oppure H (parte IV), oppure certificazione europea di cibersicurezza di livello almeno "sostanziale" (art. 27 par. 9).

**Conclusione: il piano del fabbricante di usare il modulo A senza applicazione integrale delle norme armonizzate viola l'art. 32 par. 2.** Va rivisto a B+C, H, o certificazione europea.

**Nota PMI**: art. 32 par. 6 prevede **tariffe ridotte degli organismi notificati** per PMI e start-up. Inoltre, l'art. 33 par. 5 prevede un **modulo semplificato di documentazione tecnica** per le microimprese e PMI per cui la Commissione adottera' atti di esecuzione.

## 4. Documentazione tecnica - copertura Allegato VII (task check-documentazione-tecnica)

Coperture: **2/8 punti coperti formalmente, 6/8 carenti o mancanti**.

- Punto 1 (descrizione generale): **parziale**: scheda tecnica e manuale presenti ma istruzioni utilizzatore (Allegato II) non strutturate sui 9 punti obbligatori. Manca riferimento esplicito a URL della DoC UE, punto di contatto unico per vulnerabilita', data finale del periodo di assistenza, istruzioni per disattivazione aggiornamenti automatici.
- Punto 2 (progettazione, sviluppo, gestione vulnerabilita'): **BLOCKER**: SBOM in formato PDF (non leggibile da dispositivo automatico - viola Allegato I parte II punto 1), politica CVD assente (viola Allegato I parte II punto 5), contatto sicurezza dedicato assente (viola Allegato I parte II punto 6).
- Punto 3 (valutazione rischi): **BLOCKER**: la valutazione dei rischi non tratta esplicitamente i 13 requisiti dell'Allegato I parte I lett. a-m, ne' giustifica eventuali non applicabilita' come richiesto dall'art. 13 par. 4.
- Punto 4 (periodo di assistenza): **BLOCKER**: 3 anni dichiarati, **inferiore al minimo legale di 5 anni** (art. 13 par. 8). Il fabbricante deve estendere il periodo o documentare che la durata di utilizzo prevista del prodotto e' inferiore a 5 anni (improbabile per un router consumer).
- Punto 5 (norme armonizzate / specifiche comuni): **mancante**: non e' descritta l'applicazione integrale di norme armonizzate, ne' sono descritte soluzioni alternative.
- Punto 6 (test reports): **mancante**: non presenti o non identificati.
- Punto 7 (DoC UE - Allegato V): **BLOCKER**: la DoC e' in formato vecchio LVD/RED; va riscritta secondo Allegato V con gli 8 elementi (riferimento esplicito al CRA, riferimento a norme armonizzate, eventuale ON, ecc.).
- Punto 8 (SBOM su richiesta): **mancante**: se prodotta in PDF non leggibile da macchina, non soddisfa l'obbligo di formato (Allegato I parte II punto 1 e Allegato VII punto 8).

Requisiti formali:

- Documentazione antecedente all'immissione: KO (incompleta).
- Lingua: da verificare con ON quando designato.
- Aggiornamento per periodo di assistenza: da formalizzare.
- Conservazione 10 anni: da formalizzare nelle procedure interne.

## 5. Azioni richieste (in ordine di priorita')

**BLOCKER (da risolvere prima di immissione sul mercato):**

1. **Cambiare modulo**: passare da modulo A a B+C o H (oppure certificazione europea ex art. 27 par. 9). Avviare dialogo con ON candidato in NANDO post 11/6/2026.
2. **Estendere periodo di assistenza**: portarlo ad almeno 5 anni (art. 13 par. 8).
3. **Riscrivere DoC UE** secondo Allegato V (8 elementi), con riferimento esplicito al Reg. (UE) 2024/2847.
4. **Riscrivere la valutazione dei rischi** trattando ciascuno dei 13 requisiti dell'Allegato I parte I lett. a-m (o motivando la non applicabilita', art. 13 par. 4).
5. **Implementare politica CVD pubblica** (Allegato I parte II punto 5) e **canale di contatto dedicato** per le vulnerabilita' (Allegato I parte II punto 6).
6. **Riprodurre la SBOM in formato leggibile da dispositivo automatico** (SPDX, CycloneDX, ecc.), con almeno le dipendenze di primo livello.

**Integrazione consigliata:**

- Strutturare la documentazione tecnica sui 8 punti dell'Allegato VII (capitoli e sottocapitoli).
- Predisporre soluzioni tecniche per la distribuzione sicura degli aggiornamenti (Allegato I parte II punti 7-8) e descriverle nella documentazione.
- Valutare il vantaggio del **modulo H** se il fabbricante intende produrre piu' modelli di router come famiglia di prodotti (un solo sistema qualita' approvato copre l'intera linea).
- Tenere conto delle **tariffe ridotte** PMI (art. 32 par. 6) e del **modulo semplificato di documentazione** (art. 33 par. 5).

## Disclaimer

L'output e' un ausilio alla verifica formale. Le decisioni operative (cambio modulo, riscrittura documentazione, designazione ON) restano responsabilita' del fabbricante.
