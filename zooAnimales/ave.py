from zooAnimales.animal import Animal
class Ave(Animal):
    aves = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, color_plumas):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.color_plumas = color_plumas
        self.aves.append(self)

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return cls(nombre, edad, "montanas", genero, "cafe glorioso")

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return cls(nombre, edad, "montanas", genero, "blanco y amarillo")

    def cantidad_aves(self):
        return self.halcones + self.aguilas

    def movimiento(self):
        return "volar"

    def getColorPlumas(self):
        return self.color_plumas

    def getGenero(self):
        return self.genero

    def getHabitat(self):
        return self.habitat

    @classmethod
    def getLista(cls):
        return cls.aves

    def cantidadAnimales():
        return len(Ave.aves)
