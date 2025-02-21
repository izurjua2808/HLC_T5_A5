class Libro:
    def _init_(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def _str_(self):
        return f"'{self.titulo}' por {self.autor}"

class Biblioteca:
    def _init_(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro agregado: {libro}")

    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("Libros en la biblioteca:")
            for libro in self.libros:
                print(libro)

biblioteca = Biblioteca()
libro1 = Libro("Crimen y castigo", "Fiódor Dostoyevski")
libro2 = Libro("El nombre del viento", "Patrick Rothfuss")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.mostrar_libros()