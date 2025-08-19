import os

class Inventario:
    def _init_(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()