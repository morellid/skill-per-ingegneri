# Note di dominio - cer-comune-piccolo-pnrr

## Perche' e' un caso conforme

- Comune con popolazione **< 5.000 abitanti** -> apre il contributo PNRR ex art. 8 DM 7/12/2023.
- POD nella **stessa cabina primaria** -> rispettato il perimetro CACER per accedere alla TIP.
- Soggetti compatibili con la CER: persone fisiche, PMI senza energia come attivita' principale, ente locale, ente religioso. **Nessuna grande impresa**.
- Impianto FER (FV) entro **1 MW** (350 kW), in fascia **200-600 kW** ai fini della parte fissa TIP.

## Punti che la skill deve cogliere correttamente

1. La presenza di un Comune e di una parrocchia non altera la natura della CER, ma rende particolarmente coerente la finalita' "sociale" (es. fondo poverta' energetica).
2. Il fattore di condivisione `eta_share` parametrico va scelto in modo realistico: 0.45 e' un valore medio per mix residenziale + PMI turismo. Va dichiarato esplicitamente.
3. Il **cumulo TIP + PNRR** e' ammesso ma con **riduzione della parte fissa della TIP**: la skill non deve ignorarlo.
4. L'impianto da 350 kW non e' eligibile a Modello Unico semplificato; serve un titolo abilitativo coerente con la potenza (PAS o autorizzazione).
5. La forma giuridica della CER (associazione, cooperativa, ETS) **non e' decisa dalla skill**: deve essere indicata come scelta da fare con notaio.
6. Il calcolo dell'energia condivisa e' parametrico: la skill non deve dare numeri esatti di TIP in EUR senza richiamare valori vigenti.

## Cosa NON deve dire la skill

- Non deve garantire un valore preciso di TIP o TR in EUR/kWh (rinvio a pubblicazioni GSE/ARERA vigenti).
- Non deve produrre lo statuto come "definitivo".
- Non deve assumere che il contributo PNRR sia automatico senza verificare i milestone temporali e il DNSH.

## Possibili insidie

- Se il Comune avesse popolazione ISTAT 31/12/2025 di 5.000 ab. esatti o piu', l'accesso PNRR salta: la skill deve segnalarlo come verifica obbligatoria.
- Se uno dei POD del Comune fosse fuori dalla cabina primaria (caso possibile in piccoli Comuni con piu' cabine), si dovrebbero costituire CACER distinte.
- Se l'impianto fosse in autoconsumo "a ridosso" (impianto e POD del Comune sullo stesso punto) si avrebbe **autoconsumo fisico** non condivisibile: la skill deve distinguere tra immesso in rete e autoconsumato fisico.
