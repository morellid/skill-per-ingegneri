# Note di dominio - caso PFTE nuova scuola

## Perche' questo caso

Esempio di **PFTE completo** per nuova costruzione con elementi che attivano vari elaborati condizionali:
- Espropri (lett. t) -> obbligatorio
- Verifica archeologica (lett. c) -> obbligatorio
- BIM applicabile (lett. g, p) -> obbligatorio per le rispettive condizioni
- Appalto integrato (art. 21) -> elaborati aggiuntivi
- Verifica di assoggettabilita' VIA con esito "no VIA" -> lett. d e lett. s **non si attivano** (in screening allegato come integrazione precauzionale, ma non e' SIA)

Non e' un caso "minimo" - e' deliberatamente piu' ricco per consentire alla skill di esercitare il routing condizionale per ciascuna lettera, **incluso** il caso in cui un elaborato precauzionale presente in cartella non corrisponde all'attivazione formale della lettera normativa.

## Cosa la skill deve riconoscere correttamente

1. **Mapping denominazioni reali -> lettere normative**: i progettisti raramente nominano i file "art. 6 co. 7 lett. b". La skill deve riconoscere che "Relazione tecnica generale" + "Relazione geologica" + "Relazione geotecnica" + "Relazione idraulica" + "Relazione strutturale specialistica" + "Relazione impiantistica specialistica" rientrano insieme nella **lett. b** (relazione tecnica con indagini e studi specialistici).

2. **Distinzione VIA / screening / niente**: opera in **verifica di assoggettabilita'** con esito "no VIA" significa che la lett. d (Studio Impatto Ambientale) **non si attiva**: la SIA e' richiesta solo per opere effettivamente soggette a VIA. Lo screening allegato e' un documento integrativo utile ma fuori dal perimetro di lett. d. La skill deve marcare lett. d come **Non-applicabile**, non "presente" - cosi' come deve marcare lett. s (monitoraggio ambientale) come **Non-applicabile** salvo richiesta espressa della SA. La presenza di file di screening o di piano monitoraggio ambientale in cartella non li rende obbligatori a posteriori.

3. **Capitolato informativo (lett. p) richiesto solo se appalto integrato + BIM**: in questo caso entrambe le condizioni sono vere, quindi la lett. p e' obbligatoria. La skill deve verificarne la presenza (file 04.01).

4. **Disciplinare descrittivo e prestazionale (art. 14)**: non e' nelle lettere a-t di art. 6 co. 7 ma e' obbligatorio per **appalto integrato** ai sensi dell'art. 21. La skill deve elencarlo nella sezione "Elaborati per appalto integrato".

5. **Relazione paesaggistica (01.08)**: NON e' un elaborato dell'Allegato I.7. E' obbligatoria solo se applicabile il DPR 31/2017 (vincolo paesaggistico). La skill deve **menzionarla** ma non valutarne l'obbligatorieta' come parte del Codice contratti.

## Punti di attenzione

- L'utente non ha fornito il **quadro esigenziale** ne' il **DIP**. La skill deve procedere ma segnalare che la verifica e' parziale.
- Lo **schema di contratto** non e' chiaramente identificato nell'indice. Casistica frequente in cui il documento c'e' ma e' annidato altrove (in "documenti amministrativi" o nel disciplinare). La skill non deve dichiararlo "assente" ma "da-verificare".

## Aspetti **fuori scope** della skill

- Validazione VIA: la skill non valuta se la verifica di assoggettabilita' e' stata correttamente svolta.
- Adeguatezza dei calcoli geotecnici/strutturali: oggetto del progettista, della verifica ex art. 42, e della validazione del Genio Civile per le strutture.
- Conformita' alla normativa antincendio scuole (DM 26/8/1992 + DM 7/8/2017 RTV scuole): rinvio al progettista antincendio firmatario.
- Conformita' DPR 503/96 e L. 13/89 per accessibilita': rinvio al progettista.
- Verifica del BIM ai sensi della UNI 11337: la skill non legge i modelli IFC.

## Esito atteso dalla validazione di dominio (Livello 2)

Un RUP / ingegnere senior dovrebbe confermare che:
1. Il routing degli elaborati condizionali e' corretto (espropri, BIM, archeologia, appalto integrato).
2. La relazione paesaggistica e' citata correttamente come "fuori Codice contratti ma potenzialmente obbligatoria DPR 31/2017".
3. Il rinvio al verificatore ex art. 42 e' corretto e non viene confuso con il controllo della skill.
