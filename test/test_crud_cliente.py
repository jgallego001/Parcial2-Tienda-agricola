import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from crud.crud_cliente import crear_cliente, buscar_por_cedula, listar_clientes

class TestCrudCliente(unittest.TestCase):
    def test_crear_cliente(self):
        cliente = crear_cliente("Juan Perez", "123456")
        self.assertEqual(cliente.nombre, "Juan Perez")
        self.assertEqual(cliente.cedula, "123456")

    def test_buscar_por_cedula_existente(self):
        crear_cliente("Maria Garcia", "789012")
        cliente = buscar_por_cedula("789012")
        self.assertEqual(cliente.nombre, "Maria Garcia")
        self.assertEqual(cliente.cedula, "789012")

    def test_buscar_por_cedula_no_existente(self):
        cliente = buscar_por_cedula("999999")
        self.assertIsNone(cliente)

    def test_listar_clientes(self):
        # Limpiar lista para test limpio
        from crud.crud_cliente import clientes
        clientes.clear()
        
        crear_cliente("Carlos Lopez", "111111")
        crear_cliente("Ana Martinez", "222222")
        
        lista = listar_clientes()
        self.assertEqual(len(lista), 2)
        self.assertEqual(lista[0].cedula, "111111")
        self.assertEqual(lista[1].cedula, "222222")

if __name__ == '__main__':
    unittest.main()