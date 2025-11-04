import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelo.Factura import Factura
from modelo.Cliente import Cliente
from modelo.Plaguicida import Plaguicida
from modelo.Fertilizante import Fertilizante
from modelo.Antibiotico import Antibiotico

class TestFactura(unittest.TestCase):
    
    def test_factura_creacion(self):
        cliente = Cliente("Test", "111")
        productos = [Plaguicida("ICA001", "Test", 15, 10000, 10)]
        factura = Factura(1, "2025-11-03", cliente, productos)
        self.assertEqual(factura.numero, 1)
        self.assertEqual(factura.fecha, "2025-11-03")
        self.assertEqual(factura.cliente, cliente)
        self.assertEqual(len(factura.articulos), 1)
        self.assertEqual(factura.valor_total, 10000)
    
    def test_factura_calculo_total(self):
        cliente = Cliente("Test", "111")
        productos = [
            Plaguicida("ICA001", "P1", 15, 10000, 10),
            Fertilizante("ICA002", "F1", 30, 15000, "2025-10-15"),
            Antibiotico("Antibov", "500mg", "Bovinos", 25000)
        ]
        factura = Factura(2, "2025-11-04", cliente, productos)
        self.assertEqual(factura.valor_total, 50000)

if __name__ == '__main__':
    unittest.main()