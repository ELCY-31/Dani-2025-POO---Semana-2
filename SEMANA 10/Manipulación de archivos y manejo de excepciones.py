import os
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

    def to_file_format(self):
        """Convierte el producto a formato de texto para guardar en archivo"""
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}\n"

    @classmethod
    def from_file_format(cls, linea):
        """Crea un producto desde una línea de texto del archivo"""
        id, nombre, cantidad, precio = linea.strip().split(',')
        return cls(int(id), nombre, int(cantidad), float(precio))

# clase hija
class Inventario:
    def __init__(self):
        self.productos = {}
        self.archivo = "inventario.txt"
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo al iniciar"""
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as f:
                    for linea in f:
                        if linea.strip():  # Ignorar líneas vacías
                            producto = Producto.from_file_format(linea)
                            self.productos[producto.id] = producto
                print("Inventario cargado exitosamente desde el archivo.")
            else:
                print("ℹNo se encontró archivo de inventario. Se creará uno nuevo.")
                # Crear archivo vacío
                with open(self.archivo, 'w') as f:
                    pass
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al cargar inventario: {e}")
        except Exception as e:
            print(f"Error inesperado al cargar: {e}")

    def guardar_inventario(self):
        """Guarda todos los productos en el archivo"""
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos.values():
                    f.write(producto.to_file_format())
            return True
        except (PermissionError, IOError) as e:
            print(f"Error al guardar inventario: {e}")
            return False
        except Exception as e:
            print(f"Error inesperado al guardar: {e}")
            return False

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("Error: Este producto ya existe en el inventario.")
            return False
        else:
            self.productos[producto.id] = producto
            if self.guardar_inventario():
                print(f"Producto '{producto.nombre}' agregado exitosamente al inventario.")
                return True
            else:
                print("Error al guardar el producto en el archivo.")
                return False

    def eliminar_producto(self, id):
        if id in self.productos:
            nombre = self.productos[id].nombre
            del self.productos[id]
            if self.guardar_inventario():
                print(f"Producto '{nombre}' eliminado exitosamente.")
                return True
            else:
                print("Error al actualizar el archivo después de eliminar.")
                return False
        else:
            print("Error: Este producto no se encuentra.")
            return False

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            cambios = []
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
                cambios.append(f"cantidad: {cantidad}")
            if precio is not None:
                self.productos[id].precio = precio
                cambios.append(f"precio: ${precio}")

            if cambios and self.guardar_inventario():
                print(f"Producto '{self.productos[id].nombre}' actualizado: {', '.join(cambios)}")
                return True
            elif not cambios:
                print("ℹNo se realizaron cambios.")
                return False
            else:
                print("Error al guardar los cambios en el archivo.")
                return False
        else:
            print("Error: Este producto no se encuentra en el inventario.")
            return False

    def buscar_producto(self, nombre):
        encontrados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                encontrados.append(producto)

        if encontrados:
            print(f"\nSe encontraron {len(encontrados)} producto(s):")
            for producto in encontrados:
                print(f"   {producto}")
        else:
            print("No se encontraron productos con ese nombre.")

    def inventario_mostrar(self):
        if not self.productos:
            print("ℹEl inventario está vacío.")
        else:
            print("\nINVENTARIO:")
            print("-" * 40)
            for producto in self.productos.values():
                print(producto)
            print("-" * 40)
            print(f"Total de productos: {len(self.productos)}")

def menu():
    inventario = Inventario()

    while True:
        print("MI INVENTARIO")
        print("=" * 50)
        print("1. Agregar, 2. Eliminar, 3. Actualizar, 4. Buscar, 5. Mostrar, 6. Salir")
        print("-" * 50)

        try:
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "6":
                print("¡Hasta luego!")
                break

            elif opcion == "1":
                print("\n➕ AGREGAR NUEVO PRODUCTO")
                try:
                    id = int(input("ID: "))
                    nombre = input("Nombre: ").strip()
                    cantidad = int(input("Cantidad: "))
                    precio = float(input("Precio: "))

                    if nombre:  # Validar que el nombre no esté vacío
                        inventario.agregar_producto(Producto(id, nombre, cantidad, precio))
                    else:
                        print("El nombre no puede estar vacío.")
                except ValueError:
                    print("Error: Por favor ingrese valores que sean válidos.")

            elif opcion == "2":
                print("\n➖ ELIMINAR PRODUCTO")
                try:
                    id = int(input("ID a eliminar: "))
                    inventario.eliminar_producto(id)
                except ValueError:
                    print("Error: El ID debe ser un número.")

            elif opcion == "3":
                print("\nACTUALIZAR PRODUCTO")
                try:
                    id = int(input("ID a actualizar: "))
                    cantidad = input("Nueva Cantidad : ").strip()
                    precio = input("Nuevo Precio : ").strip()

                    cantidad = int(cantidad) if cantidad else None
                    precio = float(precio) if precio else None

                    if cantidad is not None or precio is not None:
                        inventario.actualizar_producto(id, cantidad, precio)
                    else:
                        print("ℹNo se proporcionaron cambios.")
                except ValueError:
                    print("Error: Por favor ingrese valores válidos.")

            elif opcion == "4":
                print("\nBUSCAR PRODUCTO")
                nombre = input("Nombre a buscar: ").strip()
                if nombre:
                    inventario.buscar_producto(nombre)
                else:
                    print("Por favor ingrese un nombre para buscar.")

            elif opcion == "5":
                inventario.inventario_mostrar()

            else:
                print("Opción no válida. Por favor seleccione 1-6.")

        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido. ¡Hasta luego!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    menu()