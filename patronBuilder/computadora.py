class Computadora:
    def __init__(self):
        self.partes = []

    def agregar(self, part):
        self.partes.append(part)

    def listar_partes(self):
        print(f"Partes de la computadora: {', '.join(self.partes)}", end='')