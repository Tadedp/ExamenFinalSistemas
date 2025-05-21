from component import Component

class Carpeta(Component):
    def __init__(self, nombre):
        self.nombre = nombre
        self._hijos = []

    def agregar(self, componente):
        self._hijos.append(componente)
        componente.padre = self

    def eliminar(self, componente):
        self._hijos.remove(componente)
        componente.padre = None

    def operacion(self):
        resultados = []
        for hijo in self._hijos:
            resultados.append(hijo.operacion())
        return f"{self.nombre}({', '.join(resultados)})"