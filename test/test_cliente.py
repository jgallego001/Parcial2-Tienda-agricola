import unittest
from modelo.Cliente import Cliente
from modelo.Factura import Factura

class TestCliente(unittest.TestCase):
    def test_agregar_factura(self):
        cliente = Cliente("Juan", "1085")
        factura = Factura(1, cliente, [])
        cliente.agregar_factura(factura)
        self.assertEqual(len(cliente.facturas), 1)
        self.assertEqual(cliente.facturas[0].id, 1)

if __name__ == '__main__':
    unittest.main()
