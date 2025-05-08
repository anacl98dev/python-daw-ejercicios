# Creamos una lista vacía llamada 'inventario' donde se guardarán los productos.
# Cada producto será un diccionario con su nombre, precio y cantidad.
inventario = []

# La palabra clave 'def' se usa para definir una función en Python.
# Una función es un bloque de código reutilizable que se ejecuta cuando se llama por su nombre.
def agregar_producto():
    # La función input() muestra un mensaje y espera que el usuario escriba algo. Devuelve un string.
    nombre = input("Introduce el nombre del producto:")

    try:
        # La función float() convierte el texto introducido en un número decimal (float).
        # Si el usuario introduce algo que no se puede convertir (como letras), dará error.
        cantidad = float(input("Introduce la cantidad del producto:"))
        precio = float(input("Introduce el precio del producto:"))

        # El operador <= compara si una variable es menor o igual a un número.
        # El operador or devuelve True si alguna de las dos condiciones se cumple.
        if cantidad <= 0 or precio <= 0:
            print("La cantidad y el precio tienen que ser números positivos")

    # Si ocurre un error en el try (por ejemplo, al convertir a float), se ejecuta el bloque except.
    except ValueError:
        print("El precio y la cantidad tienen que ser numeros")

    # Un diccionario en Python se define con llaves {}.
    # Se compone de pares clave: valor. Aquí usamos strings como claves y variables como valores.
    producto = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }

    # .append() añade un elemento al final de la lista 'inventario'.
    inventario.append(producto)

def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío")
    for id, producto in enumerate(inventario, start=1):
        print(f"{id} - {producto['nombre']}")

def calcular_valor_total():
    if not inventario:
        print("El inventario está vacío")
    total = sum(p['cantidad'] * p['precio'] for p in inventario)
    print(f"El valor total del inventario es {total}")

def mostrar_menu():
    print("1. Añadir producto")
    print("2. Mostrar el inventario")
    print("3. Calcular el valor total")
    print("4. Salir")

# Bucle principal que se ejecuta mientras el usuario no elija la opción de salir.
# La variable 'ejecutando' controla si el programa debe continuar o finalizar.
def main():
    ejecutando = True
    while ejecutando:
        mostrar_menu()
        opcion = input("Elija una opción:")
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            mostrar_inventario()
        elif opcion == '3':
            calcular_valor_total()
        elif opcion == '4':
            print("Saliendo del programa...")
            ejecutando = False
        else:
            print("Opción no válida")

if __name__=="__main__":
    main()




