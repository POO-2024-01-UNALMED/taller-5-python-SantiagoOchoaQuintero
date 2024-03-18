
from zooAnimales.animal import Animal
class Pez(Animal):
    peces = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, color_escamas, cantidad_aletas):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.color_escamas = color_escamas
        self.habitat = habitat
        self.cantidad_aletas = cantidad_aletas

        Pez.peces.append(self)

    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)

    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)

    def getColorEscamas(self):
        return self.color_escamas

    def getCantidadAletas(self):
        return self.cantidad_aletas

    def cantidadPeces(self):
        return Pez.salmones + Pez.bacalaos

    def movimiento(self):
        return "nadar"

    def getGenero(self):
        return self.genero

    def getHabitat(self):
        return self.habitat

    @staticmethod
    def getLista():
        return Pez.peces
    def cantidadAnimales():
        return len(Pez.peces)