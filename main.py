from modelo.Cliente import Cliente
from modelo.Plaguicida import Plaguicida
from modelo.Fertilizante import Fertilizante
from modelo.Antibiotico import Antibiotico
from modelo.Factura import Factura

# Crear cliente
cliente1 = Cliente("Juan Esteban", "123456")

# Crear productos
plaga = Plaguicida("ICA001", "Plagox", 15, 30000, 20)
fertilizante = Fertilizante("ICA002", "NitroPlus", 30, 45000, "2025-10-15")
antibiotico = Antibiotico("Antibov", "500mg", "Bovinos", 60000)

# Crear factura con los productos
factura1 = Factura(1,"2025-11-03", cliente1, [plaga, fertilizante, antibiotico])

# Asociar la factura al cliente
cliente1.agregar_factura(factura1)

# Mostrar resultado
print(factura1)
