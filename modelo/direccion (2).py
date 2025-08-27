from modelo.comuna import Comuna

class Direccion(Comuna):
    def __init__(self, id_direccion, cod_comuna, nombre_comuna, id_comuna):
        super().__init__(id_comuna)
        self.id_direccion = id_direccion
        self.cod_comuna = cod_comuna
        self.nombre_comuna = nombre_comuna
