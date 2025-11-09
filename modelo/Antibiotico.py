class Antibiotico:
    def __init__(self, nombre, dosis, tipo_de_animal, valor):
        self.nombre = nombre
        self.dosis = dosis
        self.tipo_de_animal = tipo_de_animal
        self.valor = valor

    def __str__(self):
        return (f"Antibiotico(\n"
                f"Nombre: {self.nombre},\n"
                f"Dosis: {self.dosis},\n"
                f"Tipo de animal: {self.tipo_de_animal}\n"
                f"Precio: ${self.valor})\n")