# Clase base
class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def hablar(self):  # Metodo sobreescrito en las clases derivadas.
        pass

# Clase derivada
class Perro(Animal):
    def hablar(self):
        return f"{self.get_nombre()} ladra"

    def ladra(self):
        return "¡Guau!"

# Clase derivada
class Caballo(Animal):
    def hablar(self):
        return f"{self.get_nombre()} relincha"

    def relincha(self):
        return "¡hiiiii!"

# Uso de polimorfismo
def animal_habitual_habito(animal):
    print(animal.hablar())

# Creación de instancias y la demostración de funcionalidad
def main():
    perro = Perro("Bam")
    caballo = Caballo("Dante")

    print(perro.get_nombre())
    print(caballo.get_nombre())

    print(perro.ladra())  # Uso del metodo especifico para Perro.
    print(caballo.relincha())  # Uso de metodo especifico para Gato.

    animal_habitual_habito(perro)  # Uso de polimorfismo
    animal_habitual_habito(caballo)  # Uso de polimorfismo

if __name__ == "__main__":
    main()
