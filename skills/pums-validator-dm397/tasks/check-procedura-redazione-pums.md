# Task: Verifica procedura di redazione del PUMS (8 passi - Allegato 1 DM 397/2017)

## Obiettivo

Controllare che il PUMS abbia seguito la procedura uniforme di redazione articolata nei passi procedurali previsti dall'Allegato 1 al DM 397/2017 (come modificato dal DM 396/2019).

## Input richiesti

Chiedere all'utente:
1. Documento del PUMS (o sezioni rilevanti) e atto di adozione (delibera Giunta/Sindaco).
2. Documentazione del processo partecipato (verbali, esiti, eventuale piano di comunicazione).
3. Rapporto preliminare al quadro conoscitivo (se presente).
4. Esito della VAS (parere motivato o esclusione assoggettabilita').
5. Eventuali atti di approvazione del Consiglio comunale/metropolitano.

## Fonti

- references/estratti/dm-4-8-2017-397-pums.md (sezione "Procedura uniforme - 8 passi (Allegato 1)").
- references/estratti/vademecum-pums-mit-2022.md (Cap. 3 "Indirizzi operativi per la redazione del PUMS", in particolare 3.1-3.5).
- references/fonti/dm-4-8-2017-397-pums.md (Allegato 1, fasi a-h con dettaglio).

## Procedura

Verificare la presenza e la documentazione di ciascun passo procedurale. Per ognuno ESITO {CONFORME / NON CONFORME / NON DETERMINABILE}.

1. **Fase a - Definizione del gruppo interdisciplinare/interistituzionale di lavoro**:
   - Composizione (interni ed esterni all'amministrazione).
   - Presenza del Mobility Manager d'area (DM Transizione Ecologica 12/05/2021).
   - Coinvolgimento di comuni contermini / conurbazioni (se applicabile).

2. **Fase b - Predisposizione del quadro conoscitivo**:
   - Quadro normativo, pianificatorio e programmatico (regionale, sovralocale, locale).
   - Inquadramento territoriale e socio-economico dell'area di Piano.
   - Offerta di reti e servizi di trasporto.
   - Domanda di mobilita' (matrici O/D persone e merci, fasce orarie, picchi stagionali).
   - Interazione domanda-offerta.
   - Criticita' e impatti.
   - Punti di forza/debolezza, opportunita'/minacce (SWOT).

   (Sotto-controllo articolato nella check `check-obiettivi-pums.md` per coerenza tra criticita' e obiettivi.)

3. **Fase c - Avvio del percorso partecipato** (vedi anche Vademecum 3.3):
   - Definizione ex-ante delle modalita' di coinvolgimento (non soggette a negoziazione).
   - Avvio in concomitanza con il quadro conoscitivo (Allegato 1, par. c) e prosecuzione lungo la definizione degli obiettivi, la costruzione partecipata dello scenario e il monitoraggio.
   - Documentazione (verbali, sintesi, restituzione, controdeduzioni).

4. **Fase d - Definizione degli obiettivi**:
   - 17 macro-obiettivi minimi obbligatori (verifica dettagliata in `check-obiettivi-pums.md`).
   - Eventuali macro-obiettivi aggiuntivi e obiettivi specifici (facoltativi).
   - Indicatori di risultato e target (vedi `check-indicatori-tabella1.md`).

5. **Fase e - Costruzione partecipata dello scenario di Piano**:
   - Scenario di riferimento (SR) che si verifica per la naturale evoluzione del sistema e per effetto di altri piani sovraordinati.
   - Scenari alternativi: azioni, interventi, cronoprogramma 2/3-5-10 anni, Piano Economico e Finanziario, coperture finanziarie, stima indicatori.
   - Valutazione comparata ex-ante degli scenari alternativi rispetto allo SR (uso degli indicatori di raggiungimento dei macro-obiettivi).
   - Riferimento alle Linee guida MIT 2017 per la valutazione degli investimenti (raccomandato).
   - Scelta motivata dello Scenario di Piano (SP), con elenco interventi prioritari ed eventuali lotti funzionali (Allegato 1, par. e).

6. **Fase f - Valutazione ambientale strategica (VAS)**:
   - Presenza del parere di VAS o atto di esclusione di assoggettabilita' (a seconda di quanto previsto dalla normativa regionale).
   - Coerenza tra il PUMS adottato e le prescrizioni della VAS.

7. **Fase g - Adozione del piano e successiva approvazione**:
   - Adozione da parte della Giunta (comune) o equivalente metropolitano.
   - Pubblicazione per almeno 30 giorni per osservazioni (raccomandata da Linee guida italiane).
   - Risposta con controdeduzioni alle osservazioni nel testo finale.
   - Approvazione da parte del Consiglio comunale o metropolitano.

8. **Fase h - Monitoraggio** (verifica dettagliata in `check-monitoraggio-aggiornamento.md`):
   - Presenza del piano di monitoraggio nel documento.
   - Cadenza biennale dichiarata.
   - Indicatori e target tracciati (con valore al tempo "0").

## Output

Report con:
- Tabella esiti per ciascuna fase a-h.
- Rilievi BLOCCANTI (es. assenza di una fase, mancata adozione formale, assenza di processo partecipato).
- Rilievi NON BLOCCANTI (es. processo partecipato presente ma poco documentato).
- Rinvio al professionista per il giudizio sulle fasi normate da norme regionali (es. VAS).

## Limiti

- Non valuta nel merito la qualita' tecnica dello scenario o degli interventi proposti.
- Non sostituisce la valutazione del Tavolo Tecnico PUMS, che ha competenze specifiche di assessment qualitativo (cfr. Vademecum p.4).
- La fase VAS dipende dalla normativa regionale, non interpretata da questa skill.
