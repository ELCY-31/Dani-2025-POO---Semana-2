# inventario.py
# My pequeño Inventario
import os
# Clase Producto
class Producto:
    def __init__(self, id_, nombre, cantidad, precio):
        self.id = id_
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos “get” muy sencillos
    def obtener_id(self):
        return self.id

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    # Métodos “set” igual de sencillos
    def establecer_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def establecer_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Para imprimir bonito
    def __str__(self):
        return f"{self.id} | {self.nombre} | {self.cantidad} u. | ${self.precio:.2f}"

# Clase Inventario
class Inventario:
    def __init__(self):
        # Usamos un diccionario: la clave es el ID del producto
        self.productos = {}

    # Añadir producto nuevo
    def agregar_producto(self, producto):
        if producto.obtener_id() in self.productos:
            print("Ya existe un producto con ese ID.")
        else:
            self.productos[producto.obtener_id()] = producto
            print("Producto agregado.")

    # Eliminar por ID
    def eliminar_producto(self, id_):
        if id_ in self.productos:
            del self.productos[id_]
            print("Producto eliminado.")
        else:
            print("ID no encontrado.")

    # Actualizar cantidad o precio
    def actualizar_producto(self, id_, nueva_cantidad=None, nuevo_precio=None):
        if id_ not in self.productos:
            print("ID no encontrado.")
            return
        if nueva_cantidad is not None:
            self.productos[id_].establecer_cantidad(nueva_cantidad)
        if nuevo_precio is not None:
            self.productos[id_].establecer_precio(nuevo_precio)
        print("Producto actualizado.")

    # Buscar y mostrar productos por nombre (parcial, sin distinción mayúsculas)
    def buscar_por_nombre(self, texto):
        encontrados = [p for p in self.productos.values()
                       if texto.lower() in p.obtener_nombre().lower()]
        if encontrados:
            for prod in encontrados:
                print(prod)
        else:
            print("No se encontró ningún producto con ese nombre.")

    # Mostrar todos los productos
    def mostrar_todo(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        for prod in self.productos.values():
            print(prod)

    # 3) Guardar y cargar en archivo
    def guardar_en_archivo(self, nombre_archivo="inventario.txt"):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for prod in self.productos.values():
                linea = f"{prod.id},{prod.nombre},{prod.cantidad},{prod.precio}\n"
                archivo.write(linea)
        print("Datos guardados en disco.")

    def cargar_de_archivo(self, nombre_archivo="inventario.txt"):
        if not os.path.exists(nombre_archivo):
            print("Archivo no encontrado, se iniciará con inventario vacío.")
            return
        self.productos.clear()
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                id_, nombre, cantidad, precio = linea.strip().split(",")
                producto = Producto(int(id_), nombre, int(cantidad), float(precio))
                self.productos[producto.obtener_id()] = producto
        print("Datos cargados desde disco.")

# Un Menú simple para la consola
def mostrar_menu():
    print("\n=== MENÚ INVENTARIO ===")
    print("1) Agregar producto / 2) Eliminar producto, / 3) Actualizar producto, / 4) Buscar producto por nombre, / 5) Mostrar todos los productos, / 6) Guardar y salir")

def main():
    inventario = Inventario()
    inventario.cargar_de_archivo()  # Cargamos al iniciar

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                id_ = int(input("ID: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(Producto(id_, nombre, cantidad, precio))
            except ValueError:
                print("Error: introduce números válidos.")

        elif opcion == "2":
            try:
                id_ = int(input("ID a eliminar: "))
                inventario.eliminar_producto(id_)
            except ValueError:
                print("ID debe ser un número entero.")

        elif opcion == "3":
            try:
                id_ = int(input("ID del producto a actualizar: "))
                cant_str = input("Nueva cantidad (dejar vacío para no cambiar): ")
                prec_str = input("Nuevo precio (dejar vacío para no cambiar): ")
                nueva_cant = int(cant_str) if cant_str else None
                nuevo_prec = float(prec_str) if prec_str else None
                inventario.actualizar_producto(id_, nueva_cant, nuevo_prec)
            except ValueError:
                print("Error en los datos introducidos.")

        elif opcion == "4":
            texto = input("Texto a buscar en el nombre: ")
            inventario.buscar_por_nombre(texto)

        elif opcion == "5":
            inventario.mostrar_todo()

        elif opcion == "6":
            inventario.guardar_en_archivo()
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()