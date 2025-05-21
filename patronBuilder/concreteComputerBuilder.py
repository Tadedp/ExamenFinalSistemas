from builder import Builder
from computadora import Computadora

class ConcreteComputerBuilder(Builder):
    def __init__(self):
        self.reset_producto()

    def reset_producto(self):
        self._producto = Computadora()

    @property
    def producto(self):
        producto = self._producto
        self.reset_producto()
        return producto

    def producir_cpu(self):
        self._producto.agregar("Intel i9")

    def producir_gpu(self):
        self._producto.agregar("NVIDIA RTX 4090")

    def producir_ram(self):
        self._producto.agregar("32GB DDR5")

    def producir_almacenamiento(self):
        self._producto.agregar("2TB NVMe SSD")