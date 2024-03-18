class Animal(Zona):
    totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        Animal.totalAnimales += 1

    def __init__(self, nombre, habitat, genero, zona, Edad):
        self.nombre = nombre
        self.habitat = habitat
        self.genero = genero
        self.zona = zona
        self.edad = Edad
        Animal.totalAnimales += 1

    def __init__(self):
        self("", None, "", None, 0)

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def totalPorTipo():
        return "Mamiferos: " + str(Mamifero.getLista().size()) + "\n" + \
               "Aves: " + str(Ave.getLista().size()) + "\n" + \
               "Reptiles " + str(Reptil.getLista().size()) + "\n" + \
               "Peces: " + str(Pez.getLista().size()) + "\n" + \
               "Anfibios: " + str(Anfibio.getLista().size())

    def cantidadAnimales(self):
        return 0

    def getHabitat(self):
        return self.habitat

    def getGenero(self):
        return self.genero

    def getEdad(self):
        return self.edad

    def getNombre(self):
        return self.nombre

    def getZona(self):
        return self.zona

    def __str__(self):
        return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero()