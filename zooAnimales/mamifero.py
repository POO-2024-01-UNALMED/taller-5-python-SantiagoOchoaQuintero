from zooAnimales.animal import Animal


class Mamifero(Animal):
    Mamiferos = []
    caballos = 0
    leones = 0

    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, pelaje = False, patas = 0):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.Mamiferos.append(self)
    @staticmethod
    def crearCaballo(nombre, edad, genero):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)

    @staticmethod
    def crearLeon(nombre, edad, genero):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)
    
    def cantidadMamiferos(self):
        return Mamifero.caballos + Mamifero.leones

    def isPelaje(self):
        return self.pelaje

    def getPatas(self):
        return self.patas

    def getGenero(self):
        return self.genero

    def getHabitat(self):
        return self.habitat

    @staticmethod
    def getLista():
        return Mamifero.Mamiferos
    
    def cantidadAnimales():
        return len(Mamifero.Mamiferos)