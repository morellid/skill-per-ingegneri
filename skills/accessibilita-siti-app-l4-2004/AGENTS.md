# AGENTS.md - accessibilita-siti-app-l4-2004

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale agli obblighi di **accessibilita' dei siti web e delle
applicazioni mobili** ai sensi della **Legge Stanca (L. 4/2004)**, testo vigente
(agg. D.Lgs. 106/2018, dir. UE 2016/2102): ambito soggettivo, obblighi negli
appalti e nullita' dei contratti, requisiti tecnici (linee guida AgID), vigilanza
e responsabilita'/sanzioni. Target: PA, RTD, grandi operatori privati, consulenti.

**E' una skill documentale**: non esegue l'audit tecnico WCAG, non redige la
dichiarazione di accessibilita' ne' riproduce le linee guida AgID.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **legge-4-2004**: L. 9/1/2004 n. 4 (Legge Stanca), testo multivigente su
  Normattiva. Binario = pagina indice pinnata `!vig=2026-07-14` (hash stabile
  1cbf3409..., pattern della skill aua-dpr59-dossier). Articoli 2, 3, 4, 7, 9, 11
  letti via AJAX (caricaArticolo) e trascritti verbatim in
  `references/fonti/legge-4-2004.md`.

Estratto operativo: `references/estratti/accessibilita-checklist.md`.

## Punti chiave (verificati sul testo)

- **Ambito** (art. 3): c. 1 soggetti pubblici e assimilati (PA, concessionari di
  servizi pubblici, organismi di diritto pubblico, beneficiari di contributi
  pubblici, ecc.); c. 1-bis **grandi privati** con **fatturato medio triennale >
  500 mln** che offrono servizi al pubblico; c. 2 esclusioni (extranet/intranet
  ante 23/9/2019, ecc.).
- **Obblighi** (art. 4): requisiti di accessibilita' **necessari** negli appalti
  IT (c. 1); **nullita'** dei contratti su siti/app che non li prevedono (c. 2);
  adeguamento grandi privati entro 5/11/2022 (c. 2-bis).
- **Requisiti tecnici** (art. 11): **linee guida AgID** (ex art. 71 CAD) che
  recepiscono EN 301 549 e WCAG; non riprodotte.
- **Vigilanza** (art. 7): **AgID** monitora la conformita' (anche via ISCOM) e
  vigila sulle amministrazioni statali.
- **Responsabilita'** (art. 9): pubblici -> responsabilita' dirigenziale/
  disciplinare (c. 1); grandi privati -> **AgID** sanziona **fino al 5% del
  fatturato** dopo diffida (c. 1-bis); resta la L. 67/2006.

## Convenzioni specifiche

### Cosa NON fare
- Non eseguire l'**audit tecnico WCAG** ne' riprodurre i criteri di successo:
  rinviare alle **linee guida AgID** ed EN 301 549 / WCAG.
- Non redigere la **dichiarazione di accessibilita'** ne' compilare i modelli AgID.
- Non confondere la Legge Stanca con l'**European Accessibility Act** (D.Lgs.
  82/2022): ambiti e soglie diversi.
- Non citare a memoria soglie/sanzioni: citare l'articolo (3, 4, 9, 11).

### Cosa fare
- Distinguere il regime **pubblico** (art. 3 c. 1) da quello dei **grandi privati**
  (art. 3 c. 1-bis): autorita' e sanzioni diverse.
- Evidenziare la **nullita'** dei contratti (art. 4 c. 2) come rischio principale
  per gli appalti.
- Chiudere con il rinvio alle linee guida AgID/WCAG e ai tecnici.

## Aggiornamento della fonte Normattiva

Testo multivigente: se si aggiorna la skill, ri-pinnare la URL a nuova
`!vig=YYYY-MM-DD`, riscaricare la pagina indice (nuovo hash) e rileggere via AJAX
gli articoli modificati (attenzione a eventuali novita' dell'EAA - D.Lgs. 82/2022).

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con esperto di accessibilita'/RTD).

## Stato attuale

- Versione: 0.1.0-alpha (closes #52)
- Task files: 2 (`verifica-obbligo.md`, `checklist-appalto-contratto.md`)
- Esempi: 2 (comune - appalto sito/app; PMI privata sotto soglia)
