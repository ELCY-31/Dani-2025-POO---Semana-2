# Temperaturas semanales - POO
# Clase Base
class Clima:
    def __init__(self):
        self.__temperaturas = []

    def get_temperaturas(self):
        return self.__temperaturas

    def set_temperaturas(self, temperaturas):
        if all(isinstance(temp, (int, float)) for temp in temperaturas):
            self.__temperaturas = temperaturas

    def ingresar_temperatura(self, temp):
        if isinstance(temp, (int, float)):
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        if len(self.__temperaturas) == 0:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)

# Clase hija
class ClimaSemanal(Clima):
    def ingresar_temperaturas(self):
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        for dia in dias_semana:
            try:
                temp = float(input(f"Ingrese la temperatura del día {dia}: "))
                self.ingresar_temperatura(temp)
            except ValueError as e:
                print(e)

# Calculamos el promedio del clima semanal
    def calcular_promedio_semanal(self):
        return self.calcular_promedio()

# Mostrar temperaturas
print("Promedio de Temperaturas Semanales - POO")
semana = ClimaSemanal()
semana.ingresar_temperaturas()
promedio = semana.calcular_promedio_semanal()
print(f"El promedio de temperaturas de esta semana es: {promedio:.2f}°C")