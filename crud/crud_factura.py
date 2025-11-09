from modelo.Factura import Factura

facturas = []

def crear_factura(id, cliente, articulos):
    factura = Factura(id, cliente, articulos)
    facturas.append(factura)
    return factura


def buscar_factura_por_id(id):
    for f in facturas:
        if f.id == id:
            return f
    return None