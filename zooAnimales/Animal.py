import zooAnimales

class Animal():
    totalAnimales = 0
    zona = ""

    # def __init__(self, nombre, edad, habitat, genero):
    #     self.nombre = nombre
    #     self.edad = edad
    #     self.habitat = habitat
    #     self.genero = genero
    #     Animal.totalAnimales += 1

    def __init__(self, nombre = None, edad = 0,habitat = None, genero = None, zona = None):
        self.nombre = nombre
        self.habitat = habitat
        self.genero = genero
        self.zona = zona
        self.edad = edad
        Animal.totalAnimales += 1


    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def totalPorTipo():
        return "Mamiferos : " + str(zooAnimales.mamifero.Mamifero.cantidadAnimales()) + "\n" + \
               "Aves : "  + str(zooAnimales.ave.Ave.cantidadAnimales()) + "\n" + \
               "Reptiles : " + str(zooAnimales.reptil.Reptil.cantidadAnimales()) + "\n" + \
               "Peces : " + str(zooAnimales.pez.Pez.cantidadAnimales()) + "\n" + \
               "Anfibios : " + str(zooAnimales.anfibio.Anfibio.cantidadAnimales())

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

    def toString(self):
        return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero()