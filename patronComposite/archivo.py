from component import Component

class Archivo(Component):
    def __init__(self, nombre):
        self.nombre = nombre

    def operacion(self):
        return self.nombre