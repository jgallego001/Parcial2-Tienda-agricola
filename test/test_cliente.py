import unittest
from modelo.Cliente import Cliente
from modelo.Factura import Factura

class TestCliente(unittest.TestCase):
    def test_agregar_factura(self):
        cliente = Cliente("Juan", "123")
        factura = Factura(1, "2025-11-03", cliente, [])
        cliente.agregar_factura(factura)
        self.assertEqual(len(cliente.historial_pedidos), 1)
        self.assertEqual(cliente.historial_pedidos[0].numero, 1)

if __name__ == '__main__':
    unittest.main()
