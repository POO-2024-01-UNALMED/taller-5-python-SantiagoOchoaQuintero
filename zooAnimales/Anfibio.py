from zooAnimales.animal import Animal

class Anfibio(Animal):
    Anfibios = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, color_piel=None, venenoso=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.color_piel = color_piel
        self.venenoso = venenoso
        self.Anfibios.append(self)

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        return cls(nombre, edad, "selva", genero, "rojo", True)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return cls(nombre, edad, "selva", genero, "rojo", True)
    @staticmethod
    def cantidadAnfibios(self):
        return len(Anfibio.Anfibio)

    def movimiento(self):
        return "saltar"

    def getColorPiel(self):
        return self.color_piel

    def isVenenoso(self):
        return self.venenoso

    def getHabitat(self):
        return self.habitat

    @classmethod
    def getLista(cls):
        return cls.Anfibio
    
    def cantidadAnimales():
        return len(Anfibio.Anfibios)