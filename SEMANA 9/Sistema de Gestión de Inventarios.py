# Mi súper mini gestor de inventario
inventario = []

def agregar():
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    inventario.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    print("Producto agregado.\n")

def mostrar():
    for p in inventario:
        print(f"{p['nombre']} - Cantidad: {p['cantidad']} - Precio: ${p['precio']}")

def buscar():
    nombre = input("Buscar nombre: ").lower()
    for p in inventario:
        if nombre in p["nombre"].lower():
            print(f"{p['nombre']} - {p['cantidad']} - ${p['precio']}")

# Menú
while True:
    opcion = input("1 Agregar | 2 Mostrar | 3 Buscar | 4 Salir: ")
    if opcion == "1":
        agregar()
    elif opcion == "2":
        mostrar()
    elif opcion == "3":
        buscar()
    elif opcion == "4":
        break