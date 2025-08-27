from modelo.lector import Lector
from modelo.libro import Libro


class Prestamo(Lector, Libro): # type: ignore
    def __init__(self, id_prestamo, fecha_prestamo, plazo_devolucion, fecha_entrega, id_lector, id_libro):
        super(Lector).__init__(id_lector)
        super(Libro).__init__(id_libro)
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.plazo_devolucion = plazo_devolucion
        self.fecha_entrega = fecha_entrega