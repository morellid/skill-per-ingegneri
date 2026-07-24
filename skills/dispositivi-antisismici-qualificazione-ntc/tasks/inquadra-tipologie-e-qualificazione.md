# Task — Inquadra tipologie e qualificazione dei dispositivi antisismici (NTC 2018 §11.9-11.9.2)

Supporto documentale per individuare la **tipologia** di un dispositivo antisismico, inquadrarne i **requisiti
generali** (vita di servizio, temperatura, UNI EN 15129) e il **percorso di qualificazione** (§11.9.2) secondo le
NTC 2018 (DM 17/1/2018). **Non** esegue il progetto né dimensiona i dispositivi.

Fonte: `../references/fonti/ntc2018-par-11-9.md`; checklist: `../references/estratti/dispositivi-antisismici-checklist.md`.

## Input tipico

- Tipo di dispositivo previsto in progetto: **isolatore** (elastomerico / a scorrimento), **dissipatore** (lineare /
  non lineare / viscoso), **dispositivo di vincolo** (a fusibile / provvisorio).
- Documentazione del fabbricante (dichiarazione di prestazione, Marcatura CE, certificato/CVT).

## Passi

1. **Requisiti generali (§11.9)**
   - Verifica la **vita di servizio > 10 anni** nel campo di temperatura di riferimento delle specifiche tecniche
     del dispositivo; **in assenza di indicazioni** il campo deve essere **almeno −15 °C ÷ +45 °C** (campi diversi
     per opere particolari o dispositivi in luoghi protetti).
   - Verifica la previsione di **piani di manutenzione e sostituzione** allo scadere della vita di servizio.
   - Se si applica **UNI EN 15129**, ricorda che **dbd** = spostamento allo **SLV** e **γx·dbd** = spostamento allo
     **SLC** (grandezze da desumere dalle NTC).

2. **Tipologia (§11.9.1)**
   - Classifica il dispositivo: **vincolo temporaneo** (a fusibile / dinamico provvisorio); **dipendente dallo
     spostamento** (lineare / non lineare); **viscoso**; **isolatore** (elastomerico / a scorrimento); combinazione.

3. **Procedura di qualificazione (§11.9.2)**
   - Se il dispositivo ricade nel **punto A del §11.1** → deve essere **conforme a UNI EN 15129** e recare la
     **Marcatura CE**, con sistema di **valutazione e verifica della costanza della prestazione (VVCP) per
     applicazioni critiche**.
   - Se **non ricade (o non completamente)** nel campo della UNI EN 15129 → si applica il **caso C del §11.1**
     (Certificazione di valutazione tecnica del Servizio Tecnico Centrale).
   - In ogni caso ogni fornitura deve essere accompagnata dal **manuale** con le specifiche tecniche di posa in opera
     e manutenzione.

4. **Output**: scheda con tipologia del dispositivo, requisiti generali (vita di servizio, campo di temperatura) e
   percorso di qualificazione (UNI EN 15129 + CE vs caso C), con rinvio ai sotto-paragrafi. Segnala che il
   **progetto/dimensionamento** (§7.10) resta fuori scope.

## Cosa NON fare

- Non **progettare** il sistema di isolamento/dissipazione né **dimensionare** i dispositivi (§7.10, → skill
  `isolamento-sismico-ntc`).
- Non impostare le **prove di accettazione** (numerosità, Tab. 11.9.I-IV): sono nel task
  `imposta-accettazione-e-prove-per-tipo`.
- Non inventare valori: ogni riferimento deve essere rintracciabile in `../references/fonti/ntc2018-par-11-9.md`.
