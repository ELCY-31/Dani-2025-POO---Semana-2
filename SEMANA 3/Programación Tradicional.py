# Temperaturas en programacion tradicional
# Función para ingresar las temperatura.
def ingresar_temperaturas():
    temperaturas = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for i, dia in enumerate(dias_semana):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal.
def calcular_promedio(temperaturas):
    if not temperaturas:  # Verifica si la lista de temperaturas está vacía
        return 0
    return sum(temperaturas) / len(temperaturas)

# Mostrar el promedio de las temperaturas.
print("Promedio de Temperaturas Semanales")
temperaturas = ingresar_temperaturas()
promedio = calcular_promedio(temperaturas)
print(f"El promedio de temperaturas de esta semana es: {promedio:.2f}°C")

