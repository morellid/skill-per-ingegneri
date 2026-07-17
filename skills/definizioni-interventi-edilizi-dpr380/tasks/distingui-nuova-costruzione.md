# Task: distingui-nuova-costruzione

Verifica se un intervento ricade nella **nuova costruzione** (art. 3 lett. e)
applicando i **sottocasi e.1-e.7**. **Non sceglie** il titolo ne' redige la pratica.

## Input attesi
- Descrizione dell'opera (manufatto, pertinenza, manufatto leggero, infrastruttura,
  deposito, torre/traliccio).
- Per le **pertinenze**: rapporto tra il volume della pertinenza e quello dell'edificio
  principale; eventuale qualificazione degli strumenti urbanistici.
- Per i **manufatti leggeri**: uso (abitazione/lavoro/deposito), stabilita'/
  collegamento al suolo, collocazione in strutture ricettive autorizzate.

## Passi
1. **Premessa** (lett. e): e' nuova costruzione ogni trasformazione edilizia/urbanistica
   **non** riconducibile alle lett. a-d.
2. Verifica i **sottocasi**:
   - **e.1** manufatti fuori terra/interrati o **ampliamento fuori sagoma** (salvo
     pertinenze ex e.6);
   - **e.2** **urbanizzazione** primaria/secondaria da soggetti diversi dal Comune;
   - **e.3** **infrastrutture/impianti** con trasformazione permanente del suolo
     inedificato;
   - **e.4** **torri e tralicci** per radio-ricetrasmissione/telecom;
   - **e.5** **manufatti leggeri** (roulotte, camper, case mobili, imbarcazioni) usati
     stabilmente come abitazioni/lavoro/deposito, **salvo** esigenze temporanee o unita'
     in strutture ricettive all'aperto autorizzate, senza collegamento permanente al
     suolo e con le caratteristiche previste dalle norme regionali;
   - **e.6** **pertinenze** qualificate come nuova costruzione dagli strumenti
     urbanistici **oppure volume > 20%** del volume dell'edificio principale;
   - **e.7** **depositi** di merci/materiali e **impianti produttivi all'aperto** con
     trasformazione permanente del suolo.
3. Se **nessun** sottocaso ricorre e l'opera rientra nelle lett. a-d, **non** e' nuova
   costruzione: rimanda al task `qualifica-intervento`.

## Output
- Esito: nuova costruzione **si'/no**, con il **sottocaso e.x** applicabile (o il motivo
  dell'esclusione), e i criteri (fuori sagoma, soglia 20% per le pertinenze, stabilita'
  del manufatto leggero).
- Nota di rinvio: la nuova costruzione richiede di norma il **permesso di costruire**
  (vedi `permesso-costruire-dpr380`) o la SCIA alternativa; la scelta del titolo e'
  della skill `modulistica-edilizia-unificata`.

## Riferimenti
- `../references/fonti/dpr-380-2001-art-3.md` (art. 3 lett. e, e.1-e.7)
- `../references/estratti/definizioni-interventi-checklist.md` (sez. E)
