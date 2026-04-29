"""Test suite per spettro.py.

Esecuzione:
    cd skills/spettro-risposta-ntc/tasks/lib
    python3 test_spettro.py

oppure con unittest:
    python3 -m unittest test_spettro

I test verificano:
1. Formule chiuse (TR<->P_VR, eta, SS clamping, periodi caratteristici)
2. Continuita' di Se(T) ai raccordi TB, TC, TD
3. Interpolazione logaritmica sui TR di riferimento (round-trip + monotonia)
4. Valori canonici noti (VN=50 CU II -> TR_SLV ~ 475 anni)
5. Rifiuto esplicito di S1/S2 e di TR fuori reticolo

Per i casi di confronto numerico vs foglio Excel CSLP (validazione di
campo prima del release v1.0) si fa riferimento ai dataset documentati
in examples/. Il presente file copre la consistenza interna delle
formule e i casi limite.
"""

from __future__ import annotations

import json
import math
import os
import tempfile
import unittest

from spettro import (
    P_VR,
    TR_RIFERIMENTO,
    ParametriRiferimento,
    Se_T,
    calcola_parametri,
    carica_parametri_riferimento,
    coeff_CC,
    coeff_SS,
    coeff_eta,
    main,
    parametri_al_TR,
    periodi_caratteristici,
    tempi_ritorno_per_stati_limite,
    tempo_ritorno,
    vita_riferimento,
    _interpola_log,
)


class TestVitaTR(unittest.TestCase):
    def test_vita_riferimento_classe_uso(self):
        # VN=50 anni
        self.assertAlmostEqual(vita_riferimento(50, "I"), 35.0)  # 50*0.7=35
        self.assertAlmostEqual(vita_riferimento(50, "II"), 50.0)
        self.assertAlmostEqual(vita_riferimento(50, "III"), 75.0)
        self.assertAlmostEqual(vita_riferimento(50, "IV"), 100.0)
        # min 35 anni: VN=10 CU I -> 7 -> 35
        self.assertAlmostEqual(vita_riferimento(10, "I"), 35.0)

    def test_inverso_pvr_tr(self):
        # P_VR = 1 - exp(-VR/TR) -> TR = -VR/ln(1-P_VR)
        vr = 50.0
        for p in (0.1, 0.05, 0.63, 0.81):
            tr = tempo_ritorno(vr, p)
            self.assertAlmostEqual(1.0 - math.exp(-vr / tr), p)

    def test_tr_canonici_vn50_cu2(self):
        # Caso canonico costruzione ordinaria: VR=50.
        trs = tempi_ritorno_per_stati_limite(50, "II")
        self.assertAlmostEqual(trs["SLO"], 30.11, delta=0.05)
        self.assertAlmostEqual(trs["SLD"], 50.29, delta=0.05)
        self.assertAlmostEqual(trs["SLV"], 474.56, delta=0.5)
        self.assertAlmostEqual(trs["SLC"], 974.79, delta=1.0)


class TestCoeffSottosuolo(unittest.TestCase):
    def test_SS_categoria_A(self):
        self.assertEqual(coeff_SS("A", 0.3, 2.5), 1.0)

    def test_SS_clamping(self):
        # cat C: SS = clamp(1.70 - 0.6*F0*ag, 1.00, 1.50)
        # con ag=0.05 F0=2.0 -> 1.70 - 0.06 = 1.64 -> clamp 1.50
        self.assertAlmostEqual(coeff_SS("C", 0.05, 2.0), 1.50)
        # con ag=0.5 F0=2.5 -> 1.70 - 0.75 = 0.95 -> clamp 1.00
        self.assertAlmostEqual(coeff_SS("C", 0.5, 2.5), 1.00)
        # caso intermedio: ag=0.2 F0=2.5 -> 1.70 - 0.30 = 1.40
        self.assertAlmostEqual(coeff_SS("C", 0.2, 2.5), 1.40)

    def test_SS_S1_S2_rifiutate(self):
        with self.assertRaises(ValueError):
            coeff_SS("S1", 0.2, 2.5)
        with self.assertRaises(ValueError):
            coeff_SS("S2", 0.2, 2.5)

    def test_SS_categoria_invalida(self):
        with self.assertRaises(ValueError):
            coeff_SS("X", 0.2, 2.5)

    def test_CC_formule(self):
        # cat A -> 1.0
        self.assertEqual(coeff_CC("A", 0.3), 1.0)
        # cat B con Tc*=0.3 -> 1.10 * 0.3^-0.20 ~ 1.376
        self.assertAlmostEqual(coeff_CC("B", 0.3), 1.10 * 0.3 ** -0.20, places=8)
        # cat D con Tc*=0.3 -> 1.25 * 0.3^-0.50 ~ 2.282
        self.assertAlmostEqual(coeff_CC("D", 0.3), 1.25 * 0.3 ** -0.50, places=8)


class TestEta(unittest.TestCase):
    def test_eta_5_percento(self):
        self.assertAlmostEqual(coeff_eta(5.0), 1.0)

    def test_eta_clamp_minimo(self):
        # xi -> infinito -> eta -> 0; clamp a 0.55
        self.assertAlmostEqual(coeff_eta(1000), 0.55)


class TestPeriodi(unittest.TestCase):
    def test_TB_TC_TD(self):
        cc, tb, tc, td = periodi_caratteristici(0.3, 0.2, "C")
        # TC = CC * Tc*
        self.assertAlmostEqual(tc, cc * 0.3)
        # TB = TC/3
        self.assertAlmostEqual(tb, tc / 3.0)
        # TD = 4*ag/g + 1.6
        self.assertAlmostEqual(td, 4.0 * 0.2 + 1.6)


class TestInterpolazione(unittest.TestCase):
    def test_round_trip_su_nodo(self):
        # Su ciascuno dei 9 TR di riferimento il valore interpolato
        # deve coincidere col valore di input.
        vals = [0.030, 0.045, 0.061, 0.080, 0.105, 0.135, 0.218, 0.297, 0.420]
        for tr_k, v_atteso in zip(TR_RIFERIMENTO, vals):
            v = _interpola_log(float(tr_k), TR_RIFERIMENTO, vals)
            self.assertAlmostEqual(v, v_atteso, places=10)

    def test_interp_tra_due_nodi(self):
        # Caso lineare in log-log: due nodi T1=100, T2=400 con v1=0.1, v2=0.4
        # A T*=200: log(v) = log(0.1) + log(4) * log(2)/log(4) = log(0.1) + log(2) = log(0.2)
        tr_rif = (100.0, 400.0)
        vals = (0.1, 0.4)
        v = _interpola_log(200.0, tr_rif, vals)
        self.assertAlmostEqual(v, 0.2, places=6)

    def test_fuori_reticolo_solleva_errore(self):
        vals = [0.030, 0.045, 0.061, 0.080, 0.105, 0.135, 0.218, 0.297, 0.420]
        with self.assertRaises(ValueError):
            _interpola_log(15.0, TR_RIFERIMENTO, vals)
        with self.assertRaises(ValueError):
            _interpola_log(3000.0, TR_RIFERIMENTO, vals)


class TestRaccordiSeT(unittest.TestCase):
    """Continuita' di Se(T) ai raccordi TB, TC, TD."""

    def setUp(self):
        # Riferimento: stesso valore su tutti i 9 TR (input artificiale)
        self.rif = ParametriRiferimento(
            ag=[0.2] * 9, F0=[2.5] * 9, Tc_star=[0.30] * 9
        )

    def test_continuita_TB(self):
        p = calcola_parametri("SLV", 50, "II", "C", "T1", self.rif, xi_percento=5.0)
        eps = 1e-6
        se_giu, _ = Se_T(p.TB - eps, p)
        se_su, _ = Se_T(p.TB + eps, p)
        self.assertAlmostEqual(se_giu, se_su, places=4)
        # plateau: ag*S*eta*F0
        self.assertAlmostEqual(se_su, p.ag * p.S * p.eta * p.F0, places=6)

    def test_continuita_TC(self):
        p = calcola_parametri("SLV", 50, "II", "C", "T1", self.rif, xi_percento=5.0)
        eps = 1e-6
        se_giu, _ = Se_T(p.TC - eps, p)
        se_su, _ = Se_T(p.TC + eps, p)
        self.assertAlmostEqual(se_giu, se_su, places=4)

    def test_continuita_TD(self):
        p = calcola_parametri("SLV", 50, "II", "C", "T1", self.rif, xi_percento=5.0)
        eps = 1e-6
        se_giu, _ = Se_T(p.TD - eps, p)
        se_su, _ = Se_T(p.TD + eps, p)
        self.assertAlmostEqual(se_giu, se_su, places=6)

    def test_Se_T_zero(self):
        # In T=0 -> Se = ag*S (NTC eq. 3.2.4 a T=0)
        p = calcola_parametri("SLV", 50, "II", "C", "T1", self.rif, xi_percento=5.0)
        se, ramo = Se_T(0.0, p)
        self.assertAlmostEqual(se, p.ag * p.S, places=6)
        self.assertEqual(ramo, "0-TB")

    def test_Se_T_T_grande(self):
        p = calcola_parametri("SLV", 50, "II", "C", "T1", self.rif, xi_percento=5.0)
        se, ramo = Se_T(10.0, p)
        # ramo TD-inf
        self.assertEqual(ramo, "TD-inf")
        atteso = p.ag * p.S * p.eta * p.F0 * (p.TC * p.TD / 100.0)
        self.assertAlmostEqual(se, atteso, places=8)


class TestPipelineEndToEnd(unittest.TestCase):
    def test_calcola_parametri_struttura(self):
        rif = ParametriRiferimento(
            ag=[0.030, 0.045, 0.061, 0.080, 0.105, 0.135, 0.218, 0.297, 0.420],
            F0=[2.50, 2.55, 2.60, 2.62, 2.65, 2.68, 2.72, 2.74, 2.76],
            Tc_star=[0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34, 0.36],
        )
        p = calcola_parametri("SLV", 50, "II", "C", "T1", rif)
        # TR ~ 475 anni
        self.assertAlmostEqual(p.TR, 474.56, delta=0.5)
        # i parametri al TR=475 sono molto vicini al valore al nodo k=475
        self.assertAlmostEqual(p.ag, 0.218, delta=0.001)
        self.assertAlmostEqual(p.F0, 2.72, delta=0.01)
        self.assertAlmostEqual(p.Tc_star, 0.32, delta=0.005)
        # ST=1.0 (T1) -> S = SS
        self.assertAlmostEqual(p.S, p.SS)


class TestIO(unittest.TestCase):
    def test_carica_parametri_riferimento(self):
        data = {
            "tr_anni": list(TR_RIFERIMENTO),
            "ag_g": [0.030, 0.045, 0.061, 0.080, 0.105, 0.135, 0.218, 0.297, 0.420],
            "F0": [2.50, 2.55, 2.60, 2.62, 2.65, 2.68, 2.72, 2.74, 2.76],
            "Tc_star": [0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34, 0.36],
        }
        with tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(data, f)
            path = f.name
        try:
            rif = carica_parametri_riferimento(path)
            self.assertEqual(len(rif.ag), 9)
            self.assertAlmostEqual(rif.ag[6], 0.218)
        finally:
            os.unlink(path)

    def test_lunghezza_errata_solleva(self):
        with self.assertRaises(ValueError):
            ParametriRiferimento(ag=[0.1] * 8, F0=[2.5] * 9, Tc_star=[0.3] * 9)


class TestCLI(unittest.TestCase):
    def test_main_su_stato_singolo(self):
        data = {
            "tr_anni": list(TR_RIFERIMENTO),
            "ag_g": [0.030, 0.045, 0.061, 0.080, 0.105, 0.135, 0.218, 0.297, 0.420],
            "F0": [2.50, 2.55, 2.60, 2.62, 2.65, 2.68, 2.72, 2.74, 2.76],
            "Tc_star": [0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34, 0.36],
        }
        with tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(data, f)
            path = f.name
        try:
            rc = main(
                [
                    "--tr-riferimento",
                    path,
                    "--vn",
                    "50",
                    "--classe-uso",
                    "II",
                    "--cat-sottosuolo",
                    "C",
                    "--cat-topografica",
                    "T1",
                    "--stato-limite",
                    "SLV",
                    "--json",
                ]
            )
            self.assertEqual(rc, 0)
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
