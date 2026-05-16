# Expected output: SecureGate FX-2100

## 1. Ambito di applicazione (task check-ambito-applicabilita)

**Esito: RIENTRA nell'ambito del CRA**.

- Il prodotto e' un PDE ex art. 3 punto 1 (hardware con firmware integrato).
- Connessione dati: si', e' la funzione costitutiva del prodotto.
- Esclusioni esaminate (art. 2 par. 2-4, 6-7): **nessuna applicabile**.
  - Non e' dispositivo medico (Reg. 2017/745 / 2017/746): non applicabile.
  - Non e' componente veicolo motore (Reg. 2019/2144): non applicabile.
  - Non e' aviazione civile (Reg. 2018/1139): non applicabile.
  - Non e' equipaggiamento marittimo (Direttiva 2014/90/UE): non applicabile.
  - Non e' pezzo di ricambio identico (art. 2 par. 6): non applicabile.
  - Non e' sicurezza nazionale/difesa (art. 2 par. 7): non applicabile.

## 2. Classificazione (task classifica-pde)

- **Categoria CRA: PDE importante Classe II**.
- Funzionalita' principale dichiarata: ispezione pacchetti e filtraggio del traffico di rete (firewall stateful con DPI).
- Categoria di riferimento: **Allegato III Classe II punto 2**: "Firewall, sistemi di rilevamento e prevenzione delle intrusioni (IDS/IPS)".
- Fondamento normativo: **Art. 7 par. 1** del Regolamento (UE) 2024/2847.
- Caveat applicabili:
  - Integrazione in altro prodotto: no.
  - Open source qualificato: no.
  - Le funzionalita' secondarie (logging, VPN) non spostano la classificazione: vale la funzionalita' principale.

## 3. Procedure ammesse (task scegli-procedura-conformita)

Per la Classe II (art. 32 par. 3):

- Modulo A: **NON ammesso**.
- Modulo B + C: **ammesso**.
- Modulo H: **ammesso**.
- Certificazione europea di cibersicurezza ex art. 27 par. 9 (livello minimo "sostanziale"): **ammessa**, se disponibile per la categoria firewall.

**Procedura consigliata: Modulo H** (Allegato VIII parte IV), in linea con la dichiarazione del fabbricante di disporre di sistema qualita' approvato. Note:

- Coinvolgimento organismo notificato: approvazione del sistema qualita' e sorveglianza con audit periodici (Allegato VIII parte IV punti 3-4).
- **Numero ON apposto accanto alla marcatura CE** (art. 30 par. 4).
- Documentazione richiesta: tecnica (art. 31 + Allegato VII), sistema qualita' (parte IV punto 3.2), DoC UE per modello (art. 28 + Allegato V).
- Conservazione: 10 anni o periodo di assistenza se piu' lungo (art. 13 par. 13). Qui: 10 anni, perche' il periodo di assistenza dichiarato e' 7 anni.
- L'organismo notificato dev'essere selezionato dalla banca dati NANDO della Commissione europea (art. 43 par. 2).

## 4. Documentazione tecnica - copertura Allegato VII (task check-documentazione-tecnica)

Sintesi: indice della documentazione coerente con gli 8 punti dell'Allegato VII; verifica puntuale conferma:

- Punto 1 (descrizione generale, art. 31 + All. VII): coperto (finalita' prevista, versioni firmware, fotografie, istruzioni utilizzatore conformi Allegato II).
- Punto 2 (progettazione, sviluppo, gestione vulnerabilita'): coperto (SBOM SPDX 2.3 con dipendenze di primo livello come previsto Allegato I parte II punto 1, CVD pubblicata Allegato I parte II punto 5, contatto sicurezza Allegato I parte II punto 6, soluzioni per aggiornamenti sicuri Allegato I parte II punti 7-8).
- Punto 3 (valutazione rischi cibersicurezza, art. 13 par. 2-3-4 + All. I parte I): coperto, tutti i 13 requisiti dell'Allegato I parte I lett. a-m trattati o motivatamente non applicabili.
- Punto 4 (periodo di assistenza, art. 13 par. 8): coperto, **7 anni** (oltre il minimo di 5 anni).
- Punto 5 (norme armonizzate / specifiche comuni / certificazione UE): coperto.
- Punto 6 (test reports): coperto.
- Punto 7 (DoC UE, art. 28 + Allegato V): coperto, 8 elementi presenti.
- Punto 8 (SBOM su richiesta autorita' vigilanza): coperto.

Requisiti formali (art. 31 par. 2-4, art. 13 par. 13):

- Documentazione antecedente all'immissione: OK.
- Lingua adeguata all'ON: OK.
- Aggiornamento per periodo di assistenza: previsto.
- Conservazione 10 anni: previsto.

**Esito: documentazione completa per immissione sul mercato sotto modulo H.**

## 5. Azioni richieste

- Nessuna azione BLOCKER. Confermare con l'ON candidato la copertura specifica delle norme armonizzate applicate per la categoria firewall (post pubblicazione GUUE).
- Verificare che la SBOM venga aggiornata a ogni release maggiore del firmware durante il periodo di assistenza.
- Documentare formalmente la procedura interna per la gestione delle segnalazioni di vulnerabilita' ricevute via canale CVD (art. 14 segnalazione).

## Disclaimer

L'output e' un ausilio alla verifica formale. La responsabilita' della corretta classificazione e dell'adeguatezza tecnica della documentazione ricade sul fabbricante o sul rappresentante autorizzato.
