# Fascicolo tecnico macchine - Reg. (UE) 2023/1230

> Versione: 0.1.0-alpha
> Stato: in sviluppo

Skill di supporto alla redazione e alla verifica del **fascicolo tecnico** (documentazione tecnica) di macchine, prodotti correlati e quasi-macchine ai sensi del **Regolamento (UE) 2023/1230** del 14 giugno 2023, applicabile dal **14 gennaio 2027** in sostituzione della direttiva 2006/42/CE.

## Target

- Fabbricanti italiani ed europei (ufficio tecnico, responsabile prodotto, qualita').
- Professionisti incaricati di assistere il fabbricante (ingegneri meccanici, elettrici, dell'automazione, della sicurezza).
- Consulenti CE / Notified Body liaison.
- Studenti e neolaureati in ingegneria che devono comprendere la struttura del fascicolo CE secondo il nuovo Regolamento Macchine.

## Cosa fa

La skill organizza in cinque sotto-attivita' (file in `tasks/`) i passi tipici di costruzione/verifica del fascicolo tecnico:

1. **Qualifica del prodotto** (`tasks/qualifica-prodotto.md`): macchina, prodotto correlato, quasi-macchina, esclusione, modifica sostanziale, ruolo dell'operatore.
2. **Identificazione della procedura di valutazione della conformita'** (`tasks/identifica-procedura-conformita.md`): collocazione in All. I parte A o B, scelta tra Modulo A, B+C, G, H; coinvolgimento dell'organismo notificato; conseguenze sulla marcatura CE.
3. **Struttura del fascicolo tecnico** (`tasks/struttura-fascicolo-tecnico.md`): indice dei contenuti All. IV parte A (macchine) o parte B (quasi-macchine).
4. **Audit di completezza del fascicolo** (`tasks/check-completezza-fascicolo.md`): verifica puntuale di tutte le voci di All. IV + All. V + marcatura CE + identificazione + istruzioni + conservazione.
5. **Struttura della dichiarazione UE** (`tasks/struttura-dichiarazione-ue.md`): dichiarazione di conformita' (All. V parte A) o di incorporazione (All. V parte B).

Per il dettaglio tecnico vedi `SKILL.md`.

## Installazione

La skill e' parte del repo `skill-per-ingegneri`. Per usarla:

- **Claude Code**: simlinkare `skills/fascicolo-tecnico-macchine-reg-1230` in `~/.claude/skills/`.
- **OpenAI Codex**: simlinkare in `~/.agents/skills/` (legge `agents/openai.yaml`).

Vedi il `README.md` del repo per le istruzioni complete di installazione.

## Fonti consultate

- **Regolamento (UE) 2023/1230** del Parlamento europeo e del Consiglio del 14 giugno 2023 - testo italiano integrale (102 pagine, GU UE L 165 del 29 giugno 2023). Dettaglio in `references/sources.yaml`, trascrizione fedele dei paragrafi citati in `references/fonti/reg-ue-2023-1230-macchine.md`, estratto operativo in `references/estratti/reg-ue-2023-1230-fascicolo-tecnico.md`.

Norme armonizzate UNI/CEN (es. UNI EN ISO 12100, UNI EN ISO 13849-1, UNI EN 60204-1, UNI EN 12622) sono tecniche **proprietary-paid** e NON sono incluse nelle fonti: la skill ne usa solo rinvii strutturali (numero norma, ambito).

## Limiti noti

La skill **non**:

- produce documenti pronti al deposito o auto-firmati;
- riproduce ne' interpreta il testo integrale dell'Allegato III (RES);
- valida l'applicabilita' di specifiche norme armonizzate al progetto;
- determina parametri di sicurezza di dettaglio (PL, SIL, categoria sistema di comando di sicurezza);
- copre il regime transitorio della direttiva 2006/42/CE per prodotti immessi sul mercato prima del 14/01/2027 (art. 52 del Reg. 2023/1230);
- gestisce la procedura di notifica dell'organismo notificato (art. 26-42, fuori scope);
- sostituisce la consulenza legale per aspetti contrattuali (mandato, subfornitura, responsabilita' verso terzi).

La firma, la marcatura CE e la conservazione decennale del fascicolo restano obbligo esclusivo del fabbricante (o del mandatario nei limiti del mandato).

## Note fuori scope per v0.1

- Esempi aggiuntivi per le 6 categorie di Allegato I parte A (in particolare apprendimento automatico per funzioni di sicurezza).
- Template editabili Word/Excel per il fascicolo (la skill produce indici e checklist testuali, non file binari).
- Workflow di integrazione con un database di norme armonizzate aggiornato in tempo reale.
- Confronto strutturato con il regime previgente 2006/42/CE per il regime transitorio (rinvio ad altra skill dedicata, da creare).

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
