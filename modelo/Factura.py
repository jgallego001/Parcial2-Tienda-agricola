from datetime import date

class Factura:
    def __init__(self, id, cliente, articulos):
        self.id = id
        self.fecha = date.today()
        self.cliente = cliente
        self.articulos = articulos
        self.valor_total = self.calcular_total()

    def calcular_total(self):
        total = 0
        for articulo in self.articulos:
            total += articulo.valor
        return total

    def __str__(self):
        articulos_str = "\n   ".join(str(a) for a in self.articulos)
        return (f"Factura(\n"
                f"Nro de factura: {self.numero},\n"
                f"Fecha: {self.fecha},\n"
                f"Cliente: {self.cliente}\n"
                f"Articulos: {articulos_str}\n"
                f"Valor total: ${self.valor_total})")