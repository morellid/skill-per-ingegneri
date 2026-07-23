# Task: verifica-aeroilluminazione-servizi-impianti

Inquadra i requisiti di **riscaldamento**, **aeroilluminazione**, **ventilazione**, **servizi igienici** e
**protezione acustica** dei locali di abitazione secondo il **DM 5 luglio 1975 (artt. 4-8)**. Supporto
documentale: **non** esegue calcoli di dettaglio.

## Quando usarla

Il tecnico deve verificare aeroilluminazione, temperatura, ventilazione e dotazioni dei servizi di un alloggio.
Per altezze e superfici minime usa `verifica-altezze-superfici-minime`.

## Passi

1. **Riscaldamento e aria** (art. 4): gli alloggi devono avere **impianti di riscaldamento** ove le condizioni
   climatiche lo richiedano; **temperatura di progetto dell'aria interna 18-20 °C**, uguale in tutti gli
   ambienti abitati e nei servizi (esclusi ripostigli). Le pareti opache non devono presentare **condensazione
   permanente**.

2. **Illuminazione e aeroilluminazione** (art. 5): tutti i locali (esclusi servizi igienici, disimpegni,
   corridoi, vani-scala e ripostigli) devono avere **illuminazione naturale diretta** adeguata; per ciascun
   locale d'abitazione:
   - **fattore di luce diurna medio ≥ 2%**;
   - **superficie finestrata apribile ≥ 1/8 della superficie del pavimento** (rapporto aeroilluminante).

   (Per l'edilizia pubblica residenziale sono richieste **dimensioni unificate** di finestre e infissi.)

3. **Ventilazione** (art. 6): quando manca la **ventilazione naturale**, si ricorre alla **ventilazione
   meccanica centralizzata**; va assicurata l'**aspirazione di fumi, vapori ed esalazioni** nei punti di
   produzione (cucine, gabinetti); il **posto di cottura** annesso al soggiorno deve comunicare ampiamente ed
   avere **aspirazione forzata sui fornelli**.

4. **Stanza da bagno** (art. 7): apertura all'esterno per il ricambio d'aria **o** impianto di **aspirazione
   meccanica**; nelle stanze da bagno sprovviste di apertura è **vietata l'installazione di apparecchi a fiamma
   libera**. Per ciascun alloggio **almeno una stanza da bagno** deve essere dotata di: **vaso, bidet, vasca da
   bagno o doccia, lavabo**.

5. **Protezione acustica** (art. 8): i materiali e la loro messa in opera devono garantire adeguata
   **protezione acustica** (rumori da calpestio, traffico, impianti, suoni aerei da alloggi contigui e da
   spazi/servizi comuni); per i **valori limite** si rinvia al **DPCM 5/12/1997** (skill dedicata).

Usa la checklist in `../references/estratti/requisiti-igienico-sanitari-checklist.md` (sezioni 3-6).

## Output atteso

La verifica di **riscaldamento** (18-20 °C), **aeroilluminazione** (FLDm ≥ 2%; finestra ≥ 1/8 del pavimento),
**ventilazione** e **dotazione dei servizi** dell'alloggio rispetto ai valori del DM 5/7/1975, con **rinvio
agli articoli**. Nessun calcolo illuminotecnico/termotecnico di dettaglio.

## Cosa NON fare

- Non **eseguire** calcoli di dettaglio (fattore di luce diurna, dispersioni termiche) né dimensionare gli
  impianti.
- Non **fornire** i valori limite acustici (→ skill DPCM 5/12/1997) né i requisiti di accessibilità (→ skill DM
  236/1989); non applicare deroghe/regolamenti regionali/comunali.
