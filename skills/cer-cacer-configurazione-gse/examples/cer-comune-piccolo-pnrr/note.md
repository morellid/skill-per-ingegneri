# Note di dominio - cer-comune-piccolo-pnrr

## Perche' e' un caso conforme

- Comune con popolazione **inferiore alla soglia PNRR** (1.812 ab.): rientra sia nel regime originario (< 5.000 ab.) sia in quello esteso post DM 127/2025 (< 50.000 ab.) -> apre il contributo PNRR ex art. 8 DM 7/12/2023.
- POD nella **stessa cabina primaria** -> rispettato il perimetro CACER per accedere alla TIP sulla sotto-configurazione incentivata.
- Soggetti compatibili con la CER (art. 31 D.Lgs. 199/2021): persone fisiche, PMI senza energia come attivita' principale, ente locale, ente religioso. **Nessuna grande impresa** come socia.
- Impianto FER (FV) entro **1 MW** (350 kW), in fascia **200-600 kW** ai fini della parte fissa TIP.

## Punti che la skill deve cogliere correttamente

1. La presenza di un Comune e di una parrocchia non altera la natura della CER, ma rende particolarmente coerente la finalita' "sociale" (es. fondo poverta' energetica).
2. Il fattore di condivisione `eta_share` deve essere **dichiarato dall'utente** con motivazione/fonte (qui: ipotesi del progettista 0.45 basata su sovrapposizione produzione/prelievo per mix residenziale + PMI turismo, da rivedere con profili orari).
3. Il **cumulo TIP + PNRR** e' ammesso ma con **riduzione della parte fissa della TIP**: la skill non deve ignorarlo.
4. Il **titolo abilitativo** di un impianto FV 350 kW e' fuori dalle fonti di questa skill (DPR 380/2001, D.Lgs. 28/2011, normativa regionale): la skill deve segnalare DA VERIFICARE, non scegliere il titolo al posto del professionista.
5. La forma giuridica della CER (associazione, cooperativa, ETS) **non e' decisa dalla skill**: deve essere indicata come scelta da fare con consulente legale e formalizzata nella modalita' richiesta dalla forma scelta (atto pubblico presso notaio, scrittura privata autenticata, RUNTS, ecc.).
6. Il calcolo dell'energia condivisa e' parametrico: la skill non deve dare numeri esatti di TIP in EUR senza richiamare valori vigenti.

## Cosa NON deve dire la skill

- Non deve garantire un valore preciso di TIP o TR in EUR/kWh (rinvio a pubblicazioni GSE/ARERA vigenti).
- Non deve produrre lo statuto come "definitivo".
- Non deve assumere che il contributo PNRR sia automatico senza verificare i milestone temporali e il DNSH.

## Possibili insidie

- Se il Comune avesse popolazione ISTAT 31/12/2025 di 50.000 ab. esatti o piu' (regime post DM 127/2025), l'accesso PNRR salta: la skill deve segnalarlo come verifica obbligatoria.
- Se uno dei POD del Comune fosse fuori dalla cabina primaria della sotto-configurazione incentivata (caso possibile in piccoli Comuni con piu' cabine), si dovrebbero ipotizzare **piu' sotto-configurazioni incentivate distinte** all'interno della stessa CER (oppure escludere quel POD dal perimetro tecnico iniziale).
- Se l'impianto fosse in autoconsumo "a ridosso" (impianto e POD del Comune sullo stesso punto) si avrebbe **autoconsumo fisico** non condivisibile: la skill deve distinguere tra immesso in rete e autoconsumato fisico.
- Se la CER volesse estendersi a un Comune limitrofo con cabina primaria diversa, e' tecnicamente possibile mantenere **un unico soggetto giuridico CER** con due richieste GSE distinte: la skill non deve forzare la spaccatura del soggetto.
