from director import Director
from concreteComputerBuilder import ConcreteComputerBuilder

if __name__ == "__main__":
    director = Director()
    builder = ConcreteComputerBuilder()
    director.builder = builder

    print("Computadora básica:")
    director.construir_computadora()
    builder.producto.listar_partes()

    print("\nComputadora avanzada:")
    director.construir_computadora_avanzada()
    builder.producto.listar_partes()
    print("")