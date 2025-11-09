import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelo.Plaguicida import Plaguicida
from modelo.Fertilizante import Fertilizante
from modelo.ProductoDeControl import ProductoDeControl

class TestProductos(unittest.TestCase):
    
    def test_plaguicida_creacion(self):
        plaga = Plaguicida("ICA001", "Plagox", 15, 30000, 20)
        self.assertEqual(plaga.registro_ica, "ICA001")
        self.assertEqual(plaga.nombre, "Plagox")
        self.assertEqual(plaga.freq_de_aplicacion, 15)
        self.assertEqual(plaga.valor, 30000)
        self.assertEqual(plaga.periodo_de_carencia, 20)
    
    def test_fertilizante_creacion(self):
        fertilizante = Fertilizante("ICA002", "NitroPlus", 30, 45000, "2025-10-15")
        self.assertEqual(fertilizante.registro_ica, "ICA002")
        self.assertEqual(fertilizante.nombre, "NitroPlus")
        self.assertEqual(fertilizante.freq_de_aplicacion, 30)
        self.assertEqual(fertilizante.valor, 45000)
        self.assertEqual(fertilizante.fecha_ultima_aplicacion, "2025-10-15")

    def test_producto_control_creacion(self):
        producto = ProductoDeControl("ICA003", "ControlX", 20, 25000)
        self.assertEqual(producto.registro_ica, "ICA003")
        self.assertEqual(producto.nombre, "ControlX")
        self.assertEqual(producto.freq_de_aplicacion, 20)
        self.assertEqual(producto.valor, 25000)

if __name__ == '__main__':
    unittest.main()