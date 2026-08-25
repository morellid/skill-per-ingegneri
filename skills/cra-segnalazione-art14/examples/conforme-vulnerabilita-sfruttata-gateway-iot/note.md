# Note al caso conforme

## Perche' questo caso e' "conforme"

Il caso mostra il percorso lineare dalla qualificazione alla timeline quando gli elementi
ci sono tutti: prove documentate di sfruttamento, assenza di autorizzazione, momento
iniziale tracciabile, rimedio rilasciato con data certa, stabilimento principale non
ambiguo.

## Le quattro cose che l'agent deve fare bene qui

1. **Riconoscere che gli obblighi sono due, non uno.** Lo stesso evento integra sia la
   vulnerabilita' attivamente sfruttata (par. 1-2) sia l'incidente grave (par. 3-5).
   Sono catene parallele con relazioni finali diverse: 14 giorni dal rimedio contro un
   mese dalla trasmissione della notifica. Un output che ne presenta una sola e'
   incompleto anche se le date che riporta sono giuste.
2. **Fissare il momento iniziale sull'arrivo del ticket, non sulla riproduzione in
   laboratorio.** E' la scelta che sposta tutte le scadenze di quasi quattro ore. La
   riproduzione conferma, non fonda la conoscenza.
3. **Non confondere le due decorrenze delle relazioni finali.** Quella sulla
   vulnerabilita' decorre dalla **messa a disposizione del rimedio** (16/09 ore 18:00 ->
   30/09), quella sull'incidente dalla **trasmissione effettiva** della notifica delle 72
   ore. E' "un mese", non "30 giorni".
4. **Separare dovuto e condizionato.** Il preallarme delle 24 ore sulla vulnerabilita' non
   richiede altro che, "se del caso", gli Stati membri: un agent che pretende una
   descrizione tecnica completa entro 24 ore aggiunge requisiti che il testo non pone e
   spinge il fabbricante a sforare il termine.

## Punti di attenzione che l'agent deve sollevare anche in un caso conforme

- **Il canale potrebbe non essere praticabile.** L'art. 16 non e' fra le disposizioni
  anticipate dall'art. 71, par. 2. La verifica su ACN/CSIRT Italia ed ENISA va fatta
  prima della scadenza delle 24 ore, non dopo, e le fonti normative non contengono URL ne'
  procedure di accreditamento.
- **Il grado di sensibilita' va deciso prima dell'invio della notifica delle 72 ore**,
  perche' e' il presupposto del ritardo eccezionale nella diffusione (art. 16, par. 2). La
  decisione di ritardare e' pero' del CSIRT, e non proroga i termini dell'art. 14.
- **L'informazione agli utilizzatori (par. 8) e' autonoma**, riguarda l'intero parco
  vulnerabile e non solo i due clienti compromessi, e non attende l'esito della notifica.
- **L'attore non e' identificato**: la relazione finale riporta gli IoC e dichiara che
  l'attribuzione non e' stata possibile. Il punto (ii) del par. 2, lett. c), e' preceduto
  da "se disponibili".

## Cosa l'agent non deve fare nemmeno nel caso conforme

- Non dichiarare "conforme" o "adempiuto": la skill inquadra l'obbligo, non certifica
  l'adempimento, e nessuna notifica e' stata trasmessa.
- Non redigere il testo pronto all'invio delle notifiche: struttura il contenuto minimo.
- Non ipotizzare l'attribuzione dell'attacco sulla base degli IoC.
- Non affermare che la SBOM o la politica CVD del fabbricante siano adeguate: la loro
  presenza e' un prerequisito pratico, non oggetto di valutazione in questo task.
- Non citare un formato di notifica: l'atto di esecuzione dell'art. 14, par. 10, e' una
  facolta' della Commissione, e questa skill non ha verificato ne' letto eventuali atti
  adottati in base a quel paragrafo.
