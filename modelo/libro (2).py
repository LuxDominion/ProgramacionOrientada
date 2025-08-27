from modelo.categoria import Categoria
from modelo.autor import Autor
from modelo.biblioteca import Biblioteca

class Libro(Categoria, Autor, Biblioteca):
    def __init__(self, id_libro, titulo, paginas, copias, habilitado, id_categoria, id_autor, id_biblioteca):
        super().__init__(id_categoria)
        super().__init__(id_autor)
        super().__init__(id_biblioteca)
        self.id_libro = id_libro
        self.titulo = titulo
        self.paginas = paginas
        self.copias = copias
        self.habilitado = habilitado
