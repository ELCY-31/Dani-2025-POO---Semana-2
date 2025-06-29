# Ejemplo de área de un rombo

class Rombo:
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def calcular_area_rombo(self):
        return (self.diagonal1 * self.diagonal2) / 2

# Calculamos el perimetro del rombo, con la formula de 4 veces la mitad de la suma de las diagonales.
    def calcular_perimetro_rombo(self):
        return 4 * ((self.diagonal1*2 + self.diagonal2*2) / 4)*0.5

# Uso
diagonal1 = 10  # La longitud de la primera diagonal
diagonal2 = 8   # La longitud de la segunda diagonal

# Crear el objeto
mi_rombo = Rombo(diagonal1, diagonal2)
area_del_rombo = mi_rombo.calcular_area_rombo()
perimetro_del_rombo = mi_rombo.calcular_perimetro_rombo()

print(f"El área de un rombo es : {area_del_rombo}")
print(f"El perímetro de un rombo es : {perimetro_del_rombo}")
