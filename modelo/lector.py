from modelo.direccion import Direccion
from modelo.biblioteca import Biblioteca

class Lector(Direccion, Biblioteca): # type: ignore
    def __init__(self, id_lector, rut, digito_verificador, nombre_lector, habilitado, id_direccion, id_biblioteca):
        super().__init__(id_direccion)
        super().__init__(id_biblioteca)
        self.rut = rut
        self.id_lector = id_lector
        self.digito_verificador = digito_verificador
        self.nombre_lector = nombre_lector
        self.habilitado = habilitado