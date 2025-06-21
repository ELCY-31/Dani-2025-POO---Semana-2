# Clase base
class Disfraz:
    """Representa un traje de disfraz en el inventario de alquiler."""

    def __init__(self, id_disfraz, tipo):
        """Inicializa un nuevo traje de disfraz con un ID y tipo."""
        self.id_disfraz = id_disfraz
        self.tipo = tipo
        self.esta_alquilado = False

    def alquilar(self):
        """Alquila el disfraz si no está actualmente alquilado."""
        if not self.esta_alquilado:
            self.esta_alquilado = True
            return True
        return False

    def devolver(self):
        """Devuelve el disfraz al inventario."""
        self.esta_alquilado = False

    def __str__(self):
        """Devuelve una representación en cadena del disfraz."""
        return f"ID: {self.id_disfraz}, Tipo: {self.tipo}, Estado: {'Alquilado' if self.esta_alquilado else 'Disponible'}"

# Clase hija
class Cliente:
    """Representa a un cliente en el sistema de alquiler de disfraz."""

    def __init__(self, nombre):
        """Inicializa un nuevo cliente con un nombre."""
        self.nombre = nombre
        self.disfraces_alquilados = []

    def alquilar_disfraz(self, disfraz):
        """Alquila un disfraz si está disponible."""
        if disfraz.alquilar():
            self.disfraces_alquilados.append(disfraz)
            print(f"{self.nombre} ha alquilado el disfraz {disfraz.tipo} con ID {disfraz.id_disfraz}")
        else:
            print(f"El disfraz {disfraz.tipo} con ID {disfraz.id_disfraz} ya está alquilado.")

    def devolver_disfraz(self, id_disfraz):
        """Devuelve un disfraz."""
        for disfraz in self.disfraces_alquilados:
            if disfraz.id_disfraz == id_disfraz:
                disfraz.devolver()
                self.disfraces_alquilados.remove(disfraz)
                print(f"{self.nombre} ha devuelto el disfraz {disfraz.tipo} con ID {disfraz.id_disfraz}")
                return
        print(f"{self.nombre} no tiene el disfraz con ID {id_disfraz}")

    def ver_disfraces_alquilados(self):
        """Muestra todos los disfraces alquilados por el cliente."""
        if not self.disfraces_alquilados:
            print(f"{self.nombre} no tiene disfraces alquilados.")
        for disfraz in self.disfraces_alquilados:
            print(disfraz)

# Ejemplo de uso
disfraz1 = Disfraz(101, "Zombie")
disfraz2 = Disfraz(102, "Vampiro")
cliente = Cliente("Jonathan")

cliente.alquilar_disfraz(disfraz1)
cliente.alquilar_disfraz(disfraz2)
cliente.ver_disfraces_alquilados()
cliente.devolver_disfraz(101)
cliente.ver_disfraces_alquilados()