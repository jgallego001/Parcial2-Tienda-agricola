from modelo.Cliente import Cliente

clientes = []

def crear_cliente(nombre, cedula):
    cliente = Cliente(nombre, cedula)
    clientes.append(cliente)
    return cliente

def buscar_por_cedula(cedula):
    for cliente in clientes:
        if cliente.cedula == cedula:
            return cliente
    return None

def listar_clientes():
    return clientes