import unittest
from modelo.ProductoDeControl import ProductoDeControl

class TestProductoDeControl(unittest.TestCase):
    def test_creacion_producto(self):
        producto = ProductoDeControl("ICA001", "Fertimax", 30, 50000)
        self.assertEqual(producto.registro_ica, "ICA001")
        self.assertEqual(producto.nombre, "Fertimax")
        self.assertEqual(producto.freq_de_aplicacion, 30)
        self.assertEqual(producto.valor, 50000)

    def test_str(self):
        producto = ProductoDeControl("ICA002", "Plagox", 15, 30000)
        texto = str(producto)
        self.assertIn("ProductoDeControl", texto)
        self.assertIn("ICA002", texto)
        self.assertIn("Plagox", texto)
        self.assertIn("30000", texto)

if __name__ == '__main__':
    unittest.main()
