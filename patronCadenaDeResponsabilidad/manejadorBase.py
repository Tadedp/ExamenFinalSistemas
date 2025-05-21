from manejador import Manejador

class ManejadorBase(Manejador):
    _siguiente_manejador = None

    def establecer_siguiente(self, manejador):
        self._siguiente_manejador = manejador
        return manejador

    def manejar(self, solicitud):
        if self._siguiente_manejador:
            return self._siguiente_manejador.manejar(solicitud)
        return None