
🧾 **Sistema de Gestión de Inventario**  


## 📘 **English version**
[Click here to see the README in english version](README.en.md)
---

### 📌 **Descripción del Proyecto**
Este sistema de gestión de inventario permite realizar operaciones básicas de administración de productos en un inventario. Los usuarios pueden agregar productos, consultar su existencia, actualizar precios, eliminar productos y ver el valor total del inventario. El sistema valida las entradas de datos para asegurar que los valores sean correctos y se muestran mensajes informativos usando colores en la terminal.

---

### 🎯 **Funcionalidades**
- **Agregar productos**: Permite al usuario agregar un producto al inventario proporcionando el nombre, precio y cantidad.
- **Consultar productos**: Permite al usuario buscar productos por nombre y obtener su precio y cantidad.
- **Actualizar precios**: Permite al usuario modificar el precio de un producto existente.
- **Eliminar productos**: Permite al usuario eliminar productos del inventario.
- **Valor total del inventario**: Calcula y muestra el valor total del inventario basado en el precio y cantidad de los productos.
- **Mostrar inventario**: Muestra todos los productos registrados en el inventario.

---

### 🧠 **Lógica Implementada**
El sistema está compuesto por varias funciones y clases:
1. **InventoryService**: Clase principal encargada de gestionar las operaciones sobre el inventario, como agregar, eliminar, actualizar precios y calcular el total.
2. **Utils**: Funciones auxiliares para la validación de entradas de datos, incluyendo nombre del producto, precio y cantidad.
3. **Main**: Función que gestiona la interfaz de usuario, mostrando un menú y ejecutando las acciones seleccionadas por el usuario.

---

### ✅ **Validaciones Realizadas**
- **Nombre del producto**: Se valida que el nombre del producto no esté vacío ni contenga caracteres numéricos.
- **Precio**: Se valida que el precio sea un número positivo mayor a 0.
- **Cantidad**: Se valida que la cantidad sea un número entero positivo entre 1 y 100,000,000.
- **Menú de opciones**: Se valida que la opción seleccionada en el menú sea una de las opciones válidas (1-7).

---

### 📁 **Estructura del Proyecto**
```
/inventoryService.py          # Contiene la lógica de gestión del inventario
/utils.py                     # Funciones de validación para entradas del usuario
/main.py                      # Interfaz de usuario y lógica principal
```

---

### 🧩 **Descripción de Archivos**
- **inventoryService.py**: Contiene la clase `InventoryService` que maneja las operaciones sobre el inventario, como agregar productos, consultar productos, actualizar precios, eliminar productos y calcular el valor total del inventario.
- **utils.py**: Contiene funciones de validación para asegurar que los datos proporcionados por el usuario sean válidos (nombre, precio y cantidad).
- **main.py**: Contiene la lógica que interactúa con el usuario a través de un menú. Permite ejecutar las operaciones del inventario seleccionando opciones.

---

### 💡 **Justificación Técnica**
El sistema ha sido implementado utilizando una estructura simple y clara, dividida en clases y funciones para una mayor modularidad. Se emplearon colores en la terminal para mejorar la experiencia del usuario al interactuar con el sistema. Las validaciones se implementan para evitar errores comunes y asegurar que los datos ingresados sean correctos.

---

### 🚀 **Posibles Mejoras Futuras**
- **Persistencia de datos**: Actualmente, los datos se pierden cuando se cierra el programa. Sería útil integrar una base de datos o almacenamiento en archivos para conservar el inventario entre ejecuciones.
- **Interfaz gráfica de usuario (GUI)**: Se podría implementar una interfaz gráfica para una experiencia de usuario más intuitiva.
- **Manejo de usuarios y roles**: Se podrían agregar roles de usuario con diferentes permisos, como administrador y usuario estándar.

---

### 💻 **Instrucciones de Ejecución**
1. Clona o descarga el repositorio.
2. Asegúrate de tener Python 3.x instalado en tu sistema.
3. Ejecuta el archivo `main.py` desde la terminal:
   ```bash
   python main.py
   ```
4. Sigue las instrucciones en el menú para interactuar con el sistema de inventario.
