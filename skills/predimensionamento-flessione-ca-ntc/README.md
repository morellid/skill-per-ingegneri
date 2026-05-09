# Pre-dimensionamento sezione c.a. SLU flessione semplice (NTC 2018 par. 4.1.2)

> Versione: 0.1.0-alpha
> Stato: in sviluppo, validazione Livello 1 OK; Livello 2 (vs casi pubblicati e software certificato) da completare.

Skill per il calcolo del momento resistente M_Rd di sezione rettangolare in c.a. singolarmente armata in flessione semplice SLU, ai sensi delle NTC 2018 par. 4.1.2.1 e 4.1.2.3.4.2 + Circolare 7/2019 par. C4.1.2. Implementazione code-driven, deterministica, riproducibile.

## Target

Ingegneri strutturisti italiani in fase di pre-dimensionamento di travi e travi-piattabanda in c.a. La skill serve per stimare M_Rd di sezioni semplici e confrontarlo con M_Ed; non sostituisce la verifica completa con software di calcolo strutturale.

## Cosa fa

Sotto-attivita' supportate:
- **Calcolo M_Rd**: dato b, h, d, A_s (mm^2), fck, fyk (MPa), restituisce f_cd, f_yd, eps_yd, x, x/d, eps_s, z = d - 0.4 x e M_Rd in kNm. Usa lo stress-block rettangolare equivalente (lambda = 0.8, eta = 1) valido per Classe 1 (fck <= 50 MPa). Verifica duttilita': snervamento acciaio + raccomandazione x/d <= 0.45 (Circ. 7/2019 C4.1.2).

Per il dettaglio tecnico vedi [`SKILL.md`](SKILL.md). Per le convenzioni di dominio vedi [`AGENTS.md`](AGENTS.md).

## Installazione

Clonare il repository e copiare/linkare la cartella `skills/predimensionamento-flessione-ca-ntc/` nel proprio ambiente Claude Code o Codex secondo lo schema di distribuzione skill in vigore. Vedi `../../README.md` del repo per dettagli.

## Fonti consultate

- DM 17/01/2018 (NTC 2018), GU n. 42 del 20/02/2018 - par. 4.1.2.1 e 4.1.2.3.4.2
- Circolare MIT n. 7 del 21/01/2019, GU n. 35 dell'11/02/2019 - par. C4.1.2

Dettaglio in [`references/sources.yaml`](references/sources.yaml).

## Limiti noti

- Solo sezioni rettangolari piene b x h (no T, L, circolari, profili speciali)
- Solo sezioni singolarmente armate (no armatura compressa A's)
- Solo flessione semplice (no pressoflessione, no flessione deviata)
- Solo Classe 1 fck <= 50 MPa (no calcestruzzi ad alta resistenza)
- Solo SLU (no SLE, fessurazione, deformabilita')
- Rifiuta sezioni sovra-armate (l'acciaio non snerva): segnala l'errore senza calcolo iterativo
- Non calcola d a partire da copriferro/staffe/diametro: l'utente fornisce d
- Non calcola A_s a partire da numero/diametro barre: l'utente fornisce A_s in mm^2
- Non applica regole di gerarchia delle resistenze NTC par. 7.4 (sismica)
- Validazione Livello 2 (vs casi pubblicati e software certificato) non ancora eseguita

**La skill non sostituisce il giudizio del progettista strutturale firmatario.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
