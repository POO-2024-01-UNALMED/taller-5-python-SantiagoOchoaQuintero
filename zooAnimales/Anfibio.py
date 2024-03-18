from gestion.zona import Zona
from gestion.zoologico import Zoologico 
from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from zooAnimales.animal import Animal
class Anfibio(Animal):
    Anfibio = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, color_piel=None, venenoso=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.color_piel = color_piel
        self.venenoso = venenoso
        Anfibio.append(self)

    @classmethod
    def crear_rana(cls, nombre, edad, genero):
        cls.ranas += 1
        return cls(nombre, edad, "selva", genero, "rojo", True)

    @classmethod
    def crear_salamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return cls(nombre, edad, "selva", genero, "rojo", True)

    def cantidad_anfibios(self):
        return self.ranas + self.salamandras

    def movimiento(self):
        return "saltar"

    def get_color_piel(self):
        return self.color_piel

    def is_venenoso(self):
        return self.venenoso

    def get_habitat(self):
        return self.habitat

    @classmethod
    def get_lista(cls):
        return cls.Anfibio