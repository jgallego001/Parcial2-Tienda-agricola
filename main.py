from ui.ui import nueva_factura, mostrar_clientes, mostrar_facturas_cliente

def menu():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1 - Crear nueva factura")
        print("2 - Mostrar lista de clientes")
        print("3 - Mostrar facturas de un cliente")
        print("0 - Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nueva_factura()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            mostrar_facturas_cliente()
        elif opcion == "0":
            print("\n👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    menu()