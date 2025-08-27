from modelo.nacionalidad import Nacionalidad # as nac     #se le da un apodo a lo que se importa

class Autor(Nacionalidad):       #se le entrega info a la clase ("funcion")
    def __init__(self, id_autor, nombre, seudonimo, id_nacionalidad):
        super().__init__(id_nacionalidad)      #super como "superior" desde donde se envia la info para esta clase
        # ^^^ Herencia
        self.id_autor = id_autor
        self.nombre = nombre
        self.seudonimo = seudonimo
