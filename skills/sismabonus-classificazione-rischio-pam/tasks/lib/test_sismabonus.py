"""
Test suite per sismabonus.py.

Copre solo consistenza interna delle formule:
- formula PAM: trapezoidale 4 termini + coda SLR;
- attribuzione classi PAM ai bordi (boundary tests);
- attribuzione classi IS-V ai bordi (boundary tests);
- regola classe finale = peggiore tra PAM e IS-V;
- regola salto classi tra fatto e progetto;
- validazione input (non finiti, negativi, chiavi mancanti, NaN/inf in JSON);
- anti-drift fixture-based contro examples/caso-conforme-fittizio/.

NON valida vs software certificati (ClaSS, CDM Win, EdiSis,
MasterSap-SismiClass): la validazione di campo su 10+ edifici reali e'
prerequisito del release stabile e va eseguita seguendo
tasks/run-test-suite.md.
"""

from __future__ import annotations

import io
import json
import math
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout

# Permette di eseguire il test sia da skill dir sia da repo root.
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

import sismabonus as sb  # noqa: E402


class TestPAMFormula(unittest.TestCase):
    """Verifica la formula trapezoidale PAM."""

    def test_pam_minimo_edificio_perfetto(self):
        """Edificio fittizio con TR_C molto alti (rare events) -> PAM
        molto basso, classe A+."""
        cap = sb.StatiLimiteCapacita(
            TR_C_SLO=10000, TR_C_SLD=10000, TR_C_SLV=20000, TR_C_SLC=50000,
            PGA_C_SLO=0.05, PGA_C_SLD=0.10, PGA_C_SLV=0.50, PGA_C_SLC=1.00,
        )
        curva, _ = sb.costruisci_curva_individuazione(cap, capping=False)
        ris = sb.calcola_PAM(curva)
        # PAM dovrebbe essere molto piccolo (<<0.5%)
        self.assertLess(ris.PAM_percentuale, 0.5)
        self.assertEqual(ris.classe_PAM, "A+")
        self.assertTrue(ris.monotona)

    def test_pam_quattro_contributi_trapezoidali(self):
        """La formula deve produrre esattamente 4 contributi trapezoidali
        (SLID->SLO, SLO->SLD, SLD->SLV, SLV->SLC)."""
        cap = sb.StatiLimiteCapacita(
            TR_C_SLO=30, TR_C_SLD=50, TR_C_SLV=475, TR_C_SLC=975,
            PGA_C_SLO=0.05, PGA_C_SLD=0.07, PGA_C_SLV=0.15, PGA_C_SLC=0.20,
        )
        curva, _ = sb.costruisci_curva_individuazione(cap, capping=False)
        ris = sb.calcola_PAM(curva)
        self.assertEqual(len(ris.contributi_trapezoidali), 4)
        nomi = [c["tratto"] for c in ris.contributi_trapezoidali]
        self.assertEqual(nomi, ["SLID->SLO", "SLO->SLD", "SLD->SLV", "SLV->SLC"])

    def test_pam_formula_a_mano(self):
        """Verifica numerica esplicita della formula su valori scelti."""
        # TR convenzionale SLID = 10 -> lambda_SLID = 0.1
        # Caso con TR_C: SLO=20, SLD=50, SLV=200, SLC=500
        # lambda: SLID=0.1, SLO=0.05, SLD=0.02, SLV=0.005, SLC=0.002
        # CR:     SLID=0,   SLO=0.07, SLD=0.15, SLV=0.50,  SLC=0.80, SLR=1.00
        cap = sb.StatiLimiteCapacita(
            TR_C_SLO=20, TR_C_SLD=50, TR_C_SLV=200, TR_C_SLC=500,
            PGA_C_SLO=0.05, PGA_C_SLD=0.07, PGA_C_SLV=0.10, PGA_C_SLC=0.15,
        )
        curva, _ = sb.costruisci_curva_individuazione(cap, capping=False)
        ris = sb.calcola_PAM(curva)
        # trap = sum |dlam| * avg(CR)
        # SLID->SLO: |0.1-0.05| * (0+0.07)/2  = 0.05 * 0.035  = 0.00175
        # SLO->SLD:  |0.05-0.02| * (0.07+0.15)/2 = 0.03 * 0.11 = 0.0033
        # SLD->SLV:  |0.02-0.005| * (0.15+0.50)/2 = 0.015 * 0.325 = 0.004875
        # SLV->SLC:  |0.005-0.002| * (0.50+0.80)/2 = 0.003 * 0.65 = 0.00195
        # coda:      0.002 * 1.0 = 0.002
        # PAM:       0.00175 + 0.0033 + 0.004875 + 0.00195 + 0.002 = 0.013875
        atteso = 0.013875
        self.assertAlmostEqual(ris.PAM, atteso, places=8)

    def test_pam_non_monotona_segnalata(self):
        """Se TR_C non sono ordinati per severita' decrescente
        (lambda non monotona), il flag deve essere False (con capping
        disattivato per esporre la non monotonia originale)."""
        # TR_C(SLO)=50 piu' grande di TR_C(SLD)=30 -> edificio raggiunge
        # SLD prima di SLO (caso raro ma fisicamente possibile)
        cap = sb.StatiLimiteCapacita(
            TR_C_SLO=50, TR_C_SLD=30, TR_C_SLV=200, TR_C_SLC=500,
            PGA_C_SLO=0.10, PGA_C_SLD=0.07, PGA_C_SLV=0.15, PGA_C_SLC=0.20,
        )
        curva, _ = sb.costruisci_curva_individuazione(cap, capping=False)
        ris = sb.calcola_PAM(curva)
        self.assertFalse(ris.monotona)

    def test_pam_riferimento_decreto_VR_50(self):
        """Allegato A nota a Tab. 1: una costruzione con V_R=50 anni
        progettata al minimo NTC (TR_C identici ai TR di domanda) ha
        PAM = 1.13%.

        TR di domanda NTC per V_R=50 anni:
            P_VR = {0.81, 0.63, 0.10, 0.05} per {SLO, SLD, SLV, SLC}
            TR_D = -V_R / ln(1 - P_VR)
                 ~= {30, 50, 475, 975} anni

        Questo test e' la verifica numerica fondamentale del modulo
        contro un valore esplicitamente dichiarato dal decreto stesso.
        Tolleranza: il decreto arrotonda a 2 decimali (1.13%); la mia
        formula con abs() produce 1.1344% ~= 1.13%. Calcolato a mano
        nel CHANGELOG.
        """
        cap = sb.StatiLimiteCapacita(
            TR_C_SLO=30, TR_C_SLD=50, TR_C_SLV=475, TR_C_SLC=975,
            PGA_C_SLO=0.05, PGA_C_SLD=0.07,
            PGA_C_SLV=0.15, PGA_C_SLC=0.20,
        )
        curva, _ = sb.costruisci_curva_individuazione(cap, capping=True)
        ris = sb.calcola_PAM(curva)
        # Atteso 1.13% (decreto). Tolleranza 0.01% per arrotondamento.
        self.assertAlmostEqual(ris.PAM_percentuale, 1.13, delta=0.01)
        self.assertEqual(ris.classe_PAM, "B")

    def test_capping_punto_2_1_3_attivo_default(self):
        """Verifica capping prescritto da Allegato A passo 2.1.3:
        TR_C(SLO/SLD) := min(TR_C(SLO/SLD), TR_C(SLV))."""
        # TR_C(SLO)=2000 > TR_C(SLV)=475 -> SLO viene cappato a 475
        cap = sb.StatiLimiteCapacita(
            TR_C_SLO=2000, TR_C_SLD=50, TR_C_SLV=475, TR_C_SLC=975,
            PGA_C_SLO=0.20, PGA_C_SLD=0.07,
            PGA_C_SLV=0.15, PGA_C_SLC=0.20,
        )
        curva, info = sb.costruisci_curva_individuazione(cap, capping=True)
        self.assertTrue(info.capping_attivo)
        self.assertTrue(info.SLO_modificato)
        self.assertFalse(info.SLD_modificato)
        self.assertEqual(info.TR_C_SLO_originale, 2000)
        self.assertEqual(info.TR_C_SLO_capped, 475)
        # lambda_SLO dovrebbe essere uguale a lambda_SLV dopo capping
        self.assertAlmostEqual(curva.lam_SLO, curva.lam_SLV)

    def test_capping_disattivato_via_flag(self):
        """Con capping=False, i TR_C originali sono usati invariati."""
        cap = sb.StatiLimiteCapacita(
            TR_C_SLO=2000, TR_C_SLD=50, TR_C_SLV=475, TR_C_SLC=975,
            PGA_C_SLO=0.20, PGA_C_SLD=0.07,
            PGA_C_SLV=0.15, PGA_C_SLC=0.20,
        )
        curva, info = sb.costruisci_curva_individuazione(cap, capping=False)
        self.assertFalse(info.capping_attivo)
        self.assertFalse(info.SLO_modificato)
        self.assertEqual(info.TR_C_SLO_capped, 2000)
        self.assertAlmostEqual(curva.lam_SLO, 1.0 / 2000)

    def test_capping_no_op_su_input_gia_monotono(self):
        """Su input gia' monotono il capping non altera nulla."""
        cap = sb.StatiLimiteCapacita(
            TR_C_SLO=30, TR_C_SLD=50, TR_C_SLV=475, TR_C_SLC=975,
            PGA_C_SLO=0.05, PGA_C_SLD=0.07,
            PGA_C_SLV=0.15, PGA_C_SLC=0.20,
        )
        curva, info = sb.costruisci_curva_individuazione(cap, capping=True)
        self.assertTrue(info.capping_attivo)
        self.assertFalse(info.SLO_modificato)
        self.assertFalse(info.SLD_modificato)

    def test_pam_monotona_caso_normale(self):
        cap = sb.StatiLimiteCapacita(
            TR_C_SLO=20, TR_C_SLD=50, TR_C_SLV=200, TR_C_SLC=500,
            PGA_C_SLO=0.05, PGA_C_SLD=0.07, PGA_C_SLV=0.10, PGA_C_SLC=0.15,
        )
        curva, _ = sb.costruisci_curva_individuazione(cap, capping=False)
        ris = sb.calcola_PAM(curva)
        self.assertTrue(ris.monotona)


class TestClassiPAMBoundary(unittest.TestCase):
    """Test sui bordi della Tab. classi PAM (Allegato A punto 2.3)."""

    def test_classe_A_plus_al_bordo(self):
        self.assertEqual(sb.classifica_PAM(0.000), "A+")
        self.assertEqual(sb.classifica_PAM(0.005), "A+")  # 0.50% incluso

    def test_classe_A(self):
        self.assertEqual(sb.classifica_PAM(0.0050001), "A")
        self.assertEqual(sb.classifica_PAM(0.010), "A")    # 1.0% incluso

    def test_classe_B(self):
        self.assertEqual(sb.classifica_PAM(0.0100001), "B")
        self.assertEqual(sb.classifica_PAM(0.015), "B")

    def test_classe_C(self):
        self.assertEqual(sb.classifica_PAM(0.0150001), "C")
        self.assertEqual(sb.classifica_PAM(0.025), "C")

    def test_classe_D(self):
        self.assertEqual(sb.classifica_PAM(0.0250001), "D")
        self.assertEqual(sb.classifica_PAM(0.035), "D")

    def test_classe_E(self):
        self.assertEqual(sb.classifica_PAM(0.0350001), "E")
        self.assertEqual(sb.classifica_PAM(0.045), "E")

    def test_classe_F(self):
        self.assertEqual(sb.classifica_PAM(0.0450001), "F")
        self.assertEqual(sb.classifica_PAM(0.075), "F")

    def test_classe_G(self):
        self.assertEqual(sb.classifica_PAM(0.0750001), "G")
        self.assertEqual(sb.classifica_PAM(0.5), "G")
        self.assertEqual(sb.classifica_PAM(1.0), "G")

    def test_classifica_pam_rifiuta_negativi(self):
        with self.assertRaises(ValueError):
            sb.classifica_PAM(-0.001)

    def test_classifica_pam_rifiuta_nan(self):
        with self.assertRaises(ValueError):
            sb.classifica_PAM(float("nan"))


class TestClassiISVBoundary(unittest.TestCase):
    """Test sui bordi della Tab. 2 classi IS-V dell'Allegato A
    (testo letterale DM 65/2017):

        100% <  IS-V          -> A+
        80%  <= IS-V <  100%  -> A
        60%  <= IS-V <  80%   -> B
        45%  <= IS-V <  60%   -> C
        30%  <= IS-V <  45%   -> D
        15%  <= IS-V <  30%   -> E
                IS-V <= 15%   -> F

    Convenzione: lower bound INCLUSO, upper bound ESCLUSO per A..E.
    Caso ambiguo IS-V = 100%: il decreto non lo copre formalmente
    (A+: > 100%, A: < 100%); interpretazione conservativa = A.
    """

    def test_classe_A_plus(self):
        self.assertEqual(sb.classifica_IS_V(1.5), "A+")
        self.assertEqual(sb.classifica_IS_V(1.0001), "A+")

    def test_classe_A(self):
        # 100% esatto: ambiguita' del decreto, interpretazione conservativa -> A
        self.assertEqual(sb.classifica_IS_V(1.00), "A")
        # 99.99%: chiaramente A (< 100%)
        self.assertEqual(sb.classifica_IS_V(0.9999), "A")
        self.assertEqual(sb.classifica_IS_V(0.90), "A")
        # 80% esatto: lower bound INCLUSO di A -> A
        self.assertEqual(sb.classifica_IS_V(0.80), "A")

    def test_classe_B(self):
        # 79.99%: < 80%, quindi B (upper bound ESCLUSO di A)
        self.assertEqual(sb.classifica_IS_V(0.7999), "B")
        # 60% esatto: lower bound INCLUSO di B -> B
        self.assertEqual(sb.classifica_IS_V(0.60), "B")

    def test_classe_C(self):
        self.assertEqual(sb.classifica_IS_V(0.5999), "C")
        # 45% esatto: lower bound INCLUSO di C -> C
        self.assertEqual(sb.classifica_IS_V(0.45), "C")

    def test_classe_D(self):
        self.assertEqual(sb.classifica_IS_V(0.4499), "D")
        self.assertEqual(sb.classifica_IS_V(0.30), "D")

    def test_classe_E(self):
        self.assertEqual(sb.classifica_IS_V(0.2999), "E")
        self.assertEqual(sb.classifica_IS_V(0.15), "E")

    def test_classe_F(self):
        # 14.99%: < 15%, quindi F (upper bound ESCLUSO di E, nota: F ha
        # IS-V <= 15%, quindi anche 15% rientra in entrambi - ambiguita'
        # del decreto al solo bordo 15%; interpretazione: 15% va in E
        # come da convenzione "lower bound incluso").
        self.assertEqual(sb.classifica_IS_V(0.1499), "F")
        self.assertEqual(sb.classifica_IS_V(0.0), "F")

    def test_classifica_isv_rifiuta_negativi(self):
        with self.assertRaises(ValueError):
            sb.classifica_IS_V(-0.1)

    def test_classifica_isv_rifiuta_nan(self):
        with self.assertRaises(ValueError):
            sb.classifica_IS_V(float("inf"))


class TestClasseFinale(unittest.TestCase):
    """La classe finale e' la peggiore tra PAM e IS-V."""

    def test_peggiore_basic(self):
        self.assertEqual(sb.classe_peggiore("A+", "B"), "B")
        self.assertEqual(sb.classe_peggiore("C", "A"), "C")
        self.assertEqual(sb.classe_peggiore("E", "E"), "E")

    def test_peggiore_extremes(self):
        self.assertEqual(sb.classe_peggiore("A+", "G"), "G")
        self.assertEqual(sb.classe_peggiore("A+", "F"), "F")
        # G non puo' venire da IS-V (massima e' F), ma classe_peggiore
        # accetta input arbitrari coerenti con ORDINE_CLASSI.
        self.assertEqual(sb.classe_peggiore("F", "G"), "G")

    def test_classe_non_riconosciuta(self):
        with self.assertRaises(ValueError):
            sb.classe_peggiore("A", "Z")
        with self.assertRaises(ValueError):
            sb.classe_peggiore("A++", "B")


class TestClassificazione(unittest.TestCase):
    """Integrazione: classifica un edificio completo."""

    def test_classificazione_caso_buono(self):
        cap = sb.StatiLimiteCapacita(
            TR_C_SLO=200, TR_C_SLD=500, TR_C_SLV=1500, TR_C_SLC=3000,
            PGA_C_SLO=0.03, PGA_C_SLD=0.05, PGA_C_SLV=0.20, PGA_C_SLC=0.30,
        )
        dom = sb.StatiLimiteDomanda(
            PGA_D_SLO=0.025, PGA_D_SLD=0.03, PGA_D_SLV=0.10, PGA_D_SLC=0.13,
        )
        ris = sb.classifica(cap, dom)
        # IS-V = 0.20/0.10 = 2.0 -> 200% -> A+
        self.assertEqual(ris.isv.classe_IS_V, "A+")
        # PAM dovrebbe essere basso
        self.assertIn(ris.pam.classe_PAM, ("A+", "A", "B"))
        # Classe finale = peggiore
        self.assertEqual(ris.classe_finale,
                         sb.classe_peggiore(ris.pam.classe_PAM, ris.isv.classe_IS_V))

    def test_classificazione_caso_critico(self):
        # Edificio molto debole: TR_C bassi, PGA_C < PGA_D
        cap = sb.StatiLimiteCapacita(
            TR_C_SLO=10, TR_C_SLD=15, TR_C_SLV=30, TR_C_SLC=50,
            PGA_C_SLO=0.02, PGA_C_SLD=0.03, PGA_C_SLV=0.05, PGA_C_SLC=0.07,
        )
        dom = sb.StatiLimiteDomanda(
            PGA_D_SLO=0.05, PGA_D_SLD=0.06, PGA_D_SLV=0.20, PGA_D_SLC=0.25,
        )
        ris = sb.classifica(cap, dom)
        # IS-V = 0.05/0.20 = 0.25 = 25% -> E
        self.assertEqual(ris.isv.classe_IS_V, "E")
        # PAM alto, classe scadente
        self.assertIn(ris.pam.classe_PAM, ("D", "E", "F", "G"))


class TestSaltoClassi(unittest.TestCase):
    """Verifica il calcolo del salto classi (Allegato A punto 3)."""

    def _ris(self, classe: str) -> sb.RisultatoClassificazione:
        # Helper: costruisce un risultato fittizio con classe finale specificata
        pam = sb.RisultatoPAM(
            PAM=0.0, PAM_percentuale=0.0, classe_PAM=classe,
            contributi_trapezoidali=[], contributo_coda_SLR=0.0, monotona=True,
        )
        isv = sb.RisultatoISV(IS_V=1.0, IS_V_percentuale=100.0, classe_IS_V=classe)
        capping = sb.CappingApplicato(
            capping_attivo=True,
            TR_C_SLO_originale=30, TR_C_SLD_originale=50,
            TR_C_SLO_capped=30, TR_C_SLD_capped=50,
            SLO_modificato=False, SLD_modificato=False,
        )
        return sb.RisultatoClassificazione(
            pam=pam, isv=isv, classe_finale=classe,
            descrizione_classe_finale="(test)",
            capping=capping,
        )

    def test_salto_zero(self):
        f = self._ris("D")
        p = self._ris("D")
        s = sb.calcola_salto_classi(f, p)
        self.assertEqual(s.salto_classi, 0)

    def test_salto_due(self):
        f = self._ris("D")
        p = self._ris("B")  # D->B = 2 classi (D=3, B=2 in indice 0-based; 3-1=2 corretto: D=3, C=2, B=1?)
        # Verifichiamo la convenzione: ORDINE_CLASSI = (A+, A, B, C, D, E, F, G)
        # A+ idx=0, A=1, B=2, C=3, D=4, E=5, F=6, G=7
        # Salto = idx_fatto - idx_progetto = 4 - 2 = 2
        s = sb.calcola_salto_classi(f, p)
        self.assertEqual(s.salto_classi, 2)

    def test_salto_negativo(self):
        # Stato di progetto peggio di fatto -> anomalia
        f = self._ris("B")
        p = self._ris("D")
        s = sb.calcola_salto_classi(f, p)
        self.assertEqual(s.salto_classi, -2)

    def test_salto_massimo(self):
        f = self._ris("G")
        p = self._ris("A+")
        s = sb.calcola_salto_classi(f, p)
        self.assertEqual(s.salto_classi, 7)


class TestValidazioneInput(unittest.TestCase):
    """Validazione hardening: rifiuta input non finiti, negativi, ecc."""

    def test_TR_negativo(self):
        with self.assertRaises(ValueError):
            sb.StatiLimiteCapacita(
                TR_C_SLO=-10, TR_C_SLD=50, TR_C_SLV=100, TR_C_SLC=200,
                PGA_C_SLO=0.05, PGA_C_SLD=0.07, PGA_C_SLV=0.10, PGA_C_SLC=0.15,
            )

    def test_TR_zero(self):
        with self.assertRaises(ValueError):
            sb.StatiLimiteCapacita(
                TR_C_SLO=0, TR_C_SLD=50, TR_C_SLV=100, TR_C_SLC=200,
                PGA_C_SLO=0.05, PGA_C_SLD=0.07, PGA_C_SLV=0.10, PGA_C_SLC=0.15,
            )

    def test_PGA_nan(self):
        with self.assertRaises(ValueError):
            sb.StatiLimiteCapacita(
                TR_C_SLO=20, TR_C_SLD=50, TR_C_SLV=100, TR_C_SLC=200,
                PGA_C_SLO=float("nan"), PGA_C_SLD=0.07,
                PGA_C_SLV=0.10, PGA_C_SLC=0.15,
            )

    def test_PGA_inf(self):
        with self.assertRaises(ValueError):
            sb.StatiLimiteCapacita(
                TR_C_SLO=20, TR_C_SLD=50, TR_C_SLV=100, TR_C_SLC=200,
                PGA_C_SLO=0.05, PGA_C_SLD=0.07,
                PGA_C_SLV=float("inf"), PGA_C_SLC=0.15,
            )

    def test_PGA_string(self):
        with self.assertRaises(ValueError):
            sb.StatiLimiteCapacita(
                TR_C_SLO=20, TR_C_SLD=50, TR_C_SLV=100, TR_C_SLC=200,
                PGA_C_SLO="0.05", PGA_C_SLD=0.07,
                PGA_C_SLV=0.10, PGA_C_SLC=0.15,
            )

    def test_PGA_bool_rifiutato(self):
        with self.assertRaises(ValueError):
            sb.StatiLimiteCapacita(
                TR_C_SLO=20, TR_C_SLD=50, TR_C_SLV=100, TR_C_SLC=200,
                PGA_C_SLO=True, PGA_C_SLD=0.07,
                PGA_C_SLV=0.10, PGA_C_SLC=0.15,
            )

    def test_PGA_D_SLV_zero_rifiutato(self):
        with self.assertRaises(ValueError):
            sb.calcola_ISV(0.10, 0.0)

    def test_isv_pga_c_zero_ammesso(self):
        # PGA_C(SLV) = 0 e' valore limite (edificio crollato): IS-V = 0
        ris = sb.calcola_ISV(0.0, 0.10)
        self.assertEqual(ris.IS_V, 0.0)
        self.assertEqual(ris.classe_IS_V, "F")


class TestCLI(unittest.TestCase):
    """Smoke test CLI con file JSON. Usa tempfile per supportare
    filesystem read-only sulla skill installata."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmpdir = self._tmp.name

    def tearDown(self):
        self._tmp.cleanup()

    def _scrivi(self, payload: dict, name: str = "input.json") -> str:
        path = os.path.join(self.tmpdir, name)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f)
        return path

    def test_cli_solo_fatto(self):
        path = self._scrivi({
            "fatto": {
                "TR_C_SLO": 20, "TR_C_SLD": 50, "TR_C_SLV": 200, "TR_C_SLC": 500,
                "PGA_C_SLO": 0.05, "PGA_C_SLD": 0.07,
                "PGA_C_SLV": 0.10, "PGA_C_SLC": 0.15,
                "PGA_D_SLO": 0.03, "PGA_D_SLD": 0.04,
                "PGA_D_SLV": 0.10, "PGA_D_SLC": 0.13,
            }
        })
        buf_out = io.StringIO()
        with redirect_stdout(buf_out):
            rc = sb.main(["--input-json", path])
        self.assertEqual(rc, 0)
        out = json.loads(buf_out.getvalue())
        self.assertIn("fatto", out)
        self.assertNotIn("progetto", out)
        self.assertIn("classe_finale", out["fatto"])

    def test_cli_fatto_e_progetto(self):
        path = self._scrivi({
            "fatto": {
                "TR_C_SLO": 20, "TR_C_SLD": 50, "TR_C_SLV": 200, "TR_C_SLC": 500,
                "PGA_C_SLO": 0.05, "PGA_C_SLD": 0.07,
                "PGA_C_SLV": 0.10, "PGA_C_SLC": 0.15,
                "PGA_D_SLO": 0.03, "PGA_D_SLD": 0.04,
                "PGA_D_SLV": 0.10, "PGA_D_SLC": 0.13,
            },
            "progetto": {
                "TR_C_SLO": 100, "TR_C_SLD": 250, "TR_C_SLV": 800, "TR_C_SLC": 1500,
                "PGA_C_SLO": 0.05, "PGA_C_SLD": 0.07,
                "PGA_C_SLV": 0.18, "PGA_C_SLC": 0.25,
            }
        })
        buf_out = io.StringIO()
        with redirect_stdout(buf_out):
            rc = sb.main(["--input-json", path])
        self.assertEqual(rc, 0)
        out = json.loads(buf_out.getvalue())
        self.assertIn("progetto", out)
        self.assertIn("salto_classi", out)

    def test_cli_chiave_mancante(self):
        path = self._scrivi({
            "fatto": {
                # manca TR_C_SLC
                "TR_C_SLO": 20, "TR_C_SLD": 50, "TR_C_SLV": 200,
                "PGA_C_SLO": 0.05, "PGA_C_SLD": 0.07,
                "PGA_C_SLV": 0.10, "PGA_C_SLC": 0.15,
                "PGA_D_SLO": 0.03, "PGA_D_SLD": 0.04,
                "PGA_D_SLV": 0.10, "PGA_D_SLC": 0.13,
            }
        })
        buf_err = io.StringIO()
        with redirect_stderr(buf_err):
            rc = sb.main(["--input-json", path])
        self.assertEqual(rc, 2)
        self.assertIn("TR_C_SLC", buf_err.getvalue())

    def test_cli_input_inesistente(self):
        buf_err = io.StringIO()
        with redirect_stderr(buf_err):
            rc = sb.main(["--input-json", "/path/non/esiste.json"])
        self.assertEqual(rc, 2)

    def test_cli_nan_nel_json_rifiutato(self):
        # JSON tecnicamente valido per Python ma non per RFC 8259
        path = os.path.join(self.tmpdir, "nan.json")
        with open(path, "w", encoding="utf-8") as f:
            f.write('{"fatto": {"TR_C_SLO": NaN}}')
        buf_err = io.StringIO()
        with redirect_stderr(buf_err):
            rc = sb.main(["--input-json", path])
        self.assertEqual(rc, 2)

    def test_cli_chiave_fatto_mancante(self):
        path = self._scrivi({"progetto": {}})
        buf_err = io.StringIO()
        with redirect_stderr(buf_err):
            rc = sb.main(["--input-json", path])
        self.assertEqual(rc, 2)

    def test_cli_pga_d_progetto_parziale_errore(self):
        """Se 'progetto' contiene SOLO ALCUNE chiavi PGA_D_*, la CLI
        deve segnalare errore esplicito (no fallback silenzioso)."""
        path = self._scrivi({
            "fatto": {
                "TR_C_SLO": 30, "TR_C_SLD": 50, "TR_C_SLV": 475, "TR_C_SLC": 975,
                "PGA_C_SLO": 0.05, "PGA_C_SLD": 0.07,
                "PGA_C_SLV": 0.15, "PGA_C_SLC": 0.20,
                "PGA_D_SLO": 0.05, "PGA_D_SLD": 0.07,
                "PGA_D_SLV": 0.15, "PGA_D_SLC": 0.20,
            },
            "progetto": {
                "TR_C_SLO": 100, "TR_C_SLD": 250, "TR_C_SLV": 800, "TR_C_SLC": 1500,
                "PGA_C_SLO": 0.10, "PGA_C_SLD": 0.15,
                "PGA_C_SLV": 0.30, "PGA_C_SLC": 0.40,
                # SOLO una chiave PGA_D in progetto: typo simulato
                "PGA_D_SLV": 0.15,
            }
        })
        buf_err = io.StringIO()
        with redirect_stderr(buf_err):
            rc = sb.main(["--input-json", path])
        self.assertEqual(rc, 2)
        self.assertIn("PGA_D", buf_err.getvalue())

    def test_cli_pga_d_progetto_assente_eredita(self):
        """Se 'progetto' NON ha alcuna chiave PGA_D_*, eredita da fatto."""
        path = self._scrivi({
            "fatto": {
                "TR_C_SLO": 30, "TR_C_SLD": 50, "TR_C_SLV": 475, "TR_C_SLC": 975,
                "PGA_C_SLO": 0.05, "PGA_C_SLD": 0.07,
                "PGA_C_SLV": 0.15, "PGA_C_SLC": 0.20,
                "PGA_D_SLO": 0.05, "PGA_D_SLD": 0.07,
                "PGA_D_SLV": 0.15, "PGA_D_SLC": 0.20,
            },
            "progetto": {
                "TR_C_SLO": 100, "TR_C_SLD": 250, "TR_C_SLV": 800, "TR_C_SLC": 1500,
                "PGA_C_SLO": 0.10, "PGA_C_SLD": 0.15,
                "PGA_C_SLV": 0.30, "PGA_C_SLC": 0.40,
            }
        })
        buf_out = io.StringIO()
        with redirect_stdout(buf_out):
            rc = sb.main(["--input-json", path])
        self.assertEqual(rc, 0)
        out = json.loads(buf_out.getvalue())
        # IS-V progetto = PGA_C(SLV)/PGA_D(SLV) = 0.30/0.15 = 2.0 (eredita PGA_D fatto)
        self.assertAlmostEqual(out["progetto"]["isv"]["IS_V"], 2.0)

    def test_cli_no_capping_flag(self):
        """Verifica che --no-capping disattivi il capping prescritto."""
        path = self._scrivi({
            "fatto": {
                "TR_C_SLO": 2000, "TR_C_SLD": 50, "TR_C_SLV": 475, "TR_C_SLC": 975,
                "PGA_C_SLO": 0.20, "PGA_C_SLD": 0.07,
                "PGA_C_SLV": 0.15, "PGA_C_SLC": 0.20,
                "PGA_D_SLO": 0.05, "PGA_D_SLD": 0.07,
                "PGA_D_SLV": 0.15, "PGA_D_SLC": 0.20,
            }
        })
        # Con capping (default)
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.assertEqual(sb.main(["--input-json", path]), 0)
        with_capping = json.loads(buf.getvalue())
        self.assertTrue(with_capping["capping_attivo"])
        self.assertTrue(with_capping["fatto"]["capping"]["SLO_modificato"])

        # Senza capping
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.assertEqual(sb.main(["--input-json", path, "--no-capping"]), 0)
        no_capping = json.loads(buf.getvalue())
        self.assertFalse(no_capping["capping_attivo"])
        self.assertFalse(no_capping["fatto"]["capping"]["SLO_modificato"])


class TestAntiDriftFixture(unittest.TestCase):
    """Fixture-based: verifica che il modulo produca i numeri attesi
    salvati in examples/caso-conforme-fittizio/. Se i numeri cambiano,
    sia il fixture sia gli estratti normativi vanno aggiornati di
    conserva."""

    @classmethod
    def setUpClass(cls):
        skill_dir = os.path.dirname(os.path.dirname(_THIS_DIR))
        cls.input_path = os.path.join(
            skill_dir, "examples", "caso-conforme-fittizio", "input.json"
        )
        cls.expected_path = os.path.join(
            skill_dir, "examples", "caso-conforme-fittizio", "expected.json"
        )

    def test_fixture_conforme(self):
        if not os.path.exists(self.input_path):
            self.skipTest(f"fixture mancante: {self.input_path}")
        if not os.path.exists(self.expected_path):
            self.skipTest(f"expected mancante: {self.expected_path}")
        buf_out = io.StringIO()
        with redirect_stdout(buf_out):
            rc = sb.main(["--input-json", self.input_path])
        self.assertEqual(rc, 0)
        actual = json.loads(buf_out.getvalue())
        with open(self.expected_path, "r", encoding="utf-8") as f:
            expected = json.load(f)
        # Confronto sui campi piu' importanti per evitare fragilita'
        # su rappresentazione float dei sub-totali.
        self.assertEqual(
            actual["fatto"]["pam"]["classe_PAM"],
            expected["fatto"]["pam"]["classe_PAM"],
        )
        self.assertEqual(
            actual["fatto"]["isv"]["classe_IS_V"],
            expected["fatto"]["isv"]["classe_IS_V"],
        )
        self.assertEqual(
            actual["fatto"]["classe_finale"],
            expected["fatto"]["classe_finale"],
        )
        self.assertAlmostEqual(
            actual["fatto"]["pam"]["PAM_percentuale"],
            expected["fatto"]["pam"]["PAM_percentuale"],
            places=4,
        )
        if "progetto" in expected:
            self.assertEqual(
                actual["progetto"]["classe_finale"],
                expected["progetto"]["classe_finale"],
            )
            self.assertEqual(
                actual["salto_classi"]["salto_classi"],
                expected["salto_classi"]["salto_classi"],
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
