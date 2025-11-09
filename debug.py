import sys
import os

# Agregar el path correcto - SUBIR un nivel
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from modelo.Cliente import Cliente
from modelo.Plaguicida import Plaguicida
from modelo.Fertilizante import Fertilizante
from modelo.Antibiotico import Antibiotico
from modelo.Factura import Factura

def main():
    plaga = Plaguicida("ICA001", "Plagox", 15, 30000, 20)
    
    cliente1 = Cliente("Juan Esteban", "123456")
    productos = [plaga, Fertilizante("ICA002", "NitroPlus", 30, 45000, "2025-10-15")]
    factura1 = Factura(1, "2025-11-03", cliente1, productos)
    
    cliente1.agregar_factura(factura1)

if __name__ == "__main__":
    main()