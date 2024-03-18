from gestion.zona import Zona
from gestion.zoologico import Zoologico 
from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
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
    def crear_iguana(nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @staticmethod
    def crear_serpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "humedal", genero, "blanco", 1)

    def cantidad_reptiles(self):
        return Reptil.serpientes + Reptil.iguanas

    def movimiento(self):
        return "reptar"

    def get_color_escamas(self):
        return self.color_escamas

    def get_largo_cola(self):
        return self.largo_cola

    def get_habitat(self):
        return self.habitat

    @staticmethod
    def get_lista():
        return Reptil.reptiles