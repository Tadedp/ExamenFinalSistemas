from soporteContrasena import SoporteContrasena
from soporteConexion import SoporteConexion
from soporteSistema import SoporteSistema

if __name__ == "__main__":
    contrasena = SoporteContrasena()
    conexion = SoporteConexion()
    sistema = SoporteSistema()

    contrasena.establecer_siguiente(conexion).establecer_siguiente(sistema)

    manejador = contrasena
    print("Resolviendo solicitudes...")
    for solicitud in ["contraseña", "conexion", "sistema"]:
        print(f"Cliente: Tengo un problema con {solicitud}.")
        resultado = manejador.manejar(solicitud)
        if resultado:
            print(f"  {resultado}", end="\n")
        else:
            print(f"  Nadie pudo manejar el problema de {solicitud}.", end="\n")
