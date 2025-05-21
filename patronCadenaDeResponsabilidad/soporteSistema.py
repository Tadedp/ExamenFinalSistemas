from manejadorBase import ManejadorBase

class SoporteSistema(ManejadorBase):
    def manejar(self, solicitud):
        if solicitud == "sistema":
            return f"Soporte sistema: He tratado el problema de {solicitud}."
        else:
            return super().manejar(solicitud)