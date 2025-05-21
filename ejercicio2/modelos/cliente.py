from .persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, estadoIVA):
        super().__init__(nombre, apellido)
        self._estadoIVA = estadoIVA
    
    @property
    def estadoIVA(self):
        return self._estadoIVA
    
    def __repr__(self):
        return f"Cliente: [nombre: {self._nombre}, apellido: {self._apellido}, estadoIVA: {self._estadoIVA}]" 