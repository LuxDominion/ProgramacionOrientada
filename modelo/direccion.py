from modelo.direccion import Direccion as Dir

class Direccion(Dir):
    def __init__(self, id_direccion, nombre_dirrecion, id_comuna, calle, numero, departamento):
        super().__init__(id_comuna).__init__()
        self.id_dirrecion = id_direccion 
        self.calle = calle 
        self.numero = numero
        self.departamento = departamento 