# 🍽️ Sistema de Gestión de Restaurante
### Programación Orientada a Objetos en Python — Versión con menú interactivo
Autor: Derly Zambrano

---

## 📋 Descripción

Este proyecto implementa una versión mejorada del sistema `restaurante_app` utilizando **Programación Orientada a Objetos (POO)** en Python. El sistema permite **registrar, listar y buscar productos y clientes** mediante un **menú interactivo ejecutado desde consola**.

El proyecto refuerza tres conceptos clave de POO:
- Creación correcta de objetos mediante **constructores**.
- Control de atributos mediante **decoradores** (`@property`, `@setter`, `@dataclass`).
- Organización del código en una **estructura modular por capas**.

---

## 🗂️ Estructura del Proyecto

```
restaurante_app/
│
├── modelos/                  # Clases del dominio del problema
│   ├── __init__.py
│   ├── producto.py           # Clase Producto (__init__, @property, @setter)
│   └── cliente.py            # Clase Cliente (@dataclass)
│
├── servicios/                # Lógica principal del sistema
│   ├── __init__.py
│   └── restaurante.py        # Clase Restaurante (registrar/listar/buscar)
│
└── main.py                   # Punto de arranque con menú interactivo
```

---

## 🧩 Clases Implementadas

### 📦 `Producto` — `modelos/producto.py`

Implementada con **constructor tradicional `__init__`** y control de atributos mediante **`@property`/`@setter`**.

| Atributo | Tipo | Validación aplicada |
|---|---|---|
| `nombre` | `str` | No puede estar vacío |
| `categoria` | `str` | No puede estar vacía |
| `precio` | `float` | Debe ser mayor que cero |
| `disponible` | `bool` | Se convierte automáticamente a booleano |

Cada atributo se accede y modifica exclusivamente mediante sus propiedades (`@property` / `@setter`), lo que garantiza que un `Producto` nunca quede en un estado inválido.

| Método | Descripción |
|---|---|
| `mostrar_informacion()` | Imprime los datos del producto de forma legible |
| `__str__()` | Representación en texto del producto |

---

### 👤 `Cliente` — `modelos/cliente.py`

Implementada con el decorador **`@dataclass`**, que genera automáticamente el constructor, `__repr__` y `__eq__`.

| Atributo | Tipo | Descripción |
|---|---|---|
| `id_cliente` | `int` | Identificador único del cliente |
| `nombre` | `str` | Nombre completo del cliente |
| `correo` | `str` | Correo electrónico de contacto |

| Método | Descripción |
|---|---|
| `__str__()` | Representación en texto del cliente (sobrescribe el `__repr__` de dataclass) |

---

### 🏠 `Restaurante` — `servicios/restaurante.py`

Clase de servicio que administra las listas de productos y clientes registrados en el sistema.

| Método | Descripción |
|---|---|
| `registrar_producto(producto)` | Agrega un `Producto` a la lista interna |
| `listar_productos()` | Devuelve todos los productos registrados |
| `buscar_producto(nombre)` | Busca un producto por nombre |
| `registrar_cliente(cliente)` | Agrega un `Cliente` a la lista interna |
| `listar_clientes()` | Devuelve todos los clientes registrados |
| `buscar_cliente(id_cliente)` | Busca un cliente por su identificador |

---

## ▶️ Cómo Ejecutar el Programa

### Requisitos
- Python 3.7 o superior (por el uso de `@dataclass`)

### Pasos

1. Ubicarse en la carpeta raíz del proyecto (`restaurante_app/`).
2. Ejecutar:

```bash
python main.py
```

3. Interactuar con el menú que aparece en consola.

---

## 🖥️ Menú Interactivo

```
===== SISTEMA DE RESTAURANTE =====
1. Registrar producto
2. Listar productos
3. Buscar producto
------------------------------
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
------------------------------
0. Salir
```

El sistema permanece en ejecución en un bucle `while True` hasta que el usuario selecciona la opción **`0`**.

---

## 🔄 Flujo del Sistema

```
input() del usuario
        ↓
constructor del modelo (Producto / Cliente)
        ↓
creación del objeto (validado por @property/@setter o @dataclass)
        ↓
registro en la clase Restaurante
        ↓
listado o búsqueda del registro
```

---

## 🛡️ Manejo de Errores

El programa **no se rompe ante entradas incorrectas**. Cada opción del menú envuelve la entrada del usuario en bloques `try/except`:

- Si el precio ingresado no es numérico → se captura el error y se informa al usuario.
- Si el nombre o la categoría del producto están vacíos → el `setter` de `Producto` lanza un `ValueError` que se captura y muestra en consola.
- Si el ID del cliente no es un número entero → se captura el error sin detener el programa.
- Si se elige una opción de menú inexistente → se muestra un mensaje y se vuelve a mostrar el menú.

---

## ✅ Conceptos de POO Aplicados

| Concepto | Aplicación en el proyecto |
|---|---|
| **Constructor tradicional `__init__`** | Clase `Producto` |
| **`@property` / `@setter`** | Control de acceso y validación de atributos en `Producto` |
| **`@dataclass`** | Generación automática del constructor en `Cliente` |
| **Encapsulamiento** | Atributos internos (`_nombre`, `_precio`, etc.) protegidos por propiedades |
| **Composición** | `Restaurante` administra listas de `Producto` y `Cliente` |
| **Modularidad** | Separación en paquetes `modelos/` y `servicios/`, comunicados mediante importaciones |
| **Manejo de excepciones** | `try/except` en `main.py` para evitar que entradas inválidas rompan el programa |

---
## Reflexion 
Crear objetos a partir de datos ingresados por el usuario es fundamental porque convierte texto o números sueltos en información estructurada y confiable: el constructor y los setters de una clase como Producto no solo agrupan nombre, categoría y precio en una sola entidad coherente, sino que además validan esos datos antes de aceptarlos, evitando que el sistema termine con objetos inválidos —como un precio negativo o un nombre vacío— y garantizando que el resto del programa pueda confiar en la información con la que trabaja sin tener que revalidarla constantemente.
