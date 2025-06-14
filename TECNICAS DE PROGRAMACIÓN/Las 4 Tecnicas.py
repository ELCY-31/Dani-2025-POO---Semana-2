# Técnicas de la POO
from abc import ABC, abstractmethod

# Abstracción
# Clase base
class Articulo(ABC):
    def __init__(self, __titulo, __autor, __precio):
        self.__titulo = __titulo
        self.__autor = __autor
        self.__precio = __precio

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, value):
        self.__titulo = value

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, value):
        self.__autor = value

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, value):
        self.__precio = value

    @abstractmethod
    def mostrar_detalles(self):
        pass

# Herencia y Polimorfismo
# Clase hija 1
class Libro(Articulo):
    def __init__(self, __titulo, __autor, __precio, __genero):
        super().__init__(__titulo, __autor, __precio)
        self.__genero = __genero

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, value):
        self.__genero = value

    def mostrar_detalles(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: {self.precio}")
        print(f"Género: {self.genero}")

# Clase hija 2
class Periodico(Articulo):
    def __init__(self, __titular, __autor, __precio, __editorial):
        super().__init__(__titular, __autor, __precio)
        self.__editorial = __editorial

    @property
    def editorial(self):
        return self.__editorial

    def mostrar_detalles(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: {self.precio}")
        print(f"Editorial: {self.editorial}")

# Crear los Objetos
libro = Libro("A Game of Thrones", "George R. R. Martin", 15.00, "Fantasia")
periodico = Periodico("El impacto del cambio climático en América Latina", "J. Martinez", 5.00, "El País")

# Mostrar los detalles (Polimorfismo)
libro.mostrar_detalles()
print()
periodico.mostrar_detalles()
