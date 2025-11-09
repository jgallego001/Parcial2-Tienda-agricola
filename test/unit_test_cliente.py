import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelo.Cliente import Cliente
from modelo.Factura import Factura
from modelo.Plaguicida import Plaguicida

class TestCliente(unittest.TestCase):
    
    def test_cliente_creacion(self):
        cliente = Cliente("Juan Esteban", "123456")
        self.assertEqual(cliente.nombre, "Juan Esteban")
        self.assertEqual(cliente.cedula, "123456")
        self.assertEqual(cliente.historial_pedidos, [])
    
    def test_cliente_agregar_factura(self):
        cliente = Cliente("Test", "111")
        plaga = Plaguicida("ICA001", "Plagox", 15, 30000, 20)
        factura = Factura(1, "2025-11-03", cliente, [plaga])
        
        cliente.agregar_factura(factura)
        
        self.assertEqual(len(cliente.historial_pedidos), 1)
        self.assertEqual(cliente.historial_pedidos[0], factura)

if __name__ == '__main__':
    unittest.main()