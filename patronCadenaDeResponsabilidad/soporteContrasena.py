from manejadorBase import ManejadorBase

class SoporteContrasena(ManejadorBase):
    def manejar(self, solicitud):
        if solicitud == "contraseña":
            return f"Soporte contraseña: He resuelto el problema de {solicitud}."
        else:
            return super().manejar(solicitud)