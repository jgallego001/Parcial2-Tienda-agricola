import unittest
from modelo.Fertilizante import Fertilizante

class TestFertilizante(unittest.TestCase):
    def test_creacion_fertilizante(self):
        f = Fertilizante("ICA002", "NitroPlus", 30, 45000, "2025-10-15")
        self.assertEqual(f.nombre, "NitroPlus")
        self.assertEqual(f.valor, 45000)
        self.assertEqual(f.fecha_ultima_aplicacion, "2025-10-15")

if __name__ == '__main__':
    unittest.main()