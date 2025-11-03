from modelo.ProductoDeControl import ProductoDeControl

class Fertilizante(ProductoDeControl):
    def __init__(self, registro_ica, nombre, freq_de_aplicacion, valor, fecha_ultima_aplicacion):
        super().__init__(registro_ica, nombre, freq_de_aplicacion, valor)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion

    def __str__(self):
        return (f"Fertilizante(\n"
                f"Registro ICA: {self.registro_ica},\n"
                f"Nombre: {self.nombre},\n"
                f"Frecuencia de aplicación: {self.freq_de_aplicacion} días,\n"
                f"Valor: ${self.valor},\n"
                f"Fecha de ultima aplicación: {self.fecha_ultima_aplicacion})\n")