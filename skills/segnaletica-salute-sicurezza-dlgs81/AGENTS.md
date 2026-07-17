# AGENTS.md - segnaletica-salute-sicurezza-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **tecnico** (datore di lavoro, RSPP, coordinatore sicurezza) per la
**segnaletica di salute e sicurezza sul luogo di lavoro**: campo di applicazione, definizioni
(cartelli, colori, segnali luminosi/acustici, comunicazioni verbali, segnali gestuali), obblighi del
datore di lavoro, informazione e formazione, sanzioni, ai sensi del **D.Lgs. 9 aprile 2008, n. 81,
Titolo V (artt. 161-165)**. Target: RSPP, datori di lavoro, ingegneri/tecnici della sicurezza.

**E' una skill documentale per il tecnico**: inquadra la disciplina e gli obblighi; **non progetta**
il piano di segnaletica, **non redige** il DVR, non sostituisce il datore di lavoro, l'RSPP ne' il
CSE.

## Nota sull'area e sulla complementarita'

Area **sicurezza-lavoro-cantieri**. Complementare a `obblighi-datore-preposto-formazione-dlgs81`
(obblighi generali e formazione), a `dpi-protezione-individuale-dlgs81` (DPI) e alle skill sui rischi
specifici. La segnaletica **stradale** di cantiere (Codice della Strada / DM 10/7/2002) e' fuori
perimetro (skill `cantieri-stradali-occupazione-cds`). Questa copre la **segnaletica di sicurezza**
del Titolo V.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-segnaletica-161-165**: D.Lgs. 81/2008, pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `18fbc542...`; codice 008G0104 - stesso indice delle altre skill D.Lgs.
  81). Artt. 161-165 (idGruppo 28-29) caricati via `caricaArticolo` (formato AKN) e trascritti
  verbatim.

Trascrizione in `references/fonti/dlgs-81-2008-segnaletica-161-165.md`; estratto operativo in
`references/estratti/segnaletica-checklist.md`.

## Punti chiave (verificati sul testo)

- **Campo** (art. 161): segnaletica di sicurezza/salute; **esclusa** quella del **traffico** (salvo
  regolamento per attivita' con traffico veicolare, c. 2-bis).
- **Definizioni** (art. 162): segnali di divieto/avvertimento/prescrizione/salvataggio/informazione;
  mezzi: cartello, colore, simbolo/pittogramma, luminoso, acustico, verbale, gestuale.
- **Obbligo residuale** (art. 163): segnaletica quando i rischi non sono evitabili/limitabili con
  protezione collettiva, conformemente agli **allegati XXIV-XXXII**; situazioni non previste (buona
  tecnica); traffico interno (segnaletica stradale, salvo all. XXVIII).
- **Informazione/formazione** (art. 164): RLS/lavoratori informati; formazione sul significato,
  specie con **gesti/parole**.
- **Sanzioni** (art. 165) a datore/dirigente: art. 163 -> arresto 3-6 mesi o ammenda 2.500-6.400
  euro; art. 164 -> arresto 2-4 mesi o ammenda 750-4.000 euro; cumulo per gli allegati (c. 2).
- **Art. 166**: abrogato (D.Lgs. 106/2009).

## Convenzioni specifiche

### Cosa NON fare
- Non **progettare** il piano di segnaletica ne' scegliere in concreto cartelli/colori/segnali.
- Non **redigere** il **DVR** (art. 28).
- Non riprodurre gli **allegati XXIV-XXXII** (requisiti specifici) ne' trattare la segnaletica
  **stradale** di cantiere (CdS/DM 10/7/2002): rinvio.

### Cosa fare
- Stabilire quando la segnaletica e' dovuta (obbligo residuale), quali tipi/mezzi usare, gli obblighi
  di informazione/formazione (specie gesti/parole) e le sanzioni, sui commi degli artt. 161-165.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 81/2008 pinnato a nuovo `!vig=` (nuovo hash) e rileggere
gli artt. 161-165, verificando le modifiche segnalate dai doppi tondi `(( ))` (es. D.Lgs. 106/2009) e
l'aggiornamento degli allegati XXIV-XXXII.

## Validatori

- Non ancora assegnato (Livello 2 con RSPP / coordinatore per la sicurezza).

## Stato attuale

- Versione: 0.1.0-alpha (closes #348)
- Task files: 2 (`inquadra-obbligo-segnaletica.md`, `inquadra-informazione-formazione-sanzioni.md`)
- Esempi: 2 (carrelli elevatori in magazzino: obbligo residuale e tipi di segnale, traffico interno;
  segnali gestuali per manovre di gru: formazione obbligatoria e sanzioni)
