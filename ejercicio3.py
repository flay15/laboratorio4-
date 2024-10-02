class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")

    def mostrar_estado(self):
        estado = "disponible" if self.disponible else "prestado"
        print(f"El libro '{self.titulo}' está {estado}.")

# Ejemplo de uso
libro = Libro("Cien años de soledad", "Gabriel García Márquez")
libro.mostrar_estado()  # El libro está disponible.
libro.prestar()
libro.mostrar_estado()  # El libro está prestado.
