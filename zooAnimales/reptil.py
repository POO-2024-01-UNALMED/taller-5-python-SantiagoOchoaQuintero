
from zooAnimales.animal import Animal
class Reptil(Animal):
    reptiles = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", color_escamas="", largo_cola=0):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.color_escamas = color_escamas
        self.largo_cola = largo_cola
        Reptil.reptiles.append(self)

    @staticmethod
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "humedal", genero, "blanco", 1)

    def cantidadReptiles(self):
        return Reptil.serpientes + Reptil.iguanas

    def movimiento(self):
        return "reptar"

    def getColorEscamas(self):
        return self.color_escamas

    def getLargoCola(self):
        return self.largo_cola

    def getHabitat(self):
        return self.habitat

    @staticmethod
    def getLista():
        return Reptil.reptiles
    
    def cantidadAnimales():
        return len(Reptil.reptiles)
