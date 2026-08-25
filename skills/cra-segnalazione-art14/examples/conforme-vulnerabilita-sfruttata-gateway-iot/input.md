# Input: vulnerabilita' attivamente sfruttata in un gateway IoT industriale

## Il fabbricante

- Societa' italiana, produce gateway IoT industriali con firmware proprietario e li
  commercializza con il proprio marchio.
- Circa 120 dipendenti, tutti in Italia. Sede legale a Milano; il team di product security
  e le decisioni sulla cibersicurezza dei prodotti sono a Milano.
- Prodotti venduti in Italia, Germania, Spagna e Polonia.
- Ha una pagina "security" con un indirizzo `security@` presidiato dal PSIRT in orario
  lavorativo, una politica CVD pubblicata e SBOM in formato SPDX generata in build.

## Il prodotto

- Gateway IoT industriale IG-400, appliance hardware con firmware.
- Firmware con interfaccia web di amministrazione, esposta sulla rete locale
  dell'impianto; in alcune installazioni raggiungibile da Internet.

## L'evento

- **Lunedi' 14 settembre 2026, ore 09:20** (CET): un cliente tedesco apre un ticket al
  PSIRT allegando il report del proprio incident responder. Il report documenta accessi
  non autorizzati all'interfaccia web di due gateway IG-400, con log di richieste che
  sfruttano un bypass di autenticazione, un web shell caricato sul dispositivo e traffico
  in uscita verso un IP noto. Il cliente conferma di non aver autorizzato alcun test.
- Il PSIRT riproduce il bypass in laboratorio lo stesso giorno alle 13:00 e conferma che
  la vulnerabilita' e' nel firmware IG-400, versioni da 3.2.0 a 3.4.1.
- Il gateway continua a funzionare normalmente nelle installazioni non compromesse. Sui
  due dispositivi del cliente tedesco il codice caricato dall'attaccante ha eseguito.
- **Mercoledi' 16 settembre 2026, ore 18:00**: viene rilasciata la versione 3.4.2 che
  corregge il bypass, insieme a un workaround (disabilitare l'interfaccia web da WAN).

## Quanto e' noto

- Non e' stato individuato l'attore. Sono disponibili IoC (IP, hash del web shell).
- Il fabbricante stima circa 3.100 dispositivi in campo con firmware vulnerabile.
- Il fabbricante non ha ancora deciso se chiedere un trattamento riservato.

## Domanda all'agent

1. Scatta l'obbligo dell'art. 14? Su quale base, e da quando decorrono i termini?
2. Quali adempimenti sono dovuti, entro quando, e con quale contenuto minimo?
3. A quale CSIRT vanno indirizzate le notifiche?
4. Che cosa e' dovuto verso gli utilizzatori?
