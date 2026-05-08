# Valutazione di impatto e clima acustico (L. 447/1995 art. 8)

> Versione: 0.1.0-alpha
> Stato: in sviluppo (Livello 1)

Skill di supporto alla redazione e revisione della **documentazione
previsionale di impatto acustico** (L. 26 ottobre 1995 n. 447 art. 8
c. 2 e c. 4) e della **valutazione previsionale di clima acustico**
(art. 8 c. 3 della stessa legge) da allegare a SCIA, permesso di
costruire (PdC), autorizzazione/licenza per attivita' produttive,
sportive o ricreative, o per insediamenti sensibili.

## Target

- **Tecnico competente in acustica ambientale (TCAA)** iscritto
  all'elenco nazionale ai sensi del D.Lgs. 17 febbraio 2017 n. 42
  art. 21.
- **Ingegnere ambientale / acustico** o progettista incaricato della
  redazione della documentazione.
- **Consulente urbanistico** o consulente del committente.
- **Responsabile del procedimento** comunale (Ufficio Ambiente,
  Edilizia, Attivita' produttive) per la verifica preliminare di
  completezza delle documentazioni depositate.

## Cosa fa

Quattro sotto-attivita' (vedi `tasks/`):

1. **Mappa applicabilita' art. 8 L. 447/1995**
   (`tasks/mappa-applicabilita-art-8.md`): aiuta a identificare
   quale fattispecie si applica al caso (c. 2 impatto, c. 3 clima,
   c. 4 previsione a corredo del titolo abilitativo, c. 6 nulla-osta),
   con riferimenti puntuali al comma e rinvio alla legge regionale.
2. **Check completezza documentazione di impatto acustico**
   (`tasks/check-completezza-impatto-acustico.md`): checklist
   strutturata di sorgenti, classe acustica, valori limite di
   emissione e immissione, criterio differenziale, modalita' di
   misurazione conformi al DM 16/3/1998.
3. **Check completezza valutazione previsionale di clima acustico**
   (`tasks/check-completezza-clima-acustico.md`): checklist per
   insediamento sensibile (scuola, ospedale, casa di cura/riposo,
   parco pubblico, residenza prossima a opere c. 2), con verifica
   rispetto a Tabella C e gestione del regime delle infrastrutture
   dei trasporti.
4. **Checklist contenuti tecnici della relazione previsionale**
   (`tasks/checklist-relazione-previsionale.md`): contenuti tecnici
   minimi (descrittori, strumentazione classe 1, allegato D DM
   16/3/1998).

## Installazione

La skill e' parte del repo `skill-per-ingegneri`. Per dettagli su
distribuzione e symlink in Claude Code / Codex vedi il `README.md`
del repo principale.

## Fonti consultate

Catalogate in `references/sources.yaml`:

- **L. 26 ottobre 1995 n. 447** "Legge quadro sull'inquinamento
  acustico" (PDF MASE).
- **DPCM 14 novembre 1997** "Determinazione dei valori limite delle
  sorgenti sonore" (HTML aggregato GU n. 280 del 1/12/1997).
- **DM Ambiente 16 marzo 1998** "Tecniche di rilevamento e di
  misurazione dell'inquinamento acustico" (HTML aggregato GU n. 76
  del 1/4/1998).
- **L. 447/1995 (Normattiva)** per il testo vigente con coordinamento
  (rinvio per la verifica del testo aggiornato).

Estratti testuali pertinenti in `references/estratti/`.

## Limiti noti

Cosa la skill NON fa:

- Non produce documenti firmati ne' relazioni fonometriche pronte al
  deposito.
- Non esegue calcoli previsionali di Leq, propagazione, attenuazione,
  schermatura.
- Non riproduce in numeri valori specifici dei decreti delle
  infrastrutture dei trasporti (DPR 459/1998 ferroviario, DPR 142/2004
  stradale): solo rinvio strutturale.
- Non sostituisce la **legge regionale** in materia di inquinamento
  acustico (art. 4 c. 1 lett. l) L. 447/1995) ne' il **regolamento
  comunale** (art. 6 c. 2 L. 447/1995).
- Non gestisce il **rumore in ambiente di lavoro** (D.Lgs. 81/2008
  Titolo VIII Capo II).
- Non gestisce la **classificazione acustica comunale** (zonizzazione
  ex art. 6 c. 1 lett. a) L. 447/1995) ne' il **piano di risanamento**
  (art. 7 e art. 15 L. 447/1995).
- Non sostituisce il giudizio del **TCAA firmatario** (D.Lgs. 17
  febbraio 2017 n. 42 art. 21).

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
