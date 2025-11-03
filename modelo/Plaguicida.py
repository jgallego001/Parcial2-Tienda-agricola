from modelo.ProductoDeControl import ProductoDeControl

class Plaguicida(ProductoDeControl):
    def __init__(self, registro_ica, nombre, freq_de_aplicacion, valor, periodo_de_carencia):
        super().__init__(registro_ica, nombre, freq_de_aplicacion, valor)
        self.periodo_de_carencia = periodo_de_carencia

    def __str__(self):
        return (f"Plaguicida(\n"
                f"Registro ICA: {self.registro_ica},\n"
                f"Nombre: {self.nombre},\n"
                f"Frecuencia de aplicación: {self.freq_de_aplicacion} días,\n"
                f"Valor: ${self.valor},\n"
                f"Periodo de carencia: {self.periodo_de_carencia} días)\n")