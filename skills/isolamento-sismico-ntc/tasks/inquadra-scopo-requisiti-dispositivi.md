# Task: inquadra-scopo-requisiti-dispositivi

Inquadra lo **scopo e le strategie** dell'isolamento sismico, i **requisiti generali** e le **indicazioni
progettuali** dei dispositivi secondo le **NTC 2018 par. 7.10.1-7.10.4**. Supporto documentale: **non** progetta i
dispositivi.

## Quando usarla

Il progettista deve impostare un edificio/ponte a isolamento sismico alla base e inquadrarne scopo, requisiti e
regole progettuali. Per modellazione, analisi e verifiche usa `inquadra-modellazione-analisi-verifiche`.

## Passi

1. **Scopo e strategie** (§7.10.1): il sistema d'isolamento è posto **al di sotto della costruzione** (o di una sua
   porzione) per migliorarne la risposta alle azioni sismiche orizzontali, mediante: (a) **incremento del periodo
   fondamentale** (per portarlo nel campo delle minori accelerazioni); (b) **limitazione della massima forza
   orizzontale** trasmessa; eventualmente con **dissipazione** di energia. Le prescrizioni non si applicano ai
   sistemi con elementi dissipativi distribuiti a vari livelli della costruzione.
2. **Definizioni** (§7.10.2): **interfaccia d'isolamento** (superficie su cui è attivo il sistema);
   **sottostruttura** (sotto l'interfaccia, incl. fondazioni); **sovrastruttura** (parte isolata, sopra
   l'interfaccia).
3. **Requisiti generali** (§7.10.2): sovrastruttura e sottostruttura si devono mantenere in **campo sostanzialmente
   elastico** e possono essere progettate con i particolari costruttivi delle costruzioni con **agS ≤ 0,075g** (con
   deroga, per il c.a., ai §7.4.6 e §7.9.6). Al **sistema d'isolamento** è richiesta un'**affidabilità superiore**
   per il suo ruolo critico.
4. **Dispositivi - accettazione** (§7.10.3): i dispositivi si utilizzano **solo se conformi al §11.9** (caratteristiche
   e prove).
5. **Indicazioni progettuali** (§7.10.4):
   - **dispositivi** (§7.10.4.1): garantirne **accesso, ispezionabilità, sostituibilità**; prevedere sistemi di
     contrasto per il **ricentraggio**; proteggerli da fuoco/attacchi chimici-biologici;
   - **movimenti indesiderati** (§7.10.4.2): centro di massa e centro di rigidezza **coincidenti**; dispositivi
     **perimetrali** e **staticamente ridondanti**; il carico verticale V sul singolo isolatore sotto sisma deve
     essere di compressione o al più nullo (**V ≥ 0**); se V < 0, la trazione deve essere in modulo **< min(2G, 1
     MPa)** per gli elastomerici (o dimostrata/assorbita);
   - **spostamenti differenziali** (§7.10.4.3): **diaframma rigido sopra e sotto** il sistema; elementi verticali
     con spostamento **< 1/20** dello spostamento relativo (in campo elastico);
   - **spostamenti relativi** (§7.10.4.4): **spazio libero** tra sovrastruttura isolata e terreno/costruzioni
     circostanti in tutte le direzioni.

Usa la checklist in `../references/estratti/isolamento-sismico-checklist.md` (sezione 1).

## Output atteso

Un inquadramento che indichi scopo/strategie, i requisiti (campo elastico, agS≤0,075g, affidabilità §11.9) e le
indicazioni progettuali (V≥0, diaframma rigido, spazio libero) con **rinvio ai paragrafi** NTC. Nessun progetto dei
dispositivi.

## Cosa NON fare

- Non **progettare** né qualificare i dispositivi (§11.9); non eseguire prove.
- Non trattare modellazione/analisi/verifiche (usa l'altro task).
