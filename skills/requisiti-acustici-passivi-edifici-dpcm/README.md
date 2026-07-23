# requisiti-acustici-passivi-edifici-dpcm

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico competente in acustica da completare)

Skill di **supporto documentale** al **progettista edile o al tecnico** per l'**inquadramento dei requisiti
acustici passivi degli edifici** — classificazione dell'ambiente, grandezze e indici, valori limite — secondo il
**DPCM 5 dicembre 1997** (in attuazione della legge quadro sull'inquinamento acustico, L. 447/1995).

**Non esegue** misure o calcoli acustici né il collaudo in opera e **non sostituisce** il tecnico competente in
acustica: fornisce le categorie (Tab. A), le grandezze/indici (R'w, D2m,nT,w, L'n,w, LASmax, LAeq) e i valori
limite (Tab. B), più i limiti del rumore degli impianti.

## Target

Ingegneri e tecnici dell'edilizia che, in fase di progetto o di collaudo, devono classificare l'ambiente abitativo
e applicare i valori limite dei requisiti acustici passivi secondo il DPCM 5/12/1997.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `classifica-ambiente-e-valori-limite` | Categoria dell'ambiente (Tab. A) e valori limite dei requisiti acustici passivi per quella categoria (Tab. B: R'w, D2m,nT,w, L'n,w, LASmax, LAeq) |
| `inquadra-grandezze-e-rumore-impianti` | Grandezze e indici (R'w, D2m,nT,w con D2m,nT = D2m + 10 log(T/T0), L'n,w, LASmax, LAeq) e limiti del rumore degli impianti tecnologici (35/25 dB(A)) |

Nucleo: le **categorie** di ambiente (Tab. A, A-G), gli **indici** di valutazione (R'w, D2m,nT,w, L'n,w) e i
**valori limite** per categoria (Tab. B), con il verso della verifica (isolamenti = minimi, rumori = massimi) e i
limiti del **rumore degli impianti** (35 dB(A) LASmax discontinuo / 25 dB(A) LAeq continuo).

## Relazione con altre skill

- **Ambito distinto** dalle skill sul rumore ambientale (`valutazione-impatto-clima-acustico-l-447`,
  `mappatura-acustica-strategica-dlgs194`) e sul rumore negli ambienti di lavoro (`valutazione-rischio-rumore-dlgs81`):
  qui si tratta l'acustica **edilizia** (isolamento tra unità, facciata, calpestio, impianti). Complementa le skill
  di edilizia/energia sui requisiti dell'involucro.

## Fonti consultate

- **DPCM 5 dicembre 1997** - "Determinazione dei requisiti acustici passivi degli edifici" - G.U. Serie Generale
  n. 297 del 22 dicembre 1997 (PDF Gazzetta Ufficiale, SHA256 `5a8ae1f4...`, riproducibile via doppio download). Il
  PDF è una scansione GURITEL (immagine): contenuto letto renderizzando le pagine in immagine (`pdftoppm`) e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** misure, calcoli degli indici o il **collaudo** acustico in opera.
- **Non riproduce** le **norme UNI/ISO** citate (UNI 8270:1987 Parte 7, EN ISO 140-5/-6, ISO 3382) né la
  classificazione acustica UNI 11367.
- **Non sostituisce** il **tecnico competente in acustica** (L. 447/1995).

**La skill è un supporto documentale: non sostituisce il tecnico competente in acustica né il progettista, né la lettura diretta del DPCM 5 dicembre 1997 e delle norme tecniche applicabili.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
