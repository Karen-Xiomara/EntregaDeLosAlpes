from ordenonline.modulos.ordenes.dominio.eventos import OrdenCreada
from ordenonline.seedwork.aplicacion.handlers import Handler
from ordenonline.modulos.ordenes.infraestructura.despachadores import Despachador

class HandlerOrdenIntegracion(Handler):

    @staticmethod
    def handle_orden_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-orden')

    