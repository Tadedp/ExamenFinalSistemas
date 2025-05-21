class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def construir_computadora(self):
        self.builder.producir_cpu()
        self.builder.producir_ram()

    def construir_computadora_avanzada(self):
        self.builder.producir_cpu()
        self.builder.producir_gpu()
        self.builder.producir_ram()
        self.builder.producir_almacenamiento()