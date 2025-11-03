class ProductoDeControl:
    def __init__(self, registro_ica, nombre, freq_de_aplicacion, valor):
        self.registro_ica = registro_ica
        self.nombre = nombre
        self.freq_de_aplicacion = freq_de_aplicacion
        self.valor = valor

    def __str__(self):
        return (f"ProductoDeControl(\n"
                f"Registro ICA: {self.registro_ica},\n"
                f"Nombre: {self.nombre},\n"
                f"Frecuencia de aplicación: {self.freq_de_aplicacion} días,\n"
                f"Valor: ${self.valor})\n")