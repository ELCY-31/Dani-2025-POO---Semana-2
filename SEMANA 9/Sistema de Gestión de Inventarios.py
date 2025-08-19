# Mi mini super e inventario
# class base
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    def __str__(self):
        return f"{self.id} | {self.nombre} | {self.cantidad} | ${self.precio}"

# clase hija
class Inventario:
    def __init__(self):
        self.productos = {}
    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("Error: Este producto ya existe en el inventario.")
        else:
            self.productos[producto.id] = producto
    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Error: Este producto no se encuentra.")
    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
        else:
            print("Error: Este producto no se encuentra.")
    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)
    def inventario_mostrar(self):
        for producto in self.productos.values():
            print(producto)

def menu():
    inventario = Inventario()
    while True:
        print("\n1. Agregar, 2. Eliminar, 3. Actualizar, 4. Buscar, 5. Mostrar, 6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "6":
            break
        elif opcion == "1":
            id = int(input("Id: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id, nombre, cantidad, precio))
        elif opcion == "2":
            inventario.eliminar_producto(int(input("ID a eliminar: ")))
        elif opcion == "3":
            id = int(input("ID a actualizar: "))
            cantidad = input("Nueva Cantidad: ")
            precio = input("Nuevo Precio: ")
            inventario.actualizar_producto(id, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == "4":
            inventario.buscar_producto(input("Nombre a buscar: "))
        elif opcion == "5":
            inventario.inventario_mostrar()

if __name__ == "__main__":
    menu()