---
name: dvr-generico
description: Supporta la stesura, verifica e aggiornamento del Documento di Valutazione dei Rischi (DVR) per qualsiasi azienda italiana, ai sensi degli art. 17, 28 e 29 del D.Lgs. 81/2008. Use when an Italian datore di lavoro, RSPP, HSE manager, or consultant needs to draft a DVR for a new business, verify completeness of an existing DVR, decide whether a DVR update is required, or map risks for specific job profiles. Skill cross-settoriale, applicabile a uffici, manifattura, servizi, sanita', commercio, ecc.
license: MIT
---

# DVR Generico (D.Lgs. 81/2008 art. 17, 28, 29)

## Quando usare questa skill

Usare quando un **datore di lavoro**, **RSPP** (interno/esterno), **HSE manager** o **consulente sicurezza** chiede di:
- Redigere il DVR per una nuova attivita'
- Verificare la completezza di un DVR esistente
- Valutare se serve aggiornare un DVR (modifiche, infortuni, riorganizzazione)
- Mappare i rischi attesi per una specifica mansione/luogo di lavoro

Skill **cross-settoriale**: applicabile a uffici, manifattura, servizi, sanita', commercio, ristorazione, ecc. Ogni settore aggiunge specificita' (Titoli specifici D.Lgs. 81), ma il framework di valutazione e' comune.

**Non usare** quando l'utente chiede:
- POS (Piano Operativo Sicurezza per cantieri) - usa skill `pos-allegato-xv-checker`
- DUVRI (art. 26 - interferenze appalti) - skill futura dedicata
- Valutazioni specialistiche (es. dimensionamento misure rumore) - rinvio a tecnico abilitato
- Pareri legali su responsabilita' del datore di lavoro

## Avvertenza

Questa skill e' uno strumento di supporto alla redazione/verifica del DVR. **Non sostituisce il giudizio del RSPP, del medico competente o del datore di lavoro firmatario.** Il DVR e' atto di **competenza non delegabile** del datore di lavoro (art. 17 co. 1 lett. a). Sanzioni penali per assenza/incompletezza DVR:
- **Arresto da 3 a 6 mesi o ammenda da 2.949,03 a 7.532,82 euro** per omessa redazione
- **Ammenda da 2.847,69 a 5.695,36 euro** se DVR redatto senza elementi art. 28 co. 2 lett. b/c/d
- **Ammenda da 1.423,83 a 2.847,69 euro** per assenza elementi art. 28 co. 2 lett. a (primo periodo) ed f
*(Importi rivalutati periodicamente.)*

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il task file appropriato:

- **Stesura DVR**: l'utente chiede "redigi il DVR", "compila il DVR" -> leggi [`tasks/draft-dvr.md`](tasks/draft-dvr.md)
- **Verifica DVR esistente**: l'utente chiede "controlla questo DVR", "e' completo?" -> leggi [`tasks/check-dvr.md`](tasks/check-dvr.md)
- **Aggiornamento DVR**: l'utente chiede "serve aggiornare il DVR?", "abbiamo cambiato X" -> leggi [`tasks/valuta-aggiornamento.md`](tasks/valuta-aggiornamento.md)
- **Mappatura rischi mansione**: l'utente chiede "che rischi ha il ruolo X?" -> leggi [`tasks/mappa-rischi-mansione.md`](tasks/mappa-rischi-mansione.md)

Se richiesta generica ("aiutami con il DVR"), parti da `mappa-rischi-mansione.md` per identificare la natura dei rischi, poi indirizza alla stesura/verifica.

## Processo generale

1. Identifica la sotto-attivita' richiesta.
2. Carica il task file specifico.
3. Acquisisci dall'utente:
   - Tipologia dell'attivita' (codice ATECO o descrizione)
   - Numero e qualifica dei lavoratori
   - Luoghi di lavoro
   - Attrezzature, sostanze, processi
4. Applica la procedura del task.
5. Produci output strutturato.
6. Concludi con rinvio al RSPP/medico competente/datore di lavoro.

## Strategie semplificate per piccole imprese

- **Fino a 10 lavoratori** (art. 29 co. 5): possibile uso delle **procedure standardizzate** del Coordinamento Tecnico Regioni
- **Fino a 50 lavoratori** (art. 29 co. 6): possibile uso delle procedure standardizzate (salvo settori esclusi)
- **OIRA** (Online Interactive Risk Assessment) e' lo strumento europeo per micro/PMI - INAIL ne ha versione italiana per molti settori

La skill puo' supportare sia approccio "DVR completo" sia approccio "procedure standardizzate" sia OIRA.

## Sinergia con altre skill

- **POS** (cantieri): se l'azienda lavora in cantieri temporanei, anche `pos-allegato-xv-checker`. Il POS NON sostituisce il DVR ma lo integra per il singolo cantiere.
- **GDPR**: se il DVR include sorveglianza sanitaria, dati biometrici per accessi, videosorveglianza -> attivare `gdpr-registro-dpia` per il trattamento corrispondente
- **AI Act**: se l'azienda usa sistemi AI per gestione lavoratori (HR scoring, video monitoring) -> attivare `ai-act-compliance` (potenzialmente high-risk Allegato III par. 4)

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- D.Lgs. 9 aprile 2008 n. 81 (testo coordinato INL gennaio 2025)
  - Art. 17: obblighi non delegabili del datore di lavoro
  - Art. 28: oggetto della valutazione dei rischi (contenuti minimi DVR)
  - Art. 29: modalita' di effettuazione della valutazione
  - Titoli specifici per rischi specialistici (rumore, vibrazioni, chimico, etc.)
- INAIL: strumenti di settore (OIRA), linee guida specifiche
- Coordinamento Tecnico Regioni: procedure standardizzate

Estratti testuali in [`references/estratti/`](references/estratti/).

## Limiti

Questa skill NON fa:
- Non sostituisce il RSPP, il medico competente, o il datore di lavoro firmatario
- Non quantifica numericamente l'esposizione (es. dB, soglie chimiche) - serve tecnico abilitato
- Non valuta i rischi in cantieri temporanei (POS skill dedicata)
- Non sostituisce la sorveglianza sanitaria del medico competente
- Non e' aggiornata in tempo reale a modifiche normative continue

**Ogni DVR prodotto richiede revisione del RSPP, validazione del datore di lavoro, e consultazione obbligatoria del RLS (art. 29 co. 2). Coinvolgimento del medico competente nei casi di art. 41.**
