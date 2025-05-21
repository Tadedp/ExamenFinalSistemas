from archivo import Archivo
from carpeta import Carpeta

if __name__ == "__main__":
    archivo = Archivo("archivo.txt")
    print("Estructura simple...")
    print(f"RESULTADO: {archivo.operacion()}", end="\n")

    sistema = Carpeta("raíz")

    carpeta1 = Carpeta("archivos")
    carpeta1.agregar(Archivo("archivo1.pdf"))
    carpeta1.agregar(Archivo("archivo2.pdf"))

    carpeta2 = Carpeta("imagenes")
    carpeta2.agregar(Archivo("imagen1.png"))

    sistema.agregar(carpeta1)
    sistema.agregar(carpeta2)

    print("\nEstructura compuesta...")
    print(f"RESULTADO: {sistema.operacion()}", end="\n")