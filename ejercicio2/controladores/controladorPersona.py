class ControladorPersona():
    def __init__(self):
        self._facturas = []
    
    @property
    def facturas(self):
        return self._facturas
    
    def agregar_factura(self,  factura):
        self._facturas.append(factura)