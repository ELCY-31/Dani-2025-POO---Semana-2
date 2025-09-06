# CLASE BASE
# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # tupla (inmutable)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} de {self.info[1]} (Cat..: {self.categoria}, ISBN: {self.isbn})"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.prestados = []  # lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}       # diccionario {ISBN: Libro}
        self.usuarios = set()  # conjunto con IDs de los usuarios
        self.usuarios_data = {}  # guardar informacion de los usuarios

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios:
            self.usuarios.add(usuario.user_id)
            self.usuarios_data[usuario.user_id] = usuario

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            self.usuarios.remove(user_id)
            del self.usuarios_data[user_id]

    def prestar_libro(self, isbn, user_id):
        if isbn in self.libros and user_id in self.usuarios:
            libro = self.libros.pop(isbn)  # quitar de libros disponibles
            self.usuarios_data[user_id].prestados.append(libro)

    def devolver_libro(self, isbn, user_id):
        usuario = self.usuarios_data[user_id]
        for libro in usuario.prestados:
            if libro.isbn == isbn:
                usuario.prestados.remove(libro)
                self.libros[isbn] = libro
                break

    def buscar_libro(self, texto):
        resultados = []
        for libro in self.libros.values():
            if texto.lower() in libro.info[0].lower() or \
               texto.lower() in libro.info[1].lower() or \
               texto.lower() in libro.categoria.lower():
                resultados.append(str(libro))
        return resultados

    def listar_prestados(self, user_id):
        return [str(libro) for libro in self.usuarios_data[user_id].prestados]

# Ejemplo de uso
lib1 = Libro("El Quijote", "Cervantes", "Novela", "001")
lib2 = Libro("Cien Años de Soledad", "García Márquez", "Realismo", "002")

user1 = Usuario("Ana", "U001")

biblio = Biblioteca()
biblio.agregar_libro(lib1)
biblio.agregar_libro(lib2)
biblio.registrar_usuario(user1)

print("Libros encontrados:", biblio.buscar_libro("Soledad"))

biblio.prestar_libro("001", "U001")
print("Libros prestados a Ana:", biblio.listar_prestados("U001"))
