4# ============================================================
# main.py
# Punto de arranque del sistema de gestión de restaurante.
# Presenta un menú interactivo por consola que permite
# registrar, listar y buscar productos y clientes.
# ============================================================

from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


def mostrar_menu():
    """Imprime las opciones disponibles del sistema."""
    print("\n===== SISTEMA DE RESTAURANTE =====")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("------------------------------")
    print("0. Salir")


# ----------------------------------------------------------
# Opciones de productos
# ----------------------------------------------------------
def registrar_producto(restaurante):
    """Solicita los datos de un producto y lo registra en el sistema."""
    print("\n-- Registrar nuevo producto --")
    try:
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        resp = input("¿Disponible? (s/n): ").strip().lower()
        disponible = resp == "s"

        # El constructor de Producto valida nombre, categoría y precio
        producto = Producto(nombre, categoria, precio, disponible)
        restaurante.registrar_producto(producto)
        print(f"✔ Producto '{producto.nombre}' registrado correctamente.")
    except ValueError as error:
        # Captura tanto errores de conversión (float) como de validación
        print(f"✘ No se pudo registrar el producto: {error}")


def listar_productos(restaurante):
    """Muestra todos los productos registrados en el sistema."""
    print("\n-- Lista de productos --")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for producto in productos:
        producto.mostrar_informacion()


def buscar_producto(restaurante):
    """Busca y muestra un producto según el nombre ingresado."""
    print("\n-- Buscar producto --")
    nombre = input("Nombre del producto a buscar: ")
    producto = restaurante.buscar_producto(nombre)
    if producto:
        producto.mostrar_informacion()
    else:
        print(f"✘ No se encontró ningún producto con el nombre '{nombre}'.")


# ----------------------------------------------------------
# Opciones de clientes
# ----------------------------------------------------------
def registrar_cliente(restaurante):
    """Solicita los datos de un cliente y lo registra en el sistema."""
    print("\n-- Registrar nuevo cliente --")
    try:
        id_cliente = int(input("ID del cliente: "))
        nombre = input("Nombre del cliente: ")
        correo = input("Correo del cliente: ")

        cliente = Cliente(id_cliente=id_cliente, nombre=nombre, correo=correo)
        restaurante.registrar_cliente(cliente)
        print(f"✔ Cliente '{cliente.nombre}' registrado correctamente.")
    except ValueError:
        print("✘ El ID del cliente debe ser un número entero.")


def listar_clientes(restaurante):
    """Muestra todos los clientes registrados en el sistema."""
    print("\n-- Lista de clientes --")
    clientes = restaurante.listar_clientes()
    if not clientes:
        print("No hay clientes registrados.")
        return
    for cliente in clientes:
        print(f"  {cliente}")


def buscar_cliente(restaurante):
    """Busca y muestra un cliente según el ID ingresado."""
    print("\n-- Buscar cliente --")
    try:
        id_cliente = int(input("ID del cliente a buscar: "))
        cliente = restaurante.buscar_cliente(id_cliente)
        if cliente:
            print(f"  {cliente}")
        else:
            print(f"✘ No se encontró ningún cliente con ID {id_cliente}.")
    except ValueError:
        print("✘ El ID debe ser un número entero.")


# ----------------------------------------------------------
# Bucle principal del programa
# ----------------------------------------------------------
def main():
    """Ejecuta el menú interactivo hasta que el usuario decida salir."""
    restaurante = Restaurante()

    # Diccionario que enlaza cada opción del menú con su función
    opciones = {
        "1": registrar_producto,
        "2": listar_productos,
        "3": buscar_producto,
        "4": registrar_cliente,
        "5": listar_clientes,
        "6": buscar_cliente,
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            print("\nSaliendo del sistema. ¡Hasta pronto!")
            break
        elif opcion in opciones:
            opciones[opcion](restaurante)
        else:
            print("✘ Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
