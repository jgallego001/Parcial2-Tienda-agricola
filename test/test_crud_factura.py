import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from crud.crud_factura import crear_factura, buscar_factura_por_id
from modelo.Cliente import Cliente
from modelo.Plaguicida import Plaguicida

class TestCrudFactura(unittest.TestCase):
    def test_crear_factura(self):
        cliente = Cliente("Test Cliente", "123456")
        producto = Plaguicida("ICA001", "Test Product", 15, 30000, 20)
        factura = crear_factura("F001", cliente, [producto])
        
        self.assertEqual(factura.id, "F001")
        self.assertEqual(factura.cliente, cliente)
        self.assertEqual(len(factura.articulos), 1)

    def test_buscar_factura_por_id_existente(self):
        cliente = Cliente("Test Cliente", "123456")
        producto = Plaguicida("ICA001", "Test Product", 15, 30000, 20)
        crear_factura("F002", cliente, [producto])
        
        factura = buscar_factura_por_id("F002")
        self.assertEqual(factura.id, "F002")
        self.assertEqual(factura.cliente.nombre, "Test Cliente")

    def test_buscar_factura_por_id_no_existente(self):
        factura = buscar_factura_por_id("F999")
        self.assertIsNone(factura)

if __name__ == '__main__':
    unittest.main()