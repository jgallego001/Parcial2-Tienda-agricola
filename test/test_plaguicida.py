import unittest
from modelo.Plaguicida import Plaguicida

class TestPlaguicida(unittest.TestCase):
    def test_creacion_plaguicida(self):
        p = Plaguicida("ICA001", "Plagox", 15, 30000, 20)
        self.assertEqual(p.registro_ica, "ICA001")
        self.assertEqual(p.nombre, "Plagox")
        self.assertEqual(p.freq_de_aplicacion, 15)
        self.assertEqual(p.valor, 30000)
        self.assertEqual(p.periodo_de_carencia, 20)

if __name__ == '__main__':
    unittest.main()