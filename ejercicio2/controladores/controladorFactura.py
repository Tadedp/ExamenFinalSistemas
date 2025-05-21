class ControladorFactura():
    def __init__(self):
        self._detalles = []
    
    @property
    def detalles(self):
        return self._detalles
    
    def agregar_detalle(self, detalle):
        self._detalles.append(detalle)