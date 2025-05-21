class DetalleFactura():
    def __init__(self, cantidad, producto):
        self._cantidad = cantidad 
        self._producto = producto
        self._subtotal = producto.precio * cantidad
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @property
    def subtotal(self):
        return self._subtotal
    
    @property
    def producto(self):
        return self._producto
    
    def __repr__(self):
        return f"Detalle: [producto: {self._producto}, cantidad: {self._cantidad}, producto: {self._subtotal}]"