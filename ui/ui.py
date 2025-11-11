from modelo.Antibiotico import Antibiotico
from modelo.Fertilizante import Fertilizante
from modelo.Plaguicida import Plaguicida

from crud.crud_factura import crear_factura, buscar_factura_por_id
from crud.crud_cliente import crear_cliente, buscar_por_cedula, listar_clientes


def mostrar_clientes():
    print("\n=== LISTA DE CLIENTES ===")
    clientes = listar_clientes()

    if not clientes:
        print("No hay clientes registrados.")
        return

    for i, cliente in enumerate(clientes, start=1):
        print(f"{i}. {cliente.nombre} - Cédula: {cliente.cedula}")


def mostrar_facturas_cliente():
    print("\n=== FACTURAS DE UN CLIENTE ===")
    cedula = input("Ingrese la cédula del cliente: ").strip()

    cliente = buscar_por_cedula(cedula)
    if not cliente:
        print("❌ Cliente no encontrado.")
        return

    if not cliente.facturas:
        print(f"El cliente {cliente.nombre} no tiene facturas registradas.")
        return

    print(f"\nFacturas del cliente {cliente.nombre} ({cliente.cedula}):")
    for factura in cliente.facturas:
        print(f"\n🧾 Factura ID: {factura.id}")
        print(f"   Fecha: {factura.fecha}")
        print(f"   Total: ${factura.valor_total}")
        print("   Artículos:")

        if not factura.articulos:
            print("    (Sin artículos)")
        else:
            for articulo in factura.articulos:
                print(f"    - {articulo.nombre} (${articulo.valor})")

def nueva_factura():
    nuevo_id = input("\nIngrese el nuevo ID de factura:")

    if buscar_factura_por_id(nuevo_id):
        print("\n❌ Ya existe este ID")
        return None

    cliente = obtener_o_crear_cliente()
    cliente.agregar_factura(crear_factura(nuevo_id, cliente, ingresar_articulos()))

def obtener_o_crear_cliente():
    cedula = input("Ingrese la cédula del cliente: ").strip()

    cliente = buscar_por_cedula(cedula)

    if not cliente:
        print("\n⚠️ Cliente no encontrado. Procediendo a registrar uno nuevo.")
        nombre = input("Ingrese el nombre del cliente: ").strip()
        cliente = crear_cliente(nombre, cedula)
        print(f"\n✅ Cliente '{cliente.nombre}' con cédula {cliente.cedula} registrado correctamente.")

    return cliente

def ingresar_articulos():
    articulos = []

    print("\nIngrese los productos. Cuando no desee agregar más, escriba 0 en el tipo de producto.\n")

    while True:
        print("\nSeleccione el tipo de producto:")
        print("1 - Antibiótico")
        print("2 - Fertilizante")
        print("3 - Plaguicida")
        print("0 - Salir")
        tipo = input("Opción:  ")

        if tipo == "0":
            print("\nFinalizando la lista de productos...\n")
            break

        if tipo not in ["1", "2", "3"]:
            print("❌ Opción inválida, intente nuevamente.")
            continue

        nombre = input("Nombre del producto:  ")

        try:
            valor = float(input("Valor del producto:  "))
        except ValueError:
            print("❌ Error: debe ingresar un número válido para el valor.")
            continue

        # Crear el tipo de producto correspondiente
        if tipo == "1":
            dosis = input("Dosis (en mg):  ")
            tipo_de_animal = input("Tipo de animal:  ")
            producto = Antibiotico(nombre, dosis, tipo_de_animal, valor)

        elif tipo == "2":
            registro_ica = input("Registro ICA: ")
            freq_de_aplicacion = input("Frecuencia de aplicación (en días):  ")
            fecha_ultima_aplicacion = input("Fecha última aplicación (YYYY-MM-DD):  ")
            producto = Fertilizante(registro_ica, nombre, freq_de_aplicacion, valor, fecha_ultima_aplicacion)

        else:  # tipo == "3"
            registro_ica = input("Registro ICA: ")
            freq_de_aplicacion = input("Frecuencia de aplicación (en días):  ")
            periodo_de_carencia = int(input("Periodo de carencia (en días):  "))
            producto = Plaguicida(registro_ica, nombre, freq_de_aplicacion, valor, periodo_de_carencia)

        articulos.append(producto)
        print(f"✅ '{nombre}' agregado correctamente.")

    return articulos


