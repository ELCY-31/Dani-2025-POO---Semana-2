# Implementación de Constructores y Destructores en Python
# class base
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        print(f"Libro '{self.titulo}' de {self.autor} INICIALIZADO.")

    def __del__(self):
        print(f"Libro '{self.titulo}' de {self.autor} DESTRUIDO.")

# Uso de los Constructores y de los Destructores
mi_libro = Libro("Alas de Sangre", "Rebecca Yarros")
del mi_libro
