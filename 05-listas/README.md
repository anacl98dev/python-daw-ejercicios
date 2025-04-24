# 🧺 [InventarioProductos.py](./InventarioProductos.py)

Ejercicio práctico para gestionar un inventario de productos utilizando listas, diccionarios y funciones en Python. Se trabaja con entrada de datos, validación, estructuras condicionales y un menú interactivo.

---

## 🧠 ¿Qué hace este programa?

🔹 Permite añadir productos (nombre, cantidad, precio).  
🔹 Muestra el inventario con todos los productos registrados.  
🔹 Calcula el valor total del inventario.  
🔹 Usa funciones y estructuras condicionales para organizar la lógica.  
🔹 Incluye un menú que se repite hasta que el usuario decide salir.

---

## 🎯 Objetivo didáctico

Este ejercicio sirve para practicar:

- 📝 **Listas** (`append`, `for`, validación)
- 🧱 **Diccionarios** para representar objetos
- ⚙️ **Funciones definidas por el usuario**
- 🔁 **Estructuras condicionales y bucles** (`if`, `while`)
- 💬 **Entrada y salida de datos por consola**

---

## Pseudocódigo
Crear una lista vacía llamada inventario

Mientras el usuario no elija salir:
    Mostrar el menú con opciones:
        1. Añadir producto
        2. Mostrar el inventario
        3. Calcular el valor total
        4. Salir

    Leer la opción del usuario

    Si la opción es 1:
        Pedir nombre, cantidad y precio del producto
        Validar que la cantidad y el precio sean mayores que 0
        Si los datos son válidos:
            Crear un diccionario con el producto
            Añadirlo a la lista inventario

    Si la opción es 2:
        Si el inventario está vacío:
            Mostrar mensaje
        Si no:
            Mostrar todos los productos con su nombre y cantidad

    Si la opción es 3:
        Si el inventario está vacío:
            Mostrar mensaje
        Si no:
            Calcular y mostrar el valor total (cantidad × precio)

    Si la opción es 4:
        Mostrar mensaje de despedida y salir del bucle

    Si la opción no es válida:
        Mostrar mensaje de error

---

## 💻 Entorno de desarrollo

- Lenguaje: **Python 3.x**  
- IDE: **[PyCharm](https://www.jetbrains.com/pycharm/)**
