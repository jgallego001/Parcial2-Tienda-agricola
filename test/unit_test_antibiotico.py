import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelo.Antibiotico import Antibiotico

class TestAntibiotico(unittest.TestCase):
    
    def test_antibiotico_creacion(self):
        antibiotico = Antibiotico("Antibov", "500mg", "Bovinos", 60000)
        self.assertEqual(antibiotico.nombre, "Antibov")
        self.assertEqual(antibiotico.dosis, "500mg")
        self.assertEqual(antibiotico.tipo_de_animal, "Bovinos")
        self.assertEqual(antibiotico.precio, 60000)
    
    def test_antibiotico_tipos_animales(self):
        antibiotico_bovinos = Antibiotico("Antibov", "500mg", "Bovinos", 60000)
        antibiotico_porcinos = Antibiotico("Antiporc", "450mg", "Porcinos", 55000)
        self.assertEqual(antibiotico_bovinos.tipo_de_animal, "Bovinos")
        self.assertEqual(antibiotico_porcinos.tipo_de_animal, "Porcinos")

if __name__ == '__main__':
    unittest.main()