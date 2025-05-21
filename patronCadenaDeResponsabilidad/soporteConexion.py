from manejadorBase import ManejadorBase

class SoporteConexion(ManejadorBase):
    def manejar(self, solicitud):
        if solicitud == "conexion":
            return f"Soporte conexión: He solucionado el problema de {solicitud}."
        else:
            return super().manejar(solicitud)