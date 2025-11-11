import sys
import os

# Agregar el path correcto - SUBIR un nivel
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from modelo.Cliente import Cliente
from modelo.Plaguicida import Plaguicida
from modelo.Fertilizante import Fertilizante
from modelo.Antibiotico import Antibiotico
from modelo.Factura import Factura
from crud.crud_cliente import crear_cliente, buscar_por_cedula
from crud.crud_factura import crear_factura

def main():
    print("=== 🔍 DEBUG EJECUTANDO ===")
    
    # 1. Crear productos
    plaga = Plaguicida("ICA001", "Plagox", 15, 30000, 20)
    fertilizante = Fertilizante("ICA002", "NitroPlus", 30, 45000, "2025-10-15")
    antibiotico = Antibiotico("AntibioMax", "500mg", "Bovinos", 35000)
    
    # 2. Usar CRUD para crear cliente
    cliente = crear_cliente("Juan Esteban", "123456")
    
    # 3. Usar CRUD para crear factura
    productos = [plaga, fertilizante, antibiotico]
    factura = crear_factura("DEBUG-001", cliente, productos)
    
    # 4. Agregar factura al cliente
    cliente.agregar_factura(factura)
    
    # 5. Mostrar información para debug
    print(f"Cliente: {cliente.nombre} - {cliente.cedula}")
   
    print(f"Factura ID: {factura.id} - Total: ${factura.valor_total}")
    print(f"Artículos en factura: {len(factura.articulos)}")
    print(f"Cliente tiene {len(cliente.facturas)} factura(s)")
    
    print("✅ Debug completado - Presiona F5 para ver variables")

if __name__ == "__main__":
    main()