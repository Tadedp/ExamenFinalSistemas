from controladores.controladorProducto import ControladorProducto

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad
        self._controlador = ControladorProducto()
            
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio(self):
        return self._precio
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @property
    def controlador(self):
        return self._controlador
        
    def __repr__(self):
        return f"Prducto: [nombre: {self._nombre}, precio: {self._precio}, cantidad: {self._cantidad}]"