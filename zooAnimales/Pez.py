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

    def crear_salmon(self, nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)

    def crear_bacalao(self, nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)

    def get_color_escamas(self):
        return self.color_escamas

    def get_cantidad_aletas(self):
        return self.cantidad_aletas

    def cantidad_peces(self):
        return Pez.salmones + Pez.bacalaos

    def movimiento(self):
        return "nadar"

    def get_genero(self):
        return self.genero

    def get_habitat(self):
        return self.habitat

    @staticmethod
    def get_lista():
        return Pez.peces