from abc import ABC, abstractmethod

# Abstracción
# Clase base
class Articulo(ABC):
    def __init__(self, titulo, autor, precio):
        self._titulo = titulo
        self._autor = autor
        self._precio = precio

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, value):
        self._autor = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value

    @abstractmethod
    def mostrar_detalles(self):
        pass

# Herencia y Polimorfismo
# Clase hija 1
class Libro(Articulo):
    def __init__(self, titulo, autor, precio, genero):
        super().__init__(titulo, autor, precio)
        self.genero = genero

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        self._genero = value

    def mostrar_detalles(self):
        print(f"Título: {self._titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: {self.precio}")
        print(f"Género: {self.genero}")

# Herencia y Polimorfismo
# Clase hija 2
class Periodico(Articulo):
    def __init__(self, titular, autor, precio_editorial, editorial):
        super().__init__(titular, autor, precio_editorial)
        self.editorial = editorial

    @property
    def editorial(self):
        return self._editorial

    @editorial.setter
    def editorial(self, value):
        self._editorial = value

    def mostrar_detalles(self):
        print(f"Título: {self._titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: {self.precio}")
        print(f"Editorial: {self.editorial}")

# Crear los Objetos
libro = Libro("A Game of Thrones", "George R. R. Martin", 15.00, "Fantasia")
periodico = Periodico("El impacto del cambio climático en América Latina", "J. Martínez", 5.00, "El País")

# Mostrar los detalles (Polimorfismo)
libro.mostrar_detalles()
print()
periodico.mostrar_detalles()
