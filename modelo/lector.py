from modelo.direccion  import Direccion
from modelo.biblioteca import Biblioteca


class Lector(Direccion, Biblioteca):
    def __init__(self, id_lector, id_direccion, id_biblioteca, rut, digito_verificador, nombre_lector):
        super().__init__(id_biblioteca).__init__()
        super().__init__(id_direccion).__init__()
        self.id_lector = id_lector 
        self.rut = rut
        self.digito_verificador = digito_verificador 
        self.nombre_lector = nombre_lector 