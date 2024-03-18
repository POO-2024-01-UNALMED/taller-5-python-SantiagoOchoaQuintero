class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.Zonas = []
        Zoologico.cantidadTotal = 0

    def agregarZonas(self, zona):
        self.Zonas.append(zona)

    def cantidadTotalAnimales(self):
        totalAnimales = 0
        for zonas in self.Zonas:
            totalAnimales += zonas.cantidadAnimales()
        return totalAnimales

    def getZona(self):
        return self.Zonas

    def getNombre(self):
        return self.nombre