# Clase Animal
class Animal:
    # Constructor
    def __init__(self, Nombre, Raza, Edad, Fuerza, Inteligencia):
        self.Nombre = Nombre
        self.Raza = Raza
        self.Edad = Edad
        self.Fuerza = Fuerza
        self.Inteligencia = Inteligencia

# Intanciar un objeto

Animal= Animal("Zeus", "Rottweiler", "3 años", "9/10", "65%")
print(Animal.Nombre)
print(Animal.Raza)
print(Animal.Edad)



