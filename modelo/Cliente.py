class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.historial_pedidos = []

    def agregar_factura(self, factura):
        self.historial_pedidos.append(factura)
    def __str__(self):
        return (f"Cliente(\n"
                f"Nombre: {self.nombre},\n"
                f"Cedula: {self.cedula})\n")