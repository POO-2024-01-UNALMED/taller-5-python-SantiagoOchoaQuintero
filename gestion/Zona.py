
class Zona:
    def __init__(self, nombre, zoo):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def get_animales(self):
        return self.animales

    def cantidad_animales(self):
        cantidad_animales = len(self.animales)
        return cantidad_animales

    def set_animales(self, animales):
        self.animales = animales

    def agregar_animales(self, animal):
        self.animales.append(animal)

    def get_nombre(self):
        return self.nombre

    def get_zoo(self):
        return self.zoo