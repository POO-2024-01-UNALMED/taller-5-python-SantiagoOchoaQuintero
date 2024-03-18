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
    def crear_halcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return cls(nombre, edad, "montanas", genero, "cafe glorioso")

    @classmethod
    def crear_aguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return cls(nombre, edad, "montanas", genero, "blanco y amarillo")

    def cantidad_aves(self):
        return self.halcones + self.aguilas

    def movimiento(self):
        return "volar"

    def get_color_plumas(self):
        return self.color_plumas

    def get_genero(self):
        return self.genero

    def get_habitat(self):
        return self.habitat

    @classmethod
    def get_lista(cls):
        return cls.aves