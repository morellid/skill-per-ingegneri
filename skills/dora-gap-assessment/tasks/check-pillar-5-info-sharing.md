# Pillar 5 - Gap assessment: Condivisione informazioni e analisi delle minacce (DORA art. 45)

## Obiettivo

Mappare le pratiche dell'entita' finanziaria in materia di partecipazione a meccanismi di condivisione delle informazioni e delle analisi delle minacce informatiche e notifica alle autorita' competenti, rispetto agli obblighi e alle facolta' dell'art. 45 del Regolamento (UE) 2022/2554 (DORA).

## Input richiesti

Chiedere all'utente:

1. **Identificazione dell'entita'**:
   - Categoria DORA (art. 2 par. 1 lettere a-u).
   - Quadro semplificato (art. 16): si' / no. (L'art. 45 e' una **facolta'** non obbligatoria; si applica a tutte le entita' DORA che decidono di partecipare).
2. **Posizione attuale dell'entita'**:
   - L'entita' partecipa attualmente a uno o piu' meccanismi di condivisione delle informazioni (ISAC settoriali finanziari come FI-ISAC EU, Banca d'Italia OF (Operatore Finanziario), CERTFin in Italia, FS-ISAC globale)? Se si', elenco dei meccanismi.
   - L'entita' ha notificato all'autorita' competente la propria partecipazione (art. 45 par. 3)?
   - L'entita' ha cessato la partecipazione a qualche meccanismo dopo notifica iniziale? Se si', e' stata notificata anche la cessazione (art. 45 par. 3)?
3. **Documentazione disponibile**:
   - Policy di information sharing / threat intelligence (interna).
   - Accordo o norme di adesione del meccanismo (memorandum of understanding, ToR del meccanismo).
   - Documentazione del meccanismo sulla conformita' a GDPR (reg. 2016/679) e diritto della concorrenza.
   - Procedura di gestione delle informazioni ricevute (IoC, TTP, indicatori di allerta, configurazioni di strumenti) - integrazione con SOC/SIEM/threat intelligence platform.
   - Procedura di anonimizzazione e classificazione (sensible/non-sensible) prima della condivisione.

## Fonti

- Trascrizione del Regolamento DORA: `references/fonti/reg-ue-2022-2554-dora.md`.
- Estratti curati Pillar 5: `references/estratti/reg-ue-2022-2554-dora.md` sezione "Pillar 5 - Condivisione informazioni".
- In particolare:
  - Art. 45 par. 1: contenuto della condivisione (IoC, TTP, segnali di allarme, strumenti) e condizioni (lettere a-c).
  - Art. 45 par. 2: elementi operativi dei meccanismi.
  - Art. 45 par. 3: notifica all'autorita' competente della partecipazione e della cessazione.

## Procedura

Per ciascuna delle voci di controllo:

1. Confronta le evidenze documentali/operative con l'obbligo o la facolta' DORA.
2. Cita l'articolo e paragrafo esatto.
3. Classifica lo stato: **CONFORME** / **PARZIALE** / **NON CONFORME** / **NON APPLICABILE** (con motivazione).
4. **Importante**: l'art. 45 par. 1 stabilisce una **facolta'** ("possono"), non un obbligo. Se l'entita' decide di **non partecipare** a meccanismi di condivisione, marcare le voci 5.1-5.7 come **NON APPLICABILE - decisione organizzativa di non partecipare ai meccanismi ex art. 45**, e applicare solo le voci di controllo organizzativo (5.8-5.10). Se l'entita' partecipa, l'obbligo di notifica del par. 3 e i requisiti di tutela del par. 1 lettere a-c sono vincolanti.

### Voci di controllo

**Partecipazione e finalita' (art. 45 par. 1)**:
5.1 Se l'entita' partecipa: la finalita' della partecipazione e' potenziare la resilienza operativa digitale (consapevolezza, contenimento delle minacce, capacita' di difesa, individuazione, mitigazione, risposta/ripristino) (par. 1 lettera a)?
5.2 La condivisione avviene entro **comunita' fidate** di entita' finanziarie (par. 1 lettera b)?
5.3 La condivisione avviene tramite meccanismi che tutelano la natura sensibile delle informazioni e sono conformi a:
- norme di condotta sulla riservatezza;
- reg. (UE) 2016/679 (GDPR) per dati personali;
- diritto della concorrenza (par. 1 lettera c)?

**Elementi operativi (art. 45 par. 2)**:
5.4 Il meccanismo cui l'entita' aderisce definisce condizioni di partecipazione, ruolo delle autorita' pubbliche, coinvolgimento di fornitori terzi, elementi operativi (formati, piattaforme tecniche) (par. 2)?

**Notifica all'autorita' competente (art. 45 par. 3)**:
5.5 L'entita' ha **notificato all'autorita' competente la propria partecipazione** ai meccanismi al momento della convalida dell'adesione (par. 3)?
5.6 L'entita' notifica all'autorita' competente la **cessazione** della partecipazione (par. 3)?

**Procedure interne di gestione (deduzioni dal par. 1 lettera c)**:
5.7 Esiste una procedura interna che assicura che le informazioni condivise rispettino GDPR (anonimizzazione di dati personali ove non strettamente necessari, base giuridica del trattamento)?
5.8 Esiste una procedura interna di gestione delle informazioni ricevute (IoC, TTP, indicatori di allerta) e di integrazione nei sistemi di monitoraggio (SOC/SIEM)?
5.9 Esiste una valutazione documentata del beneficio di partecipare/non partecipare a un meccanismo di condivisione, formalizzata e riesaminata periodicamente? (Buona pratica conseguente all'art. 13 par. 1 sulla raccolta di informazioni su vulnerabilita' e minacce).
5.10 Se non si partecipa: e' stato considerato l'art. 13 par. 1 (capacita' di raccogliere informazioni su vulnerabilita' e minacce informatiche) come fonte indipendente per il monitoraggio del rischio?

## Output

Generare un report markdown con la seguente struttura:

```
# Gap Assessment DORA - Pillar 5 (Condivisione informazioni)

## Profilo dell'entita'
- Categoria (art. 2 par. 1): ...
- Decisione di partecipare ai meccanismi ex art. 45: si' / no
- Meccanismi cui partecipa: [es. CERTFin, FI-ISAC EU, FS-ISAC, altro]
- Notifica all'autorita' competente (art. 45 par. 3): si' / no / non applicabile
- Data assessment: 2026-MM-DD
- Documenti analizzati: <elenco>

## Sintesi
| Stato | Numero voci |
| - | - |
| CONFORME | N |
| PARZIALE | N |
| NON CONFORME | N |
| NON APPLICABILE | N |
| Totale | 10 |

## Dettaglio per area

### Partecipazione e finalita' (art. 45 par. 1)
### Elementi operativi del meccanismo (art. 45 par. 2)
### Notifica all'autorita' competente (art. 45 par. 3)
### Procedure interne di gestione (procedure conseguenti)

## Punti che richiedono giudizio del professionista
[Elenco delle voci PARZIALI/NON APPLICABILI, con attenzione a: scelta di partecipare o meno, valutazione di una "comunita' fidata" ex art. 45 par. 1 lettera b, profili GDPR e diritto della concorrenza per la condivisione di informazioni operative.]

## Avvertenza
Il presente report e' uno strumento di supporto. La decisione di partecipare a un meccanismo di condivisione e' una facolta' dell'entita' (art. 45 par. 1: "possono"), non un obbligo. Una volta partecipata, gli obblighi di notifica del par. 3 e i requisiti di tutela del par. 1 lettere a-c (norme di condotta, GDPR, diritto della concorrenza) sono vincolanti. La valutazione di adesione (o non adesione) e' un giudizio del professionista responsabile. Le citazioni di articoli sono ricavate dalla trascrizione fedele del Regolamento (UE) 2022/2554 in `references/fonti/reg-ue-2022-2554-dora.md`.
```

## Limiti

- Il task **non** valuta il merito di adesione a uno specifico meccanismo (es. costi/benefici di entrare in FS-ISAC o CERTFin): l'analisi va condotta dal CISO/management.
- Il task **non** valuta la compliance GDPR del meccanismo: rinvio al DPO/legale.
- Il task **non** rilascia attestazioni: solo mappature.
- L'art. 45 e' una facolta', quindi la "non conformita'" e' rara: piu' spesso si tratta di "PARZIALE" (es. partecipazione informale a una community senza notifica ex par. 3) o "NON APPLICABILE - non si partecipa".
