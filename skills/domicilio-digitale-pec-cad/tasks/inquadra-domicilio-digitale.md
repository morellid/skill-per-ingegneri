# Task: inquadra-domicilio-digitale

Determina l'**indice competente** (INI-PEC, IPA, INAD) e il **regime** (obbligo/facoltà)
del domicilio digitale in base al **soggetto**, ai sensi degli **artt. 3-bis, 6-bis, 6-ter,
6-quater del CAD**. Non elegge né registra il domicilio: fornisce l'inquadramento.

## Input

- Tipo di soggetto: **PA / gestore di pubblico servizio / società a controllo pubblico**;
  **impresa** (registro imprese); **professionista** iscritto in albo/elenco;
  **professionista non iscritto**, **persona fisica** o altro ente di diritto privato.
- Finalità (comunicazioni con la PA, ricezione di notifiche, elezione volontaria).

## Procedura

1. **Regime obbligo/facoltà (art. 3-bis cc. 1, 1-bis)**
   - **Obbligo** per PA, professionisti tenuti all'iscrizione in albi/elenchi e imprese: si
     dotano di un domicilio digitale in **INI-PEC** (6-bis) o **IPA** (6-ter).
   - **Facoltà** per chiunque altro: elezione in **INAD** (6-quater).

2. **Indice competente**
   - **PA / gestori di pubblici servizi / società a controllo pubblico** → **IPA** (art.
     6-ter), gestito da **AgID**.
   - **Imprese e professionisti iscritti in albi/registri** → **INI-PEC** (art. 6-bis),
     presso il **MISE/MIMIT**; i domicili ivi inseriti sono **mezzo esclusivo** con la PA.
   - **Persone fisiche, professionisti non iscritti, altri enti** → **INAD** (art. 6-quater),
     gestito da **AgID**.

3. **Elezione e modalità (art. 3-bis cc. 1-ter, 1-quater)**
   - Le persone fisiche possono eleggere il domicilio anche via **ANPR** (art. 62) o presso
     l'ufficio anagrafe; obbligo di **uso diligente** e di comunicare variazioni (Linee guida).
   - Valuta l'eventuale **domicilio digitale speciale** per determinati atti/affari (c.
     4-quinquies).

4. **Coordinamento tra indici**
   - Segnala l'**allineamento** INI-PEC/IPA (art. 6-ter c. 2-bis) e il trasferimento
     INAD/ANPR (art. 6-quater c. 3); per i professionisti iscritti in albo il domicilio è
     quello in INI-PEC salvo elezione diversa.

## Output

Inquadramento con: indice competente (INI-PEC/IPA/INAD), regime (obbligo/facoltà), modalità
di elezione e note sul coordinamento tra indici. Rinvia elezione/registrazione ai gestori
(AgID, MIMIT, Camere di commercio) e alle Linee guida AgID.

## Riferimenti

- `../references/fonti/dlgs-82-2005-domicilio-digitale.md` (artt. 3-bis, 6-bis, 6-ter, 6-quater)
- `../references/estratti/domicilio-digitale-checklist.md` (sez. 1-2, 4, sintesi)
