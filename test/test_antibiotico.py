import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from modelo.Antibiotico import Antibiotico

class TestAntibiotico(unittest.TestCase):
    def test_creacion_antibiotico(self):
        a = Antibiotico("Antibov", "500mg", "Bovinos", 60000)
        self.assertEqual(a.nombre, "Antibov")
        self.assertEqual(a.dosis, "500mg")
        self.assertEqual(a.tipo_de_animal, "Bovinos")
        self.assertEqual(a.valor, 60000)

    def test_str(self):
        a = Antibiotico("Antiporc", "300mg", "Porcinos", 45000)
        texto = str(a)
        self.assertIn("Antibiotico", texto)
        self.assertIn("Porcinos", texto)
        self.assertIn("45000", texto)

if __name__ == '__main__':
    unittest.main()