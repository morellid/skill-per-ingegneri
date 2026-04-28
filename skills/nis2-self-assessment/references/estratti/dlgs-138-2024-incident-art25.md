# D.Lgs. 138/2024 - Notifica incidente significativo (art. 25)

> Fonte: D.Lgs. 4 settembre 2024, n. 138 - GU Serie Generale n. 230 del 01/10/2024.
> Fonte catalogata in `sources.yaml` come `dlgs-138-2024`.
> Estratto verbatim dell'art. 25 e note operative.
> Data consultazione: 2026-04-29.

## Art. 25 - Obblighi in materia di notifica di incidente

> 1. I soggetti essenziali e i soggetti importanti notificano, senza ingiustificato ritardo, al CSIRT Italia ogni incidente che, ai sensi del comma 4, ha un impatto significativo sulla fornitura dei loro servizi, secondo le modalita' e i termini di cui agli articoli 30, 31 e 32.
>
> 2. Le notifiche includono le informazioni che consentono al CSIRT Italia di determinare un eventuale impatto transfrontaliero dell'incidente.
>
> 3. La notifica non espone il soggetto che la effettua a una maggiore responsabilita' rispetto a quella derivante dall'incidente.
>
> 4. Un incidente e' considerato significativo se:
>    a) ha causato o e' in grado di causare una grave perturbazione operativa dei servizi o perdite finanziarie per il soggetto interessato;
>    b) ha avuto ripercussioni o e' idoneo a provocare ripercussioni su altre persone fisiche o giuridiche causando perdite materiali o immateriali considerevoli.
>
> 5. Ai fini della notifica di cui al comma 1, i soggetti interessati trasmettono al CSIRT Italia:
>    a) senza ingiustificato ritardo, e comunque entro 24 ore da quando sono venuti a conoscenza dell'incidente significativo, una pre-notifica che, ove possibile, indichi se l'incidente significativo possa ritenersi il risultato di atti illegittimi o malevoli o puo' avere un impatto transfrontaliero;
>    b) senza ingiustificato ritardo, e comunque entro 72 ore da quando sono venuti a conoscenza dell'incidente significativo, una notifica dell'incidente che, ove possibile, aggiorni le informazioni di cui alla lettera a) e indichi una valutazione iniziale dell'incidente significativo, comprensiva della sua gravita' e del suo impatto, nonche', ove disponibili, gli indicatori di compromissione;
>    c) su richiesta del CSIRT Italia, una relazione intermedia sui pertinenti aggiornamenti della situazione;
>    d) una relazione finale entro un mese dalla trasmissione della notifica dell'incidente di cui alla lettera b), che comprenda:
>       1) una descrizione dettagliata dell'incidente, ivi inclusi la sua gravita' e il suo impatto;
>       2) il tipo di minaccia o la causa originale (root cause) che ha probabilmente innescato l'incidente;
>       3) le misure di attenuazione adottate e in corso;
>       4) ove noto, l'impatto transfrontaliero dell'incidente;
>    e) in caso di incidente in corso al momento della trasmissione della relazione finale di cui alla lettera d), una relazione mensile sui progressi e una relazione finale entro un mese dalla conclusione della gestione dell'incidente.
>
> 6. In deroga a quanto previsto dal comma 5, lettera b), un prestatore di servizi fiduciari, in relazione a incidenti significativi che abbiano un impatto sulla fornitura dei suoi servizi fiduciari, provvede alla notifica di cui alla medesima lettera, senza indebito ritardo e comunque entro 24 ore da quando sono venuti a conoscenza dell'incidente significativo.
>
> 7. Fermo restando quanto previsto dall'articolo 15, comma 4, senza ingiustificato ritardo e ove possibile entro 24 ore dal ricevimento della pre-notifica di cui al comma 5, lettera a), il CSIRT Italia fornisce una risposta al soggetto notificante, comprensiva di un riscontro iniziale sull'incidente significativo e, su richiesta del soggetto, orientamenti o consulenza sull'attuazione di possibili misure tecniche di mitigazione. Su richiesta del soggetto notificante, il CSIRT Italia fornisce ulteriore supporto tecnico.
>
> 8. Qualora si sospetti che l'incidente significativo abbia carattere criminale, il CSIRT Italia fornisce al soggetto notificante anche orientamenti sulla segnalazione dell'incidente significativo, all'organo centrale del Ministero dell'interno per la sicurezza e per la regolarita' dei servizi di telecomunicazione [...] (Autorita' di contrasto).
>
> 9. Sentito il CSIRT Italia, se ritenuto opportuno e qualora possibile, i soggetti essenziali e i soggetti importanti comunicano, senza ingiustificato ritardo, ai destinatari dei loro servizi gli incidenti significativi che possono ripercuotersi negativamente sulla fornitura di tali servizi.
>
> 10. I soggetti essenziali e i soggetti importanti, se ritenuto opportuno e qualora possibile, sentito il CSIRT Italia, comunicano senza ingiustificato ritardo, ai destinatari dei loro servizi che sono potenzialmente interessati da una minaccia informatica significativa, misure o azioni correttive o di mitigazione che tali destinatari possono adottare in risposta a tale minaccia. [...]

## Sintesi delle tempistiche

| Step | Termine | Cosa | Riferimento |
|------|---------|------|-------------|
| Pre-notifica | **entro 24 ore** dalla conoscenza | Prima segnalazione: atto illegittimo/malevolo? impatto transfrontaliero? | art. 25 co. 5 lett. a |
| Notifica | **entro 72 ore** dalla conoscenza | Valutazione iniziale di gravita' e impatto + IoC ove disponibili | art. 25 co. 5 lett. b |
| (Deroga prestatori serv. fiduciari) | **entro 24 ore** dalla conoscenza | Notifica anticipata | art. 25 co. 6 |
| Relazione intermedia | Su richiesta CSIRT | Aggiornamenti | art. 25 co. 5 lett. c |
| Relazione finale | **entro 1 mese** dalla notifica | Descrizione completa, root cause, mitigazione, impatto transfrontaliero | art. 25 co. 5 lett. d |
| Incidente in corso al momento del report finale | Mensile | Aggiornamento progressi | art. 25 co. 5 lett. e |
| Relazione finale alternativa | **entro 1 mese** dalla conclusione | Quando l'incidente continua oltre il primo mese | art. 25 co. 5 lett. e |
| Riscontro CSIRT | entro 24h dalla pre-notifica | Riscontro iniziale + orientamenti | art. 25 co. 7 |
| Comunicazione ai destinatari | Senza ingiustificato ritardo | Quando l'incidente puo' ripercuotersi sui servizi forniti | art. 25 co. 9 |

## Soglia di significativita'

L'incidente e' significativo (art. 25 co. 4) se:
- **lettera a)**: ha causato o e' in grado di causare grave perturbazione operativa o perdite finanziarie per il soggetto **OPPURE**
- **lettera b)**: ha avuto o puo' avere ripercussioni su altre persone fisiche/giuridiche causando perdite materiali o immateriali **considerevoli**.

Questi sono criteri elevati ma volutamente generali. La **Determinazione ACN 164179/2025** definisce gli "incidenti significativi di base" con soglie quantitative (vedi `acn-incidenti-significativi.md`).

## Coordinamento con altre notifiche

- **GDPR art. 33**: data breach con dati personali -> notifica al Garante Privacy entro 72h. Le due notifiche **si sommano** (parallele) quando l'incidente coinvolge anche dati personali.
- **Codice comunicazioni elettroniche**: per fornitori di reti e servizi di comunicazione elettronica, art. 40 D.Lgs. 259/2003 prevede notifica all'Autorita'. La notifica NIS2 al CSIRT Italia non sostituisce automaticamente quella ex codice (verificare le determine ACN di settore per l'eventuale unificazione).
- **PSNC** (Perimetro Sicurezza Nazionale Cibernetica, DL 105/2019): la notifica ex art. 1 co. 3 lett. a) del DL 105/2019, effettuata dai soggetti rientranti anche nell'ambito NIS2, **assolve** agli obblighi di cui all'art. 25 (cfr. art. 44 D.Lgs. 138/2024 che modifica l'art. 1 co. 8 del DL 105/2019).
- **DORA** (Reg. UE 2022/2554): per le entita' finanziarie identificate da DORA, la notifica DORA prevale sulla NIS2 per i settori 3 e 4 dell'Allegato I (cfr. art. 3 co. 14 D.Lgs. 138/2024).
