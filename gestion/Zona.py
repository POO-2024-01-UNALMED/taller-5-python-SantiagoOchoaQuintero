class Zona():
    def __init__(self, nombre, zoo = None):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def getAnimales(self):
        return self.animales

    def cantidadAnimales(self):
        cantidad_animales = len(self.animales)
        return cantidad_animales

    def setAnimales(self, animales):
        self.animales = animales

    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def getNombre(self):
        return self.nombre

    def getZoo(self):
        return self.zoo