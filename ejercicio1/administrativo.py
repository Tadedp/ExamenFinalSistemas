from persona import Persona

class Administrativo(Persona):
    def __init__(self, nombre, apellido, cargo):
        super().__init__(nombre, apellido)
        self._cargo = cargo
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def cargo(self):
        return self._cargo    
            
    def __repr__(self):
        return f"Cliente: [nombre: {self._nombre}, apellido: {self._apellido}, cargo: {self._cargo}]"