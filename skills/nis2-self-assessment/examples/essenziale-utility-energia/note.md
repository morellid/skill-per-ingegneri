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

> Le seguenti considerazioni sono **note di esperienza di dominio**, non normative. Le specifiche tecniche e le interazioni con ARERA/TERNA/CEI vanno verificate caso per caso con il consulente cyber specializzato per il settore energia. La skill non cataloga queste fonti tecniche come riferimento primario.

1. **Sistemi ICS/OT (SCADA)**: ipotesi tipiche - patching su finestre di manutenzione, segregazione di rete, autenticazione su HMI. La Det. ACN 379907/2025 richiede per gli essenziali ID.AM-03 (mappa flussi), PR.IR-01 (segmentazione), PR.PS-04 (logging) anche su questi sistemi.
2. **Telecontrollo cabine secondarie**: spesso su reti dedicate (es. PLC su radio/4G), con superfici di attacco peculiari da considerare nei requisiti DE.CM-01/09.
3. **Vendor management**: il mercato dei fornitori SCADA/RTU e' concentrato; questo puo' limitare la negoziabilita' delle clausole TPRM. Approccio pragmatico tipico: applicare i requisiti GV.SC con risk acceptance documentata sulle clausole non ottenibili.
4. **Incident response in scenario blackout**: la procedura di notifica al CSIRT Italia interagisce con eventuali procedure di emergenza settoriali (es. CEI/ARERA/TERNA) e con il regime PSNC quando applicabile. Gestire le sovrapposizioni con l'ufficio compliance/regolatorio.
5. **ARERA e NIS2**: il regolatore di settore ha proprie leve di vigilanza sul DSO; documentare le evidenze in modo riusabile per entrambe le finalita'. **Nota**: la skill non cataloga le delibere ARERA come fonti normative; verificare separatamente con il responsabile regolatorio.

## Possibili evoluzioni future del caso

Se ENERGOSPA viene successivamente identificata come **soggetto critico** ex Dir. 2022/2557 / decreto di recepimento italiano:
- Resta essenziale ex NIS2 + acquisisce obblighi aggiuntivi su **resilienza fisica**
- I due regimi sono cumulativi e parzialmente sovrapposti

Se il fatturato cresce oltre 500M EUR:
- Possibile attenzione speciale ACN per individuazione discrezionale ex art. 6 co. 2

## Riferimenti per validazione domain expert

Validatore profilo target: CISO o consulente cybersecurity con esperienza specifica su utility/energia. La validazione delle raccomandazioni operative su SCADA/OT, procedure di emergenza, integrazione con i regolatori di settore (TERNA, ARERA) e standard tecnici settoriali (IEC 62443, ENISA Energy CSIRT Network) richiede competenze settoriali aggiuntive non incluse in questa skill alpha.
