#!/usr/bin/env python3
"""Test suite per flessione_ca.py - consistenza interna formule NTC 2018."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from flessione_ca import (  # noqa: E402
    ALPHA_CC_DEFAULT,
    EPS_CU_DEFAULT,
    ES_DEFAULT,
    FCK_MAX_CLASSE_1,
    GAMMA_C_DEFAULT,
    GAMMA_S_DEFAULT,
    LAMBDA_SB,
    ZETA_LIM_DUTTILITA,
    asse_neutro_x,
    calcola_m_rd,
    deformazione_acciaio_eps_s,
    deformazione_snervamento_eyd,
    resistenza_acciaio_fyd,
    resistenza_calcestruzzo_fcd,
)


class TestMateriali(unittest.TestCase):
    def test_fcd_C25_30(self):
        # fck = 25, alpha_cc = 0.85, gamma_c = 1.5  -> fcd = 14.166...
        self.assertAlmostEqual(resistenza_calcestruzzo_fcd(25.0), 0.85 * 25.0 / 1.5)

    def test_fcd_C30_37(self):
        self.assertAlmostEqual(resistenza_calcestruzzo_fcd(30.0), 0.85 * 30.0 / 1.5)

    def test_fcd_alpha_e_gamma_custom(self):
        # alpha_cc = 1.0 (carico breve durata), gamma_c = 1.5
        self.assertAlmostEqual(
            resistenza_calcestruzzo_fcd(25.0, alpha_cc=1.0, gamma_c=1.5),
            25.0 / 1.5,
        )

    def test_fcd_oltre_classe_1_solleva(self):
        # fck > 50 MPa -> non coperto
        with self.assertRaises(ValueError) as cm:
            resistenza_calcestruzzo_fcd(60.0)
        self.assertIn("50", str(cm.exception))

    def test_fcd_negativo_solleva(self):
        with self.assertRaises(ValueError):
            resistenza_calcestruzzo_fcd(-5.0)

    def test_fcd_nan_solleva(self):
        with self.assertRaises(ValueError):
            resistenza_calcestruzzo_fcd(float("nan"))

    def test_fyd_B450C(self):
        # B450C: fyk = 450, gamma_s = 1.15 -> fyd = 391.30...
        self.assertAlmostEqual(resistenza_acciaio_fyd(450.0), 450.0 / 1.15)

    def test_fyd_gamma_custom(self):
        # combinazione eccezionale: gamma_s = 1.0
        self.assertAlmostEqual(resistenza_acciaio_fyd(450.0, gamma_s=1.0), 450.0)

    def test_eps_yd_B450C(self):
        # fyd = 391.30 / 200000 = 0.001957
        fyd = resistenza_acciaio_fyd(450.0)
        self.assertAlmostEqual(deformazione_snervamento_eyd(fyd), fyd / 200000.0)


class TestAsseNeutro(unittest.TestCase):
    def test_x_da_equilibrio(self):
        # b=300, As=1000, fyd=391.3, fcd=14.17, lambda=0.8
        # x = (1000*391.3) / (0.8 * 300 * 14.17) = 391300 / 3400.8 = 115.06...
        b, a_s = 300.0, 1000.0
        fyd = 450.0 / 1.15
        fcd = 0.85 * 25.0 / 1.5
        x = asse_neutro_x(a_s, fyd, b, fcd)
        expected = (a_s * fyd) / (LAMBDA_SB * b * fcd)
        self.assertAlmostEqual(x, expected)

    def test_x_zero_solleva(self):
        with self.assertRaises(ValueError):
            asse_neutro_x(0.0, 391.3, 300.0, 14.17)

    def test_x_b_zero_solleva(self):
        with self.assertRaises(ValueError):
            asse_neutro_x(1000.0, 391.3, 0.0, 14.17)


class TestDeformazione(unittest.TestCase):
    def test_eps_s_acciaio_in_zona_tesa(self):
        # x = 100, d = 400 -> eps_s = 0.0035 * 300/100 = 0.0105
        self.assertAlmostEqual(deformazione_acciaio_eps_s(100.0, 400.0), 0.0035 * 3.0)

    def test_eps_s_x_uguale_d_solleva(self):
        with self.assertRaises(ValueError):
            deformazione_acciaio_eps_s(400.0, 400.0)

    def test_eps_s_x_oltre_d_solleva(self):
        with self.assertRaises(ValueError):
            deformazione_acciaio_eps_s(500.0, 400.0)


class TestEndToEnd(unittest.TestCase):
    def test_caso_standard_b300_h500_d460_3F16(self):
        # Trave 300x500, copriferro 30+stf 8+barra 16/2 -> d = 500-30-8-8 = 454; uso d=460
        # As = 3 phi 16 = 3*pi*16^2/4 = 603.19 mm2
        # fck = 25 (C25/30), fyk = 450 (B450C)
        # Calcolo atteso:
        # fcd = 14.1667, fyd = 391.304
        # x = (603.19 * 391.304) / (0.8 * 300 * 14.1667) = 236010 / 3400 = 69.41 mm
        # zeta = 69.41/460 = 0.151 (ben sotto 0.45)
        # eps_s = 0.0035 * (460-69.41)/69.41 = 0.0197 (ben oltre eps_yd=0.00196)
        # z = 460 - 0.4*69.41 = 432.24
        # M_Rd = 603.19 * 391.304 * 432.24 = 102026807 Nmm = 102.03 kNm
        res = calcola_m_rd(b=300, h=500, d=460, a_s=603.19, fck=25, fyk=450)
        self.assertGreater(res.m_rd_kNm, 100.0)
        self.assertLess(res.m_rd_kNm, 105.0)
        self.assertTrue(res.duttile_snervamento)
        self.assertTrue(res.duttile_zeta_limite)

    def test_acciaio_snerva(self):
        res = calcola_m_rd(b=300, h=500, d=460, a_s=603.19, fck=25, fyk=450)
        self.assertGreater(res.eps_s, res.eps_yd)

    def test_zeta_calcolato(self):
        res = calcola_m_rd(b=300, h=500, d=460, a_s=603.19, fck=25, fyk=450)
        self.assertAlmostEqual(res.zeta, res.x / res.d)

    def test_z_braccio_leva(self):
        res = calcola_m_rd(b=300, h=500, d=460, a_s=603.19, fck=25, fyk=450)
        self.assertAlmostEqual(res.z, res.d - 0.4 * res.x)

    def test_m_rd_consistente_con_z(self):
        res = calcola_m_rd(b=300, h=500, d=460, a_s=603.19, fck=25, fyk=450)
        self.assertAlmostEqual(res.m_rd_Nmm, res.a_s * res.fyd * res.z)

    def test_d_maggiore_di_h_solleva(self):
        with self.assertRaises(ValueError):
            calcola_m_rd(b=300, h=500, d=600, a_s=603.19, fck=25, fyk=450)

    def test_input_negativi_sollevano(self):
        with self.assertRaises(ValueError):
            calcola_m_rd(b=-300, h=500, d=460, a_s=603, fck=25, fyk=450)
        with self.assertRaises(ValueError):
            calcola_m_rd(b=300, h=500, d=460, a_s=-603, fck=25, fyk=450)
        with self.assertRaises(ValueError):
            calcola_m_rd(b=300, h=500, d=460, a_s=603, fck=-25, fyk=450)

    def test_fck_oltre_50_solleva(self):
        with self.assertRaises(ValueError):
            calcola_m_rd(b=300, h=500, d=460, a_s=603, fck=60, fyk=450)

    def test_warn_zeta_oltre_limite(self):
        # forzo molto As per superare zeta = 0.45 ma restando in zona snervata
        # As grande -> x grande -> zeta grande. Cerchiamo As tale che zeta > 0.45 ma eps_s > eps_yd.
        # In B450C eps_yd ~ 0.00196; zeta_yield = eps_cu/(eps_cu+eps_yd) = 0.0035/(0.0035+0.00196) = 0.641.
        # Quindi per zeta tra 0.45 e ~0.641 acciaio snerva ma duttilita' insufficiente.
        # Provo As = 2200 mm2:
        # x = (2200 * 391.304)/(0.8*300*14.1667) = 860868/3400 = 253.20 mm
        # zeta = 253.20/460 = 0.550 -> snerva ma > 0.45
        res = calcola_m_rd(b=300, h=500, d=460, a_s=2200, fck=25, fyk=450)
        self.assertTrue(res.duttile_snervamento)
        self.assertFalse(res.duttile_zeta_limite)
        self.assertTrue(any("0.45" in a for a in res.avvertenze))

    def test_sezione_sovra_armata_solleva(self):
        # As enorme -> eps_s < eps_yd
        # zeta_yield ~ 0.641 (per B450C). Per zeta > 0.641 acciaio non snerva.
        # As = 3500 mm2:
        # x = (3500*391.304)/(3400) = 402.93 mm
        # zeta = 402.93/460 = 0.876 > 0.641 -> non snerva
        with self.assertRaises(ValueError) as cm:
            calcola_m_rd(b=300, h=500, d=460, a_s=3500, fck=25, fyk=450)
        self.assertIn("sovra-armata", str(cm.exception))

    def test_serializzazione_dict(self):
        res = calcola_m_rd(b=300, h=500, d=460, a_s=603, fck=25, fyk=450)
        d = res.as_dict()
        self.assertIn("input", d)
        self.assertIn("materiali", d)
        self.assertIn("geometria_interna", d)
        self.assertIn("output", d)
        self.assertIn("M_Rd_kNm", d["output"])
        self.assertIn("M_Rd_Nmm", d["output"])
        self.assertIn("riferimenti_ntc", d)

    def test_riferimenti_ntc_presenti(self):
        res = calcola_m_rd(b=300, h=500, d=460, a_s=603, fck=25, fyk=450)
        joined = "\n".join(res.riferimenti)
        self.assertIn("4.1.2", joined)
        self.assertIn("Circ. 7/2019", joined)


class TestRapportoMateriale(unittest.TestCase):
    """Verifica monotonia: aumentando As deve aumentare MRd (in zona snervata).
    Aumentando fck deve aumentare MRd. Aumentando d deve aumentare MRd."""

    def test_m_rd_cresce_con_As(self):
        m1 = calcola_m_rd(b=300, h=500, d=460, a_s=603, fck=25, fyk=450).m_rd_kNm
        m2 = calcola_m_rd(b=300, h=500, d=460, a_s=1000, fck=25, fyk=450).m_rd_kNm
        self.assertLess(m1, m2)

    def test_m_rd_cresce_con_d(self):
        m1 = calcola_m_rd(b=300, h=500, d=400, a_s=603, fck=25, fyk=450).m_rd_kNm
        m2 = calcola_m_rd(b=300, h=500, d=460, a_s=603, fck=25, fyk=450).m_rd_kNm
        self.assertLess(m1, m2)

    def test_m_rd_cresce_con_fck(self):
        # con As fissa, fck maggiore -> x minore -> z maggiore -> MRd maggiore (in zona snervata)
        m1 = calcola_m_rd(b=300, h=500, d=460, a_s=603, fck=25, fyk=450).m_rd_kNm
        m2 = calcola_m_rd(b=300, h=500, d=460, a_s=603, fck=35, fyk=450).m_rd_kNm
        self.assertLess(m1, m2)


class TestCLI(unittest.TestCase):
    def _run(self, payload):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(payload, fh)
            path = fh.name
        try:
            module_path = os.path.join(HERE, "flessione_ca.py")
            res = subprocess.run(
                [sys.executable, module_path, "--input-json", path],
                capture_output=True,
                text=True,
            )
            return res
        finally:
            os.unlink(path)

    def test_cli_ok(self):
        res = self._run(
            {"b": 300, "h": 500, "d": 460, "As": 603.19, "fck": 25, "fyk": 450}
        )
        self.assertEqual(res.returncode, 0, res.stderr)
        out = json.loads(res.stdout)
        self.assertIn("M_Rd_kNm", out["output"])
        self.assertGreater(out["output"]["M_Rd_kNm"], 100.0)

    def test_cli_campo_mancante(self):
        res = self._run({"b": 300, "h": 500})
        self.assertEqual(res.returncode, 2)
        self.assertIn("ERRORE", res.stderr)

    def test_cli_fck_invalido(self):
        res = self._run(
            {"b": 300, "h": 500, "d": 460, "As": 603, "fck": 60, "fyk": 450}
        )
        self.assertEqual(res.returncode, 2)
        self.assertIn("ERRORE", res.stderr)

    def test_cli_sovra_armata(self):
        res = self._run(
            {"b": 300, "h": 500, "d": 460, "As": 3500, "fck": 25, "fyk": 450}
        )
        self.assertEqual(res.returncode, 2)
        self.assertIn("sovra-armata", res.stderr)


if __name__ == "__main__":
    unittest.main()
