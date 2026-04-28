# Note di dominio - Caso utility energetica essenziale

## Perche' questo caso

Esempio paradigmatico di **soggetto essenziale** ex art. 6 co. 1 lett. a) D.Lgs. 138/2024:
- Settore Allegato I (energia, sottosettore elettrica)
- Tipologia di soggetto chiaramente elencata (DSO + produttore)
- Dimensione "grande" (tutti e tre i parametri ben oltre i massimali)

L'esito di classificazione e' netto e non richiede valutazione discrezionale.

## Aspetti utili per l'auto-validazione della skill

- La **size-cap rule** opera in due passaggi: (1) supera massimali piccole imprese -> in ambito; (2) supera massimali medie imprese -> essenziale (se Allegato I). In questo caso entrambi i passaggi sono soddisfatti.
- Il fatto che ENERGOSPA non sia stata identificata come OES sotto NIS originale (D.Lgs. 65/2018) **non e' rilevante** per NIS2: la classificazione NIS2 e' indipendente.
- I **gap di governance** (politiche non approvate dal CdA, formazione CdA assente) sono **violazioni dirette** dell'art. 23 e quindi sanzionate ex art. 38 co. 8 lett. a). Spesso sottostimate da soggetti che hanno gia' un ISMS tecnicamente solido ma non hanno formalizzato il livello CdA.
- Il caso evidenzia la **separazione fra art. 23 (governance) e art. 24 (misure)**: sono cumulativi. Avere un buon ISMS non basta se manca la formalizzazione di livello board.

## Punti di attenzione tipici per soggetti essenziali energia

1. **Sistemi ICS/OT (SCADA)**: regimi di patching specifici, segregazione di rete, autenticazione su HMI. La Det. ACN richiede ID.AM-03 (mappa flussi), PR.IR-01 (segmentazione), PR.PS-04 (logging) anche su questi sistemi.
2. **Telecontrollo cabine secondarie**: spesso su rete di comunicazione dedicata (PLC su radio/4G), espone superfici di attacco peculiari.
3. **Vendor management**: i fornitori di SCADA/RTU sono pochi (oligopolio internazionale), questo limita la negoziabilita' delle clausole TPRM. Approccio pragmatico: applicare i requisiti GV.SC con risk acceptance documentata su clausole non ottenibili.
4. **Incident response in scenario blackout**: la procedura di notifica al CSIRT Italia deve interagire con la procedura di emergenza ARERA (CEI 11-37) e con eventuale notifica TERNA. Gestire la sovrapposizione.
5. **ARERA e NIS2**: ARERA puo' chiedere reportistica sull'adeguamento NIS2 nell'ambito del proprio potere di vigilanza sul DSO. Documentare le evidenze in modo riusabile.

## Possibili evoluzioni future del caso

Se ENERGOSPA viene successivamente identificata come **soggetto critico** ex Dir. 2022/2557 / decreto di recepimento italiano:
- Resta essenziale ex NIS2 + acquisisce obblighi aggiuntivi su **resilienza fisica**
- I due regimi sono cumulativi e parzialmente sovrapposti

Se il fatturato cresce oltre 500M EUR:
- Possibile attenzione speciale ACN per individuazione discrezionale ex art. 6 co. 2

## Riferimenti per validazione domain expert

Validatore profilo target: CISO o consulente cybersecurity **con esperienza specifica su utility/energia** + familiarita' con:
- Codice di Rete TERNA
- Linee guida ARERA su sicurezza ICT (es. delibere su misure cyber per gestori reti)
- IEC 62443 (cybersecurity per sistemi di automazione industriale)
- ENISA Energy CSIRT Network reports

Senza questa esperienza, la validazione delle raccomandazioni operative su SCADA/OT e procedure di emergenza puo' essere parziale.
