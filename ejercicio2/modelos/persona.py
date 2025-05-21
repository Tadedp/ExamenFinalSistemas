from abc import ABC
from controladores.controladorPersona import ControladorPersona

class Persona(ABC):
    def __init__(self, nombre, apellido):
        super().__init__()
        self._nombre = nombre
        self._apellido = apellido
        self._controlador = ControladorPersona()
        
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def controlador(self):
        return self._controlador
