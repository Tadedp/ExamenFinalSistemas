from abc import ABC, abstractmethod

class Builder(ABC):
    @property
    @abstractmethod
    def producto(self):
        pass

    @abstractmethod
    def producir_cpu(self):
        pass

    @abstractmethod
    def producir_gpu(self):
        pass

    @abstractmethod
    def producir_ram(self):
        pass

    @abstractmethod
    def producir_almacenamiento(self):
        pass