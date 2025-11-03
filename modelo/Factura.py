from datetime import date

class Factura:
    def __init__(self, numero, fecha, cliente, articulos):
        self.numero = numero
        self.cliente = cliente
        self.fecha = fecha if fecha else date.today()
        self.articulos = articulos
        self.valor_total = self.calcular_valor_total()

    def calcular_valor_total(self):
        total = 0
        for articulo in self.articulos:
            # Todos los productos tienen un atributo valor o precio
            if hasattr(articulo, 'valor'):
                total += articulo.valor
            elif hasattr(articulo, 'precio'):
                total += articulo.precio
        return total
    def __str__(self):
        articulos_str = "\n   ".join(str(a) for a in self.articulos)
        return (f"Factura(\n"
                f"Nro de factura: {self.numero},\n"
                f"Fecha: {self.fecha},\n"
                f"Cliente: {self.cliente}\n"
                f"Articulos: {articulos_str}\n"
                f"Valor total: ${self.valor_total})")