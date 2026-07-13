# ============================================================
# servicios/restaurante.py
# Clase Restaurante — administra las listas de productos y
# clientes registrados: agregar, listar y buscar.
# ============================================================

# Importación de los modelos desde la carpeta modelos/
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Clase de servicio que administra productos y clientes del restaurante."""

    def __init__(self):
        # Listas internas donde se almacenan los objetos registrados
        self._productos = []
        self._clientes = []

    # --------------------------------------------------------
    # Gestión de productos
    # --------------------------------------------------------
    def registrar_producto(self, producto: Producto):
        """Agrega un objeto Producto a la lista de productos."""
        self._productos.append(producto)

    def listar_productos(self):
        """Devuelve la lista completa de productos registrados."""
        return self._productos

    def buscar_producto(self, nombre):
        """Busca un producto por nombre (sin distinguir mayúsculas/minúsculas)."""
        for producto in self._productos:
            if producto.nombre.lower() == nombre.strip().lower():
                return producto
        return None

    # --------------------------------------------------------
    # Gestión de clientes
    # --------------------------------------------------------
    def registrar_cliente(self, cliente: Cliente):
        """Agrega un objeto Cliente a la lista de clientes."""
        self._clientes.append(cliente)

    def listar_clientes(self):
        """Devuelve la lista completa de clientes registrados."""
        return self._clientes

    def buscar_cliente(self, id_cliente):
        """Busca un cliente por su identificador único."""
        for cliente in self._clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None
