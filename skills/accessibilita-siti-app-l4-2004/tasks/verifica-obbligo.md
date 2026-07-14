# Task: verifica-obbligo

Determina se un soggetto e' obbligato agli adempimenti di accessibilita' della
Legge Stanca (L. 4/2004) e quale regime di responsabilita'/sanzioni si applica.

## Input richiesto

- Natura del soggetto (PA, ente pubblico economico, concessionario di servizi
  pubblici, organismo di diritto pubblico, azienda a partecipazione pubblica,
  beneficiario di contributi pubblici; oppure soggetto privato).
- Per i privati: **fatturato medio degli ultimi 3 anni** e se offre **servizi al
  pubblico** tramite siti/app.
- Tipo di contenuti (pubblici vs extranet/intranet; data di pubblicazione).

## Procedura (art. 3, art. 9)

1. **Soggetto pubblico o assimilato (art. 3 c. 1)?** PA (art. 1 c. 2 D.Lgs.
   165/2001), enti pubblici economici, **concessionari di servizi pubblici**,
   aziende municipalizzate regionali, enti pubblici di assistenza/riabilitazione,
   aziende di trasporto/telecomunicazione a prevalente capitale pubblico, aziende
   appaltatrici di servizi informatici, **organismi di diritto pubblico** (dir.
   2014/24/UE), soggetti con **contributi/agevolazioni pubbliche** -> **obbligato**.

2. **Grande privato (art. 3 c. 1-bis)?** Soggetto privato che offre **servizi al
   pubblico** via siti/app con **fatturato medio (ultimi 3 anni) > 500 milioni di
   euro** -> **obbligato** (adeguamento entro il 5/11/2022, art. 4 c. 2-bis).

3. **Esclusioni (art. 3 c. 2)?** Contenuti solo su dispositivi mobili/programmi
   per gruppi chiusi o usi specifici non diffusi; contenuti **extranet/intranet
   pubblicati prima del 23/9/2019** fino a revisione sostanziale.

4. **Regime di responsabilita' (art. 9)**:
   - **Pubblici (c. 1)**: rilevanza sulla **performance**, **responsabilita'
     dirigenziale e disciplinare** (artt. 21 e 55 D.Lgs. 165/2001).
   - **Grandi privati (c. 1-bis)**: **AgID** accerta e sanziona; dopo **diffida**,
     in caso di inottemperanza **sanzione fino al 5% del fatturato**; resta il
     diritto del discriminato di agire (L. 67/2006).

## Output

- Esito: obbligato (art. 3 c. 1 / c. 1-bis) o non obbligato/escluso, con
  l'articolo.
- Regime di responsabilita'/sanzioni applicabile.
- Rinvio agli obblighi contrattuali (task `checklist-appalto-contratto`).
- Avvertenza: i requisiti tecnici e l'audit di conformita' seguono le linee guida
  AgID e le WCAG.

## Regole

- Distinguere il regime **pubblico** (art. 3 c. 1) da quello dei **grandi privati**
  (art. 3 c. 1-bis): sanzioni e autorita' diverse.
- Non stabilire la conformita' tecnica (WCAG): rinviare alle linee guida AgID.
- Citare l'articolo (3, 9).
