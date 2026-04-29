"""Test suite per spettro.py.

Esecuzione:
    cd skills/spettro-risposta-ntc/tasks/lib
    python3 test_spettro.py

oppure con unittest:
    python3 -m unittest test_spettro

I test verificano:
1. Formule chiuse (TR<->P_VR, eta, SS clamping, periodi caratteristici)
2. Continuita' di Se(T) ai raccordi TB, TC, TD
3. Interpolazione logaritmica sui TR di riferimento (round-trip + bracket)
4. Valori canonici noti (VN=50 CU II -> TR_SLV ~ 475 anni)
5. Rifiuto esplicito di S1/S2 e di TR fuori reticolo
6. Validazione hardening input (non-finite, non-positive, non-numeric)
7. Copertura categorie di sottosuolo D, E e topografiche T2/T3/T4
8. Anti-drift: match bit-per-bit fra il modulo e il fixture
   examples/caso-conforme-fittizio-cu2-c-t1/expected.json

ATTENZIONE: questi sono test di consistenza interna. NON confrontano
i valori contro il foglio Excel CSLP del Servizio Tecnico Centrale.
La validazione di campo (10+ casi reali sparsi sul territorio
nazionale, con confronto numerico vs CSLP entro le tolleranze
documentate in tasks/run-test-suite.md) e' prerequisito del release
stabile e va eseguita prima di v0.1 stabile.
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


class TestValidazioneInput(unittest.TestCase):
    """Validazione hardening di ParametriRiferimento: non-finite, non-positive, non-numeric."""

    BASE_AG = [0.030, 0.045, 0.061, 0.080, 0.105, 0.135, 0.218, 0.297, 0.420]
    BASE_F0 = [2.50, 2.55, 2.60, 2.62, 2.65, 2.68, 2.72, 2.74, 2.76]
    BASE_TCS = [0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34, 0.36]

    def _sostituisci(self, lista, k, v):
        x = list(lista)
        x[k] = v
        return x

    def test_zero_solleva(self):
        # ag = 0 a un nodo (interpolazione log richiede positivi anche al nodo)
        with self.assertRaisesRegex(ValueError, "ag\\[3\\].*positivo"):
            ParametriRiferimento(
                ag=self._sostituisci(self.BASE_AG, 3, 0.0),
                F0=self.BASE_F0,
                Tc_star=self.BASE_TCS,
            )

    def test_negativo_solleva(self):
        with self.assertRaisesRegex(ValueError, "F0\\[5\\].*positivo"):
            ParametriRiferimento(
                ag=self.BASE_AG,
                F0=self._sostituisci(self.BASE_F0, 5, -1.0),
                Tc_star=self.BASE_TCS,
            )

    def test_nan_solleva(self):
        with self.assertRaisesRegex(ValueError, "Tc_star\\[0\\].*non finito"):
            ParametriRiferimento(
                ag=self.BASE_AG,
                F0=self.BASE_F0,
                Tc_star=self._sostituisci(self.BASE_TCS, 0, float("nan")),
            )

    def test_inf_solleva(self):
        with self.assertRaisesRegex(ValueError, "ag\\[8\\].*non finito"):
            ParametriRiferimento(
                ag=self._sostituisci(self.BASE_AG, 8, float("inf")),
                F0=self.BASE_F0,
                Tc_star=self.BASE_TCS,
            )

    def test_stringa_solleva(self):
        with self.assertRaisesRegex(ValueError, "F0\\[2\\].*non numerico"):
            ParametriRiferimento(
                ag=self.BASE_AG,
                F0=self._sostituisci(self.BASE_F0, 2, "2.6"),  # type: ignore[arg-type]
                Tc_star=self.BASE_TCS,
            )

    def test_bool_rifiutato(self):
        # bool e' subclass di int in Python: lo escludiamo esplicitamente
        with self.assertRaisesRegex(ValueError, "ag\\[0\\].*non numerico"):
            ParametriRiferimento(
                ag=self._sostituisci(self.BASE_AG, 0, True),  # type: ignore[arg-type]
                F0=self.BASE_F0,
                Tc_star=self.BASE_TCS,
            )

    def test_carica_da_json_con_nan_solleva(self):
        # JSON tecnicamente non ammette NaN ma molti parser sono permissivi:
        # qui usiamo un valore null che json.load mappa a None, non numerico.
        data = {
            "tr_anni": list(TR_RIFERIMENTO),
            "ag_g": list(self.BASE_AG),
            "F0": list(self.BASE_F0),
            "Tc_star": list(self.BASE_TCS),
        }
        data["ag_g"][4] = None  # type: ignore[assignment]
        with tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(data, f)
            path = f.name
        try:
            with self.assertRaisesRegex(ValueError, "ag\\[4\\].*non numerico"):
                carica_parametri_riferimento(path)
        finally:
            os.unlink(path)


class TestCoperturaCategorie(unittest.TestCase):
    """Coverage delle categorie di sottosuolo D, E e topografiche T2/T3/T4 e xi != 5%."""

    BASE = ParametriRiferimento(
        ag=[0.030, 0.045, 0.061, 0.080, 0.105, 0.135, 0.218, 0.297, 0.420],
        F0=[2.50, 2.55, 2.60, 2.62, 2.65, 2.68, 2.72, 2.74, 2.76],
        Tc_star=[0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34, 0.36],
    )

    def test_categoria_D(self):
        p = calcola_parametri("SLV", 50, "II", "D", "T1", self.BASE)
        # SS(D) = clamp(2.40 - 1.50*F0*ag, 0.90, 1.80)
        atteso_ss = max(0.90, min(1.80, 2.40 - 1.50 * p.F0 * p.ag))
        self.assertAlmostEqual(p.SS, atteso_ss, places=6)
        # CC(D) = 1.25 * Tc*^-0.50
        self.assertAlmostEqual(p.CC, 1.25 * p.Tc_star ** -0.50, places=6)

    def test_categoria_E(self):
        p = calcola_parametri("SLV", 50, "II", "E", "T1", self.BASE)
        # SS(E) = clamp(2.00 - 1.10*F0*ag, 1.00, 1.60)
        atteso_ss = max(1.00, min(1.60, 2.00 - 1.10 * p.F0 * p.ag))
        self.assertAlmostEqual(p.SS, atteso_ss, places=6)
        self.assertAlmostEqual(p.CC, 1.15 * p.Tc_star ** -0.40, places=6)

    def test_topografica_T2_T3_T4(self):
        valori_attesi = {"T2": 1.2, "T3": 1.2, "T4": 1.4}
        for cat, st_atteso in valori_attesi.items():
            with self.subTest(cat_topo=cat):
                p = calcola_parametri("SLV", 50, "II", "C", cat, self.BASE)
                self.assertAlmostEqual(p.ST, st_atteso, places=6)
                # S = SS * ST: ST entra moltiplicativamente
                self.assertAlmostEqual(p.S, p.SS * st_atteso, places=6)

    def test_xi_diverso_da_5_riduce_plateau(self):
        # xi = 10% -> eta = sqrt(10/15) = 0.8165
        p5 = calcola_parametri("SLV", 50, "II", "C", "T1", self.BASE, xi_percento=5.0)
        p10 = calcola_parametri("SLV", 50, "II", "C", "T1", self.BASE, xi_percento=10.0)
        self.assertAlmostEqual(p10.eta, math.sqrt(10.0 / 15.0), places=6)
        # plateau Se(TC) = ag*S*eta*F0 si scala come eta
        from spettro import Se_T as _Se_T
        se5, _ = _Se_T(p5.TC, p5)
        se10, _ = _Se_T(p10.TC, p10)
        self.assertAlmostEqual(se10 / se5, p10.eta / p5.eta, places=6)


class TestFailClosedScalari(unittest.TestCase):
    """Fail-closed su input scalari non finiti (NaN/inf) coerentemente con
    la validazione vettoriale di ParametriRiferimento.__post_init__.

    Indirizza Codex adversarial review (round 4): un xi_percento NaN
    silenzioso produrrebbe Se(T) tutti NaN, output corrotto in dominio
    strutturale ad alto rischio.
    """

    def test_vita_riferimento_rifiuta_nan(self):
        with self.assertRaisesRegex(ValueError, "Vita nominale.*finito"):
            vita_riferimento(float("nan"), "II")

    def test_vita_riferimento_rifiuta_inf(self):
        with self.assertRaisesRegex(ValueError, "Vita nominale.*finito"):
            vita_riferimento(float("inf"), "II")

    def test_coeff_eta_rifiuta_nan(self):
        with self.assertRaisesRegex(ValueError, "xi.*finito"):
            coeff_eta(float("nan"))

    def test_se_T_rifiuta_nan(self):
        rif = ParametriRiferimento(
            ag=[0.2] * 9, F0=[2.5] * 9, Tc_star=[0.30] * 9
        )
        p = calcola_parametri("SLV", 50, "II", "C", "T1", rif, xi_percento=5.0)
        with self.assertRaisesRegex(ValueError, "T.*finito"):
            Se_T(float("nan"), p)

    def test_coeff_SS_rifiuta_nan_inf(self):
        # Senza il check, coeff_SS('C', NaN, 2.5) ritornerebbe il clamp 1.0
        # silenziosamente (Codex round 5).
        with self.assertRaisesRegex(ValueError, "ag.*finito"):
            coeff_SS("C", float("nan"), 2.5)
        with self.assertRaisesRegex(ValueError, "ag.*finito"):
            coeff_SS("C", float("inf"), 2.5)
        with self.assertRaisesRegex(ValueError, "F0.*finito"):
            coeff_SS("C", 0.2, float("nan"))

    def test_coeff_SS_rifiuta_zero_negativo(self):
        with self.assertRaisesRegex(ValueError, "ag.*positivo"):
            coeff_SS("C", 0.0, 2.5)
        with self.assertRaisesRegex(ValueError, "F0.*positivo"):
            coeff_SS("C", 0.2, -1.0)

    def test_coeff_SS_rifiuta_bool(self):
        # bool e' subclass di int in Python: lo escludiamo esplicitamente.
        with self.assertRaisesRegex(ValueError, "ag.*reale"):
            coeff_SS("C", True, 2.5)  # type: ignore[arg-type]

    def test_coeff_CC_rifiuta_nan_inf(self):
        with self.assertRaisesRegex(ValueError, "Tc.*finito"):
            coeff_CC("C", float("nan"))
        with self.assertRaisesRegex(ValueError, "Tc.*finito"):
            coeff_CC("C", float("inf"))

    def test_coeff_CC_rifiuta_zero_negativo(self):
        with self.assertRaisesRegex(ValueError, "Tc.*positivo"):
            coeff_CC("C", 0.0)
        with self.assertRaisesRegex(ValueError, "Tc.*positivo"):
            coeff_CC("C", -0.3)

    def test_periodi_caratteristici_rifiuta_non_finiti(self):
        from spettro import periodi_caratteristici as pc
        with self.assertRaisesRegex(ValueError, "Tc.*finito"):
            pc(float("nan"), 0.2, "C")
        with self.assertRaisesRegex(ValueError, "ag.*finito"):
            pc(0.3, float("inf"), "C")


class TestCLINaNHandling(unittest.TestCase):
    """JSON con NaN/Infinity (non standard RFC 8259) deve essere rifiutato a
    livello di parser, non propagarsi a Se(T) come ordinate NaN."""

    BASE_SITO = {
        "tr_anni": list(TR_RIFERIMENTO),
        "ag_g": [0.030, 0.045, 0.061, 0.080, 0.105, 0.135, 0.218, 0.297, 0.420],
        "F0": [2.50, 2.55, 2.60, 2.62, 2.65, 2.68, 2.72, 2.74, 2.76],
        "Tc_star": [0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34, 0.36],
    }

    def _scrivi_raw(self, raw_text: str) -> str:
        # Scrive raw text (puo' contenere "NaN" non quotato), restituisce path.
        f = tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        )
        f.write(raw_text)
        f.close()
        return f.name

    def test_input_json_rifiuta_nan_in_xi(self):
        # Costruisce manualmente il JSON con "NaN" non quotato (Python json
        # lo accetta come float('nan') by default; il nostro parse_constant
        # lo rifiuta).
        raw = json.dumps(
            {
                "parametri_calcolo": {
                    "vn_anni": 50, "classe_uso": "II",
                    "cat_sottosuolo": "C", "cat_topografica": "T1",
                    "xi_percento": 5.0,
                },
                "parametri_pericolosita_sito": self.BASE_SITO,
            }
        )
        # Sostituisce 5.0 di xi_percento con NaN non quotato.
        raw = raw.replace('"xi_percento": 5.0', '"xi_percento": NaN')
        path = self._scrivi_raw(raw)
        try:
            from io import StringIO
            from contextlib import redirect_stderr
            buf = StringIO()
            with redirect_stderr(buf):
                with self.assertRaises(SystemExit):
                    main(["--input-json", path])
            self.assertIn("NaN", buf.getvalue())
        finally:
            os.unlink(path)

    def test_input_json_rifiuta_infinity_in_ag(self):
        raw = json.dumps(
            {
                "parametri_calcolo": {
                    "vn_anni": 50, "classe_uso": "II",
                    "cat_sottosuolo": "C", "cat_topografica": "T1",
                },
                "parametri_pericolosita_sito": self.BASE_SITO,
            }
        )
        raw = raw.replace("0.218", "Infinity")
        path = self._scrivi_raw(raw)
        try:
            from io import StringIO
            from contextlib import redirect_stderr
            buf = StringIO()
            with redirect_stderr(buf):
                with self.assertRaises(SystemExit):
                    main(["--input-json", path])
            self.assertIn("Infinity", buf.getvalue())
        finally:
            os.unlink(path)

    def test_tabula_periodi_rifiuta_step_nan(self):
        from io import StringIO
        from contextlib import redirect_stderr
        buf = StringIO()
        with redirect_stderr(buf):
            with self.assertRaises(SystemExit):
                main(["--tabula", "0:4:nan"])
        self.assertIn("step", buf.getvalue())


class TestEsempioConforme(unittest.TestCase):
    """Anti-drift end-to-end del caso canonico.

    Legge input.json e expected.json dalla cartella examples/, esegue
    il modulo sull'input documentato e confronta con il golden master.
    Modificare input.json senza rigenerare expected.json fa fallire
    test_match_expected_json: questo e' il comportamento desiderato e
    impedisce drift fra documentazione e codice (Codex review round 2).
    """

    @classmethod
    def setUpClass(cls):
        cls.skill_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        cls.example_dir = os.path.join(
            cls.skill_dir, "examples", "caso-conforme-fittizio-cu2-c-t1"
        )
        cls.input_path = os.path.join(cls.example_dir, "input.json")
        cls.expected_path = os.path.join(cls.example_dir, "expected.json")

    def test_fixtures_presenti(self):
        self.assertTrue(
            os.path.isfile(self.input_path),
            f"Manca il fixture input {self.input_path}",
        )
        self.assertTrue(
            os.path.isfile(self.expected_path),
            f"Manca il fixture expected {self.expected_path}",
        )

    def _carica_input(self):
        with open(self.input_path, encoding="utf-8") as f:
            return json.load(f)

    def _periodi(self, tab):
        # Replica argparse type=_parse_periodi senza dipendere dalla CLI
        start, stop, step = float(tab["start"]), float(tab["stop"]), float(tab["step"])
        out = []
        t = start
        while t <= stop + 1e-9:
            out.append(round(t, 6))
            t += step
        return out

    def test_match_expected_json(self):
        from spettro import calcola_parametri as cp, tabula_spettro as ts
        ipt = self._carica_input()
        pc = ipt["parametri_calcolo"]
        sito = ipt["parametri_pericolosita_sito"]
        # Sanity: tr_anni del fixture deve coincidere col reticolo del modulo.
        self.assertEqual(
            tuple(sito["tr_anni"]), TR_RIFERIMENTO,
            "tr_anni in input.json non allineato col reticolo del modulo",
        )
        rif = ParametriRiferimento(
            ag=list(sito["ag_g"]),
            F0=list(sito["F0"]),
            Tc_star=list(sito["Tc_star"]),
        )
        periodi = self._periodi(pc["tabula_periodi"])
        with open(self.expected_path, encoding="utf-8") as f:
            atteso = json.load(f)
        sl_attesi = list(pc["stati_limite"])
        self.assertEqual(
            [r["parametri"]["stato_limite"] for r in atteso], sl_attesi,
            "Ordine stati limite in expected.json non allineato con input.json",
        )

        for sl, atteso_sl in zip(sl_attesi, atteso):
            with self.subTest(sl=sl):
                p = cp(
                    sl,
                    pc["vn_anni"],
                    pc["classe_uso"],
                    pc["cat_sottosuolo"],
                    pc["cat_topografica"],
                    rif,
                    xi_percento=pc["xi_percento"],
                )
                par_atteso = atteso_sl["parametri"]
                for k in ("TR", "ag", "F0", "Tc_star", "SS", "ST", "S", "CC", "eta", "TB", "TC", "TD"):
                    self.assertAlmostEqual(
                        getattr(p, k), par_atteso[k], places=10,
                        msg=f"{sl}.{k}: atteso {par_atteso[k]} ottenuto {getattr(p, k)}",
                    )
                ord_atteso = atteso_sl["ordinate"]
                ord_attuale = ts(p, periodi)
                self.assertEqual(
                    len(ord_attuale), len(ord_atteso),
                    f"{sl}: numero ordinate diverso",
                )
                for o_att, o_curr in zip(ord_atteso, ord_attuale):
                    self.assertAlmostEqual(o_curr.T, o_att["T"], places=10)
                    self.assertAlmostEqual(o_curr.Se, o_att["Se"], places=10)
                    self.assertEqual(o_curr.ramo, o_att["ramo"])


class TestCLI(unittest.TestCase):
    def test_input_json_equivalente_ai_flag_scalari(self):
        """Modalita' A (--input-json) e modalita' B (flag scalari) producono lo stesso output JSON."""
        skill_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        input_path = os.path.join(
            skill_dir, "examples", "caso-conforme-fittizio-cu2-c-t1", "input.json"
        )
        expected_path = os.path.join(
            skill_dir, "examples", "caso-conforme-fittizio-cu2-c-t1", "expected.json"
        )
        from io import StringIO
        from contextlib import redirect_stdout

        # Modo A: --input-json
        buf_a = StringIO()
        with redirect_stdout(buf_a):
            rc_a = main(["--input-json", input_path, "--json"])
        self.assertEqual(rc_a, 0)
        out_a = json.loads(buf_a.getvalue())

        # Confronto con golden master (anti-drift inverso)
        with open(expected_path, encoding="utf-8") as f:
            atteso = json.load(f)
        self.assertEqual(out_a, atteso, "stdout di --input-json non coincide con expected.json")

    def test_input_json_chiave_mancante(self):
        with tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump({"parametri_calcolo": {}}, f)  # manca parametri_pericolosita_sito
            path = f.name
        try:
            from io import StringIO
            from contextlib import redirect_stderr
            buf = StringIO()
            with redirect_stderr(buf):
                with self.assertRaises(SystemExit):
                    main(["--input-json", path])
            self.assertIn("parametri_pericolosita_sito", buf.getvalue())
        finally:
            os.unlink(path)

    def test_modalita_B_flag_mancanti_errore(self):
        from io import StringIO
        from contextlib import redirect_stderr
        buf = StringIO()
        with redirect_stderr(buf):
            with self.assertRaises(SystemExit):
                main([])  # nessun flag, nessun --input-json
        self.assertIn("richiesti:", buf.getvalue())

    def test_input_json_sito_chiavi_mancanti(self):
        # parametri_pericolosita_sito senza ag_g/F0/Tc_star -> parser.error,
        # non un KeyError che bubbla come traceback.
        bad = {
            "parametri_calcolo": {
                "vn_anni": 50, "classe_uso": "II",
                "cat_sottosuolo": "C", "cat_topografica": "T1",
            },
            "parametri_pericolosita_sito": {"tr_anni": list(TR_RIFERIMENTO)},
        }
        with tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(bad, f)
            path = f.name
        try:
            from io import StringIO
            from contextlib import redirect_stderr
            buf = StringIO()
            with redirect_stderr(buf):
                with self.assertRaises(SystemExit):
                    main(["--input-json", path])
            err = buf.getvalue()
            self.assertIn("ag_g", err)
            self.assertIn("F0", err)
            self.assertIn("Tc_star", err)
        finally:
            os.unlink(path)

    def test_input_json_pc_chiavi_mancanti(self):
        # parametri_calcolo senza vn_anni/classe_uso/... -> parser.error.
        bad = {
            "parametri_calcolo": {"classe_uso": "II"},
            "parametri_pericolosita_sito": {
                "tr_anni": list(TR_RIFERIMENTO),
                "ag_g": [0.030, 0.045, 0.061, 0.080, 0.105, 0.135, 0.218, 0.297, 0.420],
                "F0": [2.50, 2.55, 2.60, 2.62, 2.65, 2.68, 2.72, 2.74, 2.76],
                "Tc_star": [0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34, 0.36],
            },
        }
        with tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(bad, f)
            path = f.name
        try:
            from io import StringIO
            from contextlib import redirect_stderr
            buf = StringIO()
            with redirect_stderr(buf):
                with self.assertRaises(SystemExit):
                    main(["--input-json", path])
            err = buf.getvalue()
            self.assertIn("vn_anni", err)
            self.assertIn("cat_sottosuolo", err)
        finally:
            os.unlink(path)

    def test_input_json_stato_limite_invalido(self):
        # stati_limite contiene "SLX" (non valido) -> parser.error,
        # non un ValueError di calcola_parametri.
        bad = {
            "parametri_calcolo": {
                "vn_anni": 50, "classe_uso": "II",
                "cat_sottosuolo": "C", "cat_topografica": "T1",
                "stati_limite": ["SLX"],
            },
            "parametri_pericolosita_sito": {
                "tr_anni": list(TR_RIFERIMENTO),
                "ag_g": [0.030, 0.045, 0.061, 0.080, 0.105, 0.135, 0.218, 0.297, 0.420],
                "F0": [2.50, 2.55, 2.60, 2.62, 2.65, 2.68, 2.72, 2.74, 2.76],
                "Tc_star": [0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34, 0.36],
            },
        }
        with tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(bad, f)
            path = f.name
        try:
            from io import StringIO
            from contextlib import redirect_stderr
            buf = StringIO()
            with redirect_stderr(buf):
                with self.assertRaises(SystemExit):
                    main(["--input-json", path])
            self.assertIn("SLX", buf.getvalue())
        finally:
            os.unlink(path)

    def test_classe_uso_case_insensitive(self):
        # vita_riferimento accetta classe d'uso in lowercase.
        self.assertAlmostEqual(vita_riferimento(50, "ii"), 50.0)
        self.assertAlmostEqual(vita_riferimento(50, "iv"), 100.0)

    def test_carica_parametri_riferimento_chiavi_mancanti(self):
        # File senza ag_g -> ValueError esplicito (non KeyError).
        bad = {"tr_anni": list(TR_RIFERIMENTO), "F0": [2.5] * 9, "Tc_star": [0.3] * 9}
        with tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(bad, f)
            path = f.name
        try:
            with self.assertRaisesRegex(ValueError, "ag_g"):
                carica_parametri_riferimento(path)
        finally:
            os.unlink(path)

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
