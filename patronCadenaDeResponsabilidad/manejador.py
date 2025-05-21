from abc import ABC, abstractmethod

class Manejador(ABC):
    @abstractmethod
    def establecer_siguiente(self, manejador):
        pass

    @abstractmethod
    def manejar(self, solicitud):
        pass