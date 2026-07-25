# Note — Esodo ed estintori per un laboratorio a basso rischio

## Perché questo esempio

Mostra l'applicazione concreta dei **parametri numerici** dell'Allegato I (esodo, estintori, operatività) con i **versi
corretti delle disuguaglianze**, verificati a immagine dalla fonte. È il complemento del task
`imposta-strategia-antincendio`.

## Ancoraggio alla fonte

Ogni parametro è tratto da `../../references/fonti/dm-3-9-2021-progettazione-antincendio.md` (Allegato I, §4):

- Esodo: densità 0,7 persone/m², ≥ 2 vie indipendenti, Lcc ≤ 30/45 m, Les ≤ 60 m, altezza 2 m, larghezze ≥ 900/800/700/
  600 mm, porte per > 25 occupanti al pubblico (UNI EN 1125) — §4.2.
- Estintori: ≥ 13A, ≥ 6 kg/6 litri, distanza max 30 m, classe B ≥ 89 B — §4.4.
- Operatività: mezzi di soccorso ≤ 50 m — §4.7.

Tutte le costanti sono state **verificate a immagine** (pdftoppm) perché `pdftotext` perde i segni di disuguaglianza.

## Limiti

L'esempio non dimensiona né firma gli elaborati e non sceglie prodotti specifici: sono compiti del tecnico. La
prescrizione sulle porte con dispositivo UNI EN 1125 riguarda le attività aperte al pubblico con più di 25 occupanti,
non applicabile a questo laboratorio.
