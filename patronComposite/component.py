from abc import ABC, abstractmethod

class Component(ABC):
    @property
    def padre(self):
        return self._padre

    @padre.setter
    def padre(self, padre):
        self._padre = padre

    def agregar(self, componente):
        pass

    def eliminar(self, componente):
        pass

    @abstractmethod
    def operacion(self):
        pass