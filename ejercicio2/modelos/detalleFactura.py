from controladores.controladorDetalleFactura import ControladorDetalleFactura

class DetalleFactura():
    def __init__(self, cantidad, producto):
        self._cantidad = cantidad 
        self._producto = producto
        self._subtotal = producto.precio * cantidad
        self._controlador = ControladorDetalleFactura()
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @property
    def subtotal(self):
        return self._subtotal
    
    @property
    def producto(self):
        return self._producto
    
    @property
    def controlador(self):
        return self._controlador
    
    def __repr__(self):
        return f"Detalle: [producto: {self._producto}, cantidad: {self._cantidad}, producto: {self._subtotal}]"