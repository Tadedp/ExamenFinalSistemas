from controladores.controladorFactura import ControladorFactura

class Factura():
    def __init__(self, fecha, tipo, total, administrativo, cliente):
        self._fecha = fecha
        self._tipo = tipo
        self._total = total
        self._administativo = administrativo
        self._cliente = cliente
        self._controlador = ControladorFactura()
        
    @property
    def fecha(self):
        return self._fecha
    
    @property
    def tipo(self):
        return self._tipo
    
    @property
    def total(self):
        return self._total
    
    @property
    def administrativo(self):
        return self._administativo
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def controlador(self):
        return self._controlador
        
    def __repr__(self):
        return f"Factura: [fecha: {self._fecha}, tipo: {self._tipo}, total: {self._total}, administrativo: {self._administativo}, cliente: {self._cliente}, detalles: {self.controlador.detalles}]"