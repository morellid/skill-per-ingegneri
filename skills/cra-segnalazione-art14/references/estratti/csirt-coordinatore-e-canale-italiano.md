# Estratto: chi e' il CSIRT coordinatore per un fabbricante stabilito in Italia

Fonti: `../fonti/dlgs-138-2024-csirt-italia.md` (D.Lgs. 4 settembre 2024, n. 138, GU
Serie generale n. 230 del 1/10/2024, cod. red. 24G00155),
`../fonti/dir-ue-2022-2555-nis2-segnalazione.md` (art. 12, par. 1, Dir. (UE) 2022/2555),
`../fonti/reg-ue-2024-2847-cra-segnalazione.md` (art. 14, par. 7, CRA).
Accessed 2026-08-25.

## A. La catena di rinvii

L'art. 14, par. 7, del CRA impone di trasmettere la notifica "utilizzando il terminale
per la notifica elettronica del **CSIRT designato come coordinatore** dello Stato membro
in cui i fabbricanti hanno lo stabilimento principale nell'Unione". Il Regolamento **non
nomina** il CSIRT di alcuno Stato membro: la figura del "CSIRT designato come
coordinatore" nasce dall'art. 12, par. 1, della direttiva (UE) 2022/2555, secondo cui
"ogni Stato membro designa uno dei propri CSIRT come coordinatore ai fini della
divulgazione coordinata delle vulnerabilita'".

Per l'Italia la designazione e' nel decreto di recepimento:

- **D.Lgs. 138/2024, art. 16, comma 1**: "Il **CSIRT Italia e' designato coordinatore**
  ai fini della divulgazione coordinata delle vulnerabilita' ai sensi dell'articolo 12
  della direttiva (UE) 2022/2555 e agisce da intermediario di fiducia agevolando, se
  necessario, l'interazione tra la persona fisica o giuridica che segnala la
  vulnerabilita' e il fabbricante o fornitore di servizi TIC o prodotti TIC
  potenzialmente vulnerabili, su richiesta di una delle parti."
- **D.Lgs. 138/2024, art. 2, comma 1, lett. i)**: il CSIRT Italia e' "il Gruppo nazionale
  di risposta agli incidenti di sicurezza informatica ai sensi dell'articolo 15, comma 1,
  **operante all'interno dell'Agenzia per la cybersicurezza nazionale**".

Quindi: fabbricante con stabilimento principale in Italia -> CSIRT coordinatore = **CSIRT
Italia, presso ACN**.

## B. Cosa fa il CSIRT Italia in veste di coordinatore

Art. 16, comma 2, del D.Lgs. 138/2024 - i compiti comprendono:

- lett. a) l'individuazione e il contatto dei soggetti interessati;
- lett. b) l'assistenza alle persone fisiche o giuridiche che segnalano una
  vulnerabilita';
- lett. c) la negoziazione dei tempi di divulgazione e la gestione delle vulnerabilita'
  che interessano piu' soggetti.

Art. 16, comma 3: chi segnala puo' chiedere di farlo **in forma anonima**; il CSIRT
Italia assicura l'anonimato del segnalante e, se la vulnerabilita' e' suscettibile di
avere impatto significativo in piu' di uno Stato membro, coopera con gli altri CSIRT
coordinatori nella Rete di CSIRT nazionali.

Art. 16, comma 4: l'Autorita' nazionale competente NIS adotta una **politica nazionale di
divulgazione coordinata delle vulnerabilita'**; ACN implementa i mezzi tecnici per
agevolarne l'attuazione.

## C. Limiti da non superare: quello che queste fonti NON dicono

Questa e' la parte piu' importante dell'estratto, perche' e' dove si annidano le
affermazioni fabbricabili.

1. **Il D.Lgs. 138/2024 non disciplina l'art. 14 del CRA.** E' il recepimento della NIS2,
   adottato nel settembre 2024. La sua utilita' qui e' esattamente una: stabilire **chi**
   e' il CSIRT coordinatore italiano ai fini dell'art. 12 NIS2, cui l'art. 14, par. 7,
   del CRA rinvia. Di quel decreto sono trascritti i soli artt. 2, 15 e 16: **le
   disposizioni che ne definiscono l'ambito soggettivo e gli obblighi di notifica non
   sono state lette**, e questa skill non afferma quindi ne' chi vi sia sottoposto ne'
   che un fabbricante di PDE vi rientri o ne sia escluso.
2. **Un obbligo NIS2 e un obbligo CRA non si assorbono a vicenda.** Se il fabbricante e'
   sottoposto anche al regime di notifica del D.Lgs. 138/2024, i due regimi hanno
   presupposti, termini e destinatari propri. Nessuna delle fonti lette prevede che
   l'adempimento dell'uno esoneri dall'altro. La skill non deve suggerire il contrario,
   e deve rinviare al consulente la verifica dell'applicabilita' del decreto al caso.
3. **Nessuna delle fonti lette descrive il terminale italiano per la notifica
   elettronica** previsto dall'art. 16, par. 1, del CRA: non c'e' testo su URL, modalita'
   di accreditamento, credenziali, tempistiche di attivazione. La procedura operativa di
   accesso va verificata sui canali ufficiali ACN/CSIRT Italia ed ENISA al momento
   dell'uso.
4. **La politica nazionale CVD dell'art. 16, comma 4, del D.Lgs. 138/2024 non e' stata
   letta.** Non e' contenuta in questo decreto: e' un atto successivo dell'Autorita'
   nazionale competente NIS. La skill non ne cita alcun contenuto.
5. **Il D.L. 82/2021 (istitutivo di ACN), conv. L. 109/2021, e' citato ma non letto.**
   L'art. 15, comma 1, del D.Lgs. 138/2024 lo richiama ("fermo restando quanto previsto
   dal decreto-legge 14 giugno 2021, n. 82"). La skill non ne afferma alcun contenuto.
