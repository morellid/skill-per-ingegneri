#!/usr/bin/env python3
"""Test per trasmittanza.py. Valori attesi calcolati a mano (legge di Fourier)
e limiti verificati sulla trascrizione del DM 26/06/2015 (Appendici A e B)."""

import unittest

from trasmittanza import (
    APP_A,
    APP_B,
    Strato,
    calcola_trasmittanza,
    _norm_zona,
)


class TestCalcoloU(unittest.TestCase):
    def test_strato_singolo(self):
        # s=0.20, lambda=0.040 -> R=5.0; R_tot=0.13+5.0+0.04=5.17; U=0.193423
        r = calcola_trasmittanza(
            [Strato("iso", 0.20, 0.040)], R_si=0.13, R_se=0.04,
            zona="E", tipo="parete_verticale", regime="riqualificazione", anno="2021",
        )
        self.assertAlmostEqual(r.R_tot, 5.17, places=6)
        self.assertAlmostEqual(r.U_W_m2K, 1.0 / 5.17, places=6)
        self.assertAlmostEqual(r.U_W_m2K, 0.1934236, places=6)

    def test_parete_multistrato_verificata(self):
        # intonaco int 0.015/0.70; muratura 0.25/0.40; EPS 0.12/0.036; intonaco est 0.015/0.90
        strati = [
            Strato("intonaco_int", 0.015, 0.70),
            Strato("muratura", 0.25, 0.40),
            Strato("eps", 0.12, 0.036),
            Strato("intonaco_est", 0.015, 0.90),
        ]
        r = calcola_trasmittanza(
            strati, R_si=0.13, R_se=0.04, zona="E",
            regime="riqualificazione", anno="2021",
        )
        r_strati = 0.015 / 0.70 + 0.25 / 0.40 + 0.12 / 0.036 + 0.015 / 0.90
        self.assertAlmostEqual(r.R_strati, r_strati, places=6)
        self.assertAlmostEqual(r.R_tot, 0.13 + r_strati + 0.04, places=6)
        self.assertAlmostEqual(r.U_W_m2K, 1.0 / (0.13 + r_strati + 0.04), places=6)
        self.assertAlmostEqual(r.U_limite_applicato, 0.28, places=6)  # zona E, B, 2021
        self.assertLess(r.U_W_m2K, 0.28)
        self.assertTrue(r.verifica_soddisfatta)

    def test_parete_non_verificata(self):
        # stessa parete con isolante piu' sottile: U > limite
        strati = [
            Strato("intonaco_int", 0.015, 0.70),
            Strato("muratura", 0.25, 0.40),
            Strato("eps", 0.08, 0.036),
            Strato("intonaco_est", 0.015, 0.90),
        ]
        r = calcola_trasmittanza(
            strati, R_si=0.13, R_se=0.04, zona="E",
            regime="riqualificazione", anno="2021",
        )
        self.assertGreater(r.U_W_m2K, 0.28)
        self.assertFalse(r.verifica_soddisfatta)

    def test_incremento_30pct_isolamento_interno(self):
        # U ~0.327 fallisce senza incremento; con +30% il limite 0.28 -> 0.364 -> passa
        strati = [
            Strato("intonaco_int", 0.015, 0.70),
            Strato("muratura", 0.25, 0.40),
            Strato("eps", 0.08, 0.036),
            Strato("intonaco_est", 0.015, 0.90),
        ]
        base = calcola_trasmittanza(
            strati, R_si=0.13, R_se=0.04, zona="E",
            regime="riqualificazione", anno="2021",
        )
        inc = calcola_trasmittanza(
            strati, R_si=0.13, R_se=0.04, zona="E",
            regime="riqualificazione", anno="2021",
            isolamento_interno_o_intercapedine=True,
        )
        self.assertFalse(base.verifica_soddisfatta)
        self.assertTrue(inc.incremento_applicato)
        self.assertAlmostEqual(inc.U_limite_applicato, 0.28 * 1.30, places=6)
        self.assertTrue(inc.verifica_soddisfatta)


class TestLimiti(unittest.TestCase):
    def test_appendice_b_parete_zone(self):
        # Tabella 1 App. B (2021): AB 0.40, C 0.36, D 0.32, E 0.28, F 0.26
        attesi = {"AB": 0.40, "C": 0.36, "D": 0.32, "E": 0.28, "F": 0.26}
        for z, u in attesi.items():
            self.assertAlmostEqual(APP_B["parete_verticale"][z][1], u, places=6)

    def test_appendice_b_copertura_2015(self):
        # Tabella 2 App. B (2015): AB 0.34, C 0.34, D 0.28, E 0.26, F 0.24
        attesi = {"AB": 0.34, "C": 0.34, "D": 0.28, "E": 0.26, "F": 0.24}
        for z, u in attesi.items():
            self.assertAlmostEqual(APP_B["copertura"][z][0], u, places=6)

    def test_appendice_a_parete_2019_2021(self):
        # Tabella 1 App. A (col.2): AB 0.43, C 0.34, D 0.29, E 0.26, F 0.24
        attesi = {"AB": 0.43, "C": 0.34, "D": 0.29, "E": 0.26, "F": 0.24}
        for z, u in attesi.items():
            self.assertAlmostEqual(APP_A["parete_verticale"][z][1], u, places=6)

    def test_regime_riferimento_usa_app_a(self):
        r = calcola_trasmittanza(
            [Strato("iso", 0.20, 0.040)], R_si=0.13, R_se=0.04, zona="D",
            tipo="parete_verticale", regime="edificio_riferimento", anno="2021",
        )
        self.assertAlmostEqual(r.U_limite_base, 0.29, places=6)  # App. A parete D col.2

    def test_norm_zona_ab(self):
        self.assertEqual(_norm_zona("A"), "AB")
        self.assertEqual(_norm_zona("b"), "AB")
        self.assertEqual(_norm_zona("A e B"), "AB")
        self.assertEqual(_norm_zona("F"), "F")


class TestRifiuti(unittest.TestCase):
    def test_nessuno_strato(self):
        with self.assertRaises(ValueError):
            calcola_trasmittanza([], R_si=0.13, R_se=0.04, zona="E")

    def test_lambda_non_positivo(self):
        with self.assertRaises(ValueError):
            calcola_trasmittanza(
                [Strato("x", 0.1, 0.0)], R_si=0.13, R_se=0.04, zona="E"
            )

    def test_spessore_negativo(self):
        with self.assertRaises(ValueError):
            calcola_trasmittanza(
                [Strato("x", -0.1, 0.04)], R_si=0.13, R_se=0.04, zona="E"
            )

    def test_rsi_mancante(self):
        with self.assertRaises(ValueError):
            calcola_trasmittanza(
                [Strato("x", 0.1, 0.04)], R_si=None, R_se=0.04, zona="E"
            )

    def test_zona_invalida(self):
        with self.assertRaises(ValueError):
            calcola_trasmittanza(
                [Strato("x", 0.1, 0.04)], R_si=0.13, R_se=0.04, zona="G"
            )

    def test_chiusura_trasparente_rifiutata(self):
        with self.assertRaises(ValueError):
            calcola_trasmittanza(
                [Strato("x", 0.1, 0.04)], R_si=0.13, R_se=0.04, zona="E",
                tipo="chiusura_trasparente",
            )

    def test_incremento_su_riferimento_rifiutato(self):
        with self.assertRaises(ValueError):
            calcola_trasmittanza(
                [Strato("x", 0.1, 0.04)], R_si=0.13, R_se=0.04, zona="E",
                regime="edificio_riferimento",
                isolamento_interno_o_intercapedine=True,
            )

    def test_anno_invalido(self):
        with self.assertRaises(ValueError):
            calcola_trasmittanza(
                [Strato("x", 0.1, 0.04)], R_si=0.13, R_se=0.04, zona="E", anno="2030"
            )


class TestAvvertenze(unittest.TestCase):
    def test_avvertenza_ponti_termici_sempre(self):
        r = calcola_trasmittanza(
            [Strato("iso", 0.20, 0.040)], R_si=0.13, R_se=0.04, zona="E",
        )
        self.assertTrue(any("ponti termici" in a for a in r.avvertenze))

    def test_avvertenza_non_climatizzato(self):
        r = calcola_trasmittanza(
            [Strato("iso", 0.20, 0.040)], R_si=0.13, R_se=0.04, zona="E",
            verso_ambiente_non_climatizzato=True,
        )
        self.assertTrue(any("non climatizzato" in a for a in r.avvertenze))


if __name__ == "__main__":
    unittest.main()
