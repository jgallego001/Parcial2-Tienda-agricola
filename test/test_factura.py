import unittest
from modelo.Factura import Factura
from modelo.Cliente import Cliente
from modelo.Fertilizante import Fertilizante
from modelo.Plaguicida import Plaguicida

class TestFactura(unittest.TestCase):
    def test_calculo_valor_total(self):
        cliente = Cliente("Pedro", "456")
        p1 = Plaguicida("ICA001", "Plagox", 15, 30000, 20)
        f1 = Fertilizante("ICA002", "NitroPlus", 30, 45000, "2025-10-15")
        factura = Factura(1, "2025-11-03", cliente, [p1, f1])
        self.assertEqual(factura.valor_total, 75000)

    def test_factura_vacia(self):
        cliente = Cliente("Pedro", "456")
        factura = Factura(2, "2025-11-03", cliente, [])
        self.assertEqual(factura.valor_total, 0)

if __name__ == '__main__':
    unittest.main()