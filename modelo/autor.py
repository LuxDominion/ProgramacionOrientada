from modelo.nacionalidad import Nacionalidad as Nac

class autor(Nac):
    def __init__(self, id_autor, nombre_autor, pseudonimo, id_nacionalidad):
        super().__init__(Nac, id_nacionalidad).__init__()
        self.id_autor = id_autor
        self.nombre_autor = nombre_autor
        self.pseudonimo = pseudonimo

